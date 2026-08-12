---
title: Microsoft Patch Tuesday August 2026, (Tue, Aug 11th)
url: https://isc.sans.edu/diary/rss/33236
source: SANS Internet Storm Center, InfoCON: green
date: 2026-08-11
fetch_date: 2026-08-12T04:02:44.558994
---

# Microsoft Patch Tuesday August 2026, (Tue, Aug 11th)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Renato Marinho](/handler_list.html#renato-marinho "Renato Marinho")

Threat Level: [green](/infocon.html)

* [previous](/diary/33230)

Click HERE to learn more about classes Renato is teaching for SANS

# [Microsoft Patch Tuesday August 2026](/forums/diary/Microsoft%2BPatch%2BTuesday%2BAugust%2B2026/33236/)

**Published**: 2026-08-11. **Last Updated**: 2026-08-11 17:54:49 UTC
**by** [Renato Marinho](/handler_list.html#renato-marinho) (Version: 1)

[0 comment(s)](/diary/Microsoft%2BPatch%2BTuesday%2BAugust%2B2026/33236/#comments)

This month we got patches for 418 vulnerabilities. Of these, 62 are critical, 1 is being exploited in the wild, and 2 were publicly disclosed as zero-days. Notable fixes include Windows privilege escalation, container tampering, and critical QUIC and DNS Server remote code execution bugs.

A few vulnerabilities worth mentioning:

**Windows Ancillary Function Driver for WinSock Elevation of Privilege Vulnerability ([CVE-2026-68820](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-68820))**
This Important-severity elevation of privilege vulnerability is listed by Microsoft as exploited in the wild but not publicly disclosed, and it has a CVSS score of 7.0. The flaw is a use-after-free issue in the Windows Ancillary Function Driver for WinSock affecting supported Windows client and server versions; a locally authenticated attacker with low privileges could run a specially crafted application to trigger a race condition and, if successful, gain SYSTEM privileges. The CVSS vector reflects local access, low privileges required, no user interaction, and high attack complexity because exploitation requires winning that race condition. Administrators should prioritize applying the relevant Windows security updates, particularly on systems where local code execution by untrusted users is possible, and monitor for suspicious privilege-escalation activity.

**Windows User Profile Service Elevation of Privilege Vulnerability ([CVE-2026-62832](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-62832))**
Microsoft says this vulnerability has been publicly disclosed but has not been exploited in the wild, making it a zero-day disclosure without confirmed exploitation at this time. Rated Important with a CVSS score of 7.8, this Windows User Profile Service flaw is an improper link resolution, or “link following,” issue that could allow a local authenticated attacker to elevate privileges. To exploit it, an attacker would need credentials for another local account and could run a specially crafted application to load another user’s registry hive; successful exploitation could allow access to or modification of another user’s data and ultimately grant administrator privileges. User interaction is not required. Administrators should prioritize applying the Microsoft security updates across affected Windows 10, Windows 11, Windows Server 2022, and Windows Server 2025 systems, and should also limit local account reuse and monitor for unusual registry hive loading or profile service activity.

**Windows Container Isolation FS Filter Driver (unionfs.sys) Tampering Vulnerability ([CVE-2026-72971](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-72971))**
This vulnerability was publicly disclosed before Patch Tuesday, making it a zero-day, but Microsoft says it has not been exploited in the wild; it is rated Important with a CVSS score of 5.5. The flaw is an improper link-resolution, or “link following,” issue in the Windows Container Isolation file system filter driver, unionfs.sys, affecting Windows 11 Version 26H1 on x64 and ARM64 systems. A local, authenticated attacker could exploit it with low complexity and no user interaction to tamper with files, resulting in high integrity impact, though Microsoft rates confidentiality and availability impact as none. Administrators should apply the Windows updates that correct the driver’s link-handling behavior, particularly on systems using Windows containers or container isolation features.

**Microsoft QUIC Remote Code Execution Vulnerability ([CVE-2026-62815](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-62815))**
This Critical Microsoft QUIC remote code execution vulnerability is not listed as exploited in the wild or publicly disclosed. It carries a CVSS score of 9.8 and is a use-after-free flaw that could allow an unauthenticated remote attacker to send a specially crafted packet to an affected service over the network and execute code on the target system, with no user interaction required. Affected platforms include Windows 11 and Windows Server 2022/2025, including Server Core installations. Administrators should prioritize applying the Microsoft update, especially on systems exposing QUIC-enabled services to untrusted networks, and consider limiting network exposure where patching cannot be completed immediately.

**Windows DNS Server Remote Code Execution Vulnerability ([CVE-2026-62878](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-62878))**
Microsoft reports that CVE-2026-62878 is neither exploited in the wild nor publicly disclosed; it is a Critical Windows DNS Server remote code execution vulnerability with a CVSS score of 9.8. The flaw is a stack-based buffer overflow in Windows DNS that can be triggered remotely by an unauthenticated attacker sending a specially crafted packet to an affected service over the network, with no user interaction required, potentially allowing code execution on the target DNS server. Affected systems include multiple Windows Server releases from 2012 through 2025, as well as listed Windows 10 versions where the vulnerable component is present. Administrators should apply Microsoft’s security updates promptly, especially on DNS servers, and reduce exposure by limiting DNS service access to trusted networks where possible, blocking unnecessary inbound traffic at firewalls, and monitoring DNS servers for crashes or anomalous traffic patterns.

This was a summary of Microsoft’s monthly updates highlighting some important vulnerabilities. Prioritize the exploited WinSock privilege-escalation flaw, then the publicly disclosed User Profile Service and unionfs.sys issues, and patch internet-exposed QUIC services and DNS servers quickly due to remote code execution risk.

A detailed list of this month's vulnerabilities follows below. To search and filter them, visit my dashboard: <https://patchlens.io>

| Description | | | | | | | |
| --- | --- | --- | --- | --- | --- | --- | --- |
| CVE | Disclosed | Exploited | Exploitability (old versions) | current version | Severity | CVSS Base (AVG) | CVSS Temporal (AVG) |
| .NET Core Remote Code Execution Vulnerability | | | | | | | |
| [CVE-2026-70354](/vuln.html?cve=2026-70354) | No | No | - | - | Important | 7.8 | 6.8 |
| .NET Denial of Service Vulnerability | | | | | | | |
| [CVE-2026-62901](/vuln.html?cve=2026-62901) | No | No | - | - | Important | 7.5 | 6.5 |
| .NET Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2026-62909](/vuln.html?cve=2026-62909) | No | No | - | - | Important | 7.8 | 6.8 |
| [CVE-2026-58641](/vuln.html?cve=2026-58641) | No | No | - | - | Important | 7.8 | 6.8 |
| [CVE-2026-62871](/vuln.html?cve=2026-62871) | No | No | - | - | Important | 7.8 | 6.8 |
| [CVE-2026-62886](/vuln.html?cve=2026-62886) | No | No | - | - | Important | 7.8 | 6.8 |
| .NET Framework Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2026-62872](/vuln.html?cve=2026-62872) | No | No | - | - | Important | 8.8 | 7.7 |
| [CVE-2026-65810](/vuln.html?cve=2026-65810) | No | No | - | - | Important | 7.8 | 6.8 |
| .NET Framework Remote Code Execution Vulnerability | | | | | | | |
| [CVE-2026-62897](/vuln.html?cve=2026-62897) | No | No | - | - | Important | 7.0 | 6.1 |
| .NET Information Disclosure Vulnerability | | | | | | | |
| [CVE-2026-62900](/v...