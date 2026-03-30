---
title: APPLE-SA-03-24-2026-1 iOS 26.4 and iPadOS 26.4
url: https://seclists.org/fulldisclosure/2026/Mar/16
source: Full Disclosure
date: 2026-03-29
fetch_date: 2026-03-30T04:46:59.391658
---

# APPLE-SA-03-24-2026-1 iOS 26.4 and iPadOS 26.4

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

[![Previous](/images/left-icon-16x16.png)](15)
[By Date](date.html#16)
[![Next](/images/right-icon-16x16.png)](17)

[![Previous](/images/left-icon-16x16.png)](15)
[By Thread](index.html#16)
[![Next](/images/right-icon-16x16.png)](17)

![](/shared/images/nst-icons.svg#search)

# APPLE-SA-03-24-2026-1 iOS 26.4 and iPadOS 26.4

---

*From*: Apple Product Security via Fulldisclosure <fulldisclosure () seclists org>
*Date*: Tue, 24 Mar 2026 17:00:35 -0700

---

```
-----BEGIN PGP SIGNED MESSAGE-----
Hash: SHA256

APPLE-SA-03-24-2026-1 iOS 26.4 and iPadOS 26.4

iOS 26.4 and iPadOS 26.4 addresses the following issues.
Information about the security content is also available at
https://support.apple.com/126792.

Apple maintains a Security Releases page at
https://support.apple.com/100100 which lists recent
software updates with security advisories.

802.1X
Available for: iPhone 11 and later, iPad Pro 12.9-inch 3rd generation
and later, iPad Pro 11-inch 1st generation and later, iPad Air 3rd
generation and later, iPad 8th generation and later, and iPad mini 5th
generation and later
Impact: An attacker in a privileged network position may be able to
intercept network traffic
Description: An authentication issue was addressed with improved state
management.
CVE-2026-28865: Héloïse Gollier and Mathy Vanhoef (KU Leuven)

Accounts
Available for: iPhone 11 and later, iPad Pro 12.9-inch 3rd generation
and later, iPad Pro 11-inch 1st generation and later, iPad Air 3rd
generation and later, iPad 8th generation and later, and iPad mini 5th
generation and later
Impact: An app may be able to access sensitive user data
Description: An authorization issue was addressed with improved state
management.
CVE-2026-28877: Rosyna Keller of Totally Not Malicious Software

App Protection
Available for: iPhone 11 and later
Impact: An attacker with physical access to an iOS device with Stolen
Device Protection enabled may be able to access biometrics-gated
Protected Apps with the passcode
Description: The issue was addressed with improved checks.
CVE-2026-28895: Zack Tickman

Audio
Available for: iPhone 11 and later, iPad Pro 12.9-inch 3rd generation
and later, iPad Pro 11-inch 1st generation and later, iPad Air 3rd
generation and later, iPad 8th generation and later, and iPad mini 5th
generation and later
Impact: Processing maliciously crafted web content may lead to an
unexpected process crash
Description: A use-after-free issue was addressed with improved memory
management.
CVE-2026-28879: Justin Cohen of Google

Audio
Available for: iPhone 11 and later, iPad Pro 12.9-inch 3rd generation
and later, iPad Pro 11-inch 1st generation and later, iPad Air 3rd
generation and later, iPad 8th generation and later, and iPad mini 5th
generation and later
Impact: An attacker may be able to cause unexpected app termination
Description: A type confusion issue was addressed with improved memory
handling.
CVE-2026-28822: Jex Amro

Baseband
Available for: iPhone 11 and later, iPad Pro 12.9-inch 3rd generation
and later, iPad Pro 11-inch 1st generation and later, iPad Air 3rd
generation and later, iPad 8th generation and later, and iPad mini 5th
generation and later
Impact: A remote attacker may cause an unexpected app termination
Description: The issue was addressed with improved checks.
CVE-2026-28874: Hazem Issa, Tuan D. Hoang, and Yongdae Kim @ SysSec,
KAIST

Baseband
Available for: iPhone 16e
Impact: A remote attacker may be able to cause a denial-of-service
Description: A buffer overflow was addressed with improved bounds
checking.
CVE-2026-28875: Tuan D. Hoang and Yongdae Kim @ KAIST SysSec Lab

Calling Framework
Available for: iPhone 11 and later, iPad Pro 12.9-inch 3rd generation
and later, iPad Pro 11-inch 1st generation and later, iPad Air 3rd
generation and later, iPad 8th generation and later, and iPad mini 5th
generation and later
Impact: A remote attacker may be able to cause a denial-of-service
Description: A denial-of-service issue was addressed with improved input
validation.
CVE-2026-28894: an anonymous researcher

Clipboard
Available for: iPhone 11 and later, iPad Pro 12.9-inch 3rd generation
and later, iPad Pro 11-inch 1st generation and later, iPad Air 3rd
generation and later, iPad 8th generation and later, and iPad mini 5th
generation and later
Impact: An app may be able to access sensitive user data
Description: This issue was addressed with improved validation of
symlinks.
CVE-2026-28866: Cristian Dinca (icmd.tech)

CoreMedia
Available for: iPhone 11 and later, iPad Pro 12.9-inch 3rd generation
and later, iPad Pro 11-inch 1st generation and later, iPad Air 3rd
generation and later, iPad 8th generation and later, and iPad mini 5th
generation and later
Impact: Processing an audio stream in a maliciously crafted media file
may terminate the process
Description: An out-of-bounds access issue was addressed with improved
bounds checking.
CVE-2026-20690: Hossein Lotfi (@hosselot) of Trend Micro Zero Day
Initiative

CoreUtils
Available for: iPhone 11 and later, iPad Pro 12.9-inch 3rd generation
and later, iPad Pro 11-inch 1st generation and later, iPad Air 3rd
generation and later, iPad 8th generation and later, and iPad mini 5th
generation and later
Impact: A user in a privileged network position may be able to cause a
denial-of-service
Description: A null pointer dereference was addressed with improved
input validation.
CVE-2026-28886: Etienne Charron (Renault) and Victoria Martini (Renault)

Crash Reporter
Available for: iPhone 11 and later, iPad Pro 12.9-inch 3rd generation
and later, iPad Pro 11-inch 1st generation and later, iPad Air 3rd
generation and later, iPad 8th generation and later, and iPad mini 5th
generation and later
Impact: An app may be able to enumerate a user's installed apps
Description: A privacy issue was addressed by removing sensitive data.
CVE-2026-28878: Zhongcheng Li from IES Red Team

curl
Available for: iPhone 11 and later, iPad Pro 12.9-inch 3rd generation
and later, iPad Pro 11-inch 1st generation and later, iPad Air 3rd
generation and later, iPad 8th generation and later, and iPad mini 5th
generation and later
Impact: An issue existed in curl which may result in unintentionally
sending sensitive information via an incorrect connection
Description: This is a vulnerability in open source code and Apple
Software is among the affected projects. The CVE-ID was assigned by a
third party. Learn more about the issue and CVE-ID at cve.org.
CVE-2025-14524

DeviceLink
Available for: iPhone 11 and later, iPad Pro 12.9-inch 3rd generation
and later, iPad Pro 11-inch 1st generation and later, iPad Air 3rd
generation and later, iPad 8th generation and later, and iPad mini 5th
generation and later
Impact: An app may be able to access sensitive user data
Description: A parsing issue in the handling of directory paths was
addressed with improved path validation.
CVE-2026-28876: Andreas Jaegersberger & Ro Achterberg of Nosebeard Labs

GeoServices
Available for: iPhone 11 and later, iPad Pro 12.9-inch 3rd generation
and later, iPad Pro 11-inch 1st generation and later, iPad Air 3rd
generation and later, iPad 8th generation and later, and iPad mini 5th
generation and later
Impact: An app may be able to access sensitive user data
Description: An information leakage was addressed with additional
validation.
CVE-2026-28870: XiguaSec

iCloud
Available for: iPhone 11 and later, iPad Pro 12.9-inch 3rd generation
and later, iPad Pro 11-inch 1st generation and later, iPad Air 3rd
generation a...