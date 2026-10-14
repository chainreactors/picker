---
title: October 2026 Microsoft Patch Tuesday, (Tue, Oct 13th)
url: https://isc.sans.edu/diary/rss/33422
source: SANS Internet Storm Center, InfoCON: green
date: 2026-10-13
fetch_date: 2026-10-14T06:53:22.073996
---

# October 2026 Microsoft Patch Tuesday, (Tue, Oct 13th)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Didier Stevens](/handler_list.html#didier-stevens "Didier Stevens")

Threat Level: [green](/infocon.html)

* [previous](/diary/33420)

Click [HERE](https://www.sans.org/profiles/dr-johannes-ullrich) to learn more about classes Johannes is teaching for SANS

# [October 2026 Microsoft Patch Tuesday](/forums/diary/October%2B2026%2BMicrosoft%2BPatch%2BTuesday/33422/)

**Published**: 2026-10-13. **Last Updated**: 2026-10-13 19:25:52 UTC
**by** [Johannes Ullrich](https://plus.google.com/101587262224166552564?rel=author) (Version: 1)

[0 comment(s)](/diary/October%2B2026%2BMicrosoft%2BPatch%2BTuesday/33422/#comments)

Microsoft today released patches for 1,417 vulnerabilities. 76 of these vulnerabilities are rated critical, with 7 critical vulnerabiilties requiring no customer actions. One vulnerability was disclosed before today's patch Tuesday, and one is already exploited.

**CVE-2026-96951**: An already exploited Windows Shell Security Feature Bypass Vulnerability. This vulnerabliity allows bypassing the "Mark of the Web" making it easier to exeucte code by sending a malicious message to a user via e-mail or instant messaging. The victim will still have to open the file.

**CVE-2026-108398**: This vulnerability, a .NET framework security feature bypass, could be used to bypass application control and execute unauthorized applications. Details were available public head of today's release, but Microsoft did not detect exploitation in the wild.

**Windows DHCP Server**: 10 remote code execution vulenrabilities, including five critical vulnerabilities, affect the Windows DHCP server.

**CVE-2026-70571**: Microsoft Exchange Server Remote Code Execution Vulnerability. Microsoft considers the attack complexity high. The vulnerability is triggered by an attacker sending a specific email to the exchange server that triggers the vulnerability during content conversion.

Aside from these specific vulnerabilities, the larger number of Office vulnerabilities is noteworthy, and the Office updates should likely be addressed quickly.

| Description | | | | | | | |
| --- | --- | --- | --- | --- | --- | --- | --- |
| CVE | Disclosed | Exploited | Exploitability (old versions) | current version | Severity | CVSS Base (AVG) | CVSS Temporal (AVG) |
| .NET Denial of Service Vulnerability | | | | | | | |
| [CVE-2026-58280](/vuln.html?cve=2026-58280) | No | No | - | - | Important | 7.5 | 6.5 |
| [CVE-2026-69651](/vuln.html?cve=2026-69651) | No | No | - | - | Important | 7.5 | 6.5 |
| [CVE-2026-70162](/vuln.html?cve=2026-70162) | No | No | - | - | Important | 5.9 | 5.2 |
| [CVE-2026-84008](/vuln.html?cve=2026-84008) | No | No | - | - | Important | 7.5 | 6.5 |
| [CVE-2026-96958](/vuln.html?cve=2026-96958) | No | No | - | - | Important | 7.5 | 6.5 |
| [CVE-2026-96959](/vuln.html?cve=2026-96959) | No | No | - | - | Important | 7.5 | 6.5 |
| [CVE-2026-96960](/vuln.html?cve=2026-96960) | No | No | - | - | Important | 7.5 | 6.5 |
| .NET Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2026-70161](/vuln.html?cve=2026-70161) | No | No | - | - | Important | 7.3 | 6.4 |
| [CVE-2026-70165](/vuln.html?cve=2026-70165) | No | No | - | - | Important | 6.7 | 5.8 |
| [CVE-2026-70190](/vuln.html?cve=2026-70190) | No | No | - | - | Important | 7.3 | 6.4 |
| [CVE-2026-96225](/vuln.html?cve=2026-96225) | No | No | - | - | Important | 7.8 | 6.8 |
| [CVE-2026-96231](/vuln.html?cve=2026-96231) | No | No | - | - | Important | 7.8 | 6.8 |
| .NET Framework Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2026-85363](/vuln.html?cve=2026-85363) | No | No | - | - | Important | 8.8 | 7.7 |
| .NET Framework Remote Code Execution Vulnerability | | | | | | | |
| [CVE-2026-70007](/vuln.html?cve=2026-70007) | No | No | - | - | Important | 8.8 | 7.7 |
| [CVE-2026-70035](/vuln.html?cve=2026-70035) | No | No | - | - | Important | 8.8 | 7.7 |
| .NET Framework Security Feature Bypass Vulnerability | | | | | | | |
| [CVE-2026-108398](/vuln.html?cve=2026-108398) | Yes | No | - | - | Important | 8.8 | 7.7 |
| [CVE-2026-70194](/vuln.html?cve=2026-70194) | No | No | - | - | Important | 6.5 | 5.7 |
| .NET Framework Tampering Vulnerability | | | | | | | |
| [CVE-2026-97801](/vuln.html?cve=2026-97801) | No | No | - | - | Important | 7.5 | 6.5 |
| .NET Information Disclosure Vulnerability | | | | | | | |
| [CVE-2026-66822](/vuln.html?cve=2026-66822) | No | No | - | - | Important | 5.9 | 5.2 |
| [CVE-2026-96229](/vuln.html?cve=2026-96229) | No | No | - | - | Important | 6.5 | 5.7 |
| [CVE-2026-96232](/vuln.html?cve=2026-96232) | No | No | - | - | Important | 7.5 | 6.5 |
| [CVE-2026-96234](/vuln.html?cve=2026-96234) | No | No | - | - | Important | 5.3 | 4.6 |
| .NET Remote Code Execution Vulnerability | | | | | | | |
| [CVE-2026-70174](/vuln.html?cve=2026-70174) | No | No | - | - | Important | 8.8 | 7.7 |
| [CVE-2026-70197](/vuln.html?cve=2026-70197) | No | No | - | - | Important | 8.1 | 7.1 |
| [CVE-2026-83520](/vuln.html?cve=2026-83520) | No | No | - | - | Important | 8.8 | 7.7 |
| [CVE-2026-87697](/vuln.html?cve=2026-87697) | No | No | - | - | Important | 8.8 | 7.7 |
| [CVE-2026-96224](/vuln.html?cve=2026-96224) | No | No | - | - | Important | 8.8 | 7.7 |
| [CVE-2026-96235](/vuln.html?cve=2026-96235) | No | No | - | - | Important | 8.8 | 7.7 |
| [CVE-2026-96237](/vuln.html?cve=2026-96237) | No | No | - | - | Important | 7.5 | 6.5 |
| .NET Security Feature Bypass Vulnerability | | | | | | | |
| [CVE-2026-96238](/vuln.html?cve=2026-96238) | No | No | - | - | Important | 6.5 | 5.7 |
| [CVE-2026-96957](/vuln.html?cve=2026-96957) | No | No | - | - | Important | 8.8 | 7.7 |
| .NET and Visual Studio Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2026-102869](/vuln.html?cve=2026-102869) | No | No | - | - | Important | 8.8 | 7.7 |
| ADV260001 Hardening changes for ReFS volumes on removable media | | | | | | | |
| [ADV260001](https://portal.msrc.microsoft.com/en-us/security-guidance/advisory/ADV260001) | No | No | - | - | None |  |  |
| ASP.NET Core Denial of Service Vulnerability | | | | | | | |
| [CVE-2026-70159](/vuln.html?cve=2026-70159) | No | No | - | - | Important | 7.5 | 6.5 |
| [CVE-2026-70181](/vuln.html?cve=2026-70181) | No | No | - | - | Important | 7.5 | 6.5 |
| [CVE-2026-70186](/vuln.html?cve=2026-70186) | No | No | - | - | Important | 7.5 | 6.5 |
| [CVE-2026-70196](/vuln.html?cve=2026-70196) | No | No | - | - | Important | 5.9 | 5.2 |
| [CVE-2026-96233](/vuln.html?cve=2026-96233) | No | No | - | - | Important | 7.5 | 6.5 |
| [CVE-2026-96236](/vuln.html?cve=2026-96236) | No | No | - | - | Important | 7.5 | 6.5 |
| ASP.NET Core Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2026-70175](/vuln.html?cve=2026-70175) | No | No | - | - | Important | 8.1 | 7.1 |
| [CVE-2026-70179](/vuln.html?cve=2026-70179) | No | No | - | - | Important | 7.5 | 6.5 |
| [CVE-2026-70183](/vuln.html?cve=2026-70183) | No | No | - | - | Important | 7.5 | 6.5 |
| ASP.NET Core Remote Code Execution Vulnerability | | | | | | | |
| [CVE-2026-102870](/vuln.html?cve=2026-102870) | No | No | - | - | Important | 8.8 | 7.7 |
| [CVE-2026-96230](/vuln.html?cve=2026-96230) | No | No | - | - | Important | 8.8 | 7.7 |
| ASP.NET Core Security Feature Bypass Vulnerability | | | | | | | |
| [CVE-2026-70188](/vuln.html?cve=2026-70188) | No | No | - | - | Important | 9.1 | 7.9 |
| ASP.NET Core Tampering Vulnerability | | | | | | | |
| [CVE-2026-88092](/vuln.html?cve=2026-88092) | No | No | - | - | Important | 9.4 | 8.2 |
| Active Directory Certificate Services (AD CS) Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2026-83666](/vuln.html?cve=2026-83666) | No | No | - | - | Important | 7.0 | 6.1 |
| Active Directory Federation Services (AD FS) Denial of Service Vulnerability | | | | | | | |
| [CVE-2026-83645](/vuln.html?cve=2026-83645) | No | No | - | - | Important | 7.5 | 6.5 |
| [CVE-2026-85319](/vuln.html?cve=...