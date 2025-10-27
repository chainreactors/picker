---
title: From Bing Search to Ransomware: Bumblebee and AdaptixC2 Deliver Akira
url: https://thedfirreport.com/2025/08/05/from-bing-search-to-ransomware-bumblebee-and-adaptixc2-deliver-akira/
source: Over Security - Cybersecurity news aggregator
date: 2025-08-06
fetch_date: 2025-10-07T00:59:56.987089
---

# From Bing Search to Ransomware: Bumblebee and AdaptixC2 Deliver Akira

[Skip to content](#content)

Menu

* [Reports](https://thedfirreport.com/)
* [Analysts](https://thedfirreport.com/analysts/)
* [Services](https://thedfirreport.com/services/)
  + [Threat Intelligence](https://thedfirreport.com/services/threat-intelligence/)
  + [Detection Rules](https://thedfirreport.com/services/detection-rules/)
  + [DFIR Labs](https://thedfirreport.com/services/dfir-labs/)
    - [Digital Forensics Challenge](https://thedfirreport.com/services/dfir-labs/ctf/)
    - [Leaderboard](https://thedfirreport.com/services/dfir-labs/dfir-labs-leaderboard/)
    - [Digital Forensics Challenge Winners](https://thedfirreport.com/services/dfir-labs/digital-forensics-challenge-winners/)
    - [Testimonials](https://thedfirreport.com/services/dfir-labs/testimonials/)
  + [Case Artifacts](https://thedfirreport.com/services/case-artifacts/)
* [Access DFIR Labs](https://dfirlabs.thedfirreport.com/)
* [Subscribe](https://thedfirreport.com/subscribe/)
* [Contact Us](https://thedfirreport.com/contact/)

Menu

* [Threat Intelligence](https://thedfirreport.com/services/threat-intelligence/)
* [Detection Rules](https://thedfirreport.com/services/detection-rules/)
* [DFIR Labs](https://thedfirreport.com/services/dfir-labs/)
  + [Digital Forensics Challenge](https://thedfirreport.com/services/dfir-labs/ctf/)
  + [Leaderboard](https://thedfirreport.com/services/dfir-labs/dfir-labs-leaderboard/)
  + [Digital Forensics Challenge Winners](https://thedfirreport.com/services/dfir-labs/digital-forensics-challenge-winners/)
  + [Testimonials](https://thedfirreport.com/services/dfir-labs/testimonials/)
* [Case Artifacts](https://thedfirreport.com/services/case-artifacts/)

[The DFIR Report](https://thedfirreport.com/)

Real Intrusions by Real Attackers, The Truth Behind the Intrusion

Menu

* [Reports](https://thedfirreport.com/)
* [Analysts](https://thedfirreport.com/analysts/)
* [Services](https://thedfirreport.com/services/)
  + [Threat Intelligence](https://thedfirreport.com/services/threat-intelligence/)
  + [Detection Rules](https://thedfirreport.com/services/detection-rules/)
  + [DFIR Labs](https://thedfirreport.com/services/dfir-labs/)
    - [Digital Forensics Challenge](https://thedfirreport.com/services/dfir-labs/ctf/)
    - [Leaderboard](https://thedfirreport.com/services/dfir-labs/dfir-labs-leaderboard/)
    - [Digital Forensics Challenge Winners](https://thedfirreport.com/services/dfir-labs/digital-forensics-challenge-winners/)
    - [Testimonials](https://thedfirreport.com/services/dfir-labs/testimonials/)
  + [Case Artifacts](https://thedfirreport.com/services/case-artifacts/)
* [Access DFIR Labs](https://dfirlabs.thedfirreport.com/)
* [Subscribe](https://thedfirreport.com/subscribe/)
* [Contact Us](https://thedfirreport.com/contact/)

Monday, October 06, 2025

Menu

* [Threat Intelligence](https://thedfirreport.com/services/threat-intelligence/)
* [Detection Rules](https://thedfirreport.com/services/detection-rules/)
* [DFIR Labs](https://thedfirreport.com/services/dfir-labs/)
  + [Digital Forensics Challenge](https://thedfirreport.com/services/dfir-labs/ctf/)
  + [Leaderboard](https://thedfirreport.com/services/dfir-labs/dfir-labs-leaderboard/)
  + [Digital Forensics Challenge Winners](https://thedfirreport.com/services/dfir-labs/digital-forensics-challenge-winners/)
  + [Testimonials](https://thedfirreport.com/services/dfir-labs/testimonials/)
* [Case Artifacts](https://thedfirreport.com/services/case-artifacts/)

[akira](https://thedfirreport.com/category/ransomware/akira/)
[Flash Alert](https://thedfirreport.com/category/flash-alert/)
[ransomware](https://thedfirreport.com/category/ransomware/)

# From Bing Search to Ransomware: Bumblebee and AdaptixC2 Deliver Akira

[August 5, 2025](https://thedfirreport.com/2025/08/05/from-bing-search-to-ransomware-bumblebee-and-adaptixc2-deliver-akira/)

## Overview

[Bumblebee malware](https://malpedia.caad.fkie.fraunhofer.de/details/win.bumblebee) has been an initial access tool used by threat actors since late 2021. In 2023 the malware was first reported as using [SEO poisoning](https://www.secureworks.com/blog/bumblebee-malware-distributed-via-trojanized-installer-downloads) as a delivery mechanism. Recently in May of 2025 [Cyjax reported](https://www.cyjax.com/resources/blog/a-sting-on-bing-bumblebee-delivered-through-bing-seo-poisoning-campaign/) on a campaign using this method again, impersonating various IT tools. We observed a similar campaign in July in which a download of an IT management tool ended with Akira ransomware.

In July 2025, we observed a threat actor compromise an organization through this SEO poisoning campaign. A user searching for “ManageEngine OpManager” was directed to a malicious website, which delivered a trojanized software installer. This action led to the deployment of the Bumblebee malware, granting the threat actor initial access to the environment. The intrusion quickly escalated from a single infected host to a full-scale network compromise.

Following initial access, the threat actor moved laterally to a domain controller, dumped credentials, installed persistent remote access tools, and exfiltrated data using an SFTP client. The intrusion culminated in the deployment of Akira ransomware across the root domain. The threat actor returned two days later to repeat the process, encrypting systems within a child domain and causing significant operational disruption across the enterprise.

This campaign affected multiple organizations during July as we received confirmation of a similar intrusion responded to by the [Swisscom B2B CSIRT](https://www.swisscom.ch/de/business/enterprise/angebot/security/threat-detection-and-response/csirt-as-a-service-and-rapid-response.html) in which a malicious IT tool dropped Bumblebee and also ended with Akira ransomware deployment.

## DFIR Report Services

Our customers received notice of this [campaign](https://intel.thedfirreport.com/collections/view/1) in early July followed by a private [threat brief report](https://intel.thedfirreport.com/eventReports/view/87). If you are interested in the full report or additional IOCs please contact us.

* [Private Threat Briefs](https://thedfirreport.com/services/threat-intelligence/#threat-brief): 20+ private DFIR reports annually.
* [Threat Feed](https://thedfirreport.com/services/threat-intelligence/#threat-feed): Focuses on tracking Command and Control frameworks like Cobalt Strike, Metasploit, Sliver, etc.
* [All Intel](https://thedfirreport.com/services/threat-intelligence/#all-intel): Includes everything from Private Threat Briefs and Threat Feed, plus private events, Threat Actor Insights reports, long-term tracking, data clustering, and other curated intel.
* [Private Sigma Ruleset](https://thedfirreport.com/services/detection-rules/): Features 170+ Sigma rules derived from 50+ cases, mapped to ATT&CK with test examples.
* [DFIR Labs](https://thedfirreport.com/services/dfir-labs/): Offers cloud-based, hands-on learning experiences, using real data, from real intrusions. Interactive labs are available with different difficulty levels and can be accessed on-demand, accommodating various learning speeds.

[Contact us](https://thedfirreport.com/contact/) today for pricing or a demo!

## Intrusion Details

This intrusion began when a user, searching for “ManageEngine OpManager” on Bing, was directed to the malicious site opmanager[.]pro.

[![](https://thedfirreport.com/wp-content/uploads/2025/08/36726_fa_001.png)](https://thedfirreport.com/wp-content/uploads/2025/08/36726_fa_001.png)

[![](https://thedfirreport.com/wp-content/uploads/2025/08/36726_fa_002.png)](https://thedfirreport.com/wp-content/uploads/2025/08/36726_fa_002.png)

The user downloaded a trojanized MSI installer, ManageEngine-OpManager.msi, which, upon execution, installed the legitimate software while simultaneously loading the Bumblebee malware msimg32.dll via consent.exe.

[![](https://thedfirreport.com/wp-content/uploads/2025/0...