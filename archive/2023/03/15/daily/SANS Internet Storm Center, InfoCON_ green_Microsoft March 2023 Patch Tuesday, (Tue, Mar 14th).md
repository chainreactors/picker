---
title: Microsoft March 2023 Patch Tuesday, (Tue, Mar 14th)
url: https://isc.sans.edu/diary/rss/29634
source: SANS Internet Storm Center, InfoCON: green
date: 2023-03-15
fetch_date: 2025-10-04T09:39:14.866908
---

# Microsoft March 2023 Patch Tuesday, (Tue, Mar 14th)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Johannes Ullrich](/handler_list.html#johannes-ullrich "Johannes Ullrich")

Threat Level: [green](/infocon.html)

* [previous](/diary/29630)
* [next](/diary/29638)

# [Microsoft March 2023 Patch Tuesday](/forums/diary/Microsoft%2BMarch%2B2023%2BPatch%2BTuesday/29634/)

**Published**: 2023-03-14. **Last Updated**: 2023-03-14 19:43:59 UTC
**by** [Renato Marinho](/handler_list.html#renato-marinho) (Version: 1)

[5 comment(s)](/diary/Microsoft%2BMarch%2B2023%2BPatch%2BTuesday/29634/#comments)

This month we got patches for 76 vulnerabilities. Of these, 9 are critical and 2 are already being exploited, according to Microsoft.

One of the exploited vulnerabilities is an elevation of privilege affecting Microsoft Outlook ([CVE-2023-23397](https://msrc.microsoft.com/update-guide/en-US/vulnerability/CVE-2023-23397)). According to the advisory, an attacker who successfully exploited this vulnerability could access a user's Net-NTLMv2 hash which could be used as a basis of an NTLM Relay attack against another service to authenticate as the user. The attacker could exploit this vulnerability by sending a specially crafted email that triggers automatically when it is retrieved and processed by the Outlook client. This could lead to exploitation BEFORE the email is viewed in the Preview Pane. The CVSS for this vulnerability is 9.8.

The second exploit vulnerability is a security feature bypass affecting Windows SmartScreen ([CVE-2023-24880](https://msrc.microsoft.com/update-guide/en-US/vulnerability/CVE-2023-24880)). According to the advisory, an attacker can craft a malicious file that would evade Mark of the Web (MOTW) defenses, resulting in a limited loss of integrity and availability of security features such as Protected View in Microsoft Office, which rely on MOTW tagging. The CVSS for this vulnerability is 5.4.

There is another critical vulnerability worth mentioning which is Remote Code Execution (RCE) affecting HTTP Protocol Stack ([CVE-2023-23392](https://msrc.microsoft.com/update-guide/en-US/vulnerability/CVE-2023-23392)). A prerequisite for a server to be vulnerable is that the binding has HTTP/3 enabled and the server uses buffered I/O. HTTP/3 support for services is a new feature of Windows Server 2022. This vulnerability requires no user interaction, no privileges, and the attack complexity is low. The CVSS for this vulnerability is 9.8.

See my dashboard for a more detailed breakout: https://patchtuesdaydashboard.com/

March 2023 Security Updates

| Description | | | | | | | |
| --- | --- | --- | --- | --- | --- | --- | --- |
| CVE | Disclosed | Exploited | Exploitability (old versions) | current version | Severity | CVSS Base (AVG) | CVSS Temporal (AVG) |
| Azure Apache AmbariSpoofing Vulnerability | | | | | | | |
| [CVE-2023-23408](/vuln.html?cve=2023-23408) | No | No | - | - | Important | 4.5 | 3.9 |
| CERT/CC: CVE-2023-1017 TPM2.0 Module Library Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2023-1017](/vuln.html?cve=2023-1017) | No | No | - | - | Critical | 8.8 | 7.7 |
| CERT/CC: CVE-2023-1018 TPM2.0 Module Library Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2023-1018](/vuln.html?cve=2023-1018) | No | No | - | - | Critical | 8.8 | 7.7 |
| Chromium: CVE-2023-1213 Use after free in Swiftshader | | | | | | | |
| [CVE-2023-1213](/vuln.html?cve=2023-1213) | No | No | - | - | - |  |  |
| Chromium: CVE-2023-1214 Type Confusion in V8 | | | | | | | |
| [CVE-2023-1214](/vuln.html?cve=2023-1214) | No | No | - | - | - |  |  |
| Chromium: CVE-2023-1215 Type Confusion in CSS | | | | | | | |
| [CVE-2023-1215](/vuln.html?cve=2023-1215) | No | No | - | - | - |  |  |
| Chromium: CVE-2023-1216 Use after free in DevTools | | | | | | | |
| [CVE-2023-1216](/vuln.html?cve=2023-1216) | No | No | - | - | - |  |  |
| Chromium: CVE-2023-1217 Stack buffer overflow in Crash reporting | | | | | | | |
| [CVE-2023-1217](/vuln.html?cve=2023-1217) | No | No | - | - | - |  |  |
| Chromium: CVE-2023-1218 Use after free in WebRTC | | | | | | | |
| [CVE-2023-1218](/vuln.html?cve=2023-1218) | No | No | - | - | - |  |  |
| Chromium: CVE-2023-1219 Heap buffer overflow in Metrics | | | | | | | |
| [CVE-2023-1219](/vuln.html?cve=2023-1219) | No | No | - | - | - |  |  |
| Chromium: CVE-2023-1220 Heap buffer overflow in UMA | | | | | | | |
| [CVE-2023-1220](/vuln.html?cve=2023-1220) | No | No | - | - | - |  |  |
| Chromium: CVE-2023-1221 Insufficient policy enforcement in Extensions API | | | | | | | |
| [CVE-2023-1221](/vuln.html?cve=2023-1221) | No | No | - | - | - |  |  |
| Chromium: CVE-2023-1222 Heap buffer overflow in Web Audio API | | | | | | | |
| [CVE-2023-1222](/vuln.html?cve=2023-1222) | No | No | - | - | - |  |  |
| Chromium: CVE-2023-1223 Insufficient policy enforcement in Autofill | | | | | | | |
| [CVE-2023-1223](/vuln.html?cve=2023-1223) | No | No | - | - | - |  |  |
| Chromium: CVE-2023-1224 Insufficient policy enforcement in Web Payments API | | | | | | | |
| [CVE-2023-1224](/vuln.html?cve=2023-1224) | No | No | - | - | - |  |  |
| Chromium: CVE-2023-1228 Insufficient policy enforcement in Intents | | | | | | | |
| [CVE-2023-1228](/vuln.html?cve=2023-1228) | No | No | - | - | - |  |  |
| Chromium: CVE-2023-1229 Inappropriate implementation in Permission prompts | | | | | | | |
| [CVE-2023-1229](/vuln.html?cve=2023-1229) | No | No | - | - | - |  |  |
| Chromium: CVE-2023-1230 Inappropriate implementation in WebApp Installs | | | | | | | |
| [CVE-2023-1230](/vuln.html?cve=2023-1230) | No | No | - | - | - |  |  |
| Chromium: CVE-2023-1231 Inappropriate implementation in Autofill | | | | | | | |
| [CVE-2023-1231](/vuln.html?cve=2023-1231) | No | No | - | - | - |  |  |
| Chromium: CVE-2023-1232 Insufficient policy enforcement in Resource Timing | | | | | | | |
| [CVE-2023-1232](/vuln.html?cve=2023-1232) | No | No | - | - | - |  |  |
| Chromium: CVE-2023-1233 Insufficient policy enforcement in Resource Timing | | | | | | | |
| [CVE-2023-1233](/vuln.html?cve=2023-1233) | No | No | - | - | - |  |  |
| Chromium: CVE-2023-1234 Inappropriate implementation in Intents | | | | | | | |
| [CVE-2023-1234](/vuln.html?cve=2023-1234) | No | No | - | - | - |  |  |
| Chromium: CVE-2023-1235 Type Confusion in DevTools | | | | | | | |
| [CVE-2023-1235](/vuln.html?cve=2023-1235) | No | No | - | - | - |  |  |
| Chromium: CVE-2023-1236 Inappropriate implementation in Internals | | | | | | | |
| [CVE-2023-1236](/vuln.html?cve=2023-1236) | No | No | - | - | - |  |  |
| Client Server Run-Time Subsystem (CSRSS) Information Disclosure Vulnerability | | | | | | | |
| [CVE-2023-23394](/vuln.html?cve=2023-23394) | No | No | - | - | Important | 5.5 | 4.8 |
| [CVE-2023-23409](/vuln.html?cve=2023-23409) | No | No | - | - | Important | 5.5 | 4.8 |
| GitHub: CVE-2023-22490 mingit Information Disclosure Vulnerability | | | | | | | |
| [CVE-2023-22490](/vuln.html?cve=2023-22490) | No | No | - | - | Important |  |  |
| GitHub: CVE-2023-22743 Git for Windows Installer Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2023-22743](/vuln.html?cve=2023-22743) | No | No | - | - | Important |  |  |
| GitHub: CVE-2023-23618 Git for Windows Remote Code Execution Vulnerability | | | | | | | |
| [CVE-2023-23618](/vuln.html?cve=2023-23618) | No | No | - | - | Important |  |  |
| GitHub: CVE-2023-23946 mingit Remote Code Execution Vulnerability | | | | | | | |
| [CVE-2023-23946](/vuln.html?cve=2023-23946) | No | No | - | - | Important |  |  |
| HTTP Protocol Stack Remote Code Execution Vulnerability | | | | | | | |
| [CVE-2023-23392](/vuln.html?cve=2023-23392) | No | No | - | - | Critical | 9.8 | 8.5 |
| Internet Control Message Protocol (ICMP) Remote Code Execution Vulnerability | | | | | | | |
| [CVE-2023-23415](/vuln.html?cve=2023-23415) | No | No | - | - | Critical | 9.8 | 8.5 |
| Microsoft Defender Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2023-23389](/vuln.html?cv...