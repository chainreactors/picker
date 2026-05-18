---
title: APPLE-SA-05-11-2026-11 visionOS 26.5
url: https://seclists.org/fulldisclosure/2026/May/15
source: Full Disclosure
date: 2026-05-17
fetch_date: 2026-05-18T06:10:46.137641
---

# APPLE-SA-05-11-2026-11 visionOS 26.5

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

[![Previous](/images/left-icon-16x16.png)](14)
[By Date](date.html#15)
[![Next](/images/right-icon-16x16.png)](16)

[![Previous](/images/left-icon-16x16.png)](14)
[By Thread](index.html#15)
[![Next](/images/right-icon-16x16.png)](16)

![](/shared/images/nst-icons.svg#search)

# APPLE-SA-05-11-2026-11 visionOS 26.5

---

*From*: Apple Product Security via Fulldisclosure <fulldisclosure () seclists org>
*Date*: Mon, 11 May 2026 15:35:21 -0700

---

```
-----BEGIN PGP SIGNED MESSAGE-----
Hash: SHA256

APPLE-SA-05-11-2026-11 visionOS 26.5

visionOS 26.5 addresses the following issues.
Information about the security content is also available at
https://support.apple.com/en-us/127120.

Apple maintains a Security Releases page at
https://support.apple.com/100100 which lists recent
software updates with security advisories.

Accelerate
Available for: Apple Vision Pro (all models)
Impact: An app may be able to cause a denial-of-service
Description: An out-of-bounds read was addressed with improved bounds
checking.
CVE-2026-28991: Seiji Sakurai (@HeapSmasher)

Accounts
Available for: Apple Vision Pro (all models)
Impact: An app may be able to bypass certain Privacy preferences
Description: A permissions issue was addressed with additional
restrictions.
CVE-2026-28988: Asaf Cohen

APFS
Available for: Apple Vision Pro (all models)
Impact: An app may be able to cause unexpected system termination
Description: A buffer overflow was addressed with improved bounds
checking.
CVE-2026-28959: Dave G.

App Intents
Available for: Apple Vision Pro (all models)
Impact: A malicious app may be able to break out of its sandbox
Description: A logic issue was addressed with improved restrictions.
CVE-2026-28995: Vamshi Paili, Tony Gorez (@tonygo_) for Reverse Society

AppleJPEG
Available for: Apple Vision Pro (all models)
Impact: Processing a maliciously crafted image may lead to a
denial-of-service
Description: This is a vulnerability in open source code and Apple
Software is among the affected projects. The CVE-ID was assigned by a
third party. Learn more about the issue and CVE-ID at cve.org.
CVE-2026-1837

AppleJPEG
Available for: Apple Vision Pro (all models)
Impact: Processing a maliciously crafted media file may lead to
unexpected app termination or corrupt process memory
Description: A memory corruption issue was addressed with improved input
validation.
CVE-2026-28956: impost0r (ret2plt)

Audio
Available for: Apple Vision Pro (all models)
Impact: Processing an audio stream in a maliciously crafted media file
may terminate the process
Description: The issue was addressed with improved memory handling.
CVE-2026-39869: David Ige of Beryllium Security

CoreAnimation
Available for: Apple Vision Pro (all models)
Impact: An app may be able to access sensitive user data
Description: An inconsistent user interface issue was addressed with
improved state management.
CVE-2026-28964: Alan Wang, Christopher W. Fletcher, Hovav Shacham, David
Kohlbrenner, Riccardo Paccagnella

CoreServices
Available for: Apple Vision Pro (all models)
Impact: Processing a maliciously crafted file may lead to unexpected app
termination
Description: The issue was addressed with improved checks.
CVE-2026-28936: Andreas Jaegersberger & Ro Achterberg of Nosebeard Labs

CoreSymbolication
Available for: Apple Vision Pro (all models)
Impact: Parsing a maliciously crafted file may lead to an unexpected app
termination
Description: An out-of-bounds access issue was addressed with improved
bounds checking.
CVE-2026-28918: Niels Hofmans, Anonymous working with TrendAI Zero Day
Initiative

FileProvider
Available for: Apple Vision Pro (all models)
Impact: An app may be able to access sensitive user data
Description: A race condition was addressed with additional validation.
CVE-2026-43659: Alex Radocea

ImageIO
Available for: Apple Vision Pro (all models)
Impact: Processing a maliciously crafted file may lead to unexpected app
termination
Description: The issue was addressed with improved bounds checks.
CVE-2026-28977: Suresh Sundaram

ImageIO
Available for: Apple Vision Pro (all models)
Impact: Processing a maliciously crafted image may corrupt process
memory
Description: The issue was addressed with improved memory handling.
CVE-2026-28990: Jiri Ha, Arni Hardarson

IOHIDFamily
Available for: Apple Vision Pro (all models)
Impact: An attacker may be able to cause unexpected app termination
Description: A memory corruption vulnerability was addressed with
improved locking.
CVE-2026-28992: Johnny Franks (@zeroxjf)

IOKit
Available for: Apple Vision Pro (all models)
Impact: An app may be able to cause unexpected system termination
Description: A use after free issue was addressed with improved memory
management.
CVE-2026-28969: Mihalis Haatainen, Ari Hawking, Ashish Kunwar

Kernel
Available for: Apple Vision Pro (all models)
Impact: An app may be able to disclose kernel memory
Description: The issue was addressed with improved memory handling.
CVE-2026-43654: Vaagn Vardanian, Nathaniel Oh (@calysteon)

Kernel
Available for: Apple Vision Pro (all models)
Impact: A local user may be able to cause unexpected system termination
or read kernel memory
Description: A buffer overflow was addressed with improved input
validation.
CVE-2026-28897: popku1337, Billy Jheng Bing Jhong and Pan Zhenpeng
(@Peterpan0927) of STAR Labs SG Pte. Ltd., Robert Tran, Aswin kumar
Gokulakannan

Kernel
Available for: Apple Vision Pro (all models)
Impact: An app may be able to cause unexpected system termination or
write kernel memory
Description: An out-of-bounds write issue was addressed with improved
input validation.
CVE-2026-28972: Billy Jheng Bing Jhong and Pan Zhenpeng (@Peterpan0927)
of STAR Labs SG Pte. Ltd., Ryan Hileman via Xint Code (xint.io)

LaunchServices
Available for: Apple Vision Pro (all models)
Impact: A remote attacker may be able to cause a denial of service
Description: A type confusion issue was addressed with improved checks.
CVE-2026-28983: Ruslan Dautov

mDNSResponder
Available for: Apple Vision Pro (all models)
Impact: A remote attacker may be able to cause unexpected system
termination or corrupt kernel memory
Description: A use after free issue was addressed with improved memory
management.
CVE-2026-43668: Anton Pakhunov, Ricardo Prado

mDNSResponder
Available for: Apple Vision Pro (all models)
Impact: An attacker on the local network may be able to cause a
denial-of-service
Description: An out-of-bounds write issue was addressed with improved
bounds checking.
CVE-2026-43666: Ian van der Wurff (ian.nl)

Model I/O
Available for: Apple Vision Pro (all models)
Impact: Processing a maliciously crafted image may corrupt process
memory
Description: The issue was addressed with improved memory handling.
CVE-2026-28940: Michael DePlante (@izobashi) of TrendAI Zero Day
Initiative

Networking
Available for: Apple Vision Pro (all models)
Impact: An attacker may be able to track users through their IP address
Description: This issue was addressed through improved state management.
CVE-2026-28906: Ilya Sc. Jowell A.

SceneKit
Available for: Apple Vision Pro (all models)
Impact: A remote attacker may be able to cause unexpected app
termination
Description: A buffer overflow was addressed with improved bounds
checking.
CVE-2026-28846: Peter Malone

Shortcuts
Available for: Apple Vision Pro (all models)
Impact: An app may be able to access user-sensitive data
Description: This issue was addressed by adding an additional prompt for
user consent.
CVE-2...