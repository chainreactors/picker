---
title: Tracking the Cost of Quantum Factoring
url: http://security.googleblog.com/2025/05/tracking-cost-of-quantum-factori.html
source: Google Online Security Blog
date: 2025-05-24
fetch_date: 2025-10-06T22:27:43.770050
---

# Tracking the Cost of Quantum Factoring

![](https://ad.doubleclick.net/ddm/activity/src=2542116;type=gblog;cat=googl0;ord=1?)

[![](https://www.gstatic.com/images/branding/googlelogo/2x/googlelogo_color_150x54dp.png)](https://security.googleblog.com/)
[## Security Blog](/.)

The latest news and insights from Google on security and safety on the Internet

## [Tracking the Cost of Quantum Factoring](https://security.googleblog.com/2025/05/tracking-cost-of-quantum-factori.html "Tracking the Cost of Quantum Factoring")

May 23, 2025

Posted by Craig Gidney, Quantum Research Scientist, and Sophie Schmieg, Senior Staff Cryptography Engineer

Google Quantum AI's mission is to build best in class quantum computing for [otherwise unsolvable problems](https://research.google/blog/developing-industrial-use-cases-for-physical-simulation-on-future-error-corrected-quantum-computers/). For decades the quantum and security communities have also known that large-scale quantum computers will at some point in the future likely be able to break many of today’s secure public key cryptography algorithms, such as [Rivest–Shamir–Adleman (RSA)](https://en.wikipedia.org/wiki/RSA_cryptosystem). Google has long worked with the U.S. National Institute of Standards and Technology (NIST) and others in government, industry, and academia to develop and transition to post-quantum cryptography (PQC), which is expected to be resistant to quantum computing attacks. As quantum computing technology continues to advance, ongoing multi-stakeholder collaboration and action on PQC is critical.

In order to plan for the transition from today’s cryptosystems to an era of PQC, it's important the size and performance of a future quantum computer that could likely break current cryptography algorithms is carefully characterized. Yesterday, we published a [preprint](https://arxiv.org/abs/2505.15917) demonstrating that 2048-bit RSA encryption could theoretically be broken by a quantum computer with 1 million noisy qubits running for one week. This is a 20-fold decrease in the number of qubits from [our previous estimate](https://arxiv.org/abs/1905.09749), published in 2019. Notably, quantum computers with relevant error rates currently have on the order of only 100 to 1000 qubits, and the National Institute of Standards and Technology (NIST) recently released [standard PQC algorithms](https://www.federalregister.gov/documents/2024/08/14/2024-17956/announcing-issuance-of-federal-information-processing-standards-fips-fips-203-module-lattice-based) that are expected to be resistant to future large-scale quantum computers. However, this new result does underscore the importance of migrating to these standards in line with [NIST recommended timelines](https://nvlpubs.nist.gov/nistpubs/ir/2024/NIST.IR.8547.ipd.pdf).

Estimated resources for factoring have been steadily decreasing

Quantum computers break RSA by factoring numbers, using Shor’s algorithm. Since Peter Shor [published](https://ieeexplore.ieee.org/document/365700) this algorithm in 1994, the estimated number of qubits needed to run it has steadily decreased. For example, in 2012, it was [estimated](https://doi.org/10.1103/PhysRevA.86.032324) that a 2048-bit RSA key could be broken by a quantum computer with a billion physical qubits. In 2019, using the same physical assumptions – which consider qubits with a slightly lower error rate than Google Quantum AI’s [current quantum computers](https://doi.org/10.1038/s41586-024-08449-y) – the estimate was [lowered](https://doi.org/10.22331/q-2021-04-15-433) to 20 million physical qubits.

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEh_tljknRmP1Ypp9OiFdhj4dSP3FPYTp8WsIDrJWcQvLIJkziuUT1bE4eTU6zkmHovjQ9wafhaIlDvFYhT-OhHoNnJVfk2DI5uz3gBwwtNN2SLTz4Nuqi_Eehrrs9UnCY8OWe_8RVYEBuNgBXZeIZ7Cld9WzuuS8K5i1dW0LKKiPGTzNim6hoDSCjb46FZV/w575-h325/Screenshot%202025-05-22%20at%204.07.26%E2%80%AFPM.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEh_tljknRmP1Ypp9OiFdhj4dSP3FPYTp8WsIDrJWcQvLIJkziuUT1bE4eTU6zkmHovjQ9wafhaIlDvFYhT-OhHoNnJVfk2DI5uz3gBwwtNN2SLTz4Nuqi_Eehrrs9UnCY8OWe_8RVYEBuNgBXZeIZ7Cld9WzuuS8K5i1dW0LKKiPGTzNim6hoDSCjb46FZV/s620/Screenshot%202025-05-22%20at%204.07.26%E2%80%AFPM.png)

*Historical estimates of the number of physical qubits needed to factor 2048-bit RSA integers.*

This result represents a 20-fold decrease compared to our estimate from 2019

The reduction in physical qubit count comes from two sources: better algorithms and better error correction – whereby qubits used by the algorithm ("logical qubits") are redundantly encoded across many physical qubits, so that errors can be detected and corrected.

On the algorithmic side, the key change is to compute an approximate modular exponentiation rather than an exact one. An algorithm for doing this, while using only small work registers, was discovered [in 2024 by Chevignard and Fouque and Schrottenloher](https://eprint.iacr.org/2024/222). Their algorithm used 1000x more operations than prior work, but we found ways to reduce that overhead down to 2x.

On the error correction side, the key change is tripling the storage density of idle logical qubits by adding a second layer of error correction. Normally more error correction layers means more overhead, but a good combination was [discovered](https://doi.org/10.1038/s41467-025-59714-1) by the Google Quantum AI team in 2023. Another notable error correction improvement is using "magic state cultivation", [proposed](https://arxiv.org/abs/2409.17595) by the Google Quantum AI team in 2024, to reduce the workspace required for certain basic quantum operations. These error correction improvements aren't specific to factoring and also reduce the required resources for other quantum computations like in chemistry and materials simulation.

Security implications

NIST recently [concluded](https://www.nist.gov/news-events/news/2024/08/nist-releases-first-3-finalized-post-quantum-encryption-standards) a PQC competition that resulted in the first set of PQC standards. These algorithms can already be deployed to defend against quantum computers well before a working cryptographically relevant quantum computer is built.

To assess the security implications of quantum computers, however, it’s instructive to additionally take a closer look at the affected algorithms (see [here](https://bughunters.google.com/blog/5108747984306176/google-s-threat-model-for-post-quantum-cryptography) for a detailed look): RSA and Elliptic Curve Diffie-Hellman. As asymmetric algorithms, they are used for encryption in transit, including encryption for messaging services, as well as digital signatures (widely used to prove the authenticity of documents or software, e.g. the identity of websites). For asymmetric encryption, in particular encryption in transit, the motivation to migrate to PQC is made more urgent due to the fact that an adversary can collect ciphertexts, and later decrypt them once a quantum computer is available, known as a “store now, decrypt later” attack. Google has therefore been encrypting traffic both [in Chrome](https://blog.chromium.org/2024/05/advancing-our-amazing-bet-on-asymmetric.html) and [internally](https://cloud.google.com/blog/products/identity-security/why-google-now-uses-post-quantum-cryptography-for-internal-comms?e=48754805), switching to the standardized version of ML-KEM once it became available. Notably not affected is symmetric cryptography, which is primarily deployed in encryption at rest, and to enable some stateless services.

For signatures, things are more complex. Some signature use cases are similarly urgent, e.g., when public keys are fixed in hardware. In general, the landscape for signatures is mostly remarkable due to the higher complexity of the transition, since signature keys are used in many different places, and since these keys tend to be longer lived than the usually ephemeral encryption keys. Signature keys are therefore harder to replace and much more attractive targets to attack...