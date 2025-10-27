---
title: APPLE-SA-09-15-2025-8 tvOS 26
url: https://seclists.org/fulldisclosure/2025/Sep/56
source: Full Disclosure
date: 2025-09-17
fetch_date: 2025-10-02T20:16:45.975774
---

# APPLE-SA-09-15-2025-8 tvOS 26

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

[![Previous](/images/left-icon-16x16.png)](55)
[By Date](date.html#56)
[![Next](/images/right-icon-16x16.png)](57)

[![Previous](/images/left-icon-16x16.png)](55)
[By Thread](index.html#56)
[![Next](/images/right-icon-16x16.png)](57)

![](/shared/images/nst-icons.svg#search)

# APPLE-SA-09-15-2025-8 tvOS 26

---

*From*: Apple Product Security via Fulldisclosure <fulldisclosure () seclists org>
*Date*: Mon, 15 Sep 2025 16:36:37 -0700

---

```
-----BEGIN PGP SIGNED MESSAGE-----
Hash: SHA256

APPLE-SA-09-15-2025-8 tvOS 26

tvOS 26 addresses the following issues.
Information about the security content is also available at
https://support.apple.com/125114.

Apple maintains a Security Releases page at
https://support.apple.com/100100 which lists recent
software updates with security advisories.

Apple Neural Engine
Available for: Apple TV 4K (2nd generation and later)
Impact: An app may be able to cause unexpected system termination
Description: An out-of-bounds access issue was addressed with improved
bounds checking.
CVE-2025-43344: an anonymous researcher

AppleMobileFileIntegrity
Available for: Apple TV HD and Apple TV 4K (all models)
Impact: An app may be able to access sensitive user data
Description: A permissions issue was addressed with additional
restrictions.
CVE-2025-43317: Mickey Jin (@patch1t)

Audio
Available for: Apple TV HD and Apple TV 4K (all models)
Impact: Processing a maliciously crafted media file may lead to
unexpected app termination or corrupt process memory
Description: An out-of-bounds access issue was addressed with improved
bounds checking.
CVE-2025-43346: Hossein Lotfi (@hosselot) of Trend Micro Zero Day
Initiative

Bluetooth
Available for: Apple TV HD and Apple TV 4K (all models)
Impact: An app may be able to access sensitive user data
Description: A logging issue was addressed with improved data redaction.
CVE-2025-43354: Csaba Fitzl (@theevilbit) of Kandji
CVE-2025-43303: Csaba Fitzl (@theevilbit) of Kandji

CoreAudio
Available for: Apple TV HD and Apple TV 4K (all models)
Impact: Processing a maliciously crafted video file may lead to
unexpected app termination
Description: An out-of-bounds write issue was addressed with improved
input validation.
CVE-2025-43349: @zlluny working with Trend Micro Zero Day Initiative

CoreMedia
Available for: Apple TV HD and Apple TV 4K (all models)
Impact: Processing a maliciously crafted media file may lead to
unexpected app termination or corrupt process memory
Description: The issue was addressed with improved input validation.
CVE-2025-43372: 이동하 (Lee Dong Ha) of SSA Lab

IOHIDFamily
Available for: Apple TV HD and Apple TV 4K (all models)
Impact: An app may be able to cause unexpected system termination
Description: An out-of-bounds write issue was addressed with improved
bounds checking.
CVE-2025-43302: Keisuke Hosoda

IOKit
Available for: Apple TV HD and Apple TV 4K (all models)
Impact: An app may be able to access sensitive user data
Description: An authorization issue was addressed with improved state
management.
CVE-2025-31255: Csaba Fitzl (@theevilbit) of Kandji

Kernel
Available for: Apple TV HD and Apple TV 4K (all models)
Impact: A UDP server socket bound to a local interface may become bound
to all interfaces
Description: A logic issue was addressed with improved state management.
CVE-2025-43359: Viktor Oreshkin

MobileStorageMounter
Available for: Apple TV HD and Apple TV 4K (all models)
Impact: An app may be able to cause a denial-of-service
Description: A type confusion issue was addressed with improved memory
handling.
CVE-2025-43355: Dawuge of Shuffle Team

Sandbox
Available for: Apple TV HD and Apple TV 4K (all models)
Impact: An app may be able to break out of its sandbox
Description: A permissions issue was addressed with additional
restrictions.
CVE-2025-43329: an anonymous researcher

SQLite
Available for: Apple TV HD and Apple TV 4K (all models)
Impact: Processing a file may lead to memory corruption
Description: This is a vulnerability in open source code and Apple
Software is among the affected projects. The CVE-ID was assigned by a
third party. Learn more about the issue and CVE-ID at cve.org.
CVE-2025-6965

System
Available for: Apple TV HD and Apple TV 4K (all models)
Impact: An input validation issue was addressed
Description: This issue was addressed by removing the vulnerable code.
CVE-2025-43347: JZ, Seo Hyun-gyu (@wh1te4ever), Luke Roberts (@rookuu)

WebKit
Available for: Apple TV HD and Apple TV 4K (all models)
Impact: A website may be able to access sensor information without user
consent
Description: The issue was addressed with improved handling of caches.
WebKit Bugzilla: 296153
CVE-2025-43356: Jaydev Ahire

WebKit
Available for: Apple TV HD and Apple TV 4K (all models)
Impact: Processing maliciously crafted web content may lead to an
unexpected process crash
Description: The issue was addressed with improved memory handling.
WebKit Bugzilla: 296490
CVE-2025-43343: an anonymous researcher

WebKit
Available for: Apple TV HD and Apple TV 4K (all models)
Impact: Processing maliciously crafted web content may lead to an
unexpected process crash
Description: A correctness issue was addressed with improved checks.
WebKit Bugzilla: 296042
CVE-2025-43342: an anonymous researcher

Additional recognition

Accounts
We would like to acknowledge 要乐奈 for their assistance.

AuthKit
We would like to acknowledge Rosyna Keller of Totally Not Malicious
Software for their assistance.

CFNetwork
We would like to acknowledge Christian Kohlschütter for their
assistance.

CloudKit
We would like to acknowledge Yinyi Wu (@_3ndy1) from Dawn Security Lab
of JD.com, Inc for their assistance.

CoreMedia
We would like to acknowledge Noah Gregory (wts.dev) for their
assistance.

darwinOS
We would like to acknowledge Nathaniel Oh (@calysteon) for their
assistance.

Foundation
We would like to acknowledge Csaba Fitzl (@theevilbit) of Kandji for
their assistance.

ImageIO
We would like to acknowledge DongJun Kim (@smlijun) and JongSeong Kim
(@nevul37) in Enki WhiteHat for their assistance.

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

MediaRemote
We would like to acknowledge Dora Orak for their assistance.

Sandbox Profiles
We would like to acknowledge Rosyna Keller of Totally Not Malicious
Software for their assistance.

Transparency
We would like to acknowledge Wojciech Regula of SecuRing
(wojciechregula.blog), 要乐奈 for their assistance.

WebKit
We would like to acknowledge Bob Lord, Matthew Liang, Mike Cardwell of
grepular.com for their assistance.

Wi-Fi
We would like to acknowledge Aobo Wang (@M4x_1997), Csaba Fitzl
(@theevilbit) of Kandji, Noah Gregory (wts.dev), Wojciech Regula of
SecuRing (wojciechregula.blog), an anonymous researcher for their
assistance.

Apple TV will periodically check for software updates. Alternatively,
you may manually check for software updates by selecting
"Settings -> System -> Software Update -> Update Software."

To check the current version of software, select
"Settings -> General -> About."

All information is also posted on the Apple Security Releases
web site: https://support.a...