---
title: APPLE-SA-07-29-2025-4 macOS Sonoma 14.7.7
url: https://seclists.org/fulldisclosure/2025/Jul/33
source: Full Disclosure
date: 2025-07-31
fetch_date: 2025-10-06T23:56:41.167340
---

# APPLE-SA-07-29-2025-4 macOS Sonoma 14.7.7

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

[![Previous](/images/left-icon-16x16.png)](32)
[By Date](date.html#33)
[![Next](/images/right-icon-16x16.png)](34)

[![Previous](/images/left-icon-16x16.png)](32)
[By Thread](index.html#33)
[![Next](/images/right-icon-16x16.png)](34)

![](/shared/images/nst-icons.svg#search)

# APPLE-SA-07-29-2025-4 macOS Sonoma 14.7.7

---

*From*: Apple Product Security via Fulldisclosure <fulldisclosure () seclists org>
*Date*: Tue, 29 Jul 2025 16:28:49 -0700

---

```
-----BEGIN PGP SIGNED MESSAGE-----
Hash: SHA256

APPLE-SA-07-29-2025-4 macOS Sonoma 14.7.7

macOS Sonoma 14.7.7 addresses the following issues.
Information about the security content is also available at
https://support.apple.com/124150.

Apple maintains a Security Releases page at
https://support.apple.com/100100 which lists recent
software updates with security advisories.

Admin Framework
Available for: macOS Sonoma
Impact: An app may be able to cause a denial-of-service
Description: A path handling issue was addressed with improved
validation.
CVE-2025-43191: Ryan Dowd (@_rdowd)

afclip
Available for: macOS Sonoma
Impact: Parsing a file may lead to an unexpected app termination
Description: The issue was addressed with improved memory handling.
CVE-2025-43186: Hossein Lotfi (@hosselot) of Trend Micro Zero Day
Initiative

AMD
Available for: macOS Sonoma
Impact: An app may be able to cause unexpected system termination
Description: A race condition was addressed with improved state
handling.
CVE-2025-43244: ABC Research s.r.o.

AppleMobileFileIntegrity
Available for: macOS Sonoma
Impact: An app may be able to gain root privileges
Description: A permissions issue was addressed with additional
restrictions.
CVE-2025-31243: Mickey Jin (@patch1t)

AppleMobileFileIntegrity
Available for: macOS Sonoma
Impact: A malicious app may be able to launch arbitrary binaries on a
trusted device
Description: This issue was addressed with improved input validation.
CVE-2025-43253: Noah Gregory (wts.dev)

AppleMobileFileIntegrity
Available for: macOS Sonoma
Impact: An app may be able to gain root privileges
Description: A logic issue was addressed with improved checks.
CVE-2025-43249: Mickey Jin (@patch1t)

AppleMobileFileIntegrity
Available for: macOS Sonoma
Impact: A malicious app may be able to gain root privileges
Description: A logic issue was addressed with improved restrictions.
CVE-2025-43248: Mickey Jin (@patch1t)

AppleMobileFileIntegrity
Available for: macOS Sonoma
Impact: An app may be able to access protected user data
Description: A downgrade issue was addressed with additional code-
signing restrictions.
CVE-2025-43245: Mickey Jin (@patch1t)

CFNetwork
Available for: macOS Sonoma
Impact: An attacker may be able to cause unexpected app termination
Description: A use-after-free issue was addressed by removing the
vulnerable code.
CVE-2025-43222: Andreas Jaegersberger & Ro Achterberg of Nosebeard Labs

CFNetwork
Available for: macOS Sonoma
Impact: A non-privileged user may be able to modify restricted network
settings
Description: A denial-of-service issue was addressed with improved input
validation.
CVE-2025-43223: Andreas Jaegersberger & Ro Achterberg of Nosebeard Labs

copyfile
Available for: macOS Sonoma
Impact: An app may be able to access protected user data
Description: This issue was addressed with improved validation of
symlinks.
CVE-2025-43220: Mickey Jin (@patch1t)

Core Services
Available for: macOS Sonoma
Impact: A malicious app may be able to gain root privileges
Description: A permissions issue was addressed by removing the
vulnerable code.
CVE-2025-43199: an anonymous researcher, Gergely Kalman
(@gergely_kalman)

CoreMedia
Available for: macOS Sonoma
Impact: Processing a maliciously crafted media file may lead to
unexpected app termination or corrupt process memory
Description: An out-of-bounds access issue was addressed with improved
bounds checking.
CVE-2025-43210: Hossein Lotfi (@hosselot) of Trend Micro Zero Day
Initiative

CoreServices
Available for: macOS Sonoma
Impact: An app may be able to access sensitive user data
Description: An issue existed in the handling of environment variables.
This issue was addressed with improved validation.
CVE-2025-43195: 风沐云烟 (@binary_fmyy) and Minghao Lin (@Y1nKoc)

Disk Images
Available for: macOS Sonoma
Impact: Running an hdiutil command may unexpectedly execute arbitrary
code
Description: This issue was addressed by removing the vulnerable code.
CVE-2025-43187: 风沐云烟 (@binary_fmyy) and Minghao Lin (@Y1nKoc)

Dock
Available for: macOS Sonoma
Impact: An app may be able to access protected user data
Description: This issue was addressed by removing the vulnerable code.
CVE-2025-43198: Mickey Jin (@patch1t)

file
Available for: macOS Sonoma
Impact: Processing a maliciously crafted file may lead to unexpected app
termination
Description: An out-of-bounds read was addressed with improved input
validation.
CVE-2025-43254: 2ourc3 | Salim Largo

File Bookmark
Available for: macOS Sonoma
Impact: An app may be able to break out of its sandbox
Description: A logic issue was addressed with improved checks.
CVE-2025-43261: an anonymous researcher

Find My
Available for: macOS Sonoma
Impact: An app may be able to fingerprint the user
Description: A permissions issue was addressed with additional
restrictions.
CVE-2025-31279: Dawuge of Shuffle Team

Finder
Available for: macOS Sonoma
Impact: An app may be able to execute arbitrary code out of its sandbox
or with certain elevated privileges
Description: This issue was addressed through improved state management.
CVE-2025-24119: an anonymous researcher

GPU Drivers
Available for: macOS Sonoma
Impact: An app may be able to cause unexpected system termination
Description: An out-of-bounds read was addressed with improved bounds
checking.
CVE-2025-43255: Anonymous working with Trend Micro Zero Day Initiative

ICU
Available for: macOS Sonoma
Impact: Processing maliciously crafted web content may lead to an
unexpected Safari crash
Description: An out-of-bounds access issue was addressed with improved
bounds checking.
CVE-2025-43209: Gary Kwong working with Trend Micro Zero Day Initiative

ImageIO
Available for: macOS Sonoma
Impact: Processing a maliciously crafted image may result in disclosure
of process memory
Description: An out-of-bounds read was addressed with improved input
validation.
CVE-2025-43226

LaunchServices
Available for: macOS Sonoma
Impact: An app may be able to execute arbitrary code out of its sandbox
or with certain elevated privileges
Description: This issue was addressed through improved state management.
CVE-2025-24119: an anonymous researcher

libxpc
Available for: macOS Sonoma
Impact: An app may be able to gain root privileges
Description: A path handling issue was addressed with improved
validation.
CVE-2025-43196: an anonymous researcher

libxslt
Available for: macOS Sonoma
Impact: Processing maliciously crafted web content may lead to memory
corruption
Description: This is a vulnerability in open source code and Apple
Software is among the affected projects. The CVE-ID was assigned by a
third party. Learn more about the issue and CVE-ID at cve.org.
CVE-2025-7424: Ivan Fratric of Google Project Zero

Managed Configuration
Available for: macOS Sonoma
Impact: Account-driven User Enrollment may still be possible with
Lockdown Mode turned on
Description: A configuration issue was addressed with additional
restrictions.
CVE-2025-43192: Pyrophoria

NetAuth
Available for: macOS Sonoma
Impact: An app may be able to ...