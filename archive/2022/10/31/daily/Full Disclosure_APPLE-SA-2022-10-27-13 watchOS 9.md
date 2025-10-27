---
title: APPLE-SA-2022-10-27-13 watchOS 9
url: https://seclists.org/fulldisclosure/2022/Oct/49
source: Full Disclosure
date: 2022-10-31
fetch_date: 2025-10-03T21:21:54.541732
---

# APPLE-SA-2022-10-27-13 watchOS 9

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

[![Previous](/images/left-icon-16x16.png)](48)
[By Date](date.html#49)
[![Next](/images/right-icon-16x16.png)](50)

[![Previous](/images/left-icon-16x16.png)](48)
[By Thread](index.html#49)
[![Next](/images/right-icon-16x16.png)](50)

![](/shared/images/nst-icons.svg#search)

# APPLE-SA-2022-10-27-13 watchOS 9

---

*From*: Apple Product Security via Fulldisclosure <fulldisclosure () seclists org>
*Date*: Thu, 27 Oct 2022 18:23:50 -0700

---

```
-----BEGIN PGP SIGNED MESSAGE-----
Hash: SHA256

APPLE-SA-2022-10-27-13 watchOS 9

watchOS 9 addresses the following issues.
Information about the security content is also available at
https://support.apple.com/HT213486.

Accelerate Framework
Available for: Apple Watch Series 4 and later
Impact: Processing a maliciously crafted image may lead to arbitrary
code execution
Description: A memory consumption issue was addressed with improved
memory handling.
CVE-2022-42795: ryuzaki

AppleAVD
Available for: Apple Watch Series 4 and later
Impact: An app may be able to execute arbitrary code with kernel
privileges
Description: This issue was addressed with improved checks.
CVE-2022-32907: Natalie Silvanovich of Google Project Zero, Antonio
Zekic (@antoniozekic) and John Aakerblom (@jaakerblom), ABC Research
s.r.o, Yinyi Wu, Tommaso Bianco (@cutesmilee__)

Apple Neural Engine
Available for: Apple Watch Series 4 and later
Impact: An app may be able to leak sensitive kernel state
Description: The issue was addressed with improved memory handling.
CVE-2022-32858: Mohamed Ghannam (@_simo36)

Apple Neural Engine
Available for: Apple Watch Series 4 and later
Impact: An app may be able to execute arbitrary code with kernel
privileges
Description: The issue was addressed with improved memory handling.
CVE-2022-32898: Mohamed Ghannam (@_simo36)
CVE-2022-32899: Mohamed Ghannam (@_simo36)
CVE-2022-32889: Mohamed Ghannam (@_simo36)

Contacts
Available for: Apple Watch Series 4 and later
Impact: An app may be able to bypass Privacy preferences
Description: This issue was addressed with improved checks.
CVE-2022-32854: Holger Fuhrmannek of Deutsche Telekom Security

Exchange
Available for: Apple Watch Series 4 and later
Impact: A user in a privileged network position may be able to
intercept mail credentials
Description: A logic issue was addressed with improved restrictions.
CVE-2022-32928: an anonymous researcher

GPU Drivers
Available for: Apple Watch Series 4 and later
Impact: An app may be able to execute arbitrary code with kernel
privileges
Description: A use after free issue was addressed with improved
memory management.
CVE-2022-32903: an anonymous researcher

ImageIO
Available for: Apple Watch Series 4 and later
Impact: Processing an image may lead to a denial-of-service
Description: A denial-of-service issue was addressed with improved
validation.
CVE-2022-1622

Image Processing
Available for: Apple Watch Series 4 and later
Impact: A sandboxed app may be able to determine which app is
currently using the camera
Description: The issue was addressed with additional restrictions on
the observability of app states.
CVE-2022-32913: Yiğit Can YILMAZ (@yilmazcanyigit)

Kernel
Available for: Apple Watch Series 4 and later
Impact: An app may be able to disclose kernel memory
Description: The issue was addressed with improved memory handling.
CVE-2022-32864: Linus Henze of Pinauten GmbH (pinauten.de)

Kernel
Available for: Apple Watch Series 4 and later
Impact: An app may be able to execute arbitrary code with kernel
privileges
Description: The issue was addressed with improved memory handling.
CVE-2022-32866: Linus Henze of Pinauten GmbH (pinauten.de)
CVE-2022-32911: Zweig of Kunlun Lab

Kernel
Available for: Apple Watch Series 4 and later
Impact: An app may be able to execute arbitrary code with kernel
privileges
Description: A use after free issue was addressed with improved
memory management.
CVE-2022-32914: Zweig of Kunlun Lab

Kernel
Available for: Apple Watch Series 4 and later
Impact: An application may be able to execute arbitrary code with
kernel privileges. Apple is aware of a report that this issue may
have been actively exploited.
Description: An out-of-bounds write issue was addressed with improved
bounds checking.
CVE-2022-32894: an anonymous researcher

Maps
Available for: Apple Watch Series 4 and later
Impact: An app may be able to read sensitive location information
Description: A logic issue was addressed with improved restrictions.
CVE-2022-32883: Ron Masas of breakpointhq.com

MediaLibrary
Available for: Apple Watch Series 4 and later
Impact: A user may be able to elevate privileges
Description: A memory corruption issue was addressed with improved
input validation.
CVE-2022-32908: an anonymous researcher

Notifications
Available for: Apple Watch Series 4 and later
Impact: A user with physical access to a device may be able to access
contacts from the lock screen
Description: A logic issue was addressed with improved state
management.
CVE-2022-32879: Ubeydullah Sümer

Sandbox
Available for: Apple Watch Series 4 and later
Impact: An app may be able to modify protected parts of the file
system
Description: A logic issue was addressed with improved restrictions.
CVE-2022-32881: Csaba Fitzl (@theevilbit) of Offensive Security

Siri
Available for: Apple Watch Series 4 and later
Impact: A user with physical access to a device may be able to use
Siri to obtain some call history information
Description: A logic issue was addressed with improved state
management.
CVE-2022-32870: Andrew Goldberg of The McCombs School of Business,
The University of Texas at Austin (linkedin.com/in/andrew-goldberg-/)

SQLite
Available for: Apple Watch Series 4 and later
Impact: A remote user may be able to cause a denial-of-service
Description: This issue was addressed with improved checks.
CVE-2021-36690

Watch app
Available for: Apple Watch Series 4 and later
Impact: An app may be able to read a persistent device identifier
Description: This issue was addressed with improved entitlements.
CVE-2022-32835: Guilherme Rambo of Best Buddy Apps (rambo.codes)

Weather
Available for: Apple Watch Series 4 and later
Impact: An app may be able to read sensitive location information
Description: A logic issue was addressed with improved state
management.
CVE-2022-32875: an anonymous researcher

WebKit
Available for: Apple Watch Series 4 and later
Impact: Processing maliciously crafted web content may lead to
arbitrary code execution
Description: A buffer overflow issue was addressed with improved
memory handling.
WebKit Bugzilla: 241969
CVE-2022-32886: P1umer(@p1umer), afang(@afang5472),
xmzyshypnc(@xmzyshypnc1)

WebKit
Available for: Apple Watch Series 4 and later
Impact: Processing maliciously crafted web content may lead to
arbitrary code execution
Description: An out-of-bounds write issue was addressed with improved
bounds checking.
WebKit Bugzilla: 242047
CVE-2022-32888: P1umer (@p1umer)

WebKit
Available for: Apple Watch Series 4 and later
Impact: Processing maliciously crafted web content may lead to
arbitrary code execution
Description: An out-of-bounds read was addressed with improved bounds
checking.
WebKit Bugzilla: 242762
CVE-2022-32912: Jeonghoon Shin (@singi21a) at Theori working with
Trend Micro Zero Day Initiative

WebKit
Available for: Apple Watch Series 4 and later
Impact: Visiting a website that frames malicious content may lead to
UI spoofing
Description: The issue was addressed with improved UI handling.
WebKit Bugzilla: 243236
CVE-2022-32891:...