---
title: Microsoft August 2024 Patch Tuesday, (Tue, Aug 13th)
url: https://isc.sans.edu/diary/rss/31164
source: SANS Internet Storm Center, InfoCON: green
date: 2024-08-14
fetch_date: 2025-10-06T18:06:05.639401
---

# Microsoft August 2024 Patch Tuesday, (Tue, Aug 13th)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Johannes Ullrich](/handler_list.html#johannes-ullrich "Johannes Ullrich")

Threat Level: [green](/infocon.html)

* [previous](/diary/31158)
* [next](/diary/31168)

# [Microsoft August 2024 Patch Tuesday](/forums/diary/Microsoft%2BAugust%2B2024%2BPatch%2BTuesday/31164/)

**Published**: 2024-08-13. **Last Updated**: 2024-08-13 20:14:47 UTC
**by** [Renato Marinho](/handler_list.html#renato-marinho) (Version: 1)

[0 comment(s)](/diary/Microsoft%2BAugust%2B2024%2BPatch%2BTuesday/31164/#comments)

This month we got patches for 92 vulnerabilities. Of these, 9 are critical, and 9 are zero-days (3 previously disclosed, and 6 are already being exploited).

The CVEs [CVE-2024-38189](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2024-38189), [CVE-2024-38178](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2024-38178), [CVE-2024-38193](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2024-38193), [CVE-2024-38106](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2024-38106), [CVE-2024-38213](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2024-38213), and [CVE-2024-38107](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2024-38107) are related to the already exploited vulnerabilities and the CVEs [CVE-2024-38202](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2024-38202), [CVE-2024-21302](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2024-21302), and [CVE-2024-38200](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2024-38200) are related to previously disclosed ones.

Amongst exploited vulnerabilities, the highest CVSS (CVSS 8.8) is related to the Microsoft Project Remote Code Execution Vulnerability ([CVE-2024-38189](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2024-38189)) rated as Important. According to the advisory, Exploitation requires the victim to open a malicious Microsoft Office Project file on a system where the Block macros from running in Office files from the Internet policy is disabled and VBA Macro Notification Settings are not enabled allowing the attacker to perform remote code execution.

Amongst critical vulnerabilities, one of the two 9.8 CVSS this month is associated to the Windows Reliable Multicast Transport Driver (RMCAST) Remote Code Execution Vulnerability ([CVE-2024-38140](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2024-38140)). According to the exploit, this vulnerability is exploitable only if there is a program listening on a Pragmatic General Multicast (PGM) port. If PGM is installed or enabled but no programs are actively listening as a receiver, then this vulnerability is not exploitable. An unauthenticated attacker could exploit the vulnerability by sending specially crafted packets to a Windows Pragmatic General Multicast (PGM) open socket on the server, without any interaction from the user.

The other CVSS 9.8 is associated with the Windows TCP/IP Remote Code Execution Vulnerability ([CVE-2024-38063](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2024-38063)). Systems are not affected if IPv6 is disabled on the target machine. The advisory says that an unauthenticated attacker could repeatedly send IPv6 packets, that include specially crafted packets, to a Windows machine which could enable remote code execution.

| Description | | | | | | | |
| --- | --- | --- | --- | --- | --- | --- | --- |
| CVE | Disclosed | Exploited | Exploitability (old versions) | current version | Severity | CVSS Base (AVG) | CVSS Temporal (AVG) |
| .NET and Visual Studio Denial of Service Vulnerability | | | | | | | |
| [CVE-2024-38168](/vuln.html?cve=2024-38168) | No | No | - | - | Important | 7.5 | 6.5 |
| .NET and Visual Studio Information Disclosure Vulnerability | | | | | | | |
| [CVE-2024-38167](/vuln.html?cve=2024-38167) | No | No | - | - | Important | 6.5 | 5.7 |
| Azure Connected Machine Agent Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2024-38098](/vuln.html?cve=2024-38098) | No | No | - | - | Important | 7.8 | 6.8 |
| [CVE-2024-38162](/vuln.html?cve=2024-38162) | No | No | - | - | Important | 7.8 | 6.8 |
| Azure CycleCloud Remote Code Execution Vulnerability | | | | | | | |
| [CVE-2024-38195](/vuln.html?cve=2024-38195) | No | No | - | - | Important | 7.8 | 6.8 |
| Azure Health Bot Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2024-38109](/vuln.html?cve=2024-38109) | No | No | - | - | Critical | 9.1 | 7.9 |
| Azure IoT SDK Remote Code Execution Vulnerability | | | | | | | |
| [CVE-2024-38157](/vuln.html?cve=2024-38157) | No | No | - | - | Important | 7.0 | 6.1 |
| [CVE-2024-38158](/vuln.html?cve=2024-38158) | No | No | - | - | Important | 7.0 | 6.1 |
| Azure Stack Hub Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2024-38201](/vuln.html?cve=2024-38201) | No | No | - | - | Important | 7.0 | 6.1 |
| Azure Stack Hub Spoofing Vulnerability | | | | | | | |
| [CVE-2024-38108](/vuln.html?cve=2024-38108) | No | No | - | - | Important | 9.3 | 8.1 |
| Chromium: CVE-2024-6990 Uninitialized Use in Dawn | | | | | | | |
| [CVE-2024-6990](/vuln.html?cve=2024-6990) | No | No | - | - | - |  |  |
| Chromium: CVE-2024-7255 Out of bounds read in WebTransport | | | | | | | |
| [CVE-2024-7255](/vuln.html?cve=2024-7255) | No | No | - | - | - |  |  |
| Chromium: CVE-2024-7256 Insufficient data validation in Dawn | | | | | | | |
| [CVE-2024-7256](/vuln.html?cve=2024-7256) | No | No | - | - | - |  |  |
| Chromium: CVE-2024-7532 Out of bounds memory access in ANGLE | | | | | | | |
| [CVE-2024-7550](/vuln.html?cve=2024-7550) | No | No | - | - | - |  |  |
| Chromium: CVE-2024-7533 Use after free in Sharing | | | | | | | |
| [CVE-2024-7532](/vuln.html?cve=2024-7532) | No | No | - | - | - |  |  |
| Chromium: CVE-2024-7534 Heap buffer overflow in Layout | | | | | | | |
| [CVE-2024-7533](/vuln.html?cve=2024-7533) | No | No | - | - | - |  |  |
| Chromium: CVE-2024-7535 Inappropriate implementation in V8 | | | | | | | |
| [CVE-2024-7534](/vuln.html?cve=2024-7534) | No | No | - | - | - |  |  |
| Chromium: CVE-2024-7536 Use after free in WebAudio | | | | | | | |
| [CVE-2024-7535](/vuln.html?cve=2024-7535) | No | No | - | - | - |  |  |
| Chromium: CVE-2024-7550 Type Confusion in V8 | | | | | | | |
| [CVE-2024-7536](/vuln.html?cve=2024-7536) | No | No | - | - | - |  |  |
| Clipboard Virtual Channel Extension Remote Code Execution Vulnerability | | | | | | | |
| [CVE-2024-38131](/vuln.html?cve=2024-38131) | No | No | - | - | Important | 8.8 | 7.7 |
| Kernel Streaming Service Driver Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2024-38191](/vuln.html?cve=2024-38191) | No | No | - | - | Important | 7.8 | 6.8 |
| Kernel Streaming WOW Thunk Service Driver Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2024-38125](/vuln.html?cve=2024-38125) | No | No | - | - | Important | 7.8 | 6.8 |
| [CVE-2024-38134](/vuln.html?cve=2024-38134) | No | No | - | - | Important | 7.8 | 6.8 |
| [CVE-2024-38144](/vuln.html?cve=2024-38144) | No | No | - | - | Important | 8.8 | 7.7 |
| Microsoft Copilot Studio Information Disclosure Vulnerability | | | | | | | |
| [CVE-2024-38206](/vuln.html?cve=2024-38206) | No | No | - | - | Critical | 8.5 | 7.4 |
| Microsoft DWM Core Library Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2024-38147](/vuln.html?cve=2024-38147) | No | No | - | - | Important | 7.8 | 6.8 |
| Microsoft Dynamics 365 (on-premises) Cross-site Scripting Vulnerability | | | | | | | |
| [CVE-2024-38211](/vuln.html?cve=2024-38211) | No | No | - | - | Important | 8.2 | 7.1 |
| Microsoft Dynamics 365 Cross-site Scripting Vulnerability | | | | | | | |
| [CVE-2024-38166](/vuln.html?cve=2024-38166) | No | No | - | - | Critical | 8.2 | 7.1 |
| Microsoft Edge (Chromium-based) Information Disclosure Vulnerability | | | | | | | |
| [CVE-2024-38222](/vuln.html?cve=2024-38222) | No | No | Less Likely |...