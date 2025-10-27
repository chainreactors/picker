---
title: APPLE-SA-2022-10-27-2 Additional information for APPLE-SA-2022-10-24-1 iOS 16.1 and iPadOS 16
url: https://seclists.org/fulldisclosure/2022/Oct/38
source: Full Disclosure
date: 2022-10-31
fetch_date: 2025-10-03T21:22:08.695101
---

# APPLE-SA-2022-10-27-2 Additional information for APPLE-SA-2022-10-24-1 iOS 16.1 and iPadOS 16

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

[![Previous](/images/left-icon-16x16.png)](37)
[By Date](date.html#38)
[![Next](/images/right-icon-16x16.png)](39)

[![Previous](/images/left-icon-16x16.png)](37)
[By Thread](index.html#38)
[![Next](/images/right-icon-16x16.png)](39)

![](/shared/images/nst-icons.svg#search)

# APPLE-SA-2022-10-27-2 Additional information for APPLE-SA-2022-10-24-1 iOS 16.1 and iPadOS 16

---

*From*: Apple Product Security via Fulldisclosure <fulldisclosure () seclists org>
*Date*: Thu, 27 Oct 2022 18:23:12 -0700

---

```
-----BEGIN PGP SIGNED MESSAGE-----
Hash: SHA256

APPLE-SA-2022-10-27-2 Additional information for APPLE-SA-2022-10-24-1 iOS 16.1 and iPadOS 16

iOS 16.1 and iPadOS 16 addresses the following issues.
Information about the security content is also available at
https://support.apple.com/HT213489.

Apple Neural Engine
Available for: iPhone 8 and later, iPad Pro (all models), iPad Air
3rd generation and later, iPad 5th generation and later, iPad mini
5th generation and later
Impact: An app may be able to execute arbitrary code with kernel
privileges
Description: The issue was addressed with improved memory handling.
CVE-2022-32932: Mohamed Ghannam (@_simo36)
Entry added October 27, 2022

AppleMobileFileIntegrity
Available for: iPhone 8 and later, iPad Pro (all models), iPad Air
3rd generation and later, iPad 5th generation and later, iPad mini
5th generation and later
Impact: An app may be able to modify protected parts of the file
system
Description: This issue was addressed by removing additional
entitlements.
CVE-2022-42825: Mickey Jin (@patch1t)

Audio
Available for: iPhone 8 and later, iPad Pro (all models), iPad Air
3rd generation and later, iPad 5th generation and later, iPad mini
5th generation and later
Impact: Parsing a maliciously crafted audio file may lead to
disclosure of user information
Description: The issue was addressed with improved memory handling.
CVE-2022-42798: Anonymous working with Trend Micro Zero Day
Initiative
Entry added October 27, 2022

AVEVideoEncoder
Available for: iPhone 8 and later, iPad Pro (all models), iPad Air
3rd generation and later, iPad 5th generation and later, iPad mini
5th generation and later
Impact: An app may be able to execute arbitrary code with kernel
privileges
Description: The issue was addressed with improved bounds checks.
CVE-2022-32940: ABC Research s.r.o.

Backup
Available for: iPhone 8 and later, iPad Pro (all models), iPad Air
3rd generation and later, iPad 5th generation and later, iPad mini
5th generation and later
Impact: An app may be able to access iOS backups
Description: A permissions issue was addressed with additional
restrictions.
CVE-2022-32929: Csaba Fitzl (@theevilbit) of Offensive Security
Entry added October 27, 2022

CFNetwork
Available for: iPhone 8 and later, iPad Pro (all models), iPad Air
3rd generation and later, iPad 5th generation and later, iPad mini
5th generation and later
Impact: Processing a maliciously crafted certificate may lead to
arbitrary code execution
Description: A certificate validation issue existed in the handling
of WKWebView. This issue was addressed with improved validation.
CVE-2022-42813: Jonathan Zhang of Open Computing Facility
(ocf.berkeley.edu)

Core Bluetooth
Available for: iPhone 8 and later, iPad Pro (all models), iPad Air
3rd generation and later, iPad 5th generation and later, iPad mini
5th generation and later
Impact: An app may be able to record audio using a pair of connected
AirPods
Description: This issue was addressed with improved entitlements.
CVE-2022-32946: Guilherme Rambo of Best Buddy Apps (rambo.codes)

FaceTime
Available for: iPhone 8 and later, iPad Pro (all models), iPad Air
3rd generation and later, iPad 5th generation and later, iPad mini
5th generation and later
Impact: A user may be able to view restricted content from the lock
screen
Description: A lock screen issue was addressed with improved state
management.
CVE-2022-32935: Bistrit Dahal
Entry added October 27, 2022

GPU Drivers
Available for: iPhone 8 and later, iPad Pro (all models), iPad Air
3rd generation and later, iPad 5th generation and later, iPad mini
5th generation and later
Impact: An app may be able to execute arbitrary code with kernel
privileges
Description: The issue was addressed with improved memory handling.
CVE-2022-32947: Asahi Lina (@LinaAsahi)

Graphics Driver
Available for: iPhone 8 and later, iPad Pro (all models), iPad Air
3rd generation and later, iPad 5th generation and later, iPad mini
5th generation and later
Impact: An app may be able to execute arbitrary code with kernel
privileges
Description: The issue was addressed with improved bounds checks.
CVE-2022-32939: Willy R. Vasquez of The University of Texas at Austin
Entry added October 27, 2022

IOHIDFamily
Available for: iPhone 8 and later, iPad Pro (all models), iPad Air
3rd generation and later, iPad 5th generation and later, iPad mini
5th generation and later
Impact: An app may cause unexpected app termination or arbitrary code
execution
Description: A memory corruption issue was addressed with improved
state management.
CVE-2022-42820: Peter Pan ZhenPeng of STAR Labs

IOKit
Available for: iPhone 8 and later, iPad Pro (all models), iPad Air
3rd generation and later, iPad 5th generation and later, iPad mini
5th generation and later
Impact: An app may be able to execute arbitrary code with kernel
privileges
Description: A race condition was addressed with improved locking.
CVE-2022-42806: Tingting Yin of Tsinghua University

Kernel
Available for: iPhone 8 and later, iPad Pro (all models), iPad Air
3rd generation and later, iPad 5th generation and later, iPad mini
5th generation and later
Impact: An app may be able to execute arbitrary code with kernel
privileges
Description: A memory corruption issue was addressed with improved
state management.
CVE-2022-32944: Tim Michaud (@TimGMichaud) of Moveworks.ai
Entry added October 27, 2022

Kernel
Available for: iPhone 8 and later, iPad Pro (all models), iPad Air
3rd generation and later, iPad 5th generation and later, iPad mini
5th generation and later
Impact: An app may be able to execute arbitrary code with kernel
privileges
Description: A race condition was addressed with improved locking.
CVE-2022-42803: Xinru Chi of Pangu Lab, John Aakerblom (@jaakerblom)
Entry added October 27, 2022

Kernel
Available for: iPhone 8 and later, iPad Pro (all models), iPad Air
3rd generation and later, iPad 5th generation and later, iPad mini
5th generation and later
Impact: An app with root privileges may be able to execute arbitrary
code with kernel privileges
Description: The issue was addressed with improved bounds checks.
CVE-2022-32926: Tim Michaud (@TimGMichaud) of Moveworks.ai
Entry added October 27, 2022

Kernel
Available for: iPhone 8 and later, iPad Pro (all models), iPad Air
3rd generation and later, iPad 5th generation and later, iPad mini
5th generation and later
Impact: An app may be able to execute arbitrary code with kernel
privileges
Description: A logic issue was addressed with improved checks.
CVE-2022-42801: Ian Beer of Google Project Zero
Entry added October 27, 2022

Kernel
Available for: iPhone 8 and later, iPad Pro (all models), iPad Air
3rd generation and later, iPad 5th generation and later, iPad mini
5th generation and later
Impact: An app may be able to execute arbitrary code with kernel
privileges
Description: The issue was addressed with improved memory handling.
CVE-2022-32924: Ian Beer of Google Project Zero

Kernel
Available for: iPhone 8 ...