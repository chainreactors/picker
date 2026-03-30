---
title: APPLE-SA-03-24-2026-3 macOS Tahoe 26.4
url: https://seclists.org/fulldisclosure/2026/Mar/18
source: Full Disclosure
date: 2026-03-29
fetch_date: 2026-03-30T04:46:58.770224
---

# APPLE-SA-03-24-2026-3 macOS Tahoe 26.4

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

[![Previous](/images/left-icon-16x16.png)](17)
[By Date](date.html#18)
[![Next](/images/right-icon-16x16.png)](19)

[![Previous](/images/left-icon-16x16.png)](17)
[By Thread](index.html#18)
[![Next](/images/right-icon-16x16.png)](19)

![](/shared/images/nst-icons.svg#search)

# APPLE-SA-03-24-2026-3 macOS Tahoe 26.4

---

*From*: Apple Product Security via Fulldisclosure <fulldisclosure () seclists org>
*Date*: Tue, 24 Mar 2026 17:01:47 -0700

---

```
-----BEGIN PGP SIGNED MESSAGE-----
Hash: SHA256

APPLE-SA-03-24-2026-3 macOS Tahoe 26.4

macOS Tahoe 26.4 addresses the following issues.
Information about the security content is also available at
https://support.apple.com/126794.

Apple maintains a Security Releases page at
https://support.apple.com/100100 which lists recent
software updates with security advisories.

802.1X
Available for: macOS Tahoe
Impact: An attacker in a privileged network position may be able to
intercept network traffic
Description: An authentication issue was addressed with improved state
management.
CVE-2026-28865: Héloïse Gollier and Mathy Vanhoef (KU Leuven)

Accounts
Available for: macOS Tahoe
Impact: An app may be able to access sensitive user data
Description: An authorization issue was addressed with improved state
management.
CVE-2026-28877: Rosyna Keller of Totally Not Malicious Software

Admin Framework
Available for: macOS Tahoe
Impact: An app with root privileges may be able to delete protected
system files
Description: A path handling issue was addressed with improved
validation.
CVE-2026-28823: Ryan Dowd (@_rdowd)

apache
Available for: macOS Tahoe
Impact: Multiple issues in Apache
Description: This is a vulnerability in open source code and Apple
Software is among the affected projects. The CVE-ID was assigned by a
third party. Learn more about the issue and CVE-ID at cve.org.
CVE-2025-55753
CVE-2025-58098
CVE-2025-59775
CVE-2025-65082
CVE-2025-66200

AppleMobileFileIntegrity
Available for: macOS Tahoe
Impact: An app may be able to access sensitive user data
Description: An authorization issue was addressed with improved state
management.
CVE-2026-28824: Mickey Jin (@patch1t)

AppleMobileFileIntegrity
Available for: macOS Tahoe
Impact: An app may be able to access user-sensitive data
Description: A downgrade issue affecting Intel-based Mac computers was
addressed with additional code-signing restrictions.
CVE-2026-20699: Mickey Jin (@patch1t)

AppleScript
Available for: macOS Tahoe
Impact: An app may bypass Gatekeeper checks
Description: A permissions issue was addressed with additional
restrictions.
CVE-2026-20684: Koh M. Nakagawa (@tsunek0h) of FFRI Security, Inc.

Archive Utility
Available for: macOS Tahoe
Impact: An app may be able to access user-sensitive data
Description: This issue was addressed with improved handling of
symlinks.
CVE-2026-20633: Mickey Jin (@patch1t)

Audio
Available for: macOS Tahoe
Impact: Processing maliciously crafted web content may lead to an
unexpected process crash
Description: A use-after-free issue was addressed with improved memory
management.
CVE-2026-28879: Justin Cohen of Google

Audio
Available for: macOS Tahoe
Impact: An attacker may be able to cause unexpected app termination
Description: A type confusion issue was addressed with improved memory
handling.
CVE-2026-28822: Jex Amro

Calling Framework
Available for: macOS Tahoe
Impact: A remote attacker may be able to cause a denial-of-service
Description: A denial-of-service issue was addressed with improved input
validation.
CVE-2026-28894: an anonymous researcher

Clipboard
Available for: macOS Tahoe
Impact: An app may be able to access sensitive user data
Description: This issue was addressed with improved validation of
symlinks.
CVE-2026-28866: Cristian Dinca (icmd.tech)

CoreMedia
Available for: macOS Tahoe
Impact: Processing an audio stream in a maliciously crafted media file
may terminate the process
Description: An out-of-bounds access issue was addressed with improved
bounds checking.
CVE-2026-20690: Hossein Lotfi (@hosselot) of Trend Micro Zero Day
Initiative

CoreServices
Available for: macOS Tahoe
Impact: An app may be able to gain elevated privileges
Description: A validation issue existed in the entitlement verification.
This issue was addressed with improved validation of the process
entitlement.
CVE-2026-28821: YingQi Shi (@Mas0nShi) of DBAppSecurity's WeBin lab

CoreServices
Available for: macOS Tahoe
Impact: An app may be able to break out of its sandbox
Description: A permissions issue was addressed with additional sandbox
restrictions.
CVE-2026-28838: an anonymous researcher

CoreUtils
Available for: macOS Tahoe
Impact: A user in a privileged network position may be able to cause a
denial-of-service
Description: A null pointer dereference was addressed with improved
input validation.
CVE-2026-28886: Etienne Charron (Renault) and Victoria Martini (Renault)

Crash Reporter
Available for: macOS Tahoe
Impact: An app may be able to enumerate a user's installed apps
Description: A privacy issue was addressed by removing sensitive data.
CVE-2026-28878: Zhongcheng Li from IES Red Team

CUPS
Available for: macOS Tahoe
Impact: An app may be able to gain root privileges
Description: A race condition was addressed with improved state
handling.
CVE-2026-28888: Andreas Jaegersberger & Ro Achterberg of Nosebeard Labs

CUPS
Available for: macOS Tahoe
Impact: A document may be written to a temporary file when using print
preview
Description: A privacy issue was addressed with improved handling of
temporary files.
CVE-2026-28893: Asaf Cohen

curl
Available for: macOS Tahoe
Impact: An issue existed in curl which may result in unintentionally
sending sensitive information via an incorrect connection
Description: This is a vulnerability in open source code and Apple
Software is among the affected projects. The CVE-ID was assigned by a
third party. Learn more about the issue and CVE-ID at cve.org.
CVE-2025-14524

DeviceLink
Available for: macOS Tahoe
Impact: An app may be able to access sensitive user data
Description: A parsing issue in the handling of directory paths was
addressed with improved path validation.
CVE-2026-28876: Andreas Jaegersberger & Ro Achterberg of Nosebeard Labs

Diagnostics
Available for: macOS Tahoe
Impact: An app may be able to modify protected parts of the file system
Description: A permissions issue was addressed by removing the
vulnerable code.
CVE-2026-28892: 风沐云烟 (@binary_fmyy) and Minghao Lin (@Y1nKoc)

File System
Available for: macOS Tahoe
Impact: An app may be able to disclose kernel memory
Description: An out-of-bounds read was addressed with improved bounds
checking.
CVE-2026-28832: DARKNAVY (@DarkNavyOrg)

GeoServices
Available for: macOS Tahoe
Impact: An app may be able to access sensitive user data
Description: An information leakage was addressed with additional
validation.
CVE-2026-28870: XiguaSec

GPU Drivers
Available for: macOS Tahoe
Impact: An app may be able to cause unexpected system termination
Description: A race condition was addressed with improved state
handling.
CVE-2026-28834: an anonymous researcher

iCloud
Available for: macOS Tahoe
Impact: An app may be able to access sensitive user data
Description: A privacy issue was addressed by moving sensitive data.
CVE-2026-28881: Ye Zhang of Baidu Security, Ryan Dowd (@_rdowd), Csaba
Fitzl (@theevilbit) of Iru

iCloud
Available for: macOS Tahoe
Impact: An app may be able to enumerate a user's installed apps
Description: A permissions issue was...