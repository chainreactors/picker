---
title: Microsoft Patch Tuesday: May 2025, (Tue, May 13th)
url: https://isc.sans.edu/diary/rss/31946
source: SANS Internet Storm Center, InfoCON: green
date: 2025-05-14
fetch_date: 2025-10-06T22:31:07.076047
---

# Microsoft Patch Tuesday: May 2025, (Tue, May 13th)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Johannes Ullrich](/handler_list.html#johannes-ullrich "Johannes Ullrich")

Threat Level: [green](/infocon.html)

* [previous](/diary/31942)
* [next](/diary/31950)

My next class:

|  |  |  |
| --- | --- | --- |
| [Application Security: Securing Web Apps, APIs, and Microservices](https://www.sans.org/event/dallas-2025/course/application-security-securing-web-apps-api-microservices) | Dallas | Dec 1st - Dec 6th 2025 |

# [Microsoft Patch Tuesday: May 2025](/forums/diary/Microsoft%2BPatch%2BTuesday%2BMay%2B2025/31946/)

**Published**: 2025-05-13. **Last Updated**: 2025-05-13 17:57:17 UTC
**by** [Johannes Ullrich](https://plus.google.com/101587262224166552564?rel=author) (Version: 1)

[0 comment(s)](/diary/Microsoft%2BPatch%2BTuesday%2BMay%2B2025/31946/#comments)

Today, Microsoft released its expected update for the May patch on Tuesday. This update fixes 78 vulnerabilities. 11 are rated as critical, and 66 as important. Five of the vulnerabilities have already been exploited and two were publicly known but not yet exploited. 70 of the vulnerabilities were patched today, 8 had patches delivered earlier this month.

### Notable Vulnerabilities:

[CVE-2025-30397](/vuln.html?cve=2025-30397): This vulnerability is already exploited. It could lead to remote code execution if a user visits a malicious web page, but only if Edge is running in Internet Explorer mode.

The other four already exploited vulnerabilities are all privilege escalation vulnerabilities. The two already known vulnerabilities include a remote code execution vulnerability in Visual Studio and a spoofing vulnerability in Microsoft Defender.

Most of the critical vulnerabilities affect Microsoft Office and the Remote Desktop Client.

[CVE-2025-29831](/vuln.html?cve=2025-29831) could be interesting: It is only rated "important", but it is described as a remote code execution issue in Windows Remote Desktop. No authorization is required to exploit the vulnerability. Exploitation relies on a race collation which is often not reliably exploitable (but exploitable). The attack has to be triggered while the server is being restarted. This may be exploitable if a denial of service vulnerability can be used to restart the system.

| Description | | | | | | | |
| --- | --- | --- | --- | --- | --- | --- | --- |
| CVE | Disclosed | Exploited | Exploitability (old versions) | current version | Severity | CVSS Base (AVG) | CVSS Temporal (AVG) |
| .NET, Visual Studio, and Build Tools for Visual Studio Spoofing Vulnerability | | | | | | | |
| [CVE-2025-26646](/vuln.html?cve=2025-26646) | No | No | - | - | Important | 8.0 | 7.0 |
| Active Directory Certificate Services (AD CS) Denial of Service Vulnerability | | | | | | | |
| [CVE-2025-29968](/vuln.html?cve=2025-29968) | No | No | - | - | Important | 6.5 | 5.7 |
| Azure Automation Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2025-29827](/vuln.html?cve=2025-29827) | No | No | - | - | Critical | 9.9 | 8.9 |
| Azure DevOps Server Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2025-29813](/vuln.html?cve=2025-29813) | No | No | - | - | Critical | 10.0 | 9.0 |
| Azure Storage Resource Provider Spoofing Vulnerability | | | | | | | |
| [CVE-2025-29972](/vuln.html?cve=2025-29972) | No | No | - | - | Critical | 9.9 | 8.9 |
| Document Intelligence Studio On-Prem Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2025-30387](/vuln.html?cve=2025-30387) | No | No | - | - | Important | 9.8 | 8.5 |
| Kernel Streaming Service Driver Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2025-24063](/vuln.html?cve=2025-24063) | No | No | - | - | Important | 7.8 | 6.8 |
| MS-EVEN RPC Remote Code Execution Vulnerability | | | | | | | |
| [CVE-2025-29969](/vuln.html?cve=2025-29969) | No | No | - | - | Important | 7.5 | 6.5 |
| Microsoft Azure File Sync Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2025-29973](/vuln.html?cve=2025-29973) | No | No | - | - | Important | 7.0 | 6.1 |
| Microsoft Brokering File System Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2025-29970](/vuln.html?cve=2025-29970) | No | No | - | - | Important | 7.8 | 6.8 |
| Microsoft DWM Core Library Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2025-30400](/vuln.html?cve=2025-30400) | No | Yes | - | - | Important | 7.8 | 7.2 |
| Microsoft Dataverse Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2025-29826](/vuln.html?cve=2025-29826) | No | No | - | - | Important | 7.3 | 6.4 |
| Microsoft Dataverse Remote Code Execution Vulnerability | | | | | | | |
| [CVE-2025-47732](/vuln.html?cve=2025-47732) | No | No | - | - | Critical | 8.7 | 7.6 |
| Microsoft Defender Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2025-26684](/vuln.html?cve=2025-26684) | No | No | - | - | Important | 6.7 | 5.8 |
| Microsoft Defender for Identity Spoofing Vulnerability | | | | | | | |
| [CVE-2025-26685](/vuln.html?cve=2025-26685) | Yes | No | - | - | Important | 6.5 | 5.7 |
| Microsoft Edge (Chromium-based) Spoofing Vulnerability | | | | | | | |
| [CVE-2025-29825](/vuln.html?cve=2025-29825) | No | No | Less Likely | Less Likely | Low | 6.5 | 5.7 |
| Microsoft Excel Remote Code Execution Vulnerability | | | | | | | |
| [CVE-2025-29977](/vuln.html?cve=2025-29977) | No | No | - | - | Important | 7.8 | 6.8 |
| [CVE-2025-29979](/vuln.html?cve=2025-29979) | No | No | - | - | Important | 7.8 | 6.8 |
| [CVE-2025-30375](/vuln.html?cve=2025-30375) | No | No | - | - | Important | 7.8 | 6.8 |
| [CVE-2025-30376](/vuln.html?cve=2025-30376) | No | No | - | - | Important | 7.8 | 6.8 |
| [CVE-2025-30379](/vuln.html?cve=2025-30379) | No | No | - | - | Important | 7.8 | 6.8 |
| [CVE-2025-30381](/vuln.html?cve=2025-30381) | No | No | - | - | Important | 7.8 | 6.8 |
| [CVE-2025-30383](/vuln.html?cve=2025-30383) | No | No | - | - | Important | 7.8 | 6.8 |
| [CVE-2025-30393](/vuln.html?cve=2025-30393) | No | No | - | - | Important | 7.8 | 6.8 |
| [CVE-2025-32704](/vuln.html?cve=2025-32704) | No | No | - | - | Important | 8.4 | 7.3 |
| Microsoft Office Remote Code Execution Vulnerability | | | | | | | |
| [CVE-2025-30377](/vuln.html?cve=2025-30377) | No | No | - | - | Critical | 8.4 | 7.3 |
| [CVE-2025-30386](/vuln.html?cve=2025-30386) | No | No | - | - | Critical | 8.4 | 7.3 |
| Microsoft Outlook Remote Code Execution Vulnerability | | | | | | | |
| [CVE-2025-32705](/vuln.html?cve=2025-32705) | No | No | - | - | Important | 7.8 | 6.8 |
| Microsoft PC Manager Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2025-29975](/vuln.html?cve=2025-29975) | No | No | - | - | Important | 7.8 | 6.8 |
| Microsoft Power Apps Information Disclosure Vulnerability | | | | | | | |
| [CVE-2025-47733](/vuln.html?cve=2025-47733) | No | No | - | - | Critical | 9.1 | 7.9 |
| Microsoft PowerPoint Remote Code Execution Vulnerability | | | | | | | |
| [CVE-2025-29978](/vuln.html?cve=2025-29978) | No | No | - | - | Important | 7.8 | 6.8 |
| Microsoft SharePoint Server Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2025-29976](/vuln.html?cve=2025-29976) | No | No | - | - | Important | 7.8 | 6.8 |
| Microsoft SharePoint Server Remote Code Execution Vulnerability | | | | | | | |
| [CVE-2025-30378](/vuln.html?cve=2025-30378) | No | No | - | - | Important | 7.0 | 6.1 |
| [CVE-2025-30382](/vuln.html?cve=2025-30382) | No | No | - | - | Important | 7.8 | 6.8 |
| [CVE-2025-30384](/vuln.html?cve=2025-30384) | No | No | - | - | Important | 7.4 | 6.4 |
| Microsoft Virtual Machine Bus (VMBus) Remote Code Execution Vulnerability | | | | | | | |
| [CVE-2025-29833](/vuln.html?cve=2025-29833) | No | No | - | - | Critical | 7.1 | 6.2 |
| Microsoft Windows Hardware Lab Kit (HLK) Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2025-27488](/vuln.html?cve=2025-27488) | No | No | - | - | Important | 6.7 | 5.8 |
| Microsoft msagsfeedback.azurewebsites.net Information Disc...