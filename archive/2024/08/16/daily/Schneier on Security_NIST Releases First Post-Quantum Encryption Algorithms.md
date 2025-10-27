---
title: NIST Releases First Post-Quantum Encryption Algorithms
url: https://www.schneier.com/blog/archives/2024/08/nist-releases-first-post-quantum-encryption-algorithms.html
source: Schneier on Security
date: 2024-08-16
fetch_date: 2025-10-06T18:18:53.899903
---

# NIST Releases First Post-Quantum Encryption Algorithms

# [Schneier on Security](https://www.schneier.com/)

Menu

* [Blog](https://www.schneier.com)
* [Newsletter](https://www.schneier.com/crypto-gram/)
* [Books](https://www.schneier.com/books/)
* [Essays](https://www.schneier.com/essays/)
* [News](https://www.schneier.com/news/)
* [Talks](https://www.schneier.com/talks/)
* [Academic](https://www.schneier.com/academic/)
* [About Me](https://www.schneier.com/blog/about/)

### Search

*Powered by [DuckDuckGo](https://duckduckgo.com/)*

Blog

Essays

Whole site

### Subscribe

[![Atom](https://www.schneier.com/wp-content/uploads/2019/10/rss-32px.png)](https://www.schneier.com/feed/atom/)[![Facebook](https://www.schneier.com/wp-content/uploads/2019/10/facebook-32px.png)](https://www.facebook.com/bruce.schneier)[![Twitter](https://www.schneier.com/wp-content/uploads/2019/10/twitter-32px.png)](https://twitter.com/schneierblog)[![Email](https://www.schneier.com/wp-content/uploads/2019/10/email-32px.png)](https://www.schneier.com/crypto-gram)

[Home](https://www.schneier.com)[Blog](https://www.schneier.com/blog/archives/)

## NIST Releases First Post-Quantum Encryption Algorithms

From the [Federal Register](https://www.govinfo.gov/content/pkg/FR-2024-08-14/pdf/2024-17956.pdf):

> After three rounds of evaluation and analysis, NIST selected four algorithms it will standardize as a result of the PQC Standardization Process. The public-key encapsulation mechanism selected was CRYSTALS-KYBER, along with three digital signature schemes: CRYSTALS-Dilithium, FALCON, and SPHINCS+.

These algorithms are part of three NIST standards that have been finalized:

* FIPS 203: [Module-Lattice-Based Key-Encapsulation Mechanism Standard](https://csrc.nist.gov/pubs/fips/203/final)
* FIPS 204: [Module-Lattice-Based Digital Signature Standard](https://csrc.nist.gov/pubs/fips/204/final)
* FIPS 205: [Stateless Hash-Based Digital Signature Standard](https://csrc.nist.gov/pubs/fips/205/final)

NIST [press release](https://www.nist.gov/news-events/news/2024/08/nist-releases-first-3-finalized-post-quantum-encryption-standards). My [recent](https://www.schneier.com/blog/archives/2023/08/you-cant-rush-post-quantum-computing-standards.html) [writings](https://www.schneier.com/essays/archives/2024/05/lattice-based-cryptosystems-and-quantum-cryptanalysis.html) on post-quantum cryptographic standards.

EDITED TO ADD: Good [article](https://www.theregister.com/2024/08/14/nist_postquantum_standards/):

> One – [ML-KEM](https://nvlpubs.nist.gov/nistpubs/fips/nist.fips.203.pdf) [PDF] (based on CRYSTALS-Kyber) – is intended for general encryption, which protects data as it moves across public networks. The other two –- [ML-DSA](https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.204.pdf) [PDF] (originally known as CRYSTALS-Dilithium) and [SLH-DSA](https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.205.pdf) [PDF] (initially submitted as Sphincs+)—secure digital signatures, which are used to authenticate online identity.
>
> A fourth algorithm – [FN-DSA](https://csrc.nist.gov/csrc/media/Presentations/2024/falcon/images-media/prest-falcon-pqc2024.pdf) [PDF] (originally called FALCON) – is slated for finalization later this year and is also designed for digital signatures.
>
> NIST continued to evaluate two other sets of algorithms that could potentially serve as backup standards in the future.
>
> One of the sets includes three algorithms designed for general encryption – but the technology is based on a different type of math problem than the ML-KEM general-purpose algorithm in today’s finalized standards.
>
> NIST plans to select one or two of these algorithms by the end of 2024.

*IEEE Spectrum* [article](https://spectrum.ieee.org/post-quantum-cryptography-2668949802).

Slashdot [thread](https://it.slashdot.org/story/24/08/14/2150250/nist-finalizes-trio-of-post-quantum-encryption-standards).

Tags: [cryptography](https://www.schneier.com/tag/cryptography/), [encryption](https://www.schneier.com/tag/encryption/), [national security policy](https://www.schneier.com/tag/national-security-policy/), [NIST](https://www.schneier.com/tag/nist/), [quantum computing](https://www.schneier.com/tag/quantum-computing/), [security standards](https://www.schneier.com/tag/security-standards/)

[Posted on August 15, 2024 at 11:37 AM](https://www.schneier.com/blog/archives/2024/08/nist-releases-first-post-quantum-encryption-algorithms.html) •
[5 Comments](https://www.schneier.com/blog/archives/2024/08/nist-releases-first-post-quantum-encryption-algorithms.html#comments)

### Comments

Clive Robinson •
[August 15, 2024 12:34 PM](https://www.schneier.com/blog/archives/2024/08/nist-releases-first-post-quantum-encryption-algorithms.html/#comment-440028)

@ ALL,

I kind of guess based on the track record, one the first questions in peoples heads will be,

“How long before a break gets anounced? Especially a non quantum break?”

Which is why other questions will get asked over the next few days and months, including “What Next?”

Mind you this from the press release gave me a hollow laugh,

> *“Quantum computing technology is developing rapidly, and some experts predict that a device with the capability to break current encryption methods could appear within a decade, threatening the security and privacy of individuals, organizations and entire nations.”*

With “collect it all” that “threat” started years ago for the majority, and like a “beheading” all we are waiting for “is the axe to fall”.

I guess the majority of records for the likes of “e-commerce” won’t be of interest unless for things that lets just say are “morally questionable” or worse, or can be used to show “behaviour patterns”.

I don’t do e-commerce, and have not tried it since Amazon “behaved like a criminal” and I don’t do “social media” either and in general I keep my behaviours “uninteresting” and have done since before the 1990’s

Because I’m old enough to have lived through the failing of DES and Crypto-Wars-1 and foreseen the path that was being set for the majority to the “Guilded Cage” and took care to keep off of it, and still continue to do so.

Barbatus •
[August 15, 2024 3:49 PM](https://www.schneier.com/blog/archives/2024/08/nist-releases-first-post-quantum-encryption-algorithms.html/#comment-440031)

The link to FIPS 205 has a typo in it and instead links to FIPS 203

Z.Lozinski •
[August 15, 2024 7:09 PM](https://www.schneier.com/blog/archives/2024/08/nist-releases-first-post-quantum-encryption-algorithms.html/#comment-440033)

@ Clive,

There is firmware/software signing. Updating code signing has been the highest priority for the NSA since before 2022. For those not following the transition to Post Quantum Cryptography, the NSA has declassified and published a detailed timeline for the US Government. (Search “CNSA 2.0”). The IETF standardised quantum-safe software signing a few years ago (XMS/LMSS). (But .. XMS/LMSS are hard to implement securely at scale)

Ledgers. Digitally signed ledgers with legal force, such as the UK’s Land Registry. Forging the ownership of one set of property deeds is a personal tragedy for the person who loses their house or apartment. Forging 10,000 deeds leads to a crash in the City of London as the mortgage-backed securities market collapses. Same for Bitcoin and Central Bank Digital Currency.

Authentication. If I was a wicked person, I would be targeting the authentication of high-value payments. It is not worth using a quantum computer to forge an EMV card payment for a journey on the London Underground (GBP2.80). It is worth using a quantum computer to attack a Central Bank payment. FEDWIRE has a limit of USD 10B – 1 cent for a single transaction. And we know there have been successful attacks on Central Bank payments (2015, Federal Reserve & Bank of Bangladesh).

Military cryptographic systems have been designed to fallback if a systemic break occurs. We have never had to do this for commercial cryptography. The concept of ‘cryptographic agility’ is supposed ...