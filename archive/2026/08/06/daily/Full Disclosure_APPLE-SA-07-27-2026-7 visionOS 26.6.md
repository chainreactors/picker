---
title: APPLE-SA-07-27-2026-7 visionOS 26.6
url: https://seclists.org/fulldisclosure/2026/Aug/22
source: Full Disclosure
date: 2026-08-06
fetch_date: 2026-08-07T04:30:14.877752
---

# APPLE-SA-07-27-2026-7 visionOS 26.6

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

[![Previous](/images/left-icon-16x16.png)](21)
[By Date](date.html#22)
[![Next](/images/right-icon-16x16.png)](23)

[![Previous](/images/left-icon-16x16.png)](21)
[By Thread](index.html#22)
[![Next](/images/right-icon-16x16.png)](23)

![](/shared/images/nst-icons.svg#search)

# APPLE-SA-07-27-2026-7 visionOS 26.6

---

*From*: Apple Product Security via Fulldisclosure <fulldisclosure () seclists org>
*Date*: Mon, 27 Jul 2026 17:27:26 -0700

---

```
-----BEGIN PGP SIGNED MESSAGE-----
Hash: SHA256

APPLE-SA-07-27-2026-7 visionOS 26.6

visionOS 26.6 addresses the following issues.
Information about the security content is also available at
https://support.apple.com/en-us/128070.

Apple maintains a Security Releases page at
https://support.apple.com/100100 which lists recent
software updates with security advisories.

Accounts Framework
Available for: Apple Vision Pro (all models)
Impact: An app may be able to fingerprint the user
Description: This issue was addressed with improved data protection.
CVE-2026-64733: Rosyna Keller of Totally Not Malicious Software
(paradisefacade.com)

App Store
Available for: Apple Vision Pro (all models)
Impact: An app may be able to access sensitive user data
Description: This issue was addressed with improved checks.
CVE-2026-43801: Rahul Raj

Audio
Available for: Apple Vision Pro (all models)
Impact: An app may be able to cause a denial-of-service
Description: An out-of-bounds write issue was addressed with improved
bounds checking.
CVE-2026-64725: Seonung Park, ALTV!ST (altvi.st/)

AuthKit
Available for: Apple Vision Pro (all models)
Impact: An app may be able to fingerprint the user
Description: A permissions issue was addressed with additional
restrictions.
CVE-2026-43730: David Strnadel

AVEVideoEncoder
Available for: Apple Vision Pro (all models)
Impact: An app may be able to execute arbitrary code with kernel
privileges
Description: A buffer overflow was addressed with improved size
validation.
CVE-2026-64747: Franco Belman at Blackwing Intelligence

BackgroundAssets
Available for: Apple Vision Pro (all models)
Impact: An app may be able to delete files for which it does not have
permission
Description: A permissions issue was addressed with improved validation.
CVE-2026-64707: YingQi Shi (@Mas0nShi) of DBAppSecurity's WeBin lab

CloudAttestation
Available for: Apple Vision Pro (all models)
Impact: A maliciously crafted app may be able to bypass code signing
enforcement
Description: A validation issue was addressed with improved input
sanitization.
CVE-2026-43813: Anton Pakhunov

Contacts
Available for: Apple Vision Pro (all models)
Impact: An app may be able to add contacts without user authorization
Description: An authorization issue was addressed with improved
validation.
CVE-2026-64746: Rodolphe BRUNETTI (@eisw0lf) of Lupus Nova, Daniel
Febrero

Contacts
Available for: Apple Vision Pro (all models)
Impact: Processing a maliciously crafted contact may leak sensitive data
Description: The issue was addressed with improved checks.
CVE-2026-64734: Daniel Williams

CoreAudio
Available for: Apple Vision Pro (all models)
Impact: Processing a maliciously crafted audio file may corrupt process
memory
Description: The issue was addressed with improved memory handling.
CVE-2026-43673: Anonymous working with TrendAI Zero Day Initiative

CoreAudio
Available for: Apple Vision Pro (all models)
Impact: Processing an audio stream in a maliciously crafted media file
may terminate the process
Description: An out-of-bounds write issue was addressed with improved
bounds checking.
CVE-2026-43744: Mathis Mansière, an anonymous researcher

CoreAudio
Available for: Apple Vision Pro (all models)
Impact: A remote attacker may be able to cause unexpected system
termination
Description: An out-of-bounds write issue was addressed with improved
bounds checking.
CVE-2026-43803: Rahul Raj

CoreMedia
Available for: Apple Vision Pro (all models)
Impact: Processing a maliciously crafted video file may lead to
unexpected app termination
Description: A memory corruption issue was addressed with improved
memory handling.
CVE-2026-43711: James Duffy (@0x4A616D657344)

Foundation
Available for: Apple Vision Pro (all models)
Impact: A malicious app may be able to access protected user data
Description: The issue was addressed with improved input sanitization.
CVE-2026-43714: an anonymous researcher

FrontBoard
Available for: Apple Vision Pro (all models)
Impact: An app may be able to access sensitive user data
Description: This issue was addressed by using HTTPS when sending
information over the network.
CVE-2026-64742: Huỳnh Tấn Ngàn

Game Center
Available for: Apple Vision Pro (all models)
Impact: An app may be able to access sensitive user data
Description: This issue was addressed with improved data protection.
CVE-2026-43796: Ilya Andr (andrd3v) of Positive Technologies, Stanislav
Jelezoglo

Heimdal
Available for: Apple Vision Pro (all models)
Impact: An app may be able to cause a denial-of-service
Description: An out-of-bounds read was addressed with improved bounds
checking.
CVE-2026-64692: Redon Gashi

ImageIO
Available for: Apple Vision Pro (all models)
Impact: Processing a maliciously crafted texture may lead to unexpected
app termination
Description: An integer overflow was addressed with improved input
validation.
CVE-2026-43780: Michael DePlante (@izobashi) of TrendAI Zero Day
Initiative

ImageIO
Available for: Apple Vision Pro (all models)
Impact: Processing a maliciously crafted image may corrupt process
memory
Description: The issue was addressed with improved memory handling.
CVE-2026-64716: Arni Hardarson, Jonathan Alush-Aben, Peter Malone

ImageIO
Available for: Apple Vision Pro (all models)
Impact: Processing a maliciously crafted file may lead to unexpected app
termination
Description: The issue was addressed with improved bounds checks.
CVE-2026-64758: 진규정 (Gyujeong Jin, @G1uN4sh)

ImageIO
Available for: Apple Vision Pro (all models)
Impact: Processing a maliciously crafted file may lead to a
denial-of-service
Description: An out-of-bounds write issue was addressed with improved
bounds checking.
CVE-2026-64754: PETOWORKS의 Bugeun Choi (@Bugeun), Rahul Raj

ImageIO
Available for: Apple Vision Pro (all models)
Impact: Processing a maliciously crafted image may lead to a
denial-of-service
Description: A type confusion issue was addressed with improved checks.
CVE-2026-64693: Geonha Lee (@leegn4a)

Kernel
Available for: Apple Vision Pro (all models)
Impact: An app may be able to cause unexpected system termination or
corrupt kernel memory
Description: The issue was addressed with improved memory handling.
CVE-2026-64749: Billy Jheng Bing Jhong and Pan Zhenpeng (@Peterpan0927)
of STAR Labs SG Pte. Ltd., Ashish Kunwar, Hiroki Imai (LAC Co., Ltd.),
hxr1

Kernel
Available for: Apple Vision Pro (all models)
Impact: An app may be able to cause unexpected system termination or
corrupt kernel memory
Description: A use after free issue was addressed with improved memory
management.
CVE-2026-43778: f0r of MurphySec, Feng Xue and XGPT of ThreatBook,
Mahmoud Abdelmoniem, an anonymous researcher, Wang Yu, Lyutoon, Hiroki
Imai (LAC Co., Ltd.), DARKNAVY (@DarkNavyOrg), Fábio Luís @scanpt,
Nicolas Rabrenovic

Kernel
Available for: Apple Vision Pro (all models)
Impact: An app may be able to disclose kernel memory
Description: The issue was addressed with improved memory handling.
CVE-2026-64709: Pasquale Scola, Billy Jheng Bing Jhong and Pan Zhenpeng
(@Peterpan0927...