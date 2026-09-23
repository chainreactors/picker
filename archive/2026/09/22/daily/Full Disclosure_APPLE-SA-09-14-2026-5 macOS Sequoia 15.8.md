---
title: APPLE-SA-09-14-2026-5 macOS Sequoia 15.8
url: https://seclists.org/fulldisclosure/2026/Sep/57
source: Full Disclosure
date: 2026-09-22
fetch_date: 2026-09-23T06:55:25.113248
---

# APPLE-SA-09-14-2026-5 macOS Sequoia 15.8

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

[![Previous](/images/left-icon-16x16.png)](56)
[By Date](date.html#57)
[![Next](/images/right-icon-16x16.png)](58)

[![Previous](/images/left-icon-16x16.png)](56)
[By Thread](index.html#57)
[![Next](/images/right-icon-16x16.png)](58)

![](/shared/images/nst-icons.svg#search)

# APPLE-SA-09-14-2026-5 macOS Sequoia 15.8

---

*From*: Apple Product Security via Fulldisclosure <fulldisclosure () seclists org>
*Date*: Mon, 14 Sep 2026 15:07:43 -0700

---

```
-----BEGIN PGP SIGNED MESSAGE-----
Hash: SHA256

APPLE-SA-09-14-2026-5 macOS Sequoia 15.8

macOS Sequoia 15.8 addresses the following issues.
Information about the security content is also available at
https://support.apple.com/149043.

Apple maintains a Security Releases page at
https://support.apple.com/100100 which lists recent
software updates with security advisories.

Accelerate Framework
Available for: macOS Sequoia
Impact: Processing a maliciously crafted image may lead to unexpected
process termination
Description: An out-of-bounds write issue was addressed with improved
bounds checking.
CVE-2026-86882: Peter Malone

Accessibility
Available for: macOS Sequoia
Impact: An app may be able to access sensitive user data
Description: This issue was addressed with improved data protection.
CVE-2026-43664: Stuart Wallace, Rosyna Keller of Totally Not Malicious
Software, Jian Lee (@speedyfriend433), Ilya Andr (andrd3v), Gongyu Ma
(@Mezone0), David Strnadel, Daniel Febrero, CJ Vana, Asaf Cohen

APFS
Available for: macOS Sequoia
Impact: An application may be able to access restricted files
Description: A permissions issue was addressed with improved path
validation.
CVE-2026-86910: an anonymous researcher

APFS
Available for: macOS Sequoia
Impact: An app may be able to cause unexpected system termination or
write kernel memory
Description: An out-of-bounds write issue was addressed with improved
bounds checking.
CVE-2026-84523: Cem Onat Karagun, an anonymous researcher

AppKit
Available for: macOS Sequoia
Impact: An app may be able to access protected user data
Description: A permissions issue was addressed with additional
restrictions.
CVE-2026-84587: an anonymous researcher

Apple Account
Available for: macOS Sequoia
Impact: An app may be able to use the Sign In With Apple authentication
flow to access the user's Apple Account
Description: An authentication issue was addressed with improved state
management.
CVE-2026-20683: Lehan Dilusha Jayasingha (Sri Lanka), Jasminder Pal
Singh, Dem0ns (@天府简易信工作室), Abdelhak Kherroubi

Apple Neural Engine
Available for: macOS Sequoia
Impact: An app may be able to cause unexpected system termination
Description: An integer overflow was addressed with improved input
validation.
CVE-2026-65408: tamdao

AppleAVD
Available for: macOS Sequoia
Impact: An app may be able to cause unexpected system termination
Description: A use after free issue was addressed with improved memory
management.
CVE-2026-65407: Franco Belman at Blackwing Intelligence

AppleDouble
Available for: macOS Sequoia
Impact: Mounting a disk image with maliciously crafted files may lead to
unexpected system termination
Description: An out-of-bounds write issue was addressed with improved
bounds checking.
CVE-2026-84519: Richard Zana

AppleMobileFileIntegrity
Available for: macOS Sequoia
Impact: A malicious app may be able to break out of its sandbox
Description: A validation issue existed in the entitlement verification.
This issue was addressed with improved validation of the process
entitlement.
CVE-2026-65381: Mickey Jin (@patch1t)

ATS
Available for: macOS Sequoia
Impact: An app may be able to read files outside of its sandbox
Description: A permissions issue was addressed by removing the
vulnerable code.
CVE-2026-43763: Pavan Nallamothu, Jared Reyes

ATS
Available for: macOS Sequoia
Impact: An app may be able to access user-sensitive data
Description: A logging issue was addressed with improved data redaction.
CVE-2026-84525: D4rthL

ATS
Available for: macOS Sequoia
Impact: An app may be able to access sensitive user data
Description: A permissions issue was addressed with improved validation.
CVE-2026-65342: Mohamad Dawoud / Abodi Dawoud, Ahmed Alwardani

Audio
Available for: macOS Sequoia
Impact: An app may be able to leak sensitive user information
Description: A logic issue was addressed with improved checks.
CVE-2026-65339: Mustafa Calap (@ordinal0, dbg.re), Meta Red Team X - Nik
Tsytsarkin

AuthKit
Available for: macOS Sequoia
Impact: A local app may be able to read a persistent account identifier
Description: A permissions issue was addressed with additional
restrictions.
CVE-2026-84583: Zhongcheng Li from IES Red Team

autofs
Available for: macOS Sequoia
Impact: An attacker with control of a network directory server may be
able to execute arbitrary code with root privileges
Description: A path traversal issue was addressed with improved path
validation.
CVE-2026-84568: Mr.Gedik (@h4ck2s3c) of Turkish Technology

autofs
Available for: macOS Sequoia
Impact: An app may be able to bypass Gatekeeper checks
Description: A logic issue was addressed with improved checks.
CVE-2026-84570: Mr.Gedik (@h4ck2s3c)

Automator
Available for: macOS Sequoia
Impact: An app may be able to break out of its sandbox
Description: An authorization issue was addressed with improved state
management.
CVE-2026-84535: Sindre Sorhus, Oren Yomtov, Morris Richman
(@morrisinlife), Kun Peeks (@SwayZGl1tZyyy)

AVEVideoEncoder
Available for: macOS Sequoia
Impact: An app may be able to cause unexpected system termination
Description: A type confusion issue was addressed with improved memory
handling.
CVE-2026-84616: Peter Malone

AVEVideoEncoder
Available for: macOS Sequoia
Impact: A sandboxed app may be able to execute arbitrary code with
kernel privileges
Description: A race condition was addressed with improved state
management.
CVE-2026-84607: Ruslan Dautov

BackgroundAssets
Available for: macOS Sequoia
Impact: An app may be able to access sensitive user data
Description: A logic issue was addressed with improved validation.
CVE-2026-65406: Ye Zhang (@VAR10CK) of Baidu Security

Bluetooth
Available for: macOS Sequoia
Impact: A remote attacker may be able to cause unexpected app
termination or arbitrary code execution
Description: An out-of-bounds write issue was addressed with improved
bounds checking.
CVE-2026-65414

cd9660
Available for: macOS Sequoia
Impact: An app may be able to cause unexpected system termination
Description: The issue was addressed with improved memory handling.
CVE-2026-84567: Sanny Mitra, Sihyun Roh (Compsec, SNU), ngockhanh from
Cystack, 정우 하 (@0xfa11babe), Suresh Sundaram, Surej Sekhar, Kun Peeks
(@SwayZGl1tZyyy), Hari Shanmugam (The Hxr1), Ataberk Yavuzer

copyfile
Available for: macOS Sequoia
Impact: An archive may be able to bypass Gatekeeper
Description: A file quarantine bypass was addressed with additional
checks.
CVE-2026-65399: Rishabh Jain (rjcyber) of cyberplanet, Pasquale Scola,
an anonymous researcher

Core Bluetooth
Available for: macOS Sequoia
Impact: An app may be able to access Bluetooth device information
Description: An authorization issue was addressed with improved state
management.
CVE-2026-86891: Dawuge of Shuffle Team

CoreDrag
Available for: macOS Sequoia
Impact: An app may be able to cause unexpected process termination or
disclose process memory
Description: An out-of-bounds read was addressed with improved bounds
checking.
CVE-2026-43683: Nathaniel Oh (@calysteon)

CoreMedia
Available for...