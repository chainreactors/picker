---
title: APPLE-SA-02-11-2026-8 visionOS 26.3
url: https://seclists.org/fulldisclosure/2026/Feb/28
source: Full Disclosure
date: 2026-02-16
fetch_date: 2026-02-17T04:21:55.533006
---

# APPLE-SA-02-11-2026-8 visionOS 26.3

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

[![Previous](/images/left-icon-16x16.png)](27)
[By Date](date.html#28)
[![Next](/images/right-icon-16x16.png)](29)

[![Previous](/images/left-icon-16x16.png)](27)
[By Thread](index.html#28)
[![Next](/images/right-icon-16x16.png)](29)

![](/shared/images/nst-icons.svg#search)

# APPLE-SA-02-11-2026-8 visionOS 26.3

---

*From*: Apple Product Security via Fulldisclosure <fulldisclosure () seclists org>
*Date*: Wed, 11 Feb 2026 16:06:22 -0800

---

```
-----BEGIN PGP SIGNED MESSAGE-----
Hash: SHA256

APPLE-SA-02-11-2026-8 visionOS 26.3

visionOS 26.3 addresses the following issues.
Information about the security content is also available at
https://support.apple.com/126353.

Apple maintains a Security Releases page at
https://support.apple.com/100100 which lists recent
software updates with security advisories.

AppleMobileFileIntegrity
Available for: Apple Vision Pro (all models)
Impact: An app may be able to access sensitive user data
Description: A parsing issue in the handling of directory paths was
addressed with improved path validation.
CVE-2026-20625: Mickey Jin (@patch1t), Ryan Dowd (@_rdowd)

Bluetooth
Available for: Apple Vision Pro (all models)
Impact: An attacker in a privileged network position may be able to
perform denial-of-service attack using crafted Bluetooth packets
Description: A denial-of-service issue was addressed with improved
validation.
CVE-2026-20650: jioundai

CFNetwork
Available for: Apple Vision Pro (all models)
Impact: A remote user may be able to write arbitrary files
Description: A path handling issue was addressed with improved logic.
CVE-2026-20660: Amy (amys.website)

CoreAudio
Available for: Apple Vision Pro (all models)
Impact: Processing a maliciously crafted media file may lead to
unexpected app termination or corrupt process memory
Description: An out-of-bounds access issue was addressed with improved
bounds checking.
CVE-2026-20611: Anonymous working with Trend Micro Zero Day Initiative

CoreMedia
Available for: Apple Vision Pro (all models)
Impact: Processing a maliciously crafted file may lead to a denial-of-
service or potentially disclose memory contents
Description: The issue was addressed with improved memory handling.
CVE-2026-20609: Yiğit Can YILMAZ (@yilmazcanyigit)

CoreServices
Available for: Apple Vision Pro (all models)
Impact: An app may be able to gain root privileges
Description: A race condition was addressed with improved state
handling.
CVE-2026-20617: Gergely Kalman (@gergely_kalman), Csaba Fitzl
(@theevilbit) of Iru

CoreServices
Available for: Apple Vision Pro (all models)
Impact: An app may be able to gain root privileges
Description: A path handling issue was addressed with improved
validation.
CVE-2026-20615: Csaba Fitzl (@theevilbit) of Iru and Gergely Kalman
(@gergely_kalman)

CoreServices
Available for: Apple Vision Pro (all models)
Impact: An app may be able to access sensitive user data
Description: An issue existed in the handling of environment variables.
This issue was addressed with improved validation.
CVE-2026-20627: an anonymous researcher

dyld
Available for: Apple Vision Pro (all models)
Impact: An attacker with memory write capability may be able to execute
arbitrary code. Apple is aware of a report that this issue may have been
exploited in an extremely sophisticated attack against specific targeted
individuals on versions of iOS before iOS 26. CVE-2025-14174 and
CVE-2025-43529 were also issued in response to this report.
Description: A memory corruption issue was addressed with improved state
management.
CVE-2026-20700: Google Threat Analysis Group

ImageIO
Available for: Apple Vision Pro (all models)
Impact: Processing a maliciously crafted image may lead to disclosure of
user information
Description: The issue was addressed with improved bounds checks.
CVE-2026-20675: George Karchemsky (@gkarchemsky) working with Trend
Micro Zero Day Initiative

ImageIO
Available for: Apple Vision Pro (all models)
Impact: Processing a maliciously crafted image may result in disclosure
of process memory
Description: The issue was addressed with improved memory handling.
CVE-2026-20634: George Karchemsky (@gkarchemsky) working with Trend
Micro Zero Day Initiative

Kernel
Available for: Apple Vision Pro (all models)
Impact: An app may be able to cause unexpected system termination
Description: The issue was addressed with improved memory handling.
CVE-2026-20654: Jian Lee (@speedyfriend433)

Kernel
Available for: Apple Vision Pro (all models)
Impact: A malicious app may be able to gain root privileges
Description: This issue was addressed with improved checks.
CVE-2026-20626: Keisuke Hosoda

Kernel
Available for: Apple Vision Pro (all models)
Impact: An attacker in a privileged network position may be able to
intercept network traffic
Description: A logic issue was addressed with improved checks.
CVE-2026-20671: Xin'an Zhou, Juefei Pu, Zhutian Liu, Zhiyun Qian,
Zhaowei Tan, Srikanth V. Krishnamurthy, Mathy Vanhoef

libexpat
Available for: Apple Vision Pro (all models)
Impact: Processing a maliciously crafted file may lead to a denial-of-
service
Description: This is a vulnerability in open source code and Apple
Software is among the affected projects. The CVE-ID was assigned by a
third party. Learn more about the issue and CVE-ID at cve.org.
CVE-2025-59375

Messages
Available for: Apple Vision Pro (all models)
Impact: A shortcut may be able to bypass sandbox restrictions
Description: A race condition was addressed with improved handling of
symbolic links.
CVE-2026-20677: Ron Masas of BreakPoint.SH

Model I/O
Available for: Apple Vision Pro (all models)
Impact: Processing a maliciously crafted USD file may lead to unexpected
app termination
Description: An out-of-bounds write issue was addressed with improved
bounds checking.
CVE-2026-20616: Michael DePlante (@izobashi) of Trend Micro Zero Day
Initiative

Sandbox
Available for: Apple Vision Pro (all models)
Impact: An app may be able to break out of its sandbox
Description: A permissions issue was addressed with additional
restrictions.
CVE-2026-20628: Noah Gregory (wts.dev)

Shortcuts
Available for: Apple Vision Pro (all models)
Impact: An app may be able to access sensitive user data
Description: A parsing issue in the handling of directory paths was
addressed with improved path validation.
CVE-2026-20653: Enis Maholli (enismaholli.com)

StoreKit
Available for: Apple Vision Pro (all models)
Impact: An app may be able to identify what other apps a user has
installed
Description: A privacy issue was addressed with improved checks.
CVE-2026-20641: Gongyu Ma (@Mezone0)

WebKit
Available for: Apple Vision Pro (all models)
Impact: A remote attacker may be able to cause a denial-of-service
Description: The issue was addressed with improved memory handling.
WebKit Bugzilla: 303959
CVE-2026-20652: Nathaniel Oh (@calysteon)

WebKit
Available for: Apple Vision Pro (all models)
Impact: Processing maliciously crafted web content may lead to an
unexpected process crash
Description: This issue was addressed through improved state management.
WebKit Bugzilla: 303357
CVE-2026-20608: HanQing from TSDubhe and Nan Wang (@eternalsakura13)

WebKit
Available for: Apple Vision Pro (all models)
Impact: A website may be able to track users through Safari web
extensions
Description: This issue was addressed through improved state management.
WebKit Bugzilla: 305020
CVE-2026-20676: Tom Van Goethem

WebKit
Available for: Apple Vision Pro (all models)
Impact: Processing maliciously...