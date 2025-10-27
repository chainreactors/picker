---
title: Navigating Through The Fog
url: https://thedfirreport.com/2025/04/28/navigating-through-the-fog/
source: The DFIR Report
date: 2025-04-29
fetch_date: 2025-10-06T22:02:53.162658
---

# Navigating Through The Fog

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

[ransomware](https://thedfirreport.com/category/ransomware/)
[sliver](https://thedfirreport.com/category/sliver/)

# Navigating Through The Fog

[April 28, 2025](https://thedfirreport.com/2025/04/28/navigating-through-the-fog/)

## Key Takeaways

* An open directory associated with a ransomware affiliate, likely linked to the Fog ransomware group, was discovered in December 2024. It contained tools and scripts for reconnaissance, exploitation, lateral movement, and persistence.
* Initial access was gained using compromised SonicWall VPN credentials, while other offensive tools facilitated credential theft, exploitation of Active Directory vulnerabilities, and lateral movement.
* Persistence was maintained through AnyDesk, automated by a PowerShell script that preconfigured remote access credentials.
* Sliver C2 executables were hosted on the server for command-and-control operations, alongside Proxychains tunneling.
* The victims spanned multiple industries, including technology, education, and logistics, across Europe, North America, and South America, highlighting the affiliate’s broad targeting scope.

This report was previously provided to our All Intel customers as a Threat Actor Insight Report. If you’re interested in receiving reports like this, please [contact us](https://thedfirreport.com/contact/).

## [The DFIR Report Services](#services)

* [Private Threat Briefs](https://thedfirreport.com/services/threat-intelligence/#threat-brief): 20+ private DFIR reports annually.
* [Threat Feed](https://thedfirreport.com/services/threat-intelligence/#threat-feed): Focuses on tracking Command and Control frameworks like Cobalt Strike, Metasploit, Sliver, etc.
* [All Intel](https://thedfirreport.com/services/threat-intelligence/#all-intel): Includes everything from Private Threat Briefs and Threat Feed, plus private events, Threat Actor Insights reports, long-term tracking, data clustering, and other curated intel.
* [Private Sigma Ruleset](https://thedfirreport.com/services/detection-rules/): Features 180+ Sigma rules derived from 50+ cases, mapped to ATT&CK with test examples.
* [DFIR Labs](https://thedfirreport.com/services/dfir-labs/): Offers cloud-based, hands-on learning experiences, using real data, from real intrusions. Interactive labs are available with different difficulty levels and can be accessed on-demand, accommodating various learning speeds.

[Contact us](https://thedfirreport.com/contact/) today for pricing or demo!

#### Table of Contents:

* [Case Summary](#case-summary)
* [Services](#services)
* [Analysts](#analysts)
* [Adversary](#adversary)
* [Infrastructure](#infrastructure)
* [Capabilities](#capabilities)
* [Victims](#victim)
* [Diamond Model](#diamond-model)
* [Indicators](#indicators)
* [MITRE ATT&CK](#mitre)

## [Case Summary](#case-summary)

The DFIR Report’s Threat Intel Group identified an open directory in December 2024, hosted at 194.48.154.79:80. The directory was likely linked to a ransomware operator associated with the Fog group, first observed in mid-2024. Analysis of its contents revealed a comprehensive toolkit used for reconnaissance, exploitation, credential theft, and command-and-control activities.

Among the tools were SonicWall Scanner for exploiting VPN credentials, DonPAPI for extracting Windows DPAPI-protected credentials, Certipy for abusing Active Directory Certificate Services (AD CS), Zer0dump, and Pachine/noPac for exploiting Active Directory vulnerabilities like CVE-2020-1472.

The affiliate also leveraged AnyDesk for persistence through an automated PowerShell script and hosted Sliver C2 components on the server for managing implants. Proxychains and Powercat were used to facilitate stealthy lateral movement and reverse shells. Victim data found in the directory indicated targets across multiple industries, including technology, education, and logistics, with a geographic focus on Italy, Greece, Brazil, and the USA.

Further information about Fog ransomware can be found at the following blog posts: [Arctic Wolf](https://arcticwolf.com/resources/blog/lost-in-the-fog-a-new-ransomware-threat/), [SentinelOne](https://www.sentinelone.com/anthology/fog/) and [any.run](https://any.run/malware-trends/fog/).

## [Analysts](#analysts)

Analysis and reporting completed by [Angelo\_Violetti](https://www.linkedin.com/in/angelo-violetti/), and reviewed by [Zach Stanford](https://www.linkedin.com/in/zach-stanford-57733296/).

## [Adversary](#adversary)

The DFIR Report’s Threat Intel Group assesses...