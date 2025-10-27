---
title: APPLE-SA-2023-03-27-5 macOS Big Sur 11.7.5
url: https://seclists.org/fulldisclosure/2023/Mar/21
source: Full Disclosure
date: 2023-03-29
fetch_date: 2025-10-04T11:03:23.982404
---

# APPLE-SA-2023-03-27-5 macOS Big Sur 11.7.5

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

[![Previous](/images/left-icon-16x16.png)](20)
[By Date](date.html#21)
[![Next](/images/right-icon-16x16.png)](22)

[![Previous](/images/left-icon-16x16.png)](20)
[By Thread](index.html#21)
[![Next](/images/right-icon-16x16.png)](22)

![](/shared/images/nst-icons.svg#search)

# APPLE-SA-2023-03-27-5 macOS Big Sur 11.7.5

---

*From*: Apple Product Security via Fulldisclosure <fulldisclosure () seclists org>
*Date*: Mon, 27 Mar 2023 16:08:33 -0700

---

```
-----BEGIN PGP SIGNED MESSAGE-----
Hash: SHA256

APPLE-SA-2023-03-27-5 macOS Big Sur 11.7.5

macOS Big Sur 11.7.5 addresses the following issues.
Information about the security content is also available at
https://support.apple.com/HT213675.

Apple Neural Engine
Available for: macOS Big Sur
Impact: An app may be able to execute arbitrary code with kernel
privileges
Description: The issue was addressed with improved memory handling.
CVE-2023-23540: Mohamed GHANNAM (@_simo36)

AppleAVD
Available for: macOS Big Sur
Impact: An application may be able to execute arbitrary code with
kernel privileges
Description: A use after free issue was addressed with improved
memory management.
CVE-2022-26702: an anonymous researcher, Antonio Zekic
(@antoniozekic), and John Aakerblom (@jaakerblom)

AppleMobileFileIntegrity
Available for: macOS Big Sur
Impact: A user may gain access to protected parts of the file system
Description: The issue was addressed with improved checks.
CVE-2023-23527: Mickey Jin (@patch1t)

Archive Utility
Available for: macOS Big Sur
Impact: An archive may be able to bypass Gatekeeper
Description: The issue was addressed with improved checks.
CVE-2023-27951: Brandon Dalton of Red Canary and Csaba Fitzl
(@theevilbit) of Offensive Security

Calendar
Available for: macOS Big Sur
Impact: Importing a maliciously crafted calendar invitation may
exfiltrate user information
Description: Multiple validation issues were addressed with improved
input sanitization.
CVE-2023-27961: Rıza Sabuncu (@rizasabuncu)

Carbon Core
Available for: macOS Big Sur
Impact: Processing a maliciously crafted image may result in
disclosure of process memory
Description: The issue was addressed with improved checks.
CVE-2023-23534: Mickey Jin (@patch1t)

ColorSync
Available for: macOS Big Sur
Impact: An app may be able to read arbitrary files
Description: The issue was addressed with improved checks.
CVE-2023-27955: JeongOhKyea

CommCenter
Available for: macOS Big Sur
Impact: An app may be able to cause unexpected system termination or
write kernel memory
Description: An out-of-bounds write issue was addressed with improved
input validation.
CVE-2023-27936: Tingting Yin of Tsinghua University

dcerpc
Available for: macOS Big Sur
Impact: A remote user may be able to cause unexpected app termination
or arbitrary code execution
Description: The issue was addressed with improved bounds checks.
CVE-2023-27935: Aleksandar Nikolic of Cisco Talos

dcerpc
Available for: macOS Big Sur
Impact: A remote user may be able to cause unexpected system
termination or corrupt kernel memory
Description: The issue was addressed with improved memory handling.
CVE-2023-27953: Aleksandar Nikolic of Cisco Talos
CVE-2023-27958: Aleksandar Nikolic of Cisco Talos

Find My
Available for: macOS Big Sur
Impact: An app may be able to read sensitive location information
Description: A privacy issue was addressed with improved private data
redaction for log entries.
CVE-2023-23537: an anonymous researcher

Foundation
Available for: macOS Big Sur
Impact: Parsing a maliciously crafted plist may lead to an unexpected
app termination or arbitrary code execution
Description: An integer overflow was addressed with improved input
validation.
CVE-2023-27937: an anonymous researcher

Identity Services
Available for: macOS Big Sur
Impact: An app may be able to access information about a user’s
contacts
Description: A privacy issue was addressed with improved private data
redaction for log entries.
CVE-2023-27928: Csaba Fitzl (@theevilbit) of Offensive Security

ImageIO
Available for: macOS Big Sur
Impact: Processing a maliciously crafted file may lead to unexpected
app termination or arbitrary code execution
Description: An out-of-bounds read was addressed with improved bounds
checking.
CVE-2023-27946: Mickey Jin (@patch1t)

ImageIO
Available for: macOS Big Sur
Impact: Processing a maliciously crafted image may result in
disclosure of process memory
Description: The issue was addressed with improved memory handling.
CVE-2023-23535: ryuzaki

Kernel
Available for: macOS Big Sur
Impact: An app may be able to execute arbitrary code with kernel
privileges
Description: A use after free issue was addressed with improved
memory management.
CVE-2023-23514: Xinru Chi of Pangu Lab and Ned Williamson of Google
Project Zero

Kernel
Available for: macOS Big Sur
Impact: An app may be able to disclose kernel memory
Description: A validation issue was addressed with improved input
sanitization.
CVE-2023-28200: Arsenii Kostromin (0x3c3e)

NetworkExtension
Available for: macOS Big Sur
Impact: A user in a privileged network position may be able to spoof
a VPN server that is configured with EAP-only authentication on a
device
Description: The issue was addressed with improved authentication.
CVE-2023-28182: Zhuowei Zhang

PackageKit
Available for: macOS Big Sur
Impact: An app may be able to modify protected parts of the file
system
Description: A logic issue was addressed with improved checks.
CVE-2023-27962: Mickey Jin (@patch1t)

System Settings
Available for: macOS Big Sur
Impact: An app may be able to access user-sensitive data
Description: A privacy issue was addressed with improved private data
redaction for log entries.
CVE-2023-23542: an anonymous researcher

System Settings
Available for: macOS Big Sur
Impact: An app may be able to read sensitive location information
Description: A permissions issue was addressed with improved
validation.
CVE-2023-28192: Guilherme Rambo of Best Buddy Apps (rambo.codes)

Vim
Available for: macOS Big Sur
Impact: Multiple issues in Vim
Description: Multiple issues were addressed by updating to Vim
version 9.0.1191.
CVE-2023-0433
CVE-2023-0512

XPC
Available for: macOS Big Sur
Impact: An app may be able to break out of its sandbox
Description: This issue was addressed with a new entitlement.
CVE-2023-27944: Mickey Jin (@patch1t)

Additional recognition

Activation Lock
We would like to acknowledge Christian Mina for their assistance.

AppleMobileFileIntegrity
We would like to acknowledge Wojciech Reguła (@_r3ggi) of SecuRing
(wojciechregula.blog) for their assistance.

CoreServices
We would like to acknowledge Mickey Jin (@patch1t) for their
assistance.

NSOpenPanel
We would like to acknowledge Alexandre Colucci (@timacfr) for their
assistance.

Wi-Fi
We would like to acknowledge an anonymous researcher for their
assistance.

macOS Big Sur 11.7.5 may be obtained from the Mac App Store or
Apple's Software Downloads web site:
https://support.apple.com/downloads/
All information is also posted on the Apple Security Updates
web site: https://support.apple.com/en-us/HT201222.

This message is signed with Apple's Product Security PGP key,
and details are available at:
https://www.apple.com/support/security/pgp/
-----BEGIN PGP SIGNATURE-----

iQIzBAEBCAAdFiEEBP+4DupqR5Sgt1DB4RjMIDkeNxkFAmQiHnwACgkQ4RjMIDke
Nxks0hAAquqDdtX6QvjVigRuSd2bpQny1TxVp62Zo47F9YkrvuvKVvJjaFzQJNjE
p2Oq3BgNBkUqei26w8GLqwbg8szhCIPCOVHFcGDTPGrf53oWLlPc6WZxn8ihZOo4
r3rxH4MGFSb+dBwWnF6GVX1EBcVjO08FwOzgNqk...