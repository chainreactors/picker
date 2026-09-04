---
title: CRA Reporting – What you need to know
url: https://blog.compass-security.com/2026/09/cra-reporting-what-you-need-to-know/
source: Over Security
date: 2026-09-03
fetch_date: 2026-09-04T06:43:49.204369
---

# CRA Reporting – What you need to know

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

# [CRA Reporting – What you need to know](https://blog.compass-security.com/2026/09/cra-reporting-what-you-need-to-know/ "CRA Reporting – What you need to know")

[September 3, 2026](https://blog.compass-security.com/2026/09/cra-reporting-what-you-need-to-know/ "CRA Reporting – What you need to know")
 /
[Andreas Brombach](https://blog.compass-security.com/author/abrombach/)
 /
[0 Comments](https://blog.compass-security.com/2026/09/cra-reporting-what-you-need-to-know/#respond)

While the full implementation of the Cyber Resilience Act (CRA) won’t take effect until December 2027, another critical milestone is already approaching much sooner. Starting from **11 September 2026**, all manufacturers selling products with digital elements in countries of the European Union will be required to report actively exploited vulnerabilities in their digital products, as well as related security incidents, as well as security incidents that affect or compromise products already placed on the market.

Incidents or vulnerabilities limited to development or internal environments are therefore only relevant if they result in (or *could* result in) a compromise of production devices.

Although the platform itself is not yet available, the landmark legislation has already established a detailed framework and set of requirements. This article aims to summarize the most important aspects of the reporting process in order to help you prepare for these upcoming changes. Additionally, it provides clear guidelines for determining when a vulnerability or incident becomes mandatory to report.

## Overview

In Chapter I, Article 14, §1, the Cyber Resilience Act states the following:

> A manufacturer shall notify any actively exploited vulnerability contained in the product with digital elements that it becomes aware of simultaneously to the CSIRT designated as coordinator, in accordance with paragraph 7 of this Article, and to ENISA.

In the context of the CRA, an “*actively exploited vulnerability*” is defined as a *“vulnerability for which there is reliable evidence that it has been abused by a malicious actor in a system without permission of the system’s owner.”*

Put simply, manufacturers must publish a public report as soon as they become aware of a vulnerability in their products being actively abused. This could be, for example, a flaw in the authentication mechanism that allows attackers to access or modify data of other users.

Security incidents affecting a manufacturer’s development, production, or maintenance processes (e.g., a compromise of the software update release channel) must also be addressed in the same way. An example scenario would consist of attackers being able to compromise the firmware repository, inject malicious code into the system, which is then transferred and executed on users’ devices.

However, if a vulnerability is instead discovered during a security audit, internal inspections or other non-malicious means, it does **not** fall under mandatory reporting.

Reports must be submitted via a centralized reporting platform to the national CSIRT (Computer Security Incident Response Team) as well to ENISA, the European Union Agency for Cybersecurity.

## When to report a vulnerability?

The process begins the moment a vulnerability is discovered in a product with digital elements, whether identified internally or via an external notification. Whether or not mandatory reporting is required is determined by the following decision logic:

[![](https://blog.compass-security.com/wp-content/uploads/2026/08/Untitled-Diagram8.drawio1-1024x966.png)](https://blog.compass-security.com/wp-content/uploads/2026/08/Untitled-Diagram8.drawio1.png)

The process starts as soon as a possible a flaw is identified, either by the manufacturer themself or by an external party.

1. **Is it exploitable?** A manufacturer must first determine if the vulnerability can effectively be abused by malicious actors under practical operational conditions. If it cannot be exploited in practice (for example, if it only exists in a controlled testing environment), reporting is not required.
2. **Is it actively exploited?** If the vulnerability is exploitable under practical conditions, manufacturers must look for evidence of abuse.
3. **Is there reliable evidence that it has been exploited by malicious actors?**
   **NO:** Reporting is not required.
   **YES:** Reporting is mandatory under the CRA.

Even if reporting is not mandatory, either because the vulnerability is not exploitable or no evidence of abuse was found, vendors may still choose to submit a voluntary report. The CRA guarantees that voluntary reporting will not impose any additional legal obligations on the vendor in this case.

## When to report a security incident?

[![](https://blog.compass-security.com/wp-content/uploads/2026/08/Untitled-Diagram8.drawio-1024x821.png)](https://blog.compass-security.com/wp-content/uploads/2026/08/Untitled-Diagram8.drawio.png)

According to the CRA, any “*severe incident having an impact on the security of the product with digital elements*” is subject to mandatory reporting.

Generally, an “*incident*” is defined as “*any event that compromises the availability, authenticity, integrity or confidentiality of either stored, transmitted, or processed data, or of the services offered by, or accessible via, network and information systems*“. In other words, any event that disrupts, modifies or steals information or services is regarded as an incident.

The additional description *“having an impact on the security of the product with digital elements*” focuses strictly on a specific product. Instead of the company itself, the CRA only covers security incidents that directly affect the digital product in such a way that it is no longer able to keep sensitive data and its functions secure, reliable and private.

Finally, a security incident is categorized as *severe* if it falls into one of the following two scenarios:

* The product is no longer able to protect sensitive data or important functions.
* Attackers are able to execute malicious code on the product itself or use the device to execute malicious code on the user’s network.

At Compass Security, we interpret sensitive data as data where a compromise has meaningful security consequences, for example logon information, authentication secrets, cryptographic keys, personal data, confidential user data, security configuration or similarly protected information.

Important functions are those whose loss or manipulation would have a significant impact on the product or its security. Examples include access control, firmware verification, safety-related controls, configuration management, communication and the availability of core services and other essential product functionality.

## The Reporting Process

The reporting process consists of three stages, triggered immediately after a manufacturer becomes aware of an exploited vulnerability or a severe security incident.

[![](https://blog.compass-security.com/wp-content/uploads/2026/08/TIMELINE.drawio1-1024x171.png)](https://blog.compass-security.com/wp-content/uploads/2026/08/TIMELINE.drawio1.png)

**Early Warning**
As soon as an exploited vulnerability or an incident becomes known, an early warning must be submitted within **24 hours**. While technical details are not required at this stage, the countries...