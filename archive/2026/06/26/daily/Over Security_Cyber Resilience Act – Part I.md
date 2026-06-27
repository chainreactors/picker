---
title: Cyber Resilience Act – Part I
url: https://blog.compass-security.com/2026/06/cyber-resilience-act-part-i/
source: Over Security
date: 2026-06-26
fetch_date: 2026-06-27T05:52:09.222600
---

# Cyber Resilience Act – Part I

## [Compass Security Blog](https://blog.compass-security.com "Compass Security Blog — Offensive Defense")

### Offensive Defense

* [Home](https://blog.compass-security.com/)
* [Archive](https://blog.compass-security.com/archive/)
* [Contact](https://blog.compass-security.com/contact/)
* [Newsletter](https://blog.compass-security.com/mailing-list-tigerinfo/)

* [Home](https://blog.compass-security.com/)
* [Archive](https://blog.compass-security.com/archive/)
* [Contact](https://blog.compass-security.com/contact/)
* [Newsletter](https://blog.compass-security.com/mailing-list-tigerinfo/)

# [Cyber Resilience Act – Part I](https://blog.compass-security.com/2026/06/cyber-resilience-act-part-i/ "Cyber Resilience Act – Part I")

[June 26, 2026](https://blog.compass-security.com/2026/06/cyber-resilience-act-part-i/ "Cyber Resilience Act – Part I")
 /
[Tobias Hort-Giess](https://blog.compass-security.com/author/thort/)
 /
[0 Comments](https://blog.compass-security.com/2026/06/cyber-resilience-act-part-i/#respond)

The Cyber Resilience Act (CRA) is a regulation introduced by the European Union to strengthen cybersecurity requirements for products with digital elements.
In simple terms, the CRA sets mandatory cybersecurity rules for hardware and software sold in the EU. This includes everything from connected devices (IoT) to operating systems and even stand-alone software. Very important, this concerns any company that wants to sell their products into the EU, regardless whether that company is based in the EU or not.
The goal is to ensure that digital products placed on the EU market are secure by design and default and remain secure over time. That also means that the CRA does not stop at the launch of a product. It covers the entire lifecycle from design and development all the way through updates and vulnerability management. It also brings everyone in the product pipeline into responsibility.

The CRA entered into force on **10 December 2024**, meaning it is already officially law in the EU, although most obligations are not yet applicable. The implementation is phased. From **11 September 2026**, companies will already need to comply with certain reporting obligations, particularly related to the notification of vulnerabilities and security incidents. From **11 December 2027**, the CRA will be fully applicable.
Also, products with digital elements that have been placed on the market before 11 December 2027 are not subject to the CRA unless, from that date, they are subject to a substantial modification. Reporting obligations apply to all products with digital elements that have been made available on the Union market, including those already placed on the market before 11 December 2027.

Preparing for the CRA is ultimately not just about interpreting legal text, but about translating regulatory expectations into concrete technical security measures. Organisations may discover early on that compliance depends on answering three fundamental questions:

* Does my product fall under CRA?
* What class does my product fall into under the CRA?
* Where do we currently stand, and what is missing to comply?

And this is where we at Compass Security can support you.

We will determine whether and how your product falls under the Cyber Resilience Act (CRA) and identify the corresponding product class. We then perform threat modelling to understand the relevant attack surfaces and risks, followed by a cybersecurity and process gap analysis.
As part of this assessment, we validate the security posture of the product through hands-on technical testing. Depending on the product and technology stack, this may include source code reviews, firmware extraction and analysis, serial protocol sniffing, reverse engineering, fuzzing, authentication and update flow analysis, and other security assessment techniques.
The goal is to identify vulnerabilities such as unsigned firmware updates, exposed debugging interfaces, insecure communication channels, and authentication or authorization bypasses in human-machine interfaces, among many others, while also evaluating the effectiveness of implemented security controls and providing actionable recommendations for achieving CRA compliance.

|  |  |  |
| --- | --- | --- |
| **Critical Class** | Security Boxes, Smart Meters, Smartcards, … | Third-party assessment |
| **Important Class II** | Hypervisors, Container Runtimes, Firewalls, IDS, … | Third-party assessment with exceptions |
| **Important Class I** | IAM, PAM, Browsers, Password Managers, Anti-Malware, VPN, OS, Network Devices, … | Self-Assessment with exceptions |
| **Default Class** | All other software and hardware products | Self-Assessment |

Classes defined by the CRA

To ensure a structured and consistent approach, we use a comprehensive set of test cases aligned with IEC 62443, a globally recognized cybersecurity framework. This standard defines Security Levels as a progressive scale describing a system’s resilience against increasingly capable attackers. Although the Cyber Resilience Act does not reference IEC 62443 or mandate the use of any particular standard or methodology for demonstrating compliance, we have chosen to use IEC 62443 because it is a widely recognized and well-established cybersecurity standard that shows significant overlap with the CRA requirements and provides a practical framework for implementation and assessment. However, the alignment is not exact in every detail, and other methodologies may be equally valid for demonstrating compliance with the CRA.

|  |  |
| --- | --- |
| **Security Level** | **Description** |
| SL0 | No meaningful security measures are in place. The system has no intentional protection against attacks and is effectively exposed. |
| SL1 | Provides basic protection against accidental misuse or very simple, opportunistic attacks. Security measures are minimal and not designed to resist targeted attackers. |
| SL2 | Protects against intentional attacks using simple means by individuals with limited resources and skills. Introduces foundational and structured security controls. |
| SL3 | Protects against sophisticated, targeted attacks from adversaries with advanced knowledge, tools, and resources. Requires strong controls such as robust authentication, segmentation, and system hardening. |
| SL4 | Highest defined security level, designed to withstand highly sophisticated and well-resourced attacks, including organized criminal groups or state-sponsored threat actors. |

Security levels based on IEC 62443

Our assessment can be conducted in two ways. In the first mode, we define a target Security Level upfront and perform a focused gap analysis against it. This identifies missing controls and produces prioritized remediation measures to help the organization reach the desired level efficiently.
In the second mode, we conduct a holistic assessment without a predefined target. Instead, we evaluate the current maturity across all relevant IEC 62443 test cases, resulting in a complete security profile that includes the achieved Security Level as well as a clear view of weaknesses and improvement opportunities.
All findings are consolidated into a structured report, ensuring you are not left empty handed when the CRA comes into force, but instead have a proof of process and a clear understanding of your current security posture and the required next steps.

[![](https://blog.compass-security.com/wp-content/uploads/2026/05/image-17-1024x760.png)](https://blog.compass-security.com/wp-content/uploads/2026/05/image-17.png)

Excerpt from an example report

Stay tuned for Part II, where we will demonstrate this process in a realistic scenario…

## References

<https://digital-strategy.ec.europa.eu/en/policies/cra-summary>

[Automation](https://blog.compass-security.com/category/automation/), [Industrial Control Systems](https://blog.compass-security.com/category/industrial-control-systems/), [Internet of Things](https://blog.compass-se...