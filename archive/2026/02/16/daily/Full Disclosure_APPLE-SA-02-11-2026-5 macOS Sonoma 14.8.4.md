---
title: APPLE-SA-02-11-2026-5 macOS Sonoma 14.8.4
url: https://seclists.org/fulldisclosure/2026/Feb/25
source: Full Disclosure
date: 2026-02-16
fetch_date: 2026-02-17T04:21:56.039166
---

# APPLE-SA-02-11-2026-5 macOS Sonoma 14.8.4

[![](/shared/images/nst-icons.svg#menu)](#menu)
![](/shared/images/nst-icons.svg#close)
[![Home page logo](/images/sitelogo.png)](/)

[Nmap.org](https://nmap.org/)
[Npcap.com](https://npcap.com/)
[Seclists.org](https://seclists.org/)
[Sectools.org](https://sectools.org)
[Insecure.org](https://insecure.org/)

![](/shared/images/nst-icons.svg#search)

[![fulldisclosure logo](/images/fulldisclosure-logo.png)](/fulldisclosure/)

## [Full Disclosure](/fulldisclosure/) mailing list archives

[![Previous](/images/left-icon-16x16.png)](24)
[By Date](date.html#25)
[![Next](/images/right-icon-16x16.png)](26)

[![Previous](/images/left-icon-16x16.png)](24)
[By Thread](index.html#25)
[![Next](/images/right-icon-16x16.png)](26)

![](/shared/images/nst-icons.svg#search)

# APPLE-SA-02-11-2026-5 macOS Sonoma 14.8.4

---

*From*: Apple Product Security via Fulldisclosure <fulldisclosure () seclists org>
*Date*: Wed, 11 Feb 2026 16:04:38 -0800

---

```
-----BEGIN PGP SIGNED MESSAGE-----
Hash: SHA256

APPLE-SA-02-11-2026-5 macOS Sonoma 14.8.4

macOS Sonoma 14.8.4 addresses the following issues.
Information about the security content is also available at
https://support.apple.com/126350.

Apple maintains a Security Releases page at
https://support.apple.com/100100 which lists recent
software updates with security advisories.

AppleMobileFileIntegrity
Available for: macOS Sonoma
Impact: An app may be able to access sensitive user data
Description: An injection issue was addressed with improved validation.
CVE-2026-20624: Mickey Jin (@patch1t)

AppleMobileFileIntegrity
Available for: macOS Sonoma
Impact: An app may be able to access sensitive user data
Description: A parsing issue in the handling of directory paths was
addressed with improved path validation.
CVE-2026-20625: Mickey Jin (@patch1t), Ryan Dowd (@_rdowd)

CFNetwork
Available for: macOS Sonoma
Impact: A remote user may be able to write arbitrary files
Description: A path handling issue was addressed with improved logic.
CVE-2026-20660: Amy (amys.website)

Compression
Available for: macOS Sonoma
Impact: An app may be able to access sensitive user data
Description: An authorization issue was addressed with improved state
management.
CVE-2025-43403: Mickey Jin (@patch1t)

CoreAudio
Available for: macOS Sonoma
Impact: Processing a maliciously crafted media file may lead to
unexpected app termination or corrupt process memory
Description: An out-of-bounds access issue was addressed with improved
bounds checking.
CVE-2026-20611: Anonymous working with Trend Micro Zero Day Initiative

CoreMedia
Available for: macOS Sonoma
Impact: Processing a maliciously crafted file may lead to a denial-of-
service or potentially disclose memory contents
Description: The issue was addressed with improved memory handling.
CVE-2026-20609: Yiğit Can YILMAZ (@yilmazcanyigit)

CoreServices
Available for: macOS Sonoma
Impact: An app may be able to gain root privileges
Description: A race condition was addressed with improved state
handling.
CVE-2026-20617: Gergely Kalman (@gergely_kalman), Csaba Fitzl
(@theevilbit) of Iru

CoreServices
Available for: macOS Sonoma
Impact: An app may be able to gain root privileges
Description: A path handling issue was addressed with improved
validation.
CVE-2026-20615: Csaba Fitzl (@theevilbit) of Iru and Gergely Kalman
(@gergely_kalman)

CoreServices
Available for: macOS Sonoma
Impact: An app may be able to access sensitive user data
Description: A logic issue was addressed with improved validation.
CVE-2025-46283: an anonymous researcher

CoreServices
Available for: macOS Sonoma
Impact: An app may be able to access sensitive user data
Description: An issue existed in the handling of environment variables.
This issue was addressed with improved validation.
CVE-2026-20627: an anonymous researcher

File Bookmark
Available for: macOS Sonoma
Impact: An app may be able to access user-sensitive data
Description: A path handling issue was addressed with improved logic.
CVE-2025-43417: Ron Elemans

GPU Drivers
Available for: macOS Sonoma
Impact: An attacker may be able to cause unexpected system termination
or read kernel memory
Description: An out-of-bounds read issue was addressed with improved
input validation.
CVE-2026-20620: Murray Mike

ImageIO
Available for: macOS Sonoma
Impact: Processing a maliciously crafted media file may lead to
unexpected app termination or corrupt process memory
Description: An out-of-bounds access issue was addressed with improved
bounds checking.
CVE-2025-43338: 이동하 (Lee Dong Ha) of SSA Lab

ImageIO
Available for: macOS Sonoma
Impact: Processing a maliciously crafted image may result in disclosure
of process memory
Description: The issue was addressed with improved memory handling.
CVE-2026-20634: George Karchemsky (@gkarchemsky) working with Trend
Micro Zero Day Initiative

ImageIO
Available for: macOS Sonoma
Impact: Processing a maliciously crafted image may lead to disclosure of
user information
Description: The issue was addressed with improved bounds checks.
CVE-2026-20675: George Karchemsky (@gkarchemsky) working with Trend
Micro Zero Day Initiative

Kernel
Available for: macOS Sonoma
Impact: An attacker in a privileged network position may be able to
intercept network traffic
Description: A logic issue was addressed with improved checks.
CVE-2026-20671: Xin'an Zhou, Juefei Pu, Zhutian Liu, Zhiyun Qian,
Zhaowei Tan, Srikanth V. Krishnamurthy, Mathy Vanhoef

libexpat
Available for: macOS Sonoma
Impact: Processing a maliciously crafted file may lead to a denial-of-
service
Description: This is a vulnerability in open source code and Apple
Software is among the affected projects. The CVE-ID was assigned by a
third party. Learn more about the issue and CVE-ID at cve.org.
CVE-2025-59375

libnetcore
Available for: macOS Sonoma
Impact: An attacker in a privileged network position may be able to
intercept network traffic
Description: A logic issue was addressed with improved checks.
CVE-2026-20671: Xin'an Zhou, Juefei Pu, Zhutian Liu, Zhiyun Qian,
Zhaowei Tan, Srikanth V. Krishnamurthy, Mathy Vanhoef

libxpc
Available for: macOS Sonoma
Impact: An app may be able to break out of its sandbox
Description: A logic issue was addressed with improved checks.
CVE-2026-20667: an anonymous researcher

Mail
Available for: macOS Sonoma
Impact: Turning off "Load remote content in messages” may not apply to
all mail previews
Description: A logic issue was addressed with improved checks.
CVE-2026-20673: an anonymous researcher

Messages
Available for: macOS Sonoma
Impact: A shortcut may be able to bypass sandbox restrictions
Description: A race condition was addressed with improved handling of
symbolic links.
CVE-2026-20677: Ron Masas of BreakPoint.SH

Model I/O
Available for: macOS Sonoma
Impact: Processing a maliciously crafted USD file may lead to unexpected
app termination
Description: An out-of-bounds write issue was addressed with improved
bounds checking.
CVE-2026-20616: Michael DePlante (@izobashi) of Trend Micro Zero Day
Initiative

Multi-Touch
Available for: macOS Sonoma
Impact: A malicious HID device may cause an unexpected process crash
Description: The issue was addressed with improved bounds checks.
CVE-2025-43533: Google Threat Analysis Group
CVE-2025-46300: Google Threat Analysis Group
CVE-2025-46301: Google Threat Analysis Group
CVE-2025-46302: Google Threat Analysis Group
CVE-2025-46303: Google Threat Analysis Group
CVE-2025-46304: Google Threat Analysis Group
CVE-2025-46305: Google Threat Analysis Group

PackageKit
Available for: macOS Sonoma
Impact: An attacker with root privileges may be able to delete protected
system files
Description: This issue was addressed through improved state management.
CVE-2025-46310: Mickey Jin (@patch1t)

Remote Management
Available for: macOS Sonoma
Impact: An app may be able to gain root privileges
Description: A path handling issue was addressed with improved
validation.
CVE-2026-20614: Gergely Kalman (@gergely_kalman)

Sandbox
Available f...