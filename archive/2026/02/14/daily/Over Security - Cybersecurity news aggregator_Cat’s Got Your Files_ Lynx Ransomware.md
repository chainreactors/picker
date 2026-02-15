---
title: Cat’s Got Your Files: Lynx Ransomware
url: https://thedfirreport.com/2025/12/17/cats-got-your-files-lynx-ransomware/
source: Over Security - Cybersecurity news aggregator
date: 2026-02-14
fetch_date: 2026-02-15T04:26:20.362552
---

# Cat’s Got Your Files: Lynx Ransomware

View the latest

[DFIR Report](https://thedfirreport.com/2025/12/17/cats-got-your-files-lynx-ransomware/)
X

[![](https://thedfirreport.com/wp-content/uploads/DFIR-REPORT-Logo@2x.png)

![](https://thedfirreport.com/wp-content/uploads/DFIR-White-Logo.png)](https://thedfirreport.com)

* [Public Reports](https://thedfirreport.com/reports/)
* Products

  + - [Products Overview](https://thedfirreport.com/products/)
    - [Threat Intel](https://thedfirreport.com/products/threat-intel/)
      * [Threat Feed](https://thedfirreport.com/products/threat-feed/)
      * [Private DFIR Reports](https://thedfirreport.com/products/threat-intel/private-dfir-reports/)
      * [All Intel](https://thedfirreport.com/products/threat-intel/all-intel/)
      * [Active Defense](https://thedfirreport.com/products/active-defense/)
    - [DFIR Labs](https://thedfirreport.com/products/dfir-labs/)
    - [Case Artifacts](https://thedfirreport.com/products/case-artifacts/)
  + - -
    - [Detection Pack](https://thedfirreport.com/products/detection-pack/)
    - [AI Training Ground](https://thedfirreport.com/products/ai-training-ground/)
  + - -

      bruteratel

      [From a Single Click: How Lunar Spider Enabled a Near Two-Month Intrusion](https://thedfirreport.com/2025/09/29/from-a-single-click-how-lunar-spider-enabled-a-near-two-month-intrusion/)

      [Read More](https://thedfirreport.com/2025/09/29/from-a-single-click-how-lunar-spider-enabled-a-near-two-month-intrusion/)
    - -

      dragonforce

      [Blurring the Lines: Intrusion Shows Connection With Three Major Ransomware Gangs](https://thedfirreport.com/2025/09/08/blurring-the-lines-intrusion-shows-connection-with-three-major-ransomware-gangs/)

      [Read More](https://thedfirreport.com/2025/09/08/blurring-the-lines-intrusion-shows-connection-with-three-major-ransomware-gangs/)
* Services

  + - [Services Overview](https://thedfirreport.com/services/)
    - [Training](https://thedfirreport.com/services/training/)
      * [Threat Hunting](https://thedfirreport.com/services/training/threat-hunting/)
  + - -
    - [Professional Services](https://thedfirreport.com/services/professional-services/)
      * [Integration](https://thedfirreport.com/services/professional-services/integration/)
      * [CTI Program Advisory](https://thedfirreport.com/services/professional-services/cti-program-advisory/)
      * [Incident Response Playbook](https://thedfirreport.com/services/professional-services/incident-response-playbook/)
* Company

  + - [About us](https://thedfirreport.com/company/about-us/)
    - [Contact Us](https://thedfirreport.com/company/contact-us/)
  + - [Collaboration](https://thedfirreport.com/company/collaboration/)
    - [Careers](https://thedfirreport.com/company/careers/)
* [Analysts](https://thedfirreport.com/company/analysts/)

* [Access DFIR Labs](https://dfirlabs.thedfirreport.com/auth/login)
* [Get in Touch](https://thedfirreport.com/company/contact-us/)

* [Public Reports](https://thedfirreport.com/reports/)
* Products
  + [Products Overview](https://thedfirreport.com/products/)
  + Threat Intel
    - [Threat intel Overview](https://thedfirreport.com/products/threat-intel/)
    - [Threat Feed](https://thedfirreport.com/products/threat-feed/)
    - [Private DFIR Reports](https://thedfirreport.com/products/threat-intel/private-dfir-reports/)
    - [All Intel](https://thedfirreport.com/products/threat-intel/all-intel/)
    - [Active Defense](https://thedfirreport.com/products/active-defense/)
  + [DFIR Labs](https://thedfirreport.com/products/dfir-labs/)
  + [Case Artifacts](https://thedfirreport.com/products/case-artifacts/)
  + [Detection Pack](https://thedfirreport.com/products/detection-pack/)
  + [AI Training Ground](https://thedfirreport.com/products/ai-training-ground/)
* Services
  + [Service Overview](https://thedfirreport.com/services/)
  + [Training](https://thedfirreport.com/services/training/)
    - [Threat Hunting](https://thedfirreport.com/services/training/threat-hunting/)
  + [Professional Services](https://thedfirreport.com/services/professional-services/)
    - [Integration](https://thedfirreport.com/services/professional-services/integration/)
    - [CTI Program Advisory](https://thedfirreport.com/services/professional-services/cti-program-advisory/)
    - [Incident Response Playbook](https://thedfirreport.com/services/professional-services/incident-response-playbook/)
* Company
  + [Company Overview](https://thedfirreport.com/company/)
  + [About us](https://thedfirreport.com/company/about-us/)
  + [Contact Us](https://thedfirreport.com/company/contact-us/)
  + [Careers](https://thedfirreport.com/company/careers/)
* [Analyst](/)
* [SQL Brute Force Leads to BlueSky Ransomware](https://thedfirreport.com/2023/12/04/sql-brute-force-leads-to-bluesky-ransomware/)
* [From OneNote to RansomNote: An Ice Cold Intrusion](https://thedfirreport.com/2024/04/01/from-onenote-to-ransomnote-an-ice-cold-intrusion/)

![](https://thedfirreport.com/wp-content/uploads/1200_627-test.jpg)

[ransomware](https://thedfirreport.com/category/ransomware/)

# Cat’s Got Your Files: Lynx Ransomware

December 17, 2025

## Key Takeaways

* The intrusion began with a successful RDP login using already-compromised credentials, likely obtained via an infostealer, data breach reuse, or an initial access broker.
* Within minutes, the threat actor moved laterally to a domain controller using a separate compromised domain admin account, created multiple impersonation-style accounts, and added them to privileged groups.
* The threat actor mapped out virtualization infrastructure and file shares, conducted additional enumeration, and created one more look-alike account before pausing activity.
* Sensitive files from multiple network shares were collected, compressed using 7-Zip, and exfiltrated via temporary file-sharing service `temp.sh` .
* The threat actor connected to backup servers, deleted backup jobs, and deployed Lynx ransomware across multiple backup and file servers via RDP. The overall Time to Ransomware (TTR) was ~178 hours across nine days.

## The DFIR Report Services

* [Private Threat Briefs:](https://thedfirreport.com/products/threat-intel/) 20+ private DFIR reports annually.
* [Threat Feed:](https://thedfirreport.com/products/threat-feed/) Focuses on tracking Command and Control frameworks like Cobalt Strike, Metasploit, Sliver, etc.
* [All Intel](https://thedfirreport.com/products/threat-intel/all-intel/): Includes everything from Private Threat Briefs and Threat Feed, plus private events, Threat Actor Insights reports, long-term tracking, data clustering, and other curated intel.
* [Private Sigma Ruleset](https://thedfirreport.com/products/threat-intel/private-dfir-reports/): Features 170+ Sigma rules derived from 50+ cases, mapped to ATT&CK with test examples.
* <https://thedfirreport.com/products/dfir-labs/>DFIR Labs: Offers cloud-based, hands-on learning experiences, using real data, from real intrusions. Interactive labs are available with different difficulty levels and can be accessed on-demand, accommodating various learning speeds.

[Contact us](https://thedfirreport.com/company/contact-us/) today for pricing or a demo!

## Case Summary

The intrusion began in early March 2025 with a single successful Remote Desktop Protocol (RDP) logon to an internet-exposed system. Notably, there was no evidence of credential stuffing, brute forcing, or other failed authentication attempts from the source IP, indicating the threat actor likely possessed valid credentials before the activity occurred. Although the original source of the credentials could not be determined, they are commonly acquired through credential-stealing malware, reused passwords from prior data breaches, or purchased through initial access brokers.

Immediately after logging in, the threat actor began reconnaissance using the command prompt and standard Windows utilities. They then expanded their activity to network-wide enumeration by deploy...