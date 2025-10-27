---
title: Safer cold storage on Ethereum
url: https://blog.trailofbits.com/2025/09/05/safer-cold-storage-on-ethereum/
source: The Trail of Bits Blog
date: 2025-09-06
fetch_date: 2025-10-02T19:44:40.620266
---

# Safer cold storage on Ethereum

[The Trail of Bits Blog](/ "The Trail of Bits Blog")

[![Trail of Bits Logo](/img/tob.png)](https://trailofbits.com "Trail of Bits")

# Safer cold storage on Ethereum

Trail of Bits

September 05, 2025

[blockchain](/categories/blockchain/), [ethereum](/categories/ethereum/), [cold-storage](/categories/cold-storage/)

Page content

* [**The fatal flaw in traditional cold storage**](#the-fatal-flaw-in-traditional-cold-storage)
* [**A better way: Self-protecting smart contract wallets**](#a-better-way-self-protecting-smart-contract-wallets)
* [**Implementing defense in depth**](#implementing-defense-in-depth)
  + [**1. Role-separated multisignature architecture**](#1-role-separated-multisignature-architecture)
  + [**2. Timelocked operations with active monitoring**](#2-timelocked-operations-with-active-monitoring)
  + [**3. Progressive rate limiting**](#3-progressive-rate-limiting)
* [**Emergency response mechanisms**](#emergency-response-mechanisms)
* [**Security analysis: Attack scenarios**](#security-analysis-attack-scenarios)
* [**Getting started**](#getting-started)
* [**Secure your cold storage**](#secure-your-cold-storage)

Your exchange’s cold storage is only as secure as its weakest assumption. While the industry has relied on Bitcoin-era, unprogrammable cold storage solutions for over a decade, these approaches fundamentally underestimate Ethereum’s capabilities. By using smart contract programmability, exchanges can build custody solutions that remain secure even when multisig keys are compromised.

[At EthCC[8]](https://www.youtube.com/live/4SwmYyXDr4w), our Director of Engineering for Blockchain, Benjamin Samuels, makes the case for greater use of smart contracts when cold-storing funds on Ethereum that moves beyond the limitations of traditional key management.

## **The fatal flaw in traditional cold storage**

Traditional cold storage operates on a dangerous premise: if you control the keys, you control the funds. This creates catastrophic single points of failure:

* **Simple multisig**: Compromise M-of-N keys → drain everything
* **Blind-signing risks**: The signers accidentally sign a malicious transaction → total loss
* **Supply chain risks**: The multisig provider’s front end is compromised → game over

Even sophisticated multisignature setups suffer from the same fundamental weakness: they’re all-or-nothing security models. Once an attacker obtains the threshold of keys, no amount of operational security can prevent total fund loss.

## **A better way: Self-protecting smart contract wallets**

Ethereum enables a fundamentally different approach. Instead of relying solely on key security, we can program wallets to enforce security policies at the protocol level. The core design principle should be constrained functionality: instead of using generic wallet contracts, use purpose-built contracts that perform only specific, predefined actions. Here’s an example:

```
// DON'T: Generic execution allows arbitrary actions. Many multisig solutions have functions like this in their contracts. Don't store funds there.
function execute(address target, bytes calldata data) external onlyMultiSig {
    (bool success,) = target.call(data);
    require(success, "Execution failed");
}

// DO: Constrained functions with built-in security policies
function transferToHotWallet(
    address hotWallet,
    address token,
    uint256 amount
) external
    onlyOpsMultisig
    onlyWhitelistedReceivers(hotWallet)
    rateLimited(token, amount)
    afterTimelock
{
    IERC20(token).safeTransfer(hotWallet, amount);
    ...
}
```

Figure 1: An example of a non-ideal multi-sig execution function along with one that applies a series of security policies

By preventing wallet contracts from blindly executing whatever the multisig requests, we can apply security controls and policies to the multisig’s actions, improving the system’s defense-in-depth and overall security posture.

## **Implementing defense in depth**

To protect your cold storage infrastructure, it’s important to have multiple layers of security controls, also known as defense in depth. We discuss several of these strategies in greater detail in [Maturing your smart contracts beyond private key risk](https://blog.trailofbits.com/2025/06/25/maturing-your-smart-contracts-beyond-private-key-risk/).

### **1. Role-separated multisignature architecture**

Implement two distinct multisigs with strictly separated privileges:

**Configuration multisig**

* Highly secure, rarely accessed keys (potentially geographically distributed)
* Can modify only wallet policies (allowlist, limits, timelocks)
* Cannot directly move funds
* Requires higher threshold (e.g., 4-of-7)

**Operations multisig**

* Can only execute transfer functions for pre-approved addresses
* Cannot modify security policies
* Lower threshold for operational efficiency (e.g., 2-of-3)

This separation ensures that even complete compromise of one of the two multisigs cannot bypass security policies.

### **2. Timelocked operations with active monitoring**

All critical actions should enforce mandatory delays. Here is a model for these timelocked operations. This provides a critical window for incident response teams to detect and prevent malicious transactions.

![Flowchart showing how timelocks and role separation create defense in depth for smart contracts](/img/cold_storage_figure_1.png)

Figure 2: Timelocks and role separation create defense in depth for smart contracts

This corresponds to [maturity level 3](https://blog.trailofbits.com/2025/06/25/maturing-your-smart-contracts-beyond-private-key-risk/#level-3-enhanced-controls---timelocks-and-role-separation) in the [aforementioned blog post](https://blog.trailofbits.com/2025/06/25/maturing-your-smart-contracts-beyond-private-key-risk/).

### **3. Progressive rate limiting**

Implement rate limits that are right-sized for your exchange’s risk tolerance, ability to reimburse funds, and expected utilization frequency for transferring funds out of cold storage.

One good example of a rate limiter used in practice is [Chainlink’s CCIP `RateLimiter.sol`](https://github.com/smartcontractkit/ccip/blob/171f9f0cf249765116e3131b61f5b4157566f25f/contracts/src/v0.8/ccip/libraries/RateLimiter.sol). This bucket-based rate limiter slowly fills a “bucket” for each token at a specified rate until the bucket is full. When capacity is consumed, it is deducted from the bucket’s balance. This approach allows effective rate limiting and the ability to consume large amounts of capacity (up to the bucket limit) in quick bursts.

## **Emergency response mechanisms**

You’ll want to make sure that your exchange has an emergency response plan and monitoring infrastructure that can detect and enable your team to respond to incidents involving cold wallet infrastructure. In a normal multi-signature setup, once the malicious transaction is executed on-chain, there is no opportunity for an incident response team to minimize damage.

Cold storage wallets should use time-lock mechanisms that can be used by monitoring infrastructure to reconcile on-chain activity with expected cold wallet activity, and trigger an incident response if a discrepancy is detected.

Using a time-lock also enables incident response teams to cancel malicious transactions before they are executed, completely mitigating any loss.

## **Security analysis: Attack scenarios**

Let’s say your system is attacked: an attacker compromises one or both of the multisigs, or they discover and exploit a bug in your smart contracts. Here’s what the damage would look like for a traditional multisig compared to a well-designed, policy-enforcing wallet.

| Attack scenario | Damage for a traditional multisig | Damage to policy-enforcing wallet |
| --- | --- | --- |
| Ops multisig compromised | Total fund loss | Limited to daily rate limits and allowlisted addresses. Potentially no impact if the malicious transaction is cancelled by the timelock guardian. |
| Co...