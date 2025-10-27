---
title: Microsoft Patch Tuesday, July 2025, (Tue, Jul 8th)
url: https://isc.sans.edu/diary/rss/32088
source: SANS Internet Storm Center, InfoCON: green
date: 2025-07-09
fetch_date: 2025-10-06T23:55:44.876378
---

# Microsoft Patch Tuesday, July 2025, (Tue, Jul 8th)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Johannes Ullrich](/handler_list.html#johannes-ullrich "Johannes Ullrich")

Threat Level: [green](/infocon.html)

* [previous](/diary/32084)
* [next](/diary/32092)

My next class:

|  |  |  |
| --- | --- | --- |
| [Application Security: Securing Web Apps, APIs, and Microservices](https://www.sans.org/event/dallas-2025/course/application-security-securing-web-apps-api-microservices) | Dallas | Dec 1st - Dec 6th 2025 |

# [Microsoft Patch Tuesday, July 2025](/forums/diary/Microsoft%2BPatch%2BTuesday%2BJuly%2B2025/32088/)

**Published**: 2025-07-08. **Last Updated**: 2025-07-08 18:24:33 UTC
**by** [Johannes Ullrich](https://plus.google.com/101587262224166552564?rel=author) (Version: 1)

[0 comment(s)](/diary/Microsoft%2BPatch%2BTuesday%2BJuly%2B2025/32088/#comments)

Today, Microsoft released patches for 130 Microsoft vulnerabilities and 9 additional vulnerabilities not part of Microsoft's portfolio but distributed by Microsoft. 14 of these are rated critical. Only one of the vulnerabilities was disclosed before being patched, and none of the vulnerabilities have so far been exploited.

### Noteworthy Vulnerabilities:

**CVE-2025-49695 and CVE-2025-49696**: Both vulnerabilities affect Microsoft Office, are rated critical, and are considered "more likely" to be exploited by Microsoft. These issues do not require user interaction, so the user does not need to open a document. The exploit could be triggered via the preview pane. Macs are affected as well, but a patch is currently only available for Windows.

**CVE-2025-49719:** This vulnerability has already been made public. It does allow for information disclosure on a Microsoft SQL Server. To patch, you must patch the OLE DB Driver.

**CVE-2025-49717:** Exploitation is considered less likely for this vulnerability. But if exploited, it would allow code execution via a Microsoft SQL Server. Take this as additional motivation not to expose SQL servers.

**CVE-2025-49704:** I consider this vulnerability interesting as it appears to allow command/code injection in SharePoint. However, an attacker has to be authenticated to take advantage of this vulnerability.

| Description | | | | | | | |
| --- | --- | --- | --- | --- | --- | --- | --- |
| CVE | Disclosed | Exploited | Exploitability (old versions) | current version | Severity | CVSS Base (AVG) | CVSS Temporal (AVG) |
| AMD: CVE-2024-36350 Transient Scheduler Attack in Store Queue | | | | | | | |
| [CVE-2025-36350](/vuln.html?cve=2025-36350) | No | No | - | Less Likely | Critical | 5.6 | 4.9 |
| AMD: CVE-2025-36357 Transient Scheduler Attack in L1 Data Queue | | | | | | | |
| [CVE-2025-36357](/vuln.html?cve=2025-36357) | No | No | - | Less Likely | Critical | 5.6 | 4.9 |
| Azure Monitor Agent Remote Code Execution Vulnerability | | | | | | | |
| [CVE-2025-47988](/vuln.html?cve=2025-47988) | No | No | - | Less Likely | Important | 7.5 | 6.5 |
| Azure Service Fabric Runtime Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2025-21195](/vuln.html?cve=2025-21195) | No | No | - | Less Likely | Important | 6.0 | 5.2 |
| BitLocker Security Feature Bypass Vulnerability | | | | | | | |
| [CVE-2025-48001](/vuln.html?cve=2025-48001) | No | No | - | More Likely | Important | 6.8 | 5.9 |
| [CVE-2025-48003](/vuln.html?cve=2025-48003) | No | No | - | Less Likely | Important | 6.8 | 5.9 |
| [CVE-2025-48800](/vuln.html?cve=2025-48800) | No | No | - | More Likely | Important | 6.8 | 5.9 |
| [CVE-2025-48818](/vuln.html?cve=2025-48818) | No | No | - | More Likely | Important | 6.8 | 5.9 |
| [CVE-2025-48804](/vuln.html?cve=2025-48804) | No | No | - | More Likely | Important | 6.8 | 5.9 |
| Capability Access Management Service (camsvc) Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2025-49690](/vuln.html?cve=2025-49690) | No | No | - | Less Likely | Important | 7.4 | 6.4 |
| Credential Security Support Provider Protocol (CredSSP) Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2025-47987](/vuln.html?cve=2025-47987) | No | No | - | More Likely | Important | 7.8 | 6.8 |
| HID Class Driver Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2025-48816](/vuln.html?cve=2025-48816) | No | No | - | Unlikely | Important | 7.8 | 6.8 |
| Kernel Streaming WOW Thunk Service Driver Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2025-49675](/vuln.html?cve=2025-49675) | No | No | - | Less Likely | Important | 7.8 | 6.8 |
| MITRE: CVE-2025-27613 Gitk Arguments Vulnerability | | | | | | | |
| [CVE-2025-27613](/vuln.html?cve=2025-27613) | No | No | - | - | - |  |  |
| MITRE: CVE-2025-27614 Gitk Arbitrary Code Execution Vulnerability | | | | | | | |
| [CVE-2025-27614](/vuln.html?cve=2025-27614) | No | No | - | - | - |  |  |
| MITRE: CVE-2025-46334 Git Malicious Shell Vulnerability | | | | | | | |
| [CVE-2025-46334](/vuln.html?cve=2025-46334) | No | No | - | - | - |  |  |
| MITRE: CVE-2025-46835 Git File Overwrite Vulnerability | | | | | | | |
| [CVE-2025-46835](/vuln.html?cve=2025-46835) | No | No | - | - | - |  |  |
| MITRE: CVE-2025-48384 Git Symlink Vulnerability | | | | | | | |
| [CVE-2025-48384](/vuln.html?cve=2025-48384) | No | No | - | - | - |  |  |
| MITRE: CVE-2025-48385 Git Protocol Injection Vulnerability | | | | | | | |
| [CVE-2025-48385](/vuln.html?cve=2025-48385) | No | No | - | - | - |  |  |
| MITRE: CVE-2025-48386 Git Credential Helper Vulnerability | | | | | | | |
| [CVE-2025-48386](/vuln.html?cve=2025-48386) | No | No | - | - | - |  |  |
| Microsoft Brokering File System Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2025-49677](/vuln.html?cve=2025-49677) | No | No | - | Less Likely | Important | 7.0 | 6.1 |
| [CVE-2025-49694](/vuln.html?cve=2025-49694) | No | No | - | Less Likely | Important | 7.8 | 6.8 |
| [CVE-2025-49693](/vuln.html?cve=2025-49693) | No | No | - | Less Likely | Important | 7.8 | 6.8 |
| Microsoft Configuration Manager Remote Code Execution Vulnerability | | | | | | | |
| [CVE-2025-47178](/vuln.html?cve=2025-47178) | No | No | - | Unlikely | Important | 8.0 | 7.0 |
| Microsoft Edge (Chromium-based) Information Disclosure Vulnerability | | | | | | | |
| [CVE-2025-49741](/vuln.html?cve=2025-49741) | No | No | Less Likely | Less Likely | Important | 7.4 | 6.4 |
| Microsoft Edge (Chromium-based) Remote Code Execution Vulnerability | | | | | | | |
| [CVE-2025-49713](/vuln.html?cve=2025-49713) | No | No | - | Unlikely | Important | 8.8 | 7.7 |
| Microsoft Excel Information Disclosure Vulnerability | | | | | | | |
| [CVE-2025-48812](/vuln.html?cve=2025-48812) | No | No | - | Unlikely | Important | 5.5 | 4.8 |
| Microsoft Excel Remote Code Execution Vulnerability | | | | | | | |
| [CVE-2025-49711](/vuln.html?cve=2025-49711) | No | No | - | Less Likely | Important | 7.8 | 6.8 |
| Microsoft MPEG-2 Video Extension Remote Code Execution Vulnerability | | | | | | | |
| [CVE-2025-48805](/vuln.html?cve=2025-48805) | No | No | - | Less Likely | Important | 7.8 | 6.8 |
| [CVE-2025-48806](/vuln.html?cve=2025-48806) | No | No | - | Less Likely | Important | 7.8 | 6.8 |
| Microsoft Office Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2025-47994](/vuln.html?cve=2025-47994) | No | No | - | Less Likely | Important | 7.8 | 6.8 |
| Microsoft Office Remote Code Execution Vulnerability | | | | | | | |
| [CVE-2025-49695](/vuln.html?cve=2025-49695) | No | No | - | More Likely | Critical | 8.4 | 7.3 |
| [CVE-2025-49696](/vuln.html?cve=2025-49696) | No | No | - | More Likely | Critical | 8.4 | 7.3 |
| [CVE-2025-49697](/vuln.html?cve=2025-49697) | No | No | - | Less Likely | Critical | 8.4 | 7.3 |
| [CVE-2025-49699](/vuln.html?cve=2025-49699) | No | No | - | Less Likely | Important | 7.0 | 6.1 |
| [CVE-2025-49702](/vuln.html?cve=2025-49702) | No | No | - | Less Likely | Critical | 7.8 | 6.8 |
| Microsoft PC Manager Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2025-47993](/vuln.html?cve=2025-47993)...