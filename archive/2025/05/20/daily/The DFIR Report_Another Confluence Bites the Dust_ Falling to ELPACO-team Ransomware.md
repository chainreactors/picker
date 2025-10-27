---
title: Another Confluence Bites the Dust: Falling to ELPACO-team Ransomware
url: https://thedfirreport.com/2025/05/19/another-confluence-bites-the-dust-falling-to-elpaco-team-ransomware/
source: The DFIR Report
date: 2025-05-20
fetch_date: 2025-10-06T22:23:32.672268
---

# Another Confluence Bites the Dust: Falling to ELPACO-team Ransomware

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

[elpacoteam](https://thedfirreport.com/category/ransomware/elpacoteam/)
[mimic](https://thedfirreport.com/category/ransomware/mimic/)
[ransomware](https://thedfirreport.com/category/ransomware/)

# Another Confluence Bites the Dust: Falling to ELPACO-team Ransomware

[May 19, 2025](https://thedfirreport.com/2025/05/19/another-confluence-bites-the-dust-falling-to-elpaco-team-ransomware/)

## [Key Takeaways](https://thedfirreport.com/?p=43853&preview=true#key)

* The threat actor first gained entry by exploiting a known vulnerability (CVE-2023-22527) on an internet-facing Confluence server, allowing for remote code execution.
* Using this access, the threat actor executed a consistent sequence of commands (installing AnyDesk, adding admin users, and enabling RDP) multiple times, suggesting the use of automation scripts or a playbook.
* Tools like Mimikatz, ProcessHacker, and Impacket Secretsdump were used to harvest credentials.
* The intrusion culminated in the deployment of ELPACO-team ransomware, a Mimic variant, approximately 62 hours after the initial Confluence exploitation.
* While ransomware was deployed and some event logs were deleted, no significant exfiltration of data was observed during the intrusion.

This case was featured in our December 2024 [DFIR Labs CTF](https://thedfirreport.com/services/dfir-labs/ctf/) and is available as a lab today [here](https://store.thedfirreport.com/products/alpaca-ransomware-private-case-30043). It was originally published as a [Threat Brief](https://thedfirreport.com/services/threat-intelligence/#threat-brief) to customers in October 2024.

## [The DFIR Report Services](https://thedfirreport.com/services/)

* [Private Threat Briefs](https://thedfirreport.com/services/threat-intelligence/#threat-brief): 20+ private DFIR reports annually.
* [Threat Feed](https://thedfirreport.com/services/threat-intelligence/#threat-feed): Focuses on tracking Command and Control frameworks like Cobalt Strike, Metasploit, Sliver, etc.
* [All Intel](https://thedfirreport.com/services/threat-intelligence/#all-intel): Includes everything from Private Threat Briefs and Threat Feed, plus private events, Threat Actor Insights reports, long-term tracking, data clustering, and other curated intel.
* [Private Sigma Ruleset](https://thedfirreport.com/services/detection-rules/): Features 170+ Sigma rules derived from 50+ cases, mapped to ATT&CK with test examples.
* [DFIR Labs](https://thedfirreport.com/services/dfir-labs/): Offers cloud-based, hands-on learning experiences, using real data, from real intrusions. Interactive labs are available with different difficulty levels and can be accessed on-demand, accommodating various learning speeds.

[Contact us](https://thedfirreport.com/contact/) today for pricing or a demo!

#### Table of Contents:

* [Case Summary](https://thedfirreport.com/?p=43853&preview=true#case-summary)
* [Analysts](https://thedfirreport.com/?p=43853&preview=true#analysts)
* [Initial Access](https://thedfirreport.com/?p=43853&preview=true#initial-access)
* [Execution](https://thedfirreport.com/?p=43853&preview=true#execution)
* [Persistence](https://thedfirreport.com/?p=43853&preview=true#persistence)
* [Privilege Escalation](https://thedfirreport.com/?p=43853&preview=true#privilege-escalation)
* [Defense Evasion](https://thedfirreport.com/?p=43853&preview=true#defense-evasion)
* [Credential Access](https://thedfirreport.com/?p=43853&preview=true#credential-access)
* [Discovery](https://thedfirreport.com/?p=43853&preview=true#discovery)
* [Lateral Movement](https://thedfirreport.com/?p=43853&preview=true#lateral-movement)
* [Command and Control](https://thedfirreport.com/?p=43853&preview=true#command-and-control)
* [Exfiltration](https://thedfirreport.com/?p=43853&preview=true#exfiltration)
* [Impact](https://thedfirreport.com/?p=43853&preview=true#impact)
* [Timeline](https://thedfirreport.com/?p=43853&preview=true#timeline)
* [Diamond Model](https://thedfirreport.com/?p=43853&preview=true#diamond-model)
* [Indicators](https://thedfirreport.com/?p=43853&preview=true#indicators)
* [Detections](https://thedfirreport.com/?p=43853&preview=true#detections)
* [MITRE ATT&CK](https://thedfirreport.com/?p=43853&preview=true#mitre)

## [Case Summary](https://thedfirreport.com/?p=43853&preview=true#case-summary)

In late June 2024, an unpatched Confluence server was compromised via CVE-2023-22527, a template injection vulnerability, first from IP address 45.227.254[.]124, which just ran whoami and exited. Short...