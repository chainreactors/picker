---
title: Inside the Open Directory of the “You Dun” Threat Group
url: https://thedfirreport.com/2024/10/28/inside-the-open-directory-of-the-you-dun-threat-group/
source: Over Security - Cybersecurity news aggregator
date: 2024-10-29
fetch_date: 2025-10-06T18:54:55.780355
---

# Inside the Open Directory of the “You Dun” Threat Group

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
[opendir](https://thedfirreport.com/category/opendir/)

# Inside the Open Directory of the “You Dun” Threat Group

[October 28, 2024](https://thedfirreport.com/2024/10/28/inside-the-open-directory-of-the-you-dun-threat-group/)

## [Key Takeaways](#key)

* Analysis of an open directory found a Chinese speaking threat actor’s toolkit and history of activity.
* The threat actor displayed extensive scanning and exploitation using WebLogicScan, Vulmap, and Xray, targeting organizations in South Korea, China, Thailand, Taiwan, and Iran.
* The Viper C2 framework was present as well as a Cobalt Strike kit which included TaoWu and Ladon extensions.
* The Leaked LockBit 3 builder was used to create a LockBit payload with a custom ransom note that included reference to a Telegram group which we investigated further in the report.

An audio version of this report can be found on [Spotify](https://podcasters.spotify.com/pod/show/the-dfir-report/), [Apple](https://podcasts.apple.com/us/podcast/reports/id1728699064), [YouTube](https://www.youtube.com/%40TheDFIRReport/videos), [Audible](https://www.audible.com/pd/Reports-Podcast/B0CSZBRCFX?action_code=ASSGB149080119000H&share_location=pdp), & [Amazon](https://music.amazon.com/podcasts/c4fe897d-a4b4-4ceb-908d-d1a78af8cb6d/reports).

## [The DFIR Report Services](#services)

Reports such as this one are part of our All Intel service and are categorized as Threat Actor Insights.

* [Private Threat Briefs](https://thedfirreport.com/services/threat-intelligence/#threat-brief): Over 20 private DFIR reports annually.
* [Threat Feed](https://thedfirreport.com/services/threat-intelligence/#threat-feed): Focuses on tracking Command and Control frameworks like Cobalt Strike, Metasploit, Sliver, etc.
* [All Intel](https://thedfirreport.com/services/threat-intelligence/#all-intel): Includes everything from Private Threat Briefs and Threat Feed, plus private events, Threat Actor Insights reports, long-term tracking, data clustering, and other curated intel.
* [Private Sigma Ruleset](https://thedfirreport.com/services/detection-rules/): Features 100+ Sigma rules derived from 40+ cases, mapped to ATT&CK with test examples.
* [DFIR Labs](https://thedfirreport.com/services/dfir-labs/): Offers cloud-based, hands-on learning experiences, using real data, from real intrusions. Interactive labs are available with different difficulty levels and can be accessed on-demand, accommodating various learning speeds.

#### Table of Contents:

* [Case Summary](#case-summary)
* [Services](#services)
* [Analysts](#analysts)
* [Capability](#capability)
* [Victims](#victims)
* [Infrastructure](#infrastructure)
* [Adversary](#adversary)
* [Diamond Model](#diamond-model)
* [Indicators](#indicators)
* [MITRE ATT&CK](#mitre)

## [Case Summary](#case-summary)

The DFIR Report’s Threat Intel Team detected an open directory in January 2024 and analyzed it for trade craft and threat actor activity. Once reviewed, we identified it was related to the Chinese speaking hacking group that call themselves “You Dun”.

The threat actor conducted various activities using the host we investigated which included reconnaissance and web exploitation activities. Using tools such as WebLogicScan, Vulmap, and Xray, they were able to identify numerous vulnerable servers. They exploited several websites running Zhiyuan OA software and used SQLmap to conduct SQL injection.

We found evidence of several successful exploitation attempts. After gaining access we found use of further tools to try and use various exploits to elevate privileges on the compromised hosts, including the use of [traitor](https://github.com/liamg/traitor) for Linux privilege escalation exploits and [CDK](https://github.com/cdk-team/CDK) for docker and kubernetes privilege escalation.

Both Cobalt Strike and Viper framework files were visible in the open directory. A zip archive that contained the files for a Cobalt Strike team server, included the plugins TaoWu and Ladon which extend the capabilities of the framework greatly. The DFIR Report [Threat Intel Team](https://thedfirreport.com/services/threat-intelligence/) tracked the server as hosting active command and control from January 18th through Feburary 10th of 2024. Using data from the leaked server we identified a cluster of eight IP address’s all being used to proxy the command and control for the same threat actor and active for the same time frame.

The threat actor al...