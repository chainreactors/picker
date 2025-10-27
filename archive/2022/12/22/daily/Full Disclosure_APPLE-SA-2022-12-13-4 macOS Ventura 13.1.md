---
title: APPLE-SA-2022-12-13-4 macOS Ventura 13.1
url: https://seclists.org/fulldisclosure/2022/Dec/23
source: Full Disclosure
date: 2022-12-22
fetch_date: 2025-10-04T02:15:07.804536
---

# APPLE-SA-2022-12-13-4 macOS Ventura 13.1

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

[![Previous](/images/left-icon-16x16.png)](22)
[By Date](date.html#23)
[![Next](/images/right-icon-16x16.png)](24)

[![Previous](/images/left-icon-16x16.png)](22)
[By Thread](index.html#23)
[![Next](/images/right-icon-16x16.png)](24)

![](/shared/images/nst-icons.svg#search)

# APPLE-SA-2022-12-13-4 macOS Ventura 13.1

---

*From*: Apple Product Security via Fulldisclosure <fulldisclosure () seclists org>
*Date*: Tue, 13 Dec 2022 16:34:44 -0800

---

```
-----BEGIN PGP SIGNED MESSAGE-----
Hash: SHA256

APPLE-SA-2022-12-13-4 macOS Ventura 13.1

macOS Ventura 13.1 addresses the following issues.
Information about the security content is also available at
https://support.apple.com/HT213532.

Accounts
Available for: macOS Ventura
Impact: A user may be able to view sensitive user information
Description: This issue was addressed with improved data protection.
CVE-2022-42843: Mickey Jin (@patch1t)

AMD
Available for: macOS Ventura
Impact: An app may be able to execute arbitrary code with kernel
privileges
Description: An out-of-bounds write issue was addressed with improved
input validation.
CVE-2022-42847: ABC Research s.r.o.

AppleMobileFileIntegrity
Available for: macOS Ventura
Impact: An app may be able to bypass Privacy preferences
Description: This issue was addressed by enabling hardened runtime.
CVE-2022-42865: Wojciech Reguła (@_r3ggi) of SecuRing

Bluetooth
Available for: macOS Ventura
Impact: An app may be able to disclose kernel memory
Description: The issue was addressed with improved memory handling.
CVE-2022-42854: Pan ZhenPeng (@Peterpan0927) of STAR Labs SG Pte.
Ltd. (@starlabs_sg)

Boot Camp
Available for: macOS Ventura
Impact: An app may be able to modify protected parts of the file
system
Description: An access issue was addressed with improved access
restrictions.
CVE-2022-42853: Mickey Jin (@patch1t) of Trend Micro

CoreServices
Available for: macOS Ventura
Impact: An app may be able to bypass Privacy preferences
Description: Multiple issues were addressed by removing the
vulnerable code.
CVE-2022-42859: Mickey Jin (@patch1t), Csaba Fitzl (@theevilbit) of
Offensive Security

DriverKit
Available for: macOS Ventura
Impact: An app may be able to execute arbitrary code with kernel
privileges
Description: The issue was addressed with improved memory handling.
CVE-2022-32942: Linus Henze of Pinauten GmbH (pinauten.de)

ImageIO
Available for: macOS Ventura
Impact: Processing a maliciously crafted file may lead to arbitrary
code execution
Description: An out-of-bounds write issue was addressed with improved
input validation.
CVE-2022-46693: Mickey Jin (@patch1t)

IOHIDFamily
Available for: macOS Ventura
Impact: An app may be able to execute arbitrary code with kernel
privileges
Description: A race condition was addressed with improved state
handling.
CVE-2022-42864: Tommy Muir (@Muirey03)

IOMobileFrameBuffer
Available for: macOS Ventura
Impact: An app may be able to execute arbitrary code with kernel
privileges
Description: An out-of-bounds write issue was addressed with improved
input validation.
CVE-2022-46690: John Aakerblom (@jaakerblom)

IOMobileFrameBuffer
Available for: macOS Ventura
Impact: An app may be able to execute arbitrary code with kernel
privileges
Description: An out-of-bounds access issue was addressed with
improved bounds checking.
CVE-2022-46697: John Aakerblom (@jaakerblom) and Antonio Zekic
(@antoniozekic)

iTunes Store
Available for: macOS Ventura
Impact: A remote user may be able to cause unexpected app termination
or arbitrary code execution
Description: An issue existed in the parsing of URLs. This issue was
addressed with improved input validation.
CVE-2022-42837: Weijia Dai (@dwj1210) of Momo Security

Kernel
Available for: macOS Ventura
Impact: An app may be able to execute arbitrary code with kernel
privileges
Description: A race condition was addressed with additional
validation.
CVE-2022-46689: Ian Beer of Google Project Zero

Kernel
Available for: macOS Ventura
Impact: Connecting to a malicious NFS server may lead to arbitrary
code execution with kernel privileges
Description: The issue was addressed with improved bounds checks.
CVE-2022-46701: Felix Poulin-Belanger

Kernel
Available for: macOS Ventura
Impact: A remote user may be able to cause kernel code execution
Description: The issue was addressed with improved memory handling.
CVE-2022-42842: pattern-f (@pattern_F_) of Ant Security Light-Year
Lab

Kernel
Available for: macOS Ventura
Impact: An app may be able to break out of its sandbox
Description: This issue was addressed with improved checks.
CVE-2022-42861: pattern-f (@pattern_F_) of Ant Security Light-Year
Lab

Kernel
Available for: macOS Ventura
Impact: An app with root privileges may be able to execute arbitrary
code with kernel privileges
Description: The issue was addressed with improved memory handling.
CVE-2022-42845: Adam Doupé of ASU SEFCOM

Photos
Available for: macOS Ventura
Impact: Shake-to-undo may allow a deleted photo to be re-surfaced
without authentication
Description: The issue was addressed with improved bounds checks.
CVE-2022-32943: an anonymous researcher

ppp
Available for: macOS Ventura
Impact: An app may be able to execute arbitrary code with kernel
privileges
Description: The issue was addressed with improved memory handling.
CVE-2022-42840: an anonymous researcher

Preferences
Available for: macOS Ventura
Impact: An app may be able to use arbitrary entitlements
Description: A logic issue was addressed with improved state
management.
CVE-2022-42855: Ivan Fratric of Google Project Zero

Printing
Available for: macOS Ventura
Impact: An app may be able to bypass Privacy preferences
Description: This issue was addressed by removing the vulnerable
code.
CVE-2022-42862: Mickey Jin (@patch1t)

Ruby
Available for: macOS Ventura
Impact: A remote user may be able to cause unexpected app termination
or arbitrary code execution
Description: This issue was addressed with improved checks.
CVE-2022-24836
CVE-2022-29181

Safari
Available for: macOS Ventura
Impact: Visiting a website that frames malicious content may lead to
UI spoofing
Description: A spoofing issue existed in the handling of URLs. This
issue was addressed with improved input validation.
CVE-2022-46695: KirtiKumar Anandrao Ramchandani

Weather
Available for: macOS Ventura
Impact: An app may be able to read sensitive location information
Description: The issue was addressed with improved handling of
caches.
CVE-2022-42866: an anonymous researcher

WebKit
Available for: macOS Ventura
Impact: Processing maliciously crafted web content may lead to
arbitrary code execution
Description: A use after free issue was addressed with improved
memory management.
WebKit Bugzilla: 245521
CVE-2022-42867: Maddie Stone of Google Project Zero

WebKit
Available for: macOS Ventura
Impact: Processing maliciously crafted web content may lead to
arbitrary code execution
Description: A memory consumption issue was addressed with improved
memory handling.
WebKit Bugzilla: 245466
CVE-2022-46691: an anonymous researcher

WebKit
Available for: macOS Ventura
Impact: Processing maliciously crafted web content may bypass Same
Origin Policy
Description: A logic issue was addressed with improved state
management.
WebKit Bugzilla: 246783
CVE-2022-46692: KirtiKumar Anandrao Ramchandani

WebKit
Available for: macOS Ventura
Impact: Processing maliciously crafted web content may result in the
disclosure of process memory
Description: The issue was addressed with improved memory...