---
title: Microsoft Patch Tuesday March 2026, (Tue, Mar 10th)
url: https://isc.sans.edu/diary/rss/32782
source: SANS Internet Storm Center, InfoCON: green
date: 2026-03-10
fetch_date: 2026-03-11T04:05:27.661245
---

# Microsoft Patch Tuesday March 2026, (Tue, Mar 10th)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Johannes Ullrich](/handler_list.html#johannes-ullrich "Johannes Ullrich")

Threat Level: [green](/infocon.html)

* [previous](/diary/32778)

My next class:

|  |  |  |
| --- | --- | --- |
| [Application Security: Securing Web Apps, APIs, and Microservices](https://www.sans.org/event/sans-2026/course/application-security-securing-web-apps-api-microservices) | Orlando | Mar 29th - Apr 3rd 2026 |

# [Microsoft Patch Tuesday March 2026](/forums/diary/Microsoft%2BPatch%2BTuesday%2BMarch%2B2026/32782/)

**Published**: 2026-03-10. **Last Updated**: 2026-03-10 17:33:47 UTC
**by** [Johannes Ullrich](https://plus.google.com/101587262224166552564?rel=author) (Version: 1)

[0 comment(s)](/diary/Microsoft%2BPatch%2BTuesday%2BMarch%2B2026/32782/#comments)

Microsoft today released patches for 93 vulnerabilities, including 9 vulnerabilities in Chromium affecting Microsoft Edge. 8 of the vulnerabilities are rated critical. 2 were disclosed prior to today but have not yet been exploited. This update addresses no already-exploited vulnerabilities.

Disclose vulnerabilities:

**CVE-2026-26127**: A denial of service vulnerability in .Net. Microsoft considers exploitation unlikely. The issue arises from an out-of-bounds read and can be exploited across the network. No authentication is required.

**CVE-2026-21262**: A privilege escalation in SQL Server. An authenticated user may be able to escalate privileges to sysadmin.

Critical Vulnerabilities:

**CVE-2026-21536**: The vulnerability in Microsoft's Devices Pricing Program allows remote code execution. But this product is only offered as a cloud service, and Microsoft has already deployed the patch. Microsoft credits the AI vulnerability scanning platform XBOW with discovering this vulnerability.

**CVE-2026-26125**: Similar to the above vulnerability, this elevation-of-privilege vulnerability in Microsoft's Payment Orchestrator service has been mitigated by Microsoft.

**CVE-2026-26113, CVE-2026-26110, CVE-2026-26144**: These vulnerabilities affect Excel and Office.

**CVE-2026-23651, CVE-2026-26124, CVE-2026-26122**: These vulnerabilities affect Microsoft ACI Confidential Containers. No customer action is required. Microsoft already patched these issues.

| Description | | | | | | | |
| --- | --- | --- | --- | --- | --- | --- | --- |
| CVE | Disclosed | Exploited | Exploitability (old versions) | current version | Severity | CVSS Base (AVG) | CVSS Temporal (AVG) |
| .NET Denial of Service Vulnerability | | | | | | | |
| [CVE-2026-26127](/vuln.html?cve=2026-26127) | Yes | No | - | - | Important | 7.5 | 6.5 |
| .NET Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2026-26131](/vuln.html?cve=2026-26131) | No | No | - | - | Important | 7.8 | 6.8 |
| ASP.NET Core Denial of Service Vulnerability | | | | | | | |
| [CVE-2026-26130](/vuln.html?cve=2026-26130) | No | No | - | - | Important | 7.5 | 6.5 |
| Active Directory Domain Services Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2026-25177](/vuln.html?cve=2026-25177) | No | No | - | - | Important | 8.8 | 7.7 |
| Arc Enabled Servers - Azure Connected Machine Agent Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2026-26117](/vuln.html?cve=2026-26117) | No | No | - | - | Important | 7.8 | 6.8 |
| Azure IOT Explorer Spoofing Vulnerability | | | | | | | |
| [CVE-2026-26121](/vuln.html?cve=2026-26121) | No | No | - | - | Important | 7.5 | 6.5 |
| Azure IoT Explorer Information Disclosure Vulnerability | | | | | | | |
| [CVE-2026-23664](/vuln.html?cve=2026-23664) | No | No | - | - | Important | 7.5 | 6.5 |
| [CVE-2026-23661](/vuln.html?cve=2026-23661) | No | No | - | - | Important | 7.5 | 6.5 |
| [CVE-2026-23662](/vuln.html?cve=2026-23662) | No | No | - | - | Important | 7.5 | 6.5 |
| Azure MCP Server Tools Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2026-26118](/vuln.html?cve=2026-26118) | No | No | - | - | Important | 8.8 | 7.7 |
| Broadcast DVR Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2026-23667](/vuln.html?cve=2026-23667) | No | No | - | - | Important | 7.0 | 6.1 |
| Chromium: CVE-2026-3536 Integer overflow in ANGLE | | | | | | | |
| [CVE-2026-3536](/vuln.html?cve=2026-3536) | No | No | - | - | - |  |  |
| Chromium: CVE-2026-3538 Integer overflow in Skia | | | | | | | |
| [CVE-2026-3538](/vuln.html?cve=2026-3538) | No | No | - | - | - |  |  |
| Chromium: CVE-2026-3539 Object lifecycle issue in DevTools | | | | | | | |
| [CVE-2026-3539](/vuln.html?cve=2026-3539) | No | No | - | - | - |  |  |
| Chromium: CVE-2026-3540 Inappropriate implementation in WebAudio | | | | | | | |
| [CVE-2026-3540](/vuln.html?cve=2026-3540) | No | No | - | - | - |  |  |
| Chromium: CVE-2026-3541 Inappropriate implementation in CSS | | | | | | | |
| [CVE-2026-3541](/vuln.html?cve=2026-3541) | No | No | - | - | - |  |  |
| Chromium: CVE-2026-3542 Inappropriate implementation in WebAssembly | | | | | | | |
| [CVE-2026-3542](/vuln.html?cve=2026-3542) | No | No | - | - | - |  |  |
| Chromium: CVE-2026-3543 Inappropriate implementation in V8 | | | | | | | |
| [CVE-2026-3543](/vuln.html?cve=2026-3543) | No | No | - | - | - |  |  |
| Chromium: CVE-2026-3544 Heap buffer overflow in WebCodecs | | | | | | | |
| [CVE-2026-3544](/vuln.html?cve=2026-3544) | No | No | - | - | - |  |  |
| Chromium: CVE-2026-3545 Insufficient data validation in Navigation | | | | | | | |
| [CVE-2026-3545](/vuln.html?cve=2026-3545) | No | No | - | - | - |  |  |
| GDI Remote Code Execution Vulnerability | | | | | | | |
| [CVE-2026-25190](/vuln.html?cve=2026-25190) | No | No | - | - | Important | 7.8 | 6.8 |
| GDI+ Information Disclosure Vulnerability | | | | | | | |
| [CVE-2026-25181](/vuln.html?cve=2026-25181) | No | No | - | - | Important | 7.5 | 6.5 |
| GitHub: CVE-2026-26030 Microsoft Semantic Kernel InMemoryVectorStore filter functionality vulnerable | | | | | | | |
| [CVE-2026-26030](/vuln.html?cve=2026-26030) | No | No | - | - | Important | 9.9 | 8.6 |
| GitHub: Zero Shot SCFoundation Remote Code Execution Vulnerability | | | | | | | |
| [CVE-2026-23654](/vuln.html?cve=2026-23654) | No | No | - | - | Important | 8.8 | 7.7 |
| Hybrid Worker Extension (Arc?enabled Windows VMs) Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2026-26141](/vuln.html?cve=2026-26141) | No | No | - | - | Important | 7.8 | 6.8 |
| Linux Azure Diagnostic extension (LAD) Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2026-23665](/vuln.html?cve=2026-23665) | No | No | - | - | Important | 7.8 | 6.8 |
| MapUrlToZone Security Feature Bypass Vulnerability | | | | | | | |
| [CVE-2026-23674](/vuln.html?cve=2026-23674) | No | No | - | - | Important | 7.5 | 6.5 |
| Microsoft ACI Confidential Containers Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2026-23651](/vuln.html?cve=2026-23651) | No | No | - | - | Critical | 6.7 | 6.0 |
| [CVE-2026-26124](/vuln.html?cve=2026-26124) | No | No | - | - | Critical | 6.7 | 6.0 |
| Microsoft ACI Confidential Containers Information Disclosure Vulnerability | | | | | | | |
| [CVE-2026-26122](/vuln.html?cve=2026-26122) | No | No | - | - | Critical | 6.5 | 5.7 |
| Microsoft Authenticator Information Disclosure Vulnerability | | | | | | | |
| [CVE-2026-26123](/vuln.html?cve=2026-26123) | No | No | - | - | Important | 5.5 | 4.8 |
| Microsoft Azure AD SSH Login extension for Linux Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2026-26148](/vuln.html?cve=2026-26148) | No | No | - | - | Important | 8.1 | 7.3 |
| Microsoft Brokering File System Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2026-25167](/vuln.html?cve=2026-25167) | No | No | - | - | Important | 7.4 | 6.4 |
| Microsoft Devices Pricing Program Remote Code Execution Vulnerability | | | | | | | |
| [CVE-2026-21536](/vuln.html?cve=2026-21536) | No | No | - | - | Critical | 9.8 | 8.5 |
| Microsoft Excel Information Disclosure Vulnerability | | | | ...