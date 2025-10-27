---
title: ShareFinder: How Threat Actors Discover File Shares
url: https://thedfirreport.com/2023/01/23/sharefinder-how-threat-actors-discover-file-shares/
source: The DFIR Report
date: 2023-01-24
fetch_date: 2025-10-04T04:37:49.179420
---

# ShareFinder: How Threat Actors Discover File Shares

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

Friday, October 03, 2025

Menu

* [Threat Intelligence](https://thedfirreport.com/services/threat-intelligence/)
* [Detection Rules](https://thedfirreport.com/services/detection-rules/)
* [DFIR Labs](https://thedfirreport.com/services/dfir-labs/)
  + [Digital Forensics Challenge](https://thedfirreport.com/services/dfir-labs/ctf/)
  + [Leaderboard](https://thedfirreport.com/services/dfir-labs/dfir-labs-leaderboard/)
  + [Digital Forensics Challenge Winners](https://thedfirreport.com/services/dfir-labs/digital-forensics-challenge-winners/)
  + [Testimonials](https://thedfirreport.com/services/dfir-labs/testimonials/)
* [Case Artifacts](https://thedfirreport.com/services/case-artifacts/)

[sharefinder](https://thedfirreport.com/category/tools/sharefinder-tools/)
[Tools](https://thedfirreport.com/category/tools/)

# ShareFinder: How Threat Actors Discover File Shares

[January 23, 2023](https://thedfirreport.com/2023/01/23/sharefinder-how-threat-actors-discover-file-shares/)

Many of our reports focus on adversarial Tactics, Techniques, and Procedures (TTPs) along with the tools associated with them. After gaining a foothold in an environment, one challenge for all threat actors is discovery. One common target for discovery is the enumeration of network shares. Network shares are common targets of an intrusion to facilitate later actions on objectives such as data exfiltration or targets for ransomware encryption.

For this reason, it is important for defenders to be able to detect and proactively hunt for signs of any unauthorized network share discovery in order to mitigate the impacts of data exfiltration and anything that may follow it, such as ransomware. In this report, we’ll be profiling a commonly used tool for discovering shares in a network, the PowerShell script Invoke-ShareFinder, which we will call ShareFinder throughout the report. This publication will delve into the specific characteristics of the underlying mechanism Invoke-ShareFinder uses to enumerate network shares. This is vital for defenders to understand to detect Invoke-ShareFinder and similar tools in their environments.

## [The DFIR Report Services](https://thedfirreport.com/2024/06/10/icedid-brings-screenconnect-and-csharp-streamer-to-alphv-ransomware-deployment/#services)

* **[Private Threat Briefs](https://thedfirreport.com/services/threat-intelligence/#threat-brief):** Over 20 private reports annually, such as this one but more concise and quickly published post-intrusion.
* **[Threat Feed](https://thedfirreport.com/services/threat-intelligence/#threat-feed):** Focuses on tracking Command and Control frameworks like Cobalt Strike, Metasploit, Sliver, etc.
* **[All Intel](https://thedfirreport.com/services/threat-intelligence/#all-intel):** Includes everything from Private Threat Briefs and Threat Feed, plus private events, long-term tracking, data clustering, and other curated intel.
* **[Private Sigma Ruleset](https://thedfirreport.com/services/detection-rules/):** Features 100+ Sigma rules derived from 40+ cases, mapped to ATT&CK with test examples.
* **[DFIR Labs](https://thedfirreport.com/services/dfir-labs/):** Offers cloud-based, hands-on learning experiences, using real data, from real intrusions. Interactive labs are available with different difficulty levels and can be accessed on-demand, accommodating various learning speeds.

[Contact us](https://thedfirreport.com/contact/) today for a demo!

## Analysts

Report by [@iiamaleks](https://twitter.com/iiamaleks)

Reviewed by [@samaritan\_o](https://twitter.com/samaritan_o)

## [What is Invoke-ShareFinder?](#what-is-invoke-sharefinder)

ShareFinder has been a common theme in our reports and has generally been paired with both enumeration of network resources and exfiltration of data. In the past year, we have reported on it being used in around 40% of our [reported intrusion cases](https://thedfirreport.com/?s=sharefinder).

ShareFinder was originally part of the [PowerView](https://powersploit.readthedocs.io/en/stable/Recon/README/) module of the [PowerSploit framework](https://github.com/PowerShellMafia/PowerSploit). However, now it has been included in various other projects and is in wide use across both red teams and many threat actors. Throughout 2022, we had multiple cases that featured ShareFinder, including:

* <https://thedfirreport.com/2022/11/28/emotet-strikes-again-lnk-file-leads-to-domain-wide-ransomware/>
* <https://thedfirreport.com/2022/11/14/bumblebee-zeros-in-on-meterpreter/>
* <https://thedfirreport.com/2022/09/26/bumblebee-round-two/>
* <https://thedfirreport.com/2022/08/08/bumblebee-roasts-its-way-to-domain-admin/>
* <https://thedfirreport.com/2022/04/04/stolen-images-campaign-ends-in-conti-ransomware/>

In these cases, ShareFinder had been observed being directly executed on an endpoint using Powershell. The example below demonstrates this behavior, in which the threat actor has taken steps to save the result of the “`Invoke-ShareFinder -CheckShareAccess`” command to a txt file named shares:

```
Invoke-ShareFinder -CheckShareAccess -Verbose | Out-File -Encoding ascii C:\ProgramData\shares.txt"
```

We can see from the [Conti leaks](https://twitter.com/TheDFIRRep...