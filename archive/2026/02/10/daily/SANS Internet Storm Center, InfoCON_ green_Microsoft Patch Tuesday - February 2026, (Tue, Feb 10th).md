---
title: Microsoft Patch Tuesday - February 2026, (Tue, Feb 10th)
url: https://isc.sans.edu/diary/rss/32700
source: SANS Internet Storm Center, InfoCON: green
date: 2026-02-10
fetch_date: 2026-02-11T04:24:28.840769
---

# Microsoft Patch Tuesday - February 2026, (Tue, Feb 10th)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Johannes Ullrich](/handler_list.html#johannes-ullrich "Johannes Ullrich")

Threat Level: [green](/infocon.html)

* [previous](/diary/32692)

My next class:

|  |  |  |
| --- | --- | --- |
| [Application Security: Securing Web Apps, APIs, and Microservices](https://www.sans.org/event/sans-2026/course/application-security-securing-web-apps-api-microservices) | Orlando | Mar 29th - Apr 3rd 2026 |

# [Microsoft Patch Tuesday - February 2026](/forums/diary/Microsoft%2BPatch%2BTuesday%2BFebruary%2B2026/32700/)

**Published**: 2026-02-10. **Last Updated**: 2026-02-10 19:04:00 UTC
**by** [Johannes Ullrich](https://plus.google.com/101587262224166552564?rel=author) (Version: 1)

[0 comment(s)](/diary/Microsoft%2BPatch%2BTuesday%2BFebruary%2B2026/32700/#comments)

Today's patch Tuesday addresses 59 different vulnerabilities (plus two Chromium vulnerabilities affecting Microsoft Edge). While this is a lower-than-normal number, this includes six vulnerabilities that are already exploited. Three vulnerabilities have already been exploited and made public. In addition, five critical vulnerabilities are included in this patch Tuesday.

Vulnerabilities of Interest:

The three already exploited and public vulnerabilities are very similar, but they affect different Windows components. The issue is that the user is not properly warned when executing code they downloaded. Technologies like SmartScreen are supposed to prevent this from happening. The components affect:

[CVE-2026-21510](/vuln.html?cve=2026-21510): Windows Shell.

[CVE-2026-21513](/vuln.html?cve=2026-21513): This affects the (legacy) Internet Explorer HTML rendering engine. It is still used by some Windows components, but not by the Edge browser.

[CVE-2026-21514](/vuln.html?cve=2026-21514): Microsoft Word.

In addition, we have three more already exploited vulnerabilities:

[CVE-2026-21533](/vuln.html?cve=2026-21533): A privilege escalation in Remote Desktop

[CVE-2026-21519](/vuln.html?cve=2026-21519): A type confusion vulnerability in Windows Manager

[CVE-2026-21525](/vuln.html?cve=2026-21525): A Windows Remote Access Connection Manager Denial of Service.

Three of the critical vulnerabilities are related to Microsoft Azure and have already been patched by Microsoft.

[CVE-2026-23655](/vuln.html?cve=2026-23655) This vulnerability only affects Windows Defender on Linux and may lead to remote code execution.

| Description | | | | | | | |
| --- | --- | --- | --- | --- | --- | --- | --- |
| CVE | Disclosed | Exploited | Exploitability (old versions) | current version | Severity | CVSS Base (AVG) | CVSS Temporal (AVG) |
| .NET Spoofing Vulnerability | | | | | | | |
| [CVE-2026-21218](/vuln.html?cve=2026-21218) | No | No | - | - | Important | 7.5 | 6.5 |
| Azure Arc Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2026-24302](/vuln.html?cve=2026-24302) | No | No | - | - | Critical | 8.6 | 7.5 |
| Azure DevOps Server Cross-Site Scripting Vulnerability | | | | | | | |
| [CVE-2026-21512](/vuln.html?cve=2026-21512) | No | No | - | - | Important | 6.5 | 5.7 |
| Azure Front Door Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2026-24300](/vuln.html?cve=2026-24300) | No | No | - | - | Critical | 9.8 | 8.5 |
| Azure Function Information Disclosure Vulnerability | | | | | | | |
| [CVE-2026-21532](/vuln.html?cve=2026-21532) | No | No | - | - | Critical | 8.2 | 7.1 |
| Azure HDInsight Spoofing Vulnerability | | | | | | | |
| [CVE-2026-21529](/vuln.html?cve=2026-21529) | No | No | - | - | Important | 5.7 | 5.0 |
| Azure IoT Explorer Information Disclosure Vulnerability | | | | | | | |
| [CVE-2026-21528](/vuln.html?cve=2026-21528) | No | No | - | - | Important | 6.5 | 5.7 |
| Azure Local Remote Code Execution Vulnerability | | | | | | | |
| [CVE-2026-21228](/vuln.html?cve=2026-21228) | No | No | - | - | Important | 8.1 | 7.1 |
| Azure SDK for Python Remote Code Execution Vulnerability | | | | | | | |
| [CVE-2026-21531](/vuln.html?cve=2026-21531) | No | No | - | - | Important | 9.8 | 8.5 |
| Chromium: CVE-2026-1861 Heap buffer overflow in libvpx | | | | | | | |
| [CVE-2026-1861](/vuln.html?cve=2026-1861) | No | No | - | - | - |  |  |
| Chromium: CVE-2026-1862 Type Confusion in V8 | | | | | | | |
| [CVE-2026-1862](/vuln.html?cve=2026-1862) | No | No | - | - | - |  |  |
| Cluster Client Failover (CCF) Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2026-21251](/vuln.html?cve=2026-21251) | No | No | - | - | Important | 7.8 | 6.8 |
| Desktop Window Manager Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2026-21519](/vuln.html?cve=2026-21519) | No | Yes | - | - | Important | 7.8 | 6.8 |
| GDI+ Denial of Service Vulnerability | | | | | | | |
| [CVE-2026-20846](/vuln.html?cve=2026-20846) | No | No | - | - | Important | 7.5 | 6.5 |
| GitHub Copilot and Visual Studio Code Remote Code Execution Vulnerability | | | | | | | |
| [CVE-2026-21523](/vuln.html?cve=2026-21523) | No | No | - | - | Important | 8.0 | 7.0 |
| GitHub Copilot and Visual Studio Code Security Feature Bypass Vulnerability | | | | | | | |
| [CVE-2026-21518](/vuln.html?cve=2026-21518) | No | No | - | - | Important | 6.5 | 5.7 |
| GitHub Copilot and Visual Studio Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2026-21257](/vuln.html?cve=2026-21257) | No | No | - | - | Important | 8.0 | 7.0 |
| GitHub Copilot and Visual Studio Remote Code Execution Vulnerability | | | | | | | |
| [CVE-2026-21256](/vuln.html?cve=2026-21256) | No | No | - | - | Important | 8.8 | 7.7 |
| GitHub Copilot for Jetbrains Remote Code Execution Vulnerability | | | | | | | |
| [CVE-2026-21516](/vuln.html?cve=2026-21516) | No | No | - | - | Important | 8.8 | 7.7 |
| MSHTML Framework Security Feature Bypass Vulnerability | | | | | | | |
| [CVE-2026-21513](/vuln.html?cve=2026-21513) | Yes | Yes | - | - | Important | 8.8 | 7.7 |
| Mailslot File System Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2026-21253](/vuln.html?cve=2026-21253) | No | No | - | - | Important | 7.0 | 6.1 |
| Microsoft ACI Confidential Containers Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2026-21522](/vuln.html?cve=2026-21522) | No | No | - | - | Critical | 6.7 | 6.0 |
| Microsoft ACI Confidential Containers Information Disclosure Vulnerability | | | | | | | |
| [CVE-2026-23655](/vuln.html?cve=2026-23655) | No | No | - | - | Critical | 6.5 | 5.7 |
| Microsoft Defender for Endpoint Linux Extension Remote Code Execution Vulnerability | | | | | | | |
| [CVE-2026-21537](/vuln.html?cve=2026-21537) | No | No | - | - | Important | 8.8 | 7.7 |
| Microsoft Edge (Chromium-based) for Android Spoofing Vulnerability | | | | | | | |
| [CVE-2026-0391](/vuln.html?cve=2026-0391) | No | No | - | - | Moderate | 6.5 | 5.7 |
| Microsoft Excel Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2026-21259](/vuln.html?cve=2026-21259) | No | No | - | - | Important | 7.8 | 6.8 |
| Microsoft Excel Information Disclosure Vulnerability | | | | | | | |
| [CVE-2026-21258](/vuln.html?cve=2026-21258) | No | No | - | - | Important | 5.5 | 4.8 |
| [CVE-2026-21261](/vuln.html?cve=2026-21261) | No | No | - | - | Important | 5.5 | 4.8 |
| Microsoft Exchange Server Spoofing Vulnerability | | | | | | | |
| [CVE-2026-21527](/vuln.html?cve=2026-21527) | No | No | - | - | Important | 6.5 | 5.7 |
| Microsoft Outlook Spoofing Vulnerability | | | | | | | |
| [CVE-2026-21260](/vuln.html?cve=2026-21260) | No | No | - | - | Important | 7.5 | 6.5 |
| [CVE-2026-21511](/vuln.html?cve=2026-21511) | No | No | - | - | Important | 7.5 | 6.5 |
| Microsoft Word Security Feature Bypass Vulnerability | | | | | | | |
| [CVE-2026-21514](/vuln.html?cve=2026-21514) | Yes | Yes | - | - | Important | 7.8 | 7.2 |
| Power BI Remote Code Execution Vulnerability | | | | | | | |
| [CVE-2026-21229](/vuln.html?cve=2026-21229) | No | No | - | - | Important | 8.0 | 7.0 |
| Red Hat, Inc. CVE-2023-2804: Heap ...