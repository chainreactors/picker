---
title: We wrote the code, and the code won
url: https://blog.trailofbits.com/2024/08/15/we-wrote-the-code-and-the-code-won/
source: Trail of Bits Blog
date: 2024-08-16
fetch_date: 2025-10-06T18:03:34.197793
---

# We wrote the code, and the code won

[The Trail of Bits Blog](/ "The Trail of Bits Blog")

[![Trail of Bits Logo](/img/tob.png)](https://trailofbits.com "Trail of Bits")

# We wrote the code, and the code won

Tjaden Hess

August 15, 2024

[cryptography](/categories/cryptography/), [open-source](/categories/open-source/)

Earlier this week, [NIST officially announced](https://www.nist.gov/news-events/news/2024/08/nist-releases-first-3-finalized-post-quantum-encryption-standards) three standards specifying FIPS-approved algorithms for post-quantum cryptography. The Stateless Hash-Based Digital Signature Algorithm (SLH-DSA) is one of these standardized algorithms. The Trail of Bits cryptography team has been anticipating this announcement, and we are excited to share an announcement of our own: we built an open-source pure-Rust implementation of SLH-DSA, which has been [merged into RustCrypto](https://github.com/RustCrypto/signatures/pull/812).

Speed, memory safety, zero-cost abstractions, and an advanced type system make Rust an excellent language for cryptographic libraries. Transitioning to post-quantum cryptography is an investment in the future; these algorithms will be used in critical software for decades to come. If you’re making that kind of investment, you should use cryptography built with Rust, which is why we targeted RustCrypto with our project.

Because Trail of Bits supports the open-source community and encourages the adoption of post-quantum algorithms, we are contributing our implementation to the RustCrypto project and will maintain it there. However, securely transitioning to post-quantum cryptography will be a many-year, complex process, and we are committed to helping the industry in this transition beyond this library. If your company is thinking about how to most effectively and securely make the PQC transition, talk to our cryptography experts, and we’ll ensure you are secure and ahead of the curve.

## Why was SLH-DSA selected as a finalist?

Previously known as SPHINCS+, SLH-DSA is a highly conservative quantum-resistant signature scheme. Unlike standards that rely on the hardness of lattice problems, such as ML-DSA (Dilithium), SLH-DSA depends on the security of SHA2 or SHA3, which have been extensively studied and are confidently considered secure against both classical and quantum attacks. While experts believe ML-DSA is secure, its resistance to quantum attackers is more difficult to analyze and could someday weaken with increasingly advanced attacks. In addition, unlike stateful hash-based schemes like [LMS](https://blog.trailofbits.com/2024/04/26/announcing-two-new-lms-libraries/), SLH-DSA can safely function as a drop-in replacement for existing signature schemes such as ECDSA, EdDSA, and RSA-PSS.

The strong security properties of hash-based signature schemes come with performance costs. Due to its large signature sizes and long signing times, SLH-DSA is most appropriate for use cases with infrequent messages and long-lived keys, such as firmware signing.

## Implementation benefits

Our SLH-DSA Rust crate is no-std capable and does not use heap allocations, making it suitable for use on any platform, including embedded devices. To enhance our confidence in the correctness of the codebase, we have integrated all of the known answer test vectors available from NIST. In addition, the codebase was independently reviewed by other cryptographers on the Trail of Bits cryptography team who did not implement the codebase.

The implementation supports all 12 FIPS-approved parameter sets. It also provides the trait API defined in the RustCrypto signature crate, which allows drop-in replacement in Rust projects using RSA or elliptic curve cryptography.

## Future work

As we release this codebase publicly, we are confident in its security and correctness. However, that does not mean that this project is completed. We have multiple planned improvements to the codebase to improve its performance. For instance, we plan to support custom allocators for embedded devices with specific memory constraints. We will also continue to work with users to improve usability and documentation.

## Easing the transition to a post-quantum world

Our cryptography team has been heavily preparing for the post-quantum migration. You should talk to our experts as your organization plans or executes its post-quantum cryptography transition. Whether you need early advice on your transition plan, want feedback on a novel system design incorporating PQC, need to build a new PQC library, or need a security review of an existing PQC library, our cryptography team can help you.

In the meantime, please [check out the code](https://github.com/RustCrypto/signatures/tree/master/slh-dsa) and give us feedback! Your input is essential to help ensure that this library can be safe and effectively used by as many people as possible. We are still in the first stage of the post-quantum cryptography transition, and open-source implementations like this will play a crucial role as we continue on this journey.

#### If you enjoyed this post, share it:

[X](https://x.com/trailofbits "X")

[LinkedIn](https://linkedin.com/company/trail-of-bits "LinkedIn")

[GitHub](https://github.com/trailofbits "GitHub")

[Mastodon](https://infosec.exchange/%40trailofbits "Mastodon")

[Hacker News](https://news.ycombinator.com/from?site=trailofbits.com "Hacker News")

#### Page content

#### Recent Posts

* [Taming 2,500 compiler warnings with CodeQL, an OpenVPN2 case study](/2025/09/25/taming-2500-compiler-warnings-with-codeql-an-openvpn2-case-study/)
* [Supply chain attacks are exploiting our assumptions](/2025/09/24/supply-chain-attacks-are-exploiting-our-assumptions/)
* [Use mutation testing to find the bugs your tests don't catch](/2025/09/18/use-mutation-testing-to-find-the-bugs-your-tests-dont-catch/)
* [Fickling’s new AI/ML pickle file scanner](/2025/09/16/ficklings-new-ai/ml-pickle-file-scanner/)
* [How Sui Move rethinks flash loan security](/2025/09/10/how-sui-move-rethinks-flash-loan-security/)

© 2025 Trail of Bits.
Generated with [Hugo](https://gohugo.io/) and [Mainroad](https://github.com/Vimux/Mainroad/) theme.