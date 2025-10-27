---
title: Microsoft Patch Tuesday: December 2024, (Tue, Dec 10th)
url: https://isc.sans.edu/diary/rss/31508
source: SANS Internet Storm Center, InfoCON: green
date: 2024-12-11
fetch_date: 2025-10-06T19:42:21.038521
---

# Microsoft Patch Tuesday: December 2024, (Tue, Dec 10th)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Johannes Ullrich](/handler_list.html#johannes-ullrich "Johannes Ullrich")

Threat Level: [green](/infocon.html)

* [previous](/diary/31502)
* [next](/diary/31510)

My next class:

|  |  |  |
| --- | --- | --- |
| [Application Security: Securing Web Apps, APIs, and Microservices](https://www.sans.org/event/dallas-2025/course/application-security-securing-web-apps-api-microservices) | Dallas | Dec 1st - Dec 6th 2025 |

# [Microsoft Patch Tuesday: December 2024](/forums/diary/Microsoft%2BPatch%2BTuesday%2BDecember%2B2024/31508/)

**Published**: 2024-12-10. **Last Updated**: 2024-12-10 18:39:33 UTC
**by** [Johannes Ullrich](https://plus.google.com/101587262224166552564?rel=author) (Version: 1)

[0 comment(s)](/diary/Microsoft%2BPatch%2BTuesday%2BDecember%2B2024/31508/#comments)

Microsoft today released patches for 71 vulnerabilities. 16 of these vulnerabilities are considered critical. One vulnerability (CVE-2024-49138) has already been exploited, and details were made public before today's patch release.

### Significant Vulnerabilities

**CVE-2024-49138**: This vulnerability affects the Windows Common Log File System Driver, a subsystem affected by similar privilege escalation vulnerabilities in the past. The only reason I consider this "significant" is that it is already being exploited.

**Windows Remote Desktop Services**: 9 of the 16 critical vulnerabilities affect Windows Remote Desktop Services. Exploitation may lead to remote code execution. Microsoft considers the exploitation of these vulnerabilities less likely. Even without considering these vulnerabilities, Windows Remote Desktop Service should not be exposed to the internet.

**LDAP**: Remote code execution vulnerabilities in the LDAP service are always "interesting" given the importance of LDAP as part of Active Directory. Two critical vulnerabilities are patched for LDAP. One with a CVSS score of 9.8. A third critical vulnerability affects the LDAP client.

**CVE-2024-49126**: LSASS vulnerabilities always make me reminisce of the "Blaster" worm and the related vulnerability back in the day. This one does involve a race condition, which will make exploitation more difficult. It could become an interesting lateral movement vulnerability if a reliable exploit materializes.

| Description | | | | | | | |
| --- | --- | --- | --- | --- | --- | --- | --- |
| CVE | Disclosed | Exploited | Exploitability (old versions) | current version | Severity | CVSS Base (AVG) | CVSS Temporal (AVG) |
| Input Method Editor (IME) Remote Code Execution Vulnerability | | | | | | | |
| [CVE-2024-49079](/vuln.html?cve=2024-49079) | No | No | - | - | Important | 7.8 | 6.8 |
| Lightweight Directory Access Protocol (LDAP) Client Remote Code Execution Vulnerability | | | | | | | |
| [CVE-2024-49124](/vuln.html?cve=2024-49124) | No | No | - | - | Critical | 8.1 | 7.1 |
| Microsoft Access Remote Code Execution Vulnerability | | | | | | | |
| [CVE-2024-49142](/vuln.html?cve=2024-49142) | No | No | - | - | Important | 7.8 | 6.8 |
| Microsoft Defender for Endpoint on Android Spoofing Vulnerability | | | | | | | |
| [CVE-2024-49057](/vuln.html?cve=2024-49057) | No | No | - | - | Important | 8.1 | 7.1 |
| Microsoft Edge (Chromium-based) Spoofing Vulnerability | | | | | | | |
| [CVE-2024-49041](/vuln.html?cve=2024-49041) | No | No | Less Likely | Less Likely | Moderate | 4.3 | 3.8 |
| Microsoft Excel Remote Code Execution Vulnerability | | | | | | | |
| [CVE-2024-49069](/vuln.html?cve=2024-49069) | No | No | - | - | Important | 7.8 | 6.8 |
| Microsoft Message Queuing (MSMQ) Denial of Service Vulnerability | | | | | | | |
| [CVE-2024-49096](/vuln.html?cve=2024-49096) | No | No | - | - | Important | 7.5 | 6.5 |
| Microsoft Message Queuing (MSMQ) Remote Code Execution Vulnerability | | | | | | | |
| [CVE-2024-49122](/vuln.html?cve=2024-49122) | No | No | - | - | Critical | 8.1 | 7.1 |
| [CVE-2024-49118](/vuln.html?cve=2024-49118) | No | No | - | - | Critical | 8.1 | 7.1 |
| Microsoft Office Defense in Depth Update | | | | | | | |
| [ADV240002](https://portal.msrc.microsoft.com/en-us/security-guidance/advisory/ADV240002) | No | No | - | - | Moderate |  |  |
| Microsoft Office Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2024-49059](/vuln.html?cve=2024-49059) | No | No | - | - | Important | 7.0 | 6.1 |
| [CVE-2024-43600](/vuln.html?cve=2024-43600) | No | No | - | - | Important | 7.8 | 6.8 |
| Microsoft Office Remote Code Execution Vulnerability | | | | | | | |
| [CVE-2024-49065](/vuln.html?cve=2024-49065) | No | No | - | - | Important | 5.5 | 4.8 |
| Microsoft SharePoint Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2024-49068](/vuln.html?cve=2024-49068) | No | No | - | - | Important | 8.2 | 7.1 |
| Microsoft SharePoint Information Disclosure Vulnerability | | | | | | | |
| [CVE-2024-49064](/vuln.html?cve=2024-49064) | No | No | - | - | Important | 6.5 | 5.7 |
| [CVE-2024-49062](/vuln.html?cve=2024-49062) | No | No | - | - | Important | 6.5 | 5.7 |
| Microsoft SharePoint Remote Code Execution Vulnerability | | | | | | | |
| [CVE-2024-49070](/vuln.html?cve=2024-49070) | No | No | - | - | Important | 7.4 | 6.4 |
| Microsoft/Muzic Remote Code Execution Vulnerability | | | | | | | |
| [CVE-2024-49063](/vuln.html?cve=2024-49063) | No | No | - | - | Important | 8.4 | 7.3 |
| System Center Operations Manager Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2024-43594](/vuln.html?cve=2024-43594) | No | No | - | - | Important | 7.3 | 6.4 |
| Windows Domain Name Service Remote Code Execution Vulnerability | | | | | | | |
| [CVE-2024-49091](/vuln.html?cve=2024-49091) | No | No | - | - | Important | 7.2 | 6.3 |
| Windows Cloud Files Mini Filter Driver Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2024-49114](/vuln.html?cve=2024-49114) | No | No | - | - | Important | 7.8 | 6.8 |
| Windows Common Log File System Driver Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2024-49088](/vuln.html?cve=2024-49088) | No | No | - | - | Important | 7.8 | 6.8 |
| [CVE-2024-49090](/vuln.html?cve=2024-49090) | No | No | - | - | Important | 7.8 | 6.8 |
| [CVE-2024-49138](/vuln.html?cve=2024-49138) | Yes | Yes | - | - | Important | 7.8 | 6.8 |
| Windows File Explorer Information Disclosure Vulnerability | | | | | | | |
| [CVE-2024-49082](/vuln.html?cve=2024-49082) | No | No | - | - | Important | 6.8 | 5.9 |
| Windows Hyper-V Remote Code Execution Vulnerability | | | | | | | |
| [CVE-2024-49117](/vuln.html?cve=2024-49117) | No | No | - | - | Critical | 8.8 | 7.7 |
| Windows IP Routing Management Snapin Remote Code Execution Vulnerability | | | | | | | |
| [CVE-2024-49080](/vuln.html?cve=2024-49080) | No | No | - | - | Important | 8.8 | 7.7 |
| Windows Kernel Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2024-49084](/vuln.html?cve=2024-49084) | No | No | - | - | Important | 7.0 | 6.1 |
| Windows Kernel-Mode Driver Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2024-49074](/vuln.html?cve=2024-49074) | No | No | - | - | Important | 7.8 | 6.8 |
| Windows Lightweight Directory Access Protocol (LDAP) Denial of Service Vulnerability | | | | | | | |
| [CVE-2024-49121](/vuln.html?cve=2024-49121) | No | No | - | - | Important | 7.5 | 6.5 |
| [CVE-2024-49113](/vuln.html?cve=2024-49113) | No | No | - | - | Important | 7.5 | 6.5 |
| Windows Lightweight Directory Access Protocol (LDAP) Remote Code Execution Vulnerability | | | | | | | |
| [CVE-2024-49112](/vuln.html?cve=2024-49112) | No | No | - | - | Critical | 9.8 | 8.5 |
| [CVE-2024-49127](/vuln.html?cve=2024-49127) | No | No | - | - | Critical | 8.1 | 7.1 |
| Windows Local Security Authority Subsystem Service (LSASS) Remote Code Execution Vulnerability | | | | | | | |
| [CVE-2024-49126](/vuln.html?cve=2024-49126) | No | No | - | - | Critical | 8.1 | 7.1 |
| Windows Mobile Broadband Driver Elevation of Privilege Vulnerability | | | |...