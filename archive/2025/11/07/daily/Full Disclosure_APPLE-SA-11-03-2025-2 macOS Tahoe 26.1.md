---
title: APPLE-SA-11-03-2025-2 macOS Tahoe 26.1
url: https://seclists.org/fulldisclosure/2025/Nov/3
source: Full Disclosure
date: 2025-11-07
fetch_date: 2025-11-08T03:06:39.504798
---

# APPLE-SA-11-03-2025-2 macOS Tahoe 26.1

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

[![Previous](/images/left-icon-16x16.png)](2)
[By Date](date.html#3)
[![Next](/images/right-icon-16x16.png)](4)

[![Previous](/images/left-icon-16x16.png)](2)
[By Thread](index.html#3)
[![Next](/images/right-icon-16x16.png)](4)

![](/shared/images/nst-icons.svg#search)

# APPLE-SA-11-03-2025-2 macOS Tahoe 26.1

---

*From*: Apple Product Security via Fulldisclosure <fulldisclosure () seclists org>
*Date*: Mon, 03 Nov 2025 17:30:57 -0800

---

```
-----BEGIN PGP SIGNED MESSAGE-----
Hash: SHA256

APPLE-SA-11-03-2025-2 macOS Tahoe 26.1

macOS Tahoe 26.1 addresses the following issues.
Information about the security content is also available at
https://support.apple.com/125634.

Apple maintains a Security Releases page at
https://support.apple.com/100100 which lists recent
software updates with security advisories.

Admin Framework
Available for: macOS Tahoe
Impact: An app may be able to access sensitive user data
Description: The issue was addressed with improved checks.
CVE-2025-43471: Gergely Kalman (@gergely_kalman)

Admin Framework
Available for: macOS Tahoe
Impact: An app may be able to access user-sensitive data
Description: A logic issue was addressed with improved checks.
CVE-2025-43322: Ryan Dowd (@_rdowd)

Apple Account
Available for: macOS Tahoe
Impact: A malicious app may be able to take a screenshot of sensitive
information in embedded views
Description: A privacy issue was addressed with improved checks.
CVE-2025-43455: Ron Masas of BreakPoint.SH, Pinak Oza

Apple Neural Engine
Available for: macOS Tahoe
Impact: An app may be able to cause unexpected system termination or
corrupt kernel memory
Description: The issue was addressed with improved memory handling.
CVE-2025-43447: an anonymous researcher
CVE-2025-43462: an anonymous researcher

AppleMobileFileIntegrity
Available for: macOS Tahoe
Impact: An app may be able to access user-sensitive data
Description: A downgrade issue affecting Intel-based Mac computers was
addressed with additional code-signing restrictions.
CVE-2025-43390: Mickey Jin (@patch1t)

AppleMobileFileIntegrity
Available for: macOS Tahoe
Impact: An app may be able to access sensitive user data
Description: An injection issue was addressed with improved validation.
CVE-2025-43388: Mickey Jin (@patch1t)
CVE-2025-43466: Mickey Jin (@patch1t)

AppleMobileFileIntegrity
Available for: macOS Tahoe
Impact: An app may be able to access sensitive user data
Description: A parsing issue in the handling of directory paths was
addressed with improved path validation.
CVE-2025-43382: Gergely Kalman (@gergely_kalman)

AppleMobileFileIntegrity
Available for: macOS Tahoe
Impact: An app may be able to access sensitive user data
Description: A downgrade issue affecting Intel-based Mac computers was
addressed with additional code-signing restrictions.
CVE-2025-43468: Mickey Jin (@patch1t)

AppleMobileFileIntegrity
Available for: macOS Tahoe
Impact: An app may be able to access protected user data
Description: This issue was addressed with improved validation of
symlinks.
CVE-2025-43379: Gergely Kalman (@gergely_kalman)

AppleMobileFileIntegrity
Available for: macOS Tahoe
Impact: An app may be able to access sensitive user data
Description: A permissions issue was addressed with additional
restrictions.
CVE-2025-43378: an anonymous researcher

ASP TCP
Available for: macOS Tahoe
Impact: An app may be able to cause unexpected system termination
Description: A use after free issue was addressed with improved memory
management.
CVE-2025-43478: Joseph Ravichandran (@0xjprx) of MIT CSAIL, Dave G.
(supernetworks.org)

Assets
Available for: macOS Tahoe
Impact: An app may be able to break out of its sandbox
Description: This issue was addressed with improved entitlements.
CVE-2025-43407: JZ

Assets
Available for: macOS Tahoe
Impact: An app may be able to modify protected parts of the file system
Description: This issue was addressed with improved validation of
symlinks.
CVE-2025-43446: Zhongcheng Li from IES Red Team of ByteDance

ATS
Available for: macOS Tahoe
Impact: An app may be able to access sensitive user data
Description: A parsing issue in the handling of directory paths was
addressed with improved path validation.
CVE-2025-43465: an anonymous researcher

Audio
Available for: macOS Tahoe
Impact: An attacker with physical access to an unlocked device paired
with a Mac may be able to view sensitive user information in system
logging
Description: A logging issue was addressed with improved data redaction.
CVE-2025-43423: Duy Trần (@khanhduytran0)

BackBoardServices
Available for: macOS Tahoe
Impact: An app may be able to break out of its sandbox
Description: An access issue was addressed with additional sandbox
restrictions.
CVE-2025-43497: an anonymous researcher

bootp
Available for: macOS Tahoe
Impact: An app may be able to access protected user data
Description: This issue was addressed with improved handling of
symlinks.
CVE-2025-43394: Csaba Fitzl (@theevilbit) of Kandji

CloudKit
Available for: macOS Tahoe
Impact: An app may be able to break out of its sandbox
Description: This issue was addressed with improved validation of
symlinks.
CVE-2025-43448: Hikerell (Loadshine Lab)

configd
Available for: macOS Tahoe
Impact: An app may be able to access protected user data
Description: This issue was addressed with improved handling of
symlinks.
CVE-2025-43395: Csaba Fitzl (@theevilbit) of Kandji

configd
Available for: macOS Tahoe
Impact: An app may be able to access protected user data
Description: This issue was addressed with improved validation of
symlinks.
CVE-2025-43461: Csaba Fitzl (@theevilbit) of Kandji

Contacts
Available for: macOS Tahoe
Impact: An app may be able to access sensitive user data
Description: A logging issue was addressed with improved data redaction.
CVE-2025-43426: Wojciech Regula of SecuRing (wojciechregula.blog)

CoreAnimation
Available for: macOS Tahoe
Impact: A remote attacker may be able to cause a denial-of-service
Description: A denial-of-service issue was addressed with improved
validation.
CVE-2025-43401: 이동하 (Lee Dong Ha of BoB 14th), wac working with Trend
Micro Zero Day Initiative

CoreServices
Available for: macOS Tahoe
Impact: An app may be able to access sensitive user data
Description: A permissions issue was addressed with additional
restrictions.
CVE-2025-43479: an anonymous researcher

CoreServices
Available for: macOS Tahoe
Impact: An app may be able to enumerate a user's installed apps
Description: A permissions issue was addressed with additional
restrictions.
CVE-2025-43436: Zhongcheng Li from IES Red Team of ByteDance

CoreServicesUIAgent
Available for: macOS Tahoe
Impact: A malicious app may be able to delete protected user data
Description: This issue was addressed with improved handling of
symlinks.
CVE-2025-43381: Mickey Jin (@patch1t)

CoreText
Available for: macOS Tahoe
Impact: Processing a maliciously crafted media file may lead to
unexpected app termination or corrupt process memory
Description: An out-of-bounds read was addressed with improved input
validation.
CVE-2025-43445: Hossein Lotfi (@hosselot) of Trend Micro Zero Day
Initiative

Disk Images
Available for: macOS Tahoe
Impact: An app may be able to break out of its sandbox
Description: This issue was addressed with improved checks.
CVE-2025-43481: Adwiteeya Agrawal, Mickey Jin (@patch1t), Kenneth Chew,
an anonymous researcher

DiskArbitration
Available for: macOS Tahoe
Impact: A malicious app may be able to gain root privileges
Description: A p...