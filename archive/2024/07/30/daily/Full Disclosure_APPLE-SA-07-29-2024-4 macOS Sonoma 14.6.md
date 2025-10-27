---
title: APPLE-SA-07-29-2024-4 macOS Sonoma 14.6
url: https://seclists.org/fulldisclosure/2024/Jul/18
source: Full Disclosure
date: 2024-07-30
fetch_date: 2025-10-06T17:47:08.311752
---

# APPLE-SA-07-29-2024-4 macOS Sonoma 14.6

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

# APPLE-SA-07-29-2024-4 macOS Sonoma 14.6

---

*From*: Apple Product Security via Fulldisclosure <fulldisclosure () seclists org>
*Date*: Mon, 29 Jul 2024 16:12:52 -0700

---

```
-----BEGIN PGP SIGNED MESSAGE-----
Hash: SHA256

APPLE-SA-07-29-2024-4 macOS Sonoma 14.6

macOS Sonoma 14.6 addresses the following issues.
Information about the security content is also available at
https://support.apple.com/HT214119.

Apple maintains a Security Releases page at
https://support.apple.com/HT201222 which lists recent
software updates with security advisories.

Accounts
Available for: macOS Sonoma
Impact: A malicious application may be able to access private
information
Description: The issue was addressed with improved checks.
CVE-2024-40804: IES Red Team of ByteDance

apache
Available for: macOS Sonoma
Impact: Multiple issues in apache
Description: This is a vulnerability in open source code and Apple
Software is among the affected projects. The CVE-ID was assigned by a
third party. Learn more about the issue and CVE-ID at cve.org.
CVE-2023-38709: Yeto
CVE-2024-24795: Yeto
CVE-2024-27316: Yeto

APFS
Available for: macOS Sonoma
Impact: A malicious application may be able to bypass Privacy
preferences
Description: The issue was addressed with improved restriction of data
container access.
CVE-2024-40783: Csaba Fitzl (@theevilbit) of Kandji

AppleMobileFileIntegrity
Available for: macOS Sonoma
Impact: An app may be able to bypass Privacy preferences
Description: A downgrade issue was addressed with additional code-
signing restrictions.
CVE-2024-40774: Mickey Jin (@patch1t)
CVE-2024-40814: Mickey Jin (@patch1t)

AppleMobileFileIntegrity
Available for: macOS Sonoma
Impact: An app may be able to leak sensitive user information
Description: A downgrade issue was addressed with additional code-
signing restrictions.
CVE-2024-40775: Mickey Jin (@patch1t)

AppleVA
Available for: macOS Sonoma
Impact: Processing a maliciously crafted file may lead to unexpected app
termination
Description: The issue was addressed with improved memory handling.
CVE-2024-27877: Michael DePlante (@izobashi) of Trend Micro Zero Day
Initiative

ASP TCP
Available for: macOS Sonoma
Impact: An app with root privileges may be able to execute arbitrary
code with kernel privileges
Description: A buffer overflow issue was addressed with improved memory
handling.
CVE-2024-27878: CertiK SkyFall Team

CoreGraphics
Available for: macOS Sonoma
Impact: Processing a maliciously crafted file may lead to unexpected app
termination
Description: An out-of-bounds read issue was addressed with improved
input validation.
CVE-2024-40799: D4m0n

CoreMedia
Available for: macOS Sonoma
Impact: Processing a maliciously crafted video file may lead to
unexpected app termination
Description: An out-of-bounds write issue was addressed with improved
input validation.
CVE-2024-27873: Amir Bazine and Karsten König of CrowdStrike Counter
Adversary Operations

curl
Available for: macOS Sonoma
Impact: Multiple issues in curl
Description: This is a vulnerability in open source code and Apple
Software is among the affected projects. The CVE-ID was assigned by a
third party. Learn more about the issue and CVE-ID at cve.org.
CVE-2024-2004
CVE-2024-2379
CVE-2024-2398
CVE-2024-2466

DesktopServices
Available for: macOS Sonoma
Impact: An app may be able to overwrite arbitrary files
Description: The issue was addressed with improved checks.
CVE-2024-40827: an anonymous researcher

dyld
Available for: macOS Sonoma
Impact: A malicious attacker with arbitrary read and write capability
may be able to bypass Pointer Authentication
Description: A race condition was addressed with additional validation.
CVE-2024-40815: w0wbox

Family Sharing
Available for: macOS Sonoma
Impact: An app may be able to read sensitive location information
Description: This issue was addressed with improved data protection.
CVE-2024-40795: Csaba Fitzl (@theevilbit) of Kandji

ImageIO
Available for: macOS Sonoma
Impact: Processing an image may lead to a denial-of-service
Description: This is a vulnerability in open source code and Apple
Software is among the affected projects. The CVE-ID was assigned by a
third party. Learn more about the issue and CVE-ID at cve.org.
CVE-2023-6277
CVE-2023-52356

ImageIO
Available for: macOS Sonoma
Impact: Processing a maliciously crafted file may lead to unexpected app
termination
Description: An out-of-bounds read issue was addressed with improved
input validation.
CVE-2024-40806: Yisumi

ImageIO
Available for: macOS Sonoma
Impact: Processing a maliciously crafted file may lead to unexpected app
termination
Description: An out-of-bounds access issue was addressed with improved
bounds checking.
CVE-2024-40777: Junsung Lee working with Trend Micro Zero Day
Initiative, and Amir Bazine and Karsten König of CrowdStrike Counter
Adversary Operations

ImageIO
Available for: macOS Sonoma
Impact: Processing a maliciously crafted file may lead to unexpected app
termination
Description: An integer overflow was addressed with improved input
validation.
CVE-2024-40784: Junsung Lee working with Trend Micro Zero Day
Initiative, Gandalf4a

Kernel
Available for: macOS Sonoma
Impact: A local attacker may be able to determine kernel memory layout
Description: An information disclosure issue was addressed with improved
private data redaction for log entries.
CVE-2024-27863: CertiK SkyFall Team

Kernel
Available for: macOS Sonoma
Impact: A local attacker may be able to cause unexpected system shutdown
Description: An out-of-bounds read was addressed with improved input
validation.
CVE-2024-40816: sqrtpwn

Kernel
Available for: macOS Sonoma
Impact: A local attacker may be able to cause unexpected system shutdown
Description: A type confusion issue was addressed with improved memory
handling.
CVE-2024-40788: Minghao Lin and Jiaxun Zhu from Zhejiang University

Keychain Access
Available for: macOS Sonoma
Impact: An attacker may be able to cause unexpected app termination
Description: A type confusion issue was addressed with improved checks.
CVE-2024-40803: Patrick Wardle of DoubleYou & the Objective-See
Foundation

libxpc
Available for: macOS Sonoma
Impact: An app may be able to bypass Privacy preferences
Description: A permissions issue was addressed with additional
restrictions.
CVE-2024-40805

Messages
Available for: macOS Sonoma
Impact: An app may be able to view a contact's phone number in system
logs
Description: The issue was addressed with improved checks.
CVE-2024-40832: Rodolphe BRUNETTI (@eisw0lf)

NetworkExtension
Available for: macOS Sonoma
Impact: Private browsing may leak some browsing history
Description: A privacy issue was addressed with improved private data
redaction for log entries.
CVE-2024-40796: Adam M.

OpenSSH
Available for: macOS Sonoma
Impact: A remote attacker may be able to cause arbitrary code execution
Description: This is a vulnerability in open source code and Apple
Software is among the affected projects. The CVE-ID was assigned by a
third party. Learn more about the issue and CVE-ID at cve.org.
CVE-2024-6387

PackageKit
Available for: macOS Sonoma
Impact: A local attacker may be able to elevate their privileges
Description: The issue was addressed with improved...