---
title: APPLE-SA-2022-10-27-5 Additional information for APPLE-SA-2022-10-24-2 macOS Ventura 13
url: https://seclists.org/fulldisclosure/2022/Oct/41
source: Full Disclosure
date: 2022-10-31
fetch_date: 2025-10-03T21:22:04.867264
---

# APPLE-SA-2022-10-27-5 Additional information for APPLE-SA-2022-10-24-2 macOS Ventura 13

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

[![Previous](/images/left-icon-16x16.png)](40)
[By Date](date.html#41)
[![Next](/images/right-icon-16x16.png)](42)

[![Previous](/images/left-icon-16x16.png)](40)
[By Thread](index.html#41)
[![Next](/images/right-icon-16x16.png)](42)

![](/shared/images/nst-icons.svg#search)

# APPLE-SA-2022-10-27-5 Additional information for APPLE-SA-2022-10-24-2 macOS Ventura 13

---

*From*: Apple Product Security via Fulldisclosure <fulldisclosure () seclists org>
*Date*: Thu, 27 Oct 2022 18:23:33 -0700

---

```
-----BEGIN PGP SIGNED MESSAGE-----
Hash: SHA256

APPLE-SA-2022-10-27-5 Additional information for APPLE-SA-2022-10-24-2 macOS Ventura 13

macOS Ventura 13 addresses the following issues.
Information about the security content is also available at
https://support.apple.com/HT213488.

Accelerate Framework
Available for: Mac Studio (2022), Mac Pro (2019 and later), MacBook
Air (2018 and later), MacBook Pro (2017 and later), Mac mini (2018
and later), iMac (2017 and later), MacBook (2017), and iMac Pro
(2017)
Impact: Processing a maliciously crafted image may lead to arbitrary
code execution
Description: A memory consumption issue was addressed with improved
memory handling.
CVE-2022-42795: ryuzaki

Apple Neural Engine
Available for: Mac Studio (2022), Mac Pro (2019 and later), MacBook
Air (2018 and later), MacBook Pro (2017 and later), Mac mini (2018
and later), iMac (2017 and later), MacBook (2017), and iMac Pro
(2017)
Impact: An app may be able to leak sensitive kernel state
Description: The issue was addressed with improved memory handling.
CVE-2022-32858: Mohamed Ghannam (@_simo36)

Apple Neural Engine
Available for: Mac Studio (2022), Mac Pro (2019 and later), MacBook
Air (2018 and later), MacBook Pro (2017 and later), Mac mini (2018
and later), iMac (2017 and later), MacBook (2017), and iMac Pro
(2017)
Impact: An app may be able to execute arbitrary code with kernel
privileges
Description: The issue was addressed with improved memory handling.
CVE-2022-32898: Mohamed Ghannam (@_simo36)
CVE-2022-32899: Mohamed Ghannam (@_simo36)

AppleAVD
Available for: Mac Studio (2022), Mac Pro (2019 and later), MacBook
Air (2018 and later), MacBook Pro (2017 and later), Mac mini (2018
and later), iMac (2017 and later), MacBook (2017), and iMac Pro
(2017)
Impact: An app may be able to cause a denial-of-service
Description: A memory corruption issue was addressed with improved
state management.
CVE-2022-32827: Antonio Zekic (@antoniozekic), Natalie Silvanovich of
Google Project Zero, an anonymous researcher

AppleMobileFileIntegrity
Available for: Mac Studio (2022), Mac Pro (2019 and later), MacBook
Air (2018 and later), MacBook Pro (2017 and later), Mac mini (2018
and later), iMac (2017 and later), MacBook (2017), and iMac Pro
(2017)
Impact: An app may be able to access user-sensitive data
Description: An issue in code signature validation was addressed with
improved checks.
CVE-2022-42789: Koh M. Nakagawa of FFRI Security, Inc.

AppleMobileFileIntegrity
Available for: Mac Studio (2022), Mac Pro (2019 and later), MacBook
Air (2018 and later), MacBook Pro (2017 and later), Mac mini (2018
and later), iMac (2017 and later), MacBook (2017), and iMac Pro
(2017)
Impact: An app may be able to modify protected parts of the file
system
Description: This issue was addressed by removing additional
entitlements.
CVE-2022-42825: Mickey Jin (@patch1t)

ATS
Available for: Mac Studio (2022), Mac Pro (2019 and later), MacBook
Air (2018 and later), MacBook Pro (2017 and later), Mac mini (2018
and later), iMac (2017 and later), MacBook (2017), and iMac Pro
(2017)
Impact: An app may be able to bypass Privacy preferences
Description: A logic issue was addressed with improved state
management.
CVE-2022-32902: Mickey Jin (@patch1t)

ATS
Available for: Mac Studio (2022), Mac Pro (2019 and later), MacBook
Air (2018 and later), MacBook Pro (2017 and later), Mac mini (2018
and later), iMac (2017 and later), MacBook (2017), and iMac Pro
(2017)
Impact: An app may be able to access user-sensitive data
Description: An access issue was addressed with additional sandbox
restrictions.
CVE-2022-32904: Mickey Jin (@patch1t)

ATS
Available for: Mac Studio (2022), Mac Pro (2019 and later), MacBook
Air (2018 and later), MacBook Pro (2017 and later), Mac mini (2018
and later), iMac (2017 and later), MacBook (2017), and iMac Pro
(2017)
Impact: A sandboxed process may be able to circumvent sandbox
restrictions
Description: A logic issue was addressed with improved checks.
CVE-2022-32890: Mickey Jin (@patch1t)

Audio
Available for: Mac Studio (2022), Mac Pro (2019 and later), MacBook
Air (2018 and later), MacBook Pro (2017 and later), Mac mini (2018
and later), iMac (2017 and later), MacBook (2017), and iMac Pro
(2017)
Impact: An app may be able to gain elevated privileges
Description: This issue was addressed by removing the vulnerable
code.
CVE-2022-42796: an anonymous researcher

Audio
Available for: Mac Studio (2022), Mac Pro (2019 and later), MacBook
Air (2018 and later), MacBook Pro (2017 and later), Mac mini (2018
and later), iMac (2017 and later), MacBook (2017), and iMac Pro
(2017)
Impact: Parsing a maliciously crafted audio file may lead to
disclosure of user information
Description: The issue was addressed with improved memory handling.
CVE-2022-42798: Anonymous working with Trend Micro Zero Day
Initiative
Entry added October 27, 2022

AVEVideoEncoder
Available for: Mac Studio (2022), Mac Pro (2019 and later), MacBook
Air (2018 and later), MacBook Pro (2017 and later), Mac mini (2018
and later), iMac (2017 and later), MacBook (2017), and iMac Pro
(2017)
Impact: An app may be able to execute arbitrary code with kernel
privileges
Description: The issue was addressed with improved bounds checks.
CVE-2022-32940: ABC Research s.r.o.

Calendar
Available for: Mac Studio (2022), Mac Pro (2019 and later), MacBook
Air (2018 and later), MacBook Pro (2017 and later), Mac mini (2018
and later), iMac (2017 and later), MacBook (2017), and iMac Pro
(2017)
Impact: An app may be able to read sensitive location information
Description: An access issue was addressed with improved access
restrictions.
CVE-2022-42819: an anonymous researcher

CFNetwork
Available for: Mac Studio (2022), Mac Pro (2019 and later), MacBook
Air (2018 and later), MacBook Pro (2017 and later), Mac mini (2018
and later), iMac (2017 and later), MacBook (2017), and iMac Pro
(2017)
Impact: Processing a maliciously crafted certificate may lead to
arbitrary code execution
Description: A certificate validation issue existed in the handling
of WKWebView. This issue was addressed with improved validation.
CVE-2022-42813: Jonathan Zhang of Open Computing Facility
(ocf.berkeley.edu)

ColorSync
Available for: Mac Studio (2022), Mac Pro (2019 and later), MacBook
Air (2018 and later), MacBook Pro (2017 and later), Mac mini (2018
and later), iMac (2017 and later), MacBook (2017), and iMac Pro
(2017)
Impact: Processing a maliciously crafted image may lead to arbitrary
code execution
Description: A memory corruption issue existed in the processing of
ICC profiles. This issue was addressed with improved input
validation.
CVE-2022-26730: David Hoyt of Hoyt LLC

Crash Reporter
Available for: Mac Studio (2022), Mac Pro (2019 and later), MacBook
Air (2018 and later), MacBook Pro (2017 and later), Mac mini (2018
and later), iMac (2017 and later), MacBook (2017), and iMac Pro
(2017)
Impact: A user with physical access to an iOS device may be able to
read past diagnostic logs
Descript...