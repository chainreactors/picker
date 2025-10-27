---
title: Our crypto experts answer 10 key questions
url: https://blog.trailofbits.com/2024/07/25/our-crypto-experts-answer-10-key-questions/
source: Trail of Bits Blog
date: 2024-07-26
fetch_date: 2025-10-06T17:42:13.850030
---

# Our crypto experts answer 10 key questions

[The Trail of Bits Blog](/ "The Trail of Bits Blog")

[![Trail of Bits Logo](/img/tob.png)](https://trailofbits.com "Trail of Bits")

# Our crypto experts answer 10 key questions

Justin Jacob

July 25, 2024

[cryptography](/categories/cryptography/)

Cryptography is a fundamental part of electronics and the internet that helps secure credit cards, cell phones, web browsing (fingers crossed you’re using TLS!), and even top-secret military data. Cryptography is just as essential in the blockchain space, with blockchains like Ethereum depending on hashes, Merkle trees, and ECDSA signatures, among other primitives, to function. Innovative techniques like pairings, fully homomorphic encryption, and zero-knowledge proofs have also made their way into the blockchain realm.

Cryptography seems like a complex and perplexing “mathemagical” puzzle for many. As a blockchain security engineer, I’ve always been fascinated by cryptography but never dived deeply into the topic. Luckily, my colleagues at Trail of Bits are world-class cryptography experts! I asked them ten questions to help you unravel some of cryptography’s mysteries. Keep in mind that some questions are reasonably advanced and may require extra background knowledge. But if you’re an aspiring crypto enthusiast, don’t be discouraged—keep reading!

### 1. Can you outline the most common commitment schemes employed for SNARKS?

A polynomial commitment scheme is a protocol where a prover commits to a certain polynomial and produces a proof that the commitment is valid. The protocol consists of three main algorithms:

* Commit
* Open
* Verify

In the commit phase, the prover sends their commitment—i.e., their claimed value of an evaluation of a polynomial f at a given point (so a value a such that `f(x) = a`). The commitment should be binding, meaning that once a prover commits to a polynomial they cannot “change their mind,” so to speak, and produce a valid proof for a different polynomial. It could also be hiding, in the sense that it is cryptographically infeasible to extract the value `x` such that `f(x) = a`. In the opening phase, the prover sends a proof that the commitment is valid. In the verification phase, the verifier checks that proof for validity. If the proof is valid, we know that the prover knows `x` such that `f(x) = a`, with high probability.

We are already familiar with one type of vector commitment, a Merkle tree. The properties of polynomial commitment schemes are similar, but they apply to polynomials instead. The most common commitment schemes being used in production are:

* KZG (Kate-Zaverucha-Goldberg), used, for example, for danksharding in [EIP 4844](https://www.eip4844.com/)
* FRI (Fast Reed-Solomon Interactive Oracle Proofs of Proximity) used in STARKs
* Commitments like Pedersen commitments are used in proof systems like Bulletproofs (used by Monero and Zcash)

KZG commitments leverage the fact that if a polynomial `f(x0) = u` at some point `x0`, then `f(x) - u` must have a factor of `(x - x0)`. By the [Schwartz-Zippel](https://en.wikipedia.org/wiki/Schwartz%E2%80%93Zippel_lemma) lemma, if we choose a large enough domain, it is very unlikely for a different polynomial `g(x) - u` to be divisible by `(x - x0)`. At a high level, we can leverage this to commit to the coefficients of `f(x)` and generate a proof, which the verifier can check extremely fast without revealing the polynomial itself through an elliptic curve pairing.

FRI uses error correcting codes to “boost” the probability that a verifier will discover an invalid commitment. We can then commit to the evaluations of the error corrected polynomial using a Merkle tree. Opening involves providing a Merkle authentication path to the verifier.

Pedersen commitments use the discrete logarithm problem. Precisely, we can commit to coefficients a0, … an given a basis of group elements `(g0, g1, … gn)` as `C = g0 * a0 + g1 * a1 + … + g1 * an`. We can combine this with the [Inner Product Argument](https://dankradfeist.de/ethereum/2021/07/27/inner-product-arguments.html) (which is out of this post’s scope) to generate a polynomial commitment scheme with open and verification algorithms based on the inner product argument.

KZG has very small proof sizes consisting of one group element. However, this involves a trusted setup, and one must delete the trusted setup parameter, or else anyone can forge proofs. FRI requires no trusted setup and is plausibly post-quantum secure yet has very large proof sizes. Lastly, Pedersen commitments and IPA do not require a trusted setup but require linear verification time.

Other commitment schemes exist, such as Dory, Hyrax, and Dark, but they are much less used in practice.

To learn more about these commitments, check out [our ZKDocs page](https://www.zkdocs.com/docs/zkdocs/commitments/).

### 2. Hashing is ubiquitous, yet few people grasp its inner workings. Can you clarify popular constructions (e.g., MD, Sponge) and highlight their differences?

Most hash functions people are familiar with, like MD5 and SHA1, are Merkle-Damgard constructions. The `keccak256` function that we all know and love is a sponge construction.

In the Merkle-Damgard construction, an arbitrary-length message gets parsed into blocks with a certain size.The key part is that a compression function gets applied to each block, using the previous block as the next compression function’s key (for the first block, we use an IV, or initialization vector, instead). The Merkle-Damgard construction shows that if the compression function is collision resistant, the whole hash function will be as well.

![](/img/wpdump/10cc61dc04ce0b74aea89062c10b5224.png)

Figure 1: Merkle-Damgard construction

In contrast, sponge constructions don’t use compression functions. The core of the sponge construction consists of two stages: an “absorb” phase, where parts of the message get XOR’d with an initial state while a permutation function is applied to it, and then a “squeeze” phase where parts of the output are extracted and outputted as a hash.

![](/img/wpdump/37421108cb89ccdc637ed0f9ba43e8eb.png)

Figure 2: Sponge construction

Notably, compared to Merkle-Damgard constructions, sponge constructions are not vulnerable to [length extension attacks](https://en.wikipedia.org/wiki/Length_extension_attack), since not all of the end result is used as an output to the hash function.

### 3. Elliptic curve cryptography (ECC) is even more enigmatic and considered a major “black box” in cryptography. Numerous pitfalls and technical attacks exist. Can you shed light on some theoretical assaults on elliptic curves, like Weil descent and the MOV attack?

ECC is often seen as a complex and somewhat mysterious part of cryptography, with potential vulnerabilities to various technical attacks. Two notable theoretical attacks are Weil descent and the MOV attack. Let’s demystify these a bit.

In essence, the security of ECC relies on the difficulty of solving a certain mathematical problem, known as the discrete logarithm problem, on elliptic curves. Standard elliptic curves are chosen specifically because they make this problem hard to crack. This is why, in practice, both Weil descent and the MOV attack are generally not feasible against standard curves.

* **[Weil descent](https://www.math.uzh.ch/sepp/magma-2.25.2-ds/html/text462.htm) attack**: This method involves using concepts from algebraic geometry, particularly a technique called Weil descent. The idea is to transform the discrete logarithm problem from its original form on an elliptic curve (a complex algebraic structure) to a similar problem on a simpler algebraic structure, like a hyperelliptic curve. This transformation can make the problem easier to solve using known algorithms like index calculus, but only if the original elliptic curve is simple enough. Standardized curves are usually complex enough to resist this attack.
* [**MOV attack**](https://crypto.stackexchange.com/questions/1871/...