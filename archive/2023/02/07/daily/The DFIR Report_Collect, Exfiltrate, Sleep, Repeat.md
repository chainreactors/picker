---
title: Collect, Exfiltrate, Sleep, Repeat
url: https://thedfirreport.com/2023/02/06/collect-exfiltrate-sleep-repeat/
source: The DFIR Report
date: 2023-02-07
fetch_date: 2025-10-04T05:48:42.778866
---

# Collect, Exfiltrate, Sleep, Repeat

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

[autohotkey](https://thedfirreport.com/category/autohotkey/)
[keylogger](https://thedfirreport.com/category/keylogger/)

# Collect, Exfiltrate, Sleep, Repeat

[February 6, 2023](https://thedfirreport.com/2023/02/06/collect-exfiltrate-sleep-repeat/)

In this intrusion from August 2022, we observed a compromise that was initiated with a Word document containing a malicious VBA macro, which established persistence and communication to a command and control server (C2). Upon performing initial discovery and user enumeration, the threat actor used AutoHotkey to launch a keylogger.

AutoHotkey is an open-source scripting language for Microsoft Windows machines that was introduced to provide easy keyboard shortcuts and automation. As described in AutoHotkey [documentation](https://www.autohotkey.com/docs/AutoHotkey.htm), the AHK script can be executed in a number of ways. As observed in this intrusion, the adversary executed the AHK keylogger script by calling a renamed version of AutoHotkey.exe (module.exe) and passing the script’s filename (module.ahk) as a command-line parameter.

## [The DFIR Report Services](https://thedfirreport.com/2024/06/10/icedid-brings-screenconnect-and-csharp-streamer-to-alphv-ransomware-deployment/#services)

* **[Private Threat Briefs](https://thedfirreport.com/services/threat-intelligence/#threat-brief):** Over 20 private reports annually, such as this one but more concise and quickly published post-intrusion.
* **[Threat Feed](https://thedfirreport.com/services/threat-intelligence/#threat-feed):** Focuses on tracking Command and Control frameworks like Cobalt Strike, Metasploit, Sliver, etc.
* **[All Intel](https://thedfirreport.com/services/threat-intelligence/#all-intel):** Includes everything from Private Threat Briefs and Threat Feed, plus private events, long-term tracking, data clustering, and other curated intel.
* **[Private Sigma Ruleset](https://thedfirreport.com/services/detection-rules/):** Features 100+ Sigma rules derived from 40+ cases, mapped to ATT&CK with test examples.
* **[DFIR Labs](https://thedfirreport.com/services/dfir-labs/):** Offers cloud-based, hands-on learning experiences, using real data, from real intrusions. Interactive labs are available with different difficulty levels and can be accessed on-demand, accommodating various learning speeds.

[Contact us](https://thedfirreport.com/contact/) today for a demo!

## [Case Summary](#case-summary)

The intrusion began with the execution of a malicious macro within a Word document. The document was themed as a job application for the firm [Lumen](https://www.lumen.com/en-us/home.html). This tactic has been observed by many threat actor groups, including state sponsored actors in [North Korea](https://www.businessinsider.com/axie-infinity-crypto-hack-fake-job-offer-letter-spyware-phishing-2022-7) and [Iran](https://www.mandiant.com/resources/blog/apt33-insights-into-iranian-cyber-espionage). Upon opening the file, the user was prompted to enable macros to complete the form, which began execution of the malware.

Once executed, the macro created a VBS script (Updater.vbs), two PowerShell scripts (temp.ps1 and Script.ps1), and installed persistence through a scheduled task. The implant was fully implemented in PowerShell, which is uncommon compared to many initial access tools today.

Following the execution of the VBA embedded macros, the PowerShell script, Script.ps1**,** began to connect to the C2 server through an encrypted channel. Around a day after execution, the server became live and began sending instructions to the implant. The instructions obtained from the server were then executed through the temp.ps1 PowerShell script.

The threat actors began executing basic discovery commands, all of which were executed via PowerShell cmdlets or built-in Windows utilities like whoami, net, time, tzutil and tracert; one exception to this was when the threat actors extracted a specific function from the PowerSploit framework, [Convert-LDAPProperty](https://github.com/PowerShellMafia/PowerSploit/blob/master/Recon/PowerView.ps1#L3132), to enumerate domain accounts in the environment. All data collected was then exfiltrated over the existing C2 channel.

On the fourth day of the intrusion, the threat actors became active again by dropping of a set of files that performed keylogger functions. A scheduled task was then created to assist in execution of the keylogger. The keylogger itself was comprised of an executable, module.exe, which was a renam...