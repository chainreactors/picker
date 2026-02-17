---
title: APPLE-SA-02-11-2026-3 macOS Tahoe 26.3
url: https://seclists.org/fulldisclosure/2026/Feb/23
source: Full Disclosure
date: 2026-02-16
fetch_date: 2026-02-17T04:21:56.366095
---

# APPLE-SA-02-11-2026-3 macOS Tahoe 26.3

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

[![Previous](/images/left-icon-16x16.png)](22)
[By Date](date.html#23)
[![Next](/images/right-icon-16x16.png)](24)

[![Previous](/images/left-icon-16x16.png)](22)
[By Thread](index.html#23)
[![Next](/images/right-icon-16x16.png)](24)

![](/shared/images/nst-icons.svg#search)

# APPLE-SA-02-11-2026-3 macOS Tahoe 26.3

---

*From*: Apple Product Security via Fulldisclosure <fulldisclosure () seclists org>
*Date*: Wed, 11 Feb 2026 16:03:50 -0800

---

```
-----BEGIN PGP SIGNED MESSAGE-----
Hash: SHA256

APPLE-SA-02-11-2026-3 macOS Tahoe 26.3

macOS Tahoe 26.3 addresses the following issues.
Information about the security content is also available at
https://support.apple.com/126348.

Apple maintains a Security Releases page at
https://support.apple.com/100100 which lists recent
software updates with security advisories.

Admin Framework
Available for: macOS Tahoe
Impact: An app may be able to access sensitive user data
Description: A parsing issue in the handling of directory paths was
addressed with improved path validation.
CVE-2026-20669: Mickey Jin (@patch1t)

AppleMobileFileIntegrity
Available for: macOS Tahoe
Impact: An app may be able to access sensitive user data
Description: A parsing issue in the handling of directory paths was
addressed with improved path validation.
CVE-2026-20625: Mickey Jin (@patch1t), Ryan Dowd (@_rdowd)

AppleMobileFileIntegrity
Available for: macOS Tahoe
Impact: An app may be able to access sensitive user data
Description: An injection issue was addressed with improved validation.
CVE-2026-20624: Mickey Jin (@patch1t)

Bluetooth
Available for: macOS Tahoe
Impact: An attacker in a privileged network position may be able to
perform denial-of-service attack using crafted Bluetooth packets
Description: A denial-of-service issue was addressed with improved
validation.
CVE-2026-20650: jioundai

CFNetwork
Available for: macOS Tahoe
Impact: A remote user may be able to write arbitrary files
Description: A path handling issue was addressed with improved logic.
CVE-2026-20660: Amy (amys.website)

Contacts
Available for: macOS Tahoe
Impact: An app may be able to access information about a user's contacts
Description: A privacy issue was addressed with improved private data
redaction for log entries.
CVE-2026-20681: Kirin (@Pwnrin) and LFY (@secsys) from Fudan University

CoreAudio
Available for: macOS Tahoe
Impact: Processing a maliciously crafted media file may lead to
unexpected app termination or corrupt process memory
Description: An out-of-bounds access issue was addressed with improved
bounds checking.
CVE-2026-20611: Anonymous working with Trend Micro Zero Day Initiative

CoreMedia
Available for: macOS Tahoe
Impact: Processing a maliciously crafted file may lead to a denial-of-
service or potentially disclose memory contents
Description: The issue was addressed with improved memory handling.
CVE-2026-20609: Yiğit Can YILMAZ (@yilmazcanyigit)

CoreServices
Available for: macOS Tahoe
Impact: An app may be able to gain root privileges
Description: A race condition was addressed with improved state
handling.
CVE-2026-20617: Gergely Kalman (@gergely_kalman), Csaba Fitzl
(@theevilbit) of Iru

CoreServices
Available for: macOS Tahoe
Impact: An app may be able to gain root privileges
Description: A path handling issue was addressed with improved
validation.
CVE-2026-20615: Csaba Fitzl (@theevilbit) of Iru and Gergely Kalman
(@gergely_kalman)

CoreServices
Available for: macOS Tahoe
Impact: An app may be able to access sensitive user data
Description: An issue existed in the handling of environment variables.
This issue was addressed with improved validation.
CVE-2026-20627: an anonymous researcher

dyld
Available for: macOS Tahoe
Impact: An attacker with memory write capability may be able to execute
arbitrary code. Apple is aware of a report that this issue may have been
exploited in an extremely sophisticated attack against specific targeted
individuals on versions of iOS before iOS 26. CVE-2025-14174 and
CVE-2025-43529 were also issued in response to this report.
Description: A memory corruption issue was addressed with improved state
management.
CVE-2026-20700: Google Threat Analysis Group

Foundation
Available for: macOS Tahoe
Impact: An app may be able to access user-sensitive data
Description: A privacy issue was addressed with improved handling of
temporary files.
CVE-2026-20629: Asaf Cohen

Foundation
Available for: macOS Tahoe
Impact: An app may be able to monitor keystrokes without user permission
Description: A permissions issue was addressed with additional
restrictions.
CVE-2026-20601: an anonymous researcher

Foundation
Available for: macOS Tahoe
Impact: An app may be able to access protected user data
Description: A permissions issue was addressed by removing the
vulnerable code.
CVE-2026-20623: an anonymous researcher

Game Center
Available for: macOS Tahoe
Impact: A user may be able to view sensitive user information
Description: A logging issue was addressed with improved data redaction.
CVE-2026-20649: Asaf Cohen

GPU Drivers
Available for: macOS Tahoe
Impact: An attacker may be able to cause unexpected system termination
or read kernel memory
Description: An out-of-bounds read issue was addressed with improved
input validation.
CVE-2026-20620: Murray Mike

ImageIO
Available for: macOS Tahoe
Impact: Processing a maliciously crafted image may lead to disclosure of
user information
Description: The issue was addressed with improved bounds checks.
CVE-2026-20675: George Karchemsky (@gkarchemsky) working with Trend
Micro Zero Day Initiative

ImageIO
Available for: macOS Tahoe
Impact: Processing a maliciously crafted image may result in disclosure
of process memory
Description: The issue was addressed with improved memory handling.
CVE-2026-20634: George Karchemsky (@gkarchemsky) working with Trend
Micro Zero Day Initiative

Kernel
Available for: macOS Tahoe
Impact: An app may be able to cause unexpected system termination
Description: The issue was addressed with improved memory handling.
CVE-2026-20654: Jian Lee (@speedyfriend433)

Kernel
Available for: macOS Tahoe
Impact: A malicious app may be able to gain root privileges
Description: This issue was addressed with improved checks.
CVE-2026-20626: Keisuke Hosoda

Kernel
Available for: macOS Tahoe
Impact: An attacker in a privileged network position may be able to
intercept network traffic
Description: A logic issue was addressed with improved checks.
CVE-2026-20671: Xin'an Zhou, Juefei Pu, Zhutian Liu, Zhiyun Qian,
Zhaowei Tan, Srikanth V. Krishnamurthy, Mathy Vanhoef

LaunchServices
Available for: macOS Tahoe
Impact: An app may be able to access protected user data
Description: A permissions issue was addressed with additional
restrictions.
CVE-2026-20630: an anonymous researcher

libexpat
Available for: macOS Tahoe
Impact: Processing a maliciously crafted file may lead to a denial-of-
service
Description: This is a vulnerability in open source code and Apple
Software is among the affected projects. The CVE-ID was assigned by a
third party. Learn more about the issue and CVE-ID at cve.org.
CVE-2025-59375

libxpc
Available for: macOS Tahoe
Impact: An app may be able to break out of its sandbox
Description: A logic issue was addressed with improved checks.
CVE-2026-20667: an anonymous researcher

Mail
Available for: macOS Tahoe
Impact: Turning off "Load remote content in messages” may not apply to
all mail previews
Description: A logic issue was addressed with improved checks.
CVE-...