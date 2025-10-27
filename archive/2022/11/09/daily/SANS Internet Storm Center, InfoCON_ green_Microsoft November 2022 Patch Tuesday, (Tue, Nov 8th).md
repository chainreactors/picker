---
title: Microsoft November 2022 Patch Tuesday, (Tue, Nov 8th)
url: https://isc.sans.edu/diary/rss/29230
source: SANS Internet Storm Center, InfoCON: green
date: 2022-11-09
fetch_date: 2025-10-03T22:08:28.499236
---

# Microsoft November 2022 Patch Tuesday, (Tue, Nov 8th)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Johannes Ullrich](/handler_list.html#johannes-ullrich "Johannes Ullrich")

Threat Level: [green](/infocon.html)

* [previous](/diary/29224)
* [next](/diary/29234)

# [Microsoft November 2022 Patch Tuesday](/forums/diary/Microsoft%2BNovember%2B2022%2BPatch%2BTuesday/29230/)

**Published**: 2022-11-08. **Last Updated**: 2022-11-08 18:41:13 UTC
**by** [Renato Marinho](/handler_list.html#renato-marinho) (Version: 1)

[0 comment(s)](/diary/Microsoft%2BNovember%2B2022%2BPatch%2BTuesday/29230/#comments)

This month we got patches for 68 vulnerabilities. Of these, 10 are critical, 1 was previously disclosed, and 4 are already being exploited, according to Microsoft.

The previously disclosed (and exploited) vulnerability is a security feature bypass on Windows Mark of the Web (MOTW) ([CVE-2022-41091](https://msrc.microsoft.com/update-guide/en-US/vulnerability/CVE-2022-41091)). According to the advisory, an attacker can craft a malicious file that would evade MOTW defenses, resulting in a limited loss of integrity and availability of security features such as Protected View in Microsoft Office, which rely on MOTW tagging. The CVSS for this vulnerability is 5.4.

Another exploited vulnerability is a Remote Code Execution (RCE) on Windows Script Languages ([CVE-2022-41128](https://msrc.microsoft.com/update-guide/en-US/vulnerability/CVE-2022-41128)). This vulnerability impacts JScript9 language. To exploit this vulnerability, an attacker would have to convince users to visit a specially crafted server share or website typically through an enticement in an email or chat message. In other words, user interaction is required, but it would not be hard for an attacker to accomplish this kind of interaction which makes this vulnerability worthy of special attention. The CVSS for this vulnerability is 8.8.

Among critical vulnerabilities, there is an elevation of privilege vulnerability affecting the Microsoft Exchange Server ([CVE-2022-41080](https://msrc.microsoft.com/update-guide/en-US/vulnerability/CVE-2022-41080)). The CVSS for this vulnerability is the highest for this month: 8.8. The advisory says that this vulnerability is not exploited, but marks it as “Exploitation More Likely”.

Last but not least, there is an important elevation of privilege vulnerability affecting Microsoft Windows Sysmon ([CVE-2022-41120](https://msrc.microsoft.com/update-guide/en-US/vulnerability/CVE-2022-41120)) that you should also dedicate special attention to. An attacker who successfully exploited this vulnerability could gain administrator privileges by manipulating information on the Sysinternals services. The CVSS for this vulnerability is 7.8.

See my dashboard for a more detailed breakout: <https://patchtuesdaydashboard.com/>

November 2022 Security Updates

| Description | | | | | | | |
| --- | --- | --- | --- | --- | --- | --- | --- |
| CVE | Disclosed | Exploited | Exploitability (old versions) | current version | Severity | CVSS Base (AVG) | CVSS Temporal (AVG) |
| .NET Framework Information Disclosure Vulnerability | | | | | | | |
| [CVE-2022-41064](/vuln.html?cve=2022-41064) | No | No | Less Likely | Less Likely | Important | 5.8 | 5.1 |
| AMD: CVE-2022-23824 IBPB and Return Address Predictor Interactions | | | | | | | |
| [CVE-2022-23824](/vuln.html?cve=2022-23824) | No | No | Less Likely | Less Likely | Important |  |  |
| Azure CycleCloud Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2022-41085](/vuln.html?cve=2022-41085) | No | No | - | - | Important | 7.5 | 6.5 |
| Azure RTOS GUIX Studio Remote Code Execution Vulnerability | | | | | | | |
| [CVE-2022-41051](/vuln.html?cve=2022-41051) | No | No | Less Likely | Less Likely | Important | 7.8 | 6.8 |
| BitLocker Security Feature Bypass Vulnerability | | | | | | | |
| [CVE-2022-41099](/vuln.html?cve=2022-41099) | No | No | Less Likely | Less Likely | Important | 4.6 | 4.0 |
| GitHub: CVE-2022-39253 Local clone optimization dereferences symbolic links by default | | | | | | | |
| [CVE-2022-39253](/vuln.html?cve=2022-39253) | No | No | - | - | Important |  |  |
| GitHub: CVE-2022-39327 Improper Control of Generation of Code ('Code Injection') in Azure CLI | | | | | | | |
| [CVE-2022-39327](/vuln.html?cve=2022-39327) | No | No | Less Likely | Less Likely | Critical |  |  |
| Microsoft Business Central Information Disclosure Vulnerability | | | | | | | |
| [CVE-2022-41066](/vuln.html?cve=2022-41066) | No | No | - | - | Important | 4.4 | 3.9 |
| Microsoft DWM Core Library Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2022-41096](/vuln.html?cve=2022-41096) | No | No | Less Likely | More Likely | Important | 7.8 | 6.8 |
| Microsoft Defense in Depth Update | | | | | | | |
| [ADV220003](https://portal.msrc.microsoft.com/en-us/security-guidance/advisory/ADV220003) | No | No | - | - | Important |  |  |
| Microsoft Excel Information Disclosure Vulnerability | | | | | | | |
| [CVE-2022-41105](/vuln.html?cve=2022-41105) | No | No | Less Likely | Less Likely | Important | 5.5 | 4.8 |
| Microsoft Excel Remote Code Execution Vulnerability | | | | | | | |
| [CVE-2022-41106](/vuln.html?cve=2022-41106) | No | No | Less Likely | Less Likely | Important | 7.8 | 6.8 |
| [CVE-2022-41063](/vuln.html?cve=2022-41063) | No | No | Less Likely | Less Likely | Important | 7.8 | 6.8 |
| Microsoft Excel Security Feature Bypass Vulnerability | | | | | | | |
| [CVE-2022-41104](/vuln.html?cve=2022-41104) | No | No | Less Likely | Less Likely | Important | 5.5 | 4.8 |
| Microsoft Exchange Server Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2022-41123](/vuln.html?cve=2022-41123) | No | No | - | - | Important | 7.8 | 6.8 |
| [CVE-2022-41080](/vuln.html?cve=2022-41080) | No | No | - | - | Critical | 8.8 | 7.7 |
| Microsoft Exchange Server Spoofing Vulnerability | | | | | | | |
| [CVE-2022-41078](/vuln.html?cve=2022-41078) | No | No | - | - | Important | 8.0 | 7.0 |
| [CVE-2022-41079](/vuln.html?cve=2022-41079) | No | No | - | - | Important | 8.0 | 7.0 |
| Microsoft ODBC Driver Remote Code Execution Vulnerability | | | | | | | |
| [CVE-2022-41047](/vuln.html?cve=2022-41047) | No | No | Less Likely | Less Likely | Important | 8.8 | 7.7 |
| [CVE-2022-41048](/vuln.html?cve=2022-41048) | No | No | Less Likely | Less Likely | Important | 8.8 | 7.7 |
| Microsoft Office Graphics Remote Code Execution Vulnerability | | | | | | | |
| [CVE-2022-41107](/vuln.html?cve=2022-41107) | No | No | Unlikely | Less Likely | Important | 7.8 | 6.8 |
| Microsoft SharePoint Server Remote Code Execution Vulnerability | | | | | | | |
| [CVE-2022-41062](/vuln.html?cve=2022-41062) | No | No | Less Likely | Less Likely | Important | 8.8 | 7.7 |
| Microsoft SharePoint Server Spoofing Vulnerability | | | | | | | |
| [CVE-2022-41122](/vuln.html?cve=2022-41122) | No | No | Less Likely | More Likely | Important | 6.5 | 5.7 |
| Microsoft Windows Sysmon Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2022-41120](/vuln.html?cve=2022-41120) | No | No | Less Likely | Less Likely | Important | 7.8 | 6.8 |
| Microsoft Word Information Disclosure Vulnerability | | | | | | | |
| [CVE-2022-41060](/vuln.html?cve=2022-41060) | No | No | More Likely | Less Likely | Important | 5.5 | 4.8 |
| [CVE-2022-41103](/vuln.html?cve=2022-41103) | No | No | Less Likely | Less Likely | Important | 5.5 | 4.8 |
| Microsoft Word Remote Code Execution Vulnerability | | | | | | | |
| [CVE-2022-41061](/vuln.html?cve=2022-41061) | No | No | Unlikely | Less Likely | Important | 7.8 | 6.8 |
| Netlogon RPC Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2022-38023](/vuln.html?cve=2022-38023) | No | No | - | - | Important | 8.1 | 7.1 |
| Network Policy Server (NPS) RADIUS Protocol Denial of Service Vulnerability | | | | | | | |
| [CVE-2022-41056](/vuln.html?cve=2022-41056) | No | No | Less Likely | Less Likely | Important | 7.5 | 6.5 |
| Network Policy Server (NPS) RA...