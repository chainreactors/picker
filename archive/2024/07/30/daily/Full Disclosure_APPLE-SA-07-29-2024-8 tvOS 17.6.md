---
title: APPLE-SA-07-29-2024-8 tvOS 17.6
url: https://seclists.org/fulldisclosure/2024/Jul/22
source: Full Disclosure
date: 2024-07-30
fetch_date: 2025-10-06T17:47:02.405204
---

# APPLE-SA-07-29-2024-8 tvOS 17.6

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

[![Previous](/images/left-icon-16x16.png)](21)
[By Date](date.html#22)
[![Next](/images/right-icon-16x16.png)](23)

[![Previous](/images/left-icon-16x16.png)](21)
[By Thread](index.html#22)
[![Next](/images/right-icon-16x16.png)](23)

![](/shared/images/nst-icons.svg#search)

# APPLE-SA-07-29-2024-8 tvOS 17.6

---

*From*: Apple Product Security via Fulldisclosure <fulldisclosure () seclists org>
*Date*: Mon, 29 Jul 2024 16:14:31 -0700

---

```
-----BEGIN PGP SIGNED MESSAGE-----
Hash: SHA256

APPLE-SA-07-29-2024-8 tvOS 17.6

tvOS 17.6 addresses the following issues.
Information about the security content is also available at
https://support.apple.com/HT214122.

Apple maintains a Security Releases page at
https://support.apple.com/HT201222 which lists recent
software updates with security advisories.

AppleMobileFileIntegrity
Available for: Apple TV HD and Apple TV 4K (all models)
Impact: An app may be able to bypass Privacy preferences
Description: A downgrade issue was addressed with additional code-
signing restrictions.
CVE-2024-40774: Mickey Jin (@patch1t)

CoreGraphics
Available for: Apple TV HD and Apple TV 4K (all models)
Impact: Processing a maliciously crafted file may lead to unexpected app
termination
Description: An out-of-bounds read issue was addressed with improved
input validation.
CVE-2024-40799: D4m0n

dyld
Available for: Apple TV HD and Apple TV 4K (all models)
Impact: A malicious attacker with arbitrary read and write capability
may be able to bypass Pointer Authentication
Description: A race condition was addressed with additional validation.
CVE-2024-40815: w0wbox

Family Sharing
Available for: Apple TV HD and Apple TV 4K (all models)
Impact: An app may be able to read sensitive location information
Description: This issue was addressed with improved data protection.
CVE-2024-40795: Csaba Fitzl (@theevilbit) of Kandji

ImageIO
Available for: Apple TV HD and Apple TV 4K (all models)
Impact: Processing an image may lead to a denial-of-service
Description: This is a vulnerability in open source code and Apple
Software is among the affected projects. The CVE-ID was assigned by a
third party. Learn more about the issue and CVE-ID at cve.org.
CVE-2023-6277
CVE-2023-52356

ImageIO
Available for: Apple TV HD and Apple TV 4K (all models)
Impact: Processing a maliciously crafted file may lead to unexpected app
termination
Description: An out-of-bounds read issue was addressed with improved
input validation.
CVE-2024-40806: Yisumi

ImageIO
Available for: Apple TV HD and Apple TV 4K (all models)
Impact: Processing a maliciously crafted file may lead to unexpected app
termination
Description: An out-of-bounds access issue was addressed with improved
bounds checking.
CVE-2024-40777: Junsung Lee working with Trend Micro Zero Day
Initiative, and Amir Bazine and Karsten KÃ¶nig of CrowdStrike Counter
Adversary Operations

ImageIO
Available for: Apple TV HD and Apple TV 4K (all models)
Impact: Processing a maliciously crafted file may lead to unexpected app
termination
Description: An integer overflow was addressed with improved input
validation.
CVE-2024-40784: Junsung Lee working with Trend Micro Zero Day Initiative
and Gandalf4a

Kernel
Available for: Apple TV HD and Apple TV 4K (all models)
Impact: A local attacker may be able to determine kernel memory layout
Description: An information disclosure issue was addressed with improved
private data redaction for log entries.
CVE-2024-27863: CertiK SkyFall Team

Kernel
Available for: Apple TV HD and Apple TV 4K (all models)
Impact: A local attacker may be able to cause unexpected system shutdown
Description: A type confusion issue was addressed with improved memory
handling.
CVE-2024-40788: Minghao Lin and Jiaxun Zhu from Zhejiang University

libxpc
Available for: Apple TV HD and Apple TV 4K (all models)
Impact: An app may be able to bypass Privacy preferences
Description: A permissions issue was addressed with additional
restrictions.
CVE-2024-40805

Sandbox
Available for: Apple TV HD and Apple TV 4K (all models)
Impact: An app may be able to bypass Privacy preferences
Description: This issue was addressed through improved state management.
CVE-2024-40824: Wojciech Regula of SecuRing (wojciechregula.blog) and
Zhongquan Li (@Guluisacat) from Dawn Security Lab of JingDong

WebKit
Available for: Apple TV HD and Apple TV 4K (all models)
Impact: Processing maliciously crafted web content may lead to an
unexpected process crash
Description: A use-after-free issue was addressed with improved memory
management.
WebKit Bugzilla: 273176
CVE-2024-40776: Huang Xilin of Ant Group Light-Year Security Lab
WebKit Bugzilla: 268770
CVE-2024-40782: Maksymilian Motyl

WebKit
Available for: Apple TV HD and Apple TV 4K (all models)
Impact: Processing maliciously crafted web content may lead to an
unexpected process crash
Description: An out-of-bounds read was addressed with improved bounds
checking.
WebKit Bugzilla: 275431
CVE-2024-40779: Huang Xilin of Ant Group Light-Year Security Lab
WebKit Bugzilla: 275273
CVE-2024-40780: Huang Xilin of Ant Group Light-Year Security Lab

WebKit
Available for: Apple TV HD and Apple TV 4K (all models)
Impact: Processing maliciously crafted web content may lead to a cross
site scripting attack
Description: This issue was addressed with improved checks.
WebKit Bugzilla: 273805
CVE-2024-40785: Johan Carlsson (joaxcar)

WebKit
Available for: Apple TV HD and Apple TV 4K (all models)
Impact: Processing maliciously crafted web content may lead to an
unexpected process crash
Description: An out-of-bounds access issue was addressed with improved
bounds checking.
CVE-2024-40789: Seunghyun Lee (@0x10n) of KAIST Hacking Lab working with
Trend Micro Zero Day Initiative

Apple TV will periodically check for software updates. Alternatively,
you may manually check for software updates by selecting "Settings ->
System -> Software Update -> Update Software."  To check the current
version of software, select "Settings -> General -> About."
All information is also posted on the Apple Security Releases
web site: https://support.apple.com/HT201222.

This message is signed with Apple's Product Security PGP key,
and details are available at:
https://www.apple.com/support/security/pgp/
-----BEGIN PGP SIGNATURE-----

iQIzBAEBCAAdFiEEsz9altA7uTI+rE/qX+5d1TXaIvoFAmaoIFQACgkQX+5d1TXa
IvrqRg/+Klv/Cy1M7Ii5T/jTDQ9ggrY36CjR6GJaFwXMlC++eNYidc9LeVNU72PI
F7GpQ6ZntYJZzEm1YGUOjkU38IYid5lnfDQHsfTTm8Pzmk+1vbcLDYEfsoeGK81F
7qcirUzseRYBmvbei2X2HqiGh/bLJgHUb433lDPQcVIUNmvdYuGtaDYNnbhOJ80u
+LET8E2GjIVWY15ZtSHC59OctUPtI6l6HrncqLTjXegePCqLC2Z4BIGmnPoyOGSf
zTgFXSfekwZ/5y6PKPhDu+NgrrCI+IhP20mO0pj2IhQgd56yEdF6P7dYrWlElQmi
/MoMZTzfxQPBzHxcfmG4ANqMSJzE3oZ737r32o4dwsdIiBJ9JG+UV9722kk+CH+7
NKN1GBxf05kEXXJ+Y4c9VyCMQVxW9RaPQic89WoWA7JQsrmah8osHFnxTxL4d12X
cR5JohihgI+EE4N+MqlT/CKE+0r/Oy6yalRCJQugA1fBQiIa57twRK3+sGQUqtn0
fI2PmXTkF47pm9ed7foE+XtknEerfvGruWH3SUAKo46Q3yUGvR1cQ4v1lzXG51AR
+6rV79CKWRztAqXS6uermURsTBcUDnnHH+9HH+2kLOyNuQ/F6Th1Ng1CUWrMJeSf
eE1sp6m+eR3uuUPwfEPZwJxhlUlZj4kaQE8gipr3DBrZFCJY6To=
=prdc
-----END PGP SIGNATURE-----
_______________________________________________
Sent through the Full Disclosure mailing list
https://nmap.org/mailman/listinfo/fulldisclosure
Web Archives & RSS: https://seclists.org/fulldisclosure/
```

---

[![Previous](/images/left-icon-16x16.png)](21)
[By Date](date.html#22)
[![Next](/images/right-icon-16x16.png)](23)

[![Previous](/images/left-icon-16x16.png)](21)
[By Thread](index.html#22)
[![Next](/images/right-icon-1...