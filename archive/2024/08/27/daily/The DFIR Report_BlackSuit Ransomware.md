---
title: BlackSuit Ransomware
url: https://thedfirreport.com/2024/08/26/blacksuit-ransomware/
source: The DFIR Report
date: 2024-08-27
fetch_date: 2025-10-06T18:03:22.631975
---

# BlackSuit Ransomware

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

[adfind](https://thedfirreport.com/category/adfind/)
[blacksuit](https://thedfirreport.com/category/blacksuit/)
[cobaltstrike](https://thedfirreport.com/category/cobaltstrike/)
[ransomware](https://thedfirreport.com/category/ransomware/)

# BlackSuit Ransomware

[August 26, 2024](https://thedfirreport.com/2024/08/26/blacksuit-ransomware/)

## [Key Takeaways](#key)

* In December 2023, we observed an intrusion that started with the execution of a Cobalt Strike beacon and ended in the deployment of BlackSuit ransomware.
* The threat actor leveraged various tools, including Sharphound, Rubeus, SystemBC, Get-DataInfo.ps1, Cobalt Strike, and ADFind, along with built-in system tools.
* Command and control traffic was proxied through CloudFlare to conceal their Cobalt Strike server.
* Fifteen days after initial access, BlackSuit ransomware was deployed by copying files over SMB to admin shares and executing them through RDP sessions.
* Three rules were added to our private ruleset related to this case.

An audio version of this report can be found on [Spotify](https://podcasters.spotify.com/pod/show/the-dfir-report/), [Apple](https://podcasts.apple.com/us/podcast/reports/id1728699064), [YouTube](https://www.youtube.com/%40TheDFIRReport/videos), [Audible](https://www.audible.com/pd/Reports-Podcast/B0CSZBRCFX?action_code=ASSGB149080119000H&share_location=pdp), & [Amazon](https://music.amazon.com/podcasts/c4fe897d-a4b4-4ceb-908d-d1a78af8cb6d/reports).

## [The DFIR Report Services](#services)

* [Private Threat Briefs](https://thedfirreport.com/services/threat-intelligence/#threat-brief): Over 20 private DFIR reports annually.
* [Threat Feed](https://thedfirreport.com/services/threat-intelligence/#threat-feed): Focuses on tracking Command and Control frameworks like Cobalt Strike, Metasploit, Sliver, etc.
* [All Intel](https://thedfirreport.com/services/threat-intelligence/#all-intel): Includes everything from Private Threat Briefs and Threat Feed, plus private events, opendir reports, long-term tracking, data clustering, and other curated intel.
* [Private Sigma Ruleset](https://thedfirreport.com/services/detection-rules/): Features 100+ Sigma rules derived from 40+ cases, mapped to ATT&CK with test examples.
* [DFIR Labs](https://thedfirreport.com/services/dfir-labs/): Offers cloud-based, hands-on learning experiences, using real data, from real intrusions. Interactive labs are available with different difficulty levels and can be accessed on-demand, accommodating various learning speeds.

[Contact us](https://thedfirreport.com/contact/) today for pricing or a demo!

#### Table of Contents:

* [Case Summary](#case-summary)
* [Services](#services)
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

The intrusion began in December 2023, with the initial sign being the execution of an unusually large-sized Cobalt Strike beacon. After the beacon’s execution, there was no immediate follow-up activity. The initial access delivery method for the intrusion remains unclear, as there was no evidence available. The Cobalt Strike C2 traffic beaconed to IP addresses managed by CloudFlare, which acted as proxy server between the victim network and their team server.

Approximately six hours after the initial execution, the threat actor used Windows utilities, such as systeminfo and nltest to perform enumeration on the system and environment. After, they conducted AS-REP Roasting and Kerberoasting attacks against two of the domain controllers, utilizing Rubeus, which was executed in memory via Cobalt Strike. Following this, the threat actor ran Sharphound in memory through the Cobalt Strike beacon, and saved the output to disk.

Around ten minutes after the initial discovery, the threat actor carried out their first lateral movement. They transferred a Cobalt Strike beacon via SMB and executed it through a service to compromise another workstation. On that workstation, they accessed LSASS to obtain credentials fr...