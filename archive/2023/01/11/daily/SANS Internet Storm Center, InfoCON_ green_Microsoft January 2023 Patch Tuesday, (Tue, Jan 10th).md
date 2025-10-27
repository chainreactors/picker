---
title: Microsoft January 2023 Patch Tuesday, (Tue, Jan 10th)
url: https://isc.sans.edu/diary/rss/29420
source: SANS Internet Storm Center, InfoCON: green
date: 2023-01-11
fetch_date: 2025-10-04T03:35:02.267251
---

# Microsoft January 2023 Patch Tuesday, (Tue, Jan 10th)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Johannes Ullrich](/handler_list.html#johannes-ullrich "Johannes Ullrich")

Threat Level: [green](/infocon.html)

* [previous](/diary/29416)
* [next](/diary/29426)

# [Microsoft January 2023 Patch Tuesday](/forums/diary/Microsoft%2BJanuary%2B2023%2BPatch%2BTuesday/29420/)

**Published**: 2023-01-10. **Last Updated**: 2023-01-10 18:47:29 UTC
**by** [Renato Marinho](/handler_list.html#renato-marinho) (Version: 1)

[1 comment(s)](/diary/Microsoft%2BJanuary%2B2023%2BPatch%2BTuesday/29420/#comments)

In the first Patch Tuesday of 2023, we got patches for 98 vulnerabilities. Of these, 11 are critical, 1 was previously disclosed, and 1 is already being exploited, according to Microsoft.

The zero-day is an Elevation of Privilege Vulnerability in Windows Advanced Local Procedure Call (ALPC) ([CVE-2023-21674](https://msrc.microsoft.com/update-guide/en-US/vulnerability/CVE-2023-21674)). According to the advisory, exploitation of this vulnerability could lead to a browser sandbox escape and give the attacker SYSTEM privileges. This vulnerability deserves prioritization as it is already being exploited. The CVSS of this vulnerability is 8.8, the higher this month.

The previously disclosed is a privilege elevation vulnerability affecting Windows SMB Witness Service ([CVE-2023-21549](https://msrc.microsoft.com/update-guide/en-US/vulnerability/CVE-2023-21549)). According to the advisory, to exploit this vulnerability, an attacker could execute a specially crafted malicious script that executes an RPC call to an RPC host. This could result in elevation of privilege on the server. An attacker who successfully exploited this vulnerability could execute RPC functions that are restricted to privileged accounts only. The CVSS of this vulnerability is 8.8 as well.

There is a third critical elevation of privilege vulnerability with CVSS 8.8. This one affects Microsoft Cryptographic Services ([CVE-2023-21561](https://msrc.microsoft.com/update-guide/en-US/vulnerability/CVE-2023-21561)). According to the advisory, a locally authenticated attacker could send specially crafted data to the local CSRSS service to elevate their privileges from AppContainer to SYSTEM.

Amongst critical vulnerabilities, there are 7 remote code execution, 3 elevation of privilege and 1 security feature bypass. None of the critical vulnerabilities is marked as “Exploitation More Likely” for the Microsoft exploitability assessment.

See my dashboard for a more detailed breakout: <https://patchtuesdaydashboard.com/>

January 2023 Security Updates

| Description | | | | | | | |
| --- | --- | --- | --- | --- | --- | --- | --- |
| CVE | Disclosed | Exploited | Exploitability (old versions) | current version | Severity | CVSS Base (AVG) | CVSS Temporal (AVG) |
| .NET Denial of Service Vulnerability | | | | | | | |
| [CVE-2023-21538](/vuln.html?cve=2023-21538) | No | No | - | - | Important | 7.5 | 6.5 |
| 3D Builder Remote Code Execution Vulnerability | | | | | | | |
| [CVE-2023-21780](/vuln.html?cve=2023-21780) | No | No | - | - | Important | 7.8 | 6.8 |
| [CVE-2023-21781](/vuln.html?cve=2023-21781) | No | No | - | - | Important | 7.8 | 6.8 |
| [CVE-2023-21782](/vuln.html?cve=2023-21782) | No | No | - | - | Important | 7.8 | 6.8 |
| [CVE-2023-21784](/vuln.html?cve=2023-21784) | No | No | - | - | Important | 7.8 | 6.8 |
| [CVE-2023-21786](/vuln.html?cve=2023-21786) | No | No | - | - | Important | 7.8 | 6.8 |
| [CVE-2023-21791](/vuln.html?cve=2023-21791) | No | No | - | - | Important | 7.8 | 6.8 |
| [CVE-2023-21793](/vuln.html?cve=2023-21793) | No | No | - | - | Important | 7.8 | 6.8 |
| [CVE-2023-21783](/vuln.html?cve=2023-21783) | No | No | - | - | Important | 7.8 | 6.8 |
| [CVE-2023-21785](/vuln.html?cve=2023-21785) | No | No | - | - | Important | 7.8 | 6.8 |
| [CVE-2023-21787](/vuln.html?cve=2023-21787) | No | No | - | - | Important | 7.8 | 6.8 |
| [CVE-2023-21788](/vuln.html?cve=2023-21788) | No | No | - | - | Important | 7.8 | 6.8 |
| [CVE-2023-21789](/vuln.html?cve=2023-21789) | No | No | - | - | Important | 7.8 | 6.8 |
| [CVE-2023-21790](/vuln.html?cve=2023-21790) | No | No | - | - | Important | 7.8 | 6.8 |
| [CVE-2023-21792](/vuln.html?cve=2023-21792) | No | No | - | - | Important | 7.8 | 6.8 |
| Azure Service Fabric Container Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2023-21531](/vuln.html?cve=2023-21531) | No | No | - | - | Important | 7.0 | 6.1 |
| BitLocker Security Feature Bypass Vulnerability | | | | | | | |
| [CVE-2023-21563](/vuln.html?cve=2023-21563) | No | No | Less Likely | Less Likely | Important | 6.8 | 5.9 |
| Event Tracing for Windows Information Disclosure Vulnerability | | | | | | | |
| [CVE-2023-21753](/vuln.html?cve=2023-21753) | No | No | - | - | Important | 5.5 | 4.8 |
| [CVE-2023-21536](/vuln.html?cve=2023-21536) | No | No | Less Likely | Less Likely | Important | 4.7 | 4.1 |
| Internet Key Exchange (IKE) Protocol Denial of Service Vulnerability | | | | | | | |
| [CVE-2023-21547](/vuln.html?cve=2023-21547) | No | No | - | - | Important | 7.5 | 6.5 |
| Microsoft Cryptographic Services Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2023-21551](/vuln.html?cve=2023-21551) | No | No | - | - | Critical | 7.8 | 6.8 |
| [CVE-2023-21561](/vuln.html?cve=2023-21561) | No | No | Unlikely | Less Likely | Critical | 8.8 | 7.7 |
| [CVE-2023-21730](/vuln.html?cve=2023-21730) | No | No | Less Likely | Less Likely | Critical | 7.8 | 6.8 |
| Microsoft DWM Core Library Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2023-21724](/vuln.html?cve=2023-21724) | No | No | - | - | Important | 7.8 | 6.8 |
| Microsoft Exchange Server Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2023-21763](/vuln.html?cve=2023-21763) | No | No | - | - | Important | 7.8 | 6.8 |
| [CVE-2023-21764](/vuln.html?cve=2023-21764) | No | No | - | - | Important | 7.8 | 6.8 |
| Microsoft Exchange Server Information Disclosure Vulnerability | | | | | | | |
| [CVE-2023-21761](/vuln.html?cve=2023-21761) | No | No | - | - | Important | 7.5 | 6.5 |
| Microsoft Exchange Server Spoofing Vulnerability | | | | | | | |
| [CVE-2023-21762](/vuln.html?cve=2023-21762) | No | No | - | - | Important | 8.0 | 7.0 |
| [CVE-2023-21745](/vuln.html?cve=2023-21745) | No | No | - | - | Important | 8.0 | 7.0 |
| Microsoft Message Queuing (MSMQ) Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2023-21537](/vuln.html?cve=2023-21537) | No | No | - | - | Important | 7.8 | 6.8 |
| Microsoft ODBC Driver Remote Code Execution Vulnerability | | | | | | | |
| [CVE-2023-21732](/vuln.html?cve=2023-21732) | No | No | - | - | Important | 8.8 | 7.7 |
| Microsoft Office Remote Code Execution Vulnerability | | | | | | | |
| [CVE-2023-21734](/vuln.html?cve=2023-21734) | No | No | - | - | Important | 7.8 | 6.8 |
| [CVE-2023-21735](/vuln.html?cve=2023-21735) | No | No | - | - | Important | 7.8 | 6.8 |
| Microsoft Office Visio Information Disclosure Vulnerability | | | | | | | |
| [CVE-2023-21741](/vuln.html?cve=2023-21741) | No | No | - | - | Important | 7.1 | 6.2 |
| Microsoft Office Visio Remote Code Execution Vulnerability | | | | | | | |
| [CVE-2023-21736](/vuln.html?cve=2023-21736) | No | No | - | - | Important | 7.8 | 6.8 |
| [CVE-2023-21737](/vuln.html?cve=2023-21737) | No | No | - | - | Important | 7.8 | 6.8 |
| [CVE-2023-21738](/vuln.html?cve=2023-21738) | No | No | - | - | Important | 7.1 | 6.2 |
| Microsoft SharePoint Server Remote Code Execution Vulnerability | | | | | | | |
| [CVE-2023-21742](/vuln.html?cve=2023-21742) | No | No | - | - | Important | 8.8 | 7.7 |
| [CVE-2023-21744](/vuln.html?cve=2023-21744) | No | No | - | - | Important | 8.8 | 7.7 |
| Microsoft SharePoint Server Security Feature Bypass Vulnerability | | | | | | | |
| [CVE-2023-21743](/vuln.html?cve=2023-21743) | No | No | - | - | Critical | 5.3 | 4.6 |
| Microsoft WDAC OLE DB provider for SQL Server Remote Code Execution Vulnerabil...