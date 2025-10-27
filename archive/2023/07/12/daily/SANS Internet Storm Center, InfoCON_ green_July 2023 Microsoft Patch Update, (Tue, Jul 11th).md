---
title: July 2023 Microsoft Patch Update, (Tue, Jul 11th)
url: https://isc.sans.edu/diary/rss/30018
source: SANS Internet Storm Center, InfoCON: green
date: 2023-07-12
fetch_date: 2025-10-04T11:58:29.300418
---

# July 2023 Microsoft Patch Update, (Tue, Jul 11th)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Johannes Ullrich](/handler_list.html#johannes-ullrich "Johannes Ullrich")

Threat Level: [green](/infocon.html)

* [previous](/diary/30008)
* [next](/diary/30020)

# [July 2023 Microsoft Patch Update](/forums/diary/July%2B2023%2BMicrosoft%2BPatch%2BUpdate/30018/)

**Published**: 2023-07-11. **Last Updated**: 2023-07-11 20:37:11 UTC
**by** [Scott Fendley](/handler_list.html#scott-fendley) (Version: 1)

[0 comment(s)](/diary/July%2B2023%2BMicrosoft%2BPatch%2BUpdate/30018/#comments)

Today's Microsoft patch Tuesday addresses 132 vulnerabilities. Nine of the vulnerabilities are rated as Critical, and 6 of these are listed as exploited prior in the wild.

In particular, CVE-2023-36884 includes a remote code execution vulnerability via Microsoft Word documents and was linked to the Storm-0978 threat actor.  Microsoft Threat Intelligence has a [blog entry](https://www.microsoft.com/en-us/security/blog/2023/07/11/storm-0978-attacks-reveal-financial-and-espionage-motives/) which discusses this situation. Take special note of the mitigations which are recommended, as updates will likely be released out-of-cycle for this one.

Other exploited vulnerabilities include:

CVE-2023-35311 is a Microsoft Outlook Security Feature bypass which was being exploited in the wild which worked in the preview pane and bypasses security warning.

CVE-2023-32046 is an actively exploited privilege elevation vulnerability in Windows MSHTML which could be exploited by opening a specially crafted file in email or a malicious website.

CVE-2023-32049 is a security feature bypass vulnerability with Windows SmartScreen which was being exploited to prevent the Open File - Security Warning prompt when downloading/opening files from the Internet.

CVE-2023-36874 is an actively exploited privilege escalation flaw which could allow threat actors to gain local administrator privileges.  Attackers would need to have local access to the targeted machine and the user be able to create folder and performance traces to fully exploit this vulnerability.

Microsoft also issued a high-impact advisory (ADV230001) where attackers where abusing the drivers being certified by Microsoft's Windows Hardware Developer Program (MWHDP) as a post-exploitation activity.  The implicated developer accounts were suspected, and Microsoft has taken steps to untrust drivers which were improperly certified.

| Description | | | | | | | |
| --- | --- | --- | --- | --- | --- | --- | --- |
| CVE | Disclosed | Exploited | Exploitability (old versions) | current version | Severity | CVSS Base (AVG) | CVSS Temporal (AVG) |
| .NET and Visual Studio Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2023-33127](/vuln.html?cve=2023-33127) | No | No | - | - | Important | 8.1 | 7.3 |
| ASP.NET and Visual Studio Security Feature Bypass Vulnerability | | | | | | | |
| [CVE-2023-33170](/vuln.html?cve=2023-33170) | No | No | - | - | Important | 8.1 | 7.3 |
| Active Directory Federation Service Security Feature Bypass Vulnerability | | | | | | | |
| [CVE-2023-35348](/vuln.html?cve=2023-35348) | No | No | - | - | Important | 7.5 | 6.5 |
| Active Template Library Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2023-32055](/vuln.html?cve=2023-32055) | No | No | - | - | Important | 6.7 | 5.8 |
| Azure Active Directory Security Feature Bypass Vulnerability | | | | | | | |
| [CVE-2023-36871](/vuln.html?cve=2023-36871) | No | No | - | - | Important | 6.5 | 6.0 |
| Azure Service Fabric on Windows Information Disclosure Vulnerability | | | | | | | |
| [CVE-2023-36868](/vuln.html?cve=2023-36868) | No | No | - | - | Important | 6.5 | 5.7 |
| Connected User Experiences and Telemetry Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2023-35320](/vuln.html?cve=2023-35320) | No | No | - | - | Important | 7.8 | 6.8 |
| [CVE-2023-35353](/vuln.html?cve=2023-35353) | No | No | - | - | Important | 7.8 | 6.8 |
| Guidance on Microsoft Signed Drivers Being Used Maliciously | | | | | | | |
| [ADV230001](https://portal.msrc.microsoft.com/en-us/security-guidance/advisory/ADV230001) | No | Yes | - | - | None |  |  |
| HTTP.sys Denial of Service Vulnerability | | | | | | | |
| [CVE-2023-32084](/vuln.html?cve=2023-32084) | No | No | - | - | Important | 7.5 | 6.5 |
| [CVE-2023-35298](/vuln.html?cve=2023-35298) | No | No | - | - | Important | 7.5 | 6.5 |
| MediaWiki PandocUpload Extension Remote Code Execution Vulnerability | | | | | | | |
| [CVE-2023-35333](/vuln.html?cve=2023-35333) | No | No | - | - | Important | 8.8 | 7.7 |
| Microsoft ActiveX Remote Code Execution Vulnerability | | | | | | | |
| [CVE-2023-33152](/vuln.html?cve=2023-33152) | No | No | - | - | Important | 7.0 | 6.1 |
| Microsoft Defender Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2023-33156](/vuln.html?cve=2023-33156) | No | No | - | - | Important | 6.3 | 5.5 |
| Microsoft DirectMusic Information Disclosure Vulnerability | | | | | | | |
| [CVE-2023-35341](/vuln.html?cve=2023-35341) | No | No | - | - | Important | 6.2 | 5.4 |
| Microsoft Dynamics 365 (on-premises) Cross-site Scripting Vulnerability | | | | | | | |
| [CVE-2023-33171](/vuln.html?cve=2023-33171) | No | No | - | - | Important | 8.2 | 7.1 |
| [CVE-2023-35335](/vuln.html?cve=2023-35335) | No | No | - | - | Important | 8.2 | 7.1 |
| Microsoft Excel Information Disclosure Vulnerability | | | | | | | |
| [CVE-2023-33162](/vuln.html?cve=2023-33162) | No | No | - | - | Important | 5.5 | 4.8 |
| Microsoft Excel Remote Code Execution Vulnerability | | | | | | | |
| [CVE-2023-33158](/vuln.html?cve=2023-33158) | No | No | - | - | Important | 7.8 | 6.8 |
| [CVE-2023-33161](/vuln.html?cve=2023-33161) | No | No | - | - | Important | 7.8 | 6.8 |
| Microsoft Failover Cluster Information Disclosure Vulnerability | | | | | | | |
| [CVE-2023-32083](/vuln.html?cve=2023-32083) | No | No | - | - | Important | 6.5 | 5.7 |
| Microsoft Failover Cluster Remote Code Execution Vulnerability | | | | | | | |
| [CVE-2023-32033](/vuln.html?cve=2023-32033) | No | No | - | - | Important | 6.6 | 5.8 |
| Microsoft Guidance for Addressing Security Feature Bypass in Trend Micro EFI Modules | | | | | | | |
| [ADV230002](https://portal.msrc.microsoft.com/en-us/security-guidance/advisory/ADV230002) | No | No | Less Likely | Less Likely | Important |  |  |
| Microsoft Install Service Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2023-35347](/vuln.html?cve=2023-35347) | No | No | - | - | Important | 7.1 | 6.2 |
| Microsoft Message Queuing Denial of Service Vulnerability | | | | | | | |
| [CVE-2023-32044](/vuln.html?cve=2023-32044) | No | No | - | - | Important | 7.5 | 6.5 |
| [CVE-2023-32045](/vuln.html?cve=2023-32045) | No | No | - | - | Important | 7.5 | 6.5 |
| Microsoft Message Queuing Remote Code Execution Vulnerability | | | | | | | |
| [CVE-2023-32057](/vuln.html?cve=2023-32057) | No | No | - | - | Critical | 9.8 | 8.5 |
| [CVE-2023-35309](/vuln.html?cve=2023-35309) | No | No | - | - | Important | 7.5 | 6.5 |
| Microsoft ODBC Driver Remote Code Execution Vulnerability | | | | | | | |
| [CVE-2023-32038](/vuln.html?cve=2023-32038) | No | No | - | - | Important | 8.8 | 7.7 |
| Microsoft Office Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2023-33148](/vuln.html?cve=2023-33148) | No | No | - | - | Important | 7.8 | 6.8 |
| Microsoft Office Graphics Remote Code Execution Vulnerability | | | | | | | |
| [CVE-2023-33149](/vuln.html?cve=2023-33149) | No | No | - | - | Important | 7.8 | 6.8 |
| Microsoft Office Security Feature Bypass Vulnerability | | | | | | | |
| [CVE-2023-33150](/vuln.html?cve=2023-33150) | No | No | - | - | Important | 9.6 | 8.3 |
| Microsoft Outlook Remote Code Execution Vulnerability | | | | | | | |
| [CVE-2023-33153](/vuln.html?cve=2023-33153) | No | No | - | - | Important | 6.8 | 5.9 |
| Microsoft Outlook Security Feature Bypass Vulnerability | | | | | | | |
| [CVE-2023-35311](/...