---
title: APPLE-SA-07-29-2024-2 iOS 17.6 and iPadOS 17.6
url: https://seclists.org/fulldisclosure/2024/Jul/16
source: Full Disclosure
date: 2024-07-30
fetch_date: 2025-10-06T17:47:11.575006
---

# APPLE-SA-07-29-2024-2 iOS 17.6 and iPadOS 17.6

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

# APPLE-SA-07-29-2024-2 iOS 17.6 and iPadOS 17.6

---

*From*: Apple Product Security via Fulldisclosure <fulldisclosure () seclists org>
*Date*: Mon, 29 Jul 2024 16:11:56 -0700

---

```
-----BEGIN PGP SIGNED MESSAGE-----
Hash: SHA256

APPLE-SA-07-29-2024-2 iOS 17.6 and iPadOS 17.6

iOS 17.6 and iPadOS 17.6 addresses the following issues.
Information about the security content is also available at
https://support.apple.com/HT214117.

Apple maintains a Security Releases page at
https://support.apple.com/HT201222 which lists recent
software updates with security advisories.

AppleMobileFileIntegrity
Available for: iPhone XS and later, iPad Pro 13-inch, iPad Pro 12.9-inch
2nd generation and later, iPad Pro 10.5-inch, iPad Pro 11-inch 1st
generation and later, iPad Air 3rd generation and later, iPad 6th
generation and later, and iPad mini 5th generation and later
Impact: An app may be able to bypass Privacy preferences
Description: A downgrade issue was addressed with additional code-
signing restrictions.
CVE-2024-40774: Mickey Jin (@patch1t)

CoreGraphics
Available for: iPhone XS and later, iPad Pro 13-inch, iPad Pro 12.9-inch
2nd generation and later, iPad Pro 10.5-inch, iPad Pro 11-inch 1st
generation and later, iPad Air 3rd generation and later, iPad 6th
generation and later, and iPad mini 5th generation and later
Impact: Processing a maliciously crafted file may lead to unexpected app
termination
Description: An out-of-bounds read issue was addressed with improved
input validation.
CVE-2024-40799: D4m0n

CoreMedia
Available for: iPhone XS and later, iPad Pro 13-inch, iPad Pro 12.9-inch
2nd generation and later, iPad Pro 10.5-inch, iPad Pro 11-inch 1st
generation and later, iPad Air 3rd generation and later, iPad 6th
generation and later, and iPad mini 5th generation and later
Impact: Processing a maliciously crafted video file may lead to
unexpected app termination
Description: An out-of-bounds write issue was addressed with improved
input validation.
CVE-2024-27873: Amir Bazine and Karsten König of CrowdStrike Counter
Adversary Operations

dyld
Available for: iPhone XS and later, iPad Pro 13-inch, iPad Pro 12.9-inch
2nd generation and later, iPad Pro 10.5-inch, iPad Pro 11-inch 1st
generation and later, iPad Air 3rd generation and later, iPad 6th
generation and later, and iPad mini 5th generation and later
Impact: A malicious attacker with arbitrary read and write capability
may be able to bypass Pointer Authentication
Description: A race condition was addressed with additional validation.
CVE-2024-40815: w0wbox

Family Sharing
Available for: iPhone XS and later, iPad Pro 13-inch, iPad Pro 12.9-inch
2nd generation and later, iPad Pro 10.5-inch, iPad Pro 11-inch 1st
generation and later, iPad Air 3rd generation and later, iPad 6th
generation and later, and iPad mini 5th generation and later
Impact: An app may be able to read sensitive location information
Description: This issue was addressed with improved data protection.
CVE-2024-40795: Csaba Fitzl (@theevilbit) of Kandji

ImageIO
Available for: iPhone XS and later, iPad Pro 13-inch, iPad Pro 12.9-inch
2nd generation and later, iPad Pro 10.5-inch, iPad Pro 11-inch 1st
generation and later, iPad Air 3rd generation and later, iPad 6th
generation and later, and iPad mini 5th generation and later
Impact: Processing an image may lead to a denial-of-service
Description: This is a vulnerability in open source code and Apple
Software is among the affected projects. The CVE-ID was assigned by a
third party. Learn more about the issue and CVE-ID at cve.org.
CVE-2023-6277
CVE-2023-52356

ImageIO
Available for: iPhone XS and later, iPad Pro 13-inch, iPad Pro 12.9-inch
2nd generation and later, iPad Pro 10.5-inch, iPad Pro 11-inch 1st
generation and later, iPad Air 3rd generation and later, iPad 6th
generation and later, and iPad mini 5th generation and later
Impact: Processing a maliciously crafted file may lead to unexpected app
termination
Description: An out-of-bounds read issue was addressed with improved
input validation.
CVE-2024-40806: Yisumi

ImageIO
Available for: iPhone XS and later, iPad Pro 13-inch, iPad Pro 12.9-inch
2nd generation and later, iPad Pro 10.5-inch, iPad Pro 11-inch 1st
generation and later, iPad Air 3rd generation and later, iPad 6th
generation and later, and iPad mini 5th generation and later
Impact: Processing a maliciously crafted file may lead to unexpected app
termination
Description: An out-of-bounds access issue was addressed with improved
bounds checking.
CVE-2024-40777: Junsung Lee working with Trend Micro Zero Day
Initiative, and Amir Bazine and Karsten König of CrowdStrike Counter
Adversary Operations

ImageIO
Available for: iPhone XS and later, iPad Pro 13-inch, iPad Pro 12.9-inch
2nd generation and later, iPad Pro 10.5-inch, iPad Pro 11-inch 1st
generation and later, iPad Air 3rd generation and later, iPad 6th
generation and later, and iPad mini 5th generation and later
Impact: Processing a maliciously crafted file may lead to unexpected app
termination
Description: An integer overflow was addressed with improved input
validation.
CVE-2024-40784: Junsung Lee working with Trend Micro Zero Day
Initiative, Gandalf4a

Kernel
Available for: iPhone XS and later, iPad Pro 13-inch, iPad Pro 12.9-inch
2nd generation and later, iPad Pro 10.5-inch, iPad Pro 11-inch 1st
generation and later, iPad Air 3rd generation and later, iPad 6th
generation and later, and iPad mini 5th generation and later
Impact: A local attacker may be able to determine kernel memory layout
Description: An information disclosure issue was addressed with improved
private data redaction for log entries.
CVE-2024-27863: CertiK SkyFall Team

Kernel
Available for: iPhone XS and later, iPad Pro 13-inch, iPad Pro 12.9-inch
2nd generation and later, iPad Pro 10.5-inch, iPad Pro 11-inch 1st
generation and later, iPad Air 3rd generation and later, iPad 6th
generation and later, and iPad mini 5th generation and later
Impact: A local attacker may be able to cause unexpected system shutdown
Description: A type confusion issue was addressed with improved memory
handling.
CVE-2024-40788: Minghao Lin and Jiaxun Zhu from Zhejiang University

libxpc
Available for: iPhone XS and later, iPad Pro 13-inch, iPad Pro 12.9-inch
2nd generation and later, iPad Pro 10.5-inch, iPad Pro 11-inch 1st
generation and later, iPad Air 3rd generation and later, iPad 6th
generation and later, and iPad mini 5th generation and later
Impact: An app may be able to bypass Privacy preferences
Description: A permissions issue was addressed with additional
restrictions.
CVE-2024-40805

Phone
Available for: iPhone XS and later, iPad Pro 13-inch, iPad Pro 12.9-inch
2nd generation and later, iPad Pro 10.5-inch, iPad Pro 11-inch 1st
generation and later, iPad Air 3rd generation and later, iPad 6th
generation and later, and iPad mini 5th generation and later
Impact: An attacker with physical access may be able to use Siri to
access sensitive user data
Description: A lock screen issue was addressed with improved state
management.
CVE-2024-40813: Jacob Braun

Photos Storage
Available for: iPhone XS and later, iPad Pro 13-inch, iPad Pro 12.9-inch
2nd generation and later, iPad Pro 10.5-inch, iPad Pro 11-...