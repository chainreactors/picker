---
title: APPLE-SA-07-29-2024-5 macOS Ventura 13.6.8
url: https://seclists.org/fulldisclosure/2024/Jul/19
source: Full Disclosure
date: 2024-07-30
fetch_date: 2025-10-06T17:47:06.918103
---

# APPLE-SA-07-29-2024-5 macOS Ventura 13.6.8

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

[![Previous](/images/left-icon-16x16.png)](18)
[By Date](date.html#19)
[![Next](/images/right-icon-16x16.png)](20)

[![Previous](/images/left-icon-16x16.png)](18)
[By Thread](index.html#19)
[![Next](/images/right-icon-16x16.png)](20)

![](/shared/images/nst-icons.svg#search)

# APPLE-SA-07-29-2024-5 macOS Ventura 13.6.8

---

*From*: Apple Product Security via Fulldisclosure <fulldisclosure () seclists org>
*Date*: Mon, 29 Jul 2024 16:13:26 -0700

---

```
-----BEGIN PGP SIGNED MESSAGE-----
Hash: SHA256

APPLE-SA-07-29-2024-5 macOS Ventura 13.6.8

macOS Ventura 13.6.8 addresses the following issues.
Information about the security content is also available at
https://support.apple.com/HT214120.

Apple maintains a Security Releases page at
https://support.apple.com/HT201222 which lists recent
software updates with security advisories.

APFS
Available for: macOS Ventura
Impact: A malicious application may be able to bypass Privacy
preferences
Description: The issue was addressed with improved restriction of data
container access.
CVE-2024-40783: Csaba Fitzl (@theevilbit) of Kandji

Apple Neural Engine
Available for: macOS Ventura
Impact: An app may be able to execute arbitrary code with kernel
privileges
Description: The issue was addressed with improved memory handling.
CVE-2024-27826: Minghao Lin, and Ye Zhang (@VAR10CK) of Baidu Security

AppleMobileFileIntegrity
Available for: macOS Ventura
Impact: An app may be able to bypass Privacy preferences
Description: A downgrade issue was addressed with additional code-
signing restrictions.
CVE-2024-40774: Mickey Jin (@patch1t)

AppleMobileFileIntegrity
Available for: macOS Ventura
Impact: An app may be able to leak sensitive user information
Description: A downgrade issue was addressed with additional code-
signing restrictions.
CVE-2024-40775: Mickey Jin (@patch1t)

AppleVA
Available for: macOS Ventura
Impact: Processing a maliciously crafted file may lead to a denial-of-
service or potentially disclose memory contents
Description: The issue was addressed with improved memory handling.
CVE-2024-27877: Michael DePlante (@izobashi) of Trend Micro Zero Day
Initiative

CoreGraphics
Available for: macOS Ventura
Impact: Processing a maliciously crafted file may lead to unexpected app
termination
Description: An out-of-bounds read issue was addressed with improved
input validation.
CVE-2024-40799: D4m0n

CoreMedia
Available for: macOS Ventura
Impact: Processing a maliciously crafted video file may lead to
unexpected app termination
Description: An out-of-bounds write issue was addressed with improved
input validation.
CVE-2024-27873: Amir Bazine and Karsten König of CrowdStrike Counter
Adversary Operations

curl
Available for: macOS Ventura
Impact: Multiple issues in curl
Description: This is a vulnerability in open source code and Apple
Software is among the affected projects. The CVE-ID was assigned by a
third party. Learn more about the issue and CVE-ID at cve.org.
CVE-2024-2004
CVE-2024-2379
CVE-2024-2398
CVE-2024-2466

DesktopServices
Available for: macOS Ventura
Impact: An app may be able to overwrite arbitrary files
Description: The issue was addressed with improved checks.
CVE-2024-40827: an anonymous researcher

dyld
Available for: macOS Ventura
Impact: A malicious attacker with arbitrary read and write capability
may be able to bypass Pointer Authentication
Description: A race condition was addressed with additional validation.
CVE-2024-40815: w0wbox

ImageIO
Available for: macOS Ventura
Impact: Processing an image may lead to a denial-of-service
Description: This is a vulnerability in open source code and Apple
Software is among the affected projects. The CVE-ID was assigned by a
third party. Learn more about the issue and CVE-ID at cve.org.
CVE-2023-6277
CVE-2023-52356

ImageIO
Available for: macOS Ventura
Impact: Processing a maliciously crafted file may lead to unexpected app
termination
Description: An out-of-bounds read issue was addressed with improved
input validation.
CVE-2024-40806: Yisumi

ImageIO
Available for: macOS Ventura
Impact: Processing a maliciously crafted file may lead to unexpected app
termination
Description: An integer overflow was addressed with improved input
validation.
CVE-2024-40784: Junsung Lee working with Trend Micro Zero Day Initiative
and Gandalf4a

Kernel
Available for: macOS Ventura
Impact: A local attacker may be able to cause unexpected system shutdown
Description: An out-of-bounds read was addressed with improved input
validation.
CVE-2024-40816: sqrtpwn

Kernel
Available for: macOS Ventura
Impact: A local attacker may be able to cause unexpected system shutdown
Description: A type confusion issue was addressed with improved memory
handling.
CVE-2024-40788: Minghao Lin and Jiaxun Zhu from Zhejiang University

Keychain Access
Available for: macOS Ventura
Impact: An attacker may be able to cause unexpected app termination
Description: A type confusion issue was addressed with improved checks.
CVE-2024-40803: Patrick Wardle of DoubleYou & the Objective-See
Foundation

NetworkExtension
Available for: macOS Ventura
Impact: Private browsing may leak some browsing history
Description: A privacy issue was addressed with improved private data
redaction for log entries.
CVE-2024-40796: Adam M.

OpenSSH
Available for: macOS Ventura
Impact: A remote attacker may be able to cause arbitrary code execution
Description: This is a vulnerability in open source code and Apple
Software is among the affected projects. The CVE-ID was assigned by a
third party. Learn more about the issue and CVE-ID at cve.org.
CVE-2024-6387

PackageKit
Available for: macOS Ventura
Impact: A local attacker may be able to elevate their privileges
Description: The issue was addressed with improved checks.
CVE-2024-40781: Mickey Jin (@patch1t)
CVE-2024-40802: Mickey Jin (@patch1t)

PackageKit
Available for: macOS Ventura
Impact: An app may be able to access user-sensitive data
Description: The issue was addressed with improved checks.
CVE-2024-40823: Zhongquan Li (@Guluisacat) from Dawn Security Lab of
JingDong

PackageKit
Available for: macOS Ventura
Impact: An app may be able to modify protected parts of the file system
Description: A permissions issue was addressed with additional
restrictions.
CVE-2024-27882: Mickey Jin (@patch1t)
CVE-2024-27883: Csaba Fitzl (@theevilbit) of Kandji and Mickey Jin
(@patch1t)

Restore Framework
Available for: macOS Ventura
Impact: An app may be able to modify protected parts of the file system
Description: An input validation issue was addressed with improved input
validation.
CVE-2024-40800: Claudio Bozzato and Francesco Benvenuto of Cisco Talos.

Safari
Available for: macOS Ventura
Impact: Visiting a website that frames malicious content may lead to UI
spoofing
Description: The issue was addressed with improved UI handling.
CVE-2024-40817: Yadhu Krishna M and Narendra Bhati, Manager of Cyber
Security At Suma Soft Pvt. Ltd, Pune (India)

Scripting Bridge
Available for: macOS Ventura
Impact: An app may be able to access information about a user’s contacts
Description: A privacy issue was addressed with improved private data
redaction for log entries.
CVE-2024-27881: Kirin (@Pwnrin)

Security
Available for: macOS Ventura
Impact: Third party app extensions may not receive the correct sandbox
restrictions
Description: An access issue was addressed with additional sandbox
restrictions.
CVE-2024-40821: Joshua Jones

Security
Available for: macOS Ventura
Impact: An app may be able to read Saf...