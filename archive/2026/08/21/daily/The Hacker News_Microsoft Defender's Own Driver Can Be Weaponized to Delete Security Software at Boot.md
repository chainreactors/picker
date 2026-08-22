---
title: Microsoft Defender's Own Driver Can Be Weaponized to Delete Security Software at Boot
url: https://thehackernews.com/2026/08/microsoft-defenders-own-driver-can-be.html
source: The Hacker News
date: 2026-08-21
fetch_date: 2026-08-22T02:52:36.275459
---

# Microsoft Defender's Own Driver Can Be Weaponized to Delete Security Software at Boot

#1 Trusted Cybersecurity News Platform

Followed by 5.70+ million[**](https://twitter.com/thehackersnews)
[**](https://www.linkedin.com/company/thehackernews/)
[**](https://www.facebook.com/thehackernews)

[![The Hacker News Logo](data:image/png;base64...)](/)

**

**

[** Get the Latest News](#email-outer)

* [Home](/)
* [Newsletter](#email-outer)
* [Webinars](/p/upcoming-hacker-news-webinars.html)

* [Home](/)
* [Threat Intelligence](/search/label/Threat%20Intelligence)
* [Vulnerabilities](/search/label/Vulnerability)
* [Cyber Attacks](/search/label/Cyber%20Attack)
* [Webinars](/p/upcoming-hacker-news-webinars.html)
* [Expert Insights](https://thehackernews.com/expert-insights/)
* [Awards](https://awards.thehackernews.com/)

**

**

**

Resources

* [Webinars](/p/upcoming-hacker-news-webinars.html)
* [Awards](https://awards.thehackernews.com/)
* [Free eBooks](https://thehackernews.tradepub.com)

About Site

* [About THN](/p/about-us.html)
* [Jobs](/p/careers-technical-writer-designer-and.html)
* [Advertise with us](/p/advertising-with-hacker-news.html)

Contact/Tip Us

[**

Reach out to get featured—contact us to send your exclusive story idea, research, hacks, or ask us a question or leave a comment/feedback!](/p/submit-news.html)

Follow Us On Social Media

[**](https://www.facebook.com/thehackernews)
[**](https://twitter.com/thehackersnews)
[**](https://www.linkedin.com/company/thehackernews/)
[**](https://www.youtube.com/c/thehackernews?sub_confirmation=1)
[**](https://www.instagram.com/thehackernews/)

[** RSS Feeds](https://feeds.feedburner.com/TheHackersNews)
[** Email Alerts](#email-outer)

[![cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEipoZWeZ29mSf60rRpMZ3Ucnm7oeWBfslPFPT6xADBsdvBtjd20ovH2yLscUo8pS6OTK0ItATC25VeavJh73IgqJM6Nb3apqobQ9zEVISE-d0wEFAimLYUcnffWCTowCCqs5LofRTQP25xB32KzYhlTO8lUnkZfmtELv23LlgdeKY3nyS2etYQXGdPIQtnh/s728-e100/wiz-d.png)](https://thehackernews.uk/ai-security-playbook-d)

# [Microsoft Defender's Own Driver Can Be Weaponized to Delete Security Software at Boot](https://thehackernews.com/2026/08/microsoft-defenders-own-driver-can-be.html)

**Swati Khandelwal**Aug 21, 2026Endpoint Security / Threat Detection

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiCbsmb6Wk8pQKWQmByAl5wnZQEVjS7ZYiHrlsHRM7VlcoPL7s30TaoTReoaQ4LI8Oy3KfKlIRHn9sN_7bjEKd_FWPHi1V0JR6LERepKBWSdJOk6cSUNgfIN2KVc6ydfbTILTy11owREYfpO7K11gFQV00l6qf1zl5rzF28jPhcN744yTvRAA-EjyDSBXs/s1700-e365/windows.jpg)

Check Point Research has disclosed a technique that uses Microsoft Defender's own legitimately signed boot-time remediation driver to perform arbitrary kernel-level file and registry operations on Windows systems ranging from Windows 7 through Windows 11 25H2, with no software flaw exploited and no driver imported from outside the machine.

The driver, BTR.sys (Boot Time Removal Tool), is a required Windows component, which means it cannot be added to Microsoft's Vulnerable Driver Blocklist or blocked via Windows Defender Application Control (WDAC) without disrupting Defender itself.

Jiří Vinopal, a threat researcher and reverse engineer at Check Point Research, presented the findings as a main-stage briefing at Black Hat USA 2026 and DEF CON 34 in Las Vegas and published the accompanying research paper alongside a proof-of-concept tool, BTR\_CLI, on August 20, 2026. Check Point Research said it found no evidence the technique has been used in real-world attacks.

"During our analysis across all collected samples and telemetry sources, we did not observe evidence of real-world abuse of BTR.sys in the manner demonstrated in this research. This suggests the technique is currently unknown or unused by threat actors, making proactive detection engineering feasible before weaponization appears in the wild," Check Point Research said.

BTR.sys is embedded in Defender's `MpEngine.dll` as the `BOOTTIMETOOL` resource and is deployed when Defender must finish removing malware after a reboot, deleting files or registry entries that were locked while Windows was running.

Vinopal reverse-engineered the driver's proprietary, undocumented transaction protocol and found that every configuration blob passed to BTR.sys is RC4-encrypted with a 256-byte key hard-coded in the `.rdata` section of every BTR.sys build shipped since Windows 7, verified unchanged across 18 unique 64-bit versions.

BTR\_CLI, the proof-of-concept tool, locates `MpEngine.dll` under Defender's Definition Updates and extracts the embedded BTR.sys binary.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/zero-trust-claude-d)

The tool then constructs a valid encrypted transaction. It then installs the driver as a service via direct HKLM registry writes using `Type=1`, `Start=1`, and `Group="Boot Bus Extender"`, a method that bypasses the Service Control Manager entirely and generates no Windows Event ID 7045 (Service Installed) entry.

When loaded, BTR.sys executes the queued operations from Ring 0, attributed in telemetry to the System process (PID 4), and can delete locked files and directories, move files to unconstrained paths including `System32\drivers`, delete registry keys and values, and write new registry values of any type.

A second trigger mode schedules those operations for the next reboot.

The driver then executes during what Vinopal calls the "golden window," the interval after the filesystem becomes writable but before Defender's user-mode services have started, allowing BTR.sys to physically remove security binaries such as `WdFilter.sys` and `MsMpEng.exe` before they can lock themselves.

A live demonstration at Black Hat showed BTR\_CLI deleting the entire Defender stack from a fully updated Windows 11 25H2 machine with Tamper Protection active.

Exploitation requires an administrator account with `SeLoadDriverPrivilege`, which BTR\_CLI auto-enables for accounts that already hold it.

Unlike attacks that rely on the [bring your own vulnerable driver](https://thehackernews.com/2026/03/54-edr-killers-use-byovd-to-exploit-34.html) technique, which depend on known-vulnerable third-party signed drivers that can be added to blocklists, the BTR Reforged technique uses a driver built into every Windows installation from Windows 7 onward.

"The issue is not a vulnerability in the traditional sense, but rather an architectural trust boundary that can be crossed if an attacker already has administrative privileges. Following responsible disclosure, MSRC confirmed that these findings do not meet the criteria for immediate servicing, as the technique relies on pre-existing administrative privileges (SeLoadDriverPrivilege)," Check Point Research said in [the paper](https://research.checkpoint.com/2026/btr-reforged-weaponizing-defenders-remediation-driver-as-a-kernel-operation-primitive/).

Vinopal's GitHub repository for BTR\_CLI adds that "No patch is planned," a characterization Microsoft has not confirmed publicly.

BTR.sys was examined by security researchers for a different flaw in the same driver five years earlier.

In February 2021, SentinelLabs researcher Kasif Dekel disclosed CVE-2021-24092, a privilege escalation vulnerability that allowed a local non-administrator to overwrite arbitrary files by placing a hard link at the driver's log path. Microsoft patched CVE-2021-24092 on February 9, 2021.

"We assume that this vulnerability remained undiscovered until now because the driver is normally not present on the hard drive but rather dropped and activated when needed (with a random name) and then purged away," Kasif Dekel said in the [SentinelLabs disclosure](https://www.sentinelone.com/labs/cve-2021-24092-12-years-in-hiding-a-privilege-escalation-vulnerability-in-windows-defender/).

The use of a built-in Windows driver as a kernel offensive primitive, rather than a third-party vulnerable one, was previously demonstrated in the context of [FIN7's AvNeutralizer](https://theha...