---
title: January 2026 Microsoft Patch Tuesday Summary, (Tue, Jan 13th)
url: https://isc.sans.edu/diary/rss/32624
source: SANS Internet Storm Center, InfoCON: green
date: 2026-01-13
fetch_date: 2026-01-14T03:36:01.994030
---

# January 2026 Microsoft Patch Tuesday Summary, (Tue, Jan 13th)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Johannes Ullrich](/handler_list.html#johannes-ullrich "Johannes Ullrich")

Threat Level: [green](/infocon.html)

* [previous](/diary/32616)

My next class:

|  |  |  |
| --- | --- | --- |
| [Application Security: Securing Web Apps, APIs, and Microservices](https://www.sans.org/event/sans-2026/course/application-security-securing-web-apps-api-microservices) | Orlando | Mar 29th - Apr 3rd 2026 |

# [January 2026 Microsoft Patch Tuesday Summary](/forums/diary/January%2B2026%2BMicrosoft%2BPatch%2BTuesday%2BSummary/32624/)

**Published**: 2026-01-13. **Last Updated**: 2026-01-13 19:05:41 UTC
**by** [Johannes Ullrich](https://plus.google.com/101587262224166552564?rel=author) (Version: 1)

[0 comment(s)](/diary/January%2B2026%2BMicrosoft%2BPatch%2BTuesday%2BSummary/32624/#comments)

Today, Microsoft released patches for 113 vulnerabilities. One of these vulnerabilities affected the Edge browser and was patched upstream by Chromium.

Eight of the vulnerabilities are rated critical. One has been disclosed before today, and one is already being exploited. Five of the critical vulnerabilities affect Microsoft Office components.

**Noteworthy Vulnerabilities**

**[CVE-2026-20854](/vuln.html?cve=2026-20854)**: A remote code execution vulnerability in LSASS. This brings back memories from hallmark Windows security events like the Blaster worm. However, in this case, the attacker must be authenticated. But the attacker does not need elevated privileges. Microsoft considers exploitation less likely.

**[CVE-2026-20805](/vuln.html?cve=2026-20805):** This is an information disclosure vulnerability in the Desktop Windows Manager, and it is already being exploited. The vulnerability can be used to identify the section address from a remote ALPC port.

**[CVE-2026-21265](/vuln.html?cve=2026-21265):** Secure boot may not recognize an expired certificate. This problem was already disclosed, but so far hasn't been exploited.

| Description | | | | | | | |
| --- | --- | --- | --- | --- | --- | --- | --- |
| CVE | Disclosed | Exploited | Exploitability (old versions) | current version | Severity | CVSS Base (AVG) | CVSS Temporal (AVG) |
| Azure Connected Machine Agent Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2026-21224](/vuln.html?cve=2026-21224) | No | No | - | - | Important | 7.8 | 6.8 |
| Azure Core shared client library for Python Remote Code Execution Vulnerability | | | | | | | |
| [CVE-2026-21226](/vuln.html?cve=2026-21226) | No | No | - | - | Important | 7.5 | 6.5 |
| Capability Access Management Service (camsvc) Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2026-20815](/vuln.html?cve=2026-20815) | No | No | - | - | Important | 7.0 | 6.1 |
| [CVE-2026-20830](/vuln.html?cve=2026-20830) | No | No | - | - | Important | 7.0 | 6.1 |
| [CVE-2026-21221](/vuln.html?cve=2026-21221) | No | No | - | - | Important | 7.0 | 6.1 |
| Capability Access Management Service (camsvc) Information Disclosure Vulnerability | | | | | | | |
| [CVE-2026-20835](/vuln.html?cve=2026-20835) | No | No | - | - | Important | 5.5 | 4.8 |
| [CVE-2026-20851](/vuln.html?cve=2026-20851) | No | No | - | - | Important | 6.2 | 5.4 |
| Chromium: CVE-2026-0628 Insufficient policy enforcement in WebView tag | | | | | | | |
| [CVE-2026-0628](/vuln.html?cve=2026-0628) | No | No | - | - | - |  |  |
| Desktop Window Manager Information Disclosure Vulnerability | | | | | | | |
| [CVE-2026-20805](/vuln.html?cve=2026-20805) | No | Yes | - | - | Important | 5.5 | 4.8 |
| Desktop Windows Manager Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2026-20871](/vuln.html?cve=2026-20871) | No | No | - | - | Important | 7.8 | 6.8 |
| DirectX Graphics Kernel Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2026-20814](/vuln.html?cve=2026-20814) | No | No | - | - | Important | 7.0 | 6.1 |
| [CVE-2026-20836](/vuln.html?cve=2026-20836) | No | No | - | - | Important | 7.0 | 6.1 |
| Dynamic Root of Trust for Measurement (DRTM) Information Disclosure Vulnerability | | | | | | | |
| [CVE-2026-20962](/vuln.html?cve=2026-20962) | No | No | - | - | Important | 4.4 | 3.9 |
| Host Process for Windows Tasks Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2026-20941](/vuln.html?cve=2026-20941) | No | No | - | - | Important | 7.8 | 6.8 |
| Inbox COM Objects (Global Memory) Remote Code Execution Vulnerability | | | | | | | |
| [CVE-2026-21219](/vuln.html?cve=2026-21219) | No | No | - | - | Important | 7.0 | 6.1 |
| LDAPTampering Vulnerability | | | | | | | |
| [CVE-2026-20812](/vuln.html?cve=2026-20812) | No | No | - | - | Important | 6.5 | 5.7 |
| Microsoft DWM Core Library Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2026-20842](/vuln.html?cve=2026-20842) | No | No | - | - | Important | 7.0 | 6.1 |
| Microsoft Excel Remote Code Execution Vulnerability | | | | | | | |
| [CVE-2026-20946](/vuln.html?cve=2026-20946) | No | No | - | - | Important | 7.8 | 6.8 |
| [CVE-2026-20955](/vuln.html?cve=2026-20955) | No | No | - | - | Critical | 7.8 | 6.8 |
| [CVE-2026-20956](/vuln.html?cve=2026-20956) | No | No | - | - | Important | 7.8 | 6.8 |
| [CVE-2026-20950](/vuln.html?cve=2026-20950) | No | No | - | - | Important | 7.8 | 6.8 |
| [CVE-2026-20957](/vuln.html?cve=2026-20957) | No | No | - | - | Critical | 7.8 | 6.8 |
| Microsoft Excel Security Feature Bypass Vulnerability | | | | | | | |
| [CVE-2026-20949](/vuln.html?cve=2026-20949) | No | No | - | - | Important | 7.8 | 6.8 |
| Microsoft Office Click-To-Run Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2026-20943](/vuln.html?cve=2026-20943) | No | No | - | - | Important | 7.0 | 6.1 |
| Microsoft Office Remote Code Execution Vulnerability | | | | | | | |
| [CVE-2026-20953](/vuln.html?cve=2026-20953) | No | No | - | - | Critical | 8.4 | 7.3 |
| [CVE-2026-20952](/vuln.html?cve=2026-20952) | No | No | - | - | Critical | 8.4 | 7.3 |
| Microsoft SQL Server Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2026-20803](/vuln.html?cve=2026-20803) | No | No | - | - | Important | 7.2 | 6.3 |
| Microsoft SharePoint Information Disclosure Vulnerability | | | | | | | |
| [CVE-2026-20958](/vuln.html?cve=2026-20958) | No | No | - | - | Important | 5.4 | 4.7 |
| Microsoft SharePoint Remote Code Execution Vulnerability | | | | | | | |
| [CVE-2026-20963](/vuln.html?cve=2026-20963) | No | No | - | - | Important | 8.8 | 7.7 |
| Microsoft SharePoint Server Remote Code Execution Vulnerability | | | | | | | |
| [CVE-2026-20951](/vuln.html?cve=2026-20951) | No | No | - | - | Important | 7.8 | 6.8 |
| [CVE-2026-20947](/vuln.html?cve=2026-20947) | No | No | - | - | Important | 8.8 | 7.7 |
| Microsoft SharePoint Server Spoofing Vulnerability | | | | | | | |
| [CVE-2026-20959](/vuln.html?cve=2026-20959) | No | No | - | - | Important | 4.6 | 4.0 |
| Microsoft Windows File Explorer Spoofing Vulnerability | | | | | | | |
| [CVE-2026-20847](/vuln.html?cve=2026-20847) | No | No | - | - | Important | 6.5 | 5.7 |
| Microsoft Word Remote Code Execution Vulnerability | | | | | | | |
| [CVE-2026-20944](/vuln.html?cve=2026-20944) | No | No | - | - | Critical | 8.4 | 7.3 |
| [CVE-2026-20948](/vuln.html?cve=2026-20948) | No | No | - | - | Important | 7.8 | 6.8 |
| NTLM Hash Disclosure Spoofing Vulnerability | | | | | | | |
| [CVE-2026-20925](/vuln.html?cve=2026-20925) | No | No | - | - | Important | 6.5 | 5.7 |
| [CVE-2026-20872](/vuln.html?cve=2026-20872) | No | No | - | - | Important | 6.5 | 5.7 |
| Remote Procedure Call Information Disclosure Vulnerability | | | | | | | |
| [CVE-2026-20821](/vuln.html?cve=2026-20821) | No | No | - | - | Important | 6.2 | 5.4 |
| Secure Boot Certificate Expiration Security Feature Bypass Vulnerability | | | | | | | |
| [CVE-2026-21265](/vuln.html?cve=2026-21265) | Yes | No | - | - | Important | 6.4 | 5.6 |
| TPM Trustlet Information Disclosure Vulnerability | | | | | | | |
| [CVE-2026-20829](/vuln.html?cve=...