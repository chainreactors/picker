---
title: APPLE-SA-09-15-2025-2 iOS 18.7 and iPadOS 18.7
url: https://seclists.org/fulldisclosure/2025/Sep/50
source: Full Disclosure
date: 2025-09-17
fetch_date: 2025-10-02T20:16:55.534595
---

# APPLE-SA-09-15-2025-2 iOS 18.7 and iPadOS 18.7

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

[![Previous](/images/left-icon-16x16.png)](49)
[By Date](date.html#50)
[![Next](/images/right-icon-16x16.png)](51)

[![Previous](/images/left-icon-16x16.png)](49)
[By Thread](index.html#50)
[![Next](/images/right-icon-16x16.png)](51)

![](/shared/images/nst-icons.svg#search)

# APPLE-SA-09-15-2025-2 iOS 18.7 and iPadOS 18.7

---

*From*: Apple Product Security via Fulldisclosure <fulldisclosure () seclists org>
*Date*: Mon, 15 Sep 2025 16:32:20 -0700

---

```
-----BEGIN PGP SIGNED MESSAGE-----
Hash: SHA256

APPLE-SA-09-15-2025-2 iOS 18.7 and iPadOS 18.7

iOS 18.7 and iPadOS 18.7 addresses the following issues.
Information about the security content is also available at
https://support.apple.com/125109.

Apple maintains a Security Releases page at
https://support.apple.com/100100 which lists recent
software updates with security advisories.

Audio
Available for: iPhone XS and later, iPad Pro 13-inch, iPad Pro 12.9-inch
3rd generation and later, iPad Pro 11-inch 1st generation and later,
iPad Air 3rd generation and later, iPad 7th generation and later, and
iPad mini 5th generation and later
Impact: Processing a maliciously crafted media file may lead to
unexpected app termination or corrupt process memory
Description: An out-of-bounds access issue was addressed with improved
bounds checking.
CVE-2025-43346: Hossein Lotfi (@hosselot) of Trend Micro Zero Day
Initiative

CoreAudio
Available for: iPhone XS and later, iPad Pro 13-inch, iPad Pro 12.9-inch
3rd generation and later, iPad Pro 11-inch 1st generation and later,
iPad Air 3rd generation and later, iPad 7th generation and later, and
iPad mini 5th generation and later
Impact: Processing a maliciously crafted video file may lead to
unexpected app termination
Description: An out-of-bounds write issue was addressed with improved
input validation.
CVE-2025-43349: @zlluny working with Trend Micro Zero Day Initiative

IOHIDFamily
Available for: iPhone XS and later, iPad Pro 13-inch, iPad Pro 12.9-inch
3rd generation and later, iPad Pro 11-inch 1st generation and later,
iPad Air 3rd generation and later, iPad 7th generation and later, and
iPad mini 5th generation and later
Impact: An app may be able to cause unexpected system termination
Description: An out-of-bounds write issue was addressed with improved
bounds checking.
CVE-2025-43302: Keisuke Hosoda

Kernel
Available for: iPhone XS and later, iPad Pro 13-inch, iPad Pro 12.9-inch
3rd generation and later, iPad Pro 11-inch 1st generation and later,
iPad Air 3rd generation and later, iPad 7th generation and later, and
iPad mini 5th generation and later
Impact: A UDP server socket bound to a local interface may become bound
to all interfaces
Description: A logic issue was addressed with improved state management.
CVE-2025-43359: Viktor Oreshkin

LaunchServices
Available for: iPhone XS and later, iPad Pro 13-inch, iPad Pro 12.9-inch
3rd generation and later, iPad Pro 11-inch 1st generation and later,
iPad Air 3rd generation and later, iPad 7th generation and later, and
iPad mini 5th generation and later
Impact: An app may be able to monitor keystrokes without user permission
Description: The issue was addressed with improved checks.
CVE-2025-43362: Philipp Baldauf

libc
Available for: iPhone XS and later, iPad Pro 13-inch, iPad Pro 12.9-inch
3rd generation and later, iPad Pro 11-inch 1st generation and later,
iPad Air 3rd generation and later, iPad 7th generation and later, and
iPad mini 5th generation and later
Impact: An app may be able to cause a denial-of-service
Description: A denial-of-service issue was addressed with improved
validation.
CVE-2025-43299: Nathaniel Oh (@calysteon)
CVE-2025-43295: Nathaniel Oh (@calysteon)

MobileStorageMounter
Available for: iPhone XS and later, iPad Pro 13-inch, iPad Pro 12.9-inch
3rd generation and later, iPad Pro 11-inch 1st generation and later,
iPad Air 3rd generation and later, iPad 7th generation and later, and
iPad mini 5th generation and later
Impact: An app may be able to cause a denial-of-service
Description: A type confusion issue was addressed with improved memory
handling.
CVE-2025-43355: Dawuge of Shuffle Team

Notes
Available for: iPhone XS and later, iPad Pro 13-inch, iPad Pro 12.9-inch
3rd generation and later, iPad Pro 11-inch 1st generation and later,
iPad Air 3rd generation and later, iPad 7th generation and later, and
iPad mini 5th generation and later
Impact: An attacker with physical access to an unlocked device may be
able to view an image in the most recently viewed locked note
Description: The issue was addressed with improved handling of caches.
CVE-2025-43203: Tom Brzezinski

Shortcuts
Available for: iPhone XS and later, iPad Pro 13-inch, iPad Pro 12.9-inch
3rd generation and later, iPad Pro 11-inch 1st generation and later,
iPad Air 3rd generation and later, iPad 7th generation and later, and
iPad mini 5th generation and later
Impact: A shortcut may be able to bypass sandbox restrictions
Description: A permissions issue was addressed with additional sandbox
restrictions.
CVE-2025-43358: 정답이 아닌 해답

WebKit
Available for: iPhone XS and later, iPad Pro 13-inch, iPad Pro 12.9-inch
3rd generation and later, iPad Pro 11-inch 1st generation and later,
iPad Air 3rd generation and later, iPad 7th generation and later, and
iPad mini 5th generation and later
Impact: A website may be able to access sensor information without user
consent
Description: The issue was addressed with improved handling of caches.
WebKit Bugzilla: 296153
CVE-2025-43356: Jaydev Ahire

WebKit
Available for: iPhone XS and later, iPad Pro 13-inch, iPad Pro 12.9-inch
3rd generation and later, iPad Pro 11-inch 1st generation and later,
iPad Air 3rd generation and later, iPad 7th generation and later, and
iPad mini 5th generation and later
Impact: Processing maliciously crafted web content may lead to an
unexpected process crash
Description: A correctness issue was addressed with improved checks.
WebKit Bugzilla: 296042
CVE-2025-43342: an anonymous researcher

Additional recognition

IOGPUFamily
We would like to acknowledge Wang Yu of Cyberserval for their
assistance.

libpthread
We would like to acknowledge Nathaniel Oh (@calysteon) for their
assistance.

libxml2
We would like to acknowledge Nathaniel Oh (@calysteon) for their
assistance.

Lockdown Mode
We would like to acknowledge Pyrophoria and Ethan Day, kado for their
assistance.

Wi-Fi
We would like to acknowledge Csaba Fitzl (@theevilbit) of Kandji, Noah
Gregory (wts.dev), Wojciech Regula of SecuRing (wojciechregula.blog), an
anonymous researcher for their assistance.

This update is available through iTunes and Software Update on your
iOS device, and will not appear in your computer's Software Update
application, or in the Apple Downloads site. Make sure you have an
Internet connection and have installed the latest version of iTunes
from https://www.apple.com/itunes/

iTunes and Software Update on the device will automatically check
Apple's update server on its weekly schedule. When an update is
detected, it is downloaded and the option to be installed is
presented to the user when the iOS device is docked. We recommend
applying the update immediately if possible. Selecting Don't Install
will present the option the next time you connect your iOS device.

The automatic update process may take up to a week depending on the
day that iTunes or the device checks for updates. You may manually
obtain the update via the Check for Updates button within iTunes, or
the Software Update on your device.

...