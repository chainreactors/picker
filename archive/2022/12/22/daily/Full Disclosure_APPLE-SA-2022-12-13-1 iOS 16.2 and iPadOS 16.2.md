---
title: APPLE-SA-2022-12-13-1 iOS 16.2 and iPadOS 16.2
url: https://seclists.org/fulldisclosure/2022/Dec/20
source: Full Disclosure
date: 2022-12-22
fetch_date: 2025-10-04T02:15:11.858927
---

# APPLE-SA-2022-12-13-1 iOS 16.2 and iPadOS 16.2

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

[![Previous](/images/left-icon-16x16.png)](19)
[By Date](date.html#20)
[![Next](/images/right-icon-16x16.png)](21)

[![Previous](/images/left-icon-16x16.png)](19)
[By Thread](index.html#20)
[![Next](/images/right-icon-16x16.png)](21)

![](/shared/images/nst-icons.svg#search)

# APPLE-SA-2022-12-13-1 iOS 16.2 and iPadOS 16.2

---

*From*: Apple Product Security via Fulldisclosure <fulldisclosure () seclists org>
*Date*: Tue, 13 Dec 2022 16:34:26 -0800

---

```
-----BEGIN PGP SIGNED MESSAGE-----
Hash: SHA256

APPLE-SA-2022-12-13-1 iOS 16.2 and iPadOS 16.2

iOS 16.2 and iPadOS 16.2 addresses the following issues.
Information about the security content is also available at
https://support.apple.com/HT213530.

Accounts
Available for: iPhone 8 and later, iPad Pro (all models), iPad Air
3rd generation and later, iPad 5th generation and later, and iPad
mini 5th generation and later
Impact: A user may be able to view sensitive user information
Description: This issue was addressed with improved data protection.
CVE-2022-42843: Mickey Jin (@patch1t)

AppleAVD
Available for: iPhone 8 and later, iPad Pro (all models), iPad Air
3rd generation and later, iPad 5th generation and later, and iPad
mini 5th generation and later
Impact: Parsing a maliciously crafted video file may lead to kernel
code execution
Description: An out-of-bounds write issue was addressed with improved
input validation.
CVE-2022-46694: Andrey Labunets and Nikita Tarakanov

AppleMobileFileIntegrity
Available for: iPhone 8 and later, iPad Pro (all models), iPad Air
3rd generation and later, iPad 5th generation and later, and iPad
mini 5th generation and later
Impact: An app may be able to bypass Privacy preferences
Description: This issue was addressed by enabling hardened runtime.
CVE-2022-42865: Wojciech Reguła (@_r3ggi) of SecuRing

AVEVideoEncoder
Available for: iPhone 8 and later, iPad Pro (all models), iPad Air
3rd generation and later, iPad 5th generation and later, and iPad
mini 5th generation and later
Impact: An app may be able to execute arbitrary code with kernel
privileges
Description: A logic issue was addressed with improved checks.
CVE-2022-42848: ABC Research s.r.o

CoreServices
Available for: iPhone 8 and later, iPad Pro (all models), iPad Air
3rd generation and later, iPad 5th generation and later, and iPad
mini 5th generation and later
Impact: An app may be able to bypass Privacy preferences
Description: Multiple issues were addressed by removing the
vulnerable code.
CVE-2022-42859: Mickey Jin (@patch1t), Csaba Fitzl (@theevilbit) of
Offensive Security

GPU Drivers
Available for: iPhone 8 and later, iPad Pro (all models), iPad Air
3rd generation and later, iPad 5th generation and later, and iPad
mini 5th generation and later
Impact: An app may be able to disclose kernel memory
Description: The issue was addressed with improved memory handling.
CVE-2022-46702: Xia0o0o0o of W4terDr0p, Sun Yat-sen University

Graphics Driver
Available for: iPhone 8 and later, iPad Pro (all models), iPad Air
3rd generation and later, iPad 5th generation and later, and iPad
mini 5th generation and later
Impact: An app may be able to execute arbitrary code with kernel
privileges
Description: The issue was addressed with improved memory handling.
CVE-2022-42850: Willy R. Vasquez of The University of Texas at Austin

Graphics Driver
Available for: iPhone 8 and later, iPad Pro (all models), iPad Air
3rd generation and later, iPad 5th generation and later, and iPad
mini 5th generation and later
Impact: Parsing a maliciously crafted video file may lead to
unexpected system termination
Description: The issue was addressed with improved memory handling.
CVE-2022-42846: Willy R. Vasquez of The University of Texas at Austin

ImageIO
Available for: iPhone 8 and later, iPad Pro (all models), iPad Air
3rd generation and later, iPad 5th generation and later, and iPad
mini 5th generation and later
Impact: Processing a maliciously crafted file may lead to arbitrary
code execution
Description: An out-of-bounds write issue was addressed with improved
input validation.
CVE-2022-46693: Mickey Jin (@patch1t)

ImageIO
Available for: iPhone 8 and later, iPad Pro (all models), iPad Air
3rd generation and later, iPad 5th generation and later, and iPad
mini 5th generation and later
Impact: Parsing a maliciously crafted TIFF file may lead to
disclosure of user information
Description: The issue was addressed with improved memory handling.
CVE-2022-42851: Mickey Jin (@patch1t)

IOHIDFamily
Available for: iPhone 8 and later, iPad Pro (all models), iPad Air
3rd generation and later, iPad 5th generation and later, and iPad
mini 5th generation and later
Impact: An app may be able to execute arbitrary code with kernel
privileges
Description: A race condition was addressed with improved state
handling.
CVE-2022-42864: Tommy Muir (@Muirey03)

IOMobileFrameBuffer
Available for: iPhone 8 and later, iPad Pro (all models), iPad Air
3rd generation and later, iPad 5th generation and later, and iPad
mini 5th generation and later
Impact: An app may be able to execute arbitrary code with kernel
privileges
Description: An out-of-bounds write issue was addressed with improved
input validation.
CVE-2022-46690: John Aakerblom (@jaakerblom)

iTunes Store
Available for: iPhone 8 and later, iPad Pro (all models), iPad Air
3rd generation and later, iPad 5th generation and later, and iPad
mini 5th generation and later
Impact: A remote user may be able to cause unexpected app termination
or arbitrary code execution
Description: An issue existed in the parsing of URLs. This issue was
addressed with improved input validation.
CVE-2022-42837: Weijia Dai (@dwj1210) of Momo Security

Kernel
Available for: iPhone 8 and later, iPad Pro (all models), iPad Air
3rd generation and later, iPad 5th generation and later, and iPad
mini 5th generation and later
Impact: An app may be able to execute arbitrary code with kernel
privileges
Description: A race condition was addressed with additional
validation.
CVE-2022-46689: Ian Beer of Google Project Zero

Kernel
Available for: iPhone 8 and later, iPad Pro (all models), iPad Air
3rd generation and later, iPad 5th generation and later, and iPad
mini 5th generation and later
Impact: Connecting to a malicious NFS server may lead to arbitrary
code execution with kernel privileges
Description: The issue was addressed with improved bounds checks.
CVE-2022-46701: Felix Poulin-Belanger

Kernel
Available for: iPhone 8 and later, iPad Pro (all models), iPad Air
3rd generation and later, iPad 5th generation and later, and iPad
mini 5th generation and later
Impact: A remote user may be able to cause kernel code execution
Description: The issue was addressed with improved memory handling.
CVE-2022-42842: pattern-f (@pattern_F_) of Ant Security Light-Year
Lab

Kernel
Available for: iPhone 8 and later, iPad Pro (all models), iPad Air
3rd generation and later, iPad 5th generation and later, and iPad
mini 5th generation and later
Impact: An app may be able to break out of its sandbox
Description: This issue was addressed with improved checks.
CVE-2022-42861: pattern-f (@pattern_F_) of Ant Security Light-Year
Lab

Kernel
Available for: iPhone 8 and later, iPad Pro (all models), iPad Air
3rd generation and later, iPad 5th generation and later, and iPad
mini 5th generation and later
Impact: An app may be able to break out of its sandbox
Description: The issue was addressed with improved memory handling.
CVE-2022-42844: pattern-f (@pattern_F_) of Ant Sec...