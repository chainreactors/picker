---
title: APPLE-SA-09-14-2026-7 watchOS 27
url: https://seclists.org/fulldisclosure/2026/Sep/59
source: Full Disclosure
date: 2026-09-22
fetch_date: 2026-09-23T06:55:24.598265
---

# APPLE-SA-09-14-2026-7 watchOS 27

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

[![Previous](/images/left-icon-16x16.png)](58)
[By Date](date.html#59)
[![Next](/images/right-icon-16x16.png)](60)

[![Previous](/images/left-icon-16x16.png)](58)
[By Thread](index.html#59)
[![Next](/images/right-icon-16x16.png)](60)

![](/shared/images/nst-icons.svg#search)

# APPLE-SA-09-14-2026-7 watchOS 27

---

*From*: Apple Product Security via Fulldisclosure <fulldisclosure () seclists org>
*Date*: Mon, 14 Sep 2026 15:09:02 -0700

---

```
-----BEGIN PGP SIGNED MESSAGE-----
Hash: SHA256

APPLE-SA-09-14-2026-7 watchOS 27

watchOS 27 addresses the following issues.
Information about the security content is also available at
https://support.apple.com/149037.

Apple maintains a Security Releases page at
https://support.apple.com/100100 which lists recent
software updates with security advisories.

Accelerate Framework
Available for: Apple Watch Series 9 and later
Impact: Processing a maliciously crafted image may lead to unexpected
process termination
Description: An out-of-bounds write issue was addressed with improved
bounds checking.
CVE-2026-86882: Peter Malone

Accessibility
Available for: Apple Watch Series 9 and later
Impact: An app may be able to access sensitive user data
Description: This issue was addressed with improved data protection.
CVE-2026-43664: Stuart Wallace, Ilya Andr (andrd3v), Rosyna Keller of
Totally Not Malicious Software, CJ Vana, David Strnadel, Daniel Febrero,
Asaf Cohen, Gongyu Ma (@Mezone0), Jian Lee (@speedyfriend433)

APFS
Available for: Apple Watch Series 9 and later
Impact: An app may be able to cause unexpected system termination or
write kernel memory
Description: An out-of-bounds write issue was addressed with improved
bounds checking.
CVE-2026-84523: Cem Onat Karagun, an anonymous researcher

App Store
Available for: Apple Watch Series 9 and later
Impact: A local app may be able to read a persistent account identifier
Description: A permissions issue was addressed with additional
restrictions.
CVE-2026-86888: Zhongcheng Li (CK01)

Apple Account
Available for: Apple Watch Series 9 and later
Impact: A malicious application may be able to leak sensitive user
information
Description: An information disclosure issue was addressed with improved
state management.
CVE-2026-84586: Prashan Samarathunge, Zhongcheng Li (CK01)

AppleAVD
Available for: Apple Watch Series 9 and later
Impact: An app may be able to cause unexpected system termination
Description: A use after free issue was addressed with improved memory
management.
CVE-2026-65407: Franco Belman at Blackwing Intelligence

Audio
Available for: Apple Watch Series 9 and later
Impact: An app may be able to leak sensitive user information
Description: A logic issue was addressed with improved checks.
CVE-2026-65339: Mustafa Calap (@ordinal0, dbg.re), Meta Red Team X - Nik
Tsytsarkin

AuthKit
Available for: Apple Watch Series 9 and later
Impact: A local app may be able to read a persistent account identifier
Description: A permissions issue was addressed with additional
restrictions.
CVE-2026-84583: Zhongcheng Li from IES Red Team

AVEVideoEncoder
Available for: Apple Watch Series 9 and later
Impact: An app may be able to cause unexpected system termination
Description: The issue was addressed with improved checks.
CVE-2026-65410: Calif.io in collaboration with Claude and Anthropic
Research

AVEVideoEncoder
Available for: Apple Watch Series 9 and later
Impact: An app may be able to cause unexpected system termination
Description: A type confusion issue was addressed with improved memory
handling.
CVE-2026-84616: Peter Malone

AVEVideoEncoder
Available for: Apple Watch Series 9 and later
Impact: A sandboxed app may be able to execute arbitrary code with
kernel privileges
Description: A race condition was addressed with improved state
management.
CVE-2026-84607: Ruslan Dautov

Bluetooth
Available for: Apple Watch Series 9 and later
Impact: A remote attacker may be able to cause unexpected app
termination or arbitrary code execution
Description: An out-of-bounds write issue was addressed with improved
bounds checking.
CVE-2026-65414

Bluetooth
Available for: Apple Watch Series 9 and later
Impact: An app may gain unauthorized access to Bluetooth
Description: An authorization issue was addressed with improved state
management.
CVE-2026-84560: an anonymous researcher

CloudKit
Available for: Apple Watch Series 9 and later
Impact: A local app may be able to read a persistent account identifier
Description: An information disclosure issue was addressed with improved
state management.
CVE-2026-86895: Stanislav Jelezoglo

CloudKit
Available for: Apple Watch Series 9 and later
Impact: An app may be able to read device name
Description: A permissions issue was addressed with additional
restrictions.
CVE-2026-86893: Heiner Gerdes

copyfile
Available for: Apple Watch Series 9 and later
Impact: An archive may be able to bypass Gatekeeper
Description: A file quarantine bypass was addressed with additional
checks.
CVE-2026-65399: Rishabh Jain (rjcyber) of cyberplanet, Pasquale Scola,
an anonymous researcher

Core Bluetooth
Available for: Apple Watch Series 9 and later
Impact: An app may be able to access Bluetooth device information
Description: An authorization issue was addressed with improved state
management.
CVE-2026-86891: Dawuge of Shuffle Team

CoreMedia
Available for: Apple Watch Series 9 and later
Impact: A sandboxed process may be able to circumvent sandbox
restrictions
Description: An out-of-bounds write issue was addressed with improved
bounds checking.
CVE-2026-86876: Chris Bailey - Short Circuit

CoreMotion
Available for: Apple Watch Series 9 and later
Impact: An app may be able to access motion data from headphones without
user consent
Description: An authorization issue was addressed with improved
validation.
CVE-2026-43737: Stuart Wallace

CoreText
Available for: Apple Watch Series 9 and later
Impact: Processing web content may lead to a denial-of-service
Description: A null pointer dereference was addressed with improved
input validation.
CVE-2026-65412: Pavan Nallamothu

CoreText
Available for: Apple Watch Series 9 and later
Impact: Processing a maliciously crafted font may result in the
disclosure of process memory
Description: An out-of-bounds read was addressed with improved bounds
checking.
CVE-2026-84596: ret2happy, Meta Product Security

CoreUI
Available for: Apple Watch Series 9 and later
Impact: Processing a maliciously crafted file may lead to unexpected app
termination
Description: An out-of-bounds write issue was addressed with improved
bounds checking.
CVE-2026-84575: Mustafa Calap (@ordinal0, dbg.re)

CoreUI
Available for: Apple Watch Series 9 and later
Impact: Processing a maliciously crafted image may lead to unexpected
app termination
Description: A buffer overflow was addressed with improved bounds
checking.
CVE-2026-84571: stratan (@5tratan), Peter Malone

CoreUI
Available for: Apple Watch Series 9 and later
Impact: Processing a maliciously crafted asset catalog may lead to
unexpected process termination
Description: An out-of-bounds write issue was addressed with improved
bounds checking.
CVE-2026-84511: Rahul Raj, stratan (@5tratan)

DeviceCheck
Available for: Apple Watch Series 9 and later
Impact: An app may be able to read persistent device identifiers
Description: An authorization issue was addressed with improved access
control.
CVE-2026-84612: N.M.Praveen Nawarathne (@zblockrat), James Gill
(@jjtech@infosec.exchange)

FontParser
Available for: Apple Watch...