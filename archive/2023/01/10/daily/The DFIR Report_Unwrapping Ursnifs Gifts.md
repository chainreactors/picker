---
title: Unwrapping Ursnifs Gifts
url: https://thedfirreport.com/2023/01/09/unwrapping-ursnifs-gifts/
source: The DFIR Report
date: 2023-01-10
fetch_date: 2025-10-04T03:24:00.347672
---

# Unwrapping Ursnifs Gifts

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

[cobaltstrike](https://thedfirreport.com/category/cobaltstrike/)
[Exfiltrate Data](https://thedfirreport.com/category/exfiltrate-data/)
[ursnif](https://thedfirreport.com/category/ursnif/)
[wmiexec](https://thedfirreport.com/category/wmiexec/)

# Unwrapping Ursnifs Gifts

[January 9, 2023](https://thedfirreport.com/2023/01/09/unwrapping-ursnifs-gifts/)

In late August 2022, we investigated an incident involving Ursnif malware, which resulted in Cobalt Strike being deployed. This was followed by the threat actors moving laterally throughout the environment using an admin account.

The [Ursnif malware family](https://malpedia.caad.fkie.fraunhofer.de/details/win.gozi) (also commonly referred to as Gozi or ISFB) is one of the oldest banking trojans still active today. It has an extensive past of code forks and evolutions that has lead to several active variants in the last 5 years including Dreambot, IAP, RM2, RM3 and most recently, LDR4.

For this report, we have referred to the malware as Ursnif for simplicity, however we also recommend reading [Mandiant’s article on LDR4](https://www.mandiant.com/resources/blog/rm3-ldr4-ursnif-banking-fraud).

## [The DFIR Report Services](https://thedfirreport.com/2024/06/10/icedid-brings-screenconnect-and-csharp-streamer-to-alphv-ransomware-deployment/#services)

* **[Private Threat Briefs](https://thedfirreport.com/services/threat-intelligence/#threat-brief):** Over 20 private reports annually, such as this one but more concise and quickly published post-intrusion.
* **[Threat Feed](https://thedfirreport.com/services/threat-intelligence/#threat-feed):** Focuses on tracking Command and Control frameworks like Cobalt Strike, Metasploit, Sliver, etc.
* **[All Intel](https://thedfirreport.com/services/threat-intelligence/#all-intel):** Includes everything from Private Threat Briefs and Threat Feed, plus private events, long-term tracking, data clustering, and other curated intel.
* **[Private Sigma Ruleset](https://thedfirreport.com/services/detection-rules/):** Features 100+ Sigma rules derived from 40+ cases, mapped to ATT&CK with test examples.
* **[DFIR Labs](https://thedfirreport.com/services/dfir-labs/):** Offers cloud-based, hands-on learning experiences, using real data, from real intrusions. Interactive labs are available with different difficulty levels and can be accessed on-demand, accommodating various learning speeds.

[Contact us](https://thedfirreport.com/contact/) today for a demo!

## [Case Summary](#case-summary)

In this intrusion, a malicious ISO file was delivered to a user which contained Ursnif malware. The malware displayed an interesting execution flow, which included using a renamed copy of rundll32. Once executed, the malware conducted automatic discovery on the beachhead host, as we have observed with other loaders such as [IcedID](https://thedfirreport.com/2022/04/25/quantum-ransomware/). The malware also established persistence on the host with the creation of a registry run key.

Approximately 4 days after the initial infection, new activity on the host provided a clear distinction of a threat actor performing manual actions (hands on keyboard). The threat actor used a Background Intelligent Transfer Service (BITS) job to download a Cobalt Strike beacon, and then used the beacon for subsequent actions.

The threat actor first ran some initial discovery on the host using built-in Windows utilities like ipconfig, systeminfo, net, and ping. Shortly afterwards, the threat actor injected into various processes and then proceeded to access lsass memory on the host to extract credentials.

Using the credentials extracted from memory, the threat actors began to move laterally. They targeted a domain controller and used Impacket’s [wmiexec.py](https://github.com/fortra/impacket/blob/master/examples/wmiexec.py) to execute code on the remote host. This included executing both a msi installer for the RMM tools Atera and Splashtop, as well as a Cobalt Strike executable beacon. These files were transferred to the domain controller over SMB.

After connecting to the Cobalt Strike beacon on the domain controller, the threat actor executed another round of discovery tasks and dumped lsass memory on the domain controller. Finally, they dropped a script named `adcomp.bat` which executed a PowerShell command to collect data on computers in the Windows domain.

The following day, there was a short check-in on the beachhead host from a Cobalt Strike beacon, no other activity occurred until near t...