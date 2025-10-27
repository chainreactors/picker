---
title: APPLE-SA-09-16-2024-1 iOS 18 and iPadOS 18
url: https://seclists.org/fulldisclosure/2024/Sep/32
source: Full Disclosure
date: 2024-09-18
fetch_date: 2025-10-06T18:30:34.114492
---

# APPLE-SA-09-16-2024-1 iOS 18 and iPadOS 18

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

[![Previous](/images/left-icon-16x16.png)](31)
[By Date](date.html#32)
[![Next](/images/right-icon-16x16.png)](33)

[![Previous](/images/left-icon-16x16.png)](31)
[By Thread](index.html#32)
[![Next](/images/right-icon-16x16.png)](33)

![](/shared/images/nst-icons.svg#search)

# APPLE-SA-09-16-2024-1 iOS 18 and iPadOS 18

---

*From*: Apple Product Security via Fulldisclosure <fulldisclosure () seclists org>
*Date*: Mon, 16 Sep 2024 18:05:02 -0700

---

```
-----BEGIN PGP SIGNED MESSAGE-----
Hash: SHA256

APPLE-SA-09-16-2024-1 iOS 18 and iPadOS 18

iOS 18 and iPadOS 18 addresses the following issues.
Information about the security content is also available at
https://support.apple.com/121250.

Apple maintains a Security Releases page at
https://support.apple.com/100100 which lists recent
software updates with security advisories.

Accessibility
Available for: iPhone XS and later, iPad Pro 13-inch, iPad Pro 12.9-inch
3rd generation and later, iPad Pro 11-inch 1st generation and later,
iPad Air 3rd generation and later, iPad 7th generation and later, and
iPad mini 5th generation and later
Impact: An attacker with physical access may be able to use Siri to
access sensitive user data
Description: This issue was addressed through improved state management.
CVE-2024-40840: Abhay Kailasia (@abhay_kailasia) of Lakshmi Narain
College of Technology Bhopal India

Accessibility
Available for: iPhone XS and later, iPad Pro 13-inch, iPad Pro 12.9-inch
3rd generation and later, iPad Pro 11-inch 1st generation and later,
iPad Air 3rd generation and later, iPad 7th generation and later, and
iPad mini 5th generation and later
Impact: An app may be able to enumerate a user's installed apps
Description: This issue was addressed with improved data protection.
CVE-2024-40830: Chloe Surett

Accessibility
Available for: iPhone XS and later, iPad Pro 13-inch, iPad Pro 12.9-inch
3rd generation and later, iPad Pro 11-inch 1st generation and later,
iPad Air 3rd generation and later, iPad 7th generation and later, and
iPad mini 5th generation and later
Impact: An attacker with physical access to a locked device may be able
to Control Nearby Devices via accessibility features
Description: This issue was addressed through improved state management.
CVE-2024-44171: Jake Derouin

Accessibility
Available for: iPhone XS and later, iPad Pro 13-inch, iPad Pro 12.9-inch
3rd generation and later, iPad Pro 11-inch 1st generation and later,
iPad Air 3rd generation and later, iPad 7th generation and later, and
iPad mini 5th generation and later
Impact: An attacker may be able to see recent photos without
authentication in Assistive Access
Description: This issue was addressed by restricting options offered on
a locked device.
CVE-2024-40852: Abhay Kailasia (@abhay_kailasia) of Lakshmi Narain
College of Technology Bhopal India

Cellular
Available for: iPhone XS and later, iPad Pro 13-inch, iPad Pro 12.9-inch
3rd generation and later, iPad Pro 11-inch 1st generation and later,
iPad Air 3rd generation and later, iPad 7th generation and later, and
iPad mini 5th generation and later
Impact: A remote attacker may be able to cause a denial-of-service
Description: This issue was addressed through improved state management.
CVE-2024-27874: Tuan D. Hoang

Compression
Available for: iPhone XS and later, iPad Pro 13-inch, iPad Pro 12.9-inch
3rd generation and later, iPad Pro 11-inch 1st generation and later,
iPad Air 3rd generation and later, iPad 7th generation and later, and
iPad mini 5th generation and later
Impact: Unpacking a maliciously crafted archive may allow an attacker to
write arbitrary files
Description: A race condition was addressed with improved locking.
CVE-2024-27876: Snoolie Keffaber (@0xilis)

Control Center
Available for: iPhone XS and later, iPad Pro 13-inch, iPad Pro 12.9-inch
3rd generation and later, iPad Pro 11-inch 1st generation and later,
iPad Air 3rd generation and later, iPad 7th generation and later, and
iPad mini 5th generation and later
Impact: An app may be able to record the screen without an indicator
Description: The issue was addressed with improved checks.
CVE-2024-27869: an anonymous researcher

Core Bluetooth
Available for: iPhone XS and later, iPad Pro 13-inch, iPad Pro 12.9-inch
3rd generation and later, iPad Pro 11-inch 1st generation and later,
iPad Air 3rd generation and later, iPad 7th generation and later, and
iPad mini 5th generation and later
Impact: A malicious Bluetooth input device may bypass pairing
Description: This issue was addressed through improved state management.
CVE-2024-44124: Daniele Antonioli

FileProvider
Available for: iPhone XS and later, iPad Pro 13-inch, iPad Pro 12.9-inch
3rd generation and later, iPad Pro 11-inch 1st generation and later,
iPad Air 3rd generation and later, iPad 7th generation and later, and
iPad mini 5th generation and later
Impact: An app may be able to access sensitive user data
Description: This issue was addressed with improved validation of
symlinks.
CVE-2024-44131: @08Tc3wBB of Jamf

Game Center
Available for: iPhone XS and later, iPad Pro 13-inch, iPad Pro 12.9-inch
3rd generation and later, iPad Pro 11-inch 1st generation and later,
iPad Air 3rd generation and later, iPad 7th generation and later, and
iPad mini 5th generation and later
Impact: An app may be able to access user-sensitive data
Description: A file access issue was addressed with improved input
validation.
CVE-2024-40850: Denis Tokarev (@illusionofcha0s)

ImageIO
Available for: iPhone XS and later, iPad Pro 13-inch, iPad Pro 12.9-inch
3rd generation and later, iPad Pro 11-inch 1st generation and later,
iPad Air 3rd generation and later, iPad 7th generation and later, and
iPad mini 5th generation and later
Impact: Processing a maliciously crafted file may lead to unexpected app
termination
Description: An out-of-bounds read issue was addressed with improved
input validation.
CVE-2024-27880: Junsung Lee

ImageIO
Available for: iPhone XS and later, iPad Pro 13-inch, iPad Pro 12.9-inch
3rd generation and later, iPad Pro 11-inch 1st generation and later,
iPad Air 3rd generation and later, iPad 7th generation and later, and
iPad mini 5th generation and later
Impact: Processing an image may lead to a denial-of-service
Description: An out-of-bounds access issue was addressed with improved
bounds checking.
CVE-2024-44176: dw0r of ZeroPointer Lab working with Trend Micro Zero
Day Initiative and an anonymous researcher

IOSurfaceAccelerator
Available for: iPhone XS and later, iPad Pro 13-inch, iPad Pro 12.9-inch
3rd generation and later, iPad Pro 11-inch 1st generation and later,
iPad Air 3rd generation and later, iPad 7th generation and later, and
iPad mini 5th generation and later
Impact: An app may be able to cause unexpected system termination
Description: The issue was addressed with improved memory handling.
CVE-2024-44169: Antonio Zekić

Kernel
Available for: iPhone XS and later, iPad Pro 13-inch, iPad Pro 12.9-inch
3rd generation and later, iPad Pro 11-inch 1st generation and later,
iPad Air 3rd generation and later, iPad 7th generation and later, and
iPad mini 5th generation and later
Impact: Network traffic may leak outside a VPN tunnel
Description: A logic issue was addressed with improved checks.
CVE-2024-44165: Andrew Lytvynov

Kernel
Available for: iPhone XS and later, iPad Pro 13-inch, iPad Pro 12.9-inch
3rd generation and later, iPad Pro 11-inch 1st generation and later,
iPad Air 3rd generation and later, iPad 7th generation and later, and
iPad mini 5th ge...