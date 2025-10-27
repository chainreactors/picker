---
title: Nitrogen Campaign Drops Sliver and Ends With BlackCat Ransomware
url: https://thedfirreport.com/2024/09/30/nitrogen-campaign-drops-sliver-and-ends-with-blackcat-ransomware/
source: Over Security - Cybersecurity news aggregator
date: 2024-10-01
fetch_date: 2025-10-06T18:58:13.174974
---

# Nitrogen Campaign Drops Sliver and Ends With BlackCat Ransomware

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

[blackcat](https://thedfirreport.com/category/blackcat/)
[cobaltstrike](https://thedfirreport.com/category/cobaltstrike/)
[ransomware](https://thedfirreport.com/category/ransomware/)
[sliver](https://thedfirreport.com/category/sliver/)

# Nitrogen Campaign Drops Sliver and Ends With BlackCat Ransomware

[September 30, 2024](https://thedfirreport.com/2024/09/30/nitrogen-campaign-drops-sliver-and-ends-with-blackcat-ransomware/)

## [Key Takeaways](#key)

* In November 2023, we identified a BlackCat ransomware intrusion started by Nitrogen malware hosted on a website impersonating Advanced IP Scanner.
* Nitrogen was leveraged to deploy Sliver and Cobalt Strike beacons on the beachhead host and perform further malicious actions. The two post-exploitation frameworks were loaded in memory through Python scripts.
* After obtaining initial access and establishing further command and control connections, the threat actor enumerated the compromised network with the use of PowerSploit, SharpHound, and native Windows utilities. Impacket was employed to move laterally, after harvesting domain credentials.
* The threat actor deployed an opensource backup tool call Restic on a file server to exfiltrate share data to a remote server.
* Eight days after initial access the threat actor modified a privileged user password and deployed BlackCat ransomware across the domain using PsExec to execute a batch script.
* Six rules were added to our Private Ruleset related to this intrusion.

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

The incident began when a user unknowingly downloaded a malicious version of Advanced IP Scanner from a fraudulent website that mimicked the legitimate one, leveraging Google ads to rank higher in search results. Analysis of the attack pattern and loader signature suggests this was part of a Nitrogen campaign, consistent with previous public reports. The compromised installer came as a ZIP file, which the victim extracted before launching the embedded executable, triggering the infection.

The executable was a legitimate Python binary, which side-loaded a modified Python DLL specifically designed to execute Nitrogen code. This process then dropped a Sliver beacon in an AppData subfolder named “Notepad.” All malware deployed during the intrusion was obfuscated ...