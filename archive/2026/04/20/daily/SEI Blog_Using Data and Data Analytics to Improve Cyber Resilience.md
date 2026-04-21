---
title: Using Data and Data Analytics to Improve Cyber Resilience
url: https://www.sei.cmu.edu/blog/using-data-and-data-analytics-to-improve-cyber-resilience/?utm_source=blog&utm_medium=rss&utm_campaign=my_site_updates
source: SEI Blog
date: 2026-04-20
fetch_date: 2026-04-21T04:51:45.365999
---

# Using Data and Data Analytics to Improve Cyber Resilience

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
4. Using Data and Data Analytics to Improve Cyber Resilience

[ ]

### Cite This Post

×

* [AMS](#amsTab)
* [APA](#apaTab)
* [Chicago](#chicagoTab)
* [IEEE](#ieeeTab)
* [BibTeX](#bibTextTab)

AMS Citation

Bulisco, P., 2026: Using Data and Data Analytics to Improve Cyber Resilience. Carnegie Mellon University, Software Engineering Institute's Insights (blog), Accessed April 20, 2026, https://www.sei.cmu.edu/blog/using-data-and-data-analytics-to-improve-cyber-resilience/.

Copy

APA Citation

Bulisco, P. (2026, April 20). Using Data and Data Analytics to Improve Cyber Resilience. Retrieved April 20, 2026, from https://www.sei.cmu.edu/blog/using-data-and-data-analytics-to-improve-cyber-resilience/.

Copy

Chicago Citation

Bulisco, Patsy. "Using Data and Data Analytics to Improve Cyber Resilience." *Carnegie Mellon University, Software Engineering Institute's Insights (blog)*. Carnegie Mellon's Software Engineering Institute, April 20, 2026. https://www.sei.cmu.edu/blog/using-data-and-data-analytics-to-improve-cyber-resilience/.

Copy

IEEE Citation

P. Bulisco, "Using Data and Data Analytics to Improve Cyber Resilience," *Carnegie Mellon University, Software Engineering Institute's Insights (blog)*. Carnegie Mellon's Software Engineering Institute, 20-Apr-2026 [Online]. Available: https://www.sei.cmu.edu/blog/using-data-and-data-analytics-to-improve-cyber-resilience/. [Accessed: 20-Apr-2026].

Copy

BibTeX Code

@misc{bulisco\_2026,
author={Bulisco, Patsy},
title={Using Data and Data Analytics to Improve Cyber Resilience},
month={{Apr},
year={{2026},
howpublished={Carnegie Mellon University, Software Engineering Institute's Insights (blog)},
url={https://www.sei.cmu.edu/blog/using-data-and-data-analytics-to-improve-cyber-resilience/},
note={Accessed: 2026-Apr-20}
}

Copy

# Using Data and Data Analytics to Improve Cyber Resilience

![Headshot of Patsy Bulisco](/media/images/Bulisco_Pat_540_240530.max-180x180.format-webp.webp)

###### [Patsy Bulisco](/authors/patsy-bulisco)

###### April 20, 2026

##### PUBLISHED IN

[Enterprise Risk and Resilience Management](/blog/topics/enterprise-risk-and-resilience-management/)

##### CITE

Get Citation

##### SHARE

According to IBM’s [*Cost of a Data Breach 2025* report](https://www.ibm.com/reports/data-breach), the average cost of a corporate data breach in the United States was $10.22 million, up 9 percent from 2024, due to higher regulatory fines and detection and escalation costs. Data breaches disrupt operations, often resulting in loss of data, harm to organizational reputation, fines, and significant costs to restore systems and recover.

Data breaches remind us of the importance of [cyber resilience](https://www.sei.cmu.edu/enterprise-risk-and-resilience-management/) as an essential element of survivability and continuity of operations for all organizations, especially those operating mission-essential systems, high-value systems, and/or critical assets. Resilience is also critical to reducing the costs associated with security breaches as well as minimizing damage to mission-essential systems caused by adverse events. This post highlights an approach to using data analytics as a “force multiplier” for cyber resilience, and it suggests best practices to help organizations gain situational awareness on their current security posture. It also provides guidance for tailoring resilience efforts to enhance an organization’s ability to anticipate, withstand, recover from, and adapt to evolving threats.

## A Practical Approach to Cyber Resilience

Cybersecurity is often thought of as keeping the attackers out or simply stopping an attack. Framing the problem in all-or-nothing terms accepts unbounded risk and consequence once a boundary is breached. A resilience-focused approach helps organizations develop the ability to anticipate, withstand, recover from, and adapt to adverse events. Standard practices such as configuring security settings, undertaking periodic vulnerability scans, and timely patch management address obvious weaknesses. But these measures alone do not constitute a sufficient or unified approach to cybersecurity. An inconsistent implementation of security controls often requires security administrators to rely on experience over formal guidance as well as cycles of preparation driven by inspections or audits. Organizational leaders should instead work to develop a structured hardening framework to push security efforts toward a consistent, proactive approach. This blog post illustrates how a diverse array of existing guidelines and resources can be brought to bear to enhance resilience.

The Defense Information Systems Agency (DISA) has published [Security Technical Implementation Guides (STIGs)](https://www.cyber.mil/stigs) and [Security Requirement Guides (SRGs)](https://www.cyber.mil/stigs), These provide an important step to address the gap. The STIGs provide detailed guidance for the configuration of applications, databases, operating systems, and network devices, while SRGs tackle security requirement frameworks that align to federal standards. Both STIGs and SRGs are publicly available resources that have a control mapping structure aligning with [NIST SP 800-53 Security and Privacy Controls for Information Systems and Organization](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final) and [NIST SP 800-171 Protecting Controlled Unclassified Information in Nonfederal Systems and Organizations](https://csrc.nist.gov/pubs/sp/800/171/r3/final). While designed for the Department of War, these guides can help any organization develop a measurable and standardized security posture.

## Cyber Resilience Implementation: An Organizational Case Study

In this case study, an organization responsible for managing and maintaining critical infrastructure systems has been utilizing their asset inventory to identify applicable STIGs and SRGS. For purposes of this example, they use the following hardware and software and associated STIGs and SRGs:

STIG/SRG Requirements Table

| Hardware/Software | Required STIG/SRG Name |
| --- | --- |
| Windows 11 | Microsoft Windows 11 STIG |
| Mozilla Firefox Browser | Mozilla Firefox STIG |
| Microsoft Defender Endpoint | Microsoft Defender for Endpoint STIG |
| Juniper Router | Juniper Router STIG |
| Windows Defender Firewall | Windows Defender Firewall with Advanced Security STIG |
| Intrusion Detection and Prevention System | Intrusion Detection and Prevention System SRG |
| Virtual Private Network (VPN) | Virtual Private Network (VPN) SRG |
| Network Policy | Network Infrastructure Policy STIG |

[![04202026_figure1](/media/images/04202026_figure1.max-1280x720.format-webp.webp)](/media/images/04202026_figure1.original.png)

Figure 1: This figure details a high-level cybersecurity and network architecture for the organization, showing how the different systems are connected and protected across layers.

The organization downloaded the required STIGs and SRGs from the official [DoW Cyber Exchange](https://public.cyber.mil/stigs/). Additionally, they downloaded the [Security Content Automation Protocol (SCAP)](https://csrc.nist.gov/projects/security-content-automation-protocol) Compliance Checker and [STIG Viewer](https://www.cyber.mil/stigs/srg-stig-tools/) application from the same website.

* STIG Viewer Application allows users to view and manage the STIG and SRG checklists to assess and implement security controls, analyze compliance, and document findings.
* The Security Content Automation Protocol (SCAP) is a suite of “interoperable specifications for the standardized expression, exchange, and processing of security configuration and vulnerability in...