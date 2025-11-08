---
title: APPLE-SA-11-03-2025-4 macOS Sonoma 14.8.2
url: https://seclists.org/fulldisclosure/2025/Nov/5
source: Full Disclosure
date: 2025-11-07
fetch_date: 2025-11-08T03:06:38.881163
---

# APPLE-SA-11-03-2025-4 macOS Sonoma 14.8.2

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

[![Previous](/images/left-icon-16x16.png)](4)
[By Date](date.html#5)
[![Next](/images/right-icon-16x16.png)](6)

[![Previous](/images/left-icon-16x16.png)](4)
[By Thread](index.html#5)
[![Next](/images/right-icon-16x16.png)](6)

![](/shared/images/nst-icons.svg#search)

# APPLE-SA-11-03-2025-4 macOS Sonoma 14.8.2

---

*From*: Apple Product Security via Fulldisclosure <fulldisclosure () seclists org>
*Date*: Mon, 03 Nov 2025 17:32:07 -0800

---

```
-----BEGIN PGP SIGNED MESSAGE-----
Hash: SHA256

APPLE-SA-11-03-2025-4 macOS Sonoma 14.8.2

macOS Sonoma 14.8.2 addresses the following issues.
Information about the security content is also available at
https://support.apple.com/125636.

Apple maintains a Security Releases page at
https://support.apple.com/100100 which lists recent
software updates with security advisories.

Admin Framework
Available for: macOS Sonoma
Impact: An app may be able to access user-sensitive data
Description: A logic issue was addressed with improved checks.
CVE-2025-43322: Ryan Dowd (@_rdowd)

AppleMobileFileIntegrity
Available for: macOS Sonoma
Impact: An app may be able to access sensitive user data
Description: A downgrade issue affecting Intel-based Mac computers was
addressed with additional code-signing restrictions.
CVE-2025-43468: Mickey Jin (@patch1t)

AppleMobileFileIntegrity
Available for: macOS Sonoma
Impact: An app may be able to access protected user data
Description: This issue was addressed with improved validation of
symlinks.
CVE-2025-43379: Gergely Kalman (@gergely_kalman)

AppleMobileFileIntegrity
Available for: macOS Sonoma
Impact: An app may be able to access sensitive user data
Description: A permissions issue was addressed with additional
restrictions.
CVE-2025-43469: Mickey Jin (@patch1t)

ASP TCP
Available for: macOS Sonoma
Impact: An app may be able to cause unexpected system termination
Description: A use after free issue was addressed with improved memory
management.
CVE-2025-43478: Joseph Ravichandran (@0xjprx) of MIT CSAIL, Dave G.
(supernetworks.org)

Assets
Available for: macOS Sonoma
Impact: An app may be able to break out of its sandbox
Description: This issue was addressed with improved entitlements.
CVE-2025-43407: JZ

Assets
Available for: macOS Sonoma
Impact: An app may be able to modify protected parts of the file system
Description: This issue was addressed with improved validation of
symlinks.
CVE-2025-43446: Zhongcheng Li from IES Red Team of ByteDance

Audio
Available for: macOS Sonoma
Impact: A malicious app may be able to read kernel memory
Description: An out-of-bounds read was addressed with improved bounds
checking.
CVE-2025-43361: Michael Reeves (@IntegralPilot)

bash
Available for: macOS Sonoma
Impact: An app may be able to gain root privileges
Description: A validation issue was addressed with improved input
sanitization.
CVE-2025-43472: Morris Richman (@morrisinlife)

bootp
Available for: macOS Sonoma
Impact: An app may be able to access protected user data
Description: This issue was addressed with improved handling of
symlinks.
CVE-2025-43394: Csaba Fitzl (@theevilbit) of Kandji

CloudKit
Available for: macOS Sonoma
Impact: An app may be able to break out of its sandbox
Description: This issue was addressed with improved validation of
symlinks.
CVE-2025-43448: Hikerell (Loadshine Lab)

configd
Available for: macOS Sonoma
Impact: An app may be able to access protected user data
Description: This issue was addressed with improved handling of
symlinks.
CVE-2025-43395: Csaba Fitzl (@theevilbit) of Kandji

CoreAnimation
Available for: macOS Sonoma
Impact: A remote attacker may be able to cause a denial-of-service
Description: A denial-of-service issue was addressed with improved
validation.
CVE-2025-43401: 이동하 (Lee Dong Ha of BoB 14th), wac working with Trend
Micro Zero Day Initiative

CoreServices
Available for: macOS Sonoma
Impact: An app may be able to access sensitive user data
Description: A permissions issue was addressed with additional
restrictions.
CVE-2025-43479: an anonymous researcher

CoreServices
Available for: macOS Sonoma
Impact: An app may be able to access sensitive user data
Description: A parsing issue in the handling of directory paths was
addressed with improved path validation.
CVE-2025-43382: Gergely Kalman (@gergely_kalman)

CoreText
Available for: macOS Sonoma
Impact: Processing a maliciously crafted media file may lead to
unexpected app termination or corrupt process memory
Description: An out-of-bounds read was addressed with improved input
validation.
CVE-2025-43445: Hossein Lotfi (@hosselot) of Trend Micro Zero Day
Initiative

Dock
Available for: macOS Sonoma
Impact: An app may be able to access sensitive user data
Description: A race condition was addressed with improved state
handling.
CVE-2025-43420: Rodolphe BRUNETTI (@eisw0lf) of Lupus Nova

FileProvider
Available for: macOS Sonoma
Impact: An app may be able to access sensitive user data
Description: An authorization issue was addressed with improved state
management.
CVE-2025-43498: pattern-f (@pattern_F_)

Finder
Available for: macOS Sonoma
Impact: An app may bypass Gatekeeper checks
Description: A logic issue was addressed with improved validation.
CVE-2025-43348: Ferdous Saljooki (@malwarezoo) of Jamf

GPU Drivers
Available for: macOS Sonoma
Impact: An app may be able to cause unexpected system termination or
read kernel memory
Description: An out-of-bounds read was addressed with improved input
validation.
CVE-2025-43474: Murray Mike

ImageIO
Available for: macOS Sonoma
Impact: Processing a maliciously crafted media file may lead to
unexpected app termination or corrupt process memory
Description: The issue was addressed with improved input validation.
CVE-2025-43372: 이동하 (Lee Dong Ha) of SSA Lab

ImageIO
Available for: macOS Sonoma
Impact: Processing a maliciously crafted media file may lead to
unexpected app termination or corrupt process memory
Description: An out-of-bounds access issue was addressed with improved
bounds checking.
CVE-2025-43338: 이동하 (Lee Dong Ha) of SSA Lab

Installer
Available for: macOS Sonoma
Impact: A sandboxed app may be able to access sensitive user data
Description: A logic issue was addressed with improved checks.
CVE-2025-43396: an anonymous researcher

Kernel
Available for: macOS Sonoma
Impact: An app may be able to cause unexpected system termination
Description: The issue was addressed with improved memory handling.
CVE-2025-43398: Cristian Dinca (icmd.tech)

libxpc
Available for: macOS Sonoma
Impact: A sandboxed app may be able to observe system-wide network
connections
Description: An access issue was addressed with additional sandbox
restrictions.
CVE-2025-43413: Dave G. and Alex Radocea of supernetworks.org

Notes
Available for: macOS Sonoma
Impact: An app may be able to access sensitive user data
Description: A privacy issue was addressed by removing the vulnerable
code.
CVE-2025-43389: Kirin (@Pwnrin)

NSSpellChecker
Available for: macOS Sonoma
Impact: An app may be able to access sensitive user data
Description: A permissions issue was addressed with additional
restrictions.
CVE-2025-43469: Mickey Jin (@patch1t)

PackageKit
Available for: macOS Sonoma
Impact: An app may be able to access user-sensitive data
Description: This issue was addressed with additional entitlement
checks.
CVE-2025-43411: an anonymous researcher

Photos
Available for: macOS Sonoma
Impact: An app may be able to access user-sensitive data
Description: A permissions issue was addressed with add...