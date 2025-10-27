---
title: E2EE for the Fediverse Update – We’re Going Post-Quantum
url: https://soatok.blog/2024/09/13/e2ee-for-the-fediverse-update-were-going-post-quantum/
source: Dhole Moments
date: 2024-09-14
fetch_date: 2025-10-06T18:27:28.855244
---

# E2EE for the Fediverse Update – We’re Going Post-Quantum

[Skip to the content](#site-content)

Search

[Dhole Moments](https://soatok.blog/)

Software, Security, Cryptography, and Furries

Menu

* [Home](https://soatok.blog/)
* [Blog](https://soatok.blog/b/)
* [Explore](https://soatok.blog/explore/)
* [About](https://soatok.blog/about/)

Search

Search for:

Close search

Close Menu

* [Home](https://soatok.blog/)
* [Blog](https://soatok.blog/b/)
* [Explore](https://soatok.blog/explore/)
* [About](https://soatok.blog/about/)

Categories

[Cryptography](https://soatok.blog/category/cryptography/) [Fediverse E2EE Project](https://soatok.blog/category/technology/open-source/fediverse-e2ee-project/) [Open Source](https://soatok.blog/category/technology/open-source/)

# E2EE for the Fediverse Update – We’re Going Post-Quantum

* Post author

  By [Soatok](https://soatok.blog/author/soatok/)
* Post date

  [September 13, 2024](https://soatok.blog/2024/09/13/e2ee-for-the-fediverse-update-were-going-post-quantum/)

![E2EE for the Fediverse Update - We're Going Post-Quantum](https://i0.wp.com/soatok.blog/wp-content/uploads/2024/09/BlogHeader-2024-PostQuantum-Fedi-E2EE-1.png?fit=1200%2C675&ssl=1)

In 2022, I wrote about [my plan to build end-to-end encryption for the Fediverse](https://soatok.blog/2022/11/22/towards-end-to-end-encryption-for-direct-messages-in-the-fediverse/). The goals were simple:

1. Provide secure encryption of message content and media attachments between Fediverse users, as a new type of Direct Message which is encrypted between participants.
2. Do not pretend to be a [Signal competitor](https://soatok.blog/2024/07/31/what-does-it-mean-to-be-a-signal-competitor/).

The primary concern at the time was “honest but curious” Fediverse instance admins who might snoop on another user’s private conversations.

After I finally was happy with the client-side secret key management piece, I had moved on to figure out how to exchange public keys. And that’s where things got complicated, and work stalled for 2 years.

![](https://i0.wp.com/soatok.blog/wp-content/uploads/2023/10/SoatokGlitch.png?resize=512%2C445&ssl=1)

Art: [AJ](https://sfw.furaffinity.net/user/ajlovesdinos/)

I wrote a series of blog posts on this complication, what I’m doing about it, and some other cool stuff in the draft specification.

* [Towards Federated Key Transparency](https://soatok.blog/2024/06/06/towards-federated-key-transparency/) introduced the Public Key Directory project
* [Federated Key Transparency Project Update](https://soatok.blog/2024/08/21/federated-key-transparency-project-update/) talked about some of the trade-offs I made in this design
  + Not supporting ECDSA at all, since FIPS 186-5 supports Ed25519
  + Adding an account recovery feature, which power users can opt out of, that allows instance admins to help a user recover from losing all their keys
  + Building a Key Transparency system that can tolerate GDPR *Right To Be Forgotten* takedown requests without invalidating history
* [Introducing Alacrity to Federated Cryptography](https://soatok.blog/2024/08/28/introducing-alacrity-to-federated-cryptography/) discussed how I plan to ensure that independent third-party clients stay up-to-date or lose the ability to decrypt messages

Recently, NIST published the new Federal Information Protection Standards documents for three post-quantum cryptography algorithms:

* [FIPS-203](https://csrc.nist.gov/pubs/fips/203/final) (ML-KEM, formerly known as CRYSTALS-Kyber),
* [FIPS-204](https://csrc.nist.gov/pubs/fips/204/final) (ML-DSA, formerly known as CRYSTALS-Dilithium)
* [FIPS-205](https://csrc.nist.gov/pubs/fips/205/final) (SLH-DSA, formerly known as SPHINCS+)

The race is now on to implement and begin migrating the Internet to use post-quantum KEMs. (Post-quantum signatures are less urgent.) If you’re curious why, [this CloudFlare blog post](https://blog.cloudflare.com/sv-se/pq-2024/) explains the situation quite well.

Since I’m proposing a new protocol and implementation at the dawn of the era of post-quantum cryptography, I’ve decided to migrate the asymmetric primitives used in my proposals towards post-quantum algorithms **where it makes sense to do so**.

![Soatok Yay Sticker](https://i0.wp.com/soatok.blog/wp-content/uploads/2024/07/SoatokCheer.png?resize=512%2C379&ssl=1)

Art: [AJ](https://sfw.furaffinity.net/user/ajlovesdinos/)

The rest of this blog post is going to talk about technical specifics and the decisions I intend to make in both projects, as well as some other topics I’ve been thinking about related to this work.

## Which Algorithms, Where?

I’ll discuss these choices in detail, but for the impatient:

* Public Key Directory
  + Still just Ed25519 for now
* End-to-End Encryption
  + KEMs: [X-Wing](https://eprint.iacr.org/2024/039) (Hybrid X25519 and ML-KEM-768)
  + Signatures: Still just Ed25519 for now

Virtually all other uses of cryptography is symmetric-key or keyless (i.e., hash functions), so this isn’t a significant change to the design I have in mind.

## Post-Quantum Algorithm Selection Criteria

While I am personally skeptical if we will see a practical cryptography-relevant quantum computer in the next 30 years, due to various engineering challenges and a glacial pace of progress on solving them, [post-quantum cryptography is still a damn good idea even if a quantum computer doesn’t emerge](https://blog.trailofbits.com/2024/07/01/quantum-is-unimportant-to-post-quantum/).

Post-Quantum Cryptography comes in two flavors:

1. Key Encapsulation Mechanisms (KEMs), which [I wrote about previously](https://soatok.blog/2024/02/26/kem-trails-understanding-key-encapsulation-mechanisms/).
2. Digital Signature Algorithms (DSAs).

Originally, my proposals were going to use Elliptic Curve Diffie-Hellman (ECDH) in order to establish a symmetric key over an untrusted channel. Unfortunately, ECDH falls apart in the wake of a crypto-relevant quantum computer. ECDH is the component that will be replaced by post-quantum KEMs.

Additionally, my proposals make heavy use of Edwards Curve Digital Signatures (EdDSA) over the edwards25519 elliptic curve group (thus, Ed25519). This could be replaced with a post-quantum DSA (e.g., ML-DSA) and function just the same, albeit with bandwidth and/or performance trade-offs.

### But isn’t post-quantum cryptography somewhat new?

Lattice-based cryptography has been around almost as long as elliptic curve cryptography. One of the first designs, NTRU, was developed in 1996.

Meanwhile, ECDSA was published in 1992 by Dr. Scott Vanstone (although it was not made a standard until 1999). Lattice cryptography is pretty well-understood by experts.

However, before the post-quantum cryptography project, there hasn’t been a lot of incentive for attackers to study lattices (unless they wanted to muck with homomorphic encryption).

So, naturally, there is *some* risk of a cryptanalysis renaissance after the first post-quantum cryptography algorithms are widely deployed to the Internet.

However, this risk is mostly a concern for KEMs, due to the output of a KEM being the key used to encrypt sensitive data. Thus, when selecting KEMs for post-quantum security, I will choose a Hybrid construction.

### Hybrid what?

*We’re not talking [folfs](https://www.youtube.com/channel/UCdCxCY_jdXtnq5FNh7x4IRA), sonny!*

Hybrid isn’t just a thing that furries do with their fursonas. It’s also a term that comes up a lot in cryptography.

Unfortunately, it comes up a little *too* much.

![Parks and Rec "you go to jail" meme template about cryptography.  First panel: "You build KEM + DEM out of RSA and AES? Hybrid."  Second: "You mix classical and post-quantum? Hybrid."  Third: "You mix trust models in a PKI? Believe it or not, also Hybrid."  Final panel: "We have the most overloaded term in cryptography thanks to Hybrid."](https://i0.wp.com/soatok.blog/wp-content/uploads/2024/09/hybrid.jpg?resize=500%2C500&ssl=1)

I made this dumb meme with imgflip

When I say we use Hybrid constructions, what I r...