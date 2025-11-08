---
title: APPLE-SA-11-03-2025-3 macOS Sequoia 15.7.2
url: https://seclists.org/fulldisclosure/2025/Nov/4
source: Full Disclosure
date: 2025-11-07
fetch_date: 2025-11-08T03:06:39.192991
---

# APPLE-SA-11-03-2025-3 macOS Sequoia 15.7.2

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

[![Previous](/images/left-icon-16x16.png)](3)
[By Date](date.html#4)
[![Next](/images/right-icon-16x16.png)](5)

[![Previous](/images/left-icon-16x16.png)](3)
[By Thread](index.html#4)
[![Next](/images/right-icon-16x16.png)](5)

![](/shared/images/nst-icons.svg#search)

# APPLE-SA-11-03-2025-3 macOS Sequoia 15.7.2

---

*From*: Apple Product Security via Fulldisclosure <fulldisclosure () seclists org>
*Date*: Mon, 03 Nov 2025 17:31:26 -0800

---

```
-----BEGIN PGP SIGNED MESSAGE-----
Hash: SHA256

APPLE-SA-11-03-2025-3 macOS Sequoia 15.7.2

macOS Sequoia 15.7.2 addresses the following issues.
Information about the security content is also available at
https://support.apple.com/125635.

Apple maintains a Security Releases page at
https://support.apple.com/100100 which lists recent
software updates with security advisories.

Admin Framework
Available for: macOS Sequoia
Impact: An app may be able to access user-sensitive data
Description: A logic issue was addressed with improved checks.
CVE-2025-43322: Ryan Dowd (@_rdowd)

AppleMobileFileIntegrity
Available for: macOS Sequoia
Impact: An app may be able to access sensitive user data
Description: An access issue was addressed with additional sandbox
restrictions.
CVE-2025-43337: Csaba Fitzl (@theevilbit) and Nolan Astrein of Kandji

AppleMobileFileIntegrity
Available for: macOS Sequoia
Impact: An app may be able to access user-sensitive data
Description: A downgrade issue affecting Intel-based Mac computers was
addressed with additional code-signing restrictions.
CVE-2025-43390: Mickey Jin (@patch1t)

AppleMobileFileIntegrity
Available for: macOS Sequoia
Impact: An app may be able to access sensitive user data
Description: A downgrade issue affecting Intel-based Mac computers was
addressed with additional code-signing restrictions.
CVE-2025-43468: Mickey Jin (@patch1t)

AppleMobileFileIntegrity
Available for: macOS Sequoia
Impact: An app may be able to access protected user data
Description: This issue was addressed with improved validation of
symlinks.
CVE-2025-43379: Gergely Kalman (@gergely_kalman)

AppleMobileFileIntegrity
Available for: macOS Sequoia
Impact: An app may be able to access sensitive user data
Description: A permissions issue was addressed with additional
restrictions.
CVE-2025-43469: Mickey Jin (@patch1t)
CVE-2025-43378: an anonymous researcher

ASP TCP
Available for: macOS Sequoia
Impact: An app may be able to cause unexpected system termination
Description: A use after free issue was addressed with improved memory
management.
CVE-2025-43478: Joseph Ravichandran (@0xjprx) of MIT CSAIL, Dave G.
(supernetworks.org)

Assets
Available for: macOS Sequoia
Impact: An app may be able to break out of its sandbox
Description: This issue was addressed with improved entitlements.
CVE-2025-43407: JZ

Assets
Available for: macOS Sequoia
Impact: An app may be able to modify protected parts of the file system
Description: This issue was addressed with improved validation of
symlinks.
CVE-2025-43446: Zhongcheng Li from IES Red Team of ByteDance

Audio
Available for: macOS Sequoia
Impact: A malicious app may be able to read kernel memory
Description: An out-of-bounds read was addressed with improved bounds
checking.
CVE-2025-43361: Michael Reeves (@IntegralPilot)

Audio
Available for: macOS Sequoia
Impact: An attacker with physical access to an unlocked device paired
with a Mac may be able to view sensitive user information in system
logging
Description: A logging issue was addressed with improved data redaction.
CVE-2025-43423: Duy Trần (@khanhduytran0)

bash
Available for: macOS Sequoia
Impact: An app may be able to gain root privileges
Description: A validation issue was addressed with improved input
sanitization.
CVE-2025-43472: Morris Richman (@morrisinlife)

bootp
Available for: macOS Sequoia
Impact: An app may be able to access protected user data
Description: This issue was addressed with improved handling of
symlinks.
CVE-2025-43394: Csaba Fitzl (@theevilbit) of Kandji

CloudKit
Available for: macOS Sequoia
Impact: An app may be able to break out of its sandbox
Description: This issue was addressed with improved validation of
symlinks.
CVE-2025-43448: Hikerell (Loadshine Lab)

configd
Available for: macOS Sequoia
Impact: An app may be able to access protected user data
Description: This issue was addressed with improved handling of
symlinks.
CVE-2025-43395: Csaba Fitzl (@theevilbit) of Kandji

CoreAnimation
Available for: macOS Sequoia
Impact: A remote attacker may be able to cause a denial-of-service
Description: A denial-of-service issue was addressed with improved
validation.
CVE-2025-43401: 이동하 (Lee Dong Ha of BoB 14th), wac working with Trend
Micro Zero Day Initiative

CoreMedia
Available for: macOS Sequoia
Impact: An app may be able to access sensitive user data
Description: A race condition was addressed with improved state
handling.
CVE-2025-43292: Csaba Fitzl (@theevilbit) and Nolan Astrein of Kandji

CoreServices
Available for: macOS Sequoia
Impact: An app may be able to access sensitive user data
Description: A permissions issue was addressed with additional
restrictions.
CVE-2025-43479: an anonymous researcher

CoreServices
Available for: macOS Sequoia
Impact: An app may be able to access sensitive user data
Description: A parsing issue in the handling of directory paths was
addressed with improved path validation.
CVE-2025-43382: Gergely Kalman (@gergely_kalman)

CoreText
Available for: macOS Sequoia
Impact: Processing a maliciously crafted media file may lead to
unexpected app termination or corrupt process memory
Description: An out-of-bounds read was addressed with improved input
validation.
CVE-2025-43445: Hossein Lotfi (@hosselot) of Trend Micro Zero Day
Initiative

Disk Images
Available for: macOS Sequoia
Impact: An app may be able to break out of its sandbox
Description: This issue was addressed with improved checks.
CVE-2025-43481: Mickey Jin (@patch1t), Kenneth Chew, an anonymous
researcher, Adwiteeya Agrawal

DiskArbitration
Available for: macOS Sequoia
Impact: A malicious app may be able to gain root privileges
Description: A permissions issue was addressed with additional
restrictions.
CVE-2025-43387: an anonymous researcher

Dock
Available for: macOS Sequoia
Impact: An app may be able to access sensitive user data
Description: A race condition was addressed with improved state
handling.
CVE-2025-43420: Rodolphe BRUNETTI (@eisw0lf) of Lupus Nova

FileProvider
Available for: macOS Sequoia
Impact: An app may be able to access sensitive user data
Description: An authorization issue was addressed with improved state
management.
CVE-2025-43498: pattern-f (@pattern_F_)

Finder
Available for: macOS Sequoia
Impact: An app may bypass Gatekeeper checks
Description: A logic issue was addressed with improved validation.
CVE-2025-43348: Ferdous Saljooki (@malwarezoo) of Jamf

GPU Drivers
Available for: macOS Sequoia
Impact: An app may be able to cause unexpected system termination or
read kernel memory
Description: An out-of-bounds read was addressed with improved input
validation.
CVE-2025-43474: Murray Mike

Installer
Available for: macOS Sequoia
Impact: A sandboxed app may be able to access sensitive user data
Description: A logic issue was addressed with improved checks.
CVE-2025-43396: an anonymous researcher

Kernel
Available for: macOS Sequoia
Impact: An app may be able to cause unexpected system termination
Description: The issue was addressed with improved memory handling.
CVE-2025-43398:...