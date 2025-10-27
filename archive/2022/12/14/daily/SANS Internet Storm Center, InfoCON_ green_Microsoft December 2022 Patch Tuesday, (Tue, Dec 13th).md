---
title: Microsoft December 2022 Patch Tuesday, (Tue, Dec 13th)
url: https://isc.sans.edu/diary/rss/29336
source: SANS Internet Storm Center, InfoCON: green
date: 2022-12-14
fetch_date: 2025-10-04T01:27:39.638688
---

# Microsoft December 2022 Patch Tuesday, (Tue, Dec 13th)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Johannes Ullrich](/handler_list.html#johannes-ullrich "Johannes Ullrich")

Threat Level: [green](/infocon.html)

* [previous](/diary/29328)
* [next](/diary/29338)

# [Microsoft December 2022 Patch Tuesday](/forums/diary/Microsoft%2BDecember%2B2022%2BPatch%2BTuesday/29336/)

**Published**: 2022-12-13. **Last Updated**: 2022-12-13 18:31:55 UTC
**by** [Renato Marinho](/handler_list.html#renato-marinho) (Version: 1)

[0 comment(s)](/diary/Microsoft%2BDecember%2B2022%2BPatch%2BTuesday/29336/#comments)

In the last Patch Tuesday of 2022, we got patches for 74 vulnerabilities. Of these, 7 are critical, 1 was previously disclosed, and 1 is already being exploited, according to Microsoft.

The exploited vulnerability is a Windows SmartScreen Security Feature Bypass Vulnerability ([CVE-2022-44698](https://msrc.microsoft.com/update-guide/en-US/vulnerability/CVE-2022-44698)). When you download a file from the internet, Windows adds the zone identifier or Mark of the Web as an NTFS stream to the file. So, when you run the file, Windows SmartScreen checks if there is a zone identifier Alternate Data Stream (ADS) attached to the file. If the ADS indicates ZoneId=3 which means that the file was downloaded from the internet, the SmartScreen does a reputation check. Exploiting this vulnerability, an attacker can craft a malicious file that would evade Mark of the Web (MOTW) defenses. The CVSS for this vulnerability is 5.4.

Amongst critical vulnerabilities, there is a Remote Code Execution (RCE) affecting the .Net Framework ([CVE-2022-41089](https://msrc.microsoft.com/update-guide/en-US/vulnerability/CVE-2022-41089)). The exploitability for this one is ‘less likely’ according to Microsoft. The CVSS is 8.8.

A second critical vulnerability is an RCE affecting Microsoft SharePoint Server ([CVE-2022-44690](https://msrc.microsoft.com/update-guide/en-US/vulnerability/CVE-2022-44690)). According to the advisory, in a network-based attack, an authenticated attacker with Manage List permissions could execute code remotely on the SharePoint Server. The CVSS for this vulnerability is 8.8.

Another critical vulnerability worth mentioning is an RCE in Powershell ([CVE-2022-41076](https://msrc.microsoft.com/update-guide/en-US/vulnerability/CVE-2022-41076)). The advisory says that the attack complexity is high as to exploit this vulnerability requires an attacker to take additional actions prior to exploitation to prepare the target environment. Additionally, it says that an authenticated attacker could escape the PowerShell Remoting Session Configuration and run unapproved commands on the target system. The CVSS for this vulnerability is 8.5.

See my dashboard for a more detailed breakout: https://patchtuesdaydashboard.com/

December 2022 Security Updates

| Description | | | | | | | |
| --- | --- | --- | --- | --- | --- | --- | --- |
| CVE | Disclosed | Exploited | Exploitability (old versions) | current version | Severity | CVSS Base (AVG) | CVSS Temporal (AVG) |
| .NET Framework Remote Code Execution Vulnerability | | | | | | | |
| [CVE-2022-41089](/vuln.html?cve=2022-41089) | No | No | Less Likely | Less Likely | Critical | 8.8 | 7.7 |
| Azure Network Watcher Agent Security Feature Bypass Vulnerability | | | | | | | |
| [CVE-2022-44699](/vuln.html?cve=2022-44699) | No | No | - | - | Important | 5.5 | 5.1 |
| Chromium: CVE-2022-4174 Type Confusion in V8 | | | | | | | |
| [CVE-2022-4174](/vuln.html?cve=2022-4174) | No | No | - | - | - |  |  |
| Chromium: CVE-2022-4175 Use after free in Camera Capture | | | | | | | |
| [CVE-2022-4175](/vuln.html?cve=2022-4175) | No | No | - | - | - |  |  |
| Chromium: CVE-2022-4177 Use after free in Extensions | | | | | | | |
| [CVE-2022-4177](/vuln.html?cve=2022-4177) | No | No | - | - | - |  |  |
| Chromium: CVE-2022-4178 Use after free in Mojo | | | | | | | |
| [CVE-2022-4178](/vuln.html?cve=2022-4178) | No | No | - | - | - |  |  |
| Chromium: CVE-2022-4179 Use after free in Audio | | | | | | | |
| [CVE-2022-4179](/vuln.html?cve=2022-4179) | No | No | - | - | - |  |  |
| Chromium: CVE-2022-4180 Use after free in Mojo | | | | | | | |
| [CVE-2022-4180](/vuln.html?cve=2022-4180) | No | No | - | - | - |  |  |
| Chromium: CVE-2022-4181 Use after free in Forms | | | | | | | |
| [CVE-2022-4181](/vuln.html?cve=2022-4181) | No | No | - | - | - |  |  |
| Chromium: CVE-2022-4182 Inappropriate implementation in Fenced Frames | | | | | | | |
| [CVE-2022-4182](/vuln.html?cve=2022-4182) | No | No | - | - | - |  |  |
| Chromium: CVE-2022-4183 Insufficient policy enforcement in Popup Blocker | | | | | | | |
| [CVE-2022-4183](/vuln.html?cve=2022-4183) | No | No | - | - | - |  |  |
| Chromium: CVE-2022-4184 Insufficient policy enforcement in Autofill | | | | | | | |
| [CVE-2022-4184](/vuln.html?cve=2022-4184) | No | No | - | - | - |  |  |
| Chromium: CVE-2022-4185 Inappropriate implementation in Navigation | | | | | | | |
| [CVE-2022-4185](/vuln.html?cve=2022-4185) | No | No | - | - | - |  |  |
| Chromium: CVE-2022-4186 Insufficient validation of untrusted input in Downloads | | | | | | | |
| [CVE-2022-4186](/vuln.html?cve=2022-4186) | No | No | - | - | - |  |  |
| Chromium: CVE-2022-4187 Insufficient policy enforcement in DevTools | | | | | | | |
| [CVE-2022-4187](/vuln.html?cve=2022-4187) | No | No | - | - | - |  |  |
| Chromium: CVE-2022-4188 Insufficient validation of untrusted input in CORS | | | | | | | |
| [CVE-2022-4188](/vuln.html?cve=2022-4188) | No | No | - | - | - |  |  |
| Chromium: CVE-2022-4189 Insufficient policy enforcement in DevTools | | | | | | | |
| [CVE-2022-4189](/vuln.html?cve=2022-4189) | No | No | - | - | - |  |  |
| Chromium: CVE-2022-4190 Insufficient data validation in Directory | | | | | | | |
| [CVE-2022-4190](/vuln.html?cve=2022-4190) | No | No | - | - | - |  |  |
| Chromium: CVE-2022-4191 Use after free in Sign-In | | | | | | | |
| [CVE-2022-4191](/vuln.html?cve=2022-4191) | No | No | - | - | - |  |  |
| Chromium: CVE-2022-4192 Use after free in Live Caption | | | | | | | |
| [CVE-2022-4192](/vuln.html?cve=2022-4192) | No | No | - | - | - |  |  |
| Chromium: CVE-2022-4193 Insufficient policy enforcement in File System API | | | | | | | |
| [CVE-2022-4193](/vuln.html?cve=2022-4193) | No | No | - | - | - |  |  |
| Chromium: CVE-2022-4194 Use after free in Accessibility | | | | | | | |
| [CVE-2022-4194](/vuln.html?cve=2022-4194) | No | No | - | - | - |  |  |
| Chromium: CVE-2022-4195 Insufficient policy enforcement in Safe Browsing | | | | | | | |
| [CVE-2022-4195](/vuln.html?cve=2022-4195) | No | No | - | - | - |  |  |
| DirectX Graphics Kernel Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2022-44710](/vuln.html?cve=2022-44710) | Yes | No | - | - | Important | 7.8 | 6.8 |
| Guidance on Microsoft Signed Drivers Being Used Maliciously | | | | | | | |
| [ADV220005](https://portal.msrc.microsoft.com/en-us/security-guidance/advisory/ADV220005) | No | No | - | - | None |  |  |
| Microsoft Dynamics NAV and Microsoft Dynamics 365 Business Central (On Premises) Remote Code Execution Vulnerability | | | | | | | |
| [CVE-2022-41127](/vuln.html?cve=2022-41127) | No | No | - | - | Critical | 8.5 | 7.4 |
| Microsoft Edge (Chromium-based) Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2022-44708](/vuln.html?cve=2022-44708) | No | No | Less Likely | Less Likely | Important | 8.3 | 7.2 |
| Microsoft Edge (Chromium-based) Spoofing Vulnerability | | | | | | | |
| [CVE-2022-44688](/vuln.html?cve=2022-44688) | No | No | Less Likely | Less Likely | Moderate | 4.3 | 3.8 |
| Microsoft Edge (Chromium-based) Update Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2022-41115](/vuln.html?cve=2022-41115) | No | No | - | - | Important | 6.6 | 5.8 |
| Microsoft Office Graphics Remote Code Execution Vulnerability | | | | | | | |
| [CVE-2022-44692](/vuln.html?cve=2022-44692) | No | No | Unlikely | Unlikely | Important | 7.8 | 6....