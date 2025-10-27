---
title: IcedID Macro Ends in Nokoyawa Ransomware
url: https://thedfirreport.com/2023/05/22/icedid-macro-ends-in-nokoyawa-ransomware/
source: The DFIR Report
date: 2023-05-23
fetch_date: 2025-10-04T11:36:50.343363
---

# IcedID Macro Ends in Nokoyawa Ransomware

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

Saturday, October 04, 2025

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
[cobaltstrike](https://thedfirreport.com/category/cobaltstrike/)
[icedid](https://thedfirreport.com/category/icedid/)
[macro](https://thedfirreport.com/category/macro/)
[nokoyawa](https://thedfirreport.com/category/ransomware/nokoyawa/)
[ransomware](https://thedfirreport.com/category/ransomware/)
[xls](https://thedfirreport.com/category/xls/)

# IcedID Macro Ends in Nokoyawa Ransomware

[May 22, 2023](https://thedfirreport.com/2023/05/22/icedid-macro-ends-in-nokoyawa-ransomware/)

Threat actors have moved to other means of initial access, such as ISO files combined with LNKs or OneNote payloads, but some appearances of VBA macros in Office documents can still be seen in use.

In this case we document an incident taking place during Q4 of 2022 consisting of threat actors targeting [Italian](https://twitter.com/reecdeep/status/1577979717717721088?s=20&t=QWDIpjACeLzPOEy4DDGnUQ) organizations with Excel maldocs that deploy IcedID. The threat actors deploying such a campaign may hope to target organizations who have not updated their Microsoft Office deployments after the newly released patches to [block macros on documents downloaded from the internet](https://learn.microsoft.com/en-us/deployoffice/security/internet-macros-blocked).

We have [previously](https://thedfirreport.com/2023/04/03/malicious-iso-file-leads-to-domain-wide-ransomware/) [reported](https://thedfirreport.com/2022/04/25/quantum-ransomware/) on IcedID intrusions that have migrated to ISO files, however, this report is one of the most recent that will focus on the traditional Excel/macro intrusion vector.

Once inside, the threat actors pivoted using Cobalt Strike and RDP before a domain wide deployment of Nokoyawa ransomware with the help of PsExec. Nokowaya ransomware is a family with ties to [Karma](https://www.sentinelone.com/labs/nokoyawa-ransomware-new-karma-nemty-variant-wears-thin-disguise/)/[Nemty](https://www.fortinet.com/blog/threat-research/nokoyawa-variant-catching-up).

## [The DFIR Report Services](https://thedfirreport.com/2024/06/10/icedid-brings-screenconnect-and-csharp-streamer-to-alphv-ransomware-deployment/#services)

* **[Private Threat Briefs](https://thedfirreport.com/services/threat-intelligence/#threat-brief):** Over 20 private reports annually, such as this one but more concise and quickly published post-intrusion.
* **[Threat Feed](https://thedfirreport.com/services/threat-intelligence/#threat-feed):** Focuses on tracking Command and Control frameworks like Cobalt Strike, Metasploit, Sliver, etc.
* **[All Intel](https://thedfirreport.com/services/threat-intelligence/#all-intel):** Includes everything from Private Threat Briefs and Threat Feed, plus private events, long-term tracking, data clustering, and other curated intel.
* **[Private Sigma Ruleset](https://thedfirreport.com/services/detection-rules/):** Features 100+ Sigma rules derived from 40+ cases, mapped to ATT&CK with test examples.
* **[DFIR Labs](https://thedfirreport.com/services/dfir-labs/):** Offers cloud-based, hands-on learning experiences, using real data, from real intrusions. Interactive labs are available with different difficulty levels and can be accessed on-demand, accommodating various learning speeds.

[Contact us](https://thedfirreport.com/contact/) today for a demo!

## [Case Summary](#case-summary)

This intrusion began with a malicious Excel document. We assess with medium-high confidence that this document was delivered as part of a malicious email campaign during the first half of October 2022, based on public reporting that overlaps with multiple characteristics observed. Upon opening the Excel document, the macros would be executed when a user clicked on an embedded image. The macro code was responsible for downloading and writing an IcedID DLL payload to disk. The macro then used a renamed rundll32 binary to execute the malicious DLL.

After reaching out to the initial command and control server, automated discovery ran from the IcedID process around two minutes after execution. This discovery used the same suite of Microsoft binaries as we have [previously](https://thedfirreport.com/2022/04/04/stolen-images-campaign-ends-in-conti-ransomware/) [reported](https://thedfirreport.com/2023/04/03/malicious-iso-file-leads-to-domain-wide-ransomware/) for the IcedID malware family. At this time, the malware also established persistence on the beachhead host using a scheduled task.

Around two hours after the initial ...