---
title: APPLE-SA-07-29-2024-9 visionOS 1.3
url: https://seclists.org/fulldisclosure/2024/Jul/23
source: Full Disclosure
date: 2024-07-30
fetch_date: 2025-10-06T17:47:01.083634
---

# APPLE-SA-07-29-2024-9 visionOS 1.3

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

[![Previous](/images/left-icon-16x16.png)](22)
[By Date](date.html#23)
![Next](/images/right-icon-16x16.png)

[![Previous](/images/left-icon-16x16.png)](22)
[By Thread](index.html#23)
![Next](/images/right-icon-16x16.png)

![](/shared/images/nst-icons.svg#search)

# APPLE-SA-07-29-2024-9 visionOS 1.3

---

*From*: Apple Product Security via Fulldisclosure <fulldisclosure () seclists org>
*Date*: Mon, 29 Jul 2024 16:15:55 -0700

---

```
-----BEGIN PGP SIGNED MESSAGE-----
Hash: SHA256

APPLE-SA-07-29-2024-9 visionOS 1.3

visionOS 1.3 addresses the following issues.
Information about the security content is also available at
https://support.apple.com/HT214123.

Apple maintains a Security Releases page at
https://support.apple.com/HT201222 which lists recent
software updates with security advisories.

Apple Neural Engine
Available for: Apple Vision Pro
Impact: A local attacker may be able to cause unexpected system shutdown
Description: The issue was addressed with improved memory handling.
CVE-2024-27826: Ye Zhang (@VAR10CK) of Baidu Security and Minghao Lin

AppleAVD
Available for: Apple Vision Pro
Impact: An app may be able to cause unexpected system termination
Description: The issue was addressed with improved memory handling.
CVE-2024-27804: Meysam Firouzi (@R00tkitSMM)

CoreGraphics
Available for: Apple Vision Pro
Impact: Processing a maliciously crafted file may lead to unexpected app
termination
Description: An out-of-bounds read issue was addressed with improved
input validation.
CVE-2024-40799: D4m0n

ImageIO
Available for: Apple Vision Pro
Impact: Processing an image may lead to a denial-of-service
Description: This is a vulnerability in open source code and Apple
Software is among the affected projects. The CVE-ID was assigned by a
third party. Learn more about the issue and CVE-ID at cve.org.
CVE-2023-6277
CVE-2023-52356

ImageIO
Available for: Apple Vision Pro
Impact: Processing a maliciously crafted file may lead to unexpected app
termination
Description: An out-of-bounds read issue was addressed with improved
input validation.
CVE-2024-40806: Yisumi

ImageIO
Available for: Apple Vision Pro
Impact: Processing a maliciously crafted file may lead to unexpected app
termination
Description: An out-of-bounds access issue was addressed with improved
bounds checking.
CVE-2024-40777: Junsung Lee working with Trend Micro Zero Day
Initiative, and Amir Bazine and Karsten KÃ¶nig of CrowdStrike Counter
Adversary Operations

ImageIO
Available for: Apple Vision Pro
Impact: Processing a maliciously crafted file may lead to unexpected app
termination
Description: An integer overflow was addressed with improved input
validation.
CVE-2024-40784: Junsung Lee working with Trend Micro Zero Day Initiative
and Gandalf4a

Kernel
Available for: Apple Vision Pro
Impact: A local attacker may be able to determine kernel memory layout
Description: An information disclosure issue was addressed with improved
private data redaction for log entries.
CVE-2024-27863: CertiK SkyFall Team

Kernel
Available for: Apple Vision Pro
Impact: An attacker in a privileged network position may be able to
spoof network packets
Description: A race condition was addressed with improved locking.
CVE-2024-27823: Prof. Benny Pinkas of Bar-Ilan University, Prof. Amit
Klein of Hebrew University, and EP

Kernel
Available for: Apple Vision Pro
Impact: A local attacker may be able to cause unexpected system shutdown
Description: A type confusion issue was addressed with improved memory
handling.
CVE-2024-40788: Minghao Lin and Jiaxun Zhu from Zhejiang University

Shortcuts
Available for: Apple Vision Pro
Impact: A shortcut may be able to bypass Internet permission
requirements
Description: A logic issue was addressed with improved checks.
CVE-2024-40809: an anonymous researcher
CVE-2024-40812: an anonymous researcher

WebKit
Available for: Apple Vision Pro
Impact: Processing maliciously crafted web content may lead to an
unexpected process crash
Description: A use-after-free issue was addressed with improved memory
management.
WebKit Bugzilla: 273176
CVE-2024-40776: Huang Xilin of Ant Group Light-Year Security Lab
WebKit Bugzilla: 268770
CVE-2024-40782: Maksymilian Motyl

WebKit
Available for: Apple Vision Pro
Impact: Processing maliciously crafted web content may lead to an
unexpected process crash
Description: An out-of-bounds read was addressed with improved bounds
checking.
WebKit Bugzilla: 275431
CVE-2024-40779: Huang Xilin of Ant Group Light-Year Security Lab
WebKit Bugzilla: 275273
CVE-2024-40780: Huang Xilin of Ant Group Light-Year Security Lab

WebKit
Available for: Apple Vision Pro
Impact: Processing maliciously crafted web content may lead to a cross
site scripting attack
Description: This issue was addressed with improved checks.
WebKit Bugzilla: 273805
CVE-2024-40785: Johan Carlsson (joaxcar)

WebKit
Available for: Apple Vision Pro
Impact: Processing maliciously crafted web content may lead to an
unexpected process crash
Description: An out-of-bounds access issue was addressed with improved
bounds checking.
CVE-2024-40789: Seunghyun Lee (@0x10n) of KAIST Hacking Lab working with
Trend Micro Zero Day Initiative

Additional recognition

AirDrop
We would like to acknowledge Linwz of DEVCORE for their assistance.

Shortcuts
We would like to acknowledge an anonymous researcher for their
assistance.

Instructions on how to update visionOS are available at
https://support.apple.com/HT214009  To check the software version
on your Apple Vision Pro, open the Settings app and choose General >
About.
All information is also posted on the Apple Security Releases
web site: https://support.apple.com/HT201222.

This message is signed with Apple's Product Security PGP key,
and details are available at:
https://www.apple.com/support/security/pgp/
-----BEGIN PGP SIGNATURE-----

iQIzBAEBCAAdFiEEsz9altA7uTI+rE/qX+5d1TXaIvoFAmaoIKEACgkQX+5d1TXa
IvrPMhAAvJRTT2vBEmsCe8fWRLfDlgrh95ubjnuQ0VJ+dbM2MrdUXZr/bueevkhJ
K8bCqDg19hqeWStGG2FoVB0lThZOiS7BIBYyNmfKKyID25dXKUUGVSluLTATOFCs
YVruEya71fuY4JAFI6c6S2rCfbTDLS0/8Iq72LQX/umUo5DD9YX/fBgKA7ji6KML
49cOpRpT6xG2OYEFG+GQw4p8/ha4Dg1QSPhSgYs1n0iwv2Al5siedmhxT+j8Xnof
O0Wo54q+e7lIMTQaj8SLKh2zysYpHGNREaUIfGKCyr0FuJCEkWdGNaMlNeqI602z
CYVnLLr3H0tcOGSQtmlUodPQEjunGs3j1AUkZuezagHZzqmR1Tlh4tt3tx3s0B3+
nxIoA2ejJH6no5gvaOFZmc8MgUgwL0/LO/GRm6Ow9lu9N8Bbey34s5h4bnn78/M+
W11upSvy6j2C7Nz5n6KgySSmj3sx0AGw199+MoR3iu1+3dGt332CYCIzDI/9WJTg
sdVFJD7ZLLSjt2lDD5FkJqoAy1kkTqi9eSsbOVlfYEgBvUr4zvvL8mNgx1/l6mFH
9w+rOTo1inMKLwwtPuqJQhEq0uUSY7LcAjIqUBmPWu1PENpeGIOQaSNxkL35SGkB
6lAKhD6YpkFIrwzuGMtfD9wwPC4OK48BfOV5YMNH4YLT0G4RjMQ=
=E3LP
-----END PGP SIGNATURE-----
_______________________________________________
Sent through the Full Disclosure mailing list
https://nmap.org/mailman/listinfo/fulldisclosure
Web Archives & RSS: https://seclists.org/fulldisclosure/
```

---

[![Previous](/images/left-icon-16x16.png)](22)
[By Date](date.html#23)
![Next](/images/right-icon-16x16.png)

[![Previous](/images/left-icon-16x16.png)](22)
[By Thread](index.html#23)
![Next](/images/right-icon-16x16.png)

### Current thread:

* **APPLE-SA-07-29-2024-9 visionOS 1.3** *Apple Product Security via Fulldisclosure (Jul 29)*

![](/shared/images/nst-icons.svg#search)

## [Nmap Security Scanner](https://nmap.org/)

* [Ref Guide](https://nmap.org/book/man.html)* [Install Guide](https://nmap.org/book/install.html)* [Docs](https://nmap.org/docs.html)* [Download](https://nmap.org/download.html)* [Nmap OEM](https://nmap.org/oem/)

## [Npcap packet ...