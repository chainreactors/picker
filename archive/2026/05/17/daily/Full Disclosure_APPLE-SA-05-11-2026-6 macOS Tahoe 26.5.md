---
title: APPLE-SA-05-11-2026-6 macOS Tahoe 26.5
url: https://seclists.org/fulldisclosure/2026/May/11
source: Full Disclosure
date: 2026-05-17
fetch_date: 2026-05-18T06:10:47.698617
---

# APPLE-SA-05-11-2026-6 macOS Tahoe 26.5

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

[![Previous](/images/left-icon-16x16.png)](10)
[By Date](date.html#11)
[![Next](/images/right-icon-16x16.png)](12)

[![Previous](/images/left-icon-16x16.png)](10)
[By Thread](index.html#11)
[![Next](/images/right-icon-16x16.png)](12)

![](/shared/images/nst-icons.svg#search)

# APPLE-SA-05-11-2026-6 macOS Tahoe 26.5

---

*From*: Apple Product Security via Fulldisclosure <fulldisclosure () seclists org>
*Date*: Mon, 11 May 2026 15:32:57 -0700

---

```
-----BEGIN PGP SIGNED MESSAGE-----
Hash: SHA256

APPLE-SA-05-11-2026-6 macOS Tahoe 26.5

macOS Tahoe 26.5 addresses the following issues.
Information about the security content is also available at
https://support.apple.com/en-us/127115.

Apple maintains a Security Releases page at
https://support.apple.com/100100 which lists recent
software updates with security advisories.

Accelerate
Available for: macOS Tahoe
Impact: An app may be able to cause a denial-of-service
Description: An out-of-bounds read was addressed with improved bounds
checking.
CVE-2026-28991: Seiji Sakurai (@HeapSmasher)

Accounts
Available for: macOS Tahoe
Impact: An app may be able to bypass certain Privacy preferences
Description: A permissions issue was addressed with additional
restrictions.
CVE-2026-28988: Asaf Cohen

APFS
Available for: macOS Tahoe
Impact: An app may be able to cause unexpected system termination
Description: A buffer overflow was addressed with improved bounds
checking.
CVE-2026-28959: Dave G.

App Intents
Available for: macOS Tahoe
Impact: A malicious app may be able to break out of its sandbox
Description: A logic issue was addressed with improved restrictions.
CVE-2026-28995: Vamshi Paili, Tony Gorez (@tonygo_) for Reverse Society

AppleJPEG
Available for: macOS Tahoe
Impact: Processing a maliciously crafted image may lead to a
denial-of-service
Description: This is a vulnerability in open source code and Apple
Software is among the affected projects. The CVE-ID was assigned by a
third party. Learn more about the issue and CVE-ID at cve.org.
CVE-2026-1837

AppleJPEG
Available for: macOS Tahoe
Impact: Processing a maliciously crafted media file may lead to
unexpected app termination or corrupt process memory
Description: A memory corruption issue was addressed with improved input
validation.
CVE-2026-28956: impost0r (ret2plt)

Audio
Available for: macOS Tahoe
Impact: Processing an audio stream in a maliciously crafted media file
may terminate the process
Description: The issue was addressed with improved memory handling.
CVE-2026-39869: David Ige of Beryllium Security

CoreMedia
Available for: macOS Tahoe
Impact: An app may be able to access private information
Description: This issue was addressed through improved state management.
CVE-2026-28922: Arni Hardarson

CoreServices
Available for: macOS Tahoe
Impact: Processing a maliciously crafted file may lead to unexpected app
termination
Description: The issue was addressed with improved checks.
CVE-2026-28936: Andreas Jaegersberger & Ro Achterberg of Nosebeard Labs

CoreSymbolication
Available for: macOS Tahoe
Impact: Parsing a maliciously crafted file may lead to an unexpected app
termination
Description: An out-of-bounds access issue was addressed with improved
bounds checking.
CVE-2026-28918: Niels Hofmans, Anonymous working with TrendAI Zero Day
Initiative

CUPS
Available for: macOS Tahoe
Impact: An app may be able to gain root privileges
Description: A parsing issue in the handling of directory paths was
addressed with improved path validation.
CVE-2026-28915: Andreas Jaegersberger & Ro Achterberg of Nosebeard Labs

FileProvider
Available for: macOS Tahoe
Impact: An app may be able to access sensitive user data
Description: A race condition was addressed with additional validation.
CVE-2026-43659: Alex Radocea

GPU Drivers
Available for: macOS Tahoe
Impact: A malicious app may be able to break out of its sandbox
Description: A logging issue was addressed with improved data redaction.
CVE-2026-28923: Kun Peeks (@SwayZGl1tZyyy)

HFS
Available for: macOS Tahoe
Impact: An app may be able to cause unexpected system termination or
write kernel memory
Description: A buffer overflow was addressed with improved bounds
checking.
CVE-2026-28925: Aswin Kumar Gokula Kannan, Dave G.

ImageIO
Available for: macOS Tahoe
Impact: Processing a maliciously crafted image may corrupt process
memory
Description: A buffer overflow issue was addressed with improved memory
handling.
CVE-2026-43661: an anonymous researcher

ImageIO
Available for: macOS Tahoe
Impact: Processing a maliciously crafted file may lead to unexpected app
termination
Description: The issue was addressed with improved bounds checks.
CVE-2026-28977: Suresh Sundaram

ImageIO
Available for: macOS Tahoe
Impact: Processing a maliciously crafted image may corrupt process
memory
Description: The issue was addressed with improved memory handling.
CVE-2026-28990: Jiri Ha, Arni Hardarson

Installer
Available for: macOS Tahoe
Impact: A malicious app may be able to break out of its sandbox
Description: A permissions issue was addressed with additional
restrictions.
CVE-2026-28978: wdszzml and Atuin Automated Vulnerability Discovery
Engine

IOHIDFamily
Available for: macOS Tahoe
Impact: An attacker may be able to cause unexpected app termination
Description: A memory corruption vulnerability was addressed with
improved locking.
CVE-2026-28992: Johnny Franks (@zeroxjf)

IOHIDFamily
Available for: macOS Tahoe
Impact: An app may be able to determine kernel memory layout
Description: A logging issue was addressed with improved data redaction.
CVE-2026-28943: Google Threat Analysis Group

IOKit
Available for: macOS Tahoe
Impact: An app may be able to cause unexpected system termination
Description: A use after free issue was addressed with improved memory
management.
CVE-2026-28969: Mihalis Haatainen, Ari Hawking, Ashish Kunwar

IOSurfaceAccelerator
Available for: macOS Tahoe
Impact: An app may be able to cause unexpected system termination or
read kernel memory
Description: An out-of-bounds read was addressed with improved bounds
checking.
CVE-2026-43655: Somair Ansar and an anonymous researcher

Kernel
Available for: macOS Tahoe
Impact: An app may be able to disclose kernel memory
Description: The issue was addressed with improved memory handling.
CVE-2026-43654: Vaagn Vardanian, Nathaniel Oh (@calysteon)

Kernel
Available for: macOS Tahoe
Impact: An app may be able to modify protected parts of the file system
Description: A denial of service issue was addressed by removing the
vulnerable code.
CVE-2026-28908: beist

Kernel
Available for: macOS Tahoe
Impact: A maliciously crafted disk image may bypass Gatekeeper checks
Description: A file quarantine bypass was addressed with additional
checks.
CVE-2026-28954: Yiğit Can YILMAZ (@yilmazcanyigit)

Kernel
Available for: macOS Tahoe
Impact: A local user may be able to cause unexpected system termination
or read kernel memory
Description: A buffer overflow was addressed with improved input
validation.
CVE-2026-28897: popku1337, Billy Jheng Bing Jhong and Pan Zhenpeng
(@Peterpan0927) of STAR Labs SG Pte. Ltd., Robert Tran, Aswin kumar
Gokulakannan

Kernel
Available for: macOS Tahoe
Impact: An app may be able to cause unexpected system termination
Description: An integer overflow was addressed with improved input
validation.
CVE-2026-28952: Calif.io in collaboration with Claude and Anthropic
Research

Kernel
Available for: macOS Tahoe
Impact: An app may be able to gain root privileges
Descripti...