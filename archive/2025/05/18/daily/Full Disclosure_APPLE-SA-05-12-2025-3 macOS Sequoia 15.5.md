---
title: APPLE-SA-05-12-2025-3 macOS Sequoia 15.5
url: https://seclists.org/fulldisclosure/2025/May/7
source: Full Disclosure
date: 2025-05-18
fetch_date: 2025-10-06T22:27:56.124910
---

# APPLE-SA-05-12-2025-3 macOS Sequoia 15.5

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

# APPLE-SA-05-12-2025-3 macOS Sequoia 15.5

---

*From*: Apple Product Security via Fulldisclosure <fulldisclosure () seclists org>
*Date*: Mon, 12 May 2025 15:39:36 -0700

---

```
-----BEGIN PGP SIGNED MESSAGE-----
Hash: SHA256

APPLE-SA-05-12-2025-3 macOS Sequoia 15.5

macOS Sequoia 15.5 addresses the following issues.
Information about the security content is also available at
https://support.apple.com/122716.

Apple maintains a Security Releases page at
https://support.apple.com/100100 which lists recent
software updates with security advisories.

afpfs
Available for: macOS Sequoia
Impact: Connecting to a malicious AFP server may corrupt kernel memory
Description: The issue was addressed with improved memory handling.
CVE-2025-31246: Joseph Ravichandran (@0xjprx) of MIT CSAIL

afpfs
Available for: macOS Sequoia
Impact: Mounting a maliciously crafted AFP network share may lead to
system termination
Description: This issue was addressed with improved checks.
CVE-2025-31240: Dave G.
CVE-2025-31237: Dave G.

Apple Intelligence Reports
Available for: macOS Sequoia
Impact: An app may be able to access sensitive user data
Description: A permissions issue was addressed with additional
restrictions.
CVE-2025-31260: Thomas Völkl (@vollkorntomate), SEEMOO, TU Darmstadt

AppleJPEG
Available for: macOS Sequoia
Impact: Processing a maliciously crafted media file may lead to
unexpected app termination or corrupt process memory
Description: The issue was addressed with improved input sanitization.
CVE-2025-31251: Hossein Lotfi (@hosselot) of Trend Micro Zero Day
Initiative

Audio
Available for: macOS Sequoia
Impact: An app may be able to cause unexpected system termination
Description: A double free issue was addressed with improved memory
management.
CVE-2025-31235: Dillon Franke working with Google Project Zero

BOM
Available for: macOS Sequoia
Impact: Processing maliciously crafted web content may lead to an
unexpected process crash
Description: The issue was addressed with improved memory handling.
CVE-2025-24222: wac working with Trend Micro Zero Day Initiative

Core Bluetooth
Available for: macOS Sequoia
Impact: An app may be able to access sensitive user data
Description: This issue was addressed through improved state management.
CVE-2025-31212: Guilherme Rambo of Best Buddy Apps (rambo.codes)

CoreAudio
Available for: macOS Sequoia
Impact: Parsing a file may lead to an unexpected app termination
Description: The issue was addressed with improved checks.
CVE-2025-31208: Hossein Lotfi (@hosselot) of Trend Micro Zero Day
Initiative

CoreGraphics
Available for: macOS Sequoia
Impact: Parsing a file may lead to disclosure of user information
Description: An out-of-bounds read was addressed with improved bounds
checking.
CVE-2025-31209: Hossein Lotfi (@hosselot) of Trend Micro Zero Day
Initiative

CoreMedia
Available for: macOS Sequoia
Impact: Parsing a file may lead to an unexpected app termination
Description: A use-after-free issue was addressed with improved memory
management.
CVE-2025-31239: Hossein Lotfi (@hosselot) of Trend Micro Zero Day
Initiative

CoreMedia
Available for: macOS Sequoia
Impact: Processing a maliciously crafted video file may lead to
unexpected app termination or corrupt process memory
Description: The issue was addressed with improved input sanitization.
CVE-2025-31233: Hossein Lotfi (@hosselot) of Trend Micro Zero Day
Initiative

Finder
Available for: macOS Sequoia
Impact: An app may be able to access sensitive user data
Description: An information disclosure issue was addressed with improved
privacy controls.
CVE-2025-31236: Kirin@Pwnrin and LFY@secsys from Fudan University

Found in Apps
Available for: macOS Sequoia
Impact: An app may be able to access user-sensitive data
Description: A privacy issue was addressed by removing the vulnerable
code.
CVE-2025-30443: Bohdan Stasiuk (@bohdan_stasiuk)

ImageIO
Available for: macOS Sequoia
Impact: Processing a maliciously crafted image may lead to a denial-of-
service
Description: A logic issue was addressed with improved checks.
CVE-2025-31226: Saagar Jha

Installer
Available for: macOS Sequoia
Impact: A sandboxed app may be able to access sensitive user data
Description: A logic issue was addressed with improved checks.
CVE-2025-31232: an anonymous researcher

Kernel
Available for: macOS Sequoia
Impact: A remote attacker may cause an unexpected app termination
Description: A double free issue was addressed with improved memory
management.
CVE-2025-31241: Christian Kohlschütter

Kernel
Available for: macOS Sequoia
Impact: An attacker may be able to cause unexpected system termination
or corrupt kernel memory
Description: The issue was addressed with improved memory handling.
CVE-2025-31219: Michael DePlante (@izobashi) and Lucas Leong
(@_wmliang_) of Trend Micro Zero Day Initiative

libexpat
Available for: macOS Sequoia
Impact: Multiple issues in libexpat, including unexpected app
termination or arbitrary code execution
Description: This is a vulnerability in open source code and Apple
Software is among the affected projects. The CVE-ID was assigned by a
third party. Learn more about the issue and CVE-ID at cve.org.
CVE-2024-8176

Libinfo
Available for: macOS Sequoia
Impact: An app may be able to bypass ASLR
Description: The issue was addressed with improved checks.
CVE-2025-30440: Paweł Płatek (Trail of Bits)

mDNSResponder
Available for: macOS Sequoia
Impact: A user may be able to elevate privileges
Description: A correctness issue was addressed with improved checks.
CVE-2025-31222: Paweł Płatek (Trail of Bits)

Mobile Device Service
Available for: macOS Sequoia
Impact: A malicious app may be able to gain root privileges
Description: An input validation issue was addressed by removing the
vulnerable code.
CVE-2025-24274: an anonymous researcher

NetworkExtension
Available for: macOS Sequoia
Impact: An app may be able to observe the hostnames of new network
connections
Description: This issue was addressed by removing the vulnerable code.
CVE-2025-31218: Adam M.

Notes
Available for: macOS Sequoia
Impact: Hot corner may unexpectedly reveal a user’s deleted notes
Description: The issue was addressed with improved handling of caches.
CVE-2025-31256: Sourabhkumar Mishra

Notification Center
Available for: macOS Sequoia
Impact: An app may be able to access sensitive user data
Description: A privacy issue was addressed with improved private data
redaction for log entries.
CVE-2025-24142: LFY@secsys from Fudan University

OpenSSH
Available for: macOS Sequoia
Impact: Multiple issues in OpenSSH
Description: This is a vulnerability in open source code and Apple
Software is among the affected projects. The CVE-ID was assigned by a
third party. Learn more about the issue and CVE-ID at cve.org.
CVE-2025-26465
CVE-2025-26466

Pro Res
Available for: macOS Sequoia
Impact: An attacker may be able to cause unexpected system termination
or corrupt kernel memory
Description: The issue was addressed with improved input sanitization.
CVE-2025-31234: CertiK (@CertiK)

Pro Res
Available for: macOS Sequoia
Impact: An app may be able to cause unexpected system termination
Description: The issue was addressed with improved checks.
CVE-2025-31245: wac

quarantine
...