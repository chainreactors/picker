---
title: APPLE-SA-05-12-2025-6 watchOS 11.5
url: https://seclists.org/fulldisclosure/2025/May/10
source: Full Disclosure
date: 2025-05-18
fetch_date: 2025-10-06T22:27:51.609523
---

# APPLE-SA-05-12-2025-6 watchOS 11.5

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

[![Previous](/images/left-icon-16x16.png)](9)
[By Date](date.html#10)
[![Next](/images/right-icon-16x16.png)](11)

[![Previous](/images/left-icon-16x16.png)](9)
[By Thread](index.html#10)
[![Next](/images/right-icon-16x16.png)](11)

![](/shared/images/nst-icons.svg#search)

# APPLE-SA-05-12-2025-6 watchOS 11.5

---

*From*: Apple Product Security via Fulldisclosure <fulldisclosure () seclists org>
*Date*: Mon, 12 May 2025 15:44:27 -0700

---

```
-----BEGIN PGP SIGNED MESSAGE-----
Hash: SHA256

APPLE-SA-05-12-2025-6 watchOS 11.5

watchOS 11.5 addresses the following issues.
Information about the security content is also available at
https://support.apple.com/122722.

Apple maintains a Security Releases page at
https://support.apple.com/100100 which lists recent
software updates with security advisories.

AppleJPEG
Available for: Apple Watch Series 6 and later
Impact: Processing a maliciously crafted media file may lead to
unexpected app termination or corrupt process memory
Description: The issue was addressed with improved input sanitization.
CVE-2025-31251: Hossein Lotfi (@hosselot) of Trend Micro Zero Day
Initiative

Core Bluetooth
Available for: Apple Watch Series 6 and later
Impact: An app may be able to access sensitive user data
Description: This issue was addressed through improved state management.
CVE-2025-31212: Guilherme Rambo of Best Buddy Apps (rambo.codes)

CoreAudio
Available for: Apple Watch Series 6 and later
Impact: Processing an audio stream in a maliciously crafted media file
may result in code execution. Apple is aware of a report that this issue
may have been exploited in an extremely sophisticated attack against
specific targeted individuals on versions of iOS released before iOS
18.4.1.
Description: A memory corruption issue was addressed with improved
bounds checking.
CVE-2025-31200: Apple and Google Threat Analysis Group

CoreAudio
Available for: Apple Watch Series 6 and later
Impact: Parsing a file may lead to an unexpected app termination
Description: The issue was addressed with improved checks.
CVE-2025-31208: Hossein Lotfi (@hosselot) of Trend Micro Zero Day
Initiative

CoreGraphics
Available for: Apple Watch Series 6 and later
Impact: Parsing a file may lead to disclosure of user information
Description: An out-of-bounds read was addressed with improved bounds
checking.
CVE-2025-31209: Hossein Lotfi (@hosselot) of Trend Micro Zero Day
Initiative

CoreMedia
Available for: Apple Watch Series 6 and later
Impact: Parsing a file may lead to an unexpected app termination
Description: A use-after-free issue was addressed with improved memory
management.
CVE-2025-31239: Hossein Lotfi (@hosselot) of Trend Micro Zero Day
Initiative

CoreMedia
Available for: Apple Watch Series 6 and later
Impact: Processing a maliciously crafted video file may lead to
unexpected app termination or corrupt process memory
Description: The issue was addressed with improved input sanitization.
CVE-2025-31233: Hossein Lotfi (@hosselot) of Trend Micro Zero Day
Initiative

ImageIO
Available for: Apple Watch Series 6 and later
Impact: Processing a maliciously crafted image may lead to a denial-of-
service
Description: A logic issue was addressed with improved checks.
CVE-2025-31226: Saagar Jha

Kernel
Available for: Apple Watch Series 6 and later
Impact: An attacker may be able to cause unexpected system termination
or corrupt kernel memory
Description: The issue was addressed with improved memory handling.
CVE-2025-31219: Michael DePlante (@izobashi) and Lucas Leong
(@_wmliang_) of Trend Micro Zero Day Initiative

Kernel
Available for: Apple Watch Series 6 and later
Impact: A remote attacker may cause an unexpected app termination
Description: A double free issue was addressed with improved memory
management.
CVE-2025-31241: Christian Kohlschütter

libexpat
Available for: Apple Watch Series 6 and later
Impact: Multiple issues in libexpat, including unexpected app
termination or arbitrary code execution
Description: This is a vulnerability in open source code and Apple
Software is among the affected projects. The CVE-ID was assigned by a
third party. Learn more about the issue and CVE-ID at cve.org.
CVE-2024-8176

mDNSResponder
Available for: Apple Watch Series 6 and later
Impact: A user may be able to elevate privileges
Description: A correctness issue was addressed with improved checks.
CVE-2025-31222: Paweł Płatek (Trail of Bits)

Security
Available for: Apple Watch Series 6 and later
Impact: A remote attacker may be able to leak memory
Description: An integer overflow was addressed with improved input
validation.
CVE-2025-31221: Dave G.

WebKit
Available for: Apple Watch Series 6 and later
Impact: A type confusion issue could lead to memory corruption
Description: This issue was addressed with improved handling of floats.
WebKit Bugzilla: 286694
CVE-2025-24213: Google V8 Security Team

WebKit
Available for: Apple Watch Series 6 and later
Impact: Processing maliciously crafted web content may lead to memory
corruption
Description: The issue was addressed with improved checks.
WebKit Bugzilla: 289387
CVE-2025-31223: Andreas Jaegersberger & Ro Achterberg of Nosebeard Labs
WebKit Bugzilla: 289653
CVE-2025-31238: wac working with Trend Micro Zero Day Initiative

WebKit
Available for: Apple Watch Series 6 and later
Impact: Processing maliciously crafted web content may lead to memory
corruption
Description: The issue was addressed with improved memory handling.
WebKit Bugzilla: 287577
CVE-2025-24223: rheza (@ginggilBesel) and an anonymous researcher
WebKit Bugzilla: 291506
CVE-2025-31204: Nan Wang(@eternalsakura13)

WebKit
Available for: Apple Watch Series 6 and later
Impact: Processing maliciously crafted web content may lead to an
unexpected Safari crash
Description: The issue was addressed with improved input validation.
WebKit Bugzilla: 289677
CVE-2025-31217: Ignacio Sanmillan (@ulexec)

WebKit
Available for: Apple Watch Series 6 and later
Impact: Processing maliciously crafted web content may lead to an
unexpected process crash
Description: The issue was addressed with improved checks.
WebKit Bugzilla: 288814
CVE-2025-31215: Jiming Wang and Jikai Ren

WebKit
Available for: Apple Watch Series 6 and later
Impact: Processing maliciously crafted web content may lead to an
unexpected Safari crash
Description: A type confusion issue was addressed with improved state
handling.
WebKit Bugzilla: 290834
CVE-2025-31206: an anonymous researcher

WebKit
Available for: Apple Watch Series 6 and later
Impact: A malicious website may exfiltrate data cross-origin
Description: The issue was addressed with improved checks.
WebKit Bugzilla: 290992
CVE-2025-31205: Ivan Fratric of Google Project Zero

WebKit
Available for: Apple Watch Series 6 and later
Impact: Processing maliciously crafted web content may lead to an
unexpected Safari crash
Description: This issue was addressed with improved memory handling.
WebKit Bugzilla: 290985
CVE-2025-31257: Juergen Schmied of Lynck GmbH

Additional recognition

AirDrop
We would like to acknowledge Dalibor Milanovic for their assistance.

Kernel
We would like to acknowledge an anonymous researcher for their
assistance.

MobileGestalt
We would like to acknowledge iisBuri for their assistance.

NetworkExtension
We would like to acknowledge Andrei-Alexandru Bleorțu for their
assistance.

Shortcuts
We would like to acknowledge Candace Jensen of Kandji, Chi Yuan Chang of
ZUSO ART and taikosoup, Egor Filatov (Positive Technologies) for their
assistance.

...