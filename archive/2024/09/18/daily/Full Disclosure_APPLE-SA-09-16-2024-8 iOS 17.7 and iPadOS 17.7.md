---
title: APPLE-SA-09-16-2024-8 iOS 17.7 and iPadOS 17.7
url: https://seclists.org/fulldisclosure/2024/Sep/39
source: Full Disclosure
date: 2024-09-18
fetch_date: 2025-10-06T18:30:19.771483
---

# APPLE-SA-09-16-2024-8 iOS 17.7 and iPadOS 17.7

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

[![Previous](/images/left-icon-16x16.png)](38)
[By Date](date.html#39)
[![Next](/images/right-icon-16x16.png)](40)

[![Previous](/images/left-icon-16x16.png)](38)
[By Thread](index.html#39)
[![Next](/images/right-icon-16x16.png)](40)

![](/shared/images/nst-icons.svg#search)

# APPLE-SA-09-16-2024-8 iOS 17.7 and iPadOS 17.7

---

*From*: Apple Product Security via Fulldisclosure <fulldisclosure () seclists org>
*Date*: Mon, 16 Sep 2024 18:14:03 -0700

---

```
-----BEGIN PGP SIGNED MESSAGE-----
Hash: SHA256

APPLE-SA-09-16-2024-8 iOS 17.7 and iPadOS 17.7

iOS 17.7 and iPadOS 17.7 addresses the following issues.
Information about the security content is also available at
https://support.apple.com/121246.

Apple maintains a Security Releases page at
https://support.apple.com/100100 which lists recent
software updates with security advisories.

Accessibility
Available for: iPhone XS and later, iPad Pro 13-inch, iPad Pro 12.9-inch
2nd generation and later, iPad Pro 10.5-inch, iPad Pro 11-inch 1st
generation and later, iPad Air 3rd generation and later, iPad 6th
generation and later, and iPad mini 5th generation and later
Impact: An attacker with physical access to a locked device may be able
to Control Nearby Devices via accessibility features
Description: This issue was addressed through improved state management.
CVE-2024-44171: Jake Derouin

Compression
Available for: iPhone XS and later, iPad Pro 13-inch, iPad Pro 12.9-inch
2nd generation and later, iPad Pro 10.5-inch, iPad Pro 11-inch 1st
generation and later, iPad Air 3rd generation and later, iPad 6th
generation and later, and iPad mini 5th generation and later
Impact: Unpacking a maliciously crafted archive may allow an attacker to
write arbitrary files
Description: A race condition was addressed with improved locking.
CVE-2024-27876: Snoolie Keffaber (@0xilis)

Game Center
Available for: iPhone XS and later, iPad Pro 13-inch, iPad Pro 12.9-inch
2nd generation and later, iPad Pro 10.5-inch, iPad Pro 11-inch 1st
generation and later, iPad Air 3rd generation and later, iPad 6th
generation and later, and iPad mini 5th generation and later
Impact: An app may be able to access user-sensitive data
Description: A file access issue was addressed with improved input
validation.
CVE-2024-40850: Denis Tokarev (@illusionofcha0s)

ImageIO
Available for: iPhone XS and later, iPad Pro 13-inch, iPad Pro 12.9-inch
2nd generation and later, iPad Pro 10.5-inch, iPad Pro 11-inch 1st
generation and later, iPad Air 3rd generation and later, iPad 6th
generation and later, and iPad mini 5th generation and later
Impact: Processing a maliciously crafted file may lead to unexpected app
termination
Description: An out-of-bounds read issue was addressed with improved
input validation.
CVE-2024-27880: Junsung Lee

ImageIO
Available for: iPhone XS and later, iPad Pro 13-inch, iPad Pro 12.9-inch
2nd generation and later, iPad Pro 10.5-inch, iPad Pro 11-inch 1st
generation and later, iPad Air 3rd generation and later, iPad 6th
generation and later, and iPad mini 5th generation and later
Impact: Processing an image may lead to a denial-of-service
Description: An out-of-bounds access issue was addressed with improved
bounds checking.
CVE-2024-44176: dw0r of ZeroPointer Lab working with Trend Micro Zero
Day Initiative, an anonymous researcher

IOSurfaceAccelerator
Available for: iPhone XS and later, iPad Pro 13-inch, iPad Pro 12.9-inch
2nd generation and later, iPad Pro 10.5-inch, iPad Pro 11-inch 1st
generation and later, iPad Air 3rd generation and later, iPad 6th
generation and later, and iPad mini 5th generation and later
Impact: An app may be able to cause unexpected system termination
Description: The issue was addressed with improved memory handling.
CVE-2024-44169: Antonio ZekiÄ‡

Kernel
Available for: iPhone XS and later, iPad Pro 13-inch, iPad Pro 12.9-inch
2nd generation and later, iPad Pro 10.5-inch, iPad Pro 11-inch 1st
generation and later, iPad Air 3rd generation and later, iPad 6th
generation and later, and iPad mini 5th generation and later
Impact: Network traffic may leak outside a VPN tunnel
Description: A logic issue was addressed with improved checks.
CVE-2024-44165: Andrew Lytvynov

Kernel
Available for: iPhone XS and later, iPad Pro 13-inch, iPad Pro 12.9-inch
2nd generation and later, iPad Pro 10.5-inch, iPad Pro 11-inch 1st
generation and later, iPad Air 3rd generation and later, iPad 6th
generation and later, and iPad mini 5th generation and later
Impact: An app may gain unauthorized access to Bluetooth
Description: This issue was addressed through improved state management.
CVE-2024-44191: Alexander Heinrich, SEEMOO, DistriNet, KU Leuven
(@vanhoefm), TU Darmstadt (@Sn0wfreeze) and Mathy Vanhoef

Mail Accounts
Available for: iPhone XS and later, iPad Pro 13-inch, iPad Pro 12.9-inch
2nd generation and later, iPad Pro 10.5-inch, iPad Pro 11-inch 1st
generation and later, iPad Air 3rd generation and later, iPad 6th
generation and later, and iPad mini 5th generation and later
Impact: An app may be able to access information about a user's contacts
Description: A privacy issue was addressed with improved private data
redaction for log entries.
CVE-2024-40791: Rodolphe BRUNETTI (@eisw0lf)

mDNSResponder
Available for: iPhone XS and later, iPad Pro 13-inch, iPad Pro 12.9-inch
2nd generation and later, iPad Pro 10.5-inch, iPad Pro 11-inch 1st
generation and later, iPad Air 3rd generation and later, iPad 6th
generation and later, and iPad mini 5th generation and later
Impact: An app may be able to cause a denial-of-service
Description: A logic error was addressed with improved error handling.
CVE-2024-44183: Olivier Levon

Safari Private Browsing
Available for: iPhone XS and later, iPad Pro 13-inch, iPad Pro 12.9-inch
2nd generation and later, iPad Pro 10.5-inch, iPad Pro 11-inch 1st
generation and later, iPad Air 3rd generation and later, iPad 6th
generation and later, and iPad mini 5th generation and later
Impact: Private Browsing tabs may be accessed without authentication
Description: This issue was addressed through improved state management.
CVE-2024-44127: Anamika Adhikari

Shortcuts
Available for: iPhone XS and later, iPad Pro 13-inch, iPad Pro 12.9-inch
2nd generation and later, iPad Pro 10.5-inch, iPad Pro 11-inch 1st
generation and later, iPad Air 3rd generation and later, iPad 6th
generation and later, and iPad mini 5th generation and later
Impact: A shortcut may output sensitive user data without consent
Description: This issue was addressed with improved redaction of
sensitive information.
CVE-2024-44158: Kirin (@Pwnrin)

Shortcuts
Available for: iPhone XS and later, iPad Pro 13-inch, iPad Pro 12.9-inch
2nd generation and later, iPad Pro 10.5-inch, iPad Pro 11-inch 1st
generation and later, iPad Air 3rd generation and later, iPad 6th
generation and later, and iPad mini 5th generation and later
Impact: An app may be able to observe data displayed to the user by
Shortcuts
Description: A privacy issue was addressed with improved handling of
temporary files.
CVE-2024-40844: Kirin (@Pwnrin) and luckyu (@uuulucky) of NorthSea

Sync Services
Available for: iPhone XS and later, iPad Pro 13-inch, iPad Pro 12.9-inch
2nd generation and later, iPad Pro 10.5-inch, iPad Pro 11-inch 1st
generation and later, iPad Air 3rd generation and later, iPad 6th
generation and later, and iPad mini 5th generation and later
Impact: An app may be able to bypass Privacy preferences
Description: This issue was addressed with improved checks.
CVE-20...