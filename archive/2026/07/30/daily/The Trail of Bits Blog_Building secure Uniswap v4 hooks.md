---
title: Building secure Uniswap v4 hooks
url: https://blog.trailofbits.com/2026/07/30/building-secure-uniswap-v4-hooks/
source: The Trail of Bits Blog
date: 2026-07-30
fetch_date: 2026-07-31T05:30:05.578240
---

# Building secure Uniswap v4 hooks

[The Trail of Bits Blog

Blog](/ "The Trail of Bits Blog")

[![Trail of Bits Logo](/img/tob.png)](https://trailofbits.com "Trail of Bits")

# Building secure Uniswap v4 hooks

[Nicolas Donboly](/authors/nicolas-donboly/)

July 30, 2026

[blockchain](/categories/blockchain/), [audits](/categories/audits/), [vulnerabilities](/categories/vulnerabilities/)

Page content

* [What the PoolManager guarantees](#what-the-poolmanager-guarantees)
* [1. Anyone can call your hook](#1-anyone-can-call-your-hook)
* [2. Treating any pool as legitimate](#2-treating-any-pool-as-legitimate)
* [3. Custom accounting leaks value](#3-custom-accounting-leaks-value)
* [4. Right logic, wrong hook](#4-right-logic-wrong-hook)
* [5. Address bits are part of the API](#5-address-bits-are-part-of-the-api)
* [6. Hook failures can block pool actions](#6-hook-failures-can-block-pool-actions)
* [7. State can change during a callback sequence](#7-state-can-change-during-a-callback-sequence)
* [Building secure hooks](#building-secure-hooks)
* [Auditing v4 hooks](#auditing-v4-hooks)
* [Security responsibilities for hook developers](#security-responsibilities-for-hook-developers)

Uniswap v4 hooks let developers add custom behavior to pools, including dynamic fees, custom accounting, and external integrations. This flexibility moves some security responsibilities into application and hook code.

The Cork and Bunni exploits are two app-level incidents that show what can go wrong in that code. Together, they account for more than $20M in losses. Neither incident stemmed from a flaw in the Uniswap v4 core protocol or the PoolManager; both arose from application-specific authorization and accounting logic built around hooks.

After analyzing dozens of findings from Trail of Bits audits (including our [Uniswap v4-core security review](https://github.com/trailofbits/publications/blob/master/reviews/2024-07-uniswap-v4-core-securityreview.pdf)), public reports from other firms, and the Solodit database, I’ve identified seven recurring failure patterns in application and hook code, including missing caller checks and accounting bugs that still satisfy the PoolManager’s settlement invariant. Builders can use these patterns as a secure-development checklist; auditors can use them to focus their review.

## What the PoolManager guarantees

If you’re familiar with Uniswap v3, where each pool was a separate contract, v4 inverts the model. All pool state now lives in a singleton PoolManager contract, with each pool represented in its storage. Uniswap v4 adds hooks: independent contracts that execute custom logic at specific points in the swap and liquidity lifecycle.

![“Figure 1: Pools live inside the singleton PoolManager, and multiple pools can use the same hook contract.”](/2026/07/30/building-secure-uniswap-v4-hooks/uniswapv4-figure-1_hu_b3e8804f4c7e53ff.webp)

Figure 1: Pools live inside the singleton PoolManager, and multiple pools can use the same hook contract.

Here’s what a pool looks like in v4:

```
struct PoolKey {
    Currency currency0;
    Currency currency1;
    uint24 fee;
    int24 tickSpacing;
    IHooks hooks;
}
```

Figure 2: A pool's PoolKey includes both currencies, the fee, tick spacing, and the hook address ([v4-core/src/types/PoolKey.sol](https://github.com/Uniswap/v4-core/blob/main/src/types/PoolKey.sol)).

Notice that the hook address (`IHooks hooks;`) is part of the pool’s identity. If you change any of these fields, you’re talking to a different pool. This matters because trusting the wrong `PoolKey` means trusting the wrong pool.

v4 also introduces a session-based model that works like a flash loan. Your contract calls `unlock()` on the PoolManager, which triggers a callback into your code. At the end, the PoolManager checks that no unsettled currency deltas remain:

```
function unlock(bytes calldata data) external returns (bytes memory result) {
    Lock.unlock();
    // ... callback execution happens here ...
    if (NonzeroDeltaCount.read() != 0) revert CurrencyNotSettled();
    Lock.lock();
}
```

Figure 3: Simplified PoolManager.unlock() flow: unlock the session, execute the callback, and revert unless all currency deltas settle to zero ([v4-core/src/PoolManager.sol](https://github.com/Uniswap/v4-core/blob/main/src/PoolManager.sol)).

![“Figure 4: A periphery or hook calls PoolManager.unlock(), handles unlockCallback(), and calls swap() inside the unlocked session.”](/2026/07/30/building-secure-uniswap-v4-hooks/uniswapv4-figure-4_hu_452027c95338c4e1.webp)

Figure 4: A periphery or hook calls PoolManager.unlock(), handles unlockCallback(), and calls swap() inside the unlocked session.

The PoolManager enforces v4’s protocol mechanics, including pool initialization rules, swap and liquidity math, hook-callback sequencing, and end-of-session settlement. Hook developers are responsible for validating the application-specific assumptions their hooks add.

Each hook must decide:

* Who can call its privileged paths
* Which pools are legitimate
* How custom balances and deltas should be accounted for
* Whether external integrations can fail or reenter safely

## 1. Anyone can call your hook

Hook callbacks are external functions on your contract. If you don’t check the caller, an attacker can call those callbacks directly with malicious parameters. A loose `unlockCallback` path can also reach internal actions that should never be callable.

The fix: use `BaseHook` for hook entrypoints and `SafeCallback` for `unlockCallback`. Together, they enforce caller checks on the callback paths they cover:

```
modifier onlyPoolManager() {
    if (msg.sender != address(poolManager))
        revert NotPoolManager();
    _;
}
```

Figure 5: onlyPoolManager restricts hook callbacks to the configured PoolManager.

Add an equivalent caller check only on paths those contracts don’t cover.

**Real-world example:** The [Cork exploit](https://www.cork.tech/blog/post-mortem) (~$12M, May 2025) shows why this check matters. Cork let data from an untrusted path reach hook logic that affected redemptions. That access-control gap, combined with a pricing issue elsewhere in the protocol, gave the attacker a way to drain funds.

## 2. Treating any pool as legitimate

Pool creation through the PoolManager is permissionless by default. Unless your hook restricts initialization in beforeInitialize, anyone can create a pool with your hook address attached. If your hook trusts a user-supplied `PoolKey` without validation, an attacker can route your logic through a malicious pool with currencies and parameters they choose.

An attacker-created pool presents two immediate risks. First, if your hook stores per-pool data keyed by `PoolId`, the new pool gets its own mapping slot. The attacker can influence values written through activity in that pool, and later accounting paths may treat those values as trusted. Second, `currency0` and `currency1` are attacker-chosen currencies. If either is an ERC-20, token interactions can trigger malicious behavior or reenter other hook functions mid-flow.

The fix: bind your hook to canonical pools during deployment or trusted configuration, or maintain a strict allowlist. Re-check the derived `PoolId` on every user-controlled path:

```
// Pseudocode for pool binding
PoolId poolId = key.toId();
if (!allowedPools[poolId]) revert InvalidPool();
```

Figure 6: Derive the PoolId from the supplied PoolKey and reject pools that are not allowlisted.

**Real-world example:** In Semantic Layer’s [SVFHook finding](https://solodit.cyfrin.io/issues/chat-points-manipulation-by-adding-liquidity-to-custom-pools-via-svfhook-contract-spearbit-none-semantic-layer-pdf), the `addLiquidity` function lets callers specify the `PoolKey`. An attacker could route deposits through a custom WETH/SVF pool with a malicious hook and earn points at a lower cost than intended.

## 3. Custom accounting leaks value

In v4, a delta is a signed currency-balance change owed to or from the PoolManager. Once y...