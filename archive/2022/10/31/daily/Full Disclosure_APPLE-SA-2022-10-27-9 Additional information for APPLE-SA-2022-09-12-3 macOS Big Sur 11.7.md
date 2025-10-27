---
title: APPLE-SA-2022-10-27-9 Additional information for APPLE-SA-2022-09-12-3 macOS Big Sur 11.7
url: https://seclists.org/fulldisclosure/2022/Oct/45
source: Full Disclosure
date: 2022-10-31
fetch_date: 2025-10-03T21:21:59.506131
---

# APPLE-SA-2022-10-27-9 Additional information for APPLE-SA-2022-09-12-3 macOS Big Sur 11.7

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

[![Previous](/images/left-icon-16x16.png)](44)
[By Date](date.html#45)
[![Next](/images/right-icon-16x16.png)](46)

[![Previous](/images/left-icon-16x16.png)](44)
[By Thread](index.html#45)
[![Next](/images/right-icon-16x16.png)](46)

![](/shared/images/nst-icons.svg#search)

# APPLE-SA-2022-10-27-9 Additional information for APPLE-SA-2022-09-12-3 macOS Big Sur 11.7

---

*From*: Apple Product Security via Fulldisclosure <fulldisclosure () seclists org>
*Date*: Thu, 27 Oct 2022 18:23:44 -0700

---

```
-----BEGIN PGP SIGNED MESSAGE-----
Hash: SHA256

APPLE-SA-2022-10-27-9 Additional information for APPLE-SA-2022-09-12-3 macOS Big Sur 11.7

macOS Big Sur 11.7 addresses the following issues.
Information about the security content is also available at
https://support.apple.com/HT213443.

AppleMobileFileIntegrity
Available for: macOS Big Sur
Impact: An app may be able to access user-sensitive data
Description: An issue in code signature validation was addressed with
improved checks.
CVE-2022-42789: Koh M. Nakagawa of FFRI Security, Inc.
Entry added October 27, 2022

ATS
Available for: macOS Big Sur
Impact: An app may be able to access user-sensitive data
Description: An access issue was addressed with additional sandbox
restrictions.
CVE-2022-32904: Mickey Jin (@patch1t)
Entry added October 27, 2022

ATS
Available for: macOS Big Sur
Impact: An app may be able to bypass Privacy preferences
Description: A logic issue was addressed with improved state
management.
CVE-2022-32902: Mickey Jin (@patch1t)

Calendar
Available for: macOS Big Sur
Impact: An app may be able to read sensitive location information
Description: An access issue was addressed with improved access
restrictions.
CVE-2022-42819: an anonymous researcher
Entry added October 27, 2022

Contacts
Available for: macOS Big Sur
Impact: An app may be able to bypass Privacy preferences
Description: This issue was addressed with improved checks.
CVE-2022-32854: Holger Fuhrmannek of Deutsche Telekom Security

GarageBand
Available for: macOS Big Sur
Impact: An app may be able to access user-sensitive data
Description: A configuration issue was addressed with additional
restrictions.
CVE-2022-32877: Wojciech Reguła (@_r3ggi) of SecuRing
Entry added October 27, 2022

ImageIO
Available for: macOS Big Sur
Impact: Processing an image may lead to a denial-of-service
Description: A denial-of-service issue was addressed with improved
validation.
CVE-2022-1622
Entry added October 27, 2022

Image Processing
Available for: macOS Big Sur
Impact: A sandboxed app may be able to determine which app is
currently using the camera
Description: The issue was addressed with additional restrictions on
the observability of app states.
CVE-2022-32913: Yiğit Can YILMAZ (@yilmazcanyigit)
Entry added October 27, 2022

iMovie
Available for: macOS Big Sur
Impact: A user may be able to view sensitive user information
Description: This issue was addressed by enabling hardened runtime.
CVE-2022-32896: Wojciech Reguła (@_r3ggi)

Kernel
Available for: macOS Big Sur
Impact: An app may be able to execute arbitrary code with kernel
privileges
Description: A use after free issue was addressed with improved
memory management.
CVE-2022-32914: Zweig of Kunlun Lab
Entry added October 27, 2022

Kernel
Available for: macOS Big Sur
Impact: An app may be able to execute arbitrary code with kernel
privileges
Description: The issue was addressed with improved memory handling.
CVE-2022-32866: Linus Henze of Pinauten GmbH (pinauten.de)
CVE-2022-32911: Zweig of Kunlun Lab
CVE-2022-32924: Ian Beer of Google Project Zero
Entry updated October 27, 2022

Kernel
Available for: macOS Big Sur
Impact: An app may be able to disclose kernel memory
Description: The issue was addressed with improved memory handling.
CVE-2022-32864: Linus Henze of Pinauten GmbH (pinauten.de)

Kernel
Available for: macOS Big Sur
Impact: An application may be able to execute arbitrary code with
kernel privileges. Apple is aware of a report that this issue may
have been actively exploited.
Description: An out-of-bounds write issue was addressed with improved
bounds checking.
CVE-2022-32894: an anonymous researcher

Kernel
Available for: macOS Big Sur
Impact: An application may be able to execute arbitrary code with
kernel privileges. Apple is aware of a report that this issue may
have been actively exploited.
Description: The issue was addressed with improved bounds checks.
CVE-2022-32917: an anonymous researcher

Maps
Available for: macOS Big Sur
Impact: An app may be able to read sensitive location information
Description: A logic issue was addressed with improved restrictions.
CVE-2022-32883: Ron Masas of breakpointhq.com
Entry updated October 27, 2022

MediaLibrary
Available for: macOS Big Sur
Impact: A user may be able to elevate privileges
Description: A memory corruption issue was addressed with improved
input validation.
CVE-2022-32908: an anonymous researcher

ncurses
Available for: macOS Big Sur
Impact: A user may be able to cause unexpected app termination or
arbitrary code execution
Description: A buffer overflow was addressed with improved bounds
checking.
CVE-2021-39537
Entry added October 27, 2022

PackageKit
Available for: macOS Big Sur
Impact: An app may be able to gain elevated privileges
Description: A logic issue was addressed with improved state
management.
CVE-2022-32900: Mickey Jin (@patch1t)

Sandbox
Available for: macOS Big Sur
Impact: An app may be able to modify protected parts of the file
system
Description: A logic issue was addressed with improved restrictions.
CVE-2022-32881: Csaba Fitzl (@theevilbit) of Offensive Security
Entry added October 27, 2022

Security
Available for: macOS Big Sur
Impact: An app may be able to bypass code signing checks
Description: An issue in code signature validation was addressed with
improved checks.
CVE-2022-42793: Linus Henze of Pinauten GmbH (pinauten.de)
Entry added October 27, 2022

Sidecar
Available for: macOS Big Sur
Impact: A user may be able to view restricted content from the lock
screen
Description: A logic issue was addressed with improved state
management.
CVE-2022-42790: Om kothawade of Zaprico Digital
Entry added October 27, 2022

SMB
Available for: macOS Big Sur
Impact: A remote user may be able to cause kernel code execution
Description: The issue was addressed with improved memory handling.
CVE-2022-32934: Felix Poulin-Belanger
Entry added October 27, 2022

Vim
Available for: macOS Big Sur
Impact: Processing a maliciously crafted file may lead to a denial-
of-service or potentially disclose memory contents
Description: This issue was addressed with improved checks.
CVE-2022-1720
CVE-2022-2000
CVE-2022-2042
CVE-2022-2124
CVE-2022-2125
CVE-2022-2126
Entry added October 27, 2022

Weather
Available for: macOS Big Sur
Impact: An app may be able to read sensitive location information
Description: A logic issue was addressed with improved state
management.
CVE-2022-32875: an anonymous researcher
Entry added October 27, 2022

WebKit
Available for: macOS Big Sur
Impact: Processing maliciously crafted web content may lead to
arbitrary code execution
Description: An out-of-bounds write issue was addressed with improved
bounds checking.
WebKit Bugzilla: 242047
CVE-2022-32888: P1umer (@p1umer)
Entry added October 27, 2022

Additional recognition

Identity Services
We would like to acknowledge Joshua Jones for their assistance.

macOS Big Sur 11.7 may be obtained from the Mac App Store or Apple's
Software Downloads web site: https://supp...