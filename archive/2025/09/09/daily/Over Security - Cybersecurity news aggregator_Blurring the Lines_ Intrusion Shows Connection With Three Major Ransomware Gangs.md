---
title: Blurring the Lines: Intrusion Shows Connection With Three Major Ransomware Gangs
url: https://thedfirreport.com/2025/09/08/blurring-the-lines-intrusion-shows-connection-with-three-major-ransomware-gangs/
source: Over Security - Cybersecurity news aggregator
date: 2025-09-09
fetch_date: 2025-10-02T19:51:35.129192
---

# Blurring the Lines: Intrusion Shows Connection With Three Major Ransomware Gangs

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

[dragonforce](https://thedfirreport.com/category/ransomware/dragonforce/)
[play](https://thedfirreport.com/category/ransomware/play/)
[ransomhub](https://thedfirreport.com/category/ransomware/ransomhub/)
[sectoprat](https://thedfirreport.com/category/sectoprat/)

# Blurring the Lines: Intrusion Shows Connection With Three Major Ransomware Gangs

[September 8, 2025](https://thedfirreport.com/2025/09/08/blurring-the-lines-intrusion-shows-connection-with-three-major-ransomware-gangs/)

## Key Takeaways

* The intrusion began when a user downloaded and executed a malicious file impersonating DeskSoft’s EarthTime application but instead dropped SectopRAT malware.
* The threat actor deployed multiple malware families, including SystemBC for proxy tunneling, and later Betruger backdoor for additional capabilities. They leveraged various tools such as AdFind, SharpHound, SoftPerfect NetScan, and GT\_NET.exe (Grixba) to map out the environment and perform reconnaissance activities.
* Lateral movement was primarily accomplished through RDP connections, with additional use of Impacket’s wmiexec. The threat actor moved across multiple systems, including domain controllers, backup servers, and file servers, while maintaining persistence through local account creation and startup folder shortcuts.
* Data collection and exfiltration were performed using WinRAR to compress targeted file shares containing sensitive business documents, which were then transferred via WinSCP to an FTP server hosted by a cloud provider in clear text.
* The discovery of Grixba (a reconnaissance tool linked to Play ransomware), a previous NetScan output containing data from a company reportedly compromised by DragonForce ransomware, and the use of the Betruger backdoor suggest that the likely objective of this intrusion was ransomware deployment. Based on these findings, the threat actor behind this intrusion was most likely an affiliate operating across multiple ransomware groups.

This case was originally published as a [Threat Brief](https://thedfirreport.com/services/threat-intelligence/#threat-brief) to customers in March of 2025. Interested in pricing or have questions about our services? [Contact us](https://pt.thedfirreport.com/contact/)

## The DFIR Report Services

* + [Private Threat Briefs](https://thedfirreport.com/services/threat-intelligence/#threat-brief): 20+ private DFIR reports annually.
  + [Threat Feed](https://thedfirreport.com/services/threat-intelligence/#threat-feed): Focuses on tracking Command and Control frameworks like Cobalt Strike, Metasploit, Sliver, etc.
  + [All Intel](https://thedfirreport.com/services/threat-intelligence/#all-intel): Includes everything from Private Threat Briefs and Threat Feed, plus private events, Threat Actor Insights reports, long-term tracking, data clustering, and other curated intel.
  + [Private Sigma Ruleset](https://thedfirreport.com/services/detection-rules/): Features 170+ Sigma rules derived from 50+ cases, mapped to ATT&CK with test examples.
  + [DFIR Labs](https://thedfirreport.com/services/dfir-labs/): Offers cloud-based, hands-on learning experiences, using real data, from real intrusions. Interactive labs are available with different difficulty levels and can be accessed on-demand, accommodating various learning speeds.

  [Contact us](https://thedfirreport.com/contact/) today for pricing or a demo!

#### Table of Contents:

* [Case Summary](#case-summary)
* [Analysts](#analysts)
* [Initial Access](#initial-access)
* [Execution](#execution)
* [Persistence](#persistence)
* [Privilege Escalation](#privilege-escalation)
* [Defense Evasion](#defense-evasion)
* [Credential Access](#credential-access)
* [Discovery](#discovery)
* [Lateral Movement](#lateral-movement)
* [Collection](#collection)
* [Command and Control](#command-and-control)
* [Exfiltration](#exfiltration)
* [Impact](#impact)
* [Timeline](#timeline)
* [Diamond Model](#diamond-model)
* [Indicators](#indicators)
* [Detections](#detections)
* [MITRE ATT&CK](#mitre)

## [Case Summary](#case-summary)

The intrusion began in September 2024 with a download of a malicious file mimicking the EarthTime application by DeskSoft. Upon execution, SectopRAT was deployed which opened a connection to its command and control (C2) infrastructure. The threat actor established persistence by relocating the malicious file and placing a shortcut in the Startup folder, configured to trigger on user logon. They further elevated access by creating a new local account an...