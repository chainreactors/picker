---
title: APPLE-SA-03-24-2026-6 tvOS 26.4
url: https://seclists.org/fulldisclosure/2026/Mar/21
source: Full Disclosure
date: 2026-03-29
fetch_date: 2026-03-30T04:46:57.843938
---

# APPLE-SA-03-24-2026-6 tvOS 26.4

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

# APPLE-SA-03-24-2026-6 tvOS 26.4

---

*From*: Apple Product Security via Fulldisclosure <fulldisclosure () seclists org>
*Date*: Tue, 24 Mar 2026 17:03:21 -0700

---

```
-----BEGIN PGP SIGNED MESSAGE-----
Hash: SHA256

APPLE-SA-03-24-2026-6 tvOS 26.4

tvOS 26.4 addresses the following issues.
Information about the security content is also available at
https://support.apple.com/126797.

Apple maintains a Security Releases page at
https://support.apple.com/100100 which lists recent
software updates with security advisories.

802.1X
Available for: Apple TV HD and Apple TV 4K (all models)
Impact: An attacker in a privileged network position may be able to
intercept network traffic
Description: An authentication issue was addressed with improved state
management.
CVE-2026-28865: Héloïse Gollier and Mathy Vanhoef (KU Leuven)

Audio
Available for: Apple TV HD and Apple TV 4K (all models)
Impact: Processing maliciously crafted web content may lead to an
unexpected process crash
Description: A use-after-free issue was addressed with improved memory
management.
CVE-2026-28879: Justin Cohen of Google

Audio
Available for: Apple TV HD and Apple TV 4K (all models)
Impact: An attacker may be able to cause unexpected app termination
Description: A type confusion issue was addressed with improved memory
handling.
CVE-2026-28822: Jex Amro

CoreMedia
Available for: Apple TV HD and Apple TV 4K (all models)
Impact: Processing an audio stream in a maliciously crafted media file
may terminate the process
Description: An out-of-bounds access issue was addressed with improved
bounds checking.
CVE-2026-20690: Hossein Lotfi (@hosselot) of Trend Micro Zero Day
Initiative

CoreUtils
Available for: Apple TV HD and Apple TV 4K (all models)
Impact: A user in a privileged network position may be able to cause a
denial-of-service
Description: A null pointer dereference was addressed with improved
input validation.
CVE-2026-28886: Etienne Charron (Renault) and Victoria Martini (Renault)

Crash Reporter
Available for: Apple TV HD and Apple TV 4K (all models)
Impact: An app may be able to enumerate a user's installed apps
Description: A privacy issue was addressed by removing sensitive data.
CVE-2026-28878: Zhongcheng Li from IES Red Team

curl
Available for: Apple TV HD and Apple TV 4K (all models)
Impact: An issue existed in curl which may result in unintentionally
sending sensitive information via an incorrect connection
Description: This is a vulnerability in open source code and Apple
Software is among the affected projects. The CVE-ID was assigned by a
third party. Learn more about the issue and CVE-ID at cve.org.
CVE-2025-14524

GeoServices
Available for: Apple TV HD and Apple TV 4K (all models)
Impact: An app may be able to access sensitive user data
Description: An information leakage was addressed with additional
validation.
CVE-2026-28870: XiguaSec

ImageIO
Available for: Apple TV HD and Apple TV 4K (all models)
Impact: Processing a maliciously crafted file may lead to unexpected app
termination
Description: This is a vulnerability in open source code and Apple
Software is among the affected projects. The CVE-ID was assigned by a
third party. Learn more about the issue and CVE-ID at cve.org.
CVE-2025-64505

Kernel
Available for: Apple TV HD and Apple TV 4K (all models)
Impact: An app may be able to leak sensitive kernel state
Description: This issue was addressed with improved authentication.
CVE-2026-28867: Jian Lee (@speedyfriend433)

Kernel
Available for: Apple TV HD and Apple TV 4K (all models)
Impact: An app may be able to cause unexpected system termination or
corrupt kernel memory
Description: The issue was addressed with improved memory handling.
CVE-2026-20698: DARKNAVY (@DarkNavyOrg)

Kernel
Available for: Apple TV HD and Apple TV 4K (all models)
Impact: An app may be able to cause unexpected system termination or
write kernel memory
Description: A use after free issue was addressed with improved memory
management.
CVE-2026-20687: Johnny Franks (@zeroxjf)

libxpc
Available for: Apple TV HD and Apple TV 4K (all models)
Impact: An app may be able to enumerate a user's installed apps
Description: This issue was addressed with improved checks.
CVE-2026-28882: Ilias Morad (A2nkF) of Voynich Group, Duy Trần
(@khanhduytran0), @hugeBlack

Sandbox Profiles
Available for: Apple TV HD and Apple TV 4K (all models)
Impact: An app may be able to fingerprint the user
Description: A permissions issue was addressed with additional
restrictions.
CVE-2026-28863: Gongyu Ma (@Mezone0)

UIFoundation
Available for: Apple TV HD and Apple TV 4K (all models)
Impact: An app may be able to cause a denial-of-service
Description: A stack overflow was addressed with improved input
validation.
CVE-2026-28852: Caspian Tarafdar

WebKit
Available for: Apple TV HD and Apple TV 4K (all models)
Impact: Processing maliciously crafted web content may prevent Content
Security Policy from being enforced
Description: This issue was addressed through improved state management.
WebKit Bugzilla: 304951
CVE-2026-20665: webb

WebKit
Available for: Apple TV HD and Apple TV 4K (all models)
Impact: A malicious website may be able to process restricted web
content outside the sandbox
Description: The issue was addressed with improved memory handling.
WebKit Bugzilla: 308248
CVE-2026-28859: greenbynox, Arni Hardarson

Additional recognition

AirPort
We would like to acknowledge Yashar Shahinzadeh, Saman Ebrahimnezhad,
Amir Safari, Omid Rezaii for their assistance.

Bluetooth
We would like to acknowledge Hamid Mahmoud for their assistance.

Captive Network
We would like to acknowledge Kun Peeks (@SwayZGl1tZyyy) for their
assistance.

CoreUI
We would like to acknowledge Peter Malone for their assistance.

Find My
We would like to acknowledge Salemdomain for their assistance.

GPU Drivers
We would like to acknowledge Jian Lee (@speedyfriend433) for their
assistance.

ICU
We would like to acknowledge Jian Lee (@speedyfriend433) for their
assistance.

Kernel
We would like to acknowledge DARKNAVY (@DarkNavyOrg), Kylian Boulard De
Pouqueville From Fuzzinglabs, Patrick Ventuzelo From Fuzzinglabs, Robert
Tran, Suresh Sundaram for their assistance.

libarchive
We would like to acknowledge Andreas Jaegersberger & Ro Achterberg of
Nosebeard Labs, Arni Hardarson for their assistance.

libc
We would like to acknowledge Vitaly Simonovich for their assistance.

Libnotify
We would like to acknowledge Ilias Morad (@A2nkF_) for their assistance.

LLVM
We would like to acknowledge Nathaniel Oh (@calysteon) for their
assistance.

Messages
We would like to acknowledge JZ for their assistance.

MobileInstallation
We would like to acknowledge Gongyu Ma (@Mezone0) for their assistance.

ppp
We would like to acknowledge Dave G. for their assistance.

Quick Look
We would like to acknowledge Wojciech Regula of SecuRing
(wojciechregula.blog), an anonymous researcher for their assistance.

Safari
We would like to acknowledge @RenwaX23, Farras Givari, Syarif Muhammad
Sajjad, Yair for their assistance.

Shortcuts
We would like to acknowledge Waleed Barakat (@WilDN00B) and Paul
Montgomery (@nullevent) for their assistance.

Siri
We would like to acknowledge Anand Mallaya, Tech consultant, An...