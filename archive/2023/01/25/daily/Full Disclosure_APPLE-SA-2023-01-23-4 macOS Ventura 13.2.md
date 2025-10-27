---
title: APPLE-SA-2023-01-23-4 macOS Ventura 13.2
url: https://seclists.org/fulldisclosure/2023/Jan/19
source: Full Disclosure
date: 2023-01-25
fetch_date: 2025-10-04T04:48:36.967659
---

# APPLE-SA-2023-01-23-4 macOS Ventura 13.2

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
[By Date](date.html#19)
[![Next](/images/right-icon-16x16.png)](20)

[![Previous](/images/left-icon-16x16.png)](17)
[By Thread](index.html#19)
[![Next](/images/right-icon-16x16.png)](20)

![](/shared/images/nst-icons.svg#search)

# APPLE-SA-2023-01-23-4 macOS Ventura 13.2

---

*From*: Apple Product Security via Fulldisclosure <fulldisclosure () seclists org>
*Date*: Mon, 23 Jan 2023 18:40:48 -0800

---

```
-----BEGIN PGP SIGNED MESSAGE-----
Hash: SHA256

APPLE-SA-2023-01-23-4 macOS Ventura 13.2

macOS Ventura 13.2 addresses the following issues.
Information about the security content is also available at
https://support.apple.com/HT213605.

AppleMobileFileIntegrity
Available for: macOS Ventura
Impact: An app may be able to access user-sensitive data
Description: This issue was addressed by enabling hardened runtime.
CVE-2023-23499: Wojciech Reguła (@_r3ggi) of SecuRing
(wojciechregula.blog)

curl
Available for: macOS Ventura
Impact: Multiple issues in curl
Description: Multiple issues were addressed by updating to curl
version 7.86.0.
CVE-2022-42915
CVE-2022-42916
CVE-2022-32221
CVE-2022-35260

dcerpc
Available for: macOS Ventura
Impact: Mounting a maliciously crafted Samba network share may lead
to arbitrary code execution
Description: A buffer overflow issue was addressed with improved
memory handling.
CVE-2023-23513: Dimitrios Tatsis and Aleksandar Nikolic of Cisco
Talos

DiskArbitration
Available for: macOS Ventura
Impact: An encrypted volume may be unmounted and remounted by a
different user without prompting for the password
Description: A logic issue was addressed with improved state
management.
CVE-2023-23493: Oliver Norpoth (@norpoth) of KLIXX GmbH (klixx.com)

ImageIO
Available for: macOS Ventura
Impact: Processing an image may lead to a denial-of-service
Description: A memory corruption issue was addressed with improved
state management.
CVE-2023-23519: Yiğit Can YILMAZ (@yilmazcanyigit)

Intel Graphics Driver
Available for: macOS Ventura
Impact: An app may be able to execute arbitrary code with kernel
privileges
Description: The issue was addressed with improved bounds checks.
CVE-2023-23507: an anonymous researcher

Kernel
Available for: macOS Ventura
Impact: An app may be able to leak sensitive kernel state
Description: The issue was addressed with improved memory handling.
CVE-2023-23500: Pan ZhenPeng (@Peterpan0927) of STAR Labs SG Pte.
Ltd. (@starlabs_sg)

Kernel
Available for: macOS Ventura
Impact: An app may be able to determine kernel memory layout
Description: An information disclosure issue was addressed by
removing the vulnerable code.
CVE-2023-23502: Pan ZhenPeng (@Peterpan0927) of STAR Labs SG Pte.
Ltd. (@starlabs_sg)

Kernel
Available for: macOS Ventura
Impact: An app may be able to execute arbitrary code with kernel
privileges
Description: The issue was addressed with improved memory handling.
CVE-2023-23504: Adam Doupé of ASU SEFCOM

libxpc
Available for: macOS Ventura
Impact: An app may be able to access user-sensitive data
Description: A permissions issue was addressed with improved
validation.
CVE-2023-23506: Guilherme Rambo of Best Buddy Apps (rambo.codes)

Mail Drafts
Available for: macOS Ventura
Impact: The quoted original message may be selected from the wrong
email when forwarding an email from an Exchange account
Description: A logic issue was addressed with improved state
management.
CVE-2023-23498: an anonymous researcher

Maps
Available for: macOS Ventura
Impact: An app may be able to bypass Privacy preferences
Description: A logic issue was addressed with improved state
management.
CVE-2023-23503: an anonymous researcher

PackageKit
Available for: macOS Ventura
Impact: An app may be able to gain root privileges
Description: A logic issue was addressed with improved state
management.
CVE-2023-23497: Mickey Jin (@patch1t)

Safari
Available for: macOS Ventura
Impact: An app may be able to access a user’s Safari history
Description: A permissions issue was addressed with improved
validation.
CVE-2023-23510: Guilherme Rambo of Best Buddy Apps (rambo.codes)

Safari
Available for: macOS Ventura
Impact: Visiting a website may lead to an app denial-of-service
Description: The issue was addressed with improved handling of
caches.
CVE-2023-23512: Adriatik Raci

Screen Time
Available for: macOS Ventura
Impact: An app may be able to access information about a user’s
contacts
Description: A privacy issue was addressed with improved private data
redaction for log entries.
CVE-2023-23505: Wojciech Reguła of SecuRing (wojciechregula.blog)

Vim
Available for: macOS Ventura
Impact: Multiple issues in Vim
Description: A use after free issue was addressed with improved
memory management.
CVE-2022-3705

Weather
Available for: macOS Ventura
Impact: An app may be able to bypass Privacy preferences
Description: The issue was addressed with improved memory handling.
CVE-2023-23511: Wojciech Regula of SecuRing (wojciechregula.blog), an
anonymous researcher

WebKit
Available for: macOS Ventura
Impact: Processing maliciously crafted web content may lead to
arbitrary code execution
Description: The issue was addressed with improved checks.
WebKit Bugzilla: 245464
CVE-2023-23496: ChengGang Wu, Yan Kang, YuHao Hu, Yue Sun, Jiming
Wang, JiKai Ren and Hang Shu of Institute of Computing Technology,
Chinese Academy of Sciences

WebKit
Available for: macOS Ventura
Impact: Processing maliciously crafted web content may lead to
arbitrary code execution
Description: The issue was addressed with improved memory handling.
WebKit Bugzilla: 248268
CVE-2023-23518: YeongHyeon Choi (@hyeon101010), Hyeon Park
(@tree_segment), SeOk JEON (@_seokjeon), YoungSung Ahn (@_ZeroSung),
JunSeo Bae (@snakebjs0107), Dohyun Lee (@l33d0hyun) of Team ApplePIE
WebKit Bugzilla: 248268
CVE-2023-23517: YeongHyeon Choi (@hyeon101010), Hyeon Park
(@tree_segment), SeOk JEON (@_seokjeon), YoungSung Ahn (@_ZeroSung),
JunSeo Bae (@snakebjs0107), Dohyun Lee (@l33d0hyun) of Team ApplePIE

Wi-Fi
Available for: macOS Ventura
Impact: An app may be able to disclose kernel memory
Description: The issue was addressed with improved memory handling.
CVE-2023-23501: Pan ZhenPeng (@Peterpan0927) of STAR Labs SG Pte.
Ltd. (@starlabs_sg)

Windows Installer
Available for: macOS Ventura
Impact: An app may be able to bypass Privacy preferences
Description: The issue was addressed with improved memory handling.
CVE-2023-23508: Mickey Jin (@patch1t)

Additional recognition

Bluetooth
We would like to acknowledge an anonymous researcher for their
assistance.

Kernel
We would like to acknowledge Nick Stenning of Replicate for their
assistance.

Shortcuts
We would like to acknowledge Baibhav Anand Jha from ReconWithMe and
Cristian Dinca of Tudor Vianu National High School of Computer
Science, Romania for their assistance.

WebKit
We would like to acknowledge Eliya Stein of Confiant for their
assistance.

macOS Ventura 13.2 may be obtained from the Mac App Store or Apple's
Software Downloads web site: https://support.apple.com/downloads/
All information is also posted on the Apple Security Updates
web site: https://support.apple.com/en-us/HT201222.

This message is signed with Apple's Product Security PGP key,
and details are available at:
https://www.apple.com/support/security/pgp/
-----BEGIN PGP SIGNATURE-----

iQIzBAEBCAAdFiEEBP+4DupqR5Sgt1DB4RjMIDkeNxkFAmPPIl8ACgkQ4RjMIDke
Nxnt7RAA2a0c/Ij93MfR8eiNMkIHVnr+wL+4rckVmHvs85dSHNBqQ8+kYpAs2tEk
7CVZoxAGg8LqVa6ZmBbAp5ZJGi2nV8Lj...