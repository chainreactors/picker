---
title: Implementing Zero Trust in Operational Technology: A Practical Case Study
url: https://www.sei.cmu.edu/blog/implementing-zero-trust-in-operational-technology-a-practical-case-study/?utm_source=blog&utm_medium=rss&utm_campaign=my_site_updates
source: SEI Blog
date: 2026-06-16
fetch_date: 2026-06-17T07:04:04.054768
---

# Implementing Zero Trust in Operational Technology: A Practical Case Study

icon-carat-right

menu

search

cmu-wordmark

[Carnegie Mellon University

cmu-wordmark](https://www.cmu.edu)

About

Research and Development

Publications and Media

Education

Careers

Search

Mobile Menu

[# SEI Blog](/blog/)

1. [Home](/)
2. [Publications and Media](/publications-media/)
3. [Blog](/blog/)
4. Implementing Zero Trust in Operational Technology: A Practical Case Study

[ ]

### Cite This Post

×

* [AMS](#amsTab)
* [APA](#apaTab)
* [Chicago](#chicagoTab)
* [IEEE](#ieeeTab)
* [BibTeX](#bibTextTab)

AMS Citation

Brown, R., 2026: Implementing Zero Trust in Operational Technology: A Practical Case Study. Software Engineering Institute blog, Accessed June 17, 2026, https://doi.org/10.58012/6eyx-5204.

Copy

APA Citation

Brown, R. (2026, June 16). Implementing Zero Trust in Operational Technology: A Practical Case Study. Retrieved June 17, 2026, from https://doi.org/10.58012/6eyx-5204.

Copy

Chicago Citation

Brown, Rhonda. "Implementing Zero Trust in Operational Technology: A Practical Case Study." *Software Engineering Institute blog*. Carnegie Mellon's Software Engineering Institute, June 16, 2026. https://doi.org/10.58012/6eyx-5204.

Copy

IEEE Citation

R. Brown, "Implementing Zero Trust in Operational Technology: A Practical Case Study," *Software Engineering Institute blog*. Carnegie Mellon's Software Engineering Institute, 16-Jun-2026 [Online]. Available: https://doi.org/10.58012/6eyx-5204. [Accessed: 17-Jun-2026].

Copy

BibTeX Code

```
@misc{brown_2026,
author={Brown, Rhonda},
title={Implementing Zero Trust in Operational Technology: A Practical Case Study},
month={Jun},
year={2026},
institution={Software Engineering Institute blog},
doi={10.58012/6eyx-5204},
url={https://doi.org/10.58012/6eyx-5204},
note={Accessed: 2026-Jun-17}
}
```

Copy

# Implementing Zero Trust in Operational Technology: A Practical Case Study

![Headshot of Rhonda Brown.](/media/images/thumb_big_r-brown_blog_authors_.max-180x180.format-webp.webp)

###### [Rhonda Brown](/authors/rhonda-brown)

###### June 16, 2026

##### PUBLISHED IN

[Secure Development](/blog/topics/secure-development/)

##### CITE

<https://doi.org/10.58012/6eyx-5204>

Get Citation

##### TAGS

[Zero Trust](/blog/tags/zero-trust)

##### SHARE

While zero trust guidance for enterprise information technology (EIT) systems is well established, its direct application to operational technology (OT) environments is problematic due to fundamental differences in system architecture and operational priorities. Zero trust frameworks tailored to the unique requirements of OT systems are just beginning to emerge. The Software Engineering Institute (SEI) is pioneering research into the application of zero trust principles within weapon system environments with embedded OT. In this blog post, we explore a specific case study and examine how findings from our research on weapon systems driven by embedded OT translate to the broader OT landscape.

Zero trust is an evolving set of cybersecurity paradigms that move defenses from static, network-based perimeters to a focus on users, assets, resources, and flows within an enclave. Zero trust assumes there is no implicit trust granted to assets or user accounts based solely on their physical or network location.

In our research, we identified opportunities for zero trust integration in weapons systems OT by analyzing how the core concepts of foundational security principles—originally developed for EIT—can fit the unique OT landscape. The initiative stems from a recognized need among Department of War (DoW) stakeholders for guidance in this area.

The preliminary phase of our work involved a comprehensive examination of foundational security paradigms and zero trust principles to determine their applicability to the unique requirements of weapon systems. The findings of this work were published in the paper [*Tailoring Security and Zero Trust Principles to Weapons System Environments*](https://www.sei.cmu.edu/library/tailoring-security-and-zero-trust-principles-to-weapon-system-environments/).

Utilizing the insights from the DoW’s recently published guidance [*Zero Trust for Operational Technology*](https://dodcio.defense.gov/Portals/0/Documents/Library/ZT-OperationalTechnologyActivitiesOutcomes_v2.pdf), we are continuing to tailor and adapt zero trust concepts to address OT concerns in weapon systems. Weapon systems can be considered a specific application of OT, and as such, our findings will offer valuable insights to help advance the implementation of cybersecurity in a zero trust framework across the broader OT domain. Weapon systems, like other OT domains, must meet stringent real-time performance requirements that can’t be met with standard, IT-focused principles. We use our weapon systems analysis to help define the practical boundaries needed to protect complex OT environments.

## Securing the Grid: The Commerce Energy Case Study

To illustrate our points in this blog post, we use a case study focused on the digital substations of Commerce Energy, a fictional utility firm. A substation is a part of the broader generation, transmission, and distribution system that has the function of stepping down high-voltage levels from the transmission system (bulk power) to feed more local distribution circuits in response to the dynamic demands of homes and small businesses. A typical substation governs the protection, monitoring, and automation of all transformers and breakers directly involved in transporting bulk electricity.

Commerce Energy’s automatic control systems manage subsystem data and communicate with intelligent electronic devices (IEDs), relays, and other equipment. A web-based human-machine interface (HMI) is used to support human operators for local and remote monitoring, control, and annunciation for substations and other processes. The Supervisory Control and Data Acquisition (SCADA) system provides high-level views for monitoring overall grid stability and power flow and managing switching operations in substations.

Controls for Commerce Energy’s substations are organized into distinct levels following the [Purdue model](https://www.sans.org/blog/introduction-to-ics-security-part-2), which enables Commerce Energy’s substation communications to be structurally compartmentalized. Commerce Energy relies on these isolated enclaves at each level, where traffic is restricted through segmentation and access controls. While these controls have been effective to date, in our scenario the rising risks to critical infrastructure are prompting new concerns: lateral movement, the integrity of signals being sent to control devices, the actual security posture of their remote connections, and compromised devices they may already have in the system. There are also concerns about potential “blind spots” within their older equipment. Seeking to reinforce its defenses, Commerce Energy is considering a zero trust initiative, starting with a threat analysis.

[![figure1_06152026](/media/images/figure1_06152026.max-1280x720.format-webp.webp)](/media/images/figure1_06152026.original.png)

Figure 1: Commerce Energy OT Network Architecture

## Critical Concerns in Securing Operational Technology

Critical infrastructure, more generally, is battling a full, evolving range of cyber and physical dangers, from systemic weaknesses to sophisticated nation-state sabotage. The dangers include intentional threats (hacktivists, organized crime), insider threats, and accidental, negligent, or natural hazards. To help make informed decisions for zero trust defenses, the [Cloud Security Alliance (CSA) recently published guidelines for applying zero trust principles within unique operational technology (OT) systems](https://cloudsecurityalliance.org/artifacts/zero-trust-guidance-for-critical-infrastructure). The CSA guidance highlights the main drivers behind malicious interest in OT:

1. **Regulatory and Compliance Pressure** that may not align with effective cyberse...