---
title: APPLE-SA-05-11-2026-2 iOS 18.7.9 and iPadOS 18.7.9
url: https://seclists.org/fulldisclosure/2026/May/6
source: Full Disclosure
date: 2026-05-17
fetch_date: 2026-05-18T06:10:48.792350
---

# APPLE-SA-05-11-2026-2 iOS 18.7.9 and iPadOS 18.7.9

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

[![Previous](/images/left-icon-16x16.png)](5)
[By Date](date.html#6)
[![Next](/images/right-icon-16x16.png)](8)

[![Previous](/images/left-icon-16x16.png)](5)
[By Thread](index.html#6)
[![Next](/images/right-icon-16x16.png)](8)

![](/shared/images/nst-icons.svg#search)

# APPLE-SA-05-11-2026-2 iOS 18.7.9 and iPadOS 18.7.9

---

*From*: Apple Product Security via Fulldisclosure <fulldisclosure () seclists org>
*Date*: Mon, 11 May 2026 15:29:27 -0700

---

```
-----BEGIN PGP SIGNED MESSAGE-----
Hash: SHA256

APPLE-SA-05-11-2026-2 iOS 18.7.9 and iPadOS 18.7.9

iOS 18.7.9 and iPadOS 18.7.9 addresses the following issues.
Information about the security content is also available at
https://support.apple.com/en-us/127111.

Apple maintains a Security Releases page at
https://support.apple.com/100100 which lists recent
software updates with security advisories.

Accounts
Available for: iPhone XS, iPhone XS Max, iPhone XR, iPad 7th generation
Impact: An app may be able to access sensitive user data
Description: An authorization issue was addressed with improved state
management.
CVE-2026-28877: Rosyna Keller of Totally Not Malicious Software

APFS
Available for: iPhone XS, iPhone XS Max, iPhone XR, iPad 7th generation
Impact: An app may be able to cause unexpected system termination
Description: A buffer overflow was addressed with improved bounds
checking.
CVE-2026-28959: Dave G.

App Intents
Available for: iPhone XS, iPhone XS Max, iPhone XR, iPad 7th generation
Impact: A malicious app may be able to break out of its sandbox
Description: A logic issue was addressed with improved restrictions.
CVE-2026-28995: Vamshi Paili, Tony Gorez (@tonygo_) for Reverse Society

Audio
Available for: iPhone XS, iPhone XS Max, iPhone XR, iPad 7th generation
Impact: Processing an audio stream in a maliciously crafted media file
may terminate the process
Description: The issue was addressed with improved memory handling.
CVE-2026-39869: David Ige of Beryllium Security

Calendar
Available for: iPhone XS, iPhone XS Max, iPhone XR, iPad 7th generation
Impact: A remote attacker may be able to cause a denial-of-service
Description: A resource exhaustion issue was addressed with improved
input validation.
CVE-2026-28872: Alvin Aries Tapia

Calling Framework
Available for: iPhone XS, iPhone XS Max, iPhone XR, iPad 7th generation
Impact: A remote attacker may be able to cause a denial-of-service
Description: A denial-of-service issue was addressed with improved input
validation.
CVE-2026-28894: an anonymous researcher

CoreServices
Available for: iPhone XS, iPhone XS Max, iPhone XR, iPad 7th generation
Impact: Processing a maliciously crafted file may lead to unexpected app
termination
Description: The issue was addressed with improved checks.
CVE-2026-28936: Andreas Jaegersberger & Ro Achterberg of Nosebeard Labs

FileProvider
Available for: iPhone XS, iPhone XS Max, iPhone XR, iPad 7th generation
Impact: An app may be able to access sensitive user data
Description: A race condition was addressed with additional validation.
CVE-2026-43659: Alex Radocea

GeoServices
Available for: iPhone XS, iPhone XS Max, iPhone XR, iPad 7th generation
Impact: An app may be able to access sensitive user data
Description: An information leakage was addressed with additional
validation.
CVE-2026-28870: XiguaSec

ImageIO
Available for: iPhone XS, iPhone XS Max, iPhone XR, iPad 7th generation
Impact: Processing a maliciously crafted file may lead to unexpected app
termination
Description: The issue was addressed with improved bounds checks.
CVE-2026-28977: Suresh Sundaram

IOHIDFamily
Available for: iPhone XS, iPhone XS Max, iPhone XR, iPad 7th generation
Impact: An attacker may be able to cause unexpected app termination
Description: A memory corruption vulnerability was addressed with
improved locking.
CVE-2026-28992: Johnny Franks (@zeroxjf)

IOHIDFamily
Available for: iPhone XS, iPhone XS Max, iPhone XR, iPad 7th generation
Impact: An app may be able to determine kernel memory layout
Description: A logging issue was addressed with improved data redaction.
CVE-2026-28943: Google Threat Analysis Group

IOKit
Available for: iPhone XS, iPhone XS Max, iPhone XR, iPad 7th generation
Impact: An app may be able to cause unexpected system termination
Description: A use after free issue was addressed with improved memory
management.
CVE-2026-28969: Mihalis Haatainen, Ari Hawking, Ashish Kunwar

Kernel
Available for: iPhone XS, iPhone XS Max, iPhone XR, iPad 7th generation
Impact: An app may be able to disclose kernel memory
Description: The issue was addressed with improved memory handling.
CVE-2026-43654: Vaagn Vardanian, Nathaniel Oh (@calysteon)

Kernel
Available for: iPhone XS, iPhone XS Max, iPhone XR, iPad 7th generation
Impact: A maliciously crafted disk image may bypass Gatekeeper checks
Description: A file quarantine bypass was addressed with additional
checks.
CVE-2026-28954: Yiğit Can YILMAZ (@yilmazcanyigit)

Kernel
Available for: iPhone XS, iPhone XS Max, iPhone XR, iPad 7th generation
Impact: A local user may be able to cause unexpected system termination
or read kernel memory
Description: A buffer overflow was addressed with improved input
validation.
CVE-2026-28897: Robert Tran, popku1337, Billy Jheng Bing Jhong and Pan
Zhenpeng (@Peterpan0927) of STAR Labs SG Pte. Ltd., Aswin kumar
Gokulakannan

Kernel
Available for: iPhone XS, iPhone XS Max, iPhone XR, iPad 7th generation
Impact: An app may be able to cause unexpected system termination
Description: An integer overflow was addressed with improved input
validation.
CVE-2026-28952: Calif.io in collaboration with Claude and Anthropic
Research

Kernel
Available for: iPhone XS, iPhone XS Max, iPhone XR, iPad 7th generation
Impact: An app may be able to gain root privileges
Description: An authorization issue was addressed with improved state
management.
CVE-2026-28951: Csaba Fitzl (@theevilbit) of Iru

Kernel
Available for: iPhone XS, iPhone XS Max, iPhone XR, iPad 7th generation
Impact: An app may be able to cause unexpected system termination or
write kernel memory
Description: An out-of-bounds write issue was addressed with improved
input validation.
CVE-2026-28972: Billy Jheng Bing Jhong and Pan Zhenpeng (@Peterpan0927)
of STAR Labs SG Pte. Ltd., Ryan Hileman via Xint Code (xint.io)

Kernel
Available for: iPhone XS, iPhone XS Max, iPhone XR, iPad 7th generation
Impact: An app may be able to cause unexpected system termination
Description: A race condition was addressed with additional validation.
CVE-2026-28986: Tristan Madani (@TristanInSec) from Talence Security,
Ryan Hileman via Xint Code (xint.io), Chris Betz

Kernel
Available for: iPhone XS, iPhone XS Max, iPhone XR, iPad 7th generation
Impact: An app may be able to leak sensitive kernel state
Description: A logging issue was addressed with improved data redaction.
CVE-2026-28987: Dhiyanesh Selvaraj (@redroot97)

LaunchServices
Available for: iPhone XS, iPhone XS Max, iPhone XR, iPad 7th generation
Impact: A remote attacker may be able to cause a denial of service
Description: A type confusion issue was addressed with improved checks.
CVE-2026-28983: Ruslan Dautov

libxpc
Available for: iPhone XS, iPhone XS Max, iPhone XR, iPad 7th generation
Impact: An app may be able to enumerate a user's installed apps
Description: This issue was addressed with improved checks.
CVE-2026-28882: Ilya Andr (andrd3v), Ilias Morad (A2nkF) of Voynich
Group, Duy Trần (@khanhduytran0), @hugeBlack

Mail Drafts
Available for: iP...