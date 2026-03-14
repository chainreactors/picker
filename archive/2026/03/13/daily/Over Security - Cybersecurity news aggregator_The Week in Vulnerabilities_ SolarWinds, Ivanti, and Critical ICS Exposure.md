---
title: The Week in Vulnerabilities: SolarWinds, Ivanti, and Critical ICS Exposure
url: https://cyble.com/cyble-weekly-vulnerability-report-feb-19/
source: Over Security - Cybersecurity news aggregator
date: 2026-03-13
fetch_date: 2026-03-14T04:14:02.015411
---

# The Week in Vulnerabilities: SolarWinds, Ivanti, and Critical ICS Exposure

[ ]

* [Products](/products/) [ ]
  + For Enterprises(B2B) and Governments [ ]
    - [Cyble Vision](https://cyble.com/products/cyble-vision/)
    - [Cyble Hawk](https://cyble.com/products/cyble-hawk/)
  + For Enterprises(B2B) and Individuals(B2C) [ ]
    - [AmIBreached](https://amibreached.com/)
    - [Cyble Odin](https://getodin.com)
    - [The Cyber Express](https://thecyberexpress.com/)
* Solutions [ ]
  + [Attack Surface Management](https://cyble.com/solutions/attack-surface-management/)
  + [Brand Intelligence](https://cyble.com/solutions/brand-intelligence/)
  + [Cyber Threat Intelligence Platform | Strengthen Security](https://cyble.com/solutions/cyber-threat-intelligence/)
  + [Dark Web Monitoring](https://cyble.com/solutions/dark-web-monitoring/)
  + [Vulnerability Management](https://cyble.com/solutions/vulnerability-management/)
  + [Takedown and Disruption](https://cyble.com/solutions/takedown-services/)
  + Solutions by Industry [ ]
    - [Healthcare & Pharmaceuticals](https://cyble.com/solutions/cyble-for-healthcare-pharmaceuticals/)
    - [Financial Services](https://cyble.com/solutions/financial-services/)
    - [Retail and CPG](https://cyble.com/solutions/cyble-for-retail-and-cpg/)
    - [Technology Industry](https://cyble.com/solutions/cyble-for-technology-industry/)
    - [Educational Platform](https://cyble.com/solutions/cyble-for-educational-platform/)
  + Solutions by Role [ ]
    - [Information Security](https://cyble.com/solutions/cyble-for-information-security/)
    - [Corporate Security](https://cyble.com/solutions/cyble-for-corporate-security/)
    - [Marketing](https://cyble.com/solutions/cyble-for-marketing/)
* Why Cyble? [ ]
  + [Compare Cyble](https://cyble.com/products/why-cyble-compare-us/)
  + [Industry Recognition](https://cyble.com/industry-recognition/)
  + [success stories](https://cyble.com/customer-stories/)
* [Resources](https://cyble.com/resources/) [ ]
  + [Blog](https://cyble.com/blog/)
  + [Events](https://cyble.com/events/)
  + [Thought Leadership](https://cyble.com/thought-leadership/)
  + [Threat Assessment](https://cyble.com/external-threat-profile-report/)
  + [SAMA Compliance](https://cyble.com/sama-compliance/)
  + [Whitepapers](https://cyble.com/whitepapers/)
* Company [ ]
  + [Our Story](https://cyble.com/about-us/)
  + [Meet Our Team Cyble](https://cyble.com/leadership-team/)
  + [Careers](https://cyble.com/careers/)
  + [Press](https://cyble.com/press/)
* Partners [ ]
  + [Cyble Partner Network (CPN)](https://partnernetwork.cyble.com/)
  + [Partner Login](https://partnercentral.cyble.com/login)
  + [Become a Partner](https://partnercentral.cyble.com/partner/registration)

Type your search query and hit enter:

All Rights Reserved

Type your search query and hit enter:

* [The Ultimate Guide to Dark Web Monitoring in 2026: Protect Your Data Before Attackers Strike](https://cyble.com/dark-web-intelligence-monitoring-guide/)

Email Address\*

* [Homepage](https://cyble.com/ "Homepage")
* [Vulnerability Management](https://cyble.com/category/vulnerability-management/ "Vulnerability Management")

Categories:  [Cyber news](https://cyble.com/category/cyber-news/ "Cyber news")[Vulnerability](https://cyble.com/category/vulnerability/ "Vulnerability")[Vulnerability Management](https://cyble.com/category/vulnerability-management/ "Vulnerability Management")

# The Week in Vulnerabilities: SolarWinds, Ivanti, and Critical ICS Exposure

February 19, 2026 7:07 am

Cyble Research & Intelligence Labs (CRIL) tracked **1,158 vulnerabilities** last week. Of these, **251 vulnerabilities already have publicly available Proof-of-Concept (PoC) exploits**, significantly increasing the likelihood of real-world attacks.

A total of **94 vulnerabilities were rated critical under CVSS v3.1**, while **43 were rated critical under CVSS v4.0**.

In parallel, CISA issued **15 ICS advisories** covering **87 vulnerabilities** affecting industrial environments. These vulnerabilities impacted vendors including Siemens, Yokogawa, AVEVA, Hitachi Energy, ZLAN, ZOLL, and Airleader.

Additionally, **8 vulnerabilities were added to CISA’s Known Exploited Vulnerabilities (KEV) catalog**, reflecting confirmed exploitation in the wild.

## **The Week’s Top Vulnerabilities**

**CVE-2025-40554 — SolarWinds Web Help Desk (Critical)**

CVE-2025-40554 is a critical [authentication](https://cyble.com/blog/multi-factor-authentication-mfa-is-a-part-of-your-cyber-hygiene/) bypass vulnerability affecting SolarWinds Web Help Desk versions prior to 2026.1. The flaw allows unauthenticated remote attackers to invoke privileged functionality without valid credentials, potentially leading to full compromise of helpdesk systems.

Cyble observed this vulnerability being discussed on underground forums shortly after disclosure, and a public PoC is available. The vulnerability’s presence in enterprise environments increases the risk of initial access and lateral movement.

**CVE-2026-1340 — Ivanti Endpoint Manager Mobile (Critical)**

CVE-2026-1340 is a critical code injection vulnerability in Ivanti [Endpoint](https://cyble.com/knowledge-hub/what-is-endpoint-security-how-it-works/) Manager Mobile (EPMM). A remote, unauthenticated attacker can exploit the flaw to achieve arbitrary remote code execution without user interaction.

The vulnerability has been captured in [dark web](https://cyble.com/knowledge-hub/what-is-the-dark-web/) discussions and has a publicly available PoC , significantly lowering the barrier to exploitation.

**CVE-2026-21509 — Microsoft Office (High Severity, Actively Exploited)**

CVE-2026-21509 is a feature-bypass vulnerability in Microsoft Office that allows crafted documents to circumvent built-in security protections. Attackers can deliver malicious Office files that execute payloads once opened by the victim.

The flaw has been actively exploited by [threat actors](https://cyble.com/knowledge-hub/cyber-threat-actor-and-types/) including APT28 and RomCom , highlighting its operational impact.

**CVE-2026-1529 — Keycloak (High Impact)**

CVE-2026-1529 affects Red Hat’s Keycloak and involves improper validation of JWT invitation token signatures. Attackers can manipulate trusted token contents to gain unauthorized access to organizational resources.

A PoC is available, and the vulnerability surfaced on underground forums shortly after disclosure.

**CVE-2026-23906 — Apache Druid (Critical)**

CVE-2026-23906 is a critical authentication bypass vulnerability in Apache Druid, enabling unauthorized access to [sensitive data](https://cyble.com/knowledge-hub/what-is-data-loss-prevention/) stores.

**CVE-2026-0488 — SAP CRM & SAP S/4HANA (Critical)**

CVE-2026-0488 is a critical code injection vulnerability affecting SAP CRM and SAP S/4HANA. An authenticated attacker can exploit improper function module calls to execute arbitrary SQL statements, potentially resulting in full database compromise.

## **Vulnerabilities Added to CISA KEV**

CISA added 8 vulnerabilities to the KEV catalog during the reporting period. The most important of these were:

* **CVE-2026-24423** — SmarterTools SmarterMail unauthenticated RCE

* **CVE-2026-21510** — Microsoft Windows Shell protection mechanism bypass

KEV additions reflect confirmed exploitation in the wild and often signal heightened [ransomware](https://cyble.com/knowledge-hub/what-is-ransomware/) or espionage activity.

## **Critical ICS Vulnerabilities**

CISA issued **15 ICS advisories** covering **87 vulnerabilities**, with the majority rated high severity.

**CVE-2026-25084 & CVE-2026-24789 — ZLAN5143D (Critical)**

These critical vulnerabilities in ZLAN Information Technology Co.’s ZLAN5143D device involve missing authentication for critical functions.

Successful exploitation could allow attackers to bypass authentication controls or reset device passwords, potentially enabling unauthorized configuration changes and interference with industrial communications. Researchers also identified int...