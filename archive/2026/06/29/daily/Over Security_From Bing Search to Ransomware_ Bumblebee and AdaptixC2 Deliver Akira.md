---
title: From Bing Search to Ransomware: Bumblebee and AdaptixC2 Deliver Akira
url: https://thedfirreport.com/2026/06/29/from-bing-search-to-ransomware-bumblebee-and-adaptixc2-deliver-akira-3/
source: Over Security
date: 2026-06-29
fetch_date: 2026-06-30T06:09:56.784509
---

# From Bing Search to Ransomware: Bumblebee and AdaptixC2 Deliver Akira

View the latest

[DFIR Report](https://thedfirreport.com/2026/06/29/from-bing-search-to-ransomware-bumblebee-and-adaptixc2-deliver-akira)
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
* [Analyst](/company/analysts/)
* [SQL Brute Force Leads to BlueSky Ransomware](https://thedfirreport.com/2023/12/04/sql-brute-force-leads-to-bluesky-ransomware/)
* [From OneNote to RansomNote: An Ice Cold Intrusion](https://thedfirreport.com/2024/04/01/from-onenote-to-ransomnote-an-ice-cold-intrusion/)

![](https://thedfirreport.com/wp-content/uploads/pr_36726_001.png)

[akira](https://thedfirreport.com/category/ransomware/akira/)

# From Bing Search to Ransomware: Bumblebee and AdaptixC2 Deliver Akira

June 29, 2026

## Key Takeaways

* In July 2025, BumbleBee malware was deployed via SEO poisoning through a trojanized installer for ManageEngine OpManager.
* Following initial access, BumbleBee dropped an AdaptixC2 beacon to facilitate further intrusion activities, allowing the threat actor to pivot to a domain controller and dump the NTDS.dit.
* The threat actor returned the following day and established an SSH proxy, enabling lateral movement across the network and data exfiltration via FileZilla and SFTP to an external server.
* The threat actor concluded the intrusion by deploying Akira ransomware across the root domain and returned two days later to encrypt a child domain.

This case was first reported to customers in a threat brief released in July 2025 and in a [public flash alert](https://thedfirreport.com/2025/08/05/from-bing-search-to-ransomware-bumblebee-and-adaptixc2-deliver-akira-2/) in August 2025 in partnership with [Swisscom B2B CSIRT](https://www.swisscom.ch/en/business/enterprise/offer/security/threat-detection-and-response/csirt-as-a-service-and-rapid-response.html), which observed another intrusion tied to the same campaign. This report contains data from both intrusions. We plan to release a [DFIR Labs](https://thedfirreport.com/products/dfir-labs/) case based on this report later this quarter.

## Case Summary

The BumbleBee intrusion was initiated in July 2025 via an SEO poisoning attack that lured a user searching for “ManageEngine OpManager” to a look-alike domain. Upon downloading a trojanized MSI installer, the BumbleBee first-stage loader (msimg32.dll) was executed on a beachhead host via DLL side-loading. The loader immediately established command-and-control (C2) communication with threat actor-controlled infrastructure.

Approximately five hours after the initial infection, the threat actor deployed AdgNsy.exe, a renamed instance of the legitimate Windows Address Book utility, which was injected with AdaptixC2 shellcode. This established a persistent C2 channel, enabling the threat actor to perform living-off-the-land discovery commands such as `systeminfo` and `nltest` to map the internal network. To ensure persistence, the threat actor created new domain accounts with Enterprise Admin privileges and installed RustDesk as a Windows service on multiple servers.

On the second and third days, the threat actor moved laterally using RDP to pivot to a domain controller and a backup server. They engaged in extensive credential harvesting, utilizing wbadmin.exe to extract the NTDS.dit Active Directory database and executing custom PowerShell scripts to dump and decrypt Veeam credentials via DPAPI. The threat actor also employed the lsassy utility to dump LSASS memory across multiple hosts.

Throughout the intrusion, ...