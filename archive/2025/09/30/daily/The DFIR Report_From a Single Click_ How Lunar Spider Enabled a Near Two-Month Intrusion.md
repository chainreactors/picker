---
title: From a Single Click: How Lunar Spider Enabled a Near Two-Month Intrusion
url: https://thedfirreport.com/2025/09/29/from-a-single-click-how-lunar-spider-enabled-a-near-two-month-intrusion/
source: The DFIR Report
date: 2025-09-30
fetch_date: 2025-10-02T12:03:44.569357
---

# From a Single Click: How Lunar Spider Enabled a Near Two-Month Intrusion

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

Thursday, October 02, 2025

Menu

* [Threat Intelligence](https://thedfirreport.com/services/threat-intelligence/)
* [Detection Rules](https://thedfirreport.com/services/detection-rules/)
* [DFIR Labs](https://thedfirreport.com/services/dfir-labs/)
  + [Digital Forensics Challenge](https://thedfirreport.com/services/dfir-labs/ctf/)
  + [Leaderboard](https://thedfirreport.com/services/dfir-labs/dfir-labs-leaderboard/)
  + [Digital Forensics Challenge Winners](https://thedfirreport.com/services/dfir-labs/digital-forensics-challenge-winners/)
  + [Testimonials](https://thedfirreport.com/services/dfir-labs/testimonials/)
* [Case Artifacts](https://thedfirreport.com/services/case-artifacts/)

[bruteratel](https://thedfirreport.com/category/bruteratel/)
[cobaltstrike](https://thedfirreport.com/category/cobaltstrike/)
[latrodectus](https://thedfirreport.com/category/latrodectus/)

# From a Single Click: How Lunar Spider Enabled a Near Two-Month Intrusion

[September 29, 2025](https://thedfirreport.com/2025/09/29/from-a-single-click-how-lunar-spider-enabled-a-near-two-month-intrusion/)

## Key Takeaways

* The intrusion began with a Lunar Spider linked JavaScript file disguised as a tax form that downloaded and executed Brute Ratel via a MSI installer.
* Multiple types of malware were deployed across the intrusion, including Latrodectus, Brute Ratel C4, Cobalt Strike, BackConnect, and a custom .NET backdoor.
* Credentials were harvested from several sources like LSASS, backup software, and browsers, and also a Windows Answer file used for automated provisioning.
* Twenty days into the intrusion data was exfiltrated using Rclone and FTP.
* Threat actor activity persisted for nearly two months with intermittent command and control (C2) connections, discovery, lateral movement, and data exfiltration.

This case was featured in our September 2025 [DFIR Labs Forensics Challenge](https://thedfirreport.com/services/dfir-labs/ctf/) and is available as a lab today [here](https://dfirlabs.thedfirreport.com/store) for one time access or included in our new [subscription plan.](https://dfirlabs.thedfirreport.com/subscription-plans) It was originally published as a Threat Brief to customers in Feb 2025

## The DFIR Report Services

* [Private Threat Briefs](https://thedfirreport.com/services/threat-intelligence/#threat-brief): 20+ private DFIR reports annually.
* [Threat Feed](https://thedfirreport.com/services/threat-intelligence/#threat-feed): Focuses on tracking Command and Control frameworks like Cobalt Strike, Metasploit, Sliver, etc.
* [All Intel](https://thedfirreport.com/services/threat-intelligence/#all-intel): Includes everything from Private Threat Briefs and Threat Feed, plus private events, Threat Actor Insights reports, long-term tracking, data clustering, and other curated intel.
* [Private Sigma Ruleset](https://thedfirreport.com/services/detection-rules/): Features 170+ Sigma rules derived from 50+ cases, mapped to ATT&CK with test examples.
* [DFIR Labs](https://thedfirreport.com/services/dfir-labs/): Offers cloud-based, hands-on learning experiences, using real data, from real intrusions. Interactive labs are available with different difficulty levels and can be accessed on-demand, accommodating various learning speeds.

[Contact us](https://thedfirreport.com/contact/) today for pricing or a demo!

#### Table of Contents:

* + [Case Summary](#case-summary)
  + [Analysts](#analysts)
  + [Initial Access](#initial-access)
  + [Execution](#execution)
  + [Persistence](#persistence)
  + [Privilege Escalation](#privilege-escalation)
  + [Defense Evasion](#defense-evasion)
  + [Credential Access](#credential-access)
  + [Discovery](#discovery)
  + [Lateral Movement](#lateral-movement)
  + [Command and Control](#command-and-control)
  + [Exfiltration](#exfiltration)
  + [Impact](#impact)
  + [Timeline](#timeline)
  + [Diamond Model](#diamond-model)
  + [Indicators](#indicators)
  + [Detections](#detections)
  + [MITRE ATT&CK](#mitre)

##

* ## [Case Summary](#case-summary)

  The intrusion took place in May 2024, when a user executed a malicious JavaScript file. This JavaScript file has been previously reported as associated with the Lunar Spider initial access group by [EclecticIQ](https://blog.eclecticiq.com/inside-intelligence-center-lunar-spider-enabling-ransomware-attacks-on-financial-sector-with-brute-ratel-c4-and-latrodectus). The heavily obfuscated file, masquerading as a legitimate tax form, contained only a small amount of executable code dispersed among extensive filler content used for evasion. The JavaScript payload triggered the download of a MSI package, which deployed a Brute Ratel DLL file using rundll32.

  The Brute Ratel loader subsequently injected Latrodectus malware into the explorer.exe process, and established command and control communications with multiple CloudFlare-proxied domains. The Latrodectus payload was then observed retrieving a stealer module. Around one hour after initial access, the threat actor began reconnaissance activities using built-in Windows commands for host and domain enumeration, including ipconfig, systeminfo, nltest, and whoami commands.

  Approximately six hours after initial...