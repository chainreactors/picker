---
title: Emotet Strikes Again – LNK File Leads to Domain Wide Ransomware
url: https://thedfirreport.com/2022/11/28/emotet-strikes-again-lnk-file-leads-to-domain-wide-ransomware/
source: The DFIR Report
date: 2022-11-29
fetch_date: 2025-10-03T23:56:37.095535
---

# Emotet Strikes Again – LNK File Leads to Domain Wide Ransomware

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
[cobaltstrike](https://thedfirreport.com/category/cobaltstrike/)
[ransomware](https://thedfirreport.com/category/ransomware/)

# Emotet Strikes Again – LNK File Leads to Domain Wide Ransomware

[November 28, 2022](https://thedfirreport.com/2022/11/28/emotet-strikes-again-lnk-file-leads-to-domain-wide-ransomware/)

In June of 2022, we observed a threat actor gaining access to an environment via Emotet and operating over a eight day period. During this time period, multiple rounds of enumeration and lateral movement occurred using Cobalt Strike. Remote access tools were used for command and control, such as [Tactical RMM](https://github.com/amidaware/tacticalrmm) and [Anydesk](https://anydesk.com/en). The threat actors final actions included data exfiltration using Rclone and domain wide deployment of Quantum Ransomware.

We have observed similar traits in previous cases where [Emotet](https://thedfirreport.com/2022/09/12/dead-or-alive-an-emotet-story/) and [Quantum](https://thedfirreport.com/2022/04/25/quantum-ransomware/) were seen.

## [Case Summary](#case-summary)

The intrusion began when a user double clicked a LNK file, which then executed encoded Powershell commands to download an Emotet DLL onto the computer. Once executed, Emotet setup a Registry Run Key to maintain persistence on the beachhead host.

Emotet, then proceeded to execute a short list of discover commands using the Windows utilities systeminfo, ipconfig, and nltest targeting the network’s domain controllers. These commands would go on to be repeated daily by the Emotet process. Around one and one-half hours after execution, Emotet began sending spam emails, mailing new malicious attachments to continue spreading.

Similar activity continued over the second day, but on the third day of the incident, Emotet dropped a Cobalt Strike executable beacon onto the beachhead host. Using the Cobalt Strike beacon, the threat actors began conducting a new round of discovery activity. Windows net commands were run, targeting domain groups and computers, nltest was executed again, and they also used tasklist and ping to investigate a remote host.

The threat actor then moved laterally to a workstation. They first attempted this action using a PowerShell beacon and a remote service on the host, but while the script did execute on the remote host, it appeared to fail to connect to the command and control server. Next, they proceeded to transfer a beacon executable over SMB to the remote host’s ProgramData directory. This beacon was then successfully executed via WMI and connected successfully to the threat actors server.

Once on this new host the threat actors proceeded to run the net commands to review the Domain Administrators group again. They then proceeded to dump credentials from the LSASS process on the host. With some further process injection they then began to enumerate SMB shares across the environment and on finding a primary file server reviewed several documents present on the server. This Cobalt Strike server stopped communicating shortly there after.

On the fourth day of the intrusion, Emotet dropped a new Cobalt Strike beacon. Again, some net command discovery was run for domain admins and domain controller servers. A flight of netlogon authentications were observed from the beachhead host to the domain controller as a possible attempt at exploiting the domain controller.

The threat actors, however, proceeded along a more traditional path, using SMB file transfers and remote services to move laterally across domain controllers and several other servers in the environment using Cobalt Strike beacon DLL’s. On the domain controller, the threat actors conducted further discovery tasks running `find.bat` and `p.bat`, which executed AdFind active directory discovery and performed a ping sweep across the environment.

On one of the other targeted servers, the threat actors deployed Tactical RMM, a remote management agent, for additional access and persistence in the environment. From this server, the threat actors were observed using Rclone to exfiltrate data from a file share server in the environment. The [Mega.io](https://Mega.io) service was the location the stolen data was sent.

On the fifth day of the intrusion, the threat actors appeared again to try and exfiltrate some data from the mail server again using Rclone but this appeared to fail and the threat actors did not try to resolve the issue. After this the t...