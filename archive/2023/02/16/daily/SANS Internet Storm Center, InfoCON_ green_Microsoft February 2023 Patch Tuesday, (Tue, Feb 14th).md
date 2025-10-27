---
title: Microsoft February 2023 Patch Tuesday, (Tue, Feb 14th)
url: https://isc.sans.edu/diary/rss/29548
source: SANS Internet Storm Center, InfoCON: green
date: 2023-02-16
fetch_date: 2025-10-04T06:48:42.404148
---

# Microsoft February 2023 Patch Tuesday, (Tue, Feb 14th)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Johannes Ullrich](/handler_list.html#johannes-ullrich "Johannes Ullrich")

Threat Level: [green](/infocon.html)

* [previous](/diary/29544)
* [next](/diary/29552)

My next class:

|  |  |  |
| --- | --- | --- |
| [Application Security: Securing Web Apps, APIs, and Microservices](https://www.sans.org/event/cloudsecnext-summit-2025/course/application-security-securing-web-apps-api-microservices) | Denver | Oct 4th - Oct 9th 2025 |

# [Microsoft February 2023 Patch Tuesday](/forums/diary/Microsoft%2BFebruary%2B2023%2BPatch%2BTuesday/29548/)

**Published**: 2023-02-14. **Last Updated**: 2023-02-15 01:19:13 UTC
**by** [Johannes Ullrich](https://plus.google.com/101587262224166552564?rel=author) (Version: 1)

[1 comment(s)](/diary/Microsoft%2BFebruary%2B2023%2BPatch%2BTuesday/29548/#comments)

Microsoft today patched 80 different vulnerabilities. This includes the Chromium vulnerabilities affecting Microsoft Edge. Nine vulnerabilities are rated as "Critical" by Microsoft.

Three of the vulnerabilities, all rated "important", are already being exploited:

CVE-2023-21715: Microsoft Publisher Security Feature Bypass. This vulnerability will allow the execution of macros bypassing policies blocking them.

CVE-2023-23376: Windows Common Log File Ssytem Driver Elevation of Privilege Vulnerability

CVE-2023-21823: Windows Graphics Component Remote Code Execution Vulnerability. Patches for this vulnerability may only be available via the Microsoft Store. Make sure you have these updates enabled.

Some additional vulnerabilities of interest:

CVE-2023-21803: Windows iSCSI Discovery Service Remote Code Execution Vulnerability. Likely not the most common issue to be patched this month, but something that may easily be missed. This vulnerability, if exploited, could be used for lateral movement.

CVE-2023-21716: Microsoft Word Remote Code Execution Vulnerability. Word is always a great target as it offers a large attack surface. No known exploit for this vulnerability, but its CVSS score of 9.8 will attract some attention. The rating of "critical" implies that it is not necessary to open the document to trigger the vulnerability.

Visual Studio: Several vulnerabilities, two of them critical, affect Visual Studio. Attacks against developers are often not well documented but appear on the rise.

| Description | | | | | | | |
| --- | --- | --- | --- | --- | --- | --- | --- |
| CVE | Disclosed | Exploited | Exploitability (old versions) | current version | Severity | CVSS Base (AVG) | CVSS Temporal (AVG) |
| curl use after free vulnerability affecting CBL Mariner 2.0 | | | | | | | |
| [CVE-2022-43552](/vuln.html?cve=2022-43552) | No | No | - | - | - |  |  |
| .NET Framework Denial of Service Vulnerability | | | | | | | |
| [CVE-2023-21722](/vuln.html?cve=2023-21722) | No | No | Less Likely | Less Likely | Important | 4.4 | 3.9 |
| .NET and Visual Studio Remote Code Execution Vulnerability | | | | | | | |
| [CVE-2023-21808](/vuln.html?cve=2023-21808) | No | No | Less Likely | Less Likely | Critical | 7.8 | 6.8 |
| 3D Builder Remote Code Execution Vulnerability | | | | | | | |
| [CVE-2023-23377](/vuln.html?cve=2023-23377) | No | No | - | - | Important | 7.8 | 6.8 |
| [CVE-2023-23390](/vuln.html?cve=2023-23390) | No | No | - | - | Important | 7.8 | 6.8 |
| Azure App Service on Azure Stack Hub Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2023-21777](/vuln.html?cve=2023-21777) | No | No | - | - | Important | 8.7 | 7.6 |
| Azure Data Box Gateway Remote Code Execution Vulnerability | | | | | | | |
| [CVE-2023-21703](/vuln.html?cve=2023-21703) | No | No | - | - | Important | 6.5 | 5.7 |
| Azure DevOps Server Cross-Site Scripting Vulnerability | | | | | | | |
| [CVE-2023-21564](/vuln.html?cve=2023-21564) | No | No | - | - | Important | 7.1 | 6.2 |
| Azure DevOps Server Remote Code Execution Vulnerability | | | | | | | |
| [CVE-2023-21553](/vuln.html?cve=2023-21553) | No | No | - | - | Important | 7.5 | 6.5 |
| Azure Machine Learning Compute Instance Information Disclosure Vulnerability | | | | | | | |
| [CVE-2023-23382](/vuln.html?cve=2023-23382) | No | No | - | - | Important | 6.5 | 5.7 |
| HTTP.sys Information Disclosure Vulnerability | | | | | | | |
| [CVE-2023-21687](/vuln.html?cve=2023-21687) | No | No | - | - | Important | 5.5 | 4.8 |
| MITRE: CVE-2019-15126 Specifically timed and handcrafted traffic can cause internal errors (related to state transitions) in a WLAN device | | | | | | | |
| [CVE-2019-15126](/vuln.html?cve=2019-15126) | No | No | - | - | - |  |  |
| Microsoft Defender for Endpoint Security Feature Bypass Vulnerability | | | | | | | |
| [CVE-2023-21809](/vuln.html?cve=2023-21809) | No | No | - | - | Important | 7.8 | 6.8 |
| Microsoft Defender for IoT Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2023-23379](/vuln.html?cve=2023-23379) | No | No | - | - | Important | 6.4 | 5.6 |
| Microsoft Dynamics 365 (on-premises) Cross-site Scripting Vulnerability | | | | | | | |
| [CVE-2023-21807](/vuln.html?cve=2023-21807) | No | No | Unlikely | Less Likely | Important | 5.8 | 5.1 |
| [CVE-2023-21570](/vuln.html?cve=2023-21570) | No | No | - | - | Important | 5.4 | 4.7 |
| [CVE-2023-21571](/vuln.html?cve=2023-21571) | No | No | - | - | Important | 5.4 | 4.7 |
| [CVE-2023-21572](/vuln.html?cve=2023-21572) | No | No | - | - | Important | 6.5 | 5.7 |
| [CVE-2023-21573](/vuln.html?cve=2023-21573) | No | No | - | - | Important | 5.4 | 4.7 |
| Microsoft Dynamics Unified Service Desk Remote Code Execution Vulnerability | | | | | | | |
| [CVE-2023-21778](/vuln.html?cve=2023-21778) | No | No | Less Likely | Less Likely | Important | 8.3 | 7.2 |
| Microsoft Edge (Chromium-based) Remote Code Execution Vulnerability | | | | | | | |
| [CVE-2023-23374](/vuln.html?cve=2023-23374) | No | No | Less Likely | Less Likely | Moderate | 8.3 | 7.2 |
| Microsoft Edge (Chromium-based) Spoofing Vulnerability | | | | | | | |
| [CVE-2023-21794](/vuln.html?cve=2023-21794) | No | No | Less Likely | Less Likely | Low | 4.3 | 3.9 |
| Microsoft Edge (Chromium-based) Tampering Vulnerability | | | | | | | |
| [CVE-2023-21720](/vuln.html?cve=2023-21720) | No | No | Less Likely | Less Likely | Low | 5.3 | 4.8 |
| Microsoft Exchange Server Remote Code Execution Vulnerability | | | | | | | |
| [CVE-2023-21706](/vuln.html?cve=2023-21706) | No | No | - | - | Important | 8.8 | 7.7 |
| [CVE-2023-21707](/vuln.html?cve=2023-21707) | No | No | - | - | Important | 8.8 | 7.7 |
| [CVE-2023-21529](/vuln.html?cve=2023-21529) | No | No | - | - | Important | 8.8 | 7.7 |
| [CVE-2023-21710](/vuln.html?cve=2023-21710) | No | No | - | - | Important | 7.2 | 6.3 |
| Microsoft ODBC Driver Remote Code Execution Vulnerability | | | | | | | |
| [CVE-2023-21797](/vuln.html?cve=2023-21797) | No | No | - | - | Important | 8.8 | 7.7 |
| [CVE-2023-21798](/vuln.html?cve=2023-21798) | No | No | - | - | Important | 8.8 | 7.7 |
| Microsoft ODBC Driver for SQL Server Remote Code Execution Vulnerability | | | | | | | |
| [CVE-2023-21704](/vuln.html?cve=2023-21704) | No | No | - | - | Important | 7.8 | 6.8 |
| Microsoft Office Information Disclosure Vulnerability | | | | | | | |
| [CVE-2023-21714](/vuln.html?cve=2023-21714) | No | No | - | - | Important | 5.5 | 4.8 |
| Microsoft OneNote Spoofing Vulnerability | | | | | | | |
| [CVE-2023-21721](/vuln.html?cve=2023-21721) | No | No | - | - | Important | 6.5 | 5.7 |
| Microsoft PostScript Printer Driver Information Disclosure Vulnerability | | | | | | | |
| [CVE-2023-21693](/vuln.html?cve=2023-21693) | No | No | - | - | Important | 5.7 | 5.1 |
| Microsoft PostScript Printer Driver Remote Code Execution Vulnerability | | | | | | | |
| [CVE-2023-21684](/vuln.html?cve=2023-21684) | No | No | - | - | Important | 8.8 | 7.7 |
| [CVE-2023-21801](/vuln.html?cve=2023-21801) | No | No | - | - | Important | 7.8 | 6.8 |
| Microsoft Protected Extensible Authentication Protocol (PEAP) D...