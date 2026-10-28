---
title: APPLE-SA-10-26-2026-7 tvOS 27.2
url: https://seclists.org/fulldisclosure/2026/Oct/44
source: Full Disclosure
date: 2026-10-27
fetch_date: 2026-10-28T07:49:41.044369
---

# APPLE-SA-10-26-2026-7 tvOS 27.2

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

[![Previous](/images/left-icon-16x16.png)](43)
[By Date](date.html#44)
[![Next](/images/right-icon-16x16.png)](45)

[![Previous](/images/left-icon-16x16.png)](43)
[By Thread](index.html#44)
[![Next](/images/right-icon-16x16.png)](45)

![](/shared/images/nst-icons.svg#search)

# APPLE-SA-10-26-2026-7 tvOS 27.2

---

*From*: Apple Product Security via Fulldisclosure <fulldisclosure () seclists org>
*Date*: Mon, 26 Oct 2026 14:42:13 -0700

---

```
-----BEGIN PGP SIGNED MESSAGE-----
Hash: SHA256

APPLE-SA-10-26-2026-7 tvOS 27.2

tvOS 27.2 addresses the following issues.
Information about the security content is also available at
https://support.apple.com/149524.

Apple maintains a Security Releases page at
https://support.apple.com/100100 which lists recent
software updates with security advisories.

Accounts
Available for: Apple TV 4K 2nd generation and later
Impact: A malicious application may be able to bypass Privacy
preferences
Description: A logging issue was addressed with improved data redaction.
CVE-2026-113898: Bhaswanth Chigurupati

Accounts
Available for: Apple TV 4K 2nd generation and later
Impact: An app may be able to access sensitive user data
Description: This issue was addressed with additional entitlement
checks.
CVE-2026-112446: LiangWei, Sindre Sorhus

App Intents
Available for: Apple TV 4K 2nd generation and later
Impact: An app may be able to access sensitive user data
Description: This issue was addressed with additional entitlement
checks.
CVE-2026-112692: Huy Nguyen (@34306) of Calif.io

AppleAVD
Available for: Apple TV 4K 2nd generation and later
Impact: Processing a maliciously crafted video file may lead to
unexpected app termination
Description: An out-of-bounds write issue was addressed with improved
bounds checking.
CVE-2026-112416: an anonymous researcher, Dohyeon An @PILAB Technology,
Inc, Hcamael and 章鱼哥@aipy (aipyaipy.com), Narendra Singh (@_3P1C), Meta
Red Team X - Nik Tsytsarkin

AppleAVD
Available for: Apple TV 4K 2nd generation and later
Impact: Processing a maliciously crafted video file may lead to
unexpected app termination or corrupt process memory
Description: The issue was addressed with improved memory handling.
CVE-2026-112454: @Licht_jb, Hcamael and 章鱼哥@aipy (aipyaipy.com)

Audio
Available for: Apple TV 4K 2nd generation and later
Impact: Processing a maliciously crafted file may lead to unexpected app
termination
Description: An out-of-bounds read was addressed with improved bounds
checking.
CVE-2026-112546: lunar815, Surej Sekhar, Piotr Jerzy Duszynski, r3pwnx
(@r3pwnx), an anonymous researcher, Lily Cohl (@GenericCoding),
Nathaniel Oh (@calysteon)

AVEVideoEncoder
Available for: Apple TV 4K 2nd generation and later
Impact: An app may be able to cause unexpected system termination
Description: An out-of-bounds write issue was addressed with improved
bounds checking.
CVE-2026-112705: Marco Schmitt, Andrey Chernykh, Josh Maine of Calif.io

AVEVideoEncoder
Available for: Apple TV 4K 2nd generation and later
Impact: An app may be able to cause unexpected system termination or
corrupt kernel memory
Description: An out-of-bounds write issue was addressed with improved
input validation.
CVE-2026-112689: Franco Belman at Blackwing Intelligence

AVEVideoEncoder
Available for: Apple TV 4K 2nd generation and later
Impact: An app may be able to cause unexpected system termination or
corrupt kernel memory
Description: An out-of-bounds write issue was addressed with improved
bounds checking.
CVE-2026-112470: Hcamael and 章鱼哥@aipy (aipyaipy.com)
CVE-2026-112469: Hcamael and 章鱼哥@aipy (aipyaipy.com)
CVE-2026-112468: Hcamael and 章鱼哥@aipy (aipyaipy.com)

AVEVideoEncoder
Available for: Apple TV 4K 2nd generation and later
Impact: An app may be able to cause unexpected system termination or
read kernel memory
Description: An out-of-bounds read was addressed with improved input
validation.
CVE-2026-112466: Hcamael and 章鱼哥@aipy (aipyaipy.com)

Bluetooth
Available for: Apple TV 4K 2nd generation and later
Impact: An attacker in physical proximity may be able to cause a
denial-of-service
Description: A null pointer dereference was addressed with improved
validation.
CVE-2026-112566: Chris Bailey - Short Circuit

ColorSync
Available for: Apple TV 4K 2nd generation and later
Impact: Processing a maliciously crafted image may result in disclosure
of process memory
Description: The issue was addressed with improved checks.
CVE-2026-86988: Mateusz Jurczyk of Google Project Zero, Meta Red Team X
- - Nik Tsytsarkin

Compression
Available for: Apple TV 4K 2nd generation and later
Impact: An app may be able to disclose kernel memory
Description: A memory initialization issue was addressed with improved
memory handling.
CVE-2026-113910: Tucker Willenborg

CoreAudio
Available for: Apple TV 4K 2nd generation and later
Impact: Processing a maliciously crafted media file may lead to
unexpected app termination or corrupt process memory
Description: An out-of-bounds access issue was addressed with improved
bounds checking.
CVE-2026-113912: an anonymous researcher, 章鱼哥@aipy (aipyaipy.com), Roman
Zabicki, Anna Groza (@pwnlambda) of Calif.io

CoreAudio
Available for: Apple TV 4K 2nd generation and later
Impact: An app may be able to cause unexpected system termination or
corrupt process memory
Description: A buffer overflow issue was addressed with improved memory
handling.
CVE-2026-113907: Meta Red Team X - Nik Tsytsarkin

CoreAudio
Available for: Apple TV 4K 2nd generation and later
Impact: Processing a maliciously crafted audio file may lead to memory
corruption
Description: A buffer overflow was addressed with improved size
validation.
CVE-2026-86972: an anonymous researcher, Meta Product Security

CoreAudio
Available for: Apple TV 4K 2nd generation and later
Impact: An attacker in radio range may be able to cause unexpected
system termination
Description: A heap buffer overflow was addressed with improved bounds
checking.
CVE-2026-112638: Përparim Mjeku, Altin Gashi, Altin Gashi

CoreGraphics
Available for: Apple TV 4K 2nd generation and later
Impact: Processing a maliciously crafted font may lead to unexpected app
termination or corrupt process memory
Description: An out-of-bounds write issue was addressed with improved
bounds checking.
CVE-2026-113950: Substrate, Stefan Esser (Calif)

CoreMedia
Available for: Apple TV 4K 2nd generation and later
Impact: Processing a maliciously crafted video file may lead to
unexpected app termination
Description: The issue was addressed with improved memory handling.
CVE-2026-86992: Niels Hofmans

CoreMedia
Available for: Apple TV 4K 2nd generation and later
Impact: An app may be able to access sensitive user data
Description: A permissions issue was addressed with additional
restrictions.
CVE-2026-112706: Adriatik Raci, Rodolphe BRUNETTI (@eisw0lf) of Lupus
Nova, Chris Bailey - Short Circuit

CoreText
Available for: Apple TV 4K 2nd generation and later
Impact: Processing a maliciously crafted font may result in the
disclosure of process memory
Description: An out-of-bounds read was addressed with improved bounds
checking.
CVE-2026-112656: Nurihan Kim (HanTul) working with TrendAI Zero Day
Initiative

FontParser
Available for: Apple TV 4K 2nd generation and later
Impact: Processing a maliciously crafted font may result in the
disclosure of process memory
Description: An out-of-bounds read was addressed with improved input
validation.
CVE-2026-86970: Hcamael and 章鱼哥@aipy (aipyaipy.com)

FontParser
Available for: Apple TV 4K...