---
title: Implement EIP-7730 today
url: https://blog.trailofbits.com/2025/08/27/implement-eip-7730-today/
source: The Trail of Bits Blog
date: 2025-08-28
fetch_date: 2025-10-07T00:47:50.788778
---

# Implement EIP-7730 today

[The Trail of Bits Blog](/ "The Trail of Bits Blog")

[![Trail of Bits Logo](/img/tob.png)](https://trailofbits.com "Trail of Bits")

# Implement EIP-7730 today

Coriolan Pinhas

August 27, 2025

[blockchain](/categories/blockchain/), [vulnerabilities](/categories/vulnerabilities/)

Page content

* [Why blind signing creates an impossible security burden](#why-blind-signing-creates-an-impossible-security-burden)
* [The problem of blind signatures](#the-problem-of-blind-signatures)
* [A step forward with EIP-712, but not enough](#a-step-forward-with-eip-712-but-not-enough)
* [Hardware wallets provide an incomplete solution](#hardware-wallets-provide-an-incomplete-solution)
* [The path forward with EIP-7730 and beyond](#the-path-forward-with-eip-7730-and-beyond)
* [EIP-7730 in practice](#eip-7730-in-practice)
* [Implement EIP-7730 today](#implement-eip-7730-today)

The recent $1.5 billion Bybit hack has exposed a critical vulnerability in the Web3 ecosystem that the community has largely overlooked for years. While Bybit’s compromised supply chain and failure to verify signatures on a separate device were the immediate causes, this incident highlights broader security challenges affecting all wallet users, not just major exchanges.

As industry professionals, we must ask, do typical users have enough information to safely validate their transactions? The uncomfortable truth is no. The current expectation that users should cross-check signatures across multiple devices is unrealistic for mainstream adoption. Few, if any, users routinely verify calldata using multiple verification methods before signing transactions. We previously explored these wallet UX limitations in our [custodial stablecoin rekt test](https://blog.trailofbits.com/2025/05/29/the-custodial-stablecoin-rekt-test/#1-do-you-use-multiple-independent-controls-to-verify-transaction-contents-before-signingcross), where we highlighted how unrealistic current verification expectations are for typical users.

In this post, we’ll demonstrate how dapp developers can help protect their users from blind signing issues using EIP-7730, which enables hardware wallets to decode transactions and allows users to understand what they are really signing.

We believe that dapps that support EIP-7730 will have a huge edge over their competitors. As the number of high-profile hacks involving blind signing increases, users will demand improved security assurances from the dapps they choose to interact with.

## Why blind signing creates an impossible security burden

Consider the security steps users need to follow for each transaction:

1. Verify the transaction’s calldata matches the intended action on their primary workstation
2. Confirm that the transaction hash on their workstation matches the one on their hardware wallet
3. Cross-check on a separate workstation that the transaction hash and its decoded calldata correspond to their intended action

While theoretically secure, this multi-device verification process creates insurmountable friction for average users, requiring several minutes to rigorously cross-check each transaction across multiple devices. Security cannot come at the expense of usability if we expect dapps to achieve mainstream adoption.

## The problem of blind signatures

The core issue lies in blind signatures: asking users to sign data they cannot meaningfully interpret. This happens because wallets lack the protocol-specific knowledge needed to decode transaction data into human-readable formats. Each DeFi protocol has its own unique smart contract interfaces and parameter structures, but wallets cannot understand what these technical parameters actually mean without explicit instructions for interpretation. Would you sign a legal contract without reading its contents? Yet in Web3, users regularly sign cryptographic hashes that appear as unintelligible strings:

```
0x3b812a5cf28be8e4787e1d1d4d513744966d8684da2f9a61187a79607c1b9fca
```

Users resort to this because they often have no alternative when interacting with certain protocols. Most wallet implementations offer raw signing as a supposedly better option, where you sign non-decoded format information. For example:

```
0x0000000000000000000000008c1ed7e19abaa9f23c476da86dc1577f1ef401f50000000000000000000000007a250d5630b4cf539739df2c5dacb4c659f2488dffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000063ae3c1f
```

However, to make informed signing decisions, users need to understand critical transaction details: the exact amount of funds being transferred, swapped, or deposited, the destination addresses, the type of operation being performed, any associated risks like slippage tolerance or delegation permissions, etc. Without these details, the user is essentially trusting their workstation to send a non-malicious transaction to their hardware wallet, creating a dangerous dependency on potentially compromised systems.

This brings us back to our original blind signature problem: users signing data representations they cannot verify or understand.

## A step forward with EIP-712, but not enough

EIP-712 was originally introduced specifically to address the blind signing problem by providing a standardized way for applications to present structured, human-readable data to users before signing. This standard works by defining a structured data format that wallets can interpret and display, allowing users to see organized fields like token amounts, recipient addresses, and operation types instead of raw cryptographic data. The protocol achieves this by requiring applications to provide both the raw transaction data and a structured schema that describes what each piece of data represents, enabling wallets to render meaningful information to users.

This standard allows users to verify individual fields they’re signing, theoretically enabling “clear signing” instead of blind signing.![Figure 1: Metamask signature request without EIP-712 (left) and with EIP-712 (right)](/img/eip-7730-1.png)

Figure 1: Metamask signature request without EIP-712 (left) and with EIP-712 (right)

While EIP-712 represents significant progress by standardizing structured data signatures across many protocols, it still falls short in critical ways. The Bybit hack clearly demonstrates these limitations. Despite supporting EIP-712, the transaction data remained too complex for human verification. In the compromised transactions, some parameters of the signature input were changed, most crucially the operation type from 0 (normal call) to 1 (delegate call), along with the destination address.

[Here](https://etherscan.io/tx/0x46deef0f52e3a983b67abf4714448a41dd7ffd6d32d32da69d62081c68ad7882) is the compromised information they signed:![Figure 2: Compromised transaction signed for the Bybit hack on Etherscan](/img/eip-7730-2.png)

Figure 2: Compromised transaction signed for the Bybit hack on Etherscan

This subtle difference in operation type completely changed the transaction’s behavior, allowing the attacker to execute malicious code in the context of the Safe contract. These technical details would be nearly impossible for most users to detect when confronted with hex-encoded values that provide no human-readable context.

What signers likely saw in their wallets was slightly different representations of the EIP-712 data structure. While some hardware wallets like Trezor Model T do support EIP-712 and can display the structured message, the standard doesn’t address the challenge of rendering nested operations in a human-readable format. The wallet would need specialized knowledge that the “data” parameter represents a calldata operation requiring further decoding.

Even when compared side-by-side in interfaces like MetaMask, the original and tampered transactions would appear similar enough that users could easily mistake one f...