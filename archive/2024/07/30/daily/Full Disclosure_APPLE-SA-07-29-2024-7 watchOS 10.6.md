---
title: APPLE-SA-07-29-2024-7 watchOS 10.6
url: https://seclists.org/fulldisclosure/2024/Jul/21
source: Full Disclosure
date: 2024-07-30
fetch_date: 2025-10-06T17:47:04.104760
---

# APPLE-SA-07-29-2024-7 watchOS 10.6

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

# APPLE-SA-07-29-2024-7 watchOS 10.6

---

*From*: Apple Product Security via Fulldisclosure <fulldisclosure () seclists org>
*Date*: Mon, 29 Jul 2024 16:14:06 -0700

---

```
-----BEGIN PGP SIGNED MESSAGE-----
Hash: SHA256

APPLE-SA-07-29-2024-7 watchOS 10.6

watchOS 10.6 addresses the following issues.
Information about the security content is also available at
https://support.apple.com/HT214124.

Apple maintains a Security Releases page at
https://support.apple.com/HT201222 which lists recent
software updates with security advisories.

AppleMobileFileIntegrity
Available for: Apple Watch Series 4 and later
Impact: An app may be able to bypass Privacy preferences
Description: A downgrade issue was addressed with additional code-
signing restrictions.
CVE-2024-40774: Mickey Jin (@patch1t)

CoreGraphics
Available for: Apple Watch Series 4 and later
Impact: Processing a maliciously crafted file may lead to unexpected app
termination
Description: An out-of-bounds read issue was addressed with improved
input validation.
CVE-2024-40799: D4m0n

dyld
Available for: Apple Watch Series 4 and later
Impact: A malicious attacker with arbitrary read and write capability
may be able to bypass Pointer Authentication
Description: A race condition was addressed with additional validation.
CVE-2024-40815: w0wbox

Family Sharing
Available for: Apple Watch Series 4 and later
Impact: An app may be able to read sensitive location information
Description: This issue was addressed with improved data protection.
CVE-2024-40795: Csaba Fitzl (@theevilbit) of Kandji

ImageIO
Available for: Apple Watch Series 4 and later
Impact: Processing an image may lead to a denial-of-service
Description: This is a vulnerability in open source code and Apple
Software is among the affected projects. The CVE-ID was assigned by a
third party. Learn more about the issue and CVE-ID at cve.org.
CVE-2023-6277
CVE-2023-52356

ImageIO
Available for: Apple Watch Series 4 and later
Impact: Processing a maliciously crafted file may lead to unexpected app
termination
Description: An out-of-bounds read issue was addressed with improved
input validation.
CVE-2024-40806: Yisumi

ImageIO
Available for: Apple Watch Series 4 and later
Impact: Processing a maliciously crafted file may lead to unexpected app
termination
Description: An out-of-bounds access issue was addressed with improved
bounds checking.
CVE-2024-40777: Junsung Lee working with Trend Micro Zero Day
Initiative, Amir Bazine and Karsten KÃ¶nig of CrowdStrike Counter
Adversary Operations

ImageIO
Available for: Apple Watch Series 4 and later
Impact: Processing a maliciously crafted file may lead to unexpected app
termination
Description: An integer overflow was addressed with improved input
validation.
CVE-2024-40784: Junsung Lee working with Trend Micro Zero Day Initiative
and Gandalf4a

Kernel
Available for: Apple Watch Series 4 and later
Impact: A local attacker may be able to determine kernel memory layout
Description: An information disclosure issue was addressed with improved
private data redaction for log entries.
CVE-2024-27863: CertiK SkyFall Team

Kernel
Available for: Apple Watch Series 4 and later
Impact: A local attacker may be able to cause unexpected system shutdown
Description: A type confusion issue was addressed with improved memory
handling.
CVE-2024-40788: Minghao Lin and Jiaxun Zhu from Zhejiang University

libxpc
Available for: Apple Watch Series 4 and later
Impact: An app may be able to bypass Privacy preferences
Description: A permissions issue was addressed with additional
restrictions.
CVE-2024-40805

Phone
Available for: Apple Watch Series 4 and later
Impact: An attacker with physical access may be able to use Siri to
access sensitive user data
Description: A lock screen issue was addressed with improved state
management.
CVE-2024-40813: Jacob Braun

Sandbox
Available for: Apple Watch Series 4 and later
Impact: An app may be able to bypass Privacy preferences
Description: This issue was addressed through improved state management.
CVE-2024-40824: Wojciech Regula of SecuRing (wojciechregula.blog) and
Zhongquan Li (@Guluisacat) from Dawn Security Lab of JingDong

Shortcuts
Available for: Apple Watch Series 4 and later
Impact: A shortcut may be able to use sensitive data with certain
actions without prompting the user
Description: A logic issue was addressed with improved checks.
CVE-2024-40835: an anonymous researcher
CVE-2024-40836: an anonymous researcher

Shortcuts
Available for: Apple Watch Series 4 and later
Impact: A shortcut may be able to bypass Internet permission
requirements
Description: A logic issue was addressed with improved checks.
CVE-2024-40809: an anonymous researcher
CVE-2024-40812: an anonymous researcher

Shortcuts
Available for: Apple Watch Series 4 and later
Impact: A shortcut may be able to bypass Internet permission
requirements
Description: This issue was addressed by adding an additional prompt for
user consent.
CVE-2024-40787: an anonymous researcher

Shortcuts
Available for: Apple Watch Series 4 and later
Impact: An app may be able to access user-sensitive data
Description: This issue was addressed by removing the vulnerable code.
CVE-2024-40793: Kirin (@Pwnrin)

Siri
Available for: Apple Watch Series 4 and later
Impact: An attacker with physical access may be able to use Siri to
access sensitive user data
Description: This issue was addressed by restricting options offered on
a locked device.
CVE-2024-40818: Bistrit Dahal and Srijan Poudel

Siri
Available for: Apple Watch Series 4 and later
Impact: An attacker with physical access to a device may be able to
access contacts from the lock screen
Description: This issue was addressed by restricting options offered on
a locked device.
CVE-2024-40822: Srijan Poudel

VoiceOver
Available for: Apple Watch Series 4 and later
Impact: An attacker may be able to view restricted content from the lock
screen
Description: The issue was addressed with improved checks.
CVE-2024-40829: Abhay Kailasia (@abhay_kailasia) of Lakshmi Narain
College of Technology Bhopal India

WebKit
Available for: Apple Watch Series 4 and later
Impact: Processing maliciously crafted web content may lead to an
unexpected process crash
Description: A use-after-free issue was addressed with improved memory
management.
WebKit Bugzilla: 273176
CVE-2024-40776: Huang Xilin of Ant Group Light-Year Security Lab
WebKit Bugzilla: 268770
CVE-2024-40782: Maksymilian Motyl

WebKit
Available for: Apple Watch Series 4 and later
Impact: Processing maliciously crafted web content may lead to an
unexpected process crash
Description: An out-of-bounds read was addressed with improved bounds
checking.
WebKit Bugzilla: 275431
CVE-2024-40779: Huang Xilin of Ant Group Light-Year Security Lab
WebKit Bugzilla: 275273
CVE-2024-40780: Huang Xilin of Ant Group Light-Year Security Lab

WebKit
Available for: Apple Watch Series 4 and later
Impact: Processing maliciously crafted web content may lead to a cross
site scripting attack
Description: This issue was addressed with improved checks.
WebKit Bugzilla: 273805
CVE-2024-40785: Johan Carlsson (joaxcar)

WebKit
Available for: Apple Watch Series 4 and later
Impact: Processing maliciously crafted web content ma...