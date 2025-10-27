---
title: Microsoft September 2024 Patch Tuesday, (Tue, Sep 10th)
url: https://isc.sans.edu/diary/rss/31254
source: SANS Internet Storm Center, InfoCON: green
date: 2024-09-11
fetch_date: 2025-10-06T18:30:06.961082
---

# Microsoft September 2024 Patch Tuesday, (Tue, Sep 10th)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Johannes Ullrich](/handler_list.html#johannes-ullrich "Johannes Ullrich")

Threat Level: [green](/infocon.html)

* [previous](/diary/31250)
* [next](/diary/31258)

My next class:

|  |  |  |
| --- | --- | --- |
| [Application Security: Securing Web Apps, APIs, and Microservices](https://www.sans.org/event/dallas-2025/course/application-security-securing-web-apps-api-microservices) | Dallas | Dec 1st - Dec 6th 2025 |

# [Microsoft September 2024 Patch Tuesday](/forums/diary/Microsoft%2BSeptember%2B2024%2BPatch%2BTuesday/31254/)

**Published**: 2024-09-10. **Last Updated**: 2024-09-10 23:28:25 UTC
**by** [Johannes Ullrich](https://plus.google.com/101587262224166552564?rel=author) (Version: 1)

[1 comment(s)](/diary/Microsoft%2BSeptember%2B2024%2BPatch%2BTuesday/31254/#comments)

Today, Microsoft released its scheduled September set of patches. This update addresses 79 different vulnerabilities. Seven of these vulnerabilities are rated critical. Four vulnerabilities are already being exploited and have been made public.

Noteworthy Vulnerabilities:

CVE-2024-43491: This "downgrade" vulnerabilities. An attacker can remove previously applied patches and exploit older vulnerabilities. This issue only affects Windows 10 Version 1507, which is EOL. It appears to differ from the similar vulnerabilities (CVE-2024-38202 and CVE-2024-21302) made public by Alon Leviev during Blackhat this year. These two vulnerabilities appear to remain unpatched.

CVE-2024-38014: A Windows Installer issue could lead to attackers gaining System access.

CVE-2024-38217: Yet another "Mark of the Web" bypass that is already exploited and could be used to trick a victim into installing malware.

CVE-2024-38226: Similar to the above vulnerability, a security feature bypass in Publisher.

Microsoft also patched four remote code execution vulnerabilities in Sharepoint, but the lower CVSS score indicates that exploitation will require access and specific prerequisites.

CVE-2024-38119: A critical vulnerability in the Windows NAT code. The low CVSS score is likely because this is not enabled by default.

| Description | | | | | | | |
| --- | --- | --- | --- | --- | --- | --- | --- |
| CVE | Disclosed | Exploited | Exploitability (old versions) | current version | Severity | CVSS Base (AVG) | CVSS Temporal (AVG) |
| Azure CycleCloud Remote Code Execution Vulnerability | | | | | | | |
| [CVE-2024-43469](/vuln.html?cve=2024-43469) | No | No | - | - | Important | 8.8 | 7.7 |
| Azure Network Watcher VM Agent Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2024-38188](/vuln.html?cve=2024-38188) | No | No | - | - | Important | 7.1 | 6.2 |
| [CVE-2024-43470](/vuln.html?cve=2024-43470) | No | No | - | - | Important | 7.3 | 6.4 |
| Azure Stack Hub Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2024-38216](/vuln.html?cve=2024-38216) | No | No | - | - | Critical | 8.2 | 7.1 |
| [CVE-2024-38220](/vuln.html?cve=2024-38220) | No | No | - | - | Critical | 9.0 | 7.8 |
| Azure Web Apps Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2024-38194](/vuln.html?cve=2024-38194) | No | No | - | - | Critical | 8.4 | 7.3 |
| DHCP Server Service Denial of Service Vulnerability | | | | | | | |
| [CVE-2024-38236](/vuln.html?cve=2024-38236) | No | No | - | - | Important | 7.5 | 6.5 |
| Kernel Streaming Service Driver Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2024-38241](/vuln.html?cve=2024-38241) | No | No | - | - | Important | 7.8 | 6.8 |
| [CVE-2024-38242](/vuln.html?cve=2024-38242) | No | No | - | - | Important | 7.8 | 6.8 |
| [CVE-2024-38238](/vuln.html?cve=2024-38238) | No | No | - | - | Important | 7.8 | 6.8 |
| [CVE-2024-38243](/vuln.html?cve=2024-38243) | No | No | - | - | Important | 7.8 | 6.8 |
| [CVE-2024-38244](/vuln.html?cve=2024-38244) | No | No | - | - | Important | 7.8 | 6.8 |
| [CVE-2024-38245](/vuln.html?cve=2024-38245) | No | No | - | - | Important | 7.8 | 6.8 |
| Kernel Streaming WOW Thunk Service Driver Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2024-38237](/vuln.html?cve=2024-38237) | No | No | - | - | Important | 7.8 | 6.8 |
| Microsoft AllJoyn API Information Disclosure Vulnerability | | | | | | | |
| [CVE-2024-38257](/vuln.html?cve=2024-38257) | No | No | - | - | Important | 7.5 | 6.5 |
| Microsoft AutoUpdate (MAU) Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2024-43492](/vuln.html?cve=2024-43492) | No | No | - | - | Important | 7.8 | 6.8 |
| Microsoft Dynamics 365 (on-premises) Cross-site Scripting Vulnerability | | | | | | | |
| [CVE-2024-43476](/vuln.html?cve=2024-43476) | No | No | - | - | Important | 7.6 | 6.6 |
| Microsoft Dynamics 365 Business Central Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2024-38225](/vuln.html?cve=2024-38225) | No | No | - | - | Important | 8.8 | 7.7 |
| Microsoft Excel Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2024-43465](/vuln.html?cve=2024-43465) | No | No | - | - | Important | 7.8 | 6.8 |
| Microsoft Management Console Remote Code Execution Vulnerability | | | | | | | |
| [CVE-2024-38259](/vuln.html?cve=2024-38259) | No | No | - | - | Important | 8.8 | 7.7 |
| Microsoft Office Visio Remote Code Execution Vulnerability | | | | | | | |
| [CVE-2024-43463](/vuln.html?cve=2024-43463) | No | No | - | - | Important | 7.8 | 6.8 |
| Microsoft Outlook for iOS Information Disclosure Vulnerability | | | | | | | |
| [CVE-2024-43482](/vuln.html?cve=2024-43482) | No | No | - | - | Important | 6.5 | 5.7 |
| Microsoft Power Automate Desktop Remote Code Execution Vulnerability | | | | | | | |
| [CVE-2024-43479](/vuln.html?cve=2024-43479) | No | No | - | - | Important | 8.5 | 7.4 |
| Microsoft Publisher Security Feature Bypass Vulnerability | | | | | | | |
| [CVE-2024-38226](/vuln.html?cve=2024-38226) | No | Yes | - | - | Important | 7.3 | 6.4 |
| Microsoft SQL Server Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2024-37965](/vuln.html?cve=2024-37965) | No | No | - | - | Important | 8.8 | 7.7 |
| [CVE-2024-37341](/vuln.html?cve=2024-37341) | No | No | - | - | Important | 8.8 | 7.7 |
| [CVE-2024-37980](/vuln.html?cve=2024-37980) | No | No | - | - | Important | 8.8 | 7.7 |
| Microsoft SQL Server Information Disclosure Vulnerability | | | | | | | |
| [CVE-2024-43474](/vuln.html?cve=2024-43474) | No | No | - | - | Important | 7.6 | 6.6 |
| Microsoft SQL Server Native Scoring Information Disclosure Vulnerability | | | | | | | |
| [CVE-2024-37966](/vuln.html?cve=2024-37966) | No | No | - | - | Important | 7.1 | 6.2 |
| [CVE-2024-37337](/vuln.html?cve=2024-37337) | No | No | - | - | Important | 7.1 | 6.2 |
| [CVE-2024-37342](/vuln.html?cve=2024-37342) | No | No | - | - | Important | 7.1 | 6.2 |
| Microsoft SQL Server Native Scoring Remote Code Execution Vulnerability | | | | | | | |
| [CVE-2024-37338](/vuln.html?cve=2024-37338) | No | No | - | - | Important | 8.8 | 7.7 |
| [CVE-2024-37335](/vuln.html?cve=2024-37335) | No | No | - | - | Important | 8.8 | 7.7 |
| [CVE-2024-37340](/vuln.html?cve=2024-37340) | No | No | - | - | Important | 8.8 | 7.7 |
| [CVE-2024-37339](/vuln.html?cve=2024-37339) | No | No | - | - | Important | 8.8 | 7.7 |
| [CVE-2024-26186](/vuln.html?cve=2024-26186) | No | No | - | - | Important | 8.8 | 7.7 |
| [CVE-2024-26191](/vuln.html?cve=2024-26191) | No | No | - | - | Important | 8.8 | 7.7 |
| Microsoft SharePoint Server Denial of Service Vulnerability | | | | | | | |
| [CVE-2024-43466](/vuln.html?cve=2024-43466) | No | No | - | - | Important | 6.5 | 5.7 |
| Microsoft SharePoint Server Remote Code Execution Vulnerability | | | | | | | |
| [CVE-2024-38018](/vuln.html?cve=2024-38018) | No | No | - | - | Critical | 8.8 | 7.7 |
| [CVE-2024-43464](/vuln.html?cve=2024-43464) | No | No | - | - | Critical | 7.2 | 6.3 |
| [CVE-2024-38227](/vuln.html?cve=2024-38227) | No | No | - | - | Important | 7.2 | 6.3 |
| [CVE-2024-38228](/vuln.html?cve=20...