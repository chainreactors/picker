---
title: There's a new way to break RSA that's faster than anything we've seen before
url: https://arstechnica.com/security/2026/09/theres-a-new-way-to-break-rsa-thats-faster-than-anything-weve-seen-before/
source: Instapaper: Unread
date: 2026-09-24
fetch_date: 2026-09-25T06:53:29.950906
---

# There's a new way to break RSA that's faster than anything we've seen before

[Skip to content](#main)
[Ars Technica home](https://arstechnica.com/)

Sections

[Forum](/civis/)[Subscribe](/subscribe/)[Search](/search/)

* [AI](https://arstechnica.com/ai/)
* [Biz & IT](https://arstechnica.com/information-technology/)
* [Cars](https://arstechnica.com/cars/)
* [Culture](https://arstechnica.com/culture/)
* [Gaming](https://arstechnica.com/gaming/)
* [Health](https://arstechnica.com/health/)
* [Policy](https://arstechnica.com/tech-policy/)
* [Science](https://arstechnica.com/science/)
* [Security](https://arstechnica.com/security/)
* [Space](https://arstechnica.com/space/)
* [Tech](https://arstechnica.com/gadgets/)

* [Feature](/features/)
* [Reviews](/reviews/)

* [AI](https://arstechnica.com/ai/)
* [Biz & IT](https://arstechnica.com/information-technology/)
* [Cars](https://arstechnica.com/cars/)
* [Culture](https://arstechnica.com/culture/)
* [Gaming](https://arstechnica.com/gaming/)
* [Health](https://arstechnica.com/health/)
* [Policy](https://arstechnica.com/tech-policy/)
* [Science](https://arstechnica.com/science/)
* [Security](https://arstechnica.com/security/)
* [Space](https://arstechnica.com/space/)
* [Tech](https://arstechnica.com/gadgets/)

[Forum](/civis/)[Subscribe](/subscribe/)

Story text

Size

Small
Standard
Large
Width
\*

Standard
Wide
Links

Standard
Orange

\* Subscribers only
  [Learn more](/store/product/subscriptions/)

Pin to story

Theme

* HyperLight
* Day & Night
* Dark
* System

[Search](/search/ "Search")

Sign In

Sign in dialog...

Sign in

KNOCKING ON HEAVEN’S DOOR

# There’s a new way to break RSA that’s faster than anything we’ve seen before

Until now, cryptographers thought factoring was the only way to break RSA. Not anymore.

[Dan Goodin](https://arstechnica.com/author/dan-goodin/)
–

Sep 24, 2026 7:15 am
| [58](https://arstechnica.com/security/2026/09/theres-a-new-way-to-break-rsa-thats-faster-than-anything-weve-seen-before/#comments "58 comments")

[![A transparent digital chain breaking at its weakest point over a binary code background.](https://cdn.arstechnica.net/wp-content/uploads/2026/09/breaking-digital-chain-640x366.jpg)
![A transparent digital chain breaking at its weakest point over a binary code background.](https://cdn.arstechnica.net/wp-content/uploads/2026/09/breaking-digital-chain-1152x648.jpg)](https://cdn.arstechnica.net/wp-content/uploads/2026/09/breaking-digital-chain.jpg)

Credit:
Getty Images

Credit:
Getty Images

Text
settings

Story text

Size

Small
Standard
Large
Width
\*

Standard
Wide
Links

Standard
Orange

\* Subscribers only
  [Learn more](/store/product/subscriptions/)

Minimize to nav

The world has known for decades that the [RSA cryptosystem](https://en.wikipedia.org/wiki/RSA_cryptosystem)’s days are numbered. Once quantum computing becomes practical (estimates for that range from 3 to 20 or more years), the foundational security it provides will crumble. New research has revealed a novel method that uses classical computing to reduce the current RSA security level to an unacceptably low threshold.

The practical risk is limited, but still significant. Applying the attack against the deprecated use of 1024-bit keys took a handful of months on an academic CPU cluster, significantly less than the current estimates for 1024-bit factoring that would require resources that only nations or companies with massive resources could achieve. Widely used RSA implementations are also safe.

Nonetheless, the research has taken cryptographers by surprise because it introduces signature forgery, a new way to break RSA keys without factoring. Equally important, this novel method reduces the required computing resources by orders of magnitude.

## Out of reach no more

“If this result holds up under peer review, it would indeed be a conceptual break-through,” Karsten Nohl, a cryptography expert and the head of innovation at Allurity, said in an interview. “RSA is as difficult to break as it is to factor large integers, at least so we thought. The researcher suggests that you can practically break RSA without cracking its key.”

Nadia Heninger, a University of California at San Diego professor and co-author, elaborated:

> Cryptographers thought that the only way to compute valid RSA digital signatures was to first compute the private key by factoring, and then use the private key to compute the signatures. For 1024-bit RSA, this was thought to be very expensive, albeit probably doable if you have the computational resources of the large tech companies or the NSA—on the order of tens of millions of dollars of computation time for a single key. For 2048-bit RSA, it was thought to be totally out of reach.

The [key forgery attack](https://eprint.iacr.org/2026/2131.pdf) Heninger and the other researchers devised is fully practical now for 1024-bit RSA. Even for 2048- and 4096-bit keys, the method reduces the security of RSA to unacceptable levels. The National Security Agency, [National Institute of Standards and Technology](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-57pt1r5.pdf), and [European Union Agency for Network and Information Security](https://web.archive.org/web/20151017094652/https%3A//www.enisa.europa.eu/activities/identity-and-trust/library/deliverables/algorithms-key-size-and-parameters-report-2014/at_download/fullReport) require that any cryptosystem should provide a level of no less than 128 or more bits, meaning the operations required must exceed 2128.

The forgery attack drops these levels to 265, 290, and 2119 for 1024-, 2048-, and 4096-bit keys respectively. These levels may further drop because Heninger’s team did all the coding by hand and used no AI or GPUs in performing the forgeries. The researcher said these tools will “almost certainly” drop the security levels further.

The attack works only against [blind-signature](https://www.ietf.org/archive/id/draft-irtf-cfrg-rsa-blind-signatures-02.html) implementations of RSA. The overwhelming majority of RSA in use today provides PKCS or PSS padding, a format that adds data to the plaintext before it’s encrypted. It prevents ciphertext from being deterministic and makes it less vulnerable to side channel and similar attacks. Still, some real-world systems continue to use blind-signature, also known as textbook, RSA. The best-known example, Heninger said, is [Privacy Pass](https://www.privacyguides.org/articles/2025/04/21/privacy-pass/#card-computers), a protocol that allows users to authenticate themselves without revealing their identity. Privacy Pass is used by both Apple and Cloudflare, among many others.

An attack on Privacy Pass would require an attacker to request 243 tokens from Cloudflare, Apple, or another organization.

An attack on Privacy Pass would require an attacker to request tokens from Cloudflare, Apple, or another organization 2^43 times.

Heninger said the requirement “sounds [like] a lot, but is on the same order of magnitude of the network traffic that Cloudflare has said publicly it handles in about a day.” Most Privacy Pass implementations rotate keys regularly, a measure that greatly reduces, but doesn’t automatically eliminate, the chances of attacker success.

The technique implements a variant of the number field sieve algorithm that was [invented](https://eprint.iacr.org/2007/424) in 2007. This “‘special’ number field sieve” is used with an “oracle”, a property of some cryptographic protocols that gives answers to queried inputs. By performing a massive number of operations, attackers can gather enough information to decipher the ciphertext. (This technique doesn’t appear to pose a practical threat against RSA with PKCS or PSS padding, because they provide a different type of oracle..) While factoring a 1024-bit key requires an estimated 280 operations and 500,000 to 1 million CPU core-years, using the sieve to forge a signature took just (as noted earlier) 265 operations and 1,380 core-years.

The paper’s authors and other researchers stress that the ...