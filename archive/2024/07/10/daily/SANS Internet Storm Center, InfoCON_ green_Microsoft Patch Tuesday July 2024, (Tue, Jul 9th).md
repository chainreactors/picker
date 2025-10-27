---
title: Microsoft Patch Tuesday July 2024, (Tue, Jul 9th)
url: https://isc.sans.edu/diary/rss/31058
source: SANS Internet Storm Center, InfoCON: green
date: 2024-07-10
fetch_date: 2025-10-06T17:50:08.610554
---

# Microsoft Patch Tuesday July 2024, (Tue, Jul 9th)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Johannes Ullrich](/handler_list.html#johannes-ullrich "Johannes Ullrich")

Threat Level: [green](/infocon.html)

* [previous](/diary/31054)
* [next](/diary/31064)

My next class:

|  |  |  |
| --- | --- | --- |
| [Application Security: Securing Web Apps, APIs, and Microservices](https://www.sans.org/event/dallas-2025/course/application-security-securing-web-apps-api-microservices) | Dallas | Dec 1st - Dec 6th 2025 |

# [Microsoft Patch Tuesday July 2024](/forums/diary/Microsoft%2BPatch%2BTuesday%2BJuly%2B2024/31058/)

**Published**: 2024-07-09. **Last Updated**: 2024-07-09 17:35:23 UTC
**by** [Johannes Ullrich](https://plus.google.com/101587262224166552564?rel=author) (Version: 1)

[0 comment(s)](/diary/Microsoft%2BPatch%2BTuesday%2BJuly%2B2024/31058/#comments)

Microsoft today released patches for 142 vulnerabilities. Only four of the vulnerabilities are rated as "critical". There are two vulnerabilities that have already been discussed and two that have already been exploited.

Noteworthy Vulnerabilities:

**CVE-2024-38080: Windows Hyper-V Elevation of Privilege Vulnerability (exploited vulnerability)**

An attacker can obtain SYSTEM privilege by exploiting this integer overflow.

**CVE-2024-38112: Windows MSHTML Platform Spoofing Vulnerability**

I haven't seen any details disclosed yet. However, these vulnerabilities typically make it difficult to identify the nature and origin of an attachment. A victim may be tricked into opening a malicious attachment, leading to code execution. There have been numerous similar vulnerabilities in the past.

**CVE-2024-35264: .NET and Visual Studio Remote Code Execution Vulnerability (disclosed vulnerability)**

CVSS score for this vulnerability is 8.1. It is not considered critical. The vulnerability is exploited by closing an http/3 connection while the body is still being processed. The attacker must take advantage of a race condition to execute code.

**CVE-2024-37985: Systematic Identification and Characterization of Proprietary Prefetchers (disclosed vulnerability)**

This vulnerability only affects ARM systems. An attacker would be able to view privileged heap memory.

**CVE-2024-38074, CVE-2024-38076, CVE-2024-38077: Windows Remote Desktop Licensing Service Remote Code Execution Vulnerability**

Three of the four critical vulnerabilities affect the RDP Licensing Service. Watch our for PoC exploits for this vulnerability.

**CVE-2024-38060: Windows Imaging Component Remote Code Execution Vulnerability**

The WIC is the Windows framework used to parse images and related metadata. Toe trigger the vulnerability, an authenticated attacker must upload a TIFF image to a server.

| Description | | | | | | | |
| --- | --- | --- | --- | --- | --- | --- | --- |
| CVE | Disclosed | Exploited | Exploitability (old versions) | current version | Severity | CVSS Base (AVG) | CVSS Temporal (AVG) |
| .NET Core and Visual Studio Denial of Service Vulnerability | | | | | | | |
| [CVE-2024-30105](/vuln.html?cve=2024-30105) | No | No | - | - | Important | 7.5 | 6.5 |
| .NET and Visual Studio Denial of Service Vulnerability | | | | | | | |
| [CVE-2024-38095](/vuln.html?cve=2024-38095) | No | No | - | - | Important | 7.5 | 6.5 |
| .NET and Visual Studio Remote Code Execution Vulnerability | | | | | | | |
| [CVE-2024-35264](/vuln.html?cve=2024-35264) | Yes | No | - | - | Important | 8.1 | 7.1 |
| .NET, .NET Framework, and Visual Studio Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2024-38081](/vuln.html?cve=2024-38081) | No | No | - | - | Important | 7.3 | 6.4 |
| Arm: CVE-2024-37985 Systematic Identification and Characterization of Proprietary Prefetchers | | | | | | | |
| [CVE-2024-37985](/vuln.html?cve=2024-37985) | Yes | No | - | - | Important | 5.9 | 5.2 |
| Azure CycleCloud Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2024-38092](/vuln.html?cve=2024-38092) | No | No | - | - | Important | 8.8 | 7.9 |
| Azure DevOps Server Spoofing Vulnerability | | | | | | | |
| [CVE-2024-35266](/vuln.html?cve=2024-35266) | No | No | - | - | Important | 7.6 | 6.6 |
| [CVE-2024-35267](/vuln.html?cve=2024-35267) | No | No | - | - | Important | 7.6 | 6.6 |
| Azure Kinect SDK Remote Code Execution Vulnerability | | | | | | | |
| [CVE-2024-38086](/vuln.html?cve=2024-38086) | No | No | - | - | Important | 6.4 | 5.6 |
| Azure Network Watcher VM Extension Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2024-35261](/vuln.html?cve=2024-35261) | No | No | - | - | Important | 7.8 | 7.0 |
| BitLocker Security Feature Bypass Vulnerability | | | | | | | |
| [CVE-2024-38058](/vuln.html?cve=2024-38058) | No | No | - | - | Important | 6.8 | 5.9 |
| CERT/CC: CVE-2024-3596 RADIUS Protocol Spoofing Vulnerability | | | | | | | |
| [CVE-2024-3596](/vuln.html?cve=2024-3596) | No | No | - | - | Important | 7.5 | 6.5 |
| DCOM Remote Cross-Session Activation Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2024-38061](/vuln.html?cve=2024-38061) | No | No | - | - | Important | 7.5 | 6.5 |
| DHCP Server Service Remote Code Execution Vulnerability | | | | | | | |
| [CVE-2024-38044](/vuln.html?cve=2024-38044) | No | No | - | - | Important | 7.2 | 6.3 |
| Github: CVE-2024-38517 TenCent RapidJSON Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2024-38517](/vuln.html?cve=2024-38517) | No | No | - | - | Moderate | 7.8 | 6.8 |
| Github: CVE-2024-39684 TenCent RapidJSON Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2024-39684](/vuln.html?cve=2024-39684) | No | No | - | - | Moderate | 7.8 | 6.8 |
| Kernel Streaming WOW Thunk Service Driver Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2024-38054](/vuln.html?cve=2024-38054) | No | No | - | - | Important | 7.8 | 6.8 |
| [CVE-2024-38052](/vuln.html?cve=2024-38052) | No | No | - | - | Important | 7.8 | 6.8 |
| [CVE-2024-38057](/vuln.html?cve=2024-38057) | No | No | - | - | Important | 7.8 | 6.8 |
| Microsoft Defender for IoT Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2024-38089](/vuln.html?cve=2024-38089) | No | No | - | - | Important | 9.1 | 7.9 |
| Microsoft Dynamics 365 (On-Premises) Information Disclosure Vulnerability | | | | | | | |
| [CVE-2024-30061](/vuln.html?cve=2024-30061) | No | No | - | - | Important | 7.3 | 6.4 |
| Microsoft Message Queuing Information Disclosure Vulnerability | | | | | | | |
| [CVE-2024-38017](/vuln.html?cve=2024-38017) | No | No | - | - | Important | 5.5 | 5.0 |
| Microsoft OLE DB Driver for SQL Server Remote Code Execution Vulnerability | | | | | | | |
| [CVE-2024-37334](/vuln.html?cve=2024-37334) | No | No | - | - | Important | 8.8 | 7.7 |
| Microsoft Office Remote Code Execution Vulnerability | | | | | | | |
| [CVE-2024-38021](/vuln.html?cve=2024-38021) | No | No | - | - | Important | 8.8 | 7.7 |
| Microsoft Outlook Spoofing Vulnerability | | | | | | | |
| [CVE-2024-38020](/vuln.html?cve=2024-38020) | No | No | - | - | Moderate | 6.5 | 5.7 |
| Microsoft SharePoint Remote Code Execution Vulnerability | | | | | | | |
| [CVE-2024-38094](/vuln.html?cve=2024-38094) | No | No | - | - | Important | 7.2 | 6.3 |
| Microsoft SharePoint Server Information Disclosure Vulnerability | | | | | | | |
| [CVE-2024-32987](/vuln.html?cve=2024-32987) | No | No | - | - | Important | 7.5 | 6.5 |
| Microsoft SharePoint Server Remote Code Execution Vulnerability | | | | | | | |
| [CVE-2024-38023](/vuln.html?cve=2024-38023) | No | No | - | - | Critical | 7.2 | 6.3 |
| [CVE-2024-38024](/vuln.html?cve=2024-38024) | No | No | - | - | Important | 7.2 | 6.3 |
| Microsoft WS-Discovery Denial of Service Vulnerability | | | | | | | |
| [CVE-2024-38091](/vuln.html?cve=2024-38091) | No | No | - | - | Important | 7.5 | 6.5 |
| Microsoft Windows Codecs Library Information Disclosure Vulnerability | | | | | | | |
| [CVE-2024-38055](/vuln.html?cve=2024-38055) | No | No | - | - | Important | 5.5 | 4.8 |
| [CVE-2024-38056](/vuln.ht...