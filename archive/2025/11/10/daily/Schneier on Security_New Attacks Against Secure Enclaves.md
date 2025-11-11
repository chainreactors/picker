---
title: New Attacks Against Secure Enclaves
url: https://www.schneier.com/blog/archives/2025/11/new-attacks-against-secure-enclaves.html
source: Schneier on Security
date: 2025-11-10
fetch_date: 2025-11-11T03:14:36.376458
---

# New Attacks Against Secure Enclaves

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

## New Attacks Against Secure Enclaves

Encryption can protect data at rest and data in transit, but does nothing for data in use. What we have are secure enclaves. I’ve [written about](https://www.schneier.com/academic/archives/2023/12/decoupling-for-security.html) this before:

> Almost all cloud services have to perform some computation on our data. Even the simplest storage provider has code to copy bytes from an internal storage system and deliver them to the user. End-to-end encryption is sufficient in such a narrow context. But often we want our cloud providers to be able to perform computation on our raw data: search, analysis, AI model training or fine-tuning, and more. Without expensive, esoteric techniques, such as secure multiparty computation protocols or homomorphic encryption techniques that can perform calculations on encrypted data, cloud servers require access to the unencrypted data to do anything useful.
>
> Fortunately, the last few years have seen the advent of general-purpose, hardware-enabled secure computation. This is powered by special functionality on processors known as trusted execution environments (TEEs) or secure enclaves. TEEs decouple who runs the chip (a cloud provider, such as Microsoft Azure) from who secures the chip (a processor vendor, such as Intel) and from who controls the data being used in the computation (the customer or user). A TEE can keep the cloud provider from seeing what is being computed. The results of a computation are sent via a secure tunnel out of the enclave or encrypted and stored. A TEE can also generate a signed attestation that it actually ran the code that the customer wanted to run.

Secure enclaves are critical in our modern cloud-based computing architectures. And, of course, they have [vulnerabilities](https://arstechnica.com/security/2025/10/new-physical-attacks-are-quickly-diluting-secure-enclave-defenses-from-nvidia-amd-and-intel/):

> The most recent attack, released Tuesday, is known as TEE.fail. It defeats the latest TEE protections from all three chipmakers. The low-cost, low-complexity attack works by placing a small piece of hardware between a single physical memory chip and the motherboard slot it plugs into. It also requires the attacker to compromise the operating system kernel. Once this three-minute attack is completed, Confidential Compute, SEV-SNP, and TDX/SDX can no longer be trusted. Unlike the Battering RAM and Wiretap attacks from [last month](https://arstechnica.com/security/2025/09/intel-and-amd-trusted-enclaves-the-backbone-of-network-security-fall-to-physical-attacks/)—which worked only against CPUs using DDR4 memory—TEE.fail works against DDR5, allowing them to work against the latest TEEs.

Yes, these attacks require physical access. But that’s exactly the threat model secure enclaves are supposed to secure against.

Tags: [cloud computing](https://www.schneier.com/tag/cloud-computing/), [data protection](https://www.schneier.com/tag/data-protection/), [hardware](https://www.schneier.com/tag/hardware/), [physical security](https://www.schneier.com/tag/physical-security/)

[Posted on November 10, 2025 at 7:04 AM](https://www.schneier.com/blog/archives/2025/11/new-attacks-against-secure-enclaves.html) •
[6 Comments](https://www.schneier.com/blog/archives/2025/11/new-attacks-against-secure-enclaves.html#comments)

### Comments

jelo 117 •
[November 10, 2025 8:55 AM](https://www.schneier.com/blog/archives/2025/11/new-attacks-against-secure-enclaves.html/#comment-449761)

“Those early versions encrypted no more than 256MB of RAM, a small enough space to use the much stronger probabilistic form of encryption. The TEEs built into server chips, by contrast, must often encrypt terabytes of RAM. Probabilistic encryption doesn’t scale to that size without serious performance penalties. Finding a solution that accommodates this overhead won’t be easy.

“One mitigation over the short term is to ensure that each 128-bit block of ciphertext has sufficient entropy. Adding random plaintext to the blocks prevents ciphertext repetition. The researchers say the entropy can be added by building a custom memory layout that inserts a 64-bit counter with a random initial value to each 64-bit block before encrypting it.”

How to cook pasta:

1. Bring water to a rapid boil.
2. Add a lot of salt. The water should taste like the sea
3. Etc. etc.

Rob Stubbs •
[November 10, 2025 9:03 AM](https://www.schneier.com/blog/archives/2025/11/new-attacks-against-secure-enclaves.html/#comment-449762)

The main (and significant) benefits of TEEs include (i) protecting sensitive data from malicious code running on the same system, and (ii) attesting the validity of the code and operational environment.

While TEEs afford some level of physical security (e.g. encrypting data in RAM), it is difficult for the CPU to protect an entire system against all physical threats. This would really need anti-tamper mechanisms as deployed in HSMs.

Similarly, TEEs can’t protect against EMC threats – you still need to use best practice coding techniques for cryptography.

The bottom line is that it’s important to understand the threats you’re trying to protect against and the mitigations offered by different security technologies. There is no single silver bullet, defence in depth is needed. While not perfect, TEEs are a valuable tool in the security toolbox.

[Mexaly](https://xkcd.com/722) •
[November 10, 2025 9:21 AM](https://www.schneier.com/blog/archives/2025/11/new-attacks-against-secure-enclaves.html/#comment-449764)

Physical access rules.

AlexT •
[November 10, 2025 12:07 PM](https://www.schneier.com/blog/archives/2025/11/new-attacks-against-secure-enclaves.html/#comment-449776)

Quite frankly if you don’t have physical security all bets are off.

Clive Robinson •
[November 10, 2025 5:07 PM](https://www.schneier.com/blog/archives/2025/11/new-attacks-against-secure-enclaves.html/#comment-449778)

@ AlexT, ALL,

Every so often I comment on the issues involved on this blog you can find my limited comments on this issue back on the Squid page where it was raised.

But one fundamental mistake nearly everyone makes is from the observation,

> *“… if you don’t have physical security all bets are off.”*

It is a problem because “physical security” is not a natural phenomena as such. Simple objects have no real intrinsic security, likewise nor do components of systems.

This gives rise to a couple of things to note,

1, All security has to be built from insecure components.
2, All components have vulnerabilities around them as do the systems they are part of.

Thus security can be seen as two things,

1, Built from imperfect “methods”.
2, So “probabilistic” in nature.

Worse human dogma often gets in the way as a form of cognitive bias.

Thus we end up almost always with hierarchical systems made of components that form a tree structure. These are genera...