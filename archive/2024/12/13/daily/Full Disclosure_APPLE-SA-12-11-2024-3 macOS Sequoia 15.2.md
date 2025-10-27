---
title: APPLE-SA-12-11-2024-3 macOS Sequoia 15.2
url: https://seclists.org/fulldisclosure/2024/Dec/7
source: Full Disclosure
date: 2024-12-13
fetch_date: 2025-10-06T19:41:02.911423
---

# APPLE-SA-12-11-2024-3 macOS Sequoia 15.2

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

[![Previous](/images/left-icon-16x16.png)](6)
[By Date](date.html#7)
[![Next](/images/right-icon-16x16.png)](8)

[![Previous](/images/left-icon-16x16.png)](6)
[By Thread](index.html#7)
[![Next](/images/right-icon-16x16.png)](8)

![](/shared/images/nst-icons.svg#search)

# APPLE-SA-12-11-2024-3 macOS Sequoia 15.2

---

*From*: Apple Product Security via Fulldisclosure <fulldisclosure () seclists org>
*Date*: Wed, 11 Dec 2024 16:36:26 -0700

---

```
-----BEGIN PGP SIGNED MESSAGE-----
Hash: SHA256

APPLE-SA-12-11-2024-3 macOS Sequoia 15.2

macOS Sequoia 15.2 addresses the following issues.
Information about the security content is also available at
https://support.apple.com/121839.

Apple maintains a Security Releases page at
https://support.apple.com/100100 which lists recent
software updates with security advisories.

Apple Software Restore
Available for: macOS Sequoia
Impact: An app may be able to access user-sensitive data
Description: The issue was addressed with improved checks.
CVE-2024-54477: Mickey Jin (@patch1t), Csaba Fitzl (@theevilbit) of
Kandji

AppleGraphicsControl
Available for: macOS Sequoia
Impact: Parsing a maliciously crafted video file may lead to unexpected
system termination
Description: The issue was addressed with improved memory handling.
CVE-2024-44220: D4m0n

AppleMobileFileIntegrity
Available for: macOS Sequoia
Impact: A malicious app may be able to access private information
Description: The issue was addressed with improved checks.
CVE-2024-54526: Mickey Jin (@patch1t), Arsenii Kostromin (0x3c3e)

AppleMobileFileIntegrity
Available for: macOS Sequoia
Impact: An app may be able to access sensitive user data
Description: This issue was addressed with improved checks.
CVE-2024-54527: Mickey Jin (@patch1t)

AppleMobileFileIntegrity
Available for: macOS Sequoia
Impact: A local attacker may gain access to user's Keychain items
Description: This issue was addressed by enabling hardened runtime.
CVE-2024-54490: Mickey Jin (@patch1t)

Audio
Available for: macOS Sequoia
Impact: An app may be able to execute arbitrary code with kernel
privileges
Description: A logic issue was addressed with improved checks.
CVE-2024-54529: Dillon Franke working with Google Project Zero

Crash Reporter
Available for: macOS Sequoia
Impact: An app may be able to access sensitive user data
Description: A permissions issue was addressed with additional
restrictions.
CVE-2024-54513: an anonymous researcher

Crash Reporter
Available for: macOS Sequoia
Impact: An app may be able to access protected user data
Description: A logic issue was addressed with improved file handling.
CVE-2024-44300: an anonymous researcher

DiskArbitration
Available for: macOS Sequoia
Impact: An encrypted volume may be accessed by a different user without
prompting for the password
Description: An authorization issue was addressed with improved state
management.
CVE-2024-54466: Michael Cohen

Disk Utility
Available for: macOS Sequoia
Impact: Running a mount command may unexpectedly execute arbitrary code
Description: A path handling issue was addressed with improved
validation.
CVE-2024-54489: D’Angelo Gonzalez of CrowdStrike

FontParser
Available for: macOS Sequoia
Impact: Processing a maliciously crafted font may result in the
disclosure of process memory
Description: The issue was addressed with improved checks.
CVE-2024-54486: Hossein Lotfi (@hosselot) of Trend Micro Zero Day
Initiative

Foundation
Available for: macOS Sequoia
Impact: A malicious app may be able to gain root privileges
Description: A logic issue was addressed with improved file handling.
CVE-2024-44291: Arsenii Kostromin (0x3c3e)

ImageIO
Available for: macOS Sequoia
Impact: Processing a maliciously crafted image may result in disclosure
of process memory
Description: The issue was addressed with improved checks.
CVE-2024-54500: Junsung Lee working with Trend Micro Zero Day Initiative

IOMobileFrameBuffer
Available for: macOS Sequoia
Impact: An attacker may be able to cause unexpected system termination
or arbitrary code execution in DCP firmware
Description: An out-of-bounds access issue was addressed with improved
bounds checking.
CVE-2024-54506: Ye Zhang (@VAR10CK) of Baidu Security

Kernel
Available for: macOS Sequoia
Impact: An attacker may be able to create a read-only memory mapping
that can be written to
Description: A race condition was addressed with additional validation.
CVE-2024-54494: sohybbyk

Kernel
Available for: macOS Sequoia
Impact: An app may be able to leak sensitive kernel state
Description: A race condition was addressed with improved locking.
CVE-2024-54510: Joseph Ravichandran (@0xjprx) of MIT CSAIL

Kernel
Available for: macOS Sequoia
Impact: An app may be able to cause unexpected system termination or
corrupt kernel memory
Description: The issue was addressed with improved memory handling.
CVE-2024-44245: an anonymous researcher

Kernel
Available for: macOS Sequoia
Impact: An app may be able to bypass kASLR
Description: The issue was addressed with improved memory handling.
CVE-2024-54531: Hyerean Jang, Taehun Kim, and Youngjoo Shin

LaunchServices
Available for: macOS Sequoia
Impact: An app may be able to elevate privileges
Description: A logic issue was addressed with improved state management.
CVE-2024-54465: an anonymous researcher

libexpat
Available for: macOS Sequoia
Impact: A remote attacker may cause an unexpected app termination or
arbitrary code execution
Description: This is a vulnerability in open source code and Apple
Software is among the affected projects. The CVE-ID was assigned by a
third party. Learn more about the issue and CVE-ID at cve.org.
CVE-2024-45490

libxpc
Available for: macOS Sequoia
Impact: An app may be able to break out of its sandbox
Description: The issue was addressed with improved checks.
CVE-2024-54514: an anonymous researcher

libxpc
Available for: macOS Sequoia
Impact: An app may be able to gain elevated privileges
Description: A logic issue was addressed with improved checks.
CVE-2024-44225: 风沐云烟(@binary_fmyy)

Logging
Available for: macOS Sequoia
Impact: A malicious application may be able to determine a user's
current location
Description: The issue was resolved by sanitizing logging
CVE-2024-54491: Kirin (@Pwnrin)

MediaRemote
Available for: macOS Sequoia
Impact: An app may be able to access user-sensitive data
Description: The issue was resolved by sanitizing logging.
CVE-2024-54484: Meng Zhang (鲸落) of NorthSea

Notification Center
Available for: macOS Sequoia
Impact: An app may be able to access user-sensitive data
Description: A privacy issue was addressed with improved private data
redaction for log entries.
CVE-2024-54504: 神罚(@Pwnrin)

PackageKit
Available for: macOS Sequoia
Impact: An app may be able to access user-sensitive data
Description: The issue was addressed with improved checks.
CVE-2024-54474: Mickey Jin (@patch1t)
CVE-2024-54476: Mickey Jin (@patch1t), Bohdan Stasiuk (@Bohdan_Stasiuk)

Passwords
Available for: macOS Sequoia
Impact: An attacker in a privileged network position may be able to
alter network traffic
Description: This issue was addressed by using HTTPS when sending
information over the network.
CVE-2024-54492: Talal Haj Bakry and Tommy Mysk of Mysk Inc. (@mysk_co)

Perl
Available for: macOS Sequoia
Impact: An app may be able to modify protected parts of the file system
Description: A logic issue was addressed with improved state management.
CVE-2023-32395: Arsenii Kostromin (0x3c3e)

Safari
Available for: macOS Sequoia
Impact: O...