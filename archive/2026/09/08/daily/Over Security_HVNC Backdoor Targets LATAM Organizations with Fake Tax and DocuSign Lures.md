---
title: HVNC Backdoor Targets LATAM Organizations with Fake Tax and DocuSign Lures
url: https://any.run/cybersecurity-blog/hvnc-backdoor-targets-latam/
source: Over Security
date: 2026-09-08
fetch_date: 2026-09-09T06:56:40.998091
---

# HVNC Backdoor Targets LATAM Organizations with Fake Tax and DocuSign Lures

[![ANY.RUN's Cybersecurity Blog](https://any.run/cybersecurity-blog/wp-content/uploads/2026/02/anyrun-logo.svg)](https://any.run)
/
[BLOG](https://any.run/cybersecurity-blog/)

* [Guides and tutorials](https://any.run/cybersecurity-blog/guides/)
* [Research](https://any.run/cybersecurity-blog/research/)
* Categories
  + [Analyst Training](https://any.run/cybersecurity-blog/category/training/)
  + [Cybersecurity Lifehacks](https://any.run/cybersecurity-blog/category/lifehacks/)
  + [Instructions on ANY.RUN](https://any.run/cybersecurity-blog/category/instructions/)
  + [Interviews](https://any.run/cybersecurity-blog/category/interviews/)
  + [Malicious History](https://any.run/cybersecurity-blog/category/history/)
  + [Malware Analysis](https://any.run/cybersecurity-blog/category/malware-analysis/)
  + [News](https://any.run/cybersecurity-blog/category/news/)
  + [Service Updates](https://any.run/cybersecurity-blog/category/service-updates/)
* [Write for us](https://any.run/cybersecurity-blog/write-for-us/)
* [Go to service](https://app.any.run/)
* [Register for free](https://app.any.run/?register)
* [Register for free](https://app.any.run/?register)

* + Search

[![ANY.RUN's Cybersecurity Blog](https://any.run/cybersecurity-blog/wp-content/uploads/2026/02/anyrun-logo.svg)](https://any.run)
/
[BLOG](https://any.run/cybersecurity-blog/)

* [Guides and tutorials](https://any.run/cybersecurity-blog/guides/)
* [Research](https://any.run/cybersecurity-blog/research/)
* Categories
  + [Analyst Training](https://any.run/cybersecurity-blog/category/training/)
  + [Cybersecurity Lifehacks](https://any.run/cybersecurity-blog/category/lifehacks/)
  + [Instructions on ANY.RUN](https://any.run/cybersecurity-blog/category/instructions/)
  + [Interviews](https://any.run/cybersecurity-blog/category/interviews/)
  + [Malicious History](https://any.run/cybersecurity-blog/category/history/)
  + [Malware Analysis](https://any.run/cybersecurity-blog/category/malware-analysis/)
  + [News](https://any.run/cybersecurity-blog/category/news/)
  + [Service Updates](https://any.run/cybersecurity-blog/category/service-updates/)
* [Write for us](https://any.run/cybersecurity-blog/write-for-us/)
* [Go to service](https://app.any.run/)
* [Register for free](https://app.any.run/?register)
* [Register for free](https://app.any.run/?register)

* + Search

[![ANY.RUN's Cybersecurity Blog](https://any.run/cybersecurity-blog/wp-content/uploads/2026/02/anyrun-logo.svg)](https://any.run)
/
[BLOG](https://any.run/cybersecurity-blog/)

* + Search

![HVNC Backdoor Targets LATAM Organizations with Fake Tax and DocuSign Lures](https://any.run/cybersecurity-blog/wp-content/uploads/2026/09/HVNC-Backdoor-Attacks-scaled.png)

[Malware Analysis](https://any.run/cybersecurity-blog/category/malware-analysis/)

# HVNC Backdoor Targets LATAM Organizations with Fake Tax and DocuSign Lures

September 8, 2026

[Add comment](#comments-22995)
2239 views
15 min read

[Home](https://any.run/cybersecurity-blog/)[Malware Analysis](https://any.run/cybersecurity-blog/category/malware-analysis/)

HVNC Backdoor Targets LATAM Organizations with Fake Tax and DocuSign Lures

#### Recent posts

* [![](https://any.run/cybersecurity-blog/wp-content/uploads/2026/09/HVNC-Backdoor-Attacks-1024x497.png)

  #### HVNC Backdoor Targets LATAM Organizations with Fake Tax and DocuSign Lures

  2239
  0](https://any.run/cybersecurity-blog/hvnc-backdoor-targets-latam/)
* [![](https://any.run/cybersecurity-blog/wp-content/uploads/2026/07/Release-notes-1024x497.png)

  #### Release Notes: Faster TI Investigations, Fresh Threat Research, and 650+ Threat Coverage Updates

  7093
  0](https://any.run/cybersecurity-blog/release-notes-august-2026/)
* [![](https://any.run/cybersecurity-blog/wp-content/uploads/2026/09/mssp-cover-1024x497.png)

  #### Triage & Response Bottlenecks Eating into MSSP Margins: How to Remove the Friction

  5746
  0](https://any.run/cybersecurity-blog/mssp-triage-response-bottlenecks/)

[Home](https://any.run/cybersecurity-blog/)[Malware Analysis](https://any.run/cybersecurity-blog/category/malware-analysis/)

HVNC Backdoor Targets LATAM Organizations with Fake Tax and DocuSign Lures

*Editor’s note: The analysis is authored by Moises Cerqueira, malware researcher & threat hunter. You can find Moises on [LinkedIn](https://www.linkedin.com/in/moises-cerqueira/) and [X](https://x.com/0x_Olympus).*

Fake tax documents are being used to target organizations across LATAM, delivering a custom HVNC backdoor built for stealthy, persistent access. Once installed, the malware can give attackers hidden remote control, steal browser data, monitor keystrokes, and survive system reboots.

The attack chain combines trusted business lures, anti-analysis techniques, and infrastructure designed to keep access hidden. For security leaders, the risk goes beyond a single compromised endpoint: persistent access can expose credentials, sensitive data, and business systems while giving attackers more time to move deeper into the environment.

## HVNC Campaign Overview

The campaign uses fake DocuSign notifications, NFe tax documents, and banking-themed phishing to deliver a custom HVNC backdoor. Once installed, it can give attackers hidden remote control and persistent access to compromised systems.

|  |  |
| --- | --- |
| Threat type | Multi-stage phishing campaign; custom HVNC backdoor |
| Targeting | Banking and financial services in Latin America |
| Delivery | Fake DocuSign and NFe tax-document lures; related ClickFix-style delivery also observed |
| Objective | Persistent remote access and control of compromised systems |
| Attribution | Unconfirmed; Silver Fox / Winos4.0-adjacent tradecraft at medium confidence |

## Business Risks Behind the HVNC Campaign

For organizations, the danger lies in how much access the malware can provide once a device is compromised. Its capabilities can increase both the scope of exposure and the time attackers remain active in the environment.

* **Credential and session theft:** The malware monitors keystrokes and targets Firefox cookies, browsing history, and permissions, putting account access at risk.
* **Hidden remote control:** HVNC functionality lets attackers interact with the compromised system through a hidden desktop, including screen capture and simulated mouse and keyboard input.
* **Persistent access:** The backdoor establishes Startup-folder persistence, allowing it to remain active after system reboots.
* **Reduced visibility for defenders:** The malware checks for more than 20 AV/EDR processes and adjusts its behavior when security software is present.
* **Longer exposure to compromise:** Its persistent C2 connection and repeated reconnection attempts are designed to keep the implant available even through network interruptions.

Cut the time attackers have inside your environment.

Reduce exposure before it turns into business loss.

[Reduce Business Risk](https://any.run/enterprise/?utm_source=anyrunblog&utm_medium=article&utm_campaign=hvnc-backdoor-targets-latam&utm_term=080926&utm_content=linktoenterprise#contact-sales)

## Who Is This Campaign Targeting?

The campaign appears financially motivated, with a clear focus on **banking and financial services in Latin America**. [Threat intelligence analysis](https://any.run/threat-intelligence-lookup/?utm_source=anyrunblog&utm_medium=article&utm_campaign=hvnc-backdoor-targets-latam&utm_term=080926&utm_content=linktotilookuplanding) using ANY.RUN data revealed phishing infrastructure impersonating major banks, alongside fake tax-document lures designed to blend into routine financial and administrative workflows.

![TI Lookup used to get deeper context into HVNC Backdoor attack](https://any.run/cybersecurity-blog/wp-content/uploads/2026/09/TI-lookup-query-1024x560.png)

*TI Lookup used to get deeper context into HVNC Backdoor attack*

## Attack Chain Overview

The campaign follows a **four-stage infection chain** that moves from fake...