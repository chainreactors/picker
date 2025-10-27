---
title: A mistake in the bulletproofs paper could have led to the theft of millions of dollars
url: https://blog.trailofbits.com/2023/08/02/a-mistake-in-the-bulletproofs-paper-could-have-led-to-the-theft-of-millions-of-dollars/
source: Trail of Bits Blog
date: 2023-08-03
fetch_date: 2025-10-04T12:01:18.316660
---

# A mistake in the bulletproofs paper could have led to the theft of millions of dollars

[The Trail of Bits Blog](/ "The Trail of Bits Blog")

[![Trail of Bits Logo](/img/tob.png)](https://trailofbits.com "Trail of Bits")

# A mistake in the bulletproofs paper could have led to the theft of millions of dollars

Jim Miller

August 02, 2023

[cryptography](/categories/cryptography/), [blockchain](/categories/blockchain/)

We discovered a critical vulnerability in [Incognito Chain](https://incognito.org/) that would allow an attacker to mint arbitrary tokens and drain user funds. Incognito offers confidential transactions through zero-knowledge proofs, so an attacker could have stolen millions of dollars of shielded funds without ever being detected or identified. The vulnerability stemmed from an insecure implementation of the Fiat-Shamir transformation of Incognito’s bulletproofs.

This is not the first instance of this vulnerability; last year we disclosed a series of these same types of issues, which we dubbed [Frozen Heart vulnerabilities](https://blog.trailofbits.com/2022/04/15/the-frozen-heart-vulnerability-in-bulletproofs/). These vulnerabilities, as we detailed in our earlier blog series, resulted from a mistake in the original bulletproofs paper. The mistake was in the paper for over four years before it was corrected last year in response to our disclosure.

Since posting that blog series, Trail of Bits has continued research with Paul Grubbs (University of Michigan) and Quang Dao (Carnegie Mellon University) to review more codebases and proof systems for this issue, resulting in a paper [recently accepted for publication at IEEE S&P 2023](https://eprint.iacr.org/2023/691). The vulnerability in Incognito Chain was identified during this research.

After discovering the issue, we informed multiple members of the Incognito Chain team, who patched the vulnerability and released a new version of their privacy protocol. This new version has since been adopted by their validators, effectively patching the vulnerability and, to our knowledge, securing all funds.

## Understanding bulletproofs, Fiat-Shamir, Frozen Heart, and confidential transactions

**Bulletproofs** are a special kind of zero-knowledge proof, also known as a range proof. They permit a prover to validate that an encrypted value lies within a specific range. These proofs serve as a crucial foundation for confidential transactions.

**Fiat-Shamir** is a transformation we detailed in a series of previous blog posts. These posts delve into how it can be incorrectly implemented and exploited across several zero-knowledge proof systems.

**Frozen Heart** vulnerabilities break the security of zero-knowledge proofs. When exploited, an attacker can forge zero-knowledge proofs, tricking the verifier into accepting incorrect proofs. This compromise can have severe implications for the protocol’s security.

**Confidential transactions** are a significant feature of Incognito Chain. Similar to Monero, these transactions hide the amount being transferred and the identities of both the sender and receiver.

For a more detailed examination of the Incognito Chain protocol and the cryptographic primitives it contains, you can [check out their forum](https://we.incognito.org/t/sending-cryptocurrencies-confidentially-ring-signature-homomorphic-commitment-and-zero-knowledge-range-proofs/170). A brief explanation is that coins are the encryption of their underlying value (technically, a commitment scheme instead of an encryption scheme). The identities of the sender and receiver are concealed by using a ring signature, which proves the transaction came from a group (or ring) of keys, one of which is controlled by the sender. To hide the receiver’s identity, the protocol relies on stealth or one-time addresses; the sender in the transaction generates one-time public keys that only the receiver can access.

A transaction includes a set of input coins, output coins, and a transaction fee. For a transaction to be valid, the sum of the inputs should equal the sum of the outputs plus the transaction fee. However, the values of the coins are encrypted. This challenge is overcome through the protocol’s reliance on homomorphic encryption, which allows the values of inputs and outputs to be added and subtracted while remaining encrypted. This balance check can be performed homomorphically, allowing the verified transaction to validate that the sums are equal without knowing their actual values.

There is a caveat to this balance check. Homomorphic encryption schemes ensure sums are equal modulo some value, typically a 256-bit or larger prime value (the group order). An adept attacker could manipulate this fact to execute an attack that functions essentially as an integer overflow, where the overflow occurs modulo the large prime. Consequently, instead of the transaction not generating additional funds (as a secure protocol requires), an attacker could mint extra funds—a substantial amount equivalent to a 256-bit prime number.

The protocol designers anticipated this issue, employing bulletproofs as a safeguard. Bulletproofs, as range proofs, confirm that all input and output values are less than a specific maximum. Thus, if the group order is a 256-bit prime, we can avert this overflow attack by using bulletproofs that validate that the values of each coin are at most 264. An overflow attack would then be unattainable when using a reasonable number of inputs and outputs.

## Vulnerability details

Bulletproofs are an essential part of confidential transactions. They limit the underlying value of the privacy coins, thus safeguarding the system from attackers minting money illicitly. Like most zero-knowledge proofs, bulletproofs use the Fiat-Shamir transformation to be noninteractive. Our prior blog post highlights how an error in the original bulletproofs paper led to insecure implementations of the Fiat-Shamir protocol. If this mistake is implemented as instructed, an attacker can forge bulletproofs for values outside the range.

The original bulletproofs forgery results in a coin that has a uniformly random value. Although this could complicate exploitation since you can’t control the value exactly, it’s not entirely impossible. As we elaborate in the Attacking Mimblewimble section of our [recently published paper](https://eprint.iacr.org/2023/691), [Wagner’s k-sum algorithm](https://www.iacr.org/archive/crypto2002/24420288/24420288.pdf) could be employed to engineer such an exploit.

However, Incognito Chain uses a variant of bulletproofs known as aggregate bulletproofs. As the name suggests, this variant aggregates multiple bulletproofs into a single proof, allowing more efficient verification. When this variant of bulletproofs is vulnerable to Frozen Heart, the severity escalates notably because it grants an attacker the liberty to select arbitrary values for the coins instead of being confined to random values. With this level of control over these values, an attacker can effortlessly solve the balance equation, thereby generating free money. What amplifies the concern surrounding this vulnerability is its target: confidential transactions, which inherently hide most information from external observers, make practical detection of exploitation a formidable challenge.

## Coordinated disclosure

We notified multiple members of the Incognito Chain team of this vulnerability on April 25, 2023. They responded swiftly, confirmed the issue, and started working on a fix. On April 26, 2023, Incognito Chain submitted [this patch](https://github.com/incognitochain/incognito-chain/commit/1bd65414b630f42aa515689643221011fb4702c5) and other commits that fixed the bulletproofs implementation.

The Incognito Chain team released this patch as part of a new version (v3) of their privacy protocol to prevent future exploits. However, this initial patch inadvertently introduced a bug that caused a temporary network outage. The team detailed this issue [on their forum](https://we.incognito.org/t/resolved-recent-net...