---
title: APPLE-SA-2022-10-27-1 iOS 15.7.1 and iPadOS 15.7.1
url: https://seclists.org/fulldisclosure/2022/Oct/37
source: Full Disclosure
date: 2022-10-31
fetch_date: 2025-10-03T21:22:09.844106
---

# APPLE-SA-2022-10-27-1 iOS 15.7.1 and iPadOS 15.7.1

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

[![Previous](/images/left-icon-16x16.png)](36)
[By Date](date.html#37)
[![Next](/images/right-icon-16x16.png)](38)

[![Previous](/images/left-icon-16x16.png)](36)
[By Thread](index.html#37)
[![Next](/images/right-icon-16x16.png)](38)

![](/shared/images/nst-icons.svg#search)

# APPLE-SA-2022-10-27-1 iOS 15.7.1 and iPadOS 15.7.1

---

*From*: Apple Product Security via Fulldisclosure <fulldisclosure () seclists org>
*Date*: Thu, 27 Oct 2022 18:23:04 -0700

---

```
-----BEGIN PGP SIGNED MESSAGE-----
Hash: SHA256

APPLE-SA-2022-10-27-1 iOS 15.7.1 and iPadOS 15.7.1

iOS 15.7.1 and iPadOS 15.7.1 addresses the following issues.
Information about the security content is also available at
https://support.apple.com/HT213490.

Apple Neural Engine
Available for: iPhone 6s and later, iPad Pro (all models), iPad Air 2
and later, iPad 5th generation and later, iPad mini 4 and later, and
iPod touch (7th generation)
Impact: An app may be able to execute arbitrary code with kernel
privileges
Description: The issue was addressed with improved memory handling.
CVE-2022-32932: Mohamed Ghannam (@_simo36)

Audio
Available for: iPhone 6s and later, iPad Pro (all models), iPad Air 2
and later, iPad 5th generation and later, iPad mini 4 and later, and
iPod touch (7th generation)
Impact: Parsing a maliciously crafted audio file may lead to
disclosure of user information
Description: The issue was addressed with improved memory handling.
CVE-2022-42798: Anonymous working with Trend Micro Zero Day
Initiative

Backup
Available for: iPhone 6s and later, iPad Pro (all models), iPad Air 2
and later, iPad 5th generation and later, iPad mini 4 and later, and
iPod touch (7th generation)
Impact: An app may be able to access iOS backups
Description: A permissions issue was addressed with additional
restrictions.
CVE-2022-32929: Csaba Fitzl (@theevilbit) of Offensive Security

FaceTime
Available for: iPhone 6s and later, iPad Pro (all models), iPad Air 2
and later, iPad 5th generation and later, iPad mini 4 and later, and
iPod touch (7th generation)
Impact: A user may be able to view restricted content from the lock
screen
Description: A lock screen issue was addressed with improved state
management.
CVE-2022-32935: Bistrit Dahal

Graphics Driver
Available for: iPhone 6s and later, iPad Pro (all models), iPad Air 2
and later, iPad 5th generation and later, iPad mini 4 and later, and
iPod touch (7th generation)
Impact: An app may be able to execute arbitrary code with kernel
privileges
Description: The issue was addressed with improved bounds checks.
CVE-2022-32939: Willy R. Vasquez of The University of Texas at Austin

Image Processing
Available for: iPhone 6s and later, iPad Pro (all models), iPad Air 2
and later, iPad 5th generation and later, iPad mini 4 and later, and
iPod touch (7th generation)
Impact: An app may be able to execute arbitrary code with kernel
privileges
Description: This issue was addressed with improved checks.
CVE-2022-32949: Tingting Yin of Tsinghua University

Kernel
Available for: iPhone 6s and later, iPad Pro (all models), iPad Air 2
and later, iPad 5th generation and later, iPad mini 4 and later, and
iPod touch (7th generation)
Impact: An app may be able to execute arbitrary code with kernel
privileges
Description: A memory corruption issue was addressed with improved
state management.
CVE-2022-32944: Tim Michaud (@TimGMichaud) of Moveworks.ai

Kernel
Available for: iPhone 6s and later, iPad Pro (all models), iPad Air 2
and later, iPad 5th generation and later, iPad mini 4 and later, and
iPod touch (7th generation)
Impact: An app may be able to execute arbitrary code with kernel
privileges
Description: A race condition was addressed with improved locking.
CVE-2022-42803: Xinru Chi of Pangu Lab, John Aakerblom (@jaakerblom)

Kernel
Available for: iPhone 6s and later, iPad Pro (all models), iPad Air 2
and later, iPad 5th generation and later, iPad mini 4 and later, and
iPod touch (7th generation)
Impact: An app with root privileges may be able to execute arbitrary
code with kernel privileges
Description: The issue was addressed with improved bounds checks.
CVE-2022-32926: Tim Michaud (@TimGMichaud) of Moveworks.ai

Kernel
Available for: iPhone 6s and later, iPad Pro (all models), iPad Air 2
and later, iPad 5th generation and later, iPad mini 4 and later, and
iPod touch (7th generation)
Impact: An application may be able to execute arbitrary code with
kernel privileges. Apple is aware of a report that this issue may
have been actively exploited.
Description: An out-of-bounds write issue was addressed with improved
bounds checking.
CVE-2022-42827: an anonymous researcher

Kernel
Available for: iPhone 6s and later, iPad Pro (all models), iPad Air 2
and later, iPad 5th generation and later, iPad mini 4 and later, and
iPod touch (7th generation)
Impact: An app may be able to execute arbitrary code with kernel
privileges
Description: A logic issue was addressed with improved checks.
CVE-2022-42801: Ian Beer of Google Project Zero

Model I/O
Available for: iPhone 6s and later, iPad Pro (all models), iPad Air 2
and later, iPad 5th generation and later, iPad mini 4 and later, and
iPod touch (7th generation)
Impact: Processing a maliciously crafted USD file may disclose memory
contents
Description: The issue was addressed with improved memory handling.
CVE-2022-42810: Xingwei Lin (@xwlin_roy) and Yinyi Wu of Ant Security
Light-Year Lab

ppp
Available for: iPhone 6s and later, iPad Pro (all models), iPad Air 2
and later, iPad 5th generation and later, iPad mini 4 and later, and
iPod touch (7th generation)
Impact: A buffer overflow may result in arbitrary code execution
Description: The issue was addressed with improved bounds checks.
CVE-2022-32941: an anonymous researcher

Safari
Available for: iPhone 6s and later, iPad Pro (all models), iPad Air 2
and later, iPad 5th generation and later, iPad mini 4 and later, and
iPod touch (7th generation)
Impact: Visiting a maliciously crafted website may leak sensitive
data
Description: A logic issue was addressed with improved state
management.
CVE-2022-42817: Mir Masood Ali, PhD student, University of Illinois
at Chicago; Binoy Chitale, MS student, Stony Brook University;
Mohammad Ghasemisharif, PhD Candidate, University of Illinois at
Chicago; Chris Kanich, Associate Professor, University of Illinois at
Chicago

WebKit
Available for: iPhone 6s and later, iPad Pro (all models), iPad Air 2
and later, iPad 5th generation and later, iPad mini 4 and later, and
iPod touch (7th generation)
Impact: Processing maliciously crafted web content may disclose
internal states of the app
Description: A correctness issue in the JIT was addressed with
improved checks.
WebKit Bugzilla: 242964
CVE-2022-32923: Wonyoung Jung (@nonetype_pwn) of KAIST Hacking Lab

Wi-Fi
Available for: iPhone 6s and later, iPad Pro (all models), iPad Air 2
and later, iPad 5th generation and later, iPad mini 4 and later, and
iPod touch (7th generation)
Impact: Joining a malicious Wi-Fi network may result in a denial-of-
service of the Settings app
Description: The issue was addressed with improved memory handling.
CVE-2022-32927: Dr Hideaki Goto of Tohoku University, Japan

zlib
Available for: iPhone 6s and later, iPad Pro (all models), iPad Air 2
and later, iPad 5th generation and later, iPad mini 4 and later, and
iPod touch (7th generation)
Impact: A user may be able to cause unexpected app termination or
arbitrary code execution
Description: This issue was addressed with improved chec...