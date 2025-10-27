---
title: APPLE-SA-2022-12-13-2 iOS 15.7.2 and iPadOS 15.7.2
url: https://seclists.org/fulldisclosure/2022/Dec/21
source: Full Disclosure
date: 2022-12-22
fetch_date: 2025-10-04T02:15:10.156992
---

# APPLE-SA-2022-12-13-2 iOS 15.7.2 and iPadOS 15.7.2

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

[![Previous](/images/left-icon-16x16.png)](20)
[By Date](date.html#21)
[![Next](/images/right-icon-16x16.png)](22)

[![Previous](/images/left-icon-16x16.png)](20)
[By Thread](index.html#21)
[![Next](/images/right-icon-16x16.png)](22)

![](/shared/images/nst-icons.svg#search)

# APPLE-SA-2022-12-13-2 iOS 15.7.2 and iPadOS 15.7.2

---

*From*: Apple Product Security via Fulldisclosure <fulldisclosure () seclists org>
*Date*: Tue, 13 Dec 2022 16:34:34 -0800

---

```
-----BEGIN PGP SIGNED MESSAGE-----
Hash: SHA256

APPLE-SA-2022-12-13-2 iOS 15.7.2 and iPadOS 15.7.2

iOS 15.7.2 and iPadOS 15.7.2 addresses the following issues.
Information about the security content is also available at
https://support.apple.com/HT213531.

AppleAVD
Available for: iPhone 6s (all models), iPhone 7 (all models), iPhone
SE (1st generation), iPad Pro (all models), iPad Air 2 and later,
iPad 5th generation and later, iPad mini 4 and later, and iPod touch
(7th generation)
Impact: Parsing a maliciously crafted video file may lead to kernel
code execution
Description: An out-of-bounds write issue was addressed with improved
input validation.
CVE-2022-46694: Andrey Labunets and Nikita Tarakanov

AVEVideoEncoder
Available for: iPhone 6s (all models), iPhone 7 (all models), iPhone
SE (1st generation), iPad Pro (all models), iPad Air 2 and later,
iPad 5th generation and later, iPad mini 4 and later, and iPod touch
(7th generation)
Impact: An app may be able to execute arbitrary code with kernel
privileges
Description: A logic issue was addressed with improved checks.
CVE-2022-42848: ABC Research s.r.o

File System
Available for: iPhone 6s (all models), iPhone 7 (all models), iPhone
SE (1st generation), iPad Pro (all models), iPad Air 2 and later,
iPad 5th generation and later, iPad mini 4 and later, and iPod touch
(7th generation)
Impact: An app may be able to break out of its sandbox
Description: This issue was addressed with improved checks.
CVE-2022-42861: pattern-f (@pattern_F_) of Ant Security Light-Year
Lab

Graphics Driver
Available for: iPhone 6s (all models), iPhone 7 (all models), iPhone
SE (1st generation), iPad Pro (all models), iPad Air 2 and later,
iPad 5th generation and later, iPad mini 4 and later, and iPod touch
(7th generation)
Impact: Parsing a maliciously crafted video file may lead to
unexpected system termination
Description: The issue was addressed with improved memory handling.
CVE-2022-42846: Willy R. Vasquez of The University of Texas at Austin

IOHIDFamily
Available for: iPhone 6s (all models), iPhone 7 (all models), iPhone
SE (1st generation), iPad Pro (all models), iPad Air 2 and later,
iPad 5th generation and later, iPad mini 4 and later, and iPod touch
(7th generation)
Impact: An app may be able to execute arbitrary code with kernel
privileges
Description: A race condition was addressed with improved state
handling.
CVE-2022-42864: Tommy Muir (@Muirey03)

iTunes Store
Available for: iPhone 6s (all models), iPhone 7 (all models), iPhone
SE (1st generation), iPad Pro (all models), iPad Air 2 and later,
iPad 5th generation and later, iPad mini 4 and later, and iPod touch
(7th generation)
Impact: A remote user may be able to cause unexpected app termination
or arbitrary code execution
Description: An issue existed in the parsing of URLs. This issue was
addressed with improved input validation.
CVE-2022-42837: Weijia Dai (@dwj1210) of Momo Security

Kernel
Available for: iPhone 6s (all models), iPhone 7 (all models), iPhone
SE (1st generation), iPad Pro (all models), iPad Air 2 and later,
iPad 5th generation and later, iPad mini 4 and later, and iPod touch
(7th generation)
Impact: An app may be able to execute arbitrary code with kernel
privileges
Description: A race condition was addressed with additional
validation.
CVE-2022-46689: Ian Beer of Google Project Zero

libxml2
Available for: iPhone 6s (all models), iPhone 7 (all models), iPhone
SE (1st generation), iPad Pro (all models), iPad Air 2 and later,
iPad 5th generation and later, iPad mini 4 and later, and iPod touch
(7th generation)
Impact: A remote user may be able to cause unexpected app termination
or arbitrary code execution
Description: An integer overflow was addressed through improved input
validation.
CVE-2022-40303: Maddie Stone of Google Project Zero

libxml2
Available for: iPhone 6s (all models), iPhone 7 (all models), iPhone
SE (1st generation), iPad Pro (all models), iPad Air 2 and later,
iPad 5th generation and later, iPad mini 4 and later, and iPod touch
(7th generation)
Impact: A remote user may be able to cause unexpected app termination
or arbitrary code execution
Description: This issue was addressed with improved checks.
CVE-2022-40304: Ned Williamson and Nathan Wachholz of Google Project
Zero

ppp
Available for: iPhone 6s (all models), iPhone 7 (all models), iPhone
SE (1st generation), iPad Pro (all models), iPad Air 2 and later,
iPad 5th generation and later, iPad mini 4 and later, and iPod touch
(7th generation)
Impact: An app may be able to execute arbitrary code with kernel
privileges
Description: The issue was addressed with improved memory handling.
CVE-2022-42840: an anonymous researcher

Preferences
Available for: iPhone 6s (all models), iPhone 7 (all models), iPhone
SE (1st generation), iPad Pro (all models), iPad Air 2 and later,
iPad 5th generation and later, iPad mini 4 and later, and iPod touch
(7th generation)
Impact: An app may be able to use arbitrary entitlements
Description: A logic issue was addressed with improved state
management.
CVE-2022-42855: Ivan Fratric of Google Project Zero

Safari
Available for: iPhone 6s (all models), iPhone 7 (all models), iPhone
SE (1st generation), iPad Pro (all models), iPad Air 2 and later,
iPad 5th generation and later, iPad mini 4 and later, and iPod touch
(7th generation)
Impact: Visiting a website that frames malicious content may lead to
UI spoofing
Description: A spoofing issue existed in the handling of URLs. This
issue was addressed with improved input validation.
CVE-2022-46695: KirtiKumar Anandrao Ramchandani

WebKit
Available for: iPhone 6s (all models), iPhone 7 (all models), iPhone
SE (1st generation), iPad Pro (all models), iPad Air 2 and later,
iPad 5th generation and later, iPad mini 4 and later, and iPod touch
(7th generation)
Impact: Processing maliciously crafted web content may lead to
arbitrary code execution
Description: A memory consumption issue was addressed with improved
memory handling.
WebKit Bugzilla: 245466
CVE-2022-46691: an anonymous researcher

WebKit
Available for: iPhone 6s (all models), iPhone 7 (all models), iPhone
SE (1st generation), iPad Pro (all models), iPad Air 2 and later,
iPad 5th generation and later, iPad mini 4 and later, and iPod touch
(7th generation)
Impact: Processing maliciously crafted web content may result in the
disclosure of process memory
Description: The issue was addressed with improved memory handling.
CVE-2022-42852: hazbinhotel working with Trend Micro Zero Day
Initiative

WebKit
Available for: iPhone 6s (all models), iPhone 7 (all models), iPhone
SE (1st generation), iPad Pro (all models), iPad Air 2 and later,
iPad 5th generation and later, iPad mini 4 and later, and iPod touch
(7th generation)
Impact: Processing maliciously crafted web content may bypass Same
Origin Policy
Description: A logic issue was addressed with improved state
management.
WebKit Bugzilla: 246783
CVE-2022-46692: KirtiKumar Anandrao Ramchandani

WebKit
Available for: iPhone 6s (all models), iPhone 7 (all mod...