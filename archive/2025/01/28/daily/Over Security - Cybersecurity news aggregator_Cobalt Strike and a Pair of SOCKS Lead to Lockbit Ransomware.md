---
title: Cobalt Strike and a Pair of SOCKS Lead to Lockbit Ransomware
url: https://thedfirreport.com/2025/01/27/cobalt-strike-and-a-pair-of-socks-lead-to-lockbit-ransomware/
source: Over Security - Cybersecurity news aggregator
date: 2025-01-28
fetch_date: 2025-10-06T20:12:28.437372
---

# Cobalt Strike and a Pair of SOCKS Lead to Lockbit Ransomware

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

[cobaltstrike](https://thedfirreport.com/category/cobaltstrike/)
[lockbit](https://thedfirreport.com/category/lockbit/)
[ransomware](https://thedfirreport.com/category/ransomware/)

# Cobalt Strike and a Pair of SOCKS Lead to LockBit Ransomware

[January 27, 2025](https://thedfirreport.com/2025/01/27/cobalt-strike-and-a-pair-of-socks-lead-to-lockbit-ransomware/)

## Key Takeaways

* This intrusion began with the download and execution of a Cobalt Strike beacon that impersonated a Windows Media Configuration Utility.
* The threat actor used Rclone to exfiltrate data from the environment. First they attempted FTP transfers, that failed, before moving to using [MEGA.io](https://MEGA.io). A day later they ran a second successful FTP exfiltration.
* The threat actor created several persistent backdoors in the environment, using scheduled tasks, GhostSOCKS and SystemBC proxies, and Cobalt Strike command and control access.
* LockBit ransomware was deployed across the environment on the 11th day of the intrusion.

## [The DFIR Report Services](https://thedfirreport.com/2024/12/02/the-curious-case-of-an-egg-cellent-resume/#services)

Explore [this case](https://store.thedfirreport.com/products/lockbit-ransomware-private-case-27138) in-depth with our hands-on DFIR Labs!

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
* [Privilege Escalation](#privilege-escalation)
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

This intrusion began near the end of January 2024 when the user downloaded and executed a file using the same name (setup\_wm.exe) and executable icon, as the legitimate Microsoft Windows Media Configuration Utility. This executable was a Cobalt Strike beacon and, once executed, an outbound connection was established.

Approximately 30 minutes after the initial execution, the Cobalt Strike beacon initiated discovery commands, starting with nltest to identify domain controllers. Due to the elevated permissions of the initially compromised user, the threat actor leveraged SMB and remote services to deploy two proxy tools—SystemBC and GhostSOCKS—onto a domain controller.

Windows Defender detected these tools on the domain controller, initially leading us to believe that both were blocked. However, while GhostSOCKS was successfully prevented, the SystemBC proxy remained active, establishing a command and control channel from the domain controller. The threat actor then continued their operations from the beachhead host, executing additional situational awareness commands. They then injected code into the WUAUCLT.exe process and then extracted credentials from the LSASS process.

The injected process was observed loading the Seatbelt and SharpView CLR modules into its memory space. Simultaneously, the threat actor established persistence by creating scheduled tasks to execute the SystemBC and GhostSOCKS proxies on the beachhead host.

Approximately an hour into the intrusion, the threat actor moved laterally to a file server ...