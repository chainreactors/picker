---
title: Threat Actors’ Toolkit: Leveraging Sliver, PoshC2 & Batch Scripts
url: https://thedfirreport.com/2024/08/12/threat-actors-toolkit-leveraging-sliver-poshc2-batch-scripts/
source: Over Security - Cybersecurity news aggregator
date: 2024-08-13
fetch_date: 2025-10-06T18:08:34.636041
---

# Threat Actors’ Toolkit: Leveraging Sliver, PoshC2 & Batch Scripts

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

[opendir](https://thedfirreport.com/category/opendir/)

# Threat Actors’ Toolkit: Leveraging Sliver, PoshC2 & Batch Scripts

[August 12, 2024](https://thedfirreport.com/2024/08/12/threat-actors-toolkit-leveraging-sliver-poshc2-batch-scripts/)

## Key Takeaways

* In early December of 2023, we discovered an open directory filled with batch scripts, primarily designed for defense evasion and executing command and control payloads. These scripts execute various actions, including disabling antivirus processes and stopping services related to SQL, Hyper-V, security tools, and Exchange servers.
* This report also highlights scripts responsible for erasing backups, wiping event logs, and managing the installation or removal of remote monitoring tools like Atera.
* Our investigation uncovered the use of additional tools, including Ngrok for proxy services, SystemBC, and two well-known command and control frameworks: Sliver and PoshC2.
* The observed servers show long term usage by the threat actors, appearing in The DFIR Report Threat Feeds as far back as September 2023. They have been active intermittently since then, with the most recent activity detected in August 2024.
* Ten new sigma rules were created from this report and added to our private sigma ruleset

An audio version of this report can be found on [Spotify](https://podcasters.spotify.com/pod/show/the-dfir-report/), [Apple](https://podcasts.apple.com/us/podcast/reports/id1728699064), [YouTube](https://www.youtube.com/%40TheDFIRReport/videos), [Audible](https://www.audible.com/pd/Reports-Podcast/B0CSZBRCFX?action_code=ASSGB149080119000H&share_location=pdp), & [Amazon](https://music.amazon.com/podcasts/c4fe897d-a4b4-4ceb-908d-d1a78af8cb6d/reports).

## The DFIR Report Services

* [Private Threat Briefs](https://thedfirreport.com/services/threat-intelligence/#threat-brief): Over 20 private DFIR reports annually.
* [Threat Feed](https://thedfirreport.com/services/threat-intelligence/#threat-feed): Focuses on tracking Command and Control frameworks like Cobalt Strike, Metasploit, Sliver, etc.
* [All Intel](https://thedfirreport.com/services/threat-intelligence/#all-intel): Includes everything from Private Threat Briefs and Threat Feed, plus private events, opendir reports, long-term tracking, data clustering, and other curated intel.
* [Private Sigma Ruleset](https://thedfirreport.com/services/detection-rules/): Features 100+ Sigma rules derived from 40+ cases, mapped to ATT&CK with test examples.
* [DFIR Labs](https://thedfirreport.com/services/dfir-labs/): Offers cloud-based, hands-on learning experiences, using real data, from real intrusions. Interactive labs are available with different difficulty levels and can be accessed on-demand, accommodating various learning speeds.

[Contact us](https://thedfirreport.com/contact/) today for pricing or a demo!

**Table of Contents:**

* [Summary](#summary)
* [Analysts](#analysts)
* [Adversary](#adversary)
* [Infrastructure](#infrastructure)
* [Capability](#capability)
* [Victim](#victim)
* [Indicators](#iocs)

## [Summary](#summary)

In this report, we delve into an open directory on 94.198.53.143, first observed on December 10, 2023, during our intelligence collection process. Prior to the open directory appearing, this address had appeared in our threat intelligence feeds for PoshC2 command and control. It first appeared on September 21, 2023 and has been intermittently active, most recently on August 11, 2024, showing that the infrastructure is being utilized over a long timeframe.

Besides PoshC2, the threat actor identified utilized a range of batch scripts and malware to compromise both Windows and Linux systems. Their toolkit featured scripts such as atera\_del.bat and atera\_del2.bat to remove Atera agents, backup.bat and delbackup.bat to delete system backups and shadow copies, and clearlog.bat to erase Windows event logs and associated data.

The actor employed cmd.cmd to disable User Account Control and modify registry settings, while scripts like def1.bat and defendermalwar.bat are used to disable Windows Defender, scheduled tasks, and uninstall Malwarebytes. They also utilized tools such as Ngrok for proxy purposes, Posh\_v2\_dropper\_x64.exe for PowerShell-based command-and-control operations, and VmManagedSetup.exe, which contains SystemBC malware.

The threat actor further disrupted systems by stopping and disabling various critical services, using scripts like disable.bat and hyp.bat, and logging off user sessions with LOGOFA...