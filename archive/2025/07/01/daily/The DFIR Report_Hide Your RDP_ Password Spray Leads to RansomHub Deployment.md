---
title: Hide Your RDP: Password Spray Leads to RansomHub Deployment
url: https://thedfirreport.com/2025/06/30/hide-your-rdp-password-spray-leads-to-ransomhub-deployment/
source: The DFIR Report
date: 2025-07-01
fetch_date: 2025-10-06T23:18:17.064267
---

# Hide Your RDP: Password Spray Leads to RansomHub Deployment

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

[ransomhub](https://thedfirreport.com/category/ransomware/ransomhub/)
[ransomware](https://thedfirreport.com/category/ransomware/)
[rdp](https://thedfirreport.com/category/rdp/)

# Hide Your RDP: Password Spray Leads to RansomHub Deployment

[June 30, 2025](https://thedfirreport.com/2025/06/30/hide-your-rdp-password-spray-leads-to-ransomhub-deployment/)

## Key Takeaways

* Initial access was via a password spray attack against an exposed RDP server, targeting numerous accounts over a four-hour period.
* Mimikatz and Nirsoft were used to harvest credentials, with evidence of LSASS memory access.
* Discovery was accomplished using living-off-the-land binaries as well as Advanced IP Scanner and NetScan.
* Rclone was used to exfiltrate data to a remote server using SFTP.
* The threat actor deployed RansomHub ransomware network wide, which spread over SMB and was executed using remote services.

This case was featured in our June 2025 [DFIR Labs Forensics Challenge](https://thedfirreport.com/services/dfir-labs/ctf/) and is available as a lab today [here](https://store.thedfirreport.com/products/ransomhub-leads-to-domain-compromise-33490) for one time access or included in our new [subscription plan.](https://dfirlabs.thedfirreport.com/subscription-plans) It was originally published as a Threat Brief to customers in Feb 2025.

## The DFIR Report Services

* [Private Threat Briefs](https://thedfirreport.com/services/threat-intelligence/#threat-brief): 20+ private DFIR reports annually.
* [Threat Feed](https://thedfirreport.com/services/threat-intelligence/#threat-feed): Focuses on tracking Command and Control frameworks like Cobalt Strike, Metasploit, Sliver, etc.
* [All Intel](https://thedfirreport.com/services/threat-intelligence/#all-intel): Includes everything from Private Threat Briefs and Threat Feed, plus private events, Threat Actor Insights reports, long-term tracking, data clustering, and other curated intel.
* [Private Sigma Ruleset](https://thedfirreport.com/services/detection-rules/): Features 170+ Sigma rules derived from 50+ cases, mapped to ATT&CK with test examples.
* [DFIR Labs](https://thedfirreport.com/services/dfir-labs/): Offers cloud-based, hands-on learning experiences, using real data, from real intrusions. Interactive labs are available with different difficulty levels and can be accessed on-demand, accommodating various learning speeds.

#### Table of Contents:

* [Case Summary](#case-summary)
* [Services](#services)
* [Analysts](#analysts)
* [Initial Access](#initial-access)
* [Execution](#execution)
* [Persistence](#persistence)
* [Defense Evasion](#defense-evasion)
* [Credential Access](#credential-access)
* [Discovery](#discovery)
* [Lateral Movement](#lateral-movement)
* [Command and Control](#command-and-control)
* [Exfiltration](#exfiltration)
* [Impact](#impact)
* [Timeline](#timeline)
* [Diamond Model](#diamond-model)
* [Indicators](#indicators)
* [Detections](#detections)
* [MITRE ATT&CK](#mitre)

## [Case Summary](#case-summary)

This intrusion began in November 2024 with a password spray attack targeting an internet-facing RDP server. Over the course of several hours, the threat actor attempted logins against multiple accounts using known malicious IPs (based on OSINT). Several hours later they then logged in via RDP with one of the previously compromised users and ran a series of discovery commands, including various `net` commands to enumerate users and computers. Credential access tools, specifically Mimikatz and [Nirsoft CredentialsFileView](https://www.nirsoft.net/utils/credentials_file_view.html), were used to extract stored credentials and interact with LSASS memory.

Approximately two hours after initially authenticating to the beachhead host, the threat actor used RDP to move laterally to two domain controllers. Once on the domain controllers, they accessed the Windows Administrative Tools via the graphical user interface (GUI) to examine the DNS management console. Simultaneously, the threat actor continued to access additional servers and endpoints, conducting similar activities, namely reconnaissance via net commands and credential harvesting using Mimikatz throughout the environment. During this same time frame, Advanced IP Scanner was downloaded via the Microsoft Edge browser, and a network scan was initiated from the beachhead host.

The threat actor then continued lateral movement to additional hosts targeting backup servers, file servers, hypervisors, and more domain controllers. They uti...