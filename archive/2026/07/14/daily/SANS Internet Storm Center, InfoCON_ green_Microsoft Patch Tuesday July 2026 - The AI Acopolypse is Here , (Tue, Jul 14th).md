---
title: Microsoft Patch Tuesday July 2026 - The AI Acopolypse is Here , (Tue, Jul 14th)
url: https://isc.sans.edu/diary/rss/33154
source: SANS Internet Storm Center, InfoCON: green
date: 2026-07-14
fetch_date: 2026-07-15T04:49:48.478636
---

# Microsoft Patch Tuesday July 2026 - The AI Acopolypse is Here , (Tue, Jul 14th)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Guy Bruneau](/handler_list.html#guy-bruneau "Guy Bruneau")

Threat Level: [green](/infocon.html)

* [previous](/diary/33150)
* [next](/diary/33156)

Click [HERE](https://www.sans.org/profiles/dr-johannes-ullrich) to learn more about classes Johannes is teaching for SANS

# [Microsoft Patch Tuesday July 2026 - The AI Acopolypse is Here](/forums/diary/Microsoft%2BPatch%2BTuesday%2BJuly%2B2026%2BThe%2BAI%2BAcopolypse%2Bis%2BHere/33154/)

**Published**: 2026-07-14. **Last Updated**: 2026-07-14 19:14:58 UTC
**by** [Johannes Ullrich](https://plus.google.com/101587262224166552564?rel=author) (Version: 1)

[0 comment(s)](/diary/Microsoft%2BPatch%2BTuesday%2BJuly%2B2026%2BThe%2BAI%2BAcopolypse%2Bis%2BHere/33154/#comments)

This patch Tuesday includes a staggering 622 vulnerabilities, not including another 427 vulnerabilities in Chromium, affecting Microsoft's Edge browser. 62 of the vulnerabilities are rated critical. One was disclosed before today, and two have already been exploited.

Given the large number of vulnerabilities, it is difficult to point out "noteworthy" issues.

Already exploited vulnerabilities:

[CVE-2026-56155](/vuln.html?cve=2026-56155) : Active Directory Federation Services Elevation of Privilege Vulnerability. This is an important (not critical) vulnerablity.

[CVE-2026-56164](/vuln.html?cve=2026-56164): Microsoft SharePoint Server Elevation of Privilege Vulnerability. Microsoft considers this vulnerability's severity only moderate.

Disclosed but not yet exploited:

[CVE-2026-50661](/vuln.html?cve=2026-50661): Windows BitLocker Security Feature Bypass Vulnerability. It is not clear right now if this is one of the Nightmare Eclipse vulnerabilities. "Anonymous" is credited with discovering the vulnerability.

Random Interesting Vulnerabilities:

[CVE-2026-54128](/vuln.html?cve=2026-54128): Windows DHCP Client Remote Code Execution Vulnerability. A critical vulnerability, but it will require the victim to connect to a network exposed to a malicious DHCP server. Certainly interesting for "public wifi network" attacks. There are also a few critical DHCP server RCE vulnerabilities being addressed in this update.

[CVE-2026-54982](/vuln.html?cve=2026-54982), [CVE-2026-54995](/vuln.html?cve=2026-54995): Windows Reliable Multicast Transport Driver (RMCAST) Remote Code Execution Vulnerability. Two critical vulnerabilities. Just like DHCP, the exploit will typically require network-adjacent attackers. I have seen several similar vulnerabilities in MSFT updates in the past, but not seen exploits.

A quick word on how to deal with this flood of new vulnerabilities: You still own the same number of Microsoft products. Many products (Office..) are affected by a large number of vulnerabilities. Patching the product should not take a lot more time just because the patch addresses more vulnerabilities.

| Description | | | | | | | |
| --- | --- | --- | --- | --- | --- | --- | --- |
| CVE | Disclosed | Exploited | Exploitability (old versions) | current version | Severity | CVSS Base (AVG) | CVSS Temporal (AVG) |
| .NET Denial of Service Vulnerability | | | | | | | |
| [CVE-2026-47302](/vuln.html?cve=2026-47302) | No | No | - | - | Important | 7.5 | 6.5 |
| [CVE-2026-50525](/vuln.html?cve=2026-50525) | No | No | - | - | Important | 7.5 | 6.5 |
| [CVE-2026-50651](/vuln.html?cve=2026-50651) | No | No | - | - | Important | 7.5 | 6.5 |
| [CVE-2026-57108](/vuln.html?cve=2026-57108) | No | No | - | - | Important | 7.5 | 6.5 |
| .NET Framework Denial of Service Vulnerability | | | | | | | |
| [CVE-2026-50524](/vuln.html?cve=2026-50524) | No | No | - | - | Important | 7.5 | 6.5 |
| [CVE-2026-50527](/vuln.html?cve=2026-50527) | No | No | - | - | Important | 7.5 | 6.5 |
| [CVE-2026-50648](/vuln.html?cve=2026-50648) | No | No | - | - | Important | 7.5 | 6.5 |
| .NET Framework Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2026-50650](/vuln.html?cve=2026-50650) | No | No | - | - | Important | 7.8 | 6.8 |
| .NET Framework Remote Code Execution Vulnerability | | | | | | | |
| [CVE-2026-50646](/vuln.html?cve=2026-50646) | No | No | - | - | Important | 7.8 | 6.8 |
| .NET Remote Code Execution Vulnerability | | | | | | | |
| [CVE-2026-50649](/vuln.html?cve=2026-50649) | No | No | - | - | Important | 7.8 | 6.8 |
| .NET Security Feature Bypass Vulnerability | | | | | | | |
| [CVE-2026-47304](/vuln.html?cve=2026-47304) | No | No | - | - | Important | 8.1 | 7.1 |
| [CVE-2026-50528](/vuln.html?cve=2026-50528) | No | No | - | - | Important | 8.2 | 7.1 |
| .NET Spoofing Vulnerability | | | | | | | |
| [CVE-2026-50659](/vuln.html?cve=2026-50659) | No | No | - | - | Important | 6.5 | 5.7 |
| .NET Tampering Vulnerability | | | | | | | |
| [CVE-2026-50526](/vuln.html?cve=2026-50526) | No | No | - | - | Important | 7.0 | 6.1 |
| ASP.NET Core Denial of Service Vulnerability | | | | | | | |
| [CVE-2026-56170](/vuln.html?cve=2026-56170) | No | No | - | - | Important | 7.5 | 6.5 |
| ASP.NET Core Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2026-47300](/vuln.html?cve=2026-47300) | No | No | - | - | Important | 8.8 | 7.7 |
| [CVE-2026-47303](/vuln.html?cve=2026-47303) | No | No | - | - | Important | 8.8 | 7.7 |
| Active Directory Certificate Services Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2026-54121](/vuln.html?cve=2026-54121) | No | No | - | - | Critical | 8.8 | 7.7 |
| Active Directory Denial of Service Vulnerability | | | | | | | |
| [CVE-2026-50682](/vuln.html?cve=2026-50682) | No | No | - | - | Important | 7.1 | 6.2 |
| Active Directory Domain Services Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2026-55001](/vuln.html?cve=2026-55001) | No | No | - | - | Important | 7.8 | 6.8 |
| Active Directory Federation Server Denial of Service Vulnerability | | | | | | | |
| [CVE-2026-50647](/vuln.html?cve=2026-50647) | No | No | - | - | Important | 7.5 | 6.5 |
| Active Directory Federation Server Spoofing Vulnerability | | | | | | | |
| [CVE-2026-50684](/vuln.html?cve=2026-50684) | No | No | - | - | Important | 4.8 | 4.2 |
| Active Directory Federation Services Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2026-56155](/vuln.html?cve=2026-56155) | No | Yes | - | - | Important | 7.8 | 7.2 |
| Azure Active Directory Denial of Service Vulnerability | | | | | | | |
| [CVE-2026-50652](/vuln.html?cve=2026-50652) | No | No | - | - | Important | 7.5 | 6.5 |
| [CVE-2026-50653](/vuln.html?cve=2026-50653) | No | No | - | - | Important | 7.5 | 6.5 |
| Azure CycleCloud Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2026-57969](/vuln.html?cve=2026-57969) | No | No | - | - | Important | 8.8 | 7.7 |
| [CVE-2026-58279](/vuln.html?cve=2026-58279) | No | No | - | - | Important | 6.5 | 5.9 |
| Azure Monitor Agent Metrics Extension Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2026-47632](/vuln.html?cve=2026-47632) | No | No | - | - | Important | 8.8 | 7.7 |
| Azure OpenAI Elevation of Privilege Vulnerability  (no customer action required) | | | | | | | |
| [CVE-2026-45499](/vuln.html?cve=2026-45499) | No | No | - | - | Critical | 9.9 | 8.6 |
| Azure Spring Apps Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2026-50338](/vuln.html?cve=2026-50338) | No | No | - | - | Important | 8.2 | 7.4 |
| CVE-2026-13862 | | | | | | | |
| [CVE-2026-13862](/vuln.html?cve=2026-13862) | No | No | - | - | - |  |  |
| Clipboard User Service Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2026-50488](/vuln.html?cve=2026-50488) | No | No | - | - | Important | 7.8 | 6.8 |
| Code Integrity DLL (ci.dll) Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2026-50491](/vuln.html?cve=2026-50491) | No | No | - | - | Important | 7.0 | 6.1 |
| Composite Image File System driver (cimfs.sys) Information Disclosure Vulnerability | | | | | | | |
| [CVE-2026-50381](/vuln.html?cve=2026-50381) | No | No | - | - | Import...