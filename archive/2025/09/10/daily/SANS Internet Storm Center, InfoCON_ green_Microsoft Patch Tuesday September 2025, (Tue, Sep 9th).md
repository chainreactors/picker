---
title: Microsoft Patch Tuesday September 2025, (Tue, Sep 9th)
url: https://isc.sans.edu/diary/rss/32270
source: SANS Internet Storm Center, InfoCON: green
date: 2025-09-10
fetch_date: 2025-10-02T19:55:49.431882
---

# Microsoft Patch Tuesday September 2025, (Tue, Sep 9th)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Jesse La Grew](/handler_list.html#jesse-la-grew "Jesse La Grew")

Threat Level: [green](/infocon.html)

* [previous](/diary/32266)
* [next](/diary/32274)

My next class:

|  |  |  |
| --- | --- | --- |
| [Application Security: Securing Web Apps, APIs, and Microservices](https://www.sans.org/event/cloudsecnext-summit-2025/course/application-security-securing-web-apps-api-microservices) | Denver | Oct 4th - Oct 9th 2025 |

# [Microsoft Patch Tuesday September 2025](/forums/diary/Microsoft%2BPatch%2BTuesday%2BSeptember%2B2025/32270/)

**Published**: 2025-09-09. **Last Updated**: 2025-09-09 17:42:34 UTC
**by** [Johannes Ullrich](https://plus.google.com/101587262224166552564?rel=author) (Version: 1)

[0 comment(s)](/diary/Microsoft%2BPatch%2BTuesday%2BSeptember%2B2025/32270/#comments)

As part of its September patch Tuesday, Microsoft addressed 177 different vulnerabilities, 86 of which affect Microsoft products. None of the vulnerabilities has been exploited before today. Two of the vulnerabilities were already made public. Microsoft rates 13 of the vulnerabilities are critical.

You will see a number of vulnerabilities without assigned severity. These vulnerabilities affect Linux distributions like Mariner, Microsoft's Linux distribution used in its cloud environments, and Azure Linux.

Vulnerabilities of Interest:

**CVE-2025-54107, CVE-2025-54917**: Microsoft assigns URLs to different security zones, like "Intranet" and "Internet". URLs may be misclassified. An attacker could use this vulnerability to bypass security features that restrict more risky URLs.

**CVE-2025-55226, CVE-2025-55236**: The description for these vulnerabilities is a bit odd. Microsoft labels them as "remote code execution" vulnerabilities, but states that they allow an "authorized attacker to execute code locally." I suspect that the remote part refers to a user unknowingly executing the code by viewing an image. The CVSS score is still low for a "critical" vulnerability.

Overall, there is no "patch now" vulnerability included. Apply patches in line with your local vulnerability management policy (hopefully before next month's patch Tuesday).

| Description | | | | | | | |
| --- | --- | --- | --- | --- | --- | --- | --- |
| CVE | Disclosed | Exploited | Exploitability (old versions) | current version | Severity | CVSS Base (AVG) | CVSS Temporal (AVG) |
| ACPI: pfr\_update: Fix the driver update version check | | | | | | | |
| [CVE-2025-39701](/vuln.html?cve=2025-39701) | No | No | - | - | - |  |  |
| ALSA: usb-audio: Validate UAC3 power domain descriptors, too | | | | | | | |
| [CVE-2025-38729](/vuln.html?cve=2025-38729) | No | No | - | - | - | 7.0 | 7.0 |
| ASoC: core: Check for rtd == NULL in snd\_soc\_remove\_pcm\_runtime() | | | | | | | |
| [CVE-2025-38706](/vuln.html?cve=2025-38706) | No | No | - | - | - | 4.7 | 4.7 |
| Azure Arc Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2025-55316](/vuln.html?cve=2025-55316) | No | No | - | - | Important | 7.8 | 6.8 |
| Azure Bot Service Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2025-55244](/vuln.html?cve=2025-55244) | No | No | - | - | Critical | 9.0 | 7.8 |
| Azure Connected Machine Agent Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2025-49692](/vuln.html?cve=2025-49692) | No | No | - | - | Important | 7.8 | 6.8 |
| Azure Entra Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2025-55241](/vuln.html?cve=2025-55241) | No | No | - | - | Critical | 9.0 | 7.8 |
| Azure Networking Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2025-54914](/vuln.html?cve=2025-54914) | No | No | - | - | Critical | 10.0 | 8.7 |
| Capability Access Management Service (camsvc) Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2025-54108](/vuln.html?cve=2025-54108) | No | No | - | - | Important | 7.0 | 6.1 |
| DirectX Graphics Kernel Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2025-55223](/vuln.html?cve=2025-55223) | No | No | - | - | Important | 7.0 | 6.1 |
| Dynamics 365 FastTrack Implementation Assets Information Disclosure Vulnerability | | | | | | | |
| [CVE-2025-55238](/vuln.html?cve=2025-55238) | No | No | - | - | Critical | 7.5 | 6.5 |
| Glib: buffer under-read on glib through glib/gfileutils.c via get\_tmp\_file() | | | | | | | |
| [CVE-2025-7039](/vuln.html?cve=2025-7039) | No | No | - | - | - | 3.7 | 3.7 |
| Graphics Kernel Remote Code Execution Vulnerability | | | | | | | |
| [CVE-2025-55226](/vuln.html?cve=2025-55226) | No | No | - | - | Critical | 6.7 | 5.8 |
| [CVE-2025-55236](/vuln.html?cve=2025-55236) | No | No | - | - | Critical | 7.3 | 6.4 |
| HTTP.sys Denial of Service Vulnerability | | | | | | | |
| [CVE-2025-53805](/vuln.html?cve=2025-53805) | No | No | - | - | Important | 7.5 | 6.5 |
| Libsoup: improper handling of http vary header in libsoup caching | | | | | | | |
| [CVE-2025-9901](/vuln.html?cve=2025-9901) | No | No | - | - | - | 5.9 | 5.6 |
| Local Security Authority Subsystem Service (LSASS) Denial of Service Vulnerability | | | | | | | |
| [CVE-2025-53809](/vuln.html?cve=2025-53809) | No | No | - | - | Important | 6.5 | 5.7 |
| Local Security Authority Subsystem Service Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2025-54894](/vuln.html?cve=2025-54894) | No | No | - | - | Important | 7.8 | 6.8 |
| LoongArch: BPF: Fix jump offset calculation in tailcall | | | | | | | |
| [CVE-2025-38723](/vuln.html?cve=2025-38723) | No | No | - | - | - | 5.5 | 5.5 |
| MIPS: Don't crash in stack\_top() for tasks without ABI or vDSO | | | | | | | |
| [CVE-2025-38696](/vuln.html?cve=2025-38696) | No | No | - | - | - | 5.5 | 5.5 |
| MapUrlToZone Security Feature Bypass Vulnerability | | | | | | | |
| [CVE-2025-54107](/vuln.html?cve=2025-54107) | No | No | - | - | Important | 4.3 | 3.8 |
| [CVE-2025-54917](/vuln.html?cve=2025-54917) | No | No | - | - | Important | 4.3 | 3.8 |
| Microsoft AutoUpdate (MAU) Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2025-55317](/vuln.html?cve=2025-55317) | No | No | - | - | Important | 7.8 | 6.8 |
| Microsoft Brokering File System Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2025-54105](/vuln.html?cve=2025-54105) | No | No | - | - | Important | 7.0 | 6.1 |
| Microsoft DWM Core Library Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2025-53801](/vuln.html?cve=2025-53801) | No | No | - | - | Important | 7.8 | 6.8 |
| Microsoft Edge (Chromium-based) Security Feature Bypass Vulnerability | | | | | | | |
| [CVE-2025-53791](/vuln.html?cve=2025-53791) | No | No | - | - | Moderate | 4.7 | 4.1 |
| Microsoft Excel Information Disclosure Vulnerability | | | | | | | |
| [CVE-2025-54901](/vuln.html?cve=2025-54901) | No | No | - | - | Important | 5.5 | 4.8 |
| Microsoft Excel Remote Code Execution Vulnerability | | | | | | | |
| [CVE-2025-54896](/vuln.html?cve=2025-54896) | No | No | - | - | Important | 7.8 | 6.8 |
| [CVE-2025-54898](/vuln.html?cve=2025-54898) | No | No | - | - | Important | 7.8 | 6.8 |
| [CVE-2025-54899](/vuln.html?cve=2025-54899) | No | No | - | - | Important | 7.8 | 6.8 |
| [CVE-2025-54902](/vuln.html?cve=2025-54902) | No | No | - | - | Important | 7.8 | 6.8 |
| [CVE-2025-54903](/vuln.html?cve=2025-54903) | No | No | - | - | Important | 7.8 | 6.8 |
| [CVE-2025-54904](/vuln.html?cve=2025-54904) | No | No | - | - | Important | 7.8 | 6.8 |
| [CVE-2025-54900](/vuln.html?cve=2025-54900) | No | No | - | - | Important | 7.8 | 6.8 |
| Microsoft High Performance Compute (HPC) Pack Remote Code Execution Vulnerability | | | | | | | |
| [CVE-2025-55232](/vuln.html?cve=2025-55232) | No | No | - | - | Important | 9.8 | 8.5 |
| Microsoft Office Remote Code Execution Vulnerability | | | | | | | |
| [CVE-2025-54906](/vuln.html?cve=2025-54906) | No | No | - | - | Important | 7.8 | 6.8 |
| [CVE-2025-54910](/vuln.html?cve=2025-54910) | No | No | - | - | Critical | 8.4 | 7.3 |
| Microsoft...