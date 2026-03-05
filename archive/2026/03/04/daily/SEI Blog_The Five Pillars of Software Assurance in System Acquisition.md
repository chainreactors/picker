---
title: The Five Pillars of Software Assurance in System Acquisition
url: https://www.sei.cmu.edu/blog/the-five-pillars-of-software-assurance-in-system-acquisition/?utm_source=blog&utm_medium=rss&utm_campaign=my_site_updates
source: SEI Blog
date: 2026-03-04
fetch_date: 2026-03-05T04:07:35.545828
---

# The Five Pillars of Software Assurance in System Acquisition

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

Search

Mobile Menu

[# SEI Blog](/blog/)

1. [Home](/)
2. [Publications](/publications/)
3. [Blog](/blog/)
4. The Five Pillars of Software Assurance in System Acquisition

[ ]

### Cite This Post

×

* [AMS](#amsTab)
* [APA](#apaTab)
* [Chicago](#chicagoTab)
* [IEEE](#ieeeTab)
* [BibTeX](#bibTextTab)

AMS Citation

Woody, D., Alberts, C., Bandor, M., and Chick, T., 2026: The Five Pillars of Software Assurance in System Acquisition. Carnegie Mellon University, Software Engineering Institute's Insights (blog), Accessed March 4, 2026, https://doi.org/10.58012/r8q1-zp76.

Copy

APA Citation

Woody, D., Alberts, C., Bandor, M., & Chick, T. (2026, March 4). The Five Pillars of Software Assurance in System Acquisition. Retrieved March 4, 2026, from https://doi.org/10.58012/r8q1-zp76.

Copy

Chicago Citation

Woody, Dr. Carol, Christopher Alberts, Michael Bandor, and Timothy A. Chick. "The Five Pillars of Software Assurance in System Acquisition." *Carnegie Mellon University, Software Engineering Institute's Insights (blog)*. Carnegie Mellon's Software Engineering Institute, March 4, 2026. https://doi.org/10.58012/r8q1-zp76.

Copy

IEEE Citation

D. Woody, C. Alberts, M. Bandor, and T. Chick, "The Five Pillars of Software Assurance in System Acquisition," *Carnegie Mellon University, Software Engineering Institute's Insights (blog)*. Carnegie Mellon's Software Engineering Institute, 4-Mar-2026 [Online]. Available: https://doi.org/10.58012/r8q1-zp76. [Accessed: 4-Mar-2026].

Copy

BibTeX Code

@misc{woody\_2026,
author={Woody, Dr. Carol and Alberts, Christopher and Bandor, Michael and Chick, Timothy A.},
title={The Five Pillars of Software Assurance in System Acquisition},
month={{Mar},
year={{2026},
howpublished={Carnegie Mellon University, Software Engineering Institute's Insights (blog)},
url={https://doi.org/10.58012/r8q1-zp76},
note={Accessed: 2026-Mar-4}
}

Copy

# The Five Pillars of Software Assurance in System Acquisition

![Headshot of Dr. Carol Woody.](/media/images/Woody_Carol_137_240924.360x360.max-180x180.format-webp.webp)
![Headshot of Christopher Alberts.](/media/images/thumb_big_c-alberts_blog_author.max-180x180.format-webp.webp)

###### [Dr. Carol Woody](/authors/carol-woody), [Christopher J. Alberts](/authors/christopher-alberts), [Michael S. Bandor](/authors/michael-bandor), and [Timothy A. Chick](/authors/timothy-chick)

###### March 4, 2026

##### PUBLISHED IN

[Secure Development](/blog/topics/secure-development/)

##### CITE

<https://doi.org/10.58012/r8q1-zp76>

Get Citation

##### SHARE

Today’s systems are increasingly software-intensive and complex with a growing reliance on third-party technology. Through software reuse, systems can be assembled faster with less development cost. Traditionally, systems were primarily hardware-driven, and operational risks were primarily linked to reliability. Now systems are largely software-based. They do not wear out like hardware, so critical risks are different. Software components almost without exception contain vulnerabilities that are difficult to manage directly. Inheritance of these vulnerabilities through the supply chain, as more software is acquired, increases the management challenges and magnifies the risk of potential compromise. In addition, we have seen situations where suppliers unintentionally become propagators of malware and ransomware (e.g., SolarWinds) through features that provide automatic updates. Attacks on the software supply chain (e.g., [Shai-Hulud](https://www.microsoft.com/en-us/security/blog/2025/12/09/shai-hulud-2-0-guidance-for-detecting-investigating-and-defending-against-the-supply-chain-attack/), a self-replicating worm) are increasingly frequent and devastating.

The acquisition and operation of a system with effective software assurance requires effective software risk management throughout the lifecycle to identify and mitigate potential mission impacts. As detailed in this post, through decades of experience in working with programs across government and industry, our team of researchers in cybersecurity, acquisition, and system and software engineering have identified five foundational capabilities (pillars) that must be well established to support the acquisition of a system with effective software assurance: Software Requirements, Software Supply Chain Risk Management, Software Quality, System Integration, and Software Metrics. These pillars address inconsistencies, mistakes, and disconnects in today’s software management that represent risks to mission success. Cyber threat actors take advantage of the available gaps and potential errors in a system’s design, software, hardware, firmware, and supply chain to bypass controls and leverage software vulnerabilities in their attacks.

These gaps often include improper assumptions about how protections will perform when communications and data sharing occur among the various software and hardware components of the system. There are also gaps in the control of contents of data packets. Further misunderstandings occur when designs are created for hardware, but the resulting function is handled by software that may have inherent vulnerabilities. Complex software integrations are assembled from existing components and language libraries that are reused to perform similar actions but may not be built to specification. Additionally, reused components may include unexpected capabilities and attack surfaces that permit unacceptable behaviors that attackers can leverage.

Current system risk analysis approaches focus primarily within the boundaries of a system and encourage designing strong protections for critical assets, often largely ignoring other parts of the system. Security analysts often ignore the role of software in linking internal and external system components. Attackers will leverage third-party software, language libraries, open source, and firmware as a conduit into a target system. Connections from external systems are another avenue of risk. Attacks can be launched from less protected but connected systems, infrastructure, cloud and monitoring services, and other trusted external sources. System sustainment processes such as patching and technology refresh can be yet another means of invading a target system if effective risk management practices are not in place. The lag in implementation of both first-party and third-party software updates to reduce vulnerabilities further complicates the coordination across system components, leaving gaps that are valuable to attackers. Effective implementation of processes and practices within the five pillars can mitigate these risks.

## Research Addressing Software Assurance

The financial impact from the exploitation of software defects has grown from [an estimated $60 billion impact annually on the U.S. economy in 2002](https://www.abeacha.com/NIST_press_release_bugs_cost.html) to the $26 billion-a-day global impact on today’s economy, as noted by Yair Levy at a 2025 Cybersecurity Awareness Month Lunch & Learn, Webinar at the Center for Information Protection, Education, and Research (CIPhER), Nova Southeastern University. Efforts to address information protection risk are based largely on principles established in 1974 by Saltzer and Schroeder, but the technology context at that time was centralized mainframes, not the highly-distributed, networked, software-dependent present-day systems. Many of these original principles still hold true, but they do not address current aspects of the operational context and the related software risks. A [broader set of principles was published in 2013](https://www.irma-international.org/viewtitle/76352/?isxn=9781466631113) by researchers at the SEI and University of Detroit Mercy to include the more recent challenges of assuring ...