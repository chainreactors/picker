---
title: APPLE-SA-07-27-2026-6 watchOS 26.6
url: https://seclists.org/fulldisclosure/2026/Aug/21
source: Full Disclosure
date: 2026-08-06
fetch_date: 2026-08-07T04:30:24.040984
---

# APPLE-SA-07-27-2026-6 watchOS 26.6

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

[![Previous](/images/left-icon-16x16.png)](20)
[By Date](date.html#21)
[![Next](/images/right-icon-16x16.png)](22)

[![Previous](/images/left-icon-16x16.png)](20)
[By Thread](index.html#21)
[![Next](/images/right-icon-16x16.png)](22)

![](/shared/images/nst-icons.svg#search)

# APPLE-SA-07-27-2026-6 watchOS 26.6

---

*From*: Apple Product Security via Fulldisclosure <fulldisclosure () seclists org>
*Date*: Mon, 27 Jul 2026 17:27:00 -0700

---

```
-----BEGIN PGP SIGNED MESSAGE-----
Hash: SHA256

APPLE-SA-07-27-2026-6 watchOS 26.6

watchOS 26.6 addresses the following issues.
Information about the security content is also available at
https://support.apple.com/en-us/128068.

Apple maintains a Security Releases page at
https://support.apple.com/100100 which lists recent
software updates with security advisories.

Accounts Framework
Available for: Apple Watch Series 6 and later
Impact: An app may be able to fingerprint the user
Description: This issue was addressed with improved data protection.
CVE-2026-64733: Rosyna Keller of Totally Not Malicious Software
(paradisefacade.com)

App Store
Available for: Apple Watch Series 6 and later
Impact: An app may be able to access sensitive user data
Description: This issue was addressed with improved checks.
CVE-2026-43801: Rahul Raj

Apple Neural Engine
Available for: Apple Watch Series 6 and later
Impact: An app may be able to cause unexpected system termination
Description: A use after free issue was addressed with improved memory
management.
CVE-2026-28928: Dun

Audio
Available for: Apple Watch Series 6 and later
Impact: An app may be able to cause a denial-of-service
Description: An out-of-bounds write issue was addressed with improved
bounds checking.
CVE-2026-64725: Seonung Park, ALTV!ST (altvi.st/)

AuthKit
Available for: Apple Watch Series 6 and later
Impact: An app may be able to fingerprint the user
Description: A permissions issue was addressed with additional
restrictions.
CVE-2026-43730: David Strnadel

AVEVideoEncoder
Available for: Apple Watch Series 6 and later
Impact: An app may be able to execute arbitrary code with kernel
privileges
Description: A buffer overflow was addressed with improved size
validation.
CVE-2026-64747: Franco Belman at Blackwing Intelligence

CloudAttestation
Available for: Apple Watch Series 6 and later
Impact: A maliciously crafted app may be able to bypass code signing
enforcement
Description: A validation issue was addressed with improved input
sanitization.
CVE-2026-43813: Anton Pakhunov

Contacts
Available for: Apple Watch Series 6 and later
Impact: An app may be able to add contacts without user authorization
Description: An authorization issue was addressed with improved
validation.
CVE-2026-64746: Rodolphe BRUNETTI (@eisw0lf) of Lupus Nova, Daniel
Febrero

Contacts
Available for: Apple Watch Series 6 and later
Impact: Processing a maliciously crafted contact may leak sensitive data
Description: The issue was addressed with improved checks.
CVE-2026-64734: Daniel Williams

CoreAudio
Available for: Apple Watch Series 6 and later
Impact: Processing a maliciously crafted audio file may corrupt process
memory
Description: The issue was addressed with improved memory handling.
CVE-2026-43673: Anonymous working with TrendAI Zero Day Initiative

CoreAudio
Available for: Apple Watch Series 6 and later
Impact: Processing an audio stream in a maliciously crafted media file
may terminate the process
Description: An out-of-bounds write issue was addressed with improved
bounds checking.
CVE-2026-43744: Mathis Mansière, an anonymous researcher

CoreAudio
Available for: Apple Watch Series 6 and later
Impact: A remote attacker may be able to cause unexpected system
termination
Description: An out-of-bounds write issue was addressed with improved
bounds checking.
CVE-2026-43803: Rahul Raj

CoreMedia
Available for: Apple Watch Series 6 and later
Impact: Processing a maliciously crafted video file may lead to
unexpected app termination
Description: A memory corruption issue was addressed with improved
memory handling.
CVE-2026-43711: James Duffy (@0x4A616D657344)

CoreMedia
Available for: Apple Watch Series 6 and later
Impact: An app may be able to access sensitive user data
Description: An authorization issue was addressed with improved state
management.
CVE-2026-43759: 이재영, Rajdip Dey Sarkar, Arni Hardarson (Neonix Security)

curl
Available for: Apple Watch Series 6 and later
Impact: Authentication credentials may be sent to a server on another
origin
Description: This is a vulnerability in open source code and Apple
Software is among the affected projects. The CVE-ID was assigned by a
third party. Learn more about the issue and CVE-ID at cve.org.
CVE-2026-3784
CVE-2026-3783

Data Detectors UI
Available for: Apple Watch Series 6 and later
Impact: An app may be able to access sensitive user data
Description: An authorization issue was addressed with improved state
management.
CVE-2026-43758: HvxyZLF

Foundation
Available for: Apple Watch Series 6 and later
Impact: A malicious app may be able to access protected user data
Description: The issue was addressed with improved input sanitization.
CVE-2026-43714: an anonymous researcher

FrontBoard
Available for: Apple Watch Series 6 and later
Impact: An app may be able to access sensitive user data
Description: This issue was addressed by using HTTPS when sending
information over the network.
CVE-2026-64742: Huỳnh Tấn Ngàn

Game Center
Available for: Apple Watch Series 6 and later
Impact: An app may be able to access sensitive user data
Description: This issue was addressed with improved data protection.
CVE-2026-43796: Ilya Andr (andrd3v) of Positive Technologies, Stanislav
Jelezoglo

Heimdal
Available for: Apple Watch Series 6 and later
Impact: An app may be able to cause a denial-of-service
Description: An out-of-bounds read was addressed with improved bounds
checking.
CVE-2026-64692: Redon Gashi

ImageIO
Available for: Apple Watch Series 6 and later
Impact: Processing a maliciously crafted texture may lead to unexpected
app termination
Description: An integer overflow was addressed with improved input
validation.
CVE-2026-43780: Michael DePlante (@izobashi) of TrendAI Zero Day
Initiative

ImageIO
Available for: Apple Watch Series 6 and later
Impact: Processing a maliciously crafted image may corrupt process
memory
Description: The issue was addressed with improved memory handling.
CVE-2026-64716: Arni Hardarson, Jonathan Alush-Aben, Peter Malone

ImageIO
Available for: Apple Watch Series 6 and later
Impact: Processing a maliciously crafted file may lead to unexpected app
termination
Description: The issue was addressed with improved bounds checks.
CVE-2026-64758: 진규정 (Gyujeong Jin, @G1uN4sh)

ImageIO
Available for: Apple Watch Series 6 and later
Impact: Processing a maliciously crafted file may lead to a
denial-of-service
Description: An out-of-bounds write issue was addressed with improved
bounds checking.
CVE-2026-64754: PETOWORKS의 Bugeun Choi (@Bugeun), Rahul Raj

ImageIO
Available for: Apple Watch Series 6 and later
Impact: Processing a maliciously crafted image may lead to a
denial-of-service
Description: A type confusion issue was addressed with improved checks.
CVE-2026-64693: Geonha Lee (@leegn4a)

IOGPUFamily
Available for: Apple Watch Series 6 and later
Impact: An app may be able to cause unexpected system termination
Description: A race condition was addressed with improved state
handling.
CVE-2026-43743: Lyutoon, Dun

IOKit
Available for...