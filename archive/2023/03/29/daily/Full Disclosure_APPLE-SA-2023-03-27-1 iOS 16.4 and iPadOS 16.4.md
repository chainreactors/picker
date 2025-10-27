---
title: APPLE-SA-2023-03-27-1 iOS 16.4 and iPadOS 16.4
url: https://seclists.org/fulldisclosure/2023/Mar/19
source: Full Disclosure
date: 2023-03-29
fetch_date: 2025-10-04T11:03:26.704872
---

# APPLE-SA-2023-03-27-1 iOS 16.4 and iPadOS 16.4

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

# APPLE-SA-2023-03-27-1 iOS 16.4 and iPadOS 16.4

---

*From*: Apple Product Security via Fulldisclosure <fulldisclosure () seclists org>
*Date*: Mon, 27 Mar 2023 16:08:21 -0700

---

```
-----BEGIN PGP SIGNED MESSAGE-----
Hash: SHA256

APPLE-SA-2023-03-27-1 iOS 16.4 and iPadOS 16.4

iOS 16.4 and iPadOS 16.4 addresses the following issues.
Information about the security content is also available at
https://support.apple.com/HT213676.

Accessibility
Available for: iPhone 8 and later, iPad Pro (all models), iPad Air
3rd generation and later, iPad 5th generation and later, and iPad
mini 5th generation and later
Impact: An app may be able to access information about a user’s
contacts
Description: A privacy issue was addressed with improved private data
redaction for log entries.
CVE-2023-23541: Csaba Fitzl (@theevilbit) of Offensive Security

Apple Neural Engine
Available for: iPhone 8 and later, iPad Pro (all models), iPad Air
3rd generation and later, iPad 5th generation and later, and iPad
mini 5th generation and later
Impact: An app may be able to execute arbitrary code with kernel
privileges
Description: The issue was addressed with improved memory handling.
CVE-2023-23540: Mohamed GHANNAM (@_simo36)
CVE-2023-27959: Mohamed GHANNAM (@_simo36)

Apple Neural Engine
Available for: iPhone 8 and later, iPad Pro (all models), iPad Air
3rd generation and later, iPad 5th generation and later, and iPad
mini 5th generation and later
Impact: An app may be able to execute arbitrary code with kernel
privileges
Description: An out-of-bounds write issue was addressed with improved
bounds checking.
CVE-2023-27970: Mohamed GHANNAM

Apple Neural Engine
Available for: iPhone 8 and later, iPad Pro (all models), iPad Air
3rd generation and later, iPad 5th generation and later, and iPad
mini 5th generation and later
Impact: An app may be able to break out of its sandbox
Description: This issue was addressed with improved checks.
CVE-2023-23532: Mohamed Ghannam (@_simo36)

AppleMobileFileIntegrity
Available for: iPhone 8 and later, iPad Pro (all models), iPad Air
3rd generation and later, iPad 5th generation and later, and iPad
mini 5th generation and later
Impact: A user may gain access to protected parts of the file system
Description: The issue was addressed with improved checks.
CVE-2023-23527: Mickey Jin (@patch1t)

AppleMobileFileIntegrity
Available for: iPhone 8 and later, iPad Pro (all models), iPad Air
3rd generation and later, iPad 5th generation and later, and iPad
mini 5th generation and later
Impact: An app may be able to access user-sensitive data
Description: This issue was addressed by removing the vulnerable
code.
CVE-2023-27931: Mickey Jin (@patch1t)

Calendar
Available for: iPhone 8 and later, iPad Pro (all models), iPad Air
3rd generation and later, iPad 5th generation and later, and iPad
mini 5th generation and later
Impact: Importing a maliciously crafted calendar invitation may
exfiltrate user information
Description: Multiple validation issues were addressed with improved
input sanitization.
CVE-2023-27961: Rıza Sabuncu (@rizasabuncu)

Camera
Available for: iPhone 8 and later, iPad Pro (all models), iPad Air
3rd generation and later, iPad 5th generation and later, and iPad
mini 5th generation and later
Impact: A sandboxed app may be able to determine which app is
currently using the camera
Description: The issue was addressed with additional restrictions on
the observability of app states.
CVE-2023-23543: Yiğit Can YILMAZ (@yilmazcanyigit)

CarPlay
Available for: iPhone 8 and later, iPad Pro (all models), iPad Air
3rd generation and later, iPad 5th generation and later, and iPad
mini 5th generation and later
Impact: A user in a privileged network position may be able to cause
a denial-of-service
Description: A buffer overflow was addressed with improved bounds
checking.
CVE-2023-23494: Itay Iellin of General Motors Product Cyber Security

ColorSync
Available for: iPhone 8 and later, iPad Pro (all models), iPad Air
3rd generation and later, iPad 5th generation and later, and iPad
mini 5th generation and later
Impact: An app may be able to read arbitrary files
Description: The issue was addressed with improved checks.
CVE-2023-27955: JeongOhKyea

Core Bluetooth
Available for: iPhone 8 and later, iPad Pro (all models), iPad Air
3rd generation and later, iPad 5th generation and later, and iPad
mini 5th generation and later
Impact: Processing a maliciously crafted Bluetooth packet may result
in disclosure of process memory
Description: An out-of-bounds read was addressed with improved bounds
checking.
CVE-2023-23528: Jianjun Dai and Guang Gong of 360 Vulnerability
Research Institute

CoreCapture
Available for: iPhone 8 and later, iPad Pro (all models), iPad Air
3rd generation and later, iPad 5th generation and later, and iPad
mini 5th generation and later
Impact: An app may be able to execute arbitrary code with kernel
privileges
Description: The issue was addressed with improved memory handling.
CVE-2023-28181: Tingting Yin of Tsinghua University

Find My
Available for: iPhone 8 and later, iPad Pro (all models), iPad Air
3rd generation and later, iPad 5th generation and later, and iPad
mini 5th generation and later
Impact: An app may be able to read sensitive location information
Description: A privacy issue was addressed with improved private data
redaction for log entries.
CVE-2023-23537: an anonymous researcher

FontParser
Available for: iPhone 8 and later, iPad Pro (all models), iPad Air
3rd generation and later, iPad 5th generation and later, and iPad
mini 5th generation and later
Impact: Processing a maliciously crafted image may result in
disclosure of process memory
Description: The issue was addressed with improved memory handling.
CVE-2023-27956: Ye Zhang of Baidu Security

Foundation
Available for: iPhone 8 and later, iPad Pro (all models), iPad Air
3rd generation and later, iPad 5th generation and later, and iPad
mini 5th generation and later
Impact: Parsing a maliciously crafted plist may lead to an unexpected
app termination or arbitrary code execution
Description: An integer overflow was addressed with improved input
validation.
CVE-2023-27937: an anonymous researcher

iCloud
Available for: iPhone 8 and later, iPad Pro (all models), iPad Air
3rd generation and later, iPad 5th generation and later, and iPad
mini 5th generation and later
Impact: A file from an iCloud shared-by-me folder may be able to
bypass Gatekeeper
Description: This was addressed with additional checks by Gatekeeper
on files downloaded from an iCloud shared-by-me folder.
CVE-2023-23526: Jubaer Alnazi of TRS Group of Companies

Identity Services
Available for: iPhone 8 and later, iPad Pro (all models), iPad Air
3rd generation and later, iPad 5th generation and later, and iPad
mini 5th generation and later
Impact: An app may be able to access information about a user’s
contacts
Description: A privacy issue was addressed with improved private data
redaction for log entries.
CVE-2023-27928: Csaba Fitzl (@theevilbit) of Offensive Security

ImageIO
Available for: iPhone 8 and later, iPad Pro (all models), iPad Air
3rd generation and later, iPad 5th generation and later, and iPad
mini 5th generation and later
Impact: Pro...