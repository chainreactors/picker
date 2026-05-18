---
title: APPLE-SA-05-11-2026-7 macOS Sequoia 15.7.7
url: https://seclists.org/fulldisclosure/2026/May/12
source: Full Disclosure
date: 2026-05-17
fetch_date: 2026-05-18T06:10:47.385417
---

# APPLE-SA-05-11-2026-7 macOS Sequoia 15.7.7

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

[![Previous](/images/left-icon-16x16.png)](11)
[By Date](date.html#12)
[![Next](/images/right-icon-16x16.png)](7)

[![Previous](/images/left-icon-16x16.png)](11)
[By Thread](index.html#12)
[![Next](/images/right-icon-16x16.png)](7)

![](/shared/images/nst-icons.svg#search)

# APPLE-SA-05-11-2026-7 macOS Sequoia 15.7.7

---

*From*: Apple Product Security via Fulldisclosure <fulldisclosure () seclists org>
*Date*: Mon, 11 May 2026 15:33:20 -0700

---

```
-----BEGIN PGP SIGNED MESSAGE-----
Hash: SHA256

APPLE-SA-05-11-2026-7 macOS Sequoia 15.7.7

macOS Sequoia 15.7.7 addresses the following issues.
Information about the security content is also available at
https://support.apple.com/en-us/127116.

Apple maintains a Security Releases page at
https://support.apple.com/100100 which lists recent
software updates with security advisories.

APFS
Available for: macOS Sequoia
Impact: An app may be able to cause unexpected system termination
Description: A buffer overflow was addressed with improved bounds
checking.
CVE-2026-28959: Dave G.

AppleJPEG
Available for: macOS Sequoia
Impact: Processing a maliciously crafted media file may lead to
unexpected app termination or corrupt process memory
Description: A memory corruption issue was addressed with improved input
validation.
CVE-2026-28956: impost0r (ret2plt)

Audio
Available for: macOS Sequoia
Impact: Processing an audio stream in a maliciously crafted media file
may terminate the process
Description: The issue was addressed with improved memory handling.
CVE-2026-39869: David Ige of Beryllium Security

CoreMedia
Available for: macOS Sequoia
Impact: An app may be able to access private information
Description: This issue was addressed through improved state management.
CVE-2026-28922: Arni Hardarson

Crash Reporter
Available for: macOS Sequoia
Impact: An app may be able to enumerate a user's installed apps
Description: A privacy issue was addressed by removing sensitive data.
CVE-2026-28878: Zhongcheng Li from IES Red Team

CUPS
Available for: macOS Sequoia
Impact: An app may be able to gain root privileges
Description: A parsing issue in the handling of directory paths was
addressed with improved path validation.
CVE-2026-28915: Andreas Jaegersberger & Ro Achterberg of Nosebeard Labs

FileProvider
Available for: macOS Sequoia
Impact: An app may be able to access sensitive user data
Description: A race condition was addressed with additional validation.
CVE-2026-43659: Alex Radocea

GPU Drivers
Available for: macOS Sequoia
Impact: A malicious app may be able to break out of its sandbox
Description: A logging issue was addressed with improved data redaction.
CVE-2026-28923: Kun Peeks (@SwayZGl1tZyyy)

HFS
Available for: macOS Sequoia
Impact: An app may be able to cause unexpected system termination or
write kernel memory
Description: A buffer overflow was addressed with improved bounds
checking.
CVE-2026-28925: Dave G., Aswin Kumar Gokula Kannan

Icons
Available for: macOS Sequoia
Impact: An app may be able to break out of its sandbox
Description: An access issue was addressed with additional sandbox
restrictions.
CVE-2025-43524: Csaba Fitzl (@theevilbit) of Iru

ImageIO
Available for: macOS Sequoia
Impact: Processing a maliciously crafted file may lead to unexpected app
termination
Description: The issue was addressed with improved bounds checks.
CVE-2026-28977: Suresh Sundaram

ImageIO
Available for: macOS Sequoia
Impact: Processing a maliciously crafted image may corrupt process
memory
Description: The issue was addressed with improved memory handling.
CVE-2026-28990: Jiri Ha, Arni Hardarson

Installer
Available for: macOS Sequoia
Impact: A malicious app may be able to break out of its sandbox
Description: A permissions issue was addressed with additional
restrictions.
CVE-2026-28978: wdszzml and Atuin Automated Vulnerability Discovery
Engine

IOHIDFamily
Available for: macOS Sequoia
Impact: An attacker may be able to cause unexpected app termination
Description: A memory corruption vulnerability was addressed with
improved locking.
CVE-2026-28992: Johnny Franks (@zeroxjf)

IOHIDFamily
Available for: macOS Sequoia
Impact: An app may be able to determine kernel memory layout
Description: A logging issue was addressed with improved data redaction.
CVE-2026-28943: Google Threat Analysis Group

IOKit
Available for: macOS Sequoia
Impact: An app may be able to cause unexpected system termination
Description: A use after free issue was addressed with improved memory
management.
CVE-2026-28969: Mihalis Haatainen, Ari Hawking, Ashish Kunwar

Kernel
Available for: macOS Sequoia
Impact: An app may be able to disclose kernel memory
Description: The issue was addressed with improved memory handling.
CVE-2026-43654: Vaagn Vardanian, Nathaniel Oh (@calysteon)

Kernel
Available for: macOS Sequoia
Impact: A maliciously crafted disk image may bypass Gatekeeper checks
Description: A file quarantine bypass was addressed with additional
checks.
CVE-2026-28954: Yiğit Can YILMAZ (@yilmazcanyigit)

Kernel
Available for: macOS Sequoia
Impact: A local user may be able to cause unexpected system termination
or read kernel memory
Description: A buffer overflow was addressed with improved input
validation.
CVE-2026-28897: Robert Tran, popku1337, Billy Jheng Bing Jhong and Pan
Zhenpeng (@Peterpan0927) of STAR Labs SG Pte. Ltd., Aswin kumar
Gokulakannan

Kernel
Available for: macOS Sequoia
Impact: An app may be able to cause unexpected system termination
Description: An integer overflow was addressed with improved input
validation.
CVE-2026-28952: Calif.io in collaboration with Claude and Anthropic
Research

Kernel
Available for: macOS Sequoia
Impact: An app may be able to modify protected parts of the file system
Description: A denial of service issue was addressed by removing the
vulnerable code.
CVE-2026-28908: beist

Kernel
Available for: macOS Sequoia
Impact: An app may be able to gain root privileges
Description: An authorization issue was addressed with improved state
management.
CVE-2026-28951: Csaba Fitzl (@theevilbit) of Iru

Kernel
Available for: macOS Sequoia
Impact: An app may be able to cause unexpected system termination or
write kernel memory
Description: An out-of-bounds write issue was addressed with improved
input validation.
CVE-2026-28972: Billy Jheng Bing Jhong and Pan Zhenpeng (@Peterpan0927)
of STAR Labs SG Pte. Ltd., Ryan Hileman via Xint Code (xint.io)

Kernel
Available for: macOS Sequoia
Impact: An app may be able to cause unexpected system termination
Description: A race condition was addressed with additional validation.
CVE-2026-28986: Tristan Madani (@TristanInSec) from Talence Security,
Ryan Hileman via Xint Code (xint.io), Chris Betz

Kernel
Available for: macOS Sequoia
Impact: An app may be able to leak sensitive kernel state
Description: A logging issue was addressed with improved data redaction.
CVE-2026-28987: Dhiyanesh Selvaraj (@redroot97)

Mail Drafts
Available for: macOS Sequoia
Impact: Replying to an email could display remote images in Mail in
Lockdown Mode
Description: A logic issue was addressed with improved checks.
CVE-2026-28929: Yiğit Can YILMAZ (@yilmazcanyigit)

mDNSResponder
Available for: macOS Sequoia
Impact: A remote attacker may be able to cause unexpected system
termination or corrupt kernel memory
Description: A use after free issue was addressed with improved memory
management.
CVE-2026-43668: Ricardo Prado, Anton Pakhunov

mDNSResponder
Available for: macOS Sequoia
Impact: An attacker on the l...