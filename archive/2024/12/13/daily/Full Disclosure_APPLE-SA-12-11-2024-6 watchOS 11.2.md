---
title: APPLE-SA-12-11-2024-6 watchOS 11.2
url: https://seclists.org/fulldisclosure/2024/Dec/10
source: Full Disclosure
date: 2024-12-13
fetch_date: 2025-10-06T19:40:48.734508
---

# APPLE-SA-12-11-2024-6 watchOS 11.2

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

[![Previous](/images/left-icon-16x16.png)](9)
[By Date](date.html#10)
[![Next](/images/right-icon-16x16.png)](11)

[![Previous](/images/left-icon-16x16.png)](9)
[By Thread](index.html#10)
[![Next](/images/right-icon-16x16.png)](11)

![](/shared/images/nst-icons.svg#search)

# APPLE-SA-12-11-2024-6 watchOS 11.2

---

*From*: Apple Product Security via Fulldisclosure <fulldisclosure () seclists org>
*Date*: Wed, 11 Dec 2024 16:38:51 -0700

---

```
-----BEGIN PGP SIGNED MESSAGE-----
Hash: SHA256

APPLE-SA-12-11-2024-6 watchOS 11.2

watchOS 11.2 addresses the following issues.
Information about the security content is also available at
https://support.apple.com/121843.

Apple maintains a Security Releases page at
https://support.apple.com/100100 which lists recent
software updates with security advisories.

AppleMobileFileIntegrity
Available for: Apple Watch Series 6 and later
Impact: A malicious app may be able to access private information
Description: The issue was addressed with improved checks.
CVE-2024-54526: Mickey Jin (@patch1t), Arsenii Kostromin (0x3c3e)

AppleMobileFileIntegrity
Available for: Apple Watch Series 6 and later
Impact: An app may be able to access sensitive user data
Description: This issue was addressed with improved checks.
CVE-2024-54527: Mickey Jin (@patch1t)

Crash Reporter
Available for: Apple Watch Series 6 and later
Impact: An app may be able to access sensitive user data
Description: A permissions issue was addressed with additional
restrictions.
CVE-2024-54513: an anonymous researcher

FontParser
Available for: Apple Watch Series 6 and later
Impact: Processing a maliciously crafted font may result in the
disclosure of process memory
Description: The issue was addressed with improved checks.
CVE-2024-54486: Hossein Lotfi (@hosselot) of Trend Micro Zero Day
Initiative

ImageIO
Available for: Apple Watch Series 6 and later
Impact: Processing a maliciously crafted image may result in disclosure
of process memory
Description: The issue was addressed with improved checks.
CVE-2024-54500: Junsung Lee working with Trend Micro Zero Day Initiative

Kernel
Available for: Apple Watch Series 6 and later
Impact: An attacker may be able to create a read-only memory mapping
that can be written to
Description: A race condition was addressed with additional validation.
CVE-2024-54494: sohybbyk

Kernel
Available for: Apple Watch Series 6 and later
Impact: An app may be able to leak sensitive kernel state
Description: A race condition was addressed with improved locking.
CVE-2024-54510: Joseph Ravichandran (@0xjprx) of MIT CSAIL

libexpat
Available for: Apple Watch Series 6 and later
Impact: A remote attacker may cause an unexpected app termination or
arbitrary code execution
Description: This is a vulnerability in open source code and Apple
Software is among the affected projects. The CVE-ID was assigned by a
third party. Learn more about the issue and CVE-ID at cve.org.
CVE-2024-45490

libxpc
Available for: Apple Watch Series 6 and later
Impact: An app may be able to break out of its sandbox
Description: The issue was addressed with improved checks.
CVE-2024-54514: an anonymous researcher

libxpc
Available for: Apple Watch Series 6 and later
Impact: An app may be able to gain elevated privileges
Description: A logic issue was addressed with improved checks.
CVE-2024-44225: 风沐云烟(@binary_fmyy)

SceneKit
Available for: Apple Watch Series 6 and later
Impact: Processing a maliciously crafted file may lead to a denial of
service
Description: The issue was addressed with improved checks.
CVE-2024-54501: Michael DePlante (@izobashi) of Trend Micro's Zero Day
Initiative

WebKit
Available for: Apple Watch Series 6 and later
Impact: Processing maliciously crafted web content may lead to an
unexpected process crash
Description: The issue was addressed with improved checks.
WebKit Bugzilla: 278497
CVE-2024-54479: Seunghyun Lee
WebKit Bugzilla: 281912
CVE-2024-54502: Brendon Tiszka of Google Project Zero

WebKit
Available for: Apple Watch Series 6 and later
Impact: Processing maliciously crafted web content may lead to an
unexpected process crash
Description: The issue was addressed with improved memory handling.
WebKit Bugzilla: 282180
CVE-2024-54508: linjy of HKUS3Lab and chluo of WHUSecLab, Xiangwei Zhang
of Tencent Security YUNDING LAB

WebKit
Available for: Apple Watch Series 6 and later
Impact: Processing maliciously crafted web content may lead to memory
corruption
Description: A type confusion issue was addressed with improved memory
handling.
WebKit Bugzilla: 282661
CVE-2024-54505: Gary Kwong

WebKit
Available for: Apple Watch Series 6 and later
Impact: Processing maliciously crafted web content may lead to memory
corruption
Description: The issue was addressed with improved memory handling.
WebKit Bugzilla: 277967
CVE-2024-54534: Tashita Software Security

Additional recognition

FaceTime
We would like to acknowledge 椰椰 for their assistance.

Proximity
We would like to acknowledge Junming C. (@Chapoly1305) and Prof. Qiang
Zeng of George Mason University for their assistance.

Swift
We would like to acknowledge Marc Schoenefeld, Dr. rer. nat. for their
assistance.

WebKit
We would like to acknowledge Hafiizh for their assistance.

Instructions on how to update your Apple Watch software are
available at https://support.apple.com/108926

To check the version on your Apple Watch, open the Apple Watch app
on your iPhone and select "My Watch > General > About".

Alternatively, on your watch, select "My Watch > General > About".

All information is also posted on the Apple Security Releases
web site: https://support.apple.com/100100.

This message is signed with Apple's Product Security PGP key,
and details are available at:
https://www.apple.com/support/security/pgp/

-----BEGIN PGP SIGNATURE-----

iQIzBAEBCAAdFiEEsz9altA7uTI+rE/qX+5d1TXaIvoFAmdaAzgACgkQX+5d1TXa
Ivq4HQ//cW3A7Y5AbUSg+0l26KE/xg9ieBywCyUBvaGmBkO/JMTObhl8JM6Pz87A
McHQ3oThl7vxIZTmrbwrlbgCZ7uSaN3Zs9wPEFewb/4UcL79BMBHRnbT7j7EwK/+
V9FAQhHsE1QnMf4vhi9rN1RGw4cmx1yaT3zsOcZZEAic3+LapI7bJI1Ro2bISiMU
uU4Qpoh+XDx/oOYitXsDQePwPklN3MlJe6mRJ6lv/vf1IHWyngzHATbW+tDv3Kng
KPW5uxVE3uB6lRCq8sJSATHYBKgnoe1elViayU9xMtjnDMnyPZL1IXiJWSXNYJ32
uN8qK//5Dy0grkXEfyaGWPR/t31MA0z/NnY2hDHhhrcXJ+0VOlAPcnVTdC//1rAn
uWSc1QGPDMQfPeLmYR8bAGUdZnYOwcSY7lTpSp+06MDzkm6KHltOL3TruwKkfq8i
KYQwPfFm1W1wDRR0xJOITjnaWOtX/oXKfqQMGtnKlSx4/94KDOEN88sdwSn//RDk
Wf5W0puH6wVNxCMiKvrOCH6TAhADgkLdept09CnAVDI0weVjmYj4qei9rzdGmPRc
JkyS128OLcs9lsp+s3GfjIK7BuwSkV2Eo/lQyAEawzIiYcFy72BGkDPIe4xvpuPn
VRyQiYElWIz1mgCZKDaSQyK/MaIDMFO6HgDLakCf4x5CROw5wYI=
=acY/
-----END PGP SIGNATURE-----

_______________________________________________
Sent through the Full Disclosure mailing list
https://nmap.org/mailman/listinfo/fulldisclosure
Web Archives & RSS: https://seclists.org/fulldisclosure/
```

---

[![Previous](/images/left-icon-16x16.png)](9)
[By Date](date.html#10)
[![Next](/images/right-icon-16x16.png)](11)

[![Previous](/images/left-icon-16x16.png)](9)
[By Thread](index.html#10)
[![Next](/images/right-icon-16x16.png)](11)

### Current thread:

* **APPLE-SA-12-11-2024-6 watchOS 11.2** *Apple Product Security via Fulldisclosure (Dec 12)*

![](/shared/images/nst-icons.svg#search)

## [Nmap Security Scanner](https://nmap.org/)

* [Ref Guide](https://nmap.org/book/man.html)* [Install Guide](https://nmap.org/book/install.html)* [Docs](https://nmap.org/docs.html)* [Download](https://nmap.org/download.html)* [Nmap OEM](https://nmap.org/oem/)

## [Npcap packet capture](https:...