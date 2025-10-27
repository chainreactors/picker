---
title: APPLE-SA-09-15-2025-7 macOS Sonoma 14.8
url: https://seclists.org/fulldisclosure/2025/Sep/55
source: Full Disclosure
date: 2025-09-17
fetch_date: 2025-10-02T20:16:47.176550
---

# APPLE-SA-09-15-2025-7 macOS Sonoma 14.8

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

[![Previous](/images/left-icon-16x16.png)](54)
[By Date](date.html#55)
[![Next](/images/right-icon-16x16.png)](56)

[![Previous](/images/left-icon-16x16.png)](54)
[By Thread](index.html#55)
[![Next](/images/right-icon-16x16.png)](56)

![](/shared/images/nst-icons.svg#search)

# APPLE-SA-09-15-2025-7 macOS Sonoma 14.8

---

*From*: Apple Product Security via Fulldisclosure <fulldisclosure () seclists org>
*Date*: Mon, 15 Sep 2025 16:36:10 -0700

---

```
-----BEGIN PGP SIGNED MESSAGE-----
Hash: SHA256

APPLE-SA-09-15-2025-7 macOS Sonoma 14.8

macOS Sonoma 14.8 addresses the following issues.
Information about the security content is also available at
https://support.apple.com/125112.

Apple maintains a Security Releases page at
https://support.apple.com/100100 which lists recent
software updates with security advisories.

AMD
Available for: macOS Sonoma
Impact: An app may be able to cause unexpected system termination
Description: A buffer overflow was addressed with improved bounds
checking.
CVE-2025-43312: ABC Research s.r.o.

AppKit
Available for: macOS Sonoma
Impact: An app may be able to access protected user data
Description: The issue was resolved by blocking unsigned services from
launching on Intel Macs.
CVE-2025-43321: Mickey Jin (@patch1t)

Apple Online Store Kit
Available for: macOS Sonoma
Impact: An app may be able to access protected user data
Description: A permissions issue was addressed with additional
restrictions.
CVE-2025-31268: Csaba Fitzl (@theevilbit) and Nolan Astrein of Kandji

AppSandbox
Available for: macOS Sonoma
Impact: An app may be able to access protected user data
Description: A permissions issue was addressed with additional
restrictions.
CVE-2025-43285: Zhongquan Li (@Guluisacat), Mickey Jin (@patch1t)

CoreAudio
Available for: macOS Sonoma
Impact: Processing a maliciously crafted video file may lead to
unexpected app termination
Description: An out-of-bounds write issue was addressed with improved
input validation.
CVE-2025-43349: @zlluny working with Trend Zero Day Initiative

CoreAudio
Available for: macOS Sonoma
Impact: Processing a maliciously crafted audio file may lead to memory
corruption
Description: The issue was addressed with improved memory handling.
CVE-2025-43277: Google's Threat Analysis Group

CoreMedia
Available for: macOS Sonoma
Impact: A sandboxed process may be able to circumvent sandbox
restrictions
Description: A permissions issue was addressed with additional sandbox
restrictions.
CVE-2025-43273: Seo Hyun-gyu (@wh1te4ever), Minghao Lin (@Y1nKoc), 风
(binaryfmyy), BochengXiang(@Crispr), and YingQi Shi (@Mas0nShi), Dora
Orak

CoreServices
Available for: macOS Sonoma
Impact: A malicious app may be able to access private information
Description: A logic issue was addressed with improved checks.
CVE-2025-43305: an anonymous researcher, Mickey Jin (@patch1t)

GPU Drivers
Available for: macOS Sonoma
Impact: An app may be able to access sensitive user data
Description: An out-of-bounds read was addressed with improved bounds
checking.
CVE-2025-43326: Wang Yu of Cyberserval

IOHIDFamily
Available for: macOS Sonoma
Impact: An app may be able to cause unexpected system termination
Description: An out-of-bounds write issue was addressed with improved
bounds checking.
CVE-2025-43302: Keisuke Hosoda

IOKit
Available for: macOS Sonoma
Impact: An app may be able to access sensitive user data
Description: An authorization issue was addressed with improved state
management.
CVE-2025-31255: Csaba Fitzl (@theevilbit) of Kandji

Kernel
Available for: macOS Sonoma
Impact: A UDP server socket bound to a local interface may become bound
to all interfaces
Description: A logic issue was addressed with improved state management.
CVE-2025-43359: Viktor Oreshkin

LaunchServices
Available for: macOS Sonoma
Impact: An app may be able to access user-sensitive data
Description: A logic issue was addressed with improved checks.
CVE-2025-43231: Mickey Jin (@patch1t), Kirin@Pwnrin and LFY@secsys from
Fudan University, an anonymous researcher

libc
Available for: macOS Sonoma
Impact: An app may be able to cause a denial-of-service
Description: A denial-of-service issue was addressed with improved
validation.
CVE-2025-43299: Nathaniel Oh (@calysteon)
CVE-2025-43295: Nathaniel Oh (@calysteon)

Libinfo
Available for: macOS Sonoma
Impact: Processing a maliciously crafted string may lead to heap
corruption
Description: The issue was addressed with improved bounds checks.
CVE-2025-43353: Nathaniel Oh (@calysteon)

MediaLibrary
Available for: macOS Sonoma
Impact: An app may be able to access protected user data
Description: This issue was addressed by removing the vulnerable code.
CVE-2025-43319: Hikerell (Loadshine Lab)

MigrationKit
Available for: macOS Sonoma
Impact: An app may be able to access user-sensitive data
Description: This issue was addressed by removing the vulnerable code.
CVE-2025-43315: Rodolphe Brunetti (@eisw0lf) of Lupus Nova

MobileStorageMounter
Available for: macOS Sonoma
Impact: An app may be able to cause a denial-of-service
Description: A type confusion issue was addressed with improved memory
handling.
CVE-2025-43355: Dawuge of Shuffle Team

Notification Center
Available for: macOS Sonoma
Impact: An app may be able to access contact info related to
notifications in Notification Center
Description: A privacy issue was addressed with improved private data
redaction for log entries.
CVE-2025-43301: LFY@secsys from Fudan University

PackageKit
Available for: macOS Sonoma
Impact: An app may be able to gain root privileges
Description: A parsing issue in the handling of directory paths was
addressed with improved path validation.
CVE-2025-43298: an anonymous researcher

Perl
Available for: macOS Sonoma
Impact: Multiple issues in Perl
Description: This is a vulnerability in open source code and Apple
Software is among the affected projects. The CVE-ID was assigned by a
third party. Learn more about the issue and CVE-ID at cve.org.
CVE-2025-40909

Printing
Available for: macOS Sonoma
Impact: An app may be able to access protected user data
Description: A permissions issue was addressed with additional
restrictions.
CVE-2025-31269: Zhongcheng Li from IES Red Team of ByteDance

Ruby
Available for: macOS Sonoma
Impact: Processing a file may lead to a denial-of-service or potentially
disclose memory contents
Description: This is a vulnerability in open source code and Apple
Software is among the affected projects. The CVE-ID was assigned by a
third party. Learn more about the issue and CVE-ID at cve.org.
CVE-2024-27280

Screenshots
Available for: macOS Sonoma
Impact: An app may be able to capture a screenshot of an app entering or
exiting full screen mode
Description: A privacy issue was addressed with improved checks.
CVE-2025-31259: an anonymous researcher

Security Initialization
Available for: macOS Sonoma
Impact: An app may be able to break out of its sandbox
Description: A file quarantine bypass was addressed with additional
checks.
CVE-2025-43332: an anonymous researcher

SharedFileList
Available for: macOS Sonoma
Impact: An app may be able to access sensitive user data
Description: The issue was addressed with improved input validation.
CVE-2025-43293: an anonymous researcher

SharedFileList
Available for: macOS Sonoma
Impact: An app may be able to modify protected parts of the file system
Description: A permissions issue was addressed by removing the
vulnerable code.
CVE-2025-43291: Ye Zhang of Baidu Security

SharedFileList
Avail...