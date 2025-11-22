---
title: How to Align Security Requirements and Controls to Express System Threats
url: https://www.sei.cmu.edu/blog/how-to-align-security-requirements-and-controls-to-express-system-threats/?utm_source=blog&utm_medium=rss&utm_campaign=my_site_updates
source: SEI Blog
date: 2025-11-21
fetch_date: 2025-11-22T03:08:39.482114
---

# How to Align Security Requirements and Controls to Express System Threats

icon-carat-right

menu

search

cmu-wordmark

[Carnegie Mellon University](https://www.cmu.edu)

[Software Engineering Institute](https://www.sei.cmu.edu)

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
4. How to Align Security Requirements and Controls to Express System Threats

[ ]

### Cite This Post

×

* [AMS](#amsTab)
* [APA](#apaTab)
* [Chicago](#chicagoTab)
* [IEEE](#ieeeTab)
* [BibTeX](#bibTextTab)

AMS Citation

Miller, E., and Sisk, M., 2025: How to Align Security Requirements and Controls to Express System Threats. Carnegie Mellon University, Software Engineering Institute's Insights (blog), Accessed November 21, 2025, https://doi.org/10.58012/gb66-6518.

Copy

APA Citation

Miller, E., & Sisk, M. (2025, November 21). How to Align Security Requirements and Controls to Express System Threats. Retrieved November 21, 2025, from https://doi.org/10.58012/gb66-6518.

Copy

Chicago Citation

Miller, Elias, and Matthew Sisk. "How to Align Security Requirements and Controls to Express System Threats." *Carnegie Mellon University, Software Engineering Institute's Insights (blog)*. Carnegie Mellon's Software Engineering Institute, November 21, 2025. https://doi.org/10.58012/gb66-6518.

Copy

IEEE Citation

E. Miller, and M. Sisk, "How to Align Security Requirements and Controls to Express System Threats," *Carnegie Mellon University, Software Engineering Institute's Insights (blog)*. Carnegie Mellon's Software Engineering Institute, 21-Nov-2025 [Online]. Available: https://doi.org/10.58012/gb66-6518. [Accessed: 21-Nov-2025].

Copy

BibTeX Code

@misc{miller\_2025,
author={Miller, Elias and Sisk, Matthew},
title={How to Align Security Requirements and Controls to Express System Threats},
month={{Nov},
year={{2025},
howpublished={Carnegie Mellon University, Software Engineering Institute's Insights (blog)},
url={https://doi.org/10.58012/gb66-6518},
note={Accessed: 2025-Nov-21}
}

Copy

# How to Align Security Requirements and Controls to Express System Threats

![Headshot of Matthew Sisk.](/media/images/thumb_big_m-sisk_blog_authors_5.max-180x180.format-webp.webp)

###### [Elias Miller](/authors/elias-miller) and [Matthew Sisk](/authors/matthew-sisk)

###### November 21, 2025

##### PUBLISHED IN

[Cybersecurity Engineering](/blog/topics/cybersecurity-engineering/)

##### CITE

<https://doi.org/10.58012/gb66-6518>

Get Citation

##### SHARE

Threats and how we counter them have become key considerations in a system’s cybersecurity architecture and design. This applies whether we are designing a new system, addressing regulatory requirements to operate in a particular mission environment, or just working to meet organizational needs. Adoption of zero trust strategies, security by design guidance, and DevSecOps are core to a system's cybersecurity architecture and design in both the public and private sector.

In this blog post, we discuss a method that combines information about security requirements, controls, and capabilities with analysis regarding cyber threats to enable more effective risk-guided system planning. In plain language, it’s a way of creating a crosswalk from system and security requirements to threats. To adhere to already established federal government policies and guidelines while maintaining alignment with industry standards, we used four primary types of data:

* **Defense Information Systems Agency (DISA)** [Control Correlations Identifiers (CCIs)](https://www.dau.edu/acquipedia-article/control-correlation-identifier-cci) are used to express individual technical or procedural requirements and how they connect to higher-level control objectives. CCIs are identified with unique codes (e.g., CCI-000015) which are maintained by DISA. This creates an ability to trace security requirements from their origin (e.g., regulations, information assurance frameworks) to low-level implementation choices, allowing organizations to readily demonstrate compliance with multiple information assurance frameworks. They are primarily used by DoW agencies and contractors, but they are good for many activities that are common across other sectors, such as compliance tracking, auditing and reporting, and standardization. CCIs are mapped to multiple regulatory frameworks as well, which allows us to objectively roll up and compare related compliance assessment results across disparate technologies. If you work with [Security Technical Implementation Guides](https://www.cyber.mil/stigs) (STIGs) or NIST compliance frameworks, it is likely you’ll encounter and use CCIs.
* **National Institute of Standards and Technology (NIST) Security and Privacy Controls for Information Systems and Organizations (SP 800-53**) standardizes security and privacy safeguards for information systems. This publication details controls that are designed to protect the confidentiality, integrity, and availability of information systems. The control standards are flexible and approach security with a risk-based focus. Due to its wide use in the government as well as industry for defining security requirements for information systems and auditing them, it is a great baseline source for best practices.
* **The** [**MITRE ATT&CK**](https://attack.mitre.org/) **Framework** is used heavily to abstract the behavior of threat actors in a way that makes information sharing possible, allows behavior emulation for internal training, and creates opportunity for systems architects and security practitioners to apply strategic investments for the protection of interconnected systems. The framework is used in many products and applications across industries, and specific matrices have been created for industrial control systems, mobile devices, and enterprise systems. In this work we primarily focus on the enterprise matrix because it is the most similar to the environments that we developed this method for.
* **MITRE Detection, Denial, and Disruption Framework Empowering Network Defense (**[**D3FEND**](https://d3fend.mitre.org/resources/)**) Countermeasures** act as a complement to the MITRE ATT&CK Framework. This recently developed ontology provides a descriptive language for cybersecurity capabilities, primarily targeted at the defender’s perspective, and a method for relating ATT&CK TTPs to D3FEND through semantic connections. To support use of the ontology, MITRE developed many resources that show connections to D3FEND and allow for the development of tools like their D3FEND Profile Studio and D3FEND CAD. These tools enable modeling of D3FEND, which allows us to express the cyber terrain of interest in a manner that connects it to the potential threats of interest.

Beyond the requirements for the data, we sought to make our approach a repeatable process to provide actionable information for leaders and analysts at the strategic, operational, and tactical levels of an organization.

## Relationships and Linkages Between Data Sources

The data sources we have used so far tend to share at least some commonalities (i.e., keys where we can merge the data to gain new insights). These keys are not often exactly aligned. As noted, our work primarily utilizes the MITRE datasets for ATT&CK and D3FEND, including their references to CCI and STIG data.

Both the ATT&CK and D3FEND data are represented computationally, in both cases using monolithic JSON files: ATT&CK is a knowledge base implemented in STIXv2 format, and the D3FEND data is an ontology structured as a graph network with semantic information about the relationship type between nodes. There is a CSV of D3FEND that we used to programmatically correlate CCIs and 800-53 controls and to enable visual inspection of the mappings along the way.

[![11212025_figure1](/media/images/11212025_figure1.max-1280x720.format-webp.webp)](/media/images/11212025_figure1.original.png)

Figure 1 Simplified Offensive and Defensive Technique Relat...