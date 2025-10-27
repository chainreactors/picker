---
title: APPLE-SA-09-15-2025-10 visionOS 26
url: https://seclists.org/fulldisclosure/2025/Sep/58
source: Full Disclosure
date: 2025-09-17
fetch_date: 2025-10-02T20:16:43.179034
---

# APPLE-SA-09-15-2025-10 visionOS 26

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

[![Previous](/images/left-icon-16x16.png)](57)
[By Date](date.html#58)
[![Next](/images/right-icon-16x16.png)](59)

[![Previous](/images/left-icon-16x16.png)](57)
[By Thread](index.html#58)
[![Next](/images/right-icon-16x16.png)](59)

![](/shared/images/nst-icons.svg#search)

# APPLE-SA-09-15-2025-10 visionOS 26

---

*From*: Apple Product Security via Fulldisclosure <fulldisclosure () seclists org>
*Date*: Mon, 15 Sep 2025 16:37:23 -0700

---

```
-----BEGIN PGP SIGNED MESSAGE-----
Hash: SHA256

APPLE-SA-09-15-2025-10 visionOS 26

visionOS 26 addresses the following issues.
Information about the security content is also available at
https://support.apple.com/125115.

Apple maintains a Security Releases page at
https://support.apple.com/100100 which lists recent
software updates with security advisories.

AppleMobileFileIntegrity
Available for: Apple Vision Pro
Impact: An app may be able to access sensitive user data
Description: A permissions issue was addressed with additional
restrictions.
CVE-2025-43317: Mickey Jin (@patch1t)

Apple Neural Engine
Available for: Apple Vision Pro
Impact: An app may be able to cause unexpected system termination
Description: An out-of-bounds access issue was addressed with improved
bounds checking.
CVE-2025-43344: an anonymous researcher

Audio
Available for: Apple Vision Pro
Impact: Processing a maliciously crafted media file may lead to
unexpected app termination or corrupt process memory
Description: An out-of-bounds access issue was addressed with improved
bounds checking.
CVE-2025-43346: Hossein Lotfi (@hosselot) of Trend Micro Zero Day
Initiative

Bluetooth
Available for: Apple Vision Pro
Impact: An app may be able to access sensitive user data
Description: A logging issue was addressed with improved data redaction.
CVE-2025-43354: Csaba Fitzl (@theevilbit) of Kandji
CVE-2025-43303: Csaba Fitzl (@theevilbit) of Kandji

CoreAudio
Available for: Apple Vision Pro
Impact: Processing a maliciously crafted video file may lead to
unexpected app termination
Description: An out-of-bounds write issue was addressed with improved
input validation.
CVE-2025-43349: @zlluny working with Trend Micro Zero Day Initiative

CoreMedia
Available for: Apple Vision Pro
Impact: Processing a maliciously crafted media file may lead to
unexpected app termination or corrupt process memory
Description: The issue was addressed with improved input validation.
CVE-2025-43372: 이동하 (Lee Dong Ha) of SSA Lab

DiskArbitration
Available for: Apple Vision Pro
Impact: A malicious app may be able to gain root privileges
Description: A permissions issue was addressed with additional
restrictions.
CVE-2025-43316: Csaba Fitzl (@theevilbit) of Kandji, an anonymous
researcher

IOHIDFamily
Available for: Apple Vision Pro
Impact: An app may be able to cause unexpected system termination
Description: An out-of-bounds write issue was addressed with improved
bounds checking.
CVE-2025-43302: Keisuke Hosoda

Kernel
Available for: Apple Vision Pro
Impact: A UDP server socket bound to a local interface may become bound
to all interfaces
Description: A logic issue was addressed with improved state management.
CVE-2025-43359: Viktor Oreshkin

MobileStorageMounter
Available for: Apple Vision Pro
Impact: An app may be able to cause a denial-of-service
Description: A type confusion issue was addressed with improved memory
handling.
CVE-2025-43355: Dawuge of Shuffle Team

Spell Check
Available for: Apple Vision Pro
Impact: An app may be able to access sensitive user data
Description: A parsing issue in the handling of directory paths was
addressed with improved path validation.
CVE-2025-43190: Noah Gregory (wts.dev)

SQLite
Available for: Apple Vision Pro
Impact: Processing a file may lead to memory corruption
Description: This is a vulnerability in open source code and Apple
Software is among the affected projects. The CVE-ID was assigned by a
third party. Learn more about the issue and CVE-ID at cve.org.
CVE-2025-6965

System
Available for: Apple Vision Pro
Impact: An input validation issue was addressed
Description: This issue was addressed by removing the vulnerable code.
CVE-2025-43347: JZ, Seo Hyun-gyu (@wh1te4ever), Luke Roberts (@rookuu)

WebKit
Available for: Apple Vision Pro
Impact: A website may be able to access sensor information without user
consent
Description: The issue was addressed with improved handling of caches.
WebKit Bugzilla: 296153
CVE-2025-43356: Jaydev Ahire

WebKit
Available for: Apple Vision Pro
Impact: Processing maliciously crafted web content may lead to an
unexpected Safari crash
Description: The issue was addressed with improved memory handling.
WebKit Bugzilla: 294550
CVE-2025-43272: Big Bear

WebKit
Available for: Apple Vision Pro
Impact: Processing maliciously crafted web content may lead to an
unexpected process crash
Description: The issue was addressed with improved memory handling.
WebKit Bugzilla: 296490
CVE-2025-43343: an anonymous researcher

WebKit
Available for: Apple Vision Pro
Impact: Processing maliciously crafted web content may lead to an
unexpected process crash
Description: A correctness issue was addressed with improved checks.
WebKit Bugzilla: 296042
CVE-2025-43342: an anonymous researcher

Additional recognition

AuthKit
We would like to acknowledge Rosyna Keller of Totally Not Malicious
Software for their assistance.

Calendar
We would like to acknowledge Keisuke Chinone (Iroiro) for their
assistance.

CFNetwork
We would like to acknowledge Christian Kohlschütter for their
assistance.

CloudKit
We would like to acknowledge Yinyi Wu (@_3ndy1) from Dawn Security Lab
of JD.com, Inc for their assistance.

Control Center
We would like to acknowledge Damitha Gunawardena for their assistance.

CoreMedia
We would like to acknowledge Noah Gregory (wts.dev) for their
assistance.

darwinOS
We would like to acknowledge Nathaniel Oh (@calysteon) for their
assistance.

Files
We would like to acknowledge Tyler Montgomery for their assistance.

Foundation
We would like to acknowledge Csaba Fitzl (@theevilbit) of Kandji for
their assistance.

ImageIO
We would like to acknowledge DongJun Kim (@smlijun) and JongSeong Kim
(@nevul37) in Enki WhiteHat for their assistance.

IOGPUFamily
We would like to acknowledge Wang Yu of Cyberserval for their
assistance.

Kernel
We would like to acknowledge Yepeng Pan, Prof. Dr. Christian Rossow for
their assistance.

libc
We would like to acknowledge Nathaniel Oh (@calysteon) for their
assistance.

libpthread
We would like to acknowledge Nathaniel Oh (@calysteon) for their
assistance.

libxml2
We would like to acknowledge Nathaniel Oh (@calysteon) for their
assistance.

mDNSResponder
We would like to acknowledge Barrett Lyon for their assistance.

Networking
We would like to acknowledge Csaba Fitzl (@theevilbit) of Kandji for
their assistance.

Notes
We would like to acknowledge Atul R V for their assistance.

Passwords
We would like to acknowledge Christian Kohlschütter for their
assistance.

Safari
We would like to acknowledge Ameen Basha M K for their assistance.

Sandbox Profiles
We would like to acknowledge Rosyna Keller of Totally Not Malicious
Software for their assistance.

Spotlight
We would like to acknowledge Christian Scalese for their assistance.

Transparency
We would like to acknowledge Wojciech Regula of SecuRing
(wojciechregula.blog), 要乐奈 for their assistance.

WebKit
We would like to acknowledge Bob Lord, Matthew Liang, Mike Cardwell of
grepular.com for their assistance.

Wi-Fi
We would like to ac...