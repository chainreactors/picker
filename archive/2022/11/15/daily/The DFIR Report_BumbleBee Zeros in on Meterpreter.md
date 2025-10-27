---
title: BumbleBee Zeros in on Meterpreter
url: https://thedfirreport.com/2022/11/14/bumblebee-zeros-in-on-meterpreter/
source: The DFIR Report
date: 2022-11-15
fetch_date: 2025-10-03T22:43:52.001449
---

# BumbleBee Zeros in on Meterpreter

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

[adfind](https://thedfirreport.com/category/adfind/)
[bumblebee](https://thedfirreport.com/category/bumblebee/)
[cobaltstrike](https://thedfirreport.com/category/cobaltstrike/)
[Meterpreter](https://thedfirreport.com/category/meterpreter/)

# BumbleBee Zeros in on Meterpreter

[November 14, 2022](https://thedfirreport.com/2022/11/14/bumblebee-zeros-in-on-meterpreter/)

In this intrusion from May 2022, the threat actors used [BumbleBee](https://malpedia.caad.fkie.fraunhofer.de/details/win.bumblebee) as the initial access vector from a Contact Forms campaign. We have previously reported on two BumbleBee intrusions ([1](https://thedfirreport.com/2022/08/08/bumblebee-roasts-its-way-to-domain-admin/), [2](https://thedfirreport.com/2022/09/26/bumblebee-round-two/)), and this report is a continuation of a series of reports uncovering multiple TTPs seen by BumbleBee post exploitation operators.

The intrusion began with the delivery of an ISO file that contained an LNK and a DLL. The threat actors leveraged BumbleBee to load a Meterpreter agent and Cobalt Strike Beacons. They then performed reconnaissance, used two different UAC bypass techniques, dumped credentials, escalated privileges using a ZeroLogon exploit, and moved laterally through the environment.

## [The DFIR Report Services](#services)

* [Private Threat Briefs](https://thedfirreport.com/services/threat-intelligence/#threat-brief): Over 20 private DFIR reports annually.
* [Threat Feed](https://thedfirreport.com/services/threat-intelligence/#threat-feed): Focuses on tracking Command and Control frameworks like Cobalt Strike, Metasploit, Sliver, etc.
* [All Intel](https://thedfirreport.com/services/threat-intelligence/#all-intel): Includes everything from Private Threat Briefs and Threat Feed, plus private events, opendir reports, long-term tracking, data clustering, and other curated intel.
* [Private Sigma Ruleset](https://thedfirreport.com/services/detection-rules/): Features 100+ Sigma rules derived from 40+ cases, mapped to ATT&CK with test examples.
* [DFIR Labs](https://thedfirreport.com/services/dfir-labs/): Offers cloud-based, hands-on learning experiences, using real data, from real intrusions. Interactive labs are available with different difficulty levels and can be accessed on-demand, accommodating various learning speeds.

[Contact us](https://thedfirreport.com/contact/) today for pricing or a demo!

## Case Summary

The intrusion started with a contact form on a website. It has been reported that this delivery method has been in use for intrusions [since at least 2020](https://therecord.media/microsoft-malware-gang-uses-website-contact-forms-for-distribution/). This campaign took place in May, and appears to have run as late as June 2022, based on OSINT data related to similar delivery fingerprints. The contact form gets filled out by the threat actor with a Copyright notice, purporting a violation of the Digital Millennium Copyright Act (DMCA). It then encourages the recipient to download a file showing the purported violation.

Upon the user clicking the link, they arrive at a “Google” storage site on storage.googleapis.com. A zip file is then downloaded to the victim machine and once unzipped the user is presented with an ISO file. The ISO contains a LNK file and a DLL file. When the LNK is double-clicked, the BumbleBee DLL is executed via rundll32. Initially, contact was made with BumbleBee command and control servers but little other early activity was observed.

Approximately 12 hours later, ImagingDevices.exe was launched via WmiPrivse.exe and a Meterpreter agent was injected into the process, like we have observed in [previous reports](https://thedfirreport.com/2022/09/26/bumblebee-round-two/). This process then utilized nltest, net, tasklist, and whoami to perform reconnaissance. About 37 minutes after launching ImagingDevices.exe, the Meterpreter agent migrated to svchost.exe. Upon migrating to the svchost process, there were attempts to bypass UAC and launch a Meterpreter executable.

Several failed attempts to bypass UAC occurred, utilizing the [WSReset method,](https://lolbas-project.github.io/lolbas/Binaries/Wsreset/) followed by a failed attempt to bypass UAC utilizing the [slui hijacking method](https://github.com/rapid7/metasploit-framework/blob/master/modules/exploits/windows/local/bypassuac_sluihijack.rb). Finally, the threat actors succeeded on their final attempt, using the WSReset method. Once UAC was bypassed, Meterpreter’s getsystem command was ...