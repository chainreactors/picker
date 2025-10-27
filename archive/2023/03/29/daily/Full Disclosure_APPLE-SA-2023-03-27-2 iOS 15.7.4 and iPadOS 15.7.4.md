---
title: APPLE-SA-2023-03-27-2 iOS 15.7.4 and iPadOS 15.7.4
url: https://seclists.org/fulldisclosure/2023/Mar/20
source: Full Disclosure
date: 2023-03-29
fetch_date: 2025-10-04T11:03:25.512958
---

# APPLE-SA-2023-03-27-2 iOS 15.7.4 and iPadOS 15.7.4

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

[![Previous](/images/left-icon-16x16.png)](19)
[By Date](date.html#20)
[![Next](/images/right-icon-16x16.png)](21)

[![Previous](/images/left-icon-16x16.png)](19)
[By Thread](index.html#20)
[![Next](/images/right-icon-16x16.png)](21)

![](/shared/images/nst-icons.svg#search)

# APPLE-SA-2023-03-27-2 iOS 15.7.4 and iPadOS 15.7.4

---

*From*: Apple Product Security via Fulldisclosure <fulldisclosure () seclists org>
*Date*: Mon, 27 Mar 2023 16:08:24 -0700

---

```
-----BEGIN PGP SIGNED MESSAGE-----
Hash: SHA256

APPLE-SA-2023-03-27-2 iOS 15.7.4 and iPadOS 15.7.4

iOS 15.7.4 and iPadOS 15.7.4 addresses the following issues.
Information about the security content is also available at
https://support.apple.com/HT213673.

Accessibility
Available for: iPhone 6s (all models), iPhone 7 (all models), iPhone
SE (1st generation), iPad Air 2, iPad mini (4th generation), and iPod
touch (7th generation)
Impact: An app may be able to access information about a user’s
contacts
Description: A privacy issue was addressed with improved private data
redaction for log entries.
CVE-2023-23541: Csaba Fitzl (@theevilbit) of Offensive Security

Calendar
Available for: iPhone 6s (all models), iPhone 7 (all models), iPhone
SE (1st generation), iPad Air 2, iPad mini (4th generation), and iPod
touch (7th generation)
Impact: Importing a maliciously crafted calendar invitation may
exfiltrate user information
Description: Multiple validation issues were addressed with improved
input sanitization.
CVE-2023-27961: Rıza Sabuncu (@rizasabuncu)

Camera
Available for: iPhone 6s (all models), iPhone 7 (all models), iPhone
SE (1st generation), iPad Air 2, iPad mini (4th generation), and iPod
touch (7th generation)
Impact: A sandboxed app may be able to determine which app is
currently using the camera
Description: The issue was addressed with additional restrictions on
the observability of app states.
CVE-2023-23543: Yiğit Can YILMAZ (@yilmazcanyigit)

CommCenter
Available for: iPhone 6s (all models), iPhone 7 (all models), iPhone
SE (1st generation), iPad Air 2, iPad mini (4th generation), and iPod
touch (7th generation)
Impact: An app may be able to cause unexpected system termination or
write kernel memory
Description: An out-of-bounds write issue was addressed with improved
input validation.
CVE-2023-27936: Tingting Yin of Tsinghua University

Find My
Available for: iPhone 6s (all models), iPhone 7 (all models), iPhone
SE (1st generation), iPad Air 2, iPad mini (4th generation), and iPod
touch (7th generation)
Impact: An app may be able to read sensitive location information
Description: A privacy issue was addressed with improved private data
redaction for log entries.
CVE-2023-23537: an anonymous researcher

FontParser
Available for: iPhone 6s (all models), iPhone 7 (all models), iPhone
SE (1st generation), iPad Air 2, iPad mini (4th generation), and iPod
touch (7th generation)
Impact: Processing a maliciously crafted image may result in
disclosure of process memory
Description: The issue was addressed with improved memory handling.
CVE-2023-27956: Ye Zhang of Baidu Security

Identity Services
Available for: iPhone 6s (all models), iPhone 7 (all models), iPhone
SE (1st generation), iPad Air 2, iPad mini (4th generation), and iPod
touch (7th generation)
Impact: An app may be able to access information about a user’s
contacts
Description: A privacy issue was addressed with improved private data
redaction for log entries.
CVE-2023-27928: Csaba Fitzl (@theevilbit) of Offensive Security

ImageIO
Available for: iPhone 6s (all models), iPhone 7 (all models), iPhone
SE (1st generation), iPad Air 2, iPad mini (4th generation), and iPod
touch (7th generation)
Impact: Processing a maliciously crafted file may lead to unexpected
app termination or arbitrary code execution
Description: An out-of-bounds read was addressed with improved bounds
checking.
CVE-2023-27946: Mickey Jin (@patch1t)

ImageIO
Available for: iPhone 6s (all models), iPhone 7 (all models), iPhone
SE (1st generation), iPad Air 2, iPad mini (4th generation), and iPod
touch (7th generation)
Impact: Processing a maliciously crafted image may result in
disclosure of process memory
Description: The issue was addressed with improved memory handling.
CVE-2023-23535: ryuzaki

Kernel
Available for: iPhone 6s (all models), iPhone 7 (all models), iPhone
SE (1st generation), iPad Air 2, iPad mini (4th generation), and iPod
touch (7th generation)
Impact: An app may be able to disclose kernel memory
Description: A validation issue was addressed with improved input
sanitization.
CVE-2023-27941: Arsenii Kostromin (0x3c3e)

Kernel
Available for: iPhone 6s (all models), iPhone 7 (all models), iPhone
SE (1st generation), iPad Air 2, iPad mini (4th generation), and iPod
touch (7th generation)
Impact: An app may be able to execute arbitrary code with kernel
privileges
Description: A use after free issue was addressed with improved
memory management.
CVE-2023-27969: Adam Doupé of ASU SEFCOM

Model I/O
Available for: iPhone 6s (all models), iPhone 7 (all models), iPhone
SE (1st generation), iPad Air 2, iPad mini (4th generation), and iPod
touch (7th generation)
Impact: Processing a maliciously crafted file may lead to unexpected
app termination or arbitrary code execution
Description: An out-of-bounds read was addressed with improved input
validation.
CVE-2023-27949: Mickey Jin (@patch1t)

NetworkExtension
Available for: iPhone 6s (all models), iPhone 7 (all models), iPhone
SE (1st generation), iPad Air 2, iPad mini (4th generation), and iPod
touch (7th generation)
Impact: A user in a privileged network position may be able to spoof
a VPN server that is configured with EAP-only authentication on a
device
Description: The issue was addressed with improved authentication.
CVE-2023-28182: Zhuowei Zhang

Shortcuts
Available for: iPhone 6s (all models), iPhone 7 (all models), iPhone
SE (1st generation), iPad Air 2, iPad mini (4th generation), and iPod
touch (7th generation)
Impact: A shortcut may be able to use sensitive data with certain
actions without prompting the user
Description: The issue was addressed with additional permissions
checks.
CVE-2023-27963: Jubaer Alnazi Jabin of TRS Group Of Companies, and
Wenchao Li and Xiaolong Bai of Alibaba Group

WebKit
Available for: iPhone 6s (all models), iPhone 7 (all models), iPhone
SE (1st generation), iPad Air 2, iPad mini (4th generation), and iPod
touch (7th generation)
Impact: A website may be able to track sensitive user information
Description: The issue was addressed by removing origin information.
WebKit Bugzilla: 250837
CVE-2023-27954: an anonymous researcher

WebKit
Available for: iPhone 6s (all models), iPhone 7 (all models), iPhone
SE (1st generation), iPad Air 2, iPad mini (4th generation), and iPod
touch (7th generation)
Impact: Processing maliciously crafted web content may lead to
arbitrary code execution. Apple is aware of a report that this issue
may have been actively exploited.
Description: A type confusion issue was addressed with improved
checks.
WebKit Bugzilla: 251944
CVE-2023-23529: an anonymous researcher

Additional recognition

Mail
We would like to acknowledge Fabian Ising of FH Münster University of
Applied Sciences, Damian Poddebniak of FH Münster University of
Applied Sciences, Tobias Kappert of Münster University of Applied
Sciences, Christoph Saatjohann of Münster University of Applied
Sciences, and Sebast for their assistance.

WebKit Web Inspector
We would like to acknowledge Dohyun Lee (...