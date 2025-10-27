---
title: APPLE-SA-2022-10-27-12 Additional information for APPLE-SA-2022-10-24-5 watchOS 9.1
url: https://seclists.org/fulldisclosure/2022/Oct/48
source: Full Disclosure
date: 2022-10-31
fetch_date: 2025-10-03T21:21:55.867574
---

# APPLE-SA-2022-10-27-12 Additional information for APPLE-SA-2022-10-24-5 watchOS 9.1

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

[![Previous](/images/left-icon-16x16.png)](47)
[By Date](date.html#48)
[![Next](/images/right-icon-16x16.png)](49)

[![Previous](/images/left-icon-16x16.png)](47)
[By Thread](index.html#48)
[![Next](/images/right-icon-16x16.png)](49)

![](/shared/images/nst-icons.svg#search)

# APPLE-SA-2022-10-27-12 Additional information for APPLE-SA-2022-10-24-5 watchOS 9.1

---

*From*: Apple Product Security via Fulldisclosure <fulldisclosure () seclists org>
*Date*: Thu, 27 Oct 2022 18:23:49 -0700

---

```
-----BEGIN PGP SIGNED MESSAGE-----
Hash: SHA256

APPLE-SA-2022-10-27-12 Additional information for APPLE-SA-2022-10-24-5 watchOS 9.1

watchOS 9.1 addresses the following issues.
Information about the security content is also available at
https://support.apple.com/HT213491.

AppleMobileFileIntegrity
Available for: Apple Watch Series 4 and later
Impact: An app may be able to modify protected parts of the file
system
Description: This issue was addressed by removing additional
entitlements.
CVE-2022-42825: Mickey Jin (@patch1t)

Apple Neural Engine
Available for: Apple Watch Series 4 and later
Impact: An app may be able to execute arbitrary code with kernel
privileges
Description: The issue was addressed with improved memory handling.
CVE-2022-32932: Mohamed Ghannam (@_simo36)
Entry added October 27, 2022

Audio
Available for: Apple Watch Series 4 and later
Impact: Parsing a maliciously crafted audio file may lead to
disclosure of user information
Description: The issue was addressed with improved memory handling.
CVE-2022-42798: Anonymous working with Trend Micro Zero Day
Initiative
Entry added October 27, 2022

AVEVideoEncoder
Available for: Apple Watch Series 4 and later
Impact: An app may be able to execute arbitrary code with kernel
privileges
Description: The issue was addressed with improved bounds checks.
CVE-2022-32940: ABC Research s.r.o.

CFNetwork
Available for: Apple Watch Series 4 and later
Impact: Processing a maliciously crafted certificate may lead to
arbitrary code execution
Description: A certificate validation issue existed in the handling
of WKWebView. This issue was addressed with improved validation.
CVE-2022-42813: Jonathan Zhang of Open Computing Facility
(ocf.berkeley.edu)

GPU Drivers
Available for: Apple Watch Series 4 and later
Impact: An app may be able to execute arbitrary code with kernel
privileges
Description: The issue was addressed with improved memory handling.
CVE-2022-32947: Asahi Lina (@LinaAsahi)

Kernel
Available for: Apple Watch Series 4 and later
Impact: An app may be able to execute arbitrary code with kernel
privileges
Description: The issue was addressed with improved memory handling.
CVE-2022-32924: Ian Beer of Google Project Zero

Kernel
Available for: Apple Watch Series 4 and later
Impact: A remote user may be able to cause kernel code execution
Description: An out-of-bounds write issue was addressed with improved
bounds checking.
CVE-2022-42808: Zweig of Kunlun Lab

Kernel
Available for: Apple Watch Series 4 and later
Impact: An app may be able to execute arbitrary code with kernel
privileges
Description: A memory corruption issue was addressed with improved
state management.
CVE-2022-32944: Tim Michaud (@TimGMichaud) of Moveworks.ai
Entry added October 27, 2022

Kernel
Available for: Apple Watch Series 4 and later
Impact: An app may be able to execute arbitrary code with kernel
privileges
Description: A race condition was addressed with improved locking.
CVE-2022-42803: Xinru Chi of Pangu Lab, John Aakerblom (@jaakerblom)
Entry added October 27, 2022

Kernel
Available for: Apple Watch Series 4 and later
Impact: An app with root privileges may be able to execute arbitrary
code with kernel privileges
Description: The issue was addressed with improved bounds checks.
CVE-2022-32926: Tim Michaud (@TimGMichaud) of Moveworks.ai
Entry added October 27, 2022

Kernel
Available for: Apple Watch Series 4 and later
Impact: An app may be able to execute arbitrary code with kernel
privileges
Description: A logic issue was addressed with improved checks.
CVE-2022-42801: Ian Beer of Google Project Zero
Entry added October 27, 2022

Safari
Available for: Apple Watch Series 4 and later
Impact: Visiting a maliciously crafted website may leak sensitive
data
Description: A logic issue was addressed with improved state
management.
CVE-2022-42817: Mir Masood Ali, PhD student, University of Illinois
at Chicago; Binoy Chitale, MS student, Stony Brook University;
Mohammad Ghasemisharif, PhD Candidate, University of Illinois at
Chicago; Chris Kanich, Associate Professor, University of Illinois at
Chicago
Entry added October 27, 2022

Sandbox
Available for: Apple Watch Series 4 and later
Impact: An app may be able to access user-sensitive data
Description: An access issue was addressed with additional sandbox
restrictions.
CVE-2022-42811: Justin Bui (@slyd0g) of Snowflake

WebKit
Available for: Apple Watch Series 4 and later
Impact: Visiting a malicious website may lead to user interface
spoofing
Description: The issue was addressed with improved UI handling.
WebKit Bugzilla: 243693
CVE-2022-42799: Jihwan Kim (@gPayl0ad), Dohyun Lee (@l33d0hyun)

WebKit
Available for: Apple Watch Series 4 and later
Impact: Processing maliciously crafted web content may lead to
arbitrary code execution
Description: A type confusion issue was addressed with improved
memory handling.
WebKit Bugzilla: 244622
CVE-2022-42823: Dohyun Lee (@l33d0hyun) of SSD Labs

WebKit
Available for: Apple Watch Series 4 and later
Impact: Processing maliciously crafted web content may disclose
sensitive user information
Description: A logic issue was addressed with improved state
management.
WebKit Bugzilla: 245058
CVE-2022-42824: Abdulrahman Alqabandi of Microsoft Browser
Vulnerability Research, Ryan Shin of IAAI SecLab at Korea University,
Dohyun Lee (@l33d0hyun) of DNSLab at Korea University

WebKit
Available for: Apple Watch Series 4 and later
Impact: Processing maliciously crafted web content may disclose
internal states of the app
Description: A correctness issue in the JIT was addressed with
improved checks.
WebKit Bugzilla: 242964
CVE-2022-32923: Wonyoung Jung (@nonetype_pwn) of KAIST Hacking Lab
Entry added October 27, 2022

zlib
Available for: Apple Watch Series 4 and later
Impact: A user may be able to cause unexpected app termination or
arbitrary code execution
Description: This issue was addressed with improved checks.
CVE-2022-37434: Evgeny Legerov
CVE-2022-42800: Evgeny Legerov
Entry added October 27, 2022

Additional recognition

iCloud
We would like to acknowledge Tim Michaud (@TimGMichaud) of
Moveworks.ai for their assistance.

Kernel
We would like to acknowledge Peter Nguyen of STAR Labs, Tim Michaud
(@TimGMichaud) of Moveworks.ai, Tommy Muir (@Muirey03) for their
assistance.

WebKit
We would like to acknowledge Maddie Stone of Google Project Zero,
Narendra Bhati (@imnarendrabhati) of Suma Soft Pvt. Ltd., an
anonymous researcher for their assistance.

Instructions on how to update your Apple Watch software are available
at https://support.apple.com/kb/HT204641  To check the version on
your Apple Watch, open the Apple Watch app on your iPhone and select
"My Watch > General > About".  Alternatively, on your watch, select
"My Watch > General > About".
All information is also posted on the Apple Security Updates
web site: https://support.apple.com/en-us/HT201222.

This message is signed with Apple's Product Security PGP key,
and details are available at:
https://www.apple.com/sup...