---
title: Microsoft April 2025 Patch Tuesday, (Tue, Apr 8th)
url: https://isc.sans.edu/diary/rss/31838
source: SANS Internet Storm Center, InfoCON: green
date: 2025-04-09
fetch_date: 2025-10-06T22:08:34.059372
---

# Microsoft April 2025 Patch Tuesday, (Tue, Apr 8th)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Johannes Ullrich](/handler_list.html#johannes-ullrich "Johannes Ullrich")

Threat Level: [green](/infocon.html)

* [previous](/diary/31834)
* [next](/diary/31840)

# [Microsoft April 2025 Patch Tuesday](/forums/diary/Microsoft%2BApril%2B2025%2BPatch%2BTuesday/31838/)

**Published**: 2025-04-08. **Last Updated**: 2025-04-08 18:40:41 UTC
**by** [Renato Marinho](/handler_list.html#renato-marinho) (Version: 1)

[0 comment(s)](/diary/Microsoft%2BApril%2B2025%2BPatch%2BTuesday/31838/#comments)

This month, Microsoft has released patches addressing a total of 125 vulnerabilities. Among these, 11 are classified as critical, highlighting the potential for significant impact if exploited. Notably, one vulnerability is currently being exploited in the wild, underscoring the importance of timely updates. While no vulnerabilities were disclosed prior to this patch release, the comprehensive updates aim to fortify systems against a range of threats, including remote code execution and privilege escalation. Users are encouraged to apply these patches promptly to enhance their security posture.

**Windows Common Log File System Driver Elevation of Privilege Vulnerability** ([CVE-2025-29824](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2025-29824))
This is a zero-day vulnerability with a severity rating of Important and a CVSS score of **7.8**, which is currently being exploited in the wild but has not been publicly disclosed. This vulnerability allows an attacker to elevate their privileges to SYSTEM level, posing a significant risk to affected systems. It specifically impacts Windows 10 for both x64-based and 32-bit systems. However, security updates to address this vulnerability are not yet available, and Microsoft plans to release them as soon as possible. Customers will be notified through a revision to the CVE information once the updates are ready.

**Windows Lightweight Directory Access Protocol (LDAP) Remote Code Execution Vulnerability** ([CVE-2025-26663](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2025-26663))
This critical vulnerability, CVE-2025-26663, has not been exploited in the wild nor disclosed publicly, making it a non-zero-day threat. It carries a CVSS score of 8.1, indicating a significant risk due to its potential impact of remote code execution. The vulnerability arises from a race condition that an unauthenticated attacker could exploit by sending specially crafted requests to a vulnerable LDAP server, leading to a use-after-free scenario. Although the attack complexity is high, requiring the attacker to win a race condition, the severity of the potential impact underscores the critical nature of this vulnerability. Currently, security updates for Windows 10 systems are not immediately available, but they will be released as soon as possible, with notifications provided via a revision to the CVE information.

**Lightweight Directory Access Protocol (LDAP) Client Remote Code Execution Vulnerability ([CVE-2025-26670](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2025-26670))**
This critical vulnerability, identified as CVE-2025-26670, has not been exploited in the wild nor disclosed publicly. It carries a CVSS score of **8.1**, indicating a significant risk of remote code execution. The vulnerability arises from a race condition that can be exploited by an unauthenticated attacker sending specially crafted requests to a vulnerable LDAP server, potentially resulting in a use-after-free condition. This could be leveraged to execute arbitrary code remotely. Despite the high attack complexity (AC:H), the potential impact is severe. Currently, security updates for Windows 10 systems are not available, but Microsoft plans to release them as soon as possible, with notifications provided through a revision to the CVE information.

**Windows Remote Desktop Services Remote Code Execution Vulnerability ([CVE-2025-27480](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2025-27480))**
This is a critical vulnerability with a CVSS score of **8.1**, which has not been exploited in the wild nor publicly disclosed as a zero-day. This vulnerability allows for remote code execution by an attacker who connects to a system with the Remote Desktop Gateway role. The attack involves triggering a race condition to create a use-after-free scenario, which can then be leveraged to execute arbitrary code. Despite its critical severity, the attack complexity is high, requiring the attacker to successfully win a race condition to exploit the vulnerability.

**Windows Remote Desktop Services Remote Code Execution Vulnerability ([CVE-2025-27482](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2025-27482))**
This is a critical vulnerability with a CVSS score of **8.1**, which has not been exploited in the wild nor disclosed publicly, making it a potential zero-day threat. This vulnerability allows for remote code execution, posing a significant risk to systems with the Remote Desktop Gateway role. Exploitation requires an attacker to successfully navigate a high-complexity attack scenario, specifically by winning a race condition that leads to a use-after-free situation, ultimately enabling the execution of arbitrary code. Organizations are advised to implement robust security measures and monitor for any suspicious activities to mitigate potential risks associated with this vulnerability.

This summary highlights key vulnerabilities from Microsoft's monthly updates, focusing on those posing significant risks. The Windows Common Log File System Driver vulnerability (**CVE-2025-29824**) is a zero-day threat actively exploited, allowing attackers to gain SYSTEM-level privileges. Users should prioritize monitoring and applying updates once available. Other critical vulnerabilities, such as those affecting LDAP and Remote Desktop Services, involve complex attack scenarios but pose severe risks due to potential remote code execution. Microsoft Office and Excel vulnerabilities also present significant threats, often requiring user interaction through social engineering tactics. Users are advised to remain vigilant and apply security updates promptly upon release to mitigate these risks.

| Description | | | | | | | |
| --- | --- | --- | --- | --- | --- | --- | --- |
| CVE | Disclosed | Exploited | Exploitability (old versions) | current version | Severity | CVSS Base (AVG) | CVSS Temporal (AVG) |
| ASP.NET Core and Visual Studio Denial of Service Vulnerability | | | | | | | |
| [CVE-2025-26682](/vuln.html?cve=2025-26682) | No | No | - | - | Important | 7.5 | 6.5 |
| Active Directory Certificate Services Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2025-27740](/vuln.html?cve=2025-27740) | No | No | - | - | Important | 8.8 | 7.7 |
| Active Directory Domain Services Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2025-29810](/vuln.html?cve=2025-29810) | No | No | - | - | Important | 7.5 | 6.5 |
| Azure Local Cluster Information Disclosure Vulnerability | | | | | | | |
| [CVE-2025-25002](/vuln.html?cve=2025-25002) | No | No | - | - | Important | 6.8 | 5.9 |
| [CVE-2025-26628](/vuln.html?cve=2025-26628) | No | No | - | - | Important | 7.3 | 6.4 |
| Azure Local Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2025-27489](/vuln.html?cve=2025-27489) | No | No | - | - | Important | 7.8 | 6.8 |
| BitLocker Security Feature Bypass Vulnerability | | | | | | | |
| [CVE-2025-26637](/vuln.html?cve=2025-26637) | No | No | - | - | Important | 6.8 | 5.9 |
| DirectX Graphics Kernel Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2025-29812](/vuln.html?cve=2025-29812) | No | No | - | - | Important | 7.8 | 6.8 |
| HTTP.sys Denial of Service Vulnerability | | | | | | | |
| [CVE-2025-27473](/vuln.html?cve=2025-27473) | No | No | - | - | Im...