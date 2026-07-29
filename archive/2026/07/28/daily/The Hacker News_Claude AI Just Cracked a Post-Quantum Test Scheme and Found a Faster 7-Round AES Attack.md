---
title: Claude AI Just Cracked a Post-Quantum Test Scheme and Found a Faster 7-Round AES Attack
url: https://thehackernews.com/2026/07/claude-ai-just-cracked-post-quantum.html
source: The Hacker News
date: 2026-07-28
fetch_date: 2026-07-29T05:04:26.635353
---

# Claude AI Just Cracked a Post-Quantum Test Scheme and Found a Faster 7-Round AES Attack

#1 Trusted Cybersecurity News Platform

Followed by 5.70+ million[**](https://twitter.com/thehackersnews)
[**](https://www.linkedin.com/company/thehackernews/)
[**](https://www.facebook.com/thehackernews)

[![The Hacker News Logo](data:image/png;base64...)](/)

**

**

[** Get the Latest News](#email-outer)

* [Home](/)
* [Newsletter](#email-outer)
* [Webinars](/p/upcoming-hacker-news-webinars.html)

* [Home](/)
* [Threat Intelligence](/search/label/Threat%20Intelligence)
* [Vulnerabilities](/search/label/Vulnerability)
* [Cyber Attacks](/search/label/Cyber%20Attack)
* [Webinars](/p/upcoming-hacker-news-webinars.html)
* [Expert Insights](https://thehackernews.com/expert-insights/)
* [Awards](https://awards.thehackernews.com/)

**

**

**

Resources

* [Webinars](/p/upcoming-hacker-news-webinars.html)
* [Awards](https://awards.thehackernews.com/)
* [Free eBooks](https://thehackernews.tradepub.com)

About Site

* [About THN](/p/about-us.html)
* [Jobs](/p/careers-technical-writer-designer-and.html)
* [Advertise with us](/p/advertising-with-hacker-news.html)

Contact/Tip Us

[**

Reach out to get featured—contact us to send your exclusive story idea, research, hacks, or ask us a question or leave a comment/feedback!](/p/submit-news.html)

Follow Us On Social Media

[**](https://www.facebook.com/thehackernews)
[**](https://twitter.com/thehackersnews)
[**](https://www.linkedin.com/company/thehackernews/)
[**](https://www.youtube.com/c/thehackernews?sub_confirmation=1)
[**](https://www.instagram.com/thehackernews/)

[** RSS Feeds](https://feeds.feedburner.com/TheHackersNews)
[** Email Alerts](#email-outer)

[![cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgrKWHErc__Wn0forfQ5eJ5sIR1hVKCHCTeNQOaAX4lbygJ8S1Xpemx6JXl78dpwiT65DDBGURp48A3EemKzmli-jXPI3v1928MnJm-1j2ZPUaFXCvuySFhyphenhyphenKR-Li6fAinFT2bhLgsqUSNUR_ggMAnOHi3jD1qYWHXvueX8WdtxAd6GYety9cBGYABo18hX/s728-e100/tt-d.jpg)](https://thehackernews.uk/ai-zero-trust-h-d)

# [Claude AI Just Cracked a Post-Quantum Test Scheme and Found a Faster 7-Round AES Attack](https://thehackernews.com/2026/07/claude-ai-just-cracked-post-quantum.html)

**Swati Khandelwal**Jul 28, 2026Artificial Intelligence / Encryption

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgPhJ6dzEL23Ak57nA_XsbXtGaxl5wNrcGBPMQBVz1jddDuX_oTndpQjl3omqMxhRnQ1P4cSF7Ut18tccLFT2BxngpYTqTP8Kg6f4clFWRQ2GvxetR-uAGjMS2SsZwsiPcq5vyxCmP_AN3rCPvO5WMQeLNEit0q14i0iY9wuIUDAHMXkyvO3KjIC6c6Ozg/s1700-e365/Claude.jpg)

Anthropic says **[Claude Mythos Preview](https://thehackernews.com/2026/04/anthropics-claude-mythos-finds.html)** helped derive an end-to-end key-recovery attack against HAWK-256 and a 200- to 800-fold speedup for an attack on seven-round AES-128.

The HAWK attack exploits a previously unused symmetry in the lattice behind the signature scheme. Anthropic's released implementation gives an expected end-to-end runtime of about three hours and 42 minutes on a 96-core server. The AES result removes a 256-way guessing step from an existing meet-in-the-middle attack.

Anthropic said neither result affects production systems. HAWK remains a candidate in a National Institute of Standards and Technology (NIST) post-quantum standardization process, and the public recovery code only targets the smaller HAWK-256 parameter.

The Advanced Encryption Standard (AES) result applies to seven of AES-128's ten rounds and still requires an impractical number of chosen plaintexts. The company said no production software needs to change as a result.

Anthropic [published the findings](https://www.anthropic.com/research/discovering-cryptographic-weaknesses) alongside two technical papers and reproducibility artifacts. The company said Mythos Preview largely conducted the research itself, with humans supplying project direction, computing resources, and extensive verification.

## A symmetry hiding in HAWK's lattice

HAWK is the only lattice-based scheme among the [nine candidates that NIST advanced](https://csrc.nist.gov/projects/pqc-dig-sig/round-3-additional-signatures) to the third round of its additional post-quantum digital-signature process in May 2026. Its NIST security-level parameter sets are HAWK-512 and HAWK-1024; [HAWK-256 is a challenge parameter](https://csrc.nist.gov/csrc/media/Projects/pqc-dig-sig/documents/round-2/spec-files/hawk-spec-round2-web.pdf) provided as a cryptanalytic target.

Direct HAWK key recovery is an instance of the search module Lattice Isomorphism Problem (smLIP). An attacker must recover a hidden transformation between two lattices.

A [paper by Daniël van Gent and Ludo Pulles](https://eprint.iacr.org/2025/928) showed that a nontrivial automorphism, a symmetry that preserves the lattice, would reduce HAWK key recovery to finding a short vector in a lattice of roughly half the original dimension.

That work opened the attack path, but the authors said it did not then affect HAWK. Anthropic says Mythos Preview found the additional automorphism needed to exploit the path.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/ai-vuln-protection-d)

The resulting [HAWK-n attack](https://www.anthropic.com/document/hawk_key_recovery.pdf) constructs what the researchers call a τ-cocycle lattice from the public key. It then uses lattice reduction and sieving to recover short vectors before reconstructing a secret basis that can sign messages for the original public key.

Anthropic's [released implementation](https://github.com/anthropics/cryptography-research-demo/tree/main/HAWK) verifies the recovered key by signing a message and checking it with the NIST reference implementation. It does not recover the original 96-byte secret-key seed. Instead, it produces a 592-byte decoded key containing functionally equivalent signing material.

Anthropic's released code supports HAWK-256 only and rejects every non-HAWK-256 input. The repository includes two public keys that Anthropic says it successfully attacked. It also supports generating and testing fresh HAWK-256 keys.

Anthropic estimates that the expected HAWK-256 key-recovery work factor falls from 264 to 238. In a [same-day NIST-forum announcement](https://groups.google.com/a/list.nist.gov/g/pqc-forum/c/2r2u6SbHun4), it said the gate-count estimate falls from 2150 to 2108 for HAWK-512 and from 2288 to 2182 for HAWK-1024. Both larger parameters remain impractical to attack.

As of this review, the public record does not show whether NIST or the HAWK submitters will change the scheme's parameters, security claims or standing in the standardization process in response to those lower estimates, if at all.

The attack remains exponential. It is not a polynomial-time break of HAWK, and Anthropic said it does not extend to other NIST signature candidates or lattice cryptography generally.

Anthropic said Mythos Preview developed and verified the result over approximately 60 hours in a multi-agent environment. A human researcher provided occasional project-management guidance but was not a lattice-cryptography specialist. The company put the application programming interface (API) cost at about $100,000.

## Faster, but still impractical

The second result targets AES-128 reduced from ten rounds to seven. Studying reduced-round ciphers is standard cryptanalytic practice because it measures how much safety margin remains before an attack reaches the full construction.

The attack assumes an adversary can obtain about 2105 chosen plaintexts encrypted under one fixed, unknown key. That requirement alone puts it far outside real-world use.

Previous meet-in-the-middle attacks trade memory for computation by storing intermediate cipher states and matching calculations made from opposite ends of the cipher. One stage in the prior attack required testing 256 possible values before searching the table.

Mythos developed an invariant fingerprint Anthropic calls the Möbius Bridge. Because the fingerprint does n...