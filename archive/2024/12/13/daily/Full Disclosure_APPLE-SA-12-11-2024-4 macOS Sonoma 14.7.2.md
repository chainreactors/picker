---
title: APPLE-SA-12-11-2024-4 macOS Sonoma 14.7.2
url: https://seclists.org/fulldisclosure/2024/Dec/8
source: Full Disclosure
date: 2024-12-13
fetch_date: 2025-10-06T19:41:01.616862
---

# APPLE-SA-12-11-2024-4 macOS Sonoma 14.7.2

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

[![Previous](/images/left-icon-16x16.png)](7)
[By Date](date.html#8)
[![Next](/images/right-icon-16x16.png)](9)

[![Previous](/images/left-icon-16x16.png)](7)
[By Thread](index.html#8)
[![Next](/images/right-icon-16x16.png)](9)

![](/shared/images/nst-icons.svg#search)

# APPLE-SA-12-11-2024-4 macOS Sonoma 14.7.2

---

*From*: Apple Product Security via Fulldisclosure <fulldisclosure () seclists org>
*Date*: Wed, 11 Dec 2024 16:37:38 -0700

---

```
-----BEGIN PGP SIGNED MESSAGE-----
Hash: SHA256

APPLE-SA-12-11-2024-4 macOS Sonoma 14.7.2

macOS Sonoma 14.7.2 addresses the following issues.
Information about the security content is also available at
https://support.apple.com/121840.

Apple maintains a Security Releases page at
https://support.apple.com/100100 which lists recent
software updates with security advisories.

Apple Software Restore
Available for: macOS Sonoma
Impact: An app may be able to access user-sensitive data
Description: The issue was addressed with improved checks.
CVE-2024-54477: Mickey Jin (@patch1t), Csaba Fitzl (@theevilbit) of
Kandji

AppleGraphicsControl
Available for: macOS Sonoma
Impact: Parsing a maliciously crafted video file may lead to unexpected
system termination
Description: The issue was addressed with improved memory handling.
CVE-2024-44220: D4m0n

AppleMobileFileIntegrity
Available for: macOS Sonoma
Impact: An app may be able to access sensitive user data
Description: This issue was addressed with improved checks.
CVE-2024-54527: Mickey Jin (@patch1t)

AppleMobileFileIntegrity
Available for: macOS Sonoma
Impact: A malicious app may be able to access private information
Description: The issue was addressed with improved checks.
CVE-2024-54526: Mickey Jin (@patch1t), Arsenii Kostromin (0x3c3e)

Audio
Available for: macOS Sonoma
Impact: An app may be able to execute arbitrary code with kernel
privileges
Description: A logic issue was addressed with improved checks.
CVE-2024-54529: Dillon Franke working with Google Project Zero

Crash Reporter
Available for: macOS Sonoma
Impact: An app may be able to access protected user data
Description: A logic issue was addressed with improved file handling.
CVE-2024-44300: an anonymous researcher

DiskArbitration
Available for: macOS Sonoma
Impact: An encrypted volume may be accessed by a different user without
prompting for the password
Description: An authorization issue was addressed with improved state
management.
CVE-2024-54466: Michael Cohen

Disk Utility
Available for: macOS Sonoma
Impact: Running a mount command may unexpectedly execute arbitrary code
Description: A path handling issue was addressed with improved
validation.
CVE-2024-54489: D’Angelo Gonzalez of CrowdStrike

FontParser
Available for: macOS Sonoma
Impact: Processing a maliciously crafted font may result in the
disclosure of process memory
Description: The issue was addressed with improved checks.
CVE-2024-54486: Hossein Lotfi (@hosselot) of Trend Micro Zero Day
Initiative

ImageIO
Available for: macOS Sonoma
Impact: Processing a maliciously crafted image may result in disclosure
of process memory
Description: The issue was addressed with improved checks.
CVE-2024-54500: Junsung Lee working with Trend Micro Zero Day Initiative

Kernel
Available for: macOS Sonoma
Impact: An attacker may be able to create a read-only memory mapping
that can be written to
Description: A race condition was addressed with additional validation.
CVE-2024-54494: sohybbyk

Kernel
Available for: macOS Sonoma
Impact: An app may be able to leak sensitive kernel state
Description: A race condition was addressed with improved locking.
CVE-2024-54510: Joseph Ravichandran (@0xjprx) of MIT CSAIL

Kernel
Available for: macOS Sonoma
Impact: An app may be able to cause unexpected system termination or
corrupt kernel memory
Description: The issue was addressed with improved memory handling.
CVE-2024-44245: an anonymous researcher

libarchive
Available for: macOS Sonoma
Impact: Processing a malicious crafted file may lead to a denial-of-
service
Description: The issue was addressed with improved memory handling.
CVE-2024-44201: Ben Roeder

libexpat
Available for: macOS Sonoma
Impact: A remote attacker may cause an unexpected app termination or
arbitrary code execution
Description: This is a vulnerability in open source code and Apple
Software is among the affected projects. The CVE-ID was assigned by a
third party. Learn more about the issue and CVE-ID at cve.org.
CVE-2024-45490

libxpc
Available for: macOS Sonoma
Impact: An app may be able to break out of its sandbox
Description: The issue was addressed with improved checks.
CVE-2024-54514: an anonymous researcher

libxpc
Available for: macOS Sonoma
Impact: An app may be able to gain elevated privileges
Description: A logic issue was addressed with improved checks.
CVE-2024-44225: 风沐云烟(@binary_fmyy)

PackageKit
Available for: macOS Sonoma
Impact: An app may be able to access user-sensitive data
Description: The issue was addressed with improved checks.
CVE-2024-54474: Mickey Jin (@patch1t)
CVE-2024-54476: Mickey Jin (@patch1t), Bohdan Stasiuk (@Bohdan_Stasiuk)

SceneKit
Available for: macOS Sonoma
Impact: Processing a maliciously crafted file may lead to a denial of
service
Description: The issue was addressed with improved checks.
CVE-2024-54501: Michael DePlante (@izobashi) of Trend Micro's Zero Day
Initiative

Screen Sharing Server
Available for: macOS Sonoma
Impact: A user with screen sharing access may be able to view another
user's screen
Description: This issue was addressed through improved state management.
CVE-2024-44248: Halle Winkler, Politepix (theoffcuts.org)

SharedFileList
Available for: macOS Sonoma
Impact: An app may be able to overwrite arbitrary files
Description: A logic issue was addressed with improved restrictions.
CVE-2024-54528: an anonymous researcher

SharedFileList
Available for: macOS Sonoma
Impact: An app may be able to break out of its sandbox
Description: A path handling issue was addressed with improved
validation.
CVE-2024-54498: an anonymous researcher

Software Update
Available for: macOS Sonoma
Impact: A malicious app may be able to gain root privileges
Description: A logic issue was addressed with improved file handling.
CVE-2024-44291: Arsenii Kostromin (0x3c3e)

StorageKit
Available for: macOS Sonoma
Impact: A malicious app may be able to gain root privileges
Description: A permissions issue was addressed with additional
restrictions.
CVE-2024-44224: Amy (@asentientbot)

Swift
Available for: macOS Sonoma
Impact: An app may be able to modify protected parts of the file system
Description: The issue was addressed with improved permissions logic.
CVE-2024-54495: Claudio Bozzato and Francesco Benvenuto of Cisco Talos,
Arsenii Kostromin (0x3c3e)

Additional recognition

CUPS
We would like to acknowledge evilsocket for their assistance.

Proximity
We would like to acknowledge Junming C. (@Chapoly1305) and Prof. Qiang
Zeng of George Mason University for their assistance.

Sandbox
We would like to acknowledge IES Red Team of ByteDance for their
assistance.

macOS Sonoma 14.7.2 may be obtained from the Mac App Store or Apple's
Software Downloads web site: https://support.apple.com/downloads/

All information is also posted on the Apple Security Releases
web site: https://support.apple.com/100100.

This message is signed with Apple's Product Security PGP key,
and details are available at:
https://www.apple.com/support/security/pgp/

-----BEGIN PGP SIGNATURE-----

iQIzBAEBCAAdFiE...