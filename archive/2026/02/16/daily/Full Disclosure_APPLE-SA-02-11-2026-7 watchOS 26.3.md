---
title: APPLE-SA-02-11-2026-7 watchOS 26.3
url: https://seclists.org/fulldisclosure/2026/Feb/27
source: Full Disclosure
date: 2026-02-16
fetch_date: 2026-02-17T04:21:55.698561
---

# APPLE-SA-02-11-2026-7 watchOS 26.3

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

[![Previous](/images/left-icon-16x16.png)](26)
[By Date](date.html#27)
[![Next](/images/right-icon-16x16.png)](28)

[![Previous](/images/left-icon-16x16.png)](26)
[By Thread](index.html#27)
[![Next](/images/right-icon-16x16.png)](28)

![](/shared/images/nst-icons.svg#search)

# APPLE-SA-02-11-2026-7 watchOS 26.3

---

*From*: Apple Product Security via Fulldisclosure <fulldisclosure () seclists org>
*Date*: Wed, 11 Feb 2026 16:05:58 -0800

---

```
-----BEGIN PGP SIGNED MESSAGE-----
Hash: SHA256

APPLE-SA-02-11-2026-7 watchOS 26.3

watchOS 26.3 addresses the following issues.
Information about the security content is also available at
https://support.apple.com/126352.

Apple maintains a Security Releases page at
https://support.apple.com/100100 which lists recent
software updates with security advisories.

Bluetooth
Available for: Apple Watch Series 6 and later
Impact: An attacker in a privileged network position may be able to
perform denial-of-service attack using crafted Bluetooth packets
Description: A denial-of-service issue was addressed with improved
validation.
CVE-2026-20650: jioundai

CoreAudio
Available for: Apple Watch Series 6 and later
Impact: Processing a maliciously crafted media file may lead to
unexpected app termination or corrupt process memory
Description: An out-of-bounds access issue was addressed with improved
bounds checking.
CVE-2026-20611: Anonymous working with Trend Micro Zero Day Initiative

CoreMedia
Available for: Apple Watch Series 6 and later
Impact: Processing a maliciously crafted file may lead to a denial-of-
service or potentially disclose memory contents
Description: The issue was addressed with improved memory handling.
CVE-2026-20609: Yiğit Can YILMAZ (@yilmazcanyigit)

CoreServices
Available for: Apple Watch Series 6 and later
Impact: An app may be able to gain root privileges
Description: A race condition was addressed with improved state
handling.
CVE-2026-20617: Gergely Kalman (@gergely_kalman), Csaba Fitzl
(@theevilbit) of Iru

CoreServices
Available for: Apple Watch Series 6 and later
Impact: An app may be able to access sensitive user data
Description: An issue existed in the handling of environment variables.
This issue was addressed with improved validation.
CVE-2026-20627: an anonymous researcher

dyld
Available for: Apple Watch Series 6 and later
Impact: An attacker with memory write capability may be able to execute
arbitrary code. Apple is aware of a report that this issue may have been
exploited in an extremely sophisticated attack against specific targeted
individuals on versions of iOS before iOS 26. CVE-2025-14174 and
CVE-2025-43529 were also issued in response to this report.
Description: A memory corruption issue was addressed with improved state
management.
CVE-2026-20700: Google Threat Analysis Group

Game Center
Available for: Apple Watch Series 6 and later
Impact: A user may be able to view sensitive user information
Description: A logging issue was addressed with improved data redaction.
CVE-2026-20649: Asaf Cohen

ImageIO
Available for: Apple Watch Series 6 and later
Impact: Processing a maliciously crafted image may lead to disclosure of
user information
Description: The issue was addressed with improved bounds checks.
CVE-2026-20675: George Karchemsky (@gkarchemsky) working with Trend
Micro Zero Day Initiative

ImageIO
Available for: Apple Watch Series 6 and later
Impact: Processing a maliciously crafted image may result in disclosure
of process memory
Description: The issue was addressed with improved memory handling.
CVE-2026-20634: George Karchemsky (@gkarchemsky) working with Trend
Micro Zero Day Initiative

Kernel
Available for: Apple Watch Series 6 and later
Impact: An app may be able to cause unexpected system termination
Description: The issue was addressed with improved memory handling.
CVE-2026-20654: Jian Lee (@speedyfriend433)

Kernel
Available for: Apple Watch Series 6 and later
Impact: An attacker in a privileged network position may be able to
intercept network traffic
Description: A logic issue was addressed with improved checks.
CVE-2026-20671: Xin'an Zhou, Juefei Pu, Zhutian Liu, Zhiyun Qian,
Zhaowei Tan, Srikanth V. Krishnamurthy, Mathy Vanhoef

libexpat
Available for: Apple Watch Series 6 and later
Impact: Processing a maliciously crafted file may lead to a denial-of-
service
Description: This is a vulnerability in open source code and Apple
Software is among the affected projects. The CVE-ID was assigned by a
third party. Learn more about the issue and CVE-ID at cve.org.
CVE-2025-59375

libxpc
Available for: Apple Watch Series 6 and later
Impact: An app may be able to break out of its sandbox
Description: A logic issue was addressed with improved checks.
CVE-2026-20667: an anonymous researcher

Sandbox
Available for: Apple Watch Series 6 and later
Impact: An app may be able to break out of its sandbox
Description: A permissions issue was addressed with additional
restrictions.
CVE-2026-20628: Noah Gregory (wts.dev)

StoreKit
Available for: Apple Watch Series 6 and later
Impact: An app may be able to identify what other apps a user has
installed
Description: A privacy issue was addressed with improved checks.
CVE-2026-20641: Gongyu Ma (@Mezone0)

WebKit
Available for: Apple Watch Series 6 and later
Impact: Processing maliciously crafted web content may lead to an
unexpected process crash
Description: The issue was addressed with improved memory handling.
WebKit Bugzilla: 304661
CVE-2026-20635: EntryHi

Additional recognition

Bluetooth
We would like to acknowledge Tommaso Sacchetti for their assistance.

Kernel
We would like to acknowledge Joseph Ravichandran (@0xjprx) of MIT CSAIL,
Xinru Chi of Pangu Lab for their assistance.

libpthread
We would like to acknowledge Fabiano Anemone for their assistance.

NetworkExtension
We would like to acknowledge Gongyu Ma (@Mezone0) for their assistance.

Transparency
We would like to acknowledge Wojciech Regula of SecuRing
(wojciechregula.blog) for their assistance.

Wallet
We would like to acknowledge Lorenzo Santina (@BigNerd95) and Marco
Bartoli (@wsxarcher) for their assistance.

WebKit
We would like to acknowledge EntryHi, Luigino Camastra of Aisle
Research, Stanislav Fort of Aisle Research, Vsevolod Kokorin (Slonser)
of Solidlab and Jorian Woltjer for their assistance.

Instructions on how to update your Apple Watch software are
available at https://support.apple.com/kb/HT204641

To check the version on your Apple Watch, open the Apple Watch app
on your iPhone and select "My Watch > General > About".

Alternatively, on your watch, select "My Watch > General > About".

All information is also posted on the Apple Security Releases
web site: https://support.apple.com/100100.

This message is signed with Apple's Product Security PGP key,
and details are available at:
https://www.apple.com/support/security/pgp/

-----BEGIN PGP SIGNATURE-----

iQIzBAEBCAAdFiEEhjkl+zMLNwFiCT1o4Ifiq8DH7PUFAmmND5UACgkQ4Ifiq8DH
7PXrTA//V0gBF+jsdvuwEBOSi+t1slOUCpE0Q9m75aW2n5eoxxyR6JWAZrMbjmqY
U28crzng8tvqWukyKgenhqt9pqgoieGLSmIdk+jd9hTI3NeM0LYTuqEQ8vwFIzaz
urPLMWEy5c2YdMHzvJvlaAWyTTVAUU5A4BCKUPeMKQu+o0MIaqesXCu43RTG5Z3M
pe8uChvt29jMqXQDZN7HY5LJWz11jyzilV3on5ErU5xeKCb3BFhjnXbn0OHLWpsM
f7nZ7o9t7XBQkwgp3TB7/FkXuJT+gqp6XUdHB2NTmTEa1pDKu/Oy8+0YCPYmZWTZ
mVk/wsWwCPYEKBh9GpnFHbnuAs44qo2MvyYutEEbsm4PUqvYHGvy4Hi9l/pBVpB5
gveXlBa0WA/XD3UTZ64SPIOGrOE+o2Ik+EEQPDVgLNJpRfXmvojkxo/NfE3+LO7Q
h8NxBHCnFeVx1qz6NdN4ofC3Kj9QrEfyj2wv6swGKp7v2ZMlxhNmm+3TzJThuOx7
RjKG4SS0vja/7OMOBJdUginw...