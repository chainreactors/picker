---
title: IcedID Brings ScreenConnect and CSharp Streamer to ALPHV Ransomware Deployment
url: https://thedfirreport.com/2024/06/10/icedid-brings-screenconnect-and-csharp-streamer-to-alphv-ransomware-deployment/
source: The DFIR Report
date: 2024-06-11
fetch_date: 2025-10-06T16:55:10.779852
---

# IcedID Brings ScreenConnect and CSharp Streamer to ALPHV Ransomware Deployment

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

[alphv](https://thedfirreport.com/category/ransomware/alphv/)
[cobaltstrike](https://thedfirreport.com/category/cobaltstrike/)
[icedid](https://thedfirreport.com/category/icedid/)
[ransomware](https://thedfirreport.com/category/ransomware/)

# IcedID Brings ScreenConnect and CSharp Streamer to ALPHV Ransomware Deployment

[June 10, 2024](https://thedfirreport.com/2024/06/10/icedid-brings-screenconnect-and-csharp-streamer-to-alphv-ransomware-deployment/)

## [Key Takeaways](#key)

* In October 2023, we observed an intrusion that began with a spam campaign, distributing a forked IcedID loader.
* The threat actor used Impacket’s wmiexec and RDP to install ScreenConnect on multiple systems, enabling them to execute various commands and deploy Cobalt Strike beacons.
* Their toolkit also included CSharp Streamer, a RAT written in CSharp with numerous functionalities, as documented [here](https://cyber.wtf/2023/12/06/the-csharp-streamer-rat/).
* The attacker used a custom tool to stage, and exfiltrate data, using Rclone.
* Eight days after initial access, ALPHV ransomware was deployed across all domain joined Windows systems.

An audio version of this report can be found on [Spotify](https://podcasters.spotify.com/pod/show/the-dfir-report/), [Apple](https://podcasts.apple.com/us/podcast/reports/id1728699064), [YouTube](https://www.youtube.com/%40TheDFIRReport/videos), [Audible](https://www.audible.com/pd/Reports-Podcast/B0CSZBRCFX?action_code=ASSGB149080119000H&share_location=pdp), & [Amazon](https://music.amazon.com/podcasts/c4fe897d-a4b4-4ceb-908d-d1a78af8cb6d/reports).

## [The DFIR Report Services](#services)

→ Click [here](https://the-dfir-report-store.myshopify.com/products/icedid-brings-screenconnect-and-csharp-streamer-to-alphv-ransomware-deployment-public-case-24952) to access the DFIR Lab related to this report ←

Five new sigma rules were created from this report and added to our Private sigma Rules

Our Threat Feed was tracking the Cobalt Strike server in this case days before this case.

* **[Private Threat Briefs](https://thedfirreport.com/services/threat-intelligence/#threat-brief):** Over 25 private reports annually, such as this one but more concise and quickly published post-intrusion.
* **[Threat Feed](https://thedfirreport.com/services/threat-intelligence/#threat-feed):** Focuses on tracking Command and Control frameworks like Cobalt Strike, Metasploit, Sliver, etc.
* **[All Intel](https://thedfirreport.com/services/threat-intelligence/#all-intel):** Includes everything from Private Threat Briefs and Threat Feed, plus private events, long-term tracking, data clustering, and other curated intel.
* **[Private Sigma Ruleset](https://thedfirreport.com/services/detection-rules/):** Features 100+ Sigma rules derived from 40+ cases, mapped to ATT&CK with test examples.
* **[DFIR Labs](https://thedfirreport.com/services/dfir-labs/):** Offers cloud-based, hands-on learning experiences, using real data, from real intrusions. Interactive labs are available with different difficulty levels and can be accessed on-demand, accommodating various learning speeds.

[Contact us](https://thedfirreport.com/contact/) today for a demo!

#### Table of Contents:

* [Case Summary](#case-summary)
* [The DFIR Report Services](#services)
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

This intrusion began in October 2023 with a malicious email that enticed the recipient to download a zip archive containing a Visual Basic Script (VBS) and a benign README file. We assess with high confidence that this email was part of a spam campaign delivering a forked variant of IcedID. First reported by [ProofPoint](https://www.proofpoint.com/us/blog/threat-insight/fork-ice-new-era-icedid) in February 2023, this forked IcedID variant lacks banking functionality and prioritizes payload delivery. Upon user interaction with the archive’s contents, the VBS file was executed, initiating the embedded forked IcedID loader....