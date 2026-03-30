---
title: APPLE-SA-03-24-2026-2 iOS 18.7.7 and iPadOS 18.7.7
url: https://seclists.org/fulldisclosure/2026/Mar/17
source: Full Disclosure
date: 2026-03-29
fetch_date: 2026-03-30T04:46:59.078434
---

# APPLE-SA-03-24-2026-2 iOS 18.7.7 and iPadOS 18.7.7

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

[![Previous](/images/left-icon-16x16.png)](16)
[By Date](date.html#17)
[![Next](/images/right-icon-16x16.png)](18)

[![Previous](/images/left-icon-16x16.png)](16)
[By Thread](index.html#17)
[![Next](/images/right-icon-16x16.png)](18)

![](/shared/images/nst-icons.svg#search)

# APPLE-SA-03-24-2026-2 iOS 18.7.7 and iPadOS 18.7.7

---

*From*: Apple Product Security via Fulldisclosure <fulldisclosure () seclists org>
*Date*: Tue, 24 Mar 2026 17:01:12 -0700

---

```
-----BEGIN PGP SIGNED MESSAGE-----
Hash: SHA256

APPLE-SA-03-24-2026-2 iOS 18.7.7 and iPadOS 18.7.7

iOS 18.7.7 and iPadOS 18.7.7 addresses the following issues.
Information about the security content is also available at
https://support.apple.com/126793.

Apple maintains a Security Releases page at
https://support.apple.com/100100 which lists recent
software updates with security advisories.

802.1X
Available for: iPhone XS, iPhone XS Max, iPhone XR, iPad 7th generation
Impact: An attacker in a privileged network position may be able to
intercept network traffic
Description: An authentication issue was addressed with improved state
management.
CVE-2026-28865: Héloïse Gollier and Mathy Vanhoef (KU Leuven)

AppleKeyStore
Available for: iPhone XS, iPhone XS Max, iPhone XR, iPad 7th generation
Impact: An app may be able to cause unexpected system termination
Description: A use after free issue was addressed with improved memory
management.
CVE-2026-20637: Johnny Franks (zeroxjf), an anonymous researcher

Audio
Available for: iPhone XS, iPhone XS Max, iPhone XR, iPad 7th generation
Impact: Processing maliciously crafted web content may lead to an
unexpected process crash
Description: A use-after-free issue was addressed with improved memory
management.
CVE-2026-28879: Justin Cohen of Google

Clipboard
Available for: iPhone XS, iPhone XS Max, iPhone XR, iPad 7th generation
Impact: An app may be able to access sensitive user data
Description: This issue was addressed with improved validation of
symlinks.
CVE-2026-28866: Cristian Dinca (icmd.tech)

CoreMedia
Available for: iPhone XS, iPhone XS Max, iPhone XR, iPad 7th generation
Impact: Processing an audio stream in a maliciously crafted media file
may terminate the process
Description: An out-of-bounds access issue was addressed with improved
bounds checking.
CVE-2026-20690: Hossein Lotfi (@hosselot) of Trend Micro Zero Day
Initiative

CoreUtils
Available for: iPhone XS, iPhone XS Max, iPhone XR, iPad 7th generation
Impact: A user in a privileged network position may be able to cause a
denial-of-service
Description: A null pointer dereference was addressed with improved
input validation.
CVE-2026-28886: Etienne Charron (Renault) and Victoria Martini (Renault)

Crash Reporter
Available for: iPhone XS, iPhone XS Max, iPhone XR, iPad 7th generation
Impact: An app may be able to enumerate a user's installed apps
Description: A privacy issue was addressed by removing sensitive data.
CVE-2026-28878: Zhongcheng Li from IES Red Team

curl
Available for: iPhone XS, iPhone XS Max, iPhone XR, iPad 7th generation
Impact: An issue existed in curl which may result in unintentionally
sending sensitive information via an incorrect connection
Description: This is a vulnerability in open source code and Apple
Software is among the affected projects. The CVE-ID was assigned by a
third party. Learn more about the issue and CVE-ID at cve.org.
CVE-2025-14524

DeviceLink
Available for: iPhone XS, iPhone XS Max, iPhone XR, iPad 7th generation
Impact: An app may be able to access sensitive user data
Description: A parsing issue in the handling of directory paths was
addressed with improved path validation.
CVE-2026-28876: Andreas Jaegersberger & Ro Achterberg of Nosebeard Labs

Focus
Available for: iPhone XS, iPhone XS Max, iPhone XR, iPad 7th generation
Impact: An app may be able to access sensitive user data
Description: A logging issue was addressed with improved data redaction.
CVE-2026-20668: Kirin (@Pwnrin)

iCloud
Available for: iPhone XS, iPhone XS Max, iPhone XR, iPad 7th generation
Impact: An app may be able to enumerate a user's installed apps
Description: A permissions issue was addressed with additional
restrictions.
CVE-2026-28880: Zhongcheng Li from IES Red Team

ImageIO
Available for: iPhone XS, iPhone XS Max, iPhone XR, iPad 7th generation
Impact: Processing a maliciously crafted file may lead to unexpected app
termination
Description: This is a vulnerability in open source code and Apple
Software is among the affected projects. The CVE-ID was assigned by a
third party. Learn more about the issue and CVE-ID at cve.org.
CVE-2025-64505

iTunes Store
Available for: iPhone XS, iPhone XS Max, iPhone XR, iPad 7th generation
Impact: A user with physical access to an iOS device may be able to
bypass Activation Lock
Description: A path handling issue was addressed with improved
validation.
CVE-2025-43534: iG0x72 and JJ of XiguaSec, Lehan Dilusha Jayasinghe

Kernel
Available for: iPhone XS, iPhone XS Max, iPhone XR, iPad 7th generation
Impact: An app may be able to disclose kernel memory
Description: A logging issue was addressed with improved data redaction.
CVE-2026-28868: 이동하 (Lee Dong Ha of BoB 0xB6)

Kernel
Available for: iPhone XS, iPhone XS Max, iPhone XR, iPad 7th generation
Impact: An app may be able to leak sensitive kernel state
Description: This issue was addressed with improved authentication.
CVE-2026-28867: Jian Lee (@speedyfriend433)

Kernel
Available for: iPhone XS, iPhone XS Max, iPhone XR, iPad 7th generation
Impact: An app may be able to cause unexpected system termination or
write kernel memory
Description: A use after free issue was addressed with improved memory
management.
CVE-2026-20687: Johnny Franks (@zeroxjf)

mDNSResponder
Available for: iPhone XS, iPhone XS Max, iPhone XR, iPad 7th generation
Impact: An app may be able to leak sensitive kernel state
Description: This issue was addressed with improved authentication.
CVE-2026-28867: Jian Lee (@speedyfriend433)

Security
Available for: iPhone XS, iPhone XS Max, iPhone XR, iPad 7th generation
Impact: A local attacker may gain access to user's Keychain items
Description: This issue was addressed with improved permissions
checking.
CVE-2026-28864: Alex Radocea

UIFoundation
Available for: iPhone XS, iPhone XS Max, iPhone XR, iPad 7th generation
Impact: An app may be able to cause a denial-of-service
Description: A stack overflow was addressed with improved input
validation.
CVE-2026-28852: Caspian Tarafdar

Vision
Available for: iPhone XS, iPhone XS Max, iPhone XR, iPad 7th generation
Impact: Parsing a maliciously crafted file may lead to an unexpected app
termination
Description: The issue was addressed with improved memory handling.
CVE-2026-20657: Andrew Becker

WebKit
Available for: iPhone XS, iPhone XS Max, iPhone XR, iPad 7th generation
Impact: Processing maliciously crafted web content may prevent Content
Security Policy from being enforced
Description: This issue was addressed through improved state management.
WebKit Bugzilla: 304951
CVE-2026-20665: webb

WebKit
Available for: iPhone XS, iPhone XS Max, iPhone XR, iPad 7th generation
Impact: Processing maliciously crafted web content may bypass Same
Origin Policy
Description: A cross-origin issue in the Navigation API was addressed
with improved input validation.
WebKit Bugzilla: 306050
CVE-2026-20643: Thomas Espach

WebKit
Available for: iPhone XS, iPhone XS Max, iPhone XR, iPad 7th generation
Impact: A remote attacker may be able to view leaked D...