---
title: Microsoft Patch Tuesday December 2025, (Tue, Dec 9th)
url: https://isc.sans.edu/diary/rss/32550
source: SANS Internet Storm Center, InfoCON: green
date: 2025-12-09
fetch_date: 2025-12-10T03:22:39.695733
---

# Microsoft Patch Tuesday December 2025, (Tue, Dec 9th)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Johannes Ullrich](/handler_list.html#johannes-ullrich "Johannes Ullrich")

Threat Level: [green](/infocon.html)

* [previous](/diary/32542)

My next class:

|  |  |  |
| --- | --- | --- |
| [Network Monitoring and Threat Detection In-Depth](https://www.sans.org/event/sec503-europe-online-december-2025/course/network-monitoring-threat-detection) | Online | Central European Time | Dec 15th - Dec 20th 2025 |

# [Microsoft Patch Tuesday December 2025](/forums/diary/Microsoft%2BPatch%2BTuesday%2BDecember%2B2025/32550/)

**Published**: 2025-12-09. **Last Updated**: 2025-12-09 20:20:54 UTC
**by** [Johannes Ullrich](https://plus.google.com/101587262224166552564?rel=author) (Version: 1)

[0 comment(s)](/diary/Microsoft%2BPatch%2BTuesday%2BDecember%2B2025/32550/#comments)

This release addresses 57 vulnerabilities. 3 of these vulnerabilities are rated critical. One vulnerability was already exploited, and two were publicly disclosed before the patch was released.

CVE-2025-62221: This privilege escalation vulnerability in the Microsoft Cloud Files Mini Filters driver is already being exploited.

CVE-2025-54100: A PowerShell script using Invoke-WebRequest may execute scripts that are included in the response. This is what Invoke-WebRequest is supposed to do. The patch adds a warning suggesting adding the -UseBasicParsing parameter to avoid executing scripts.

CVE-2025-64671: The GitHub Copilot plugin for JetBrains may lead to remote code execution. This is overall an issue with many AI code assistance as they have far-reaching access to the IDE.

The critical vulnerabilities are remote code execution vulnerabilities in Office and Outlook.

| Description | | | | | | | |
| --- | --- | --- | --- | --- | --- | --- | --- |
| CVE | Disclosed | Exploited | Exploitability (old versions) | current version | Severity | CVSS Base (AVG) | CVSS Temporal (AVG) |
| Application Information Service Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2025-62572](/vuln.html?cve=2025-62572) | No | No | - | - | Important | 7.8 | 6.8 |
| Azure Monitor Agent Remote Code Execution Vulnerability | | | | | | | |
| [CVE-2025-62550](/vuln.html?cve=2025-62550) | No | No | - | - | Important | 8.8 | 7.7 |
| DirectX Graphics Kernel Denial of Service Vulnerability | | | | | | | |
| [CVE-2025-62463](/vuln.html?cve=2025-62463) | No | No | - | - | Important | 6.5 | 5.7 |
| [CVE-2025-62465](/vuln.html?cve=2025-62465) | No | No | - | - | Important | 6.5 | 5.7 |
| DirectX Graphics Kernel Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2025-62573](/vuln.html?cve=2025-62573) | No | No | - | - | Important | 7.0 | 6.1 |
| GitHub Copilot for Jetbrains Remote Code Execution Vulnerability | | | | | | | |
| [CVE-2025-64671](/vuln.html?cve=2025-64671) | Yes | No | - | - | Important | 8.4 | 7.3 |
| Microsoft Access Remote Code Execution Vulnerability | | | | | | | |
| [CVE-2025-62552](/vuln.html?cve=2025-62552) | No | No | - | - | Important | 7.8 | 6.8 |
| Microsoft Brokering File System Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2025-62469](/vuln.html?cve=2025-62469) | No | No | - | - | Important | 7.0 | 6.1 |
| [CVE-2025-62569](/vuln.html?cve=2025-62569) | No | No | - | - | Important | 7.0 | 6.1 |
| Microsoft Edge (Chromium-based) for Mac Spoofing Vulnerability | | | | | | | |
| [CVE-2025-62223](/vuln.html?cve=2025-62223) | No | No | - | - | Low | 4.3 | 3.8 |
| Microsoft Excel Remote Code Execution Vulnerability | | | | | | | |
| [CVE-2025-62561](/vuln.html?cve=2025-62561) | No | No | - | - | Important | 7.8 | 6.8 |
| [CVE-2025-62563](/vuln.html?cve=2025-62563) | No | No | - | - | Important | 7.8 | 6.8 |
| [CVE-2025-62564](/vuln.html?cve=2025-62564) | No | No | - | - | Important | 7.8 | 6.8 |
| [CVE-2025-62553](/vuln.html?cve=2025-62553) | No | No | - | - | Important | 7.8 | 6.8 |
| [CVE-2025-62556](/vuln.html?cve=2025-62556) | No | No | - | - | Important | 7.8 | 6.8 |
| [CVE-2025-62560](/vuln.html?cve=2025-62560) | No | No | - | - | Important | 7.8 | 6.8 |
| Microsoft Exchange Server Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2025-64666](/vuln.html?cve=2025-64666) | No | No | - | - | Important | 7.5 | 6.5 |
| Microsoft Exchange Server Spoofing Vulnerability | | | | | | | |
| [CVE-2025-64667](/vuln.html?cve=2025-64667) | No | No | - | - | Important | 5.3 | 4.6 |
| Microsoft Message Queuing (MSMQ) Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2025-62455](/vuln.html?cve=2025-62455) | No | No | - | - | Important | 7.8 | 6.8 |
| Microsoft Office Remote Code Execution Vulnerability | | | | | | | |
| [CVE-2025-62554](/vuln.html?cve=2025-62554) | No | No | - | - | Critical | 8.4 | 7.3 |
| [CVE-2025-62557](/vuln.html?cve=2025-62557) | No | No | - | - | Critical | 8.4 | 7.3 |
| Microsoft Outlook Remote Code Execution Vulnerability | | | | | | | |
| [CVE-2025-62562](/vuln.html?cve=2025-62562) | No | No | - | - | Critical | 7.8 | 6.8 |
| Microsoft SharePoint Server Spoofing Vulnerability | | | | | | | |
| [CVE-2025-64672](/vuln.html?cve=2025-64672) | No | No | - | - | Important | 8.8 | 7.7 |
| Microsoft Word Remote Code Execution Vulnerability | | | | | | | |
| [CVE-2025-62555](/vuln.html?cve=2025-62555) | No | No | - | - | Important | 7.0 | 6.1 |
| [CVE-2025-62558](/vuln.html?cve=2025-62558) | No | No | - | - | Important | 7.8 | 6.8 |
| [CVE-2025-62559](/vuln.html?cve=2025-62559) | No | No | - | - | Important | 7.8 | 6.8 |
| PowerShell Remote Code Execution Vulnerability | | | | | | | |
| [CVE-2025-54100](/vuln.html?cve=2025-54100) | Yes | No | - | - | Important | 7.8 | 6.8 |
| Win32k Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2025-62458](/vuln.html?cve=2025-62458) | No | No | - | - | Important | 7.8 | 6.8 |
| Windows Camera Frame Server Monitor Information Disclosure Vulnerability | | | | | | | |
| [CVE-2025-62570](/vuln.html?cve=2025-62570) | No | No | - | - | Important | 7.1 | 6.2 |
| Windows Client-Side Caching Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2025-62466](/vuln.html?cve=2025-62466) | No | No | - | - | Important | 7.8 | 6.8 |
| Windows Cloud Files Mini Filter Driver Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2025-62454](/vuln.html?cve=2025-62454) | No | No | - | - | Important | 7.8 | 6.8 |
| [CVE-2025-62457](/vuln.html?cve=2025-62457) | No | No | - | - | Important | 7.8 | 6.8 |
| [CVE-2025-62221](/vuln.html?cve=2025-62221) | No | Yes | - | - | Important | 7.8 | 6.8 |
| Windows Common Log File System Driver Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2025-62470](/vuln.html?cve=2025-62470) | No | No | - | - | Important | 7.8 | 6.8 |
| Windows DWM Core Library Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2025-64679](/vuln.html?cve=2025-64679) | No | No | - | - | Important | 7.8 | 6.8 |
| [CVE-2025-64680](/vuln.html?cve=2025-64680) | No | No | - | - | Important | 7.8 | 6.8 |
| Windows Defender Firewall Service Information Disclosure Vulnerability | | | | | | | |
| [CVE-2025-62468](/vuln.html?cve=2025-62468) | No | No | - | - | Important | 4.4 | 3.9 |
| Windows DirectX Information Disclosure Vulnerability | | | | | | | |
| [CVE-2025-64670](/vuln.html?cve=2025-64670) | No | No | - | - | Important | 6.5 | 5.7 |
| Windows File Explorer Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2025-64658](/vuln.html?cve=2025-64658) | No | No | - | - | Important | 7.5 | 6.5 |
| [CVE-2025-62565](/vuln.html?cve=2025-62565) | No | No | - | - | Important | 7.3 | 6.4 |
| Windows Hyper-V Denial of Service Vulnerability | | | | | | | |
| [CVE-2025-62567](/vuln.html?cve=2025-62567) | No | No | - | - | Important | 5.3 | 4.6 |
| Windows Installer Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2025-62571](/vuln.html?cve=2025-62571) | No | No | - | - | Important | 7.8 | 6.8 |
| Windows Projected File System Elevation of Privilege Vulnerability | | | | | | | |
| [CVE...