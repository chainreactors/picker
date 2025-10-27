---
title: APPLE-SA-2022-10-27-4 Additional information for APPLE-SA-2022-09-12-2 iOS 15.7 and iPadOS 15.7
url: https://seclists.org/fulldisclosure/2022/Oct/40
source: Full Disclosure
date: 2022-10-31
fetch_date: 2025-10-03T21:22:06.094483
---

# APPLE-SA-2022-10-27-4 Additional information for APPLE-SA-2022-09-12-2 iOS 15.7 and iPadOS 15.7

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

[![Previous](/images/left-icon-16x16.png)](39)
[By Date](date.html#40)
[![Next](/images/right-icon-16x16.png)](41)

[![Previous](/images/left-icon-16x16.png)](39)
[By Thread](index.html#40)
[![Next](/images/right-icon-16x16.png)](41)

![](/shared/images/nst-icons.svg#search)

# APPLE-SA-2022-10-27-4 Additional information for APPLE-SA-2022-09-12-2 iOS 15.7 and iPadOS 15.7

---

*From*: Apple Product Security via Fulldisclosure <fulldisclosure () seclists org>
*Date*: Thu, 27 Oct 2022 18:23:20 -0700

---

```
-----BEGIN PGP SIGNED MESSAGE-----
Hash: SHA256

APPLE-SA-2022-10-27-4 Additional information for APPLE-SA-2022-09-12-2 iOS 15.7 and iPadOS 15.7

iOS 15.7 and iPadOS 15.7 addresses the following issues.
Information about the security content is also available at
https://support.apple.com/HT213445.

Apple Neural Engine
Available for: iPhone 6s and later, iPad Pro (all models), iPad Air 2
and later, iPad 5th generation and later, iPad mini 4 and later, and
iPod touch (7th generation)
Impact: An app may be able to execute arbitrary code with kernel
privileges
Description: The issue was addressed with improved memory handling.
CVE-2022-32898: Mohamed Ghannam (@_simo36)
CVE-2022-32899: Mohamed Ghannam (@_simo36)
Entry added October 27, 2022

Audio
Available for: iPhone 6s and later, iPad Pro (all models), iPad Air 2
and later, iPad 5th generation and later, iPad mini 4 and later, and
iPod touch (7th generation)
Impact: An app may be able to gain elevated privileges
Description: This issue was addressed by removing the vulnerable
code.
CVE-2022-42796: an anonymous researcher
Entry added October 27, 2022

Backup
Available for: iPhone 6s and later, iPad Pro (all models), iPad Air 2
and later, iPad 5th generation and later, iPad mini 4 and later, and
iPod touch (7th generation)
Impact: An app may be able to access iOS backups
Description: A permissions issue was addressed with additional
restrictions.
CVE-2022-32929: Csaba Fitzl (@theevilbit) of Offensive Security
Entry added October 27, 2022

Contacts
Available for: iPhone 6s and later, iPad Pro (all models), iPad Air 2
and later, iPad 5th generation and later, iPad mini 4 and later, and
iPod touch (7th generation)
Impact: An app may be able to bypass Privacy preferences
Description: This issue was addressed with improved checks.
CVE-2022-32854: Holger Fuhrmannek of Deutsche Telekom Security

Kernel
Available for: iPhone 6s and later, iPad Pro (all models), iPad Air 2
and later, iPad 5th generation and later, iPad mini 4 and later, and
iPod touch (7th generation)
Impact: An app may be able to execute arbitrary code with kernel
privileges
Description: The issue was addressed with improved memory handling.
CVE-2022-32911: Zweig of Kunlun Lab

Kernel
Available for: iPhone 6s and later, iPad Pro (all models), iPad Air 2
and later, iPad 5th generation and later, iPad mini 4 and later, and
iPod touch (7th generation)
Impact: An app may be able to disclose kernel memory
Description: The issue was addressed with improved memory handling.
CVE-2022-32864: Linus Henze of Pinauten GmbH (pinauten.de)

Kernel
Available for: iPhone 6s and later, iPad Pro (all models), iPad Air 2
and later, iPad 5th generation and later, iPad mini 4 and later, and
iPod touch (7th generation)
Impact: An application may be able to execute arbitrary code with
kernel privileges. Apple is aware of a report that this issue may
have been actively exploited.
Description: The issue was addressed with improved bounds checks.
CVE-2022-32917: an anonymous researcher

Maps
Available for: iPhone 6s and later, iPad Pro (all models), iPad Air 2
and later, iPad 5th generation and later, iPad mini 4 and later, and
iPod touch (7th generation)
Impact: An app may be able to read sensitive location information
Description: A logic issue was addressed with improved restrictions.
CVE-2022-32883: Ron Masas, breakpointhq.com

MediaLibrary
Available for: iPhone 6s and later, iPad Pro (all models), iPad Air 2
and later, iPad 5th generation and later, iPad mini 4 and later, and
iPod touch (7th generation)
Impact: A user may be able to elevate privileges
Description: A memory corruption issue was addressed with improved
input validation.
CVE-2022-32908: an anonymous researcher

Notifications
Available for: iPhone 6s and later, iPad Pro (all models), iPad Air 2
and later, iPad 5th generation and later, iPad mini 4 and later, and
iPod touch (7th generation)
Impact: A user with physical access to a device may be able to access
contacts from the lock screen
Description: A logic issue was addressed with improved state
management.
CVE-2022-32879: Ubeydullah Sümer
Entry added October 27, 2022

Safari
Available for: iPhone 6s and later, iPad Pro (all models), iPad Air 2
and later, iPad 5th generation and later, iPad mini 4 and later, and
iPod touch (7th generation)
Impact: Visiting a malicious website may lead to address bar spoofing
Description: This issue was addressed with improved checks.
CVE-2022-32795: Narendra Bhati of Suma Soft Pvt. Ltd. Pune (India)
@imnarendrabhati

Safari Extensions
Available for: iPhone 6s and later, iPad Pro (all models), iPad Air 2
and later, iPad 5th generation and later, iPad mini 4 and later, and
iPod touch (7th generation)
Impact: A website may be able to track users through Safari web
extensions
Description: A logic issue was addressed with improved state
management.
WebKit Bugzilla: 242278
CVE-2022-32868: Michael

Security
Available for: iPhone 6s and later, iPad Pro (all models), iPad Air 2
and later, iPad 5th generation and later, iPad mini 4 and later, and
iPod touch (7th generation)
Impact: An app may be able to bypass code signing checks
Description: An issue in code signature validation was addressed with
improved checks.
CVE-2022-42793: Linus Henze of Pinauten GmbH (pinauten.de)
Entry added October 27, 2022

Shortcuts
Available for: iPhone 6s and later, iPad Pro (all models), iPad Air 2
and later, iPad 5th generation and later, iPad mini 4 and later, and
iPod touch (7th generation)
Impact: A person with physical access to an iOS device may be able to
access photos from the lock screen
Description: A logic issue was addressed with improved restrictions.
CVE-2022-32872: Elite Tech Guru

Sidecar
Available for: iPhone 6s and later, iPad Pro (all models), iPad Air 2
and later, iPad 5th generation and later, iPad mini 4 and later, and
iPod touch (7th generation)
Impact: A user may be able to view restricted content from the lock
screen
Description: A logic issue was addressed with improved state
management.
CVE-2022-42790: Om kothawade of Zaprico Digital
Entry added October 27, 2022

WebKit
Available for: iPhone 6s and later, iPad Pro (all models), iPad Air 2
and later, iPad 5th generation and later, iPad mini 4 and later, and
iPod touch (7th generation)
Impact: Processing maliciously crafted web content may lead to
arbitrary code execution
Description: An out-of-bounds write issue was addressed with improved
bounds checking.
WebKit Bugzilla: 242047
CVE-2022-32888: P1umer (@p1umer)
Entry added October 27, 2022

WebKit
Available for: iPhone 6s and later, iPad Pro (all models), iPad Air 2
and later, iPad 5th generation and later, iPad mini 4 and later, and
iPod touch (7th generation)
Impact: Processing maliciously crafted web content may lead to
arbitrary code execution
Description: A buffer overflow issue was addressed with improved
memory handling.
WebKit Bugzilla: 241969
CVE-2022-32886: P1umer, afang5472, xmzyshypnc

WebKit
Available for: iPhone 6s and...