---
title: Microsoft Patch Tuesday April 2026., (Tue, Apr 14th)
url: https://isc.sans.edu/diary/rss/32898
source: SANS Internet Storm Center, InfoCON: green
date: 2026-04-14
fetch_date: 2026-04-15T04:44:07.179741
---

# Microsoft Patch Tuesday April 2026., (Tue, Apr 14th)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Guy Bruneau](/handler_list.html#guy-bruneau "Guy Bruneau")

Threat Level: [green](/infocon.html)

* [previous](/diary/32896)

Click [HERE](https://www.sans.org/profiles/dr-johannes-ullrich) to learn more about classes Johannes is teaching for SANS

# [Microsoft Patch Tuesday April 2026.](/forums/diary/Microsoft%2BPatch%2BTuesday%2BApril%2B2026/32898/)

**Published**: 2026-04-14. **Last Updated**: 2026-04-14 17:46:09 UTC
**by** [Johannes Ullrich](https://plus.google.com/101587262224166552564?rel=author) (Version: 1)

[0 comment(s)](/diary/Microsoft%2BPatch%2BTuesday%2BApril%2B2026/32898/#comments)

This month's Microsoft Patch Tuesday looks like a record one, but let's look at it a bit closer to understand what is happening

The update patches a total of 243 vulnerabilities. However, 78 of them are Chromium issues affecting Microsoft Edge. Patches for Edge were released earlier. This leaves 165 vulnerabilities that are not Edge-related. Of these, 8 are rated critical, and 154 are important. One vulnerability has already been exploited, and another was made public before today but has not yet been seen in the wild.

Noteworthy Vulnerabilities:

CVE-2026-33827 (Windows TCP/IP Remote Code Execution Vulnerability): As a packet nerd, I love these types of vulnerabilities. Need to know more to really figure out the impact. Microsoft describes this as a race condition, allowing attackers to execute arbitrary code over the network. Exploitation is likely tricky, but never underestimate the creativity of an AI aided attacker.

CVE-2026-33825 (Microsoft Defender Elevation of Privilege Vulnerability): This vulnerability has already been disclosed.

CVE-2026-32201 (Microsoft SharePoint Server Spoofing Vulnerability): Two similar SharePoint server spoofing vulnerabilities were patched this month. Both are rated important, and this particular one is already being exploited.

CVE-2026-33826 (Windows Active Directory Remote Code Execution Vulnerability): CVSS score of "only" 8.0, but critical according to Microsoft.

CVE-2026-32190 (Microsoft Office Remote Code Execution Vulnerability): Standard fair for every monthly patch Tuesday. These are often the more worrisome vulnerabilities. Two additional critical RCE vulnerabilities affect Word (CVE-2026-33114, CVE-2026-33115).

CVE-2026-32157 (Remote Desktop Client Remote Code Execution Vulnerability): Typically, these vulnerabilities require a user to connect to a malicious RDP server, but connections may be initiated by clicking on an "rdp:" link.

CVE-2026-33824 (Windows Internet Key Exchange (IKE) Service Extensions Remote Code Execution Vulnerability): IKE, part of IPSEC, is usually not enabled by default. It isn't clear yet what the exact exploitation requirements are (will update once MSFT's page responds again)

CVE-2026-23666 (.NET Framework Denial of Service Vulnerability): Just a denial of service. Not sure why this deserved "critical".

| Description | | | | | | | |
| --- | --- | --- | --- | --- | --- | --- | --- |
| CVE | Disclosed | Exploited | Exploitability (old versions) | current version | Severity | CVSS Base (AVG) | CVSS Temporal (AVG) |
| .NET Denial of Service Vulnerability | | | | | | | |
| [CVE-2026-26171](/vuln.html?cve=2026-26171) | No | No | - | - | Important | 7.5 | 6.5 |
| .NET Framework Denial of Service Vulnerability | | | | | | | |
| [CVE-2026-32226](/vuln.html?cve=2026-32226) | No | No | - | - | Important | 5.9 | 5.2 |
| [CVE-2026-23666](/vuln.html?cve=2026-23666) | No | No | - | - | Critical | 7.5 | 6.7 |
| .NET Spoofing Vulnerability | | | | | | | |
| [CVE-2026-32178](/vuln.html?cve=2026-32178) | No | No | - | - | Important | 7.5 | 6.5 |
| .NET and Visual Studio Denial of Service Vulnerability | | | | | | | |
| [CVE-2026-32203](/vuln.html?cve=2026-32203) | No | No | - | - | Important | 7.5 | 6.5 |
| .NET, .NET Framework, and Visual Studio Denial of Service Vulnerability | | | | | | | |
| [CVE-2026-33116](/vuln.html?cve=2026-33116) | No | No | - | - | Important | 7.5 | 6.5 |
| Active Directory Spoofing Vulnerability | | | | | | | |
| [CVE-2026-32072](/vuln.html?cve=2026-32072) | No | No | - | - | Important | 6.2 | 5.4 |
| Applocker Filter Driver (applockerfltr.sys) Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2026-25184](/vuln.html?cve=2026-25184) | No | No | - | - | Important | 7.0 | 6.1 |
| Azure Logic Apps Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2026-32171](/vuln.html?cve=2026-32171) | No | No | - | - | Important | 8.8 | 7.7 |
| Azure Monitor Agent Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2026-32168](/vuln.html?cve=2026-32168) | No | No | - | - | Important | 7.8 | 6.8 |
| [CVE-2026-32192](/vuln.html?cve=2026-32192) | No | No | - | - | Important | 7.8 | 6.8 |
| Chromium: CVE-2026-5272 Heap buffer overflow in GPU | | | | | | | |
| [CVE-2026-5272](/vuln.html?cve=2026-5272) | No | No | - | - | - |  |  |
| Chromium: CVE-2026-5273 Use after free in CSS | | | | | | | |
| [CVE-2026-5273](/vuln.html?cve=2026-5273) | No | No | - | - | - |  |  |
| Chromium: CVE-2026-5274 Integer overflow in Codecs | | | | | | | |
| [CVE-2026-5274](/vuln.html?cve=2026-5274) | No | No | - | - | - |  |  |
| Chromium: CVE-2026-5275 Heap buffer overflow in ANGLE | | | | | | | |
| [CVE-2026-5275](/vuln.html?cve=2026-5275) | No | No | - | - | - |  |  |
| Chromium: CVE-2026-5276 Insufficient policy enforcement in WebUSB | | | | | | | |
| [CVE-2026-5276](/vuln.html?cve=2026-5276) | No | No | - | - | - |  |  |
| Chromium: CVE-2026-5277 Integer overflow in ANGLE | | | | | | | |
| [CVE-2026-5277](/vuln.html?cve=2026-5277) | No | No | - | - | - |  |  |
| Chromium: CVE-2026-5279 Object corruption in V8 | | | | | | | |
| [CVE-2026-5279](/vuln.html?cve=2026-5279) | No | No | - | - | - |  |  |
| Chromium: CVE-2026-5280 Use after free in WebCodecs | | | | | | | |
| [CVE-2026-5280](/vuln.html?cve=2026-5280) | No | No | - | - | - |  |  |
| Chromium: CVE-2026-5281 Use after free in Dawn | | | | | | | |
| [CVE-2026-5281](/vuln.html?cve=2026-5281) | No | No | - | - | - |  |  |
| Chromium: CVE-2026-5283 Inappropriate implementation in ANGLE | | | | | | | |
| [CVE-2026-5283](/vuln.html?cve=2026-5283) | No | No | - | - | - |  |  |
| Chromium: CVE-2026-5284 Use after free in Dawn | | | | | | | |
| [CVE-2026-5284](/vuln.html?cve=2026-5284) | No | No | - | - | - |  |  |
| Chromium: CVE-2026-5285 Use after free in WebGL | | | | | | | |
| [CVE-2026-5285](/vuln.html?cve=2026-5285) | No | No | - | - | - |  |  |
| Chromium: CVE-2026-5286 Use after free in Dawn | | | | | | | |
| [CVE-2026-5286](/vuln.html?cve=2026-5286) | No | No | - | - | - |  |  |
| Chromium: CVE-2026-5287 Use after free in PDF | | | | | | | |
| [CVE-2026-5287](/vuln.html?cve=2026-5287) | No | No | - | - | - |  |  |
| Chromium: CVE-2026-5289 Use after free in Navigation | | | | | | | |
| [CVE-2026-5289](/vuln.html?cve=2026-5289) | No | No | - | - | - |  |  |
| Chromium: CVE-2026-5290 Use after free in Compositing | | | | | | | |
| [CVE-2026-5290](/vuln.html?cve=2026-5290) | No | No | - | - | - |  |  |
| Chromium: CVE-2026-5291 Inappropriate implementation in WebGL | | | | | | | |
| [CVE-2026-5291](/vuln.html?cve=2026-5291) | No | No | - | - | - |  |  |
| Chromium: CVE-2026-5292 Out of bounds read in WebCodecs | | | | | | | |
| [CVE-2026-5292](/vuln.html?cve=2026-5292) | No | No | - | - | - |  |  |
| Chromium: CVE-2026-5858 Heap buffer overflow in WebML | | | | | | | |
| [CVE-2026-5858](/vuln.html?cve=2026-5858) | No | No | - | - | - |  |  |
| Chromium: CVE-2026-5859 Integer overflow in WebML | | | | | | | |
| [CVE-2026-5859](/vuln.html?cve=2026-5859) | No | No | - | - | - |  |  |
| Chromium: CVE-2026-5860 Use after free in WebRTC | | | | | | | |
| [CVE-2026-5860](/vuln.html?cve=2026-5860) | No | No | - | - | - |  |  |
| Chromium: CVE-2026-5861 Use after free in V8 | | | | | | | |
| [CVE-2026-5861](/vuln.html?cve=2026-5861) | No...