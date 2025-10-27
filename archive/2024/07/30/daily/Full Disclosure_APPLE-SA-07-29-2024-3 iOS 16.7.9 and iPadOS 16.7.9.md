---
title: APPLE-SA-07-29-2024-3 iOS 16.7.9 and iPadOS 16.7.9
url: https://seclists.org/fulldisclosure/2024/Jul/17
source: Full Disclosure
date: 2024-07-30
fetch_date: 2025-10-06T17:47:09.858105
---

# APPLE-SA-07-29-2024-3 iOS 16.7.9 and iPadOS 16.7.9

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

[![Previous](/images/left-icon-16x16.png)](16)
[By Date](date.html#17)
[![Next](/images/right-icon-16x16.png)](18)

[![Previous](/images/left-icon-16x16.png)](16)
[By Thread](index.html#17)
[![Next](/images/right-icon-16x16.png)](18)

![](/shared/images/nst-icons.svg#search)

# APPLE-SA-07-29-2024-3 iOS 16.7.9 and iPadOS 16.7.9

---

*From*: Apple Product Security via Fulldisclosure <fulldisclosure () seclists org>
*Date*: Mon, 29 Jul 2024 16:12:31 -0700

---

```
-----BEGIN PGP SIGNED MESSAGE-----
Hash: SHA256

APPLE-SA-07-29-2024-3 iOS 16.7.9 and iPadOS 16.7.9

iOS 16.7.9 and iPadOS 16.7.9 addresses the following issues.
Information about the security content is also available at
https://support.apple.com/HT214116.

Apple maintains a Security Releases page at
https://support.apple.com/HT201222 which lists recent
software updates with security advisories.

CoreGraphics
Available for: iPhone 8, iPhone 8 Plus, iPhone X, iPad 5th generation,
iPad Pro 9.7-inch, and iPad Pro 12.9-inch 1st generation
Impact: Processing a maliciously crafted file may lead to unexpected app
termination
Description: An out-of-bounds read issue was addressed with improved
input validation.
CVE-2024-40799: D4m0n

CoreMedia
Available for: iPhone 8, iPhone 8 Plus, iPhone X, iPad 5th generation,
iPad Pro 9.7-inch, and iPad Pro 12.9-inch 1st generation
Impact: Processing a maliciously crafted video file may lead to
unexpected app termination
Description: An out-of-bounds write issue was addressed with improved
input validation.
CVE-2024-27873: Amir Bazine and Karsten KÃ¶nig of CrowdStrike Counter
Adversary Operations

ImageIO
Available for: iPhone 8, iPhone 8 Plus, iPhone X, iPad 5th generation,
iPad Pro 9.7-inch, and iPad Pro 12.9-inch 1st generation
Impact: Processing an image may lead to a denial-of-service
Description: This is a vulnerability in open source code and Apple
Software is among the affected projects. The CVE-ID was assigned by a
third party. Learn more about the issue and CVE-ID at cve.org.
CVE-2023-6277
CVE-2023-52356

ImageIO
Available for: iPhone 8, iPhone 8 Plus, iPhone X, iPad 5th generation,
iPad Pro 9.7-inch, and iPad Pro 12.9-inch 1st generation
Impact: Processing a maliciously crafted file may lead to unexpected app
termination
Description: An out-of-bounds read issue was addressed with improved
input validation.
CVE-2024-40806: Yisumi

ImageIO
Available for: iPhone 8, iPhone 8 Plus, iPhone X, iPad 5th generation,
iPad Pro 9.7-inch, and iPad Pro 12.9-inch 1st generation
Impact: Processing a maliciously crafted file may lead to unexpected app
termination
Description: An integer overflow was addressed with improved input
validation.
CVE-2024-40784: Junsung Lee working with Trend Micro Zero Day Initiative
and Gandalf4a

Kernel
Available for: iPhone 8, iPhone 8 Plus, iPhone X, iPad 5th generation,
iPad Pro 9.7-inch, and iPad Pro 12.9-inch 1st generation
Impact: A local attacker may be able to cause unexpected system shutdown
Description: A type confusion issue was addressed with improved memory
handling.
CVE-2024-40788: Minghao Lin and Jiaxun Zhu from Zhejiang University

NetworkExtension
Available for: iPhone 8, iPhone 8 Plus, iPhone X, iPad 5th generation,
iPad Pro 9.7-inch, and iPad Pro 12.9-inch 1st generation
Impact: Private browsing may leak some browsing history
Description: A privacy issue was addressed with improved private data
redaction for log entries.
CVE-2024-40796: Adam M.

Photos Storage
Available for: iPhone 8, iPhone 8 Plus, iPhone X, iPad 5th generation,
iPad Pro 9.7-inch, and iPad Pro 12.9-inch 1st generation
Impact: Photos in the Hidden Photos Album may be viewed without
authentication
Description: An authentication issue was addressed with improved state
management.
CVE-2024-40778: Mateen Alinaghi

Security
Available for: iPhone 8, iPhone 8 Plus, iPhone X, iPad 5th generation,
iPad Pro 9.7-inch, and iPad Pro 12.9-inch 1st generation
Impact: An app may be able to read Safari's browsing history
Description: This issue was addressed with improved redaction of
sensitive information.
CVE-2024-40798: Adam M.

Shortcuts
Available for: iPhone 8, iPhone 8 Plus, iPhone X, iPad 5th generation,
iPad Pro 9.7-inch, and iPad Pro 12.9-inch 1st generation
Impact: A shortcut may be able to use sensitive data with certain
actions without prompting the user
Description: A logic issue was addressed with improved checks.
CVE-2024-40833: an anonymous researcher
CVE-2024-40835: an anonymous researcher
CVE-2024-40836: an anonymous researcher

Shortcuts
Available for: iPhone 8, iPhone 8 Plus, iPhone X, iPad 5th generation,
iPad Pro 9.7-inch, and iPad Pro 12.9-inch 1st generation
Impact: An app may be able to access user-sensitive data
Description: This issue was addressed by removing the vulnerable code.
CVE-2024-40793: Kirin (@Pwnrin)

Shortcuts
Available for: iPhone 8, iPhone 8 Plus, iPhone X, iPad 5th generation,
iPad Pro 9.7-inch, and iPad Pro 12.9-inch 1st generation
Impact: A shortcut may be able to bypass Internet permission
requirements
Description: A logic issue was addressed with improved checks.
CVE-2024-40809: an anonymous researcher
CVE-2024-40812: an anonymous researcher

Siri
Available for: iPhone 8, iPhone 8 Plus, iPhone X, iPad 5th generation,
iPad Pro 9.7-inch, and iPad Pro 12.9-inch 1st generation
Impact: An attacker with physical access may be able to use Siri to
access sensitive user data
Description: This issue was addressed by restricting options offered on
a locked device.
CVE-2024-40818: Bistrit Dahal and Srijan Poudel

Siri
Available for: iPhone 8, iPhone 8 Plus, iPhone X, iPad 5th generation,
iPad Pro 9.7-inch, and iPad Pro 12.9-inch 1st generation
Impact: An attacker may be able to view sensitive user information
Description: This issue was addressed through improved state management.
CVE-2024-40786: Bistrit Dahal

Siri
Available for: iPhone 8, iPhone 8 Plus, iPhone X, iPad 5th generation,
iPad Pro 9.7-inch, and iPad Pro 12.9-inch 1st generation
Impact: An attacker with physical access to a device may be able to
access contacts from the lock screen
Description: This issue was addressed by restricting options offered on
a locked device.
CVE-2024-40822: Srijan Poudel

VoiceOver
Available for: iPhone 8, iPhone 8 Plus, iPhone X, iPad 5th generation,
iPad Pro 9.7-inch, and iPad Pro 12.9-inch 1st generation
Impact: An attacker may be able to view restricted content from the lock
screen
Description: The issue was addressed with improved checks.
CVE-2024-40829: Abhay Kailasia (@abhay_kailasia) of Lakshmi Narain
College of Technology Bhopal India

WebKit
Available for: iPhone 8, iPhone 8 Plus, iPhone X, iPad 5th generation,
iPad Pro 9.7-inch, and iPad Pro 12.9-inch 1st generation
Impact: Processing maliciously crafted web content may lead to an
unexpected process crash
Description: An out-of-bounds access issue was addressed with improved
bounds checking.
CVE-2024-40789: Seunghyun Lee (@0x10n) of KAIST Hacking Lab working with
Trend Micro Zero Day Initiative

WebKit
Available for: iPhone 8, iPhone 8 Plus, iPhone X, iPad 5th generation,
iPad Pro 9.7-inch, and iPad Pro 12.9-inch 1st generation
Impact: Processing maliciously crafted web content may lead to an
unexpected process crash
Description: A use-after-free issue was addressed with improved memory
management.
WebKit Bugzilla: 273176
CVE-2024-40776: Huang Xilin of Ant Group Light-Year Security Lab
WebKit Bugzilla: 268770
CVE-2024-40782: Maksymilian Motyl

WebKit
Available for: iPhone 8, iPhone 8 Plus, iPhone X...