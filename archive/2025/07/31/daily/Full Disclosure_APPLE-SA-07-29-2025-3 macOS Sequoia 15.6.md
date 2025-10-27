---
title: APPLE-SA-07-29-2025-3 macOS Sequoia 15.6
url: https://seclists.org/fulldisclosure/2025/Jul/32
source: Full Disclosure
date: 2025-07-31
fetch_date: 2025-10-06T23:56:44.221374
---

# APPLE-SA-07-29-2025-3 macOS Sequoia 15.6

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

[![Previous](/images/left-icon-16x16.png)](31)
[By Date](date.html#32)
[![Next](/images/right-icon-16x16.png)](33)

[![Previous](/images/left-icon-16x16.png)](31)
[By Thread](index.html#32)
[![Next](/images/right-icon-16x16.png)](33)

![](/shared/images/nst-icons.svg#search)

# APPLE-SA-07-29-2025-3 macOS Sequoia 15.6

---

*From*: Apple Product Security via Fulldisclosure <fulldisclosure () seclists org>
*Date*: Tue, 29 Jul 2025 16:28:20 -0700

---

```
-----BEGIN PGP SIGNED MESSAGE-----
Hash: SHA256

APPLE-SA-07-29-2025-3 macOS Sequoia 15.6

macOS Sequoia 15.6 addresses the following issues.
Information about the security content is also available at
https://support.apple.com/124149.

Apple maintains a Security Releases page at
https://support.apple.com/100100 which lists recent
software updates with security advisories.

Admin Framework
Available for: macOS Sequoia
Impact: An app may be able to cause a denial-of-service
Description: A path handling issue was addressed with improved
validation.
CVE-2025-43191: Ryan Dowd (@_rdowd)

afclip
Available for: macOS Sequoia
Impact: Parsing a file may lead to an unexpected app termination
Description: The issue was addressed with improved memory handling.
CVE-2025-43186: Hossein Lotfi (@hosselot) of Trend Micro Zero Day
Initiative

AMD
Available for: macOS Sequoia
Impact: An app may be able to cause unexpected system termination
Description: A race condition was addressed with improved state
handling.
CVE-2025-43244: ABC Research s.r.o.

AppleMobileFileIntegrity
Available for: macOS Sequoia
Impact: An app may be able to gain root privileges
Description: A permissions issue was addressed with additional
restrictions.
CVE-2025-31243: Mickey Jin (@patch1t)

AppleMobileFileIntegrity
Available for: macOS Sequoia
Impact: A malicious app may be able to launch arbitrary binaries on a
trusted device
Description: This issue was addressed with improved input validation.
CVE-2025-43253: Noah Gregory (wts.dev)

AppleMobileFileIntegrity
Available for: macOS Sequoia
Impact: An app may be able to gain root privileges
Description: A logic issue was addressed with improved checks.
CVE-2025-43249: Mickey Jin (@patch1t)

AppleMobileFileIntegrity
Available for: macOS Sequoia
Impact: A malicious app may be able to gain root privileges
Description: A logic issue was addressed with improved restrictions.
CVE-2025-43248: Mickey Jin (@patch1t)

AppleMobileFileIntegrity
Available for: macOS Sequoia
Impact: An app may be able to access protected user data
Description: A downgrade issue was addressed with additional code-
signing restrictions.
CVE-2025-43245: Mickey Jin (@patch1t)

Archive Utility
Available for: macOS Sequoia
Impact: An app may be able to break out of its sandbox
Description: This issue was addressed with improved handling of
symlinks.
CVE-2025-43257: Mickey Jin (@patch1t)

CFNetwork
Available for: macOS Sequoia
Impact: An attacker may be able to cause unexpected app termination
Description: A use-after-free issue was addressed by removing the
vulnerable code.
CVE-2025-43222: Andreas Jaegersberger & Ro Achterberg of Nosebeard Labs

CFNetwork
Available for: macOS Sequoia
Impact: A non-privileged user may be able to modify restricted network
settings
Description: A denial-of-service issue was addressed with improved input
validation.
CVE-2025-43223: Andreas Jaegersberger & Ro Achterberg of Nosebeard Labs

copyfile
Available for: macOS Sequoia
Impact: An app may be able to access protected user data
Description: This issue was addressed with improved validation of
symlinks.
CVE-2025-43220: Mickey Jin (@patch1t)

Core Services
Available for: macOS Sequoia
Impact: A malicious app may be able to gain root privileges
Description: A permissions issue was addressed by removing the
vulnerable code.
CVE-2025-43199: Gergely Kalman (@gergely_kalman), an anonymous
researcher

CoreAudio
Available for: macOS Sequoia
Impact: Processing a maliciously crafted audio file may lead to memory
corruption
Description: The issue was addressed with improved memory handling.
CVE-2025-43277: Google's Threat Analysis Group

CoreMedia
Available for: macOS Sequoia
Impact: A sandboxed process may be able to circumvent sandbox
restrictions
Description: A permissions issue was addressed with additional sandbox
restrictions.
CVE-2025-43273: Seo Hyun-gyu (@wh1te4ever), Dora Orak, Minghao Lin
(@Y1nKoc) and XiLong Zhang (@Resery4) of Xiaomi and noir (@ROIS) and
fmyy (@风沐云烟)

CoreMedia
Available for: macOS Sequoia
Impact: Processing a maliciously crafted media file may lead to
unexpected app termination or corrupt process memory
Description: An out-of-bounds access issue was addressed with improved
bounds checking.
CVE-2025-43210: Hossein Lotfi (@hosselot) of Trend Micro Zero Day
Initiative

CoreMedia Playback
Available for: macOS Sequoia
Impact: An app may be able to access user-sensitive data
Description: The issue was addressed with additional permissions checks.
CVE-2025-43230: Chi Yuan Chang of ZUSO ART and taikosoup

CoreServices
Available for: macOS Sequoia
Impact: An app may be able to access sensitive user data
Description: An issue existed in the handling of environment variables.
This issue was addressed with improved validation.
CVE-2025-43195: 风沐云烟 (@binary_fmyy) and Minghao Lin (@Y1nKoc)

Directory Utility
Available for: macOS Sequoia
Impact: An app may be able to access sensitive user data
Description: An injection issue was addressed with improved validation.
CVE-2025-43267: Mickey Jin (@patch1t)

Disk Images
Available for: macOS Sequoia
Impact: Running an hdiutil command may unexpectedly execute arbitrary
code
Description: This issue was addressed by removing the vulnerable code.
CVE-2025-43187: 风沐云烟 (@binary_fmyy) and Minghao Lin (@Y1nKoc)

DiskArbitration
Available for: macOS Sequoia
Impact: A malicious app may be able to gain root privileges
Description: A permissions issue was addressed with additional
restrictions.
CVE-2025-43188: an anonymous researcher

Dock
Available for: macOS Sequoia
Impact: An app may be able to access protected user data
Description: This issue was addressed by removing the vulnerable code.
CVE-2025-43198: Mickey Jin (@patch1t)

file
Available for: macOS Sequoia
Impact: Processing a maliciously crafted file may lead to unexpected app
termination
Description: An out-of-bounds read was addressed with improved input
validation.
CVE-2025-43254: 2ourc3 | Salim Largo

File Bookmark
Available for: macOS Sequoia
Impact: An app may be able to break out of its sandbox
Description: A logic issue was addressed with improved checks.
CVE-2025-43261: an anonymous researcher

Find My
Available for: macOS Sequoia
Impact: An app may be able to fingerprint the user
Description: A permissions issue was addressed with additional
restrictions.
CVE-2025-31279: Dawuge of Shuffle Team

GPU Drivers
Available for: macOS Sequoia
Impact: An app may be able to cause unexpected system termination
Description: An out-of-bounds read was addressed with improved bounds
checking.
CVE-2025-43255: Anonymous working with Trend Micro Zero Day Initiative

ICU
Available for: macOS Sequoia
Impact: Processing maliciously crafted web content may lead to an
unexpected Safari crash
Description: An out-of-bounds access issue was addressed with improved
bounds checking.
CVE-2025-43209: Gary Kwong working with Trend Micro Zero Day Initiative

ImageIO
Available for: macOS Sequoia
Impact: Processing a maliciously crafted image may result in disclosure
of process memory
Description...