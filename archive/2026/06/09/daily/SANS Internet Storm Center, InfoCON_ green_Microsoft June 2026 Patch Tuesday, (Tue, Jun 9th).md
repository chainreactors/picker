---
title: Microsoft June 2026 Patch Tuesday, (Tue, Jun 9th)
url: https://isc.sans.edu/diary/rss/33064
source: SANS Internet Storm Center, InfoCON: green
date: 2026-06-09
fetch_date: 2026-06-10T06:17:07.947422
---

# Microsoft June 2026 Patch Tuesday, (Tue, Jun 9th)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Jan Kopriva](/handler_list.html#jan-kopriva "Jan Kopriva")

Threat Level: [green](/infocon.html)

* [previous](/diary/33060)

Click [HERE](https://www.sans.org/profiles/dr-johannes-ullrich) to learn more about classes Johannes is teaching for SANS

# [Microsoft June 2026 Patch Tuesday](/forums/diary/Microsoft%2BJune%2B2026%2BPatch%2BTuesday/33064/)

**Published**: 2026-06-09. **Last Updated**: 2026-06-09 17:34:29 UTC
**by** [Johannes Ullrich](https://plus.google.com/101587262224166552564?rel=author) (Version: 1)

[0 comment(s)](/diary/Microsoft%2BJune%2B2026%2BPatch%2BTuesday/33064/#comments)

Microsoft today released patches for 204 vulnerabilities. 38 of these vulnerabilities are considered critical, and three have been disclosed before today. Six of the vulnerabilities affect Microsoft cloud solutions and do not require any user action. In addition, Microsoft incorporated 360 different vulnerabilities affecting Chromium into its Edge browser.

This is certainly a busier-than-usual patch Tuesday. In particular, the large number of patched Chromium/Edge vulnerabilities underscores the impact of AI tools on vulnerability discovery.

Some noteworthy vulnerabilities:

**CVE-2026-49160**: This vulnerability was made public a week ago. As implemented, the "HPACK" compression algorithm in HTTP/2 and HTTP/3 can lead to a "compression bomb" that consumes excessive resources. Many HTTP/2 implementations are vulnerable. Microsoft addressed this issue by adding a "MaxHeadersCount" registry setting that limits the amount of allocated resources.

**CVE-2026-47291**: Affecting the Microsoft web server engine http.sys, just like CVE-2026-49160, this vulnerability is rated critical and allows for remote code execution. The integer overflow requires an oversized request to trigger it. Microsoft recommends restricting the "MaxRequestBytes" to prevent exploitation until the patch can be rolled out.

CVE-2026-45648: A stack-based buffer overflow in Active Directory Domain Services. A successful attack requires authentication, and Microsoft considers exploit development as "unlikely".

Microsoft fixed three different BitLocker security feature bypass vulnerabilities. One of the vulnerabilities was already publicly known. An "anonymous" researcher is credited with the discovery, but I assume it is one of the "Nightmare Eclipse" vulnerabilities.

Several critical vulnerabilities affect Microsoft Office, Outlook, and Word.

| Description | | | | | | | |
| --- | --- | --- | --- | --- | --- | --- | --- |
| CVE | Disclosed | Exploited | Exploitability (old versions) | current version | Severity | CVSS Base (AVG) | CVSS Temporal (AVG) |
| .NET SDK Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2026-45490](/vuln.html?cve=2026-45490) | No | No | - | - | Important | 7.8 | 6.8 |
| .NET Tampering Vulnerability | | | | | | | |
| [CVE-2026-45491](/vuln.html?cve=2026-45491) | No | No | - | - | Important | 6.2 | 5.4 |
| ASP.NET Core Denial of Service Vulnerability | | | | | | | |
| [CVE-2026-45591](/vuln.html?cve=2026-45591) | No | No | - | - | Important | 7.5 | 6.5 |
| Azure HorizonDB Elevation of Privilege Vulnerability  (no customer action required) | | | | | | | |
| [CVE-2026-48567](/vuln.html?cve=2026-48567) | No | No | - | - | Critical | 10.0 | 8.7 |
| Azure Kubernetes Service (AKS) Remote Code Execution Vulnerability | | | | | | | |
| [CVE-2026-32193](/vuln.html?cve=2026-32193) | No | No | - | - | Critical | 8.8 | 7.7 |
| Azure Stack Edge Remote Code Execution Vulnerability | | | | | | | |
| [CVE-2026-47643](/vuln.html?cve=2026-47643) | No | No | - | - | Important | 9.8 | 8.5 |
| Azure Stack Edge Spoofing Vulnerability | | | | | | | |
| [CVE-2026-41098](/vuln.html?cve=2026-41098) | No | No | - | - | Important | 8.4 | 7.3 |
| Copilot Chat (Microsoft Edge) Information Disclosure Vulnerability  (no customer action required) | | | | | | | |
| [CVE-2026-47644](/vuln.html?cve=2026-47644) | No | No | - | - | Critical | 6.5 | 5.7 |
| DHCP Client Service Remote Code Execution Vulnerability | | | | | | | |
| [CVE-2026-44815](/vuln.html?cve=2026-44815) | No | No | - | - | Critical | 9.8 | 8.5 |
| HTTP.sys Denial of Service Vulnerability | | | | | | | |
| [CVE-2026-49160](/vuln.html?cve=2026-49160) | Yes | No | - | - | Important | 7.5 | 6.5 |
| HTTP.sys Remote Code Execution Vulnerability | | | | | | | |
| [CVE-2026-47291](/vuln.html?cve=2026-47291) | No | No | - | - | Critical | 9.8 | 8.5 |
| M365 Copilot Information Disclosure Vulnerability  (no customer action required) | | | | | | | |
| [CVE-2026-42824](/vuln.html?cve=2026-42824) | No | No | - | - | Critical | 6.5 | 5.7 |
| Microsoft Azure Attestation service and Device Health Attestation Service Spoofing Vulnerability | | | | | | | |
| [CVE-2026-45642](/vuln.html?cve=2026-45642) | No | No | - | - | Important | 3.9 | 3.4 |
| Microsoft Azure Network Adapter Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2026-45476](/vuln.html?cve=2026-45476) | No | No | - | - | Critical | 8.2 | 7.1 |
| Microsoft Bing Search Spoofing Vulnerability | | | | | | | |
| [CVE-2026-45650](/vuln.html?cve=2026-45650) | No | No | - | - | Important | 4.3 | 3.8 |
| Microsoft Cryptographic Services Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2026-44810](/vuln.html?cve=2026-44810) | No | No | - | - | Critical | 8.4 | 7.3 |
| Microsoft DWM Core Library Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2026-45637](/vuln.html?cve=2026-45637) | No | No | - | - | Important | 7.8 | 6.8 |
| Microsoft Defender for Endpoint for Mac Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2026-45647](/vuln.html?cve=2026-45647) | No | No | - | - | Important | 5.5 | 4.8 |
| Microsoft Dynamics 365 (on-premises) Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2026-40371](/vuln.html?cve=2026-40371) | No | No | - | - | Important | 8.8 | 7.7 |
| Microsoft Excel Information Disclosure Vulnerability | | | | | | | |
| [CVE-2026-44822](/vuln.html?cve=2026-44822) | No | No | - | - | Important | 8.2 | 7.1 |
| [CVE-2026-45455](/vuln.html?cve=2026-45455) | No | No | - | - | Important | 3.3 | 2.9 |
| Microsoft Excel Remote Code Execution Vulnerability | | | | | | | |
| [CVE-2026-45469](/vuln.html?cve=2026-45469) | No | No | - | - | Important | 7.8 | 6.8 |
| [CVE-2026-44817](/vuln.html?cve=2026-44817) | No | No | - | - | Important | 7.8 | 6.8 |
| [CVE-2026-44818](/vuln.html?cve=2026-44818) | No | No | - | - | Important | 7.0 | 6.1 |
| [CVE-2026-44820](/vuln.html?cve=2026-44820) | No | No | - | - | Important | 7.8 | 6.8 |
| [CVE-2026-44823](/vuln.html?cve=2026-44823) | No | No | - | - | Important | 7.8 | 6.8 |
| Microsoft Excel Security Feature Bypass Vulnerability | | | | | | | |
| [CVE-2026-45459](/vuln.html?cve=2026-45459) | No | No | - | - | Important | 3.3 | 2.9 |
| Microsoft Exchange Online Information Disclosure Vulnerability  (no customer action required) | | | | | | | |
| [CVE-2026-48579](/vuln.html?cve=2026-48579) | No | No | - | - | Critical | 9.1 | 7.9 |
| Microsoft Exchange Server Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2026-45504](/vuln.html?cve=2026-45504) | No | No | - | - | Important | 8.8 | 7.7 |
| Microsoft Exchange Server Information Disclosure Vulnerability | | | | | | | |
| [CVE-2026-45502](/vuln.html?cve=2026-45502) | No | No | - | - | Important | 5.0 | 4.4 |
| [CVE-2026-45503](/vuln.html?cve=2026-45503) | No | No | - | - | Important | 8.1 | 7.1 |
| Microsoft Exchange Server Remote Code Execution Vulnerability | | | | | | | |
| [CVE-2026-45583](/vuln.html?cve=2026-45583) | No | No | - | - | Important | 7.5 | 6.5 |
| Microsoft Exchange Server Spoofing Vulnerability | | | | | | | |
| [CVE-2026-45500](/vuln.html?cve=2026-45500) | No | No | - | - | Important | 6.1 | 5.3 |
| [CVE-2026-45501](/vuln.html?cve=2026-45501) | No | No | - | - | Important | 6.5 | 5.7 |
| [CVE-2026-47631](/vuln.html?cve=...