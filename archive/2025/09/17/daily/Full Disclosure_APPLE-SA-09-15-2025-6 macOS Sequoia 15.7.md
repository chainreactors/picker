---
title: APPLE-SA-09-15-2025-6 macOS Sequoia 15.7
url: https://seclists.org/fulldisclosure/2025/Sep/54
source: Full Disclosure
date: 2025-09-17
fetch_date: 2025-10-02T20:16:48.611293
---

# APPLE-SA-09-15-2025-6 macOS Sequoia 15.7

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

[![Previous](/images/left-icon-16x16.png)](53)
[By Date](date.html#54)
[![Next](/images/right-icon-16x16.png)](55)

[![Previous](/images/left-icon-16x16.png)](53)
[By Thread](index.html#54)
[![Next](/images/right-icon-16x16.png)](55)

![](/shared/images/nst-icons.svg#search)

# APPLE-SA-09-15-2025-6 macOS Sequoia 15.7

---

*From*: Apple Product Security via Fulldisclosure <fulldisclosure () seclists org>
*Date*: Mon, 15 Sep 2025 16:35:44 -0700

---

```
-----BEGIN PGP SIGNED MESSAGE-----
Hash: SHA256

APPLE-SA-09-15-2025-6 macOS Sequoia 15.7

macOS Sequoia 15.7 addresses the following issues.
Information about the security content is also available at
https://support.apple.com/125111.

Apple maintains a Security Releases page at
https://support.apple.com/100100 which lists recent
software updates with security advisories.

AMD
Available for: macOS Sequoia
Impact: An app may be able to cause unexpected system termination
Description: A buffer overflow was addressed with improved bounds
checking.
CVE-2025-43312: ABC Research s.r.o.

AppKit
Available for: macOS Sequoia
Impact: An app may be able to access protected user data
Description: The issue was resolved by blocking unsigned services from
launching on Intel Macs.
CVE-2025-43321: Mickey Jin (@patch1t)

Apple Online Store Kit
Available for: macOS Sequoia
Impact: An app may be able to access protected user data
Description: A permissions issue was addressed with additional
restrictions.
CVE-2025-31268: Csaba Fitzl (@theevilbit) and Nolan Astrein of Kandji

AppSandbox
Available for: macOS Sequoia
Impact: An app may be able to access protected user data
Description: A permissions issue was addressed with additional
restrictions.
CVE-2025-43285: Zhongquan Li (@Guluisacat), Mickey Jin (@patch1t)

ATS
Available for: macOS Sequoia
Impact: An app may be able to break out of its sandbox
Description: This issue was addressed by removing the vulnerable code.
CVE-2025-43330: Bilal Siddiqui

CoreAudio
Available for: macOS Sequoia
Impact: Processing a maliciously crafted video file may lead to
unexpected app termination
Description: An out-of-bounds write issue was addressed with improved
input validation.
CVE-2025-43349: @zlluny working with Trend Zero Day Initiative

CoreMedia
Available for: macOS Sequoia
Impact: An app may be able to access sensitive user data
Description: A race condition was addressed with improved state
handling.
CVE-2025-43292: Csaba Fitzl (@theevilbit) and Nolan Astrein of Kandji

CoreServices
Available for: macOS Sequoia
Impact: A malicious app may be able to access private information
Description: A logic issue was addressed with improved checks.
CVE-2025-43305: an anonymous researcher, Mickey Jin (@patch1t)

GPU Drivers
Available for: macOS Sequoia
Impact: An app may be able to access sensitive user data
Description: An out-of-bounds read was addressed with improved bounds
checking.
CVE-2025-43326: Wang Yu of Cyberserval

IOHIDFamily
Available for: macOS Sequoia
Impact: An app may be able to cause unexpected system termination
Description: An out-of-bounds write issue was addressed with improved
bounds checking.
CVE-2025-43302: Keisuke Hosoda

IOKit
Available for: macOS Sequoia
Impact: An app may be able to access sensitive user data
Description: An authorization issue was addressed with improved state
management.
CVE-2025-31255: Csaba Fitzl (@theevilbit) of Kandji

Kernel
Available for: macOS Sequoia
Impact: A UDP server socket bound to a local interface may become bound
to all interfaces
Description: A logic issue was addressed with improved state management.
CVE-2025-43359: Viktor Oreshkin

libc
Available for: macOS Sequoia
Impact: An app may be able to cause a denial-of-service
Description: A denial-of-service issue was addressed with improved
validation.
CVE-2025-43299: Nathaniel Oh (@calysteon)
CVE-2025-43295: Nathaniel Oh (@calysteon)

Libinfo
Available for: macOS Sequoia
Impact: Processing a maliciously crafted string may lead to heap
corruption
Description: The issue was addressed with improved bounds checks.
CVE-2025-43353: Nathaniel Oh (@calysteon)

MediaLibrary
Available for: macOS Sequoia
Impact: An app may be able to access protected user data
Description: This issue was addressed by removing the vulnerable code.
CVE-2025-43319: Hikerell (Loadshine Lab)

MigrationKit
Available for: macOS Sequoia
Impact: An app may be able to access user-sensitive data
Description: This issue was addressed by removing the vulnerable code.
CVE-2025-43315: Rodolphe Brunetti (@eisw0lf) of Lupus Nova

MobileStorageMounter
Available for: macOS Sequoia
Impact: An app may be able to cause a denial-of-service
Description: A type confusion issue was addressed with improved memory
handling.
CVE-2025-43355: Dawuge of Shuffle Team

Notification Center
Available for: macOS Sequoia
Impact: An app may be able to access contact info related to
notifications in Notification Center
Description: A privacy issue was addressed with improved private data
redaction for log entries.
CVE-2025-43301: LFY@secsys from Fudan University

PackageKit
Available for: macOS Sequoia
Impact: An app may be able to gain root privileges
Description: A parsing issue in the handling of directory paths was
addressed with improved path validation.
CVE-2025-43298: an anonymous researcher

Perl
Available for: macOS Sequoia
Impact: Multiple issues in Perl
Description: This is a vulnerability in open source code and Apple
Software is among the affected projects. The CVE-ID was assigned by a
third party. Learn more about the issue and CVE-ID at cve.org.
CVE-2025-40909

Ruby
Available for: macOS Sequoia
Impact: Processing a file may lead to a denial-of-service or potentially
disclose memory contents
Description: This is a vulnerability in open source code and Apple
Software is among the affected projects. The CVE-ID was assigned by a
third party. Learn more about the issue and CVE-ID at cve.org.
CVE-2024-27280

Screenshots
Available for: macOS Sequoia
Impact: An app may be able to capture a screenshot of an app entering or
exiting full screen mode
Description: A privacy issue was addressed with improved checks.
CVE-2025-31259: an anonymous researcher

Security Initialization
Available for: macOS Sequoia
Impact: An app may be able to break out of its sandbox
Description: A file quarantine bypass was addressed with additional
checks.
CVE-2025-43332: an anonymous researcher

SharedFileList
Available for: macOS Sequoia
Impact: An app may be able to access sensitive user data
Description: The issue was addressed with improved input validation.
CVE-2025-43293: an anonymous researcher

SharedFileList
Available for: macOS Sequoia
Impact: An app may be able to modify protected parts of the file system
Description: A permissions issue was addressed by removing the
vulnerable code.
CVE-2025-43291: Ye Zhang of Baidu Security

SharedFileList
Available for: macOS Sequoia
Impact: An app may be able to break out of its sandbox
Description: A permissions issue was addressed with additional
restrictions.
CVE-2025-43286: pattern-f (@pattern_F_), @zlluny

Shortcuts
Available for: macOS Sequoia
Impact: A shortcut may be able to bypass sandbox restrictions
Description: A permissions issue was addressed with additional sandbox
restrictions.
CVE-2025-43358: 정답이 아닌 해답

Spell Check
Available for: macOS Sequoia
Impact: An app may be able to access sensitive user data
Description: A parsing issue in the handling of directory paths was
addressed with improved path validation.
CVE-20...