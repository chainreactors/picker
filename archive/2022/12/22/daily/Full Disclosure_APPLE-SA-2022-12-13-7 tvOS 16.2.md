---
title: APPLE-SA-2022-12-13-7 tvOS 16.2
url: https://seclists.org/fulldisclosure/2022/Dec/26
source: Full Disclosure
date: 2022-12-22
fetch_date: 2025-10-04T02:15:04.287370
---

# APPLE-SA-2022-12-13-7 tvOS 16.2

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

[![Previous](/images/left-icon-16x16.png)](25)
[By Date](date.html#26)
[![Next](/images/right-icon-16x16.png)](27)

[![Previous](/images/left-icon-16x16.png)](25)
[By Thread](index.html#26)
[![Next](/images/right-icon-16x16.png)](27)

![](/shared/images/nst-icons.svg#search)

# APPLE-SA-2022-12-13-7 tvOS 16.2

---

*From*: Apple Product Security via Fulldisclosure <fulldisclosure () seclists org>
*Date*: Tue, 13 Dec 2022 16:35:17 -0800

---

```
-----BEGIN PGP SIGNED MESSAGE-----
Hash: SHA256

APPLE-SA-2022-12-13-7 tvOS 16.2

tvOS 16.2 addresses the following issues.
Information about the security content is also available at
https://support.apple.com/HT213535.

Accounts
Available for: Apple TV 4K, Apple TV 4K (2nd generation and later),
and Apple TV HD
Impact: A user may be able to view sensitive user information
Description: This issue was addressed with improved data protection.
CVE-2022-42843: Mickey Jin (@patch1t)

AppleAVD
Available for: Apple TV 4K, Apple TV 4K (2nd generation and later),
and Apple TV HD
Impact: Parsing a maliciously crafted video file may lead to kernel
code execution
Description: An out-of-bounds write issue was addressed with improved
input validation.
CVE-2022-46694: Andrey Labunets and Nikita Tarakanov

AppleMobileFileIntegrity
Available for: Apple TV 4K, Apple TV 4K (2nd generation and later),
and Apple TV HD
Impact: An app may be able to bypass Privacy preferences
Description: This issue was addressed by enabling hardened runtime.
CVE-2022-42865: Wojciech Reguła (@_r3ggi) of SecuRing

AVEVideoEncoder
Available for: Apple TV 4K, Apple TV 4K (2nd generation and later),
and Apple TV HD
Impact: An app may be able to execute arbitrary code with kernel
privileges
Description: A logic issue was addressed with improved checks.
CVE-2022-42848: ABC Research s.r.o

ImageIO
Available for: Apple TV 4K, Apple TV 4K (2nd generation and later),
and Apple TV HD
Impact: Processing a maliciously crafted file may lead to arbitrary
code execution
Description: An out-of-bounds write issue was addressed with improved
input validation.
CVE-2022-46693: Mickey Jin (@patch1t)

ImageIO
Available for: Apple TV 4K, Apple TV 4K (2nd generation and later),
and Apple TV HD
Impact: Parsing a maliciously crafted TIFF file may lead to
disclosure of user information
Description: The issue was addressed with improved memory handling.
CVE-2022-42851: Mickey Jin (@patch1t)

IOHIDFamily
Available for: Apple TV 4K, Apple TV 4K (2nd generation and later),
and Apple TV HD
Impact: An app may be able to execute arbitrary code with kernel
privileges
Description: A race condition was addressed with improved state
handling.
CVE-2022-42864: Tommy Muir (@Muirey03)

IOMobileFrameBuffer
Available for: Apple TV 4K, Apple TV 4K (2nd generation and later),
and Apple TV HD
Impact: An app may be able to execute arbitrary code with kernel
privileges
Description: An out-of-bounds write issue was addressed with improved
input validation.
CVE-2022-46690: John Aakerblom (@jaakerblom)

Kernel
Available for: Apple TV 4K, Apple TV 4K (2nd generation and later),
and Apple TV HD
Impact: An app may be able to execute arbitrary code with kernel
privileges
Description: A race condition was addressed with additional
validation.
CVE-2022-46689: Ian Beer of Google Project Zero

Kernel
Available for: Apple TV 4K, Apple TV 4K (2nd generation and later),
and Apple TV HD
Impact: Connecting to a malicious NFS server may lead to arbitrary
code execution with kernel privileges
Description: The issue was addressed with improved bounds checks.
CVE-2022-46701: Felix Poulin-Belanger

Kernel
Available for: Apple TV 4K, Apple TV 4K (2nd generation and later),
and Apple TV HD
Impact: A remote user may be able to cause kernel code execution
Description: The issue was addressed with improved memory handling.
CVE-2022-42842: pattern-f (@pattern_F_) of Ant Security Light-Year
Lab

Kernel
Available for: Apple TV 4K, Apple TV 4K (2nd generation and later),
and Apple TV HD
Impact: An app with root privileges may be able to execute arbitrary
code with kernel privileges
Description: The issue was addressed with improved memory handling.
CVE-2022-42845: Adam Doupé of ASU SEFCOM

libxml2
Available for: Apple TV 4K, Apple TV 4K (2nd generation and later),
and Apple TV HD
Impact: A remote user may be able to cause unexpected app termination
or arbitrary code execution
Description: An integer overflow was addressed through improved input
validation.
CVE-2022-40303: Maddie Stone of Google Project Zero

libxml2
Available for: Apple TV 4K, Apple TV 4K (2nd generation and later),
and Apple TV HD
Impact: A remote user may be able to cause unexpected app termination
or arbitrary code execution
Description: This issue was addressed with improved checks.
CVE-2022-40304: Ned Williamson and Nathan Wachholz of Google Project
Zero

Preferences
Available for: Apple TV 4K, Apple TV 4K (2nd generation and later),
and Apple TV HD
Impact: An app may be able to use arbitrary entitlements
Description: A logic issue was addressed with improved state
management.
CVE-2022-42855: Ivan Fratric of Google Project Zero

Safari
Available for: Apple TV 4K, Apple TV 4K (2nd generation and later),
and Apple TV HD
Impact: Visiting a website that frames malicious content may lead to
UI spoofing
Description: A spoofing issue existed in the handling of URLs. This
issue was addressed with improved input validation.
CVE-2022-46695: KirtiKumar Anandrao Ramchandani

Software Update
Available for: Apple TV 4K, Apple TV 4K (2nd generation and later),
and Apple TV HD
Impact: A user may be able to elevate privileges
Description: An access issue existed with privileged API calls. This
issue was addressed with additional restrictions.
CVE-2022-42849: Mickey Jin (@patch1t)

Weather
Available for: Apple TV 4K, Apple TV 4K (2nd generation and later),
and Apple TV HD
Impact: An app may be able to read sensitive location information
Description: The issue was addressed with improved handling of
caches.
CVE-2022-42866: an anonymous researcher

WebKit
Available for: Apple TV 4K, Apple TV 4K (2nd generation and later),
and Apple TV HD
Impact: Processing maliciously crafted web content may lead to
arbitrary code execution
Description: A use after free issue was addressed with improved
memory management.
WebKit Bugzilla: 245521
CVE-2022-42867: Maddie Stone of Google Project Zero

WebKit
Available for: Apple TV 4K, Apple TV 4K (2nd generation and later),
and Apple TV HD
Impact: Processing maliciously crafted web content may lead to
arbitrary code execution
Description: A memory consumption issue was addressed with improved
memory handling.
WebKit Bugzilla: 245466
CVE-2022-46691: an anonymous researcher

WebKit
Available for: Apple TV 4K, Apple TV 4K (2nd generation and later),
and Apple TV HD
Impact: Processing maliciously crafted web content may bypass Same
Origin Policy
Description: A logic issue was addressed with improved state
management.
WebKit Bugzilla: 246783
CVE-2022-46692: KirtiKumar Anandrao Ramchandani

WebKit
Available for: Apple TV 4K, Apple TV 4K (2nd generation and later),
and Apple TV HD
Impact: Processing maliciously crafted web content may result in the
disclosure of process memory
Description: The issue was addressed with improved memory handling.
CVE-2022-42852: hazbinhotel working with Trend Micro Zero Day
Initiative

WebKit
Available for: Apple TV 4K, Apple TV 4K (2nd generation and later),
and Apple TV HD
Impact: Processing maliciously crafted web content may lead to
...