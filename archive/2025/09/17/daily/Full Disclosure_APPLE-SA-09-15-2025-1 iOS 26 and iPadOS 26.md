---
title: APPLE-SA-09-15-2025-1 iOS 26 and iPadOS 26
url: https://seclists.org/fulldisclosure/2025/Sep/49
source: Full Disclosure
date: 2025-09-17
fetch_date: 2025-10-02T20:16:56.761221
---

# APPLE-SA-09-15-2025-1 iOS 26 and iPadOS 26

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

[![Previous](/images/left-icon-16x16.png)](48)
[By Date](date.html#49)
[![Next](/images/right-icon-16x16.png)](50)

[![Previous](/images/left-icon-16x16.png)](48)
[By Thread](index.html#49)
[![Next](/images/right-icon-16x16.png)](50)

![](/shared/images/nst-icons.svg#search)

# APPLE-SA-09-15-2025-1 iOS 26 and iPadOS 26

---

*From*: Apple Product Security via Fulldisclosure <fulldisclosure () seclists org>
*Date*: Mon, 15 Sep 2025 16:31:32 -0700

---

```
-----BEGIN PGP SIGNED MESSAGE-----
Hash: SHA256

APPLE-SA-09-15-2025-1 iOS 26 and iPadOS 26

iOS 26 and iPadOS 26 addresses the following issues.
Information about the security content is also available at
https://support.apple.com/125108.

Apple maintains a Security Releases page at
https://support.apple.com/100100 which lists recent
software updates with security advisories.

Apple Neural Engine
Available for: iPhone 11 and later, iPad Pro 12.9-inch 3rd generation
and later, iPad Pro 11-inch 1st generation and later, iPad Air 3rd
generation and later, iPad 8th generation and later, and iPad mini 5th
generation and later
Impact: An app may be able to cause unexpected system termination
Description: An out-of-bounds access issue was addressed with improved
bounds checking.
CVE-2025-43344: an anonymous researcher

AppleMobileFileIntegrity
Available for: iPhone 11 and later, iPad Pro 12.9-inch 3rd generation
and later, iPad Pro 11-inch 1st generation and later, iPad Air 3rd
generation and later, iPad 8th generation and later, and iPad mini 5th
generation and later
Impact: An app may be able to access sensitive user data
Description: A permissions issue was addressed with additional
restrictions.
CVE-2025-43317: Mickey Jin (@patch1t)

Audio
Available for: iPhone 11 and later, iPad Pro 12.9-inch 3rd generation
and later, iPad Pro 11-inch 1st generation and later, iPad Air 3rd
generation and later, iPad 8th generation and later, and iPad mini 5th
generation and later
Impact: Processing a maliciously crafted media file may lead to
unexpected app termination or corrupt process memory
Description: An out-of-bounds access issue was addressed with improved
bounds checking.
CVE-2025-43346: Hossein Lotfi (@hosselot) of Trend Micro Zero Day
Initiative

Bluetooth
Available for: iPhone 11 and later, iPad Pro 12.9-inch 3rd generation
and later, iPad Pro 11-inch 1st generation and later, iPad Air 3rd
generation and later, iPad 8th generation and later, and iPad mini 5th
generation and later
Impact: An app may be able to access sensitive user data
Description: A logging issue was addressed with improved data redaction.
CVE-2025-43354: Csaba Fitzl (@theevilbit) of Kandji
CVE-2025-43303: Csaba Fitzl (@theevilbit) of Kandji

Call History
Available for: iPhone 11 and later, iPad Pro 12.9-inch 3rd generation
and later, iPad Pro 11-inch 1st generation and later, iPad Air 3rd
generation and later, iPad 8th generation and later, and iPad mini 5th
generation and later
Impact: An app may be able to fingerprint the user
Description: This issue was addressed with improved redaction of
sensitive information.
CVE-2025-43357: Rosyna Keller of Totally Not Malicious Software,
Guilherme Rambo of Best Buddy Apps (rambo.codes)

CoreAudio
Available for: iPhone 11 and later, iPad Pro 12.9-inch 3rd generation
and later, iPad Pro 11-inch 1st generation and later, iPad Air 3rd
generation and later, iPad 8th generation and later, and iPad mini 5th
generation and later
Impact: Processing a maliciously crafted video file may lead to
unexpected app termination
Description: An out-of-bounds write issue was addressed with improved
input validation.
CVE-2025-43349: @zlluny working with Trend Micro Zero Day Initiative

CoreMedia
Available for: iPhone 11 and later, iPad Pro 12.9-inch 3rd generation
and later, iPad Pro 11-inch 1st generation and later, iPad Air 3rd
generation and later, iPad 8th generation and later, and iPad mini 5th
generation and later
Impact: Processing a maliciously crafted media file may lead to
unexpected app termination or corrupt process memory
Description: The issue was addressed with improved input validation.
CVE-2025-43372: 이동하 (Lee Dong Ha) of SSA Lab

IOHIDFamily
Available for: iPhone 11 and later, iPad Pro 12.9-inch 3rd generation
and later, iPad Pro 11-inch 1st generation and later, iPad Air 3rd
generation and later, iPad 8th generation and later, and iPad mini 5th
generation and later
Impact: An app may be able to cause unexpected system termination
Description: An out-of-bounds write issue was addressed with improved
bounds checking.
CVE-2025-43302: Keisuke Hosoda

IOKit
Available for: iPhone 11 and later, iPad Pro 12.9-inch 3rd generation
and later, iPad Pro 11-inch 1st generation and later, iPad Air 3rd
generation and later, iPad 8th generation and later, and iPad mini 5th
generation and later
Impact: An app may be able to access sensitive user data
Description: An authorization issue was addressed with improved state
management.
CVE-2025-31255: Csaba Fitzl (@theevilbit) of Kandji

Kernel
Available for: iPhone 11 and later, iPad Pro 12.9-inch 3rd generation
and later, iPad Pro 11-inch 1st generation and later, iPad Air 3rd
generation and later, iPad 8th generation and later, and iPad mini 5th
generation and later
Impact: A UDP server socket bound to a local interface may become bound
to all interfaces
Description: A logic issue was addressed with improved state management.
CVE-2025-43359: Viktor Oreshkin

LaunchServices
Available for: iPhone 11 and later, iPad Pro 12.9-inch 3rd generation
and later, iPad Pro 11-inch 1st generation and later, iPad Air 3rd
generation and later, iPad 8th generation and later, and iPad mini 5th
generation and later
Impact: An app may be able to monitor keystrokes without user permission
Description: The issue was addressed with improved checks.
CVE-2025-43362: Philipp Baldauf

MobileStorageMounter
Available for: iPhone 11 and later, iPad Pro 12.9-inch 3rd generation
and later, iPad Pro 11-inch 1st generation and later, iPad Air 3rd
generation and later, iPad 8th generation and later, and iPad mini 5th
generation and later
Impact: An app may be able to cause a denial-of-service
Description: A type confusion issue was addressed with improved memory
handling.
CVE-2025-43355: Dawuge of Shuffle Team

Notes
Available for: iPhone 11 and later, iPad Pro 12.9-inch 3rd generation
and later, iPad Pro 11-inch 1st generation and later, iPad Air 3rd
generation and later, iPad 8th generation and later, and iPad mini 5th
generation and later
Impact: An attacker with physical access to an unlocked device may be
able to view an image in the most recently viewed locked note
Description: The issue was addressed with improved handling of caches.
CVE-2025-43203: Tom Brzezinski

Safari
Available for: iPhone 11 and later, iPad Pro 12.9-inch 3rd generation
and later, iPad Pro 11-inch 1st generation and later, iPad Air 3rd
generation and later, iPad 8th generation and later, and iPad mini 5th
generation and later
Impact: Processing maliciously crafted web content may lead to
unexpected URL redirection
Description: This issue was addressed with improved URL validation.
CVE-2025-31254: Evan Waelde

Sandbox
Available for: iPhone 11 and later, iPad Pro 12.9-inch 3rd generation
and later, iPad Pro 11-inch 1st generation and later, iPad Air 3rd
generation and later, iPad 8th generation and later, and iPad mini 5th
generation and later
Impact: An app may be able to break out of its sandbox
Description: A permissions issue was addres...