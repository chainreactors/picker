---
title: A Truly Graceful Wipe Out
url: https://thedfirreport.com/2023/06/12/a-truly-graceful-wipe-out/
source: The DFIR Report
date: 2023-06-13
fetch_date: 2025-10-04T11:45:59.989249
---

# A Truly Graceful Wipe Out

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
[Attribution](https://thedfirreport.com/category/attribution/)
[cobaltstrike](https://thedfirreport.com/category/cobaltstrike/)
[Exfiltrate Data](https://thedfirreport.com/category/exfiltrate-data/)
[FIN11](https://thedfirreport.com/category/fin11/)
[FlawedGrace](https://thedfirreport.com/category/flawedgrace/)
[Lace Tempest](https://thedfirreport.com/category/lace-tempest/)
[truebot](https://thedfirreport.com/category/truebot/)

# A Truly Graceful Wipe Out

[June 12, 2023](https://thedfirreport.com/2023/06/12/a-truly-graceful-wipe-out/)

In this intrusion, dated May 2023, we observed [Truebot](https://malpedia.caad.fkie.fraunhofer.de/details/win.silence) being used to deploy Cobalt Strike and [FlawedGrace](https://malpedia.caad.fkie.fraunhofer.de/details/win.flawedgrace) (aka GraceWire & BARBWIRE) resulting in the exfiltration of data and the deployment of the MBR Killer wiper. The threat actors deployed the wiper within 29 hours of initial access.

## [Services](https://thedfirreport.com/2024/04/29/from-icedid-to-dagon-locker-ransomware-in-29-days/#services)

* **[Private Threat Briefs](https://thedfirreport.com/services/threat-intelligence/#threat-brief):** Over 25 private reports annually, such as this one but more concise and quickly published post-intrusion.
* **[Threat Feed](https://thedfirreport.com/services/threat-intelligence/#threat-feed):** Focuses on tracking Command and Control frameworks like Cobalt Strike, Metasploit, Sliver, etc.
* **[All Intel](https://thedfirreport.com/services/threat-intelligence/#all-intel):** Includes everything from Private Threat Briefs and Threat Feed, plus private events, long-term tracking, data clustering, and other curated intel.
* **[Private Sigma Ruleset](https://thedfirreport.com/services/detection-rules/):** Features 100+ Sigma rules derived from 40+ cases, mapped to ATT&CK with test examples.
* **[DFIR Labs](https://thedfirreport.com/services/dfir-labs/):** Offers cloud-based, hands-on learning experiences using real data from real intrusions. Interactive labs are available with different difficulty levels and can be accessed on-demand, accommodating various learning speeds.

Contact us today for a demo!

## [Case Summary](#case-summary)

In this case, Truebot was delivered through a Traffic Distribution System (TDS) reported by [Proofpoint as “404 TDS”](https://twitter.com/threatinsight/status/1666403634312105987?s=20). This campaign, observed in May 2023, leveraged email for the initial delivery mechanism. After clicking-through the link in an email, the victim would be redirected through a series of URLs before being presented a file download at the final landing page.

The file download was a Truebot executable, which appeared as a fake Adobe Acrobat document. After executing the file, Truebot copied and renamed itself. Minutes later, Truebot loaded FlawedGrace onto the host. While loading this malware, it used a series of modifications to the registry and Print Spooler service to both escalate privileges and establish persistence. From there, FlawedGrace’s execution routine involved storing as well as extracting, encoded and encrypted payloads in registry; the creation of temporary scheduled tasks and the injection of the final payload into msiexec.exe and svchost.exe.

After this execution, the threat actors proceeded to disable Windows Defender Real-Time monitoring and added exclusions for executable files on the host. We later observed FlawedGrace creating a temporary user within the local Administrators and Remote Desktop Users groups. With this user, a tunneled RDP connection was attempted from FlawedGrace’s C2 servers. Seemingly without success, the threat actors removed the user after 15 minutes before repeating the procedure a second time. After the second failed attempt, the threat actors removed the user and did not attempt further RDP communications. The FlawedGrace process then performed discovery surrounding the domain administrators and domain controllers.

Approximately two hours after the initial execution, Truebot loaded Cobalt Strike into memory and then went dormant for the next two hours. This ended the use of Truebot for the rest of the intrusion, with FlawedGrace and Cobalt Strike being leveraged for the rest of the threat actors activity. Now, four hours into the intrusion the threat actors, through the Cobalt Strike beacon, started another round of discovery commands using net, nltest, tasklist and AdFind...