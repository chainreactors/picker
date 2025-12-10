---
title: Tailoring 9 Zero Trust and Security Principles to Weapon Systems
url: https://www.sei.cmu.edu/blog/tailoring-9-zero-trust-and-security-principles-to-weapon-systems/?utm_source=blog&utm_medium=rss&utm_campaign=my_site_updates
source: SEI Blog
date: 2025-12-09
fetch_date: 2025-12-10T03:22:36.637896
---

# Tailoring 9 Zero Trust and Security Principles to Weapon Systems

icon-carat-right

menu

search

cmu-wordmark

[Carnegie Mellon University

cmu-wordmark](https://www.cmu.edu)

About

Our Work

Publications

News and Events

Education and Outreach

Careers

[SEI Blog](/blog/)

1. [Home](/)
2. [Publications](/publications/)
3. [Blog](/blog/)
4. Tailoring 9 Zero Trust and Security Principles to Weapon Systems

[ ]

### Cite This Post

×

* [AMS](#amsTab)
* [APA](#apaTab)
* [Chicago](#chicagoTab)
* [IEEE](#ieeeTab)
* [BibTeX](#bibTextTab)

AMS Citation

Alberts, C., and Morrow, T., 2025: Tailoring 9 Zero Trust and Security Principles to Weapon Systems. Carnegie Mellon University, Software Engineering Institute's Insights (blog), Accessed December 10, 2025, https://doi.org/10.58012/1vqj-4567.

Copy

APA Citation

Alberts, C., & Morrow, T. (2025, December 9). Tailoring 9 Zero Trust and Security Principles to Weapon Systems. Retrieved December 10, 2025, from https://doi.org/10.58012/1vqj-4567.

Copy

Chicago Citation

Alberts, Christopher, and Timothy Morrow. "Tailoring 9 Zero Trust and Security Principles to Weapon Systems." *Carnegie Mellon University, Software Engineering Institute's Insights (blog)*. Carnegie Mellon's Software Engineering Institute, December 9, 2025. https://doi.org/10.58012/1vqj-4567.

Copy

IEEE Citation

C. Alberts, and T. Morrow, "Tailoring 9 Zero Trust and Security Principles to Weapon Systems," *Carnegie Mellon University, Software Engineering Institute's Insights (blog)*. Carnegie Mellon's Software Engineering Institute, 9-Dec-2025 [Online]. Available: https://doi.org/10.58012/1vqj-4567. [Accessed: 10-Dec-2025].

Copy

BibTeX Code

@misc{alberts\_2025,
author={Alberts, Christopher and Morrow, Timothy},
title={Tailoring 9 Zero Trust and Security Principles to Weapon Systems},
month={{Dec},
year={{2025},
howpublished={Carnegie Mellon University, Software Engineering Institute's Insights (blog)},
url={https://doi.org/10.58012/1vqj-4567},
note={Accessed: 2025-Dec-10}
}

Copy

# Tailoring 9 Zero Trust and Security Principles to Weapon Systems

![Headshot of Christopher Alberts.](/media/images/thumb_big_c-alberts_blog_author.max-180x180.format-webp.webp)
![Headshot of Timothy Morrow.](/media/images/thumb_big_t-morrow_blog_authors.max-180x180.format-webp.webp)

###### [Christopher J. Alberts](/authors/christopher-alberts) and [Timothy Morrow](/authors/timothy-morrow)

###### December 9, 2025

##### PUBLISHED IN

[Secure Development](/blog/topics/secure-development/)

##### CITE

<https://doi.org/10.58012/1vqj-4567>

Get Citation

##### SHARE

The Department of War (DoW) has defined an approach for implementing zero trust in weapon systems, which generally have different requirements than enterprise information technology (EIT) systems. Because of these differences, DoW stakeholders need guidance on how to tailor and adapt zero trust concepts to weapon system platforms. To help address this need, we conducted a study that analyzed the applicability of nine foundational security and zero trust principles to weapon system environments. These principles define a framework for making security decisions, implementing security controls, and enabling mission assurance through effective risk management. This blog summarizes the study and its key findings.

## What Is Zero Trust?

Zero trust is a term that describes [a cybersecurity strategy that eliminates implicit trust based on network location and requires strict identity verification, device validation, and continuous monitoring for every access request to resources](https://csrc.nist.gov/pubs/sp/800/207/final). Each request to access computing resources must be authenticated dynamically before access is granted.

Applying zero trust principles and concepts allows an organization to shift its focus from a perimeter-focused security perspective to a proactive, data-centric strategy. This shift provides several benefits, including reducing a system’s attack surface, enhancing threat detection and response capabilities, improving resilience, and adapting to modern work environments while also addressing data protection and compliance requirements.

Zero trust is based on the core concept that all networks are potentially compromised, so no entity should be trusted without verification. This philosophy runs counter to traditional cybersecurity practices and assumptions. As a result, zero trust represents a paradigm shift from the traditional cybersecurity strategy. The transition to zero trust likely will be incremental and iterative, requiring thoughtful change management and continuous monitoring.

Zero trust principles should be included with basic security principles to provide a foundation for developing, operating, and maintaining secure systems and protecting data. Security principles codify fundamental guidelines that shape how systems, applications, and processes are designed and managed to ensure they are protected against threats and vulnerabilities.

Security and zero trust principles help to ensure that systems are protected against threats and vulnerabilities, comply with applicable laws and regulations, and are able to complete their missions. Strategies for implementing security principles must evolve to address the dynamic nature of today’s cyber landscape.

## No User or Device Is Trustworthy By Default

The traditional cybersecurity approach for EIT environments employs measures and technologies to protect an organization’s systems and networks from unauthorized access by establishing a secure boundary between internal and external networks. Once attackers breach perimeter security controls and gain access to an organization’s infrastructure, [they can traverse the infrastructure’s systems and networks with relative ease](https://dodcio.defense.gov/Portals/0/Documents/Library/ZeroTrustOverlays.pdf).

The movement to a zero trust philosophy can significantly reduce this risk, but it also changes how an organization implements its cybersecurity strategy.

## SEI Zero Trust Study

Security and zero trust principles were primarily designed for general-purpose computing systems, such as those found in EIT environments. As part of this study, we explored how to tailor EIT-focused cybersecurity and zero trust principles to weapon system platforms that must meet stringent real-time performance requirements. We focused on accepted security and zero trust principles, including the following:

* Saltzer and Schroeder’s design principles for computer security [[Saltzer 1975, Pages 1278–1308](https://ieeexplore.ieee.org/document/1451869)]
* additional security principles defined by Saltzer and Kaashoek [[Saltzer 2009](https://doi.org/10.1016/C2009-0-20124-3)]
* DoW zero trust tenets and principles (documented in *DoD Zero Trust Reference Architecture Version 2.0*) [[DISA 2022](https://dodcio.defense.gov/Portals/0/Documents/Library/%28U%29ZT_RA_v2.0%28U%29_Sep22.pdf)]
* DoW strategic zero trust principles (documented in *DoD Zero Trust Strategy*) [[DoD 2022](https://dodcio.defense.gov/Portals/0/Documents/Library/DoD-ZTStrategy.pdf)]

We reviewed principles from the above sources and selected the following well-established principles to analyze in detail:

1. never trust, always verify
2. presume breach
3. least privilege
4. scrutinize explicitly
5. fail-safe defaults
6. complete mediation
7. open design
8. separation of privilege
9. minimize secrets

We made these selections after conducting a literature review of relevant publications containing principles that are generally considered to be applicable to zero trust. The ordering of the principles is designed to facilitate the presentation of the study’s results and does not reflect their priority or level of impact. The remainder of this blog summarizes our analysis of the selected security and zero trust principles, including the tradeoff challenges they present. The details of our study can be found in the SEI special report, [*Tailoring Security and Zero Trust Principles to Weapon System Environme...