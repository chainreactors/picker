---
title: Emulating and Detecting Scattered Spider-like Attacks
url: https://blog.sekoia.io/emulating-and-detecting-scattered-spider-like-attacks/
source: Over Security - Cybersecurity news aggregator
date: 2024-07-25
fetch_date: 2025-10-06T17:45:43.190441
---

# Emulating and Detecting Scattered Spider-like Attacks

### Log in

Username or Email Address

Password

[ ]  Remember Me

 [Forgot password?](https://blog.sekoia.io/wp-login.php?action=lostpassword)

### Search the site...

Search for

* All categories
* [Threat Research & Intelligence](https://blog.sekoia.io/category/threat-research/)
* [Product News](https://blog.sekoia.io/category/product-news/)
* [SOC Insights & Other News](https://blog.sekoia.io/category/soc-insights-other-news/)
* [Detection Engineering](https://blog.sekoia.io/category/detection-engineering/)

####

Reset

[![logo sekoia.io blog light](data:image/svg+xml...)![logo sekoia.io blog light](https://t7f4e9n3.delivery.rocketcdn.me/wp-content/uploads/2023/03/cropped-logo-sekoia-io-blog-light.png)](https://blog.sekoia.io/)

* [Threat Research](https://blog.sekoia.io/category/threat-research/)
* [Detection](https://blog.sekoia.io/category/detection-engineering/)
* [Product News](https://blog.sekoia.io/category/product-news/)
* [Other](https://blog.sekoia.io/category/soc-insights-other-news/)
* [Sign up](https://go.sekoia.io/Preference-center-EN.html)
* [About Sekoia.io](https://www.sekoia.io/en/about/)
  + [TDR Team](https://www.sekoia.io/en/about-threat-detection-research-team/)
  + [AI-SOC platform](https://www.sekoia.io/en/homepage/)
  + [Interactive demo](https://sekoia.storylane.io/share/8zdjfok9atpn)
  + [Contact Us](https://www.sekoia.io/en/contact/)

* [Threat Research](https://blog.sekoia.io/category/threat-research/)
* [Detection](https://blog.sekoia.io/category/detection-engineering/)
* [Product News](https://blog.sekoia.io/category/product-news/)
* [Other](https://blog.sekoia.io/category/soc-insights-other-news/)
* [Sign up](https://go.sekoia.io/Preference-center-EN.html)
* [About Sekoia.io](https://www.sekoia.io/en/about/)
  + [TDR Team](https://www.sekoia.io/en/about-threat-detection-research-team/)
  + [AI-SOC platform](https://www.sekoia.io/en/homepage/)
  + [Interactive demo](https://sekoia.storylane.io/share/8zdjfok9atpn)
  + [Contact Us](https://www.sekoia.io/en/contact/)

Log in

[Detection Engineering](https://blog.sekoia.io/category/detection-engineering/ "Detection Engineering")

# Emulating and Detecting Scattered Spider-like Attacks

[![](data:image/svg+xml...)![](https://t7f4e9n3.delivery.rocketcdn.me/wp-content/uploads/2024/04/TDR-badge.png)](#molongui-disabled-link)

[Sekoia TDR, Mitigant, Guillaume C., Erwan Chevalier and Kennedy Torkura](#molongui-disabled-link)
July 24 2024

0

10 minutes reading

*Written by* [*Mitigant*](https://www.mitigant.io/) *(Kennedy Torkura) and* [*Sekoia.io*](https://www.sekoia.io/en/homepage/) *Threat Detection and Research (TDR) team (Erwan Chevalier and Guillaume Couchard).*

## Table of contents

* [Introduction](#h-introduction)
* [Aim of This Article](#h-aim-of-this-article)
* [Threat Scenario](#h-threat-scenario)
* [Threat Model](#h-threat-model)
* [Cloud Attack Emulation](#h-cloud-attack-emulation)
* [Cloud Attack Phases and Detection](#h-cloud-attack-phases-and-detection)
  + [Initial Access](#h-initial-access)
  + [Execution](#h-execution)
  + [Persistence](#h-persistence-nbsp)
  + [Privilege Escalation](#h-privilege-escalation)
  + [Defense Evasion](#h-defense-evasion-nbsp)
  + [Credential Access](#h-credential-access-nbsp)
  + [Collection and Data Theft](#h-collection-and-data-theft)
* [Lessons Learnt](#h-lessons-learnt)
* [Conclusion](#h-conclusion)
* [Sigma Rules](#h-sigma-rules)

## Introduction

Enterprises are increasingly using cloud infrastructure to take advantage of its underlying benefits. Unlike traditional data centres, cloud infrastructure affords business agility at a cheaper cost. Consequently, several organisations are migrating workloads to the cloud. However, cybercriminals have also noticed this trend and have started targeting cloud workloads.

Defending cloud infrastructure is more complex than defending on-premises infrastructure. Enterprises often need support with interpreting and implementing the appropriate security controls that align with the shared security responsibility model, significantly for threat detection and response. One approach to address this gap is to leverage third-party products that provide effective cloud threat detection and response.

![Emulating and Detecting Scattered Spider-like Attacks on AWS](data:image/svg+xml...)![Emulating and Detecting Scattered Spider-like Attacks on AWS](https://t7f4e9n3.delivery.rocketcdn.me/wp-content/uploads/2024/07/Timeline.png)

## Aim of This Article

This article provides a use-case scenario demonstrating how defenders can address detection gaps in AWS environments. This will be achieved by combining [Mitigant Cloud Attack Emulation](https://www.mitigant.io/en/platform/cloud-attack-emulation) and the [Sekoia Security Operations Center (SOC)](https://www.sekoia.io/en/homepage/) Platform. Furthermore, this article discusses how organisations can adopt a Threat-Informed Defense strategy by combining security measures, Cyber Threat Intelligence, and evaluation/testing. This strategy enables organisations to detect and respond effectively to threats lurking in their AWS infrastructure. We provide details of how Extended Detection and Response (XDR) and adversary emulation can be synergized to defend against malicious threat actors.

## Threat Scenario

To demonstrate the importance of using a combined approach of a SOC Platform and adversary emulation, a threat scenario has been formulated based on a real-life attack observed by the Sekoia platform. The scenario is based on real events that emulate the Scattered Spider threat actor. It also demonstrates the effectiveness of leveraging a Threat-Informed Defense Strategy (TIDS).

The Scattered Spider threat actor is a cyber-criminal gang that has become notorious recently. Scattered Spider targets financial institutions, telecommunication organisations, and technology companies. The Sekoia Threat Detection and Research (TDR) team wrote a comprehensive blog post about Scattered Spider; you can [find a detailed description of it at this link](https://blog.sekoia.io/scattered-spider-laying-new-eggs/).

## Threat Model

The threat model illustrates Acme, a fictitious Fintech that hosts its sophisticated banking system on AWS cloud infrastructure. John Doe, Acme’s CISO, has been bothered about the increasing popularity of the Scattered Spider Threat actor and wants to ensure that Acme is not the next victim of this notorious threat actor. He recently attended the MITRE ATT&CK Workshop in Brussels, where he learned about **Threat-Informed Defense Strategy (TIDS)**. Consequently, he applied TIDS to enable a cyber-resilient cloud posture by adopting the three pillars: security measures, Cyber Threat Intelligence (CTI), and Security evaluation/testing.

John uses several AWS security services; however, he wants to leave no stone unturned; therefore, he adds the following cyber security products to align with TIDS:

1. Defensive Measures: [**Sekoia Defend**](https://www.sekoia.io/en/product/xdr/) is a leading SOC platform that provides threat detection and incident response capabilities offered by Sekoia.io
2. Cyber Threat Intelligence: [**Sekoia Intelligence**](https://www.sekoia.io/en/product/cti/), a highly structured, contextualised, and actionable CTI service offered by Sekoia.io
3. Testing & Evaluation: [Mitigant Cloud Attack Emulation](https://www.mitigant.io/en/platform/cloud-attack-emulation), the most comprehensive cloud-native adversary emulation platform, provides over 100 attacks that align with MITRE ATT&CK and MITRE ATLAS.

![Threat Informed Defense Triad](data:image/svg+xml...)

**Threat Informed Defense Triad**

## Cloud Attack Emulation

Mitigant Cloud Attack Emulation implements several MITRE ATT&CK TTPS used by Scattered Spider. These attacks were orchestrated against Acme’s AWS environment to mimic Scattered Spider, and the Sekoia SOC Platform is used to detect these attacks. To better understand the detection, it is essential to note...