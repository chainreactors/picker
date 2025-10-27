---
title: APPLE-SA-2023-03-27-3 macOS Ventura 13.3
url: https://seclists.org/fulldisclosure/2023/Mar/17
source: Full Disclosure
date: 2023-03-29
fetch_date: 2025-10-04T11:03:29.355925
---

# APPLE-SA-2023-03-27-3 macOS Ventura 13.3

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

[![Previous](/images/left-icon-16x16.png)](16)
[By Date](date.html#17)
[![Next](/images/right-icon-16x16.png)](18)

[![Previous](/images/left-icon-16x16.png)](16)
[By Thread](index.html#17)
[![Next](/images/right-icon-16x16.png)](18)

![](/shared/images/nst-icons.svg#search)

# APPLE-SA-2023-03-27-3 macOS Ventura 13.3

---

*From*: Apple Product Security via Fulldisclosure <fulldisclosure () seclists org>
*Date*: Mon, 27 Mar 2023 16:08:27 -0700

---

```
-----BEGIN PGP SIGNED MESSAGE-----
Hash: SHA256

APPLE-SA-2023-03-27-3 macOS Ventura 13.3

macOS Ventura 13.3 addresses the following issues.
Information about the security content is also available at
https://support.apple.com/HT213670.

AMD
Available for: macOS Ventura
Impact: An app may be able to cause unexpected system termination or
write kernel memory
Description: A buffer overflow issue was addressed with improved
memory handling.
CVE-2023-27968: ABC Research s.r.o.

Apple Neural Engine
Available for: macOS Ventura
Impact: An app may be able to break out of its sandbox
Description: This issue was addressed with improved checks.
CVE-2023-23532: Mohamed Ghannam (@_simo36)

AppleMobileFileIntegrity
Available for: macOS Ventura
Impact: A user may gain access to protected parts of the file system
Description: The issue was addressed with improved checks.
CVE-2023-23527: Mickey Jin (@patch1t)

AppleMobileFileIntegrity
Available for: macOS Ventura
Impact: An app may be able to access user-sensitive data
Description: This issue was addressed by removing the vulnerable
code.
CVE-2023-27931: Mickey Jin (@patch1t)

Archive Utility
Available for: macOS Ventura
Impact: An archive may be able to bypass Gatekeeper
Description: The issue was addressed with improved checks.
CVE-2023-27951: Brandon Dalton of Red Canary and Csaba Fitzl
(@theevilbit) of Offensive Security

Calendar
Available for: macOS Ventura
Impact: Importing a maliciously crafted calendar invitation may
exfiltrate user information
Description: Multiple validation issues were addressed with improved
input sanitization.
CVE-2023-27961: Rıza Sabuncu - twitter.com/rizasabuncu

Camera
Available for: macOS Ventura
Impact: A sandboxed app may be able to determine which app is
currently using the camera
Description: The issue was addressed with additional restrictions on
the observability of app states.
CVE-2023-23543: Yiğit Can YILMAZ (@yilmazcanyigit)

Carbon Core
Available for: macOS Ventura
Impact: Processing a maliciously crafted image may result in
disclosure of process memory
Description: The issue was addressed with improved checks.
CVE-2023-23534: Mickey Jin (@patch1t)

ColorSync
Available for: macOS Ventura
Impact: An app may be able to read arbitrary files
Description: The issue was addressed with improved checks.
CVE-2023-27955: JeongOhKyea

CommCenter
Available for: macOS Ventura
Impact: An app may be able to cause unexpected system termination or
write kernel memory
Description: An out-of-bounds write issue was addressed with improved
input validation.
CVE-2023-27936: Tingting Yin of Tsinghua University

CoreCapture
Available for: macOS Ventura
Impact: An app may be able to execute arbitrary code with kernel
privileges
Description: The issue was addressed with improved memory handling.
CVE-2023-28181: Tingting Yin of Tsinghua University

curl
Available for: macOS Ventura
Impact: Multiple issues in curl
Description: Multiple issues were addressed by updating curl.
CVE-2022-43551
CVE-2022-43552

dcerpc
Available for: macOS Ventura
Impact: A remote user may be able to cause unexpected app termination
or arbitrary code execution
Description: A memory initialization issue was addressed.
CVE-2023-27934: Aleksandar Nikolic of Cisco Talos

dcerpc
Available for: macOS Ventura
Impact: A user in a privileged network position may be able to cause
a denial-of-service
Description: A denial-of-service issue was addressed with improved
memory handling.
CVE-2023-28180: Aleksandar Nikolic of Cisco Talos

dcerpc
Available for: macOS Ventura
Impact: A remote user may be able to cause unexpected app termination
or arbitrary code execution
Description: The issue was addressed with improved bounds checks.
CVE-2023-27935: Aleksandar Nikolic of Cisco Talos

dcerpc
Available for: macOS Ventura
Impact: A remote user may be able to cause unexpected system
termination or corrupt kernel memory
Description: The issue was addressed with improved memory handling.
CVE-2023-27953: Aleksandar Nikolic of Cisco Talos
CVE-2023-27958: Aleksandar Nikolic of Cisco Talos

Display
Available for: macOS Ventura
Impact: An app may be able to execute arbitrary code with kernel
privileges
Description: A memory corruption issue was addressed with improved
state management.
CVE-2023-27965: Proteas of Pangu Lab

FaceTime
Available for: macOS Ventura
Impact: An app may be able to access user-sensitive data
Description: A privacy issue was addressed by moving sensitive data
to a more secure location.
CVE-2023-28190: Joshua Jones

Find My
Available for: macOS Ventura
Impact: An app may be able to read sensitive location information
Description: A privacy issue was addressed with improved private data
redaction for log entries.
CVE-2023-23537: an anonymous researcher

FontParser
Available for: macOS Ventura
Impact: Processing a maliciously crafted image may result in
disclosure of process memory
Description: The issue was addressed with improved memory handling.
CVE-2023-27956: Ye Zhang of Baidu Security

Foundation
Available for: macOS Ventura
Impact: Parsing a maliciously crafted plist may lead to an unexpected
app termination or arbitrary code execution
Description: An integer overflow was addressed with improved input
validation.
CVE-2023-27937: an anonymous researcher

iCloud
Available for: macOS Ventura
Impact: A file from an iCloud shared-by-me folder may be able to
bypass Gatekeeper
Description: This was addressed with additional checks by Gatekeeper
on files downloaded from an iCloud shared-by-me folder.
CVE-2023-23526: Jubaer Alnazi of TRS Group of Companies

Identity Services
Available for: macOS Ventura
Impact: An app may be able to access information about a user’s
contacts
Description: A privacy issue was addressed with improved private data
redaction for log entries.
CVE-2023-27928: Csaba Fitzl (@theevilbit) of Offensive Security

ImageIO
Available for: macOS Ventura
Impact: Processing a maliciously crafted image may result in
disclosure of process memory
Description: The issue was addressed with improved memory handling.
CVE-2023-23535: ryuzaki

ImageIO
Available for: macOS Ventura
Impact: Processing a maliciously crafted image may result in
disclosure of process memory
Description: An out-of-bounds read was addressed with improved input
validation.
CVE-2023-27929: Meysam Firouzi (@R00tkitSMM) of Mbition Mercedes-Benz
Innovation Lab and jzhu working with Trend Micro Zero Day Initiative

ImageIO
Available for: macOS Ventura
Impact: Processing a maliciously crafted file may lead to unexpected
app termination or arbitrary code execution
Description: An out-of-bounds read was addressed with improved bounds
checking.
CVE-2023-27946: Mickey Jin (@patch1t)

ImageIO
Available for: macOS Ventura
Impact: Processing a maliciously crafted file may lead to unexpected
app termination or arbitrary code execution
Description: A buffer overflow issue was addressed with improved
memory handling.
CVE-2023-27957: Yiğit Can YILMAZ (@yilmazcanyigit)

Kernel
Available for: macOS Ventura
Impact: An app may be able t...