---
title: APPLE-SA-07-29-2025-5 macOS Ventura 13.7.7
url: https://seclists.org/fulldisclosure/2025/Jul/34
source: Full Disclosure
date: 2025-07-31
fetch_date: 2025-10-06T23:56:38.927389
---

# APPLE-SA-07-29-2025-5 macOS Ventura 13.7.7

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

[![Previous](/images/left-icon-16x16.png)](33)
[By Date](date.html#34)
[![Next](/images/right-icon-16x16.png)](35)

[![Previous](/images/left-icon-16x16.png)](33)
[By Thread](index.html#34)
[![Next](/images/right-icon-16x16.png)](35)

![](/shared/images/nst-icons.svg#search)

# APPLE-SA-07-29-2025-5 macOS Ventura 13.7.7

---

*From*: Apple Product Security via Fulldisclosure <fulldisclosure () seclists org>
*Date*: Tue, 29 Jul 2025 16:29:42 -0700

---

```
-----BEGIN PGP SIGNED MESSAGE-----
Hash: SHA256

APPLE-SA-07-29-2025-5 macOS Ventura 13.7.7

macOS Ventura 13.7.7 addresses the following issues.
Information about the security content is also available at
https://support.apple.com/124151.

Apple maintains a Security Releases page at
https://support.apple.com/100100 which lists recent
software updates with security advisories.

Admin Framework
Available for: macOS Ventura
Impact: An app may be able to cause a denial-of-service
Description: A path handling issue was addressed with improved
validation.
CVE-2025-43191: Ryan Dowd (@_rdowd)

afclip
Available for: macOS Ventura
Impact: Parsing a file may lead to an unexpected app termination
Description: The issue was addressed with improved memory handling.
CVE-2025-43186: Hossein Lotfi (@hosselot) of Trend Micro Zero Day
Initiative

AMD
Available for: macOS Ventura
Impact: An app may be able to cause unexpected system termination
Description: A race condition was addressed with improved state
handling.
CVE-2025-43244: ABC Research s.r.o.

AppleMobileFileIntegrity
Available for: macOS Ventura
Impact: An app may be able to gain root privileges
Description: A permissions issue was addressed with additional
restrictions.
CVE-2025-31243: Mickey Jin (@patch1t)

AppleMobileFileIntegrity
Available for: macOS Ventura
Impact: An app may be able to gain root privileges
Description: A logic issue was addressed with improved checks.
CVE-2025-43249: Mickey Jin (@patch1t)

AppleMobileFileIntegrity
Available for: macOS Ventura
Impact: An app may be able to access protected user data
Description: A downgrade issue was addressed with additional code-
signing restrictions.
CVE-2025-43245: Mickey Jin (@patch1t)

CFNetwork
Available for: macOS Ventura
Impact: An attacker may be able to cause unexpected app termination
Description: A use-after-free issue was addressed by removing the
vulnerable code.
CVE-2025-43222: Andreas Jaegersberger & Ro Achterberg of Nosebeard Labs

CFNetwork
Available for: macOS Ventura
Impact: A non-privileged user may be able to modify restricted network
settings
Description: A denial-of-service issue was addressed with improved input
validation.
CVE-2025-43223: Andreas Jaegersberger & Ro Achterberg of Nosebeard Labs

copyfile
Available for: macOS Ventura
Impact: An app may be able to access protected user data
Description: This issue was addressed with improved validation of
symlinks.
CVE-2025-43220: Mickey Jin (@patch1t)

Core Services
Available for: macOS Ventura
Impact: A malicious app may be able to gain root privileges
Description: A permissions issue was addressed by removing the
vulnerable code.
CVE-2025-43199: Gergely Kalman (@gergely_kalman), an anonymous
researcher

CoreMedia
Available for: macOS Ventura
Impact: Processing a maliciously crafted media file may lead to
unexpected app termination or corrupt process memory
Description: An out-of-bounds access issue was addressed with improved
bounds checking.
CVE-2025-43210: Hossein Lotfi (@hosselot) of Trend Micro Zero Day
Initiative

CoreServices
Available for: macOS Ventura
Impact: An app may be able to access sensitive user data
Description: An issue existed in the handling of environment variables.
This issue was addressed with improved validation.
CVE-2025-43195: 风沐云烟 (@binary_fmyy) and Minghao Lin (@Y1nKoc)

Disk Images
Available for: macOS Ventura
Impact: Running an hdiutil command may unexpectedly execute arbitrary
code
Description: This issue was addressed by removing the vulnerable code.
CVE-2025-43187: 风沐云烟 (@binary_fmyy) and Minghao Lin (@Y1nKoc)

file
Available for: macOS Ventura
Impact: Processing a maliciously crafted file may lead to unexpected app
termination
Description: An out-of-bounds read was addressed with improved input
validation.
CVE-2025-43254: 2ourc3 | Salim Largo

File Bookmark
Available for: macOS Ventura
Impact: An app may be able to break out of its sandbox
Description: A logic issue was addressed with improved checks.
CVE-2025-43261: an anonymous researcher

Find My
Available for: macOS Ventura
Impact: An app may be able to fingerprint the user
Description: A permissions issue was addressed with additional
restrictions.
CVE-2025-31279: Dawuge of Shuffle Team

Finder
Available for: macOS Ventura
Impact: An app may be able to execute arbitrary code out of its sandbox
or with certain elevated privileges
Description: This issue was addressed through improved state management.
CVE-2025-24119: an anonymous researcher

GPU Drivers
Available for: macOS Ventura
Impact: An app may be able to cause unexpected system termination
Description: An out-of-bounds read was addressed with improved bounds
checking.
CVE-2025-43255: Anonymous working with Trend Micro Zero Day Initiative

ICU
Available for: macOS Ventura
Impact: Processing maliciously crafted web content may lead to an
unexpected Safari crash
Description: An out-of-bounds access issue was addressed with improved
bounds checking.
CVE-2025-43209: Gary Kwong working with Trend Micro Zero Day Initiative

Kernel
Available for: macOS Ventura
Impact: A remote attacker may be able to cause unexpected system
termination
Description: The issue was addressed with improved checks.
CVE-2025-24224: Tony Iskow (@Tybbow)

LaunchServices
Available for: macOS Ventura
Impact: An app may be able to execute arbitrary code out of its sandbox
or with certain elevated privileges
Description: This issue was addressed through improved state management.
CVE-2025-24119: an anonymous researcher

libxpc
Available for: macOS Ventura
Impact: An app may be able to gain root privileges
Description: A path handling issue was addressed with improved
validation.
CVE-2025-43196: an anonymous researcher

NetAuth
Available for: macOS Ventura
Impact: An app may be able to break out of its sandbox
Description: A race condition was addressed with additional validation.
CVE-2025-43275: Csaba Fitzl (@theevilbit) of Kandji

Notes
Available for: macOS Ventura
Impact: An app may gain unauthorized access to Local Network
Description: An access issue was addressed with additional sandbox
restrictions.
CVE-2025-43270: Minqiang Gui

Notes
Available for: macOS Ventura
Impact: An app may be able to access sensitive user data
Description: A logging issue was addressed with improved data redaction.
CVE-2025-43225: Kirin (@Pwnrin)

NSSpellChecker
Available for: macOS Ventura
Impact: An app may be able to break out of its sandbox
Description: A permissions issue was addressed with additional
restrictions.
CVE-2025-43266: Noah Gregory (wts.dev)

PackageKit
Available for: macOS Ventura
Impact: A malicious app with root privileges may be able to modify the
contents of system files
Description: A permissions issue was addressed with additional
restrictions.
CVE-2025-43247: Mickey Jin (@patch1t)

PackageKit
Available for: macOS Ventura
Impact: An app may be able to modify protected parts of the file system
Description: The issue was addressed with improved checks.
CVE-2025-43194: Mickey Jin (@patch1t)

PackageKit
Available for: macOS Ventura
...