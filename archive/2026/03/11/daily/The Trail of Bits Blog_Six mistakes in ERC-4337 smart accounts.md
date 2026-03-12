---
title: Six mistakes in ERC-4337 smart accounts
url: https://blog.trailofbits.com/2026/03/11/six-mistakes-in-erc-4337-smart-accounts/
source: The Trail of Bits Blog
date: 2026-03-11
fetch_date: 2026-03-12T04:07:07.682652
---

# Six mistakes in ERC-4337 smart accounts

[The Trail of Bits Blog

Blog](/ "The Trail of Bits Blog")

[![Trail of Bits Logo](/img/tob.png)](https://trailofbits.com "Trail of Bits")

# Six mistakes in ERC-4337 smart accounts

[Coriolan Pinhas](/authors/coriolan-pinhas/)

March 11, 2026

[blockchain](/categories/blockchain/), [ethereum](/categories/ethereum/), [vulnerabilities](/categories/vulnerabilities/)

Page content

* [How ERC-4337 works](#how-erc-4337-works)
* [1. Incorrect access control](#1-incorrect-access-control)
* [2. Incomplete signature validation (specifically the gas fields)](#2-incomplete-signature-validation-specifically-the-gas-fields)
* [3. State modification during validation](#3-state-modification-during-validation)
* [4. ERC‑1271 replay signature attack](#4-erc1271-replay-signature-attack)
* [5. Reverts don’t save you in ERC‑4337](#5-reverts-dont-save-you-in-erc4337)
* [6. Old ERC‑4337 accounts vs ERC‑7702](#6-old-erc4337-accounts-vs-erc7702)
* [Quick security checks before you ship](#quick-security-checks-before-you-ship)

Account abstraction transforms fixed “private key can do anything” models into programmable systems that enable batching, recovery and spending limits, and flexible gas payment. But that programmability introduces risks: a single bug can be as catastrophic as leaking a private key.

After auditing dozens of ERC‑4337 smart accounts, we’ve identified six vulnerability patterns that frequently appear. By the end of this post, you’ll be able to spot these issues and understand how to prevent them.

## How ERC-4337 works

Before we jump into the common vulnerabilities that we often encounter when auditing smart accounts, here’s the quick mental model of how ERC-4337 works. There are two kinds of accounts on Ethereum: externally owned accounts (EOAs) and contract accounts.

* **EOAs** are simple key-authorized accounts that can’t run custom logic. For example, common flows like token interactions require two steps (approve/permit, then execute), which fragments transactions and confuses users.
* **Contract accounts** are smart contracts that can enforce rules, but cannot initiate transactions on their own.

Before account abstraction, if you wanted wallet logic like spending limits, multi-sig, or recovery, you’d deploy a smart contract wallet like Safe. The problem was that an EOA still had to kick off every transaction and pay gas in ETH, so in practice, you were juggling two accounts: one to sign and one to hold funds.

ERC-4337 removes that dependency. The smart account itself becomes the primary account. A shared `EntryPoint` contract and off-chain bundlers replace the EOA’s role, and paymasters let you sponsor gas or pay in tokens instead of ETH.

Here’s how ERC-4337 works:

* Step 1: The user constructs and signs a `UserOperation` off-chain. This includes the intended action (`callData`), a nonce, gas parameters, an optional paymaster address, and the user’s signature over the entire message.
* Step 2: The signed `UserOperation` is sent to a bundler (think of it as a specialized relayer). The bundler simulates it locally to check it won’t fail, then batches it with other operations and submits the bundle on-chain to the `EntryPoint` via `handleOps`.
* Step 3: The `EntryPoint` contract calls `validateUserOp` on the smart account, which verifies the signature is valid and that the account can cover the gas cost. If a paymaster is involved, the `EntryPoint` also validates that the paymaster agrees to sponsor the fees.
* Step 4: Once validation passes, the `EntryPoint` calls back into the smart account to execute the actual operation. The following figure shows the `EntryPoint` flow diagram from [ERC-4337](https://eips.ethereum.org/EIPS/eip-4337):

![Figure 1: EntryPoint flow diagram from ERC-4337](/2026/03/11/six-mistakes-in-erc-4337-smart-accounts/erc4337-figure-1_hu_28689ebdbcaa7f49.webp)

Figure 1: EntryPoint flow diagram from ERC-4337

If you’re not already familiar with ERC-4337 or want to dig into the details we’re glossing over here, it’s worth reading through [the full EIP](https://eips.ethereum.org/EIPS/eip-4337). The rest of this post assumes you’re comfortable with the basics.

Now that we’ve covered the ERC-4337 attack surface, let’s explore the common vulnerability patterns we encounter in our audits.

## 1. Incorrect access control

If anyone can call your account’s `execute` function (or anything that moves funds) directly, they can do anything with your wallet. Only the `EntryPoint` contract should be allowed to trigger privileged paths, or a vetted executor module in ERC-7579.

A vulnerable implementation allows anyone to drain the wallet:

```
function execute(address target, uint256 value, bytes calldata data) external {
    (bool ok,) = target.call{value: value}(data);
    require(ok, "exec failed");
}
```

Figure 2: Vulnerable execute function

While in a safe implementation, the `execute` function is callable only by `entryPoint`:

```
address public immutable entryPoint;

function execute(address target, uint256 value, bytes calldata data)
    external
{
    require(msg.sender == entryPoint, "not entryPoint");
    (bool ok,) = target.call{value: value}(data);
    require(ok, "exec failed");
}
```

Figure 3: Safe execute function

Here are some important considerations for access control:

* For each `external` or `public` function, ensure that the proper access controls are set.
* In addition to the `EntryPoint` access control, some functions need to restrict access to the account itself. This is because you may frequently want to call functions on your contract to perform administrative tasks like module installation/uninstallation, validator modifications, and upgrades.

## 2. Incomplete signature validation (specifically the gas fields)

A common and serious vulnerability arises when a smart account verifies only the intended action (for example, the `callData`) but omits the gas-related fields:

* `preVerificationGas`
* `verificationGasLimit`
* `callGasLimit`
* `maxFeePerGas`
* `maxPriorityFeePerGas`

All of these values are part of the payload and must be signed and checked by the validator. Since the `EntryPoint` contract computes and settles fees using these parameters, any field that is not cryptographically bound to the signature and not sanity-checked can be altered by a bundler or a frontrunner in transit.

By inflating these values (for example, `preVerificationGas`, which directly reimburses calldata/overhead), an attacker can cause the account to overpay and drain ETH. `preVerificationGas` is the portion meant to compensate the bundler for work outside `validateUserOp`, primarily calldata size costs and fixed inclusion overhead.

We use `preVerificationGas` as the example because it’s the easiest lever to extract ETH: if it isn’t signed or strictly validated/capped, someone can simply bump that single number and get paid more, directly draining the account.

Robust implementations must bind the full `UserOperation`, including all gas fields, into the signature, and so enforce conservative caps and consistency checks during validation.

Here’s an example of an unsafe `validateUserOp` function:

```
function validateUserOp(UserOperation calldata op, bytes32 /*hash*/, uint256 /*missingFunds*/)
    external
    returns (uint256 validationData)
{
    // Only checks that the calldata is “approved”
    require(_isApprovedCall(op.callData, op.signature), "bad sig");
    return 0;
}
```

Figure 4: Unsafe validateUserOp function

And here’s an example of a safe `validateUserOp` function:

```
function validateUserOp(UserOperation calldata op, bytes32 userOpHash, uint256 /*missingFunds*/)
    external
    returns (uint256 validationData)
{
    require(_isApprovedCall(userOpHash, op.signature), "bad sig");
    return 0;
}
```

Figure 5: Safe validateUserOp function

Here are some additional considerations:

* Ideally, use the [`userOpHash`](https://eips.ethereum.org/EIPS/eip-4337#smart-contract-account-interface) sent by the `...