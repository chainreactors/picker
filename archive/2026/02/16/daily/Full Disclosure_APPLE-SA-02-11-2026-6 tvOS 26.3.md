---
title: APPLE-SA-02-11-2026-6 tvOS 26.3
url: https://seclists.org/fulldisclosure/2026/Feb/26
source: Full Disclosure
date: 2026-02-16
fetch_date: 2026-02-17T04:21:55.856925
---

# APPLE-SA-02-11-2026-6 tvOS 26.3

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

[![Previous](/images/left-icon-16x16.png)](25)
[By Date](date.html#26)
[![Next](/images/right-icon-16x16.png)](27)

[![Previous](/images/left-icon-16x16.png)](25)
[By Thread](index.html#26)
[![Next](/images/right-icon-16x16.png)](27)

![](/shared/images/nst-icons.svg#search)

# APPLE-SA-02-11-2026-6 tvOS 26.3

---

*From*: Apple Product Security via Fulldisclosure <fulldisclosure () seclists org>
*Date*: Wed, 11 Feb 2026 16:05:31 -0800

---

```
-----BEGIN PGP SIGNED MESSAGE-----
Hash: SHA256

APPLE-SA-02-11-2026-6 tvOS 26.3

tvOS 26.3 addresses the following issues.
Information about the security content is also available at
https://support.apple.com/126351.

Apple maintains a Security Releases page at
https://support.apple.com/100100 which lists recent
software updates with security advisories.

Bluetooth
Available for: Apple TV HD and Apple TV 4K (all models)
Impact: An attacker in a privileged network position may be able to
perform denial-of-service attack using crafted Bluetooth packets
Description: A denial-of-service issue was addressed with improved
validation.
CVE-2026-20650: jioundai

CoreAudio
Available for: Apple TV HD and Apple TV 4K (all models)
Impact: Processing a maliciously crafted media file may lead to
unexpected app termination or corrupt process memory
Description: An out-of-bounds access issue was addressed with improved
bounds checking.
CVE-2026-20611: Anonymous working with Trend Micro Zero Day Initiative

CoreMedia
Available for: Apple TV HD and Apple TV 4K (all models)
Impact: Processing a maliciously crafted file may lead to a denial-of-
service or potentially disclose memory contents
Description: The issue was addressed with improved memory handling.
CVE-2026-20609: Yiğit Can YILMAZ (@yilmazcanyigit)

CoreServices
Available for: Apple TV HD and Apple TV 4K (all models)
Impact: An app may be able to gain root privileges
Description: A race condition was addressed with improved state
handling.
CVE-2026-20617: Gergely Kalman (@gergely_kalman), Csaba Fitzl
(@theevilbit) of Iru

dyld
Available for: Apple TV HD and Apple TV 4K (all models)
Impact: An attacker with memory write capability may be able to execute
arbitrary code. Apple is aware of a report that this issue may have been
exploited in an extremely sophisticated attack against specific targeted
individuals on versions of iOS before iOS 26. CVE-2025-14174 and
CVE-2025-43529 were also issued in response to this report.
Description: A memory corruption issue was addressed with improved state
management.
CVE-2026-20700: Google Threat Analysis Group

Game Center
Available for: Apple TV HD and Apple TV 4K (all models)
Impact: A user may be able to view sensitive user information
Description: A logging issue was addressed with improved data redaction.
CVE-2026-20649: Asaf Cohen

ImageIO
Available for: Apple TV HD and Apple TV 4K (all models)
Impact: Processing a maliciously crafted image may lead to disclosure of
user information
Description: The issue was addressed with improved bounds checks.
CVE-2026-20675: George Karchemsky (@gkarchemsky) working with Trend
Micro Zero Day Initiative

ImageIO
Available for: Apple TV HD and Apple TV 4K (all models)
Impact: Processing a maliciously crafted image may result in disclosure
of process memory
Description: The issue was addressed with improved memory handling.
CVE-2026-20634: George Karchemsky (@gkarchemsky) working with Trend
Micro Zero Day Initiative

Kernel
Available for: Apple TV HD and Apple TV 4K (all models)
Impact: An app may be able to cause unexpected system termination
Description: The issue was addressed with improved memory handling.
CVE-2026-20654: Jian Lee (@speedyfriend433)

Kernel
Available for: Apple TV HD and Apple TV 4K (all models)
Impact: An attacker in a privileged network position may be able to
intercept network traffic
Description: A logic issue was addressed with improved checks.
CVE-2026-20671: Xin'an Zhou, Juefei Pu, Zhutian Liu, Zhiyun Qian,
Zhaowei Tan, Srikanth V. Krishnamurthy, Mathy Vanhoef

libexpat
Available for: Apple TV HD and Apple TV 4K (all models)
Impact: Processing a maliciously crafted file may lead to a denial-of-
service
Description: This is a vulnerability in open source code and Apple
Software is among the affected projects. The CVE-ID was assigned by a
third party. Learn more about the issue and CVE-ID at cve.org.
CVE-2025-59375

Sandbox
Available for: Apple TV HD and Apple TV 4K (all models)
Impact: An app may be able to break out of its sandbox
Description: A permissions issue was addressed with additional
restrictions.
CVE-2026-20628: Noah Gregory (wts.dev)

StoreKit
Available for: Apple TV HD and Apple TV 4K (all models)
Impact: An app may be able to identify what other apps a user has
installed
Description: A privacy issue was addressed with improved checks.
CVE-2026-20641: Gongyu Ma (@Mezone0)

WebKit
Available for: Apple TV HD and Apple TV 4K (all models)
Impact: Processing maliciously crafted web content may lead to an
unexpected process crash
Description: The issue was addressed with improved memory handling.
WebKit Bugzilla: 304661
CVE-2026-20635: EntryHi

Additional recognition

Bluetooth
We would like to acknowledge Tommaso Sacchetti for their assistance.

Kernel
We would like to acknowledge Joseph Ravichandran (@0xjprx) of MIT CSAIL,
Xinru Chi of Pangu Lab for their assistance.

libpthread
We would like to acknowledge Fabiano Anemone for their assistance.

NetworkExtension
We would like to acknowledge Gongyu Ma (@Mezone0) for their assistance.

Transparency
We would like to acknowledge Wojciech Regula of SecuRing
(wojciechregula.blog) for their assistance.

WebKit
We would like to acknowledge EntryHi, Luigino Camastra of Aisle
Research, Stanislav Fort of Aisle Research, Vsevolod Kokorin (Slonser)
of Solidlab and Jorian Woltjer for their assistance.

Apple TV will periodically check for software updates. Alternatively,
you may manually check for software updates by selecting
"Settings -> System -> Software Update -> Update Software."

To check the current version of software, select
"Settings -> General -> About."

All information is also posted on the Apple Security Releases
web site: https://support.apple.com/100100.

This message is signed with Apple's Product Security PGP key,
and details are available at:
https://www.apple.com/support/security/pgp/

-----BEGIN PGP SIGNATURE-----

iQIzBAEBCAAdFiEEhjkl+zMLNwFiCT1o4Ifiq8DH7PUFAmmND34ACgkQ4Ifiq8DH
7PXkdw/+IYFGSM8OHYakv+/rUPa38gqgKMWw+P0sXf6UatkBUSnvFVA1rttE5L/r
4DdPRcGBRrzgr8MuugxATYIezQly9AE/4qJfgPPS6er+CqINIOZLfHu89Xs3Dvbe
dvHjLeyMfsaklOK2VJE6WY0nMfe+PJILfbq+zwdfFs+l76rWe+qcXCDCRwnVkG6+
afBCdCF0HLNe3rZtX6/RjTsYXLGZxstKPp5Xihnu211TXZAKOtxHIP8IeoNagHkW
NvwJuHbmVJ7KVi7uz4lva4uyzqU7xiW8ktf6ScizSJMQq6y4Oxl+XHWJC3CmHAaA
mG0fQ9IDQUPD16Bj1w0JIkTPPS96R0WnOFGjnRMm6PbTeOZy3Y/6wT2wjS6oW7zN
h4cijWc5nDbXaXLwpjWazzgiFNCpLV2y5AAJNHxMtOFFO8Cm1IrzstPipuyN05/p
WPRE3w1Jn0ls6hzi7zWrZpb8eOhbC4sBBPCtTWHaLlRgM3mqyE1F449OKgRk5cLt
NBSD0xyMoDQ9JMsS3naHBNqIy5iLYSQPTbdm29HSl+P3DyU8NEUpbKFEVdMxo5iG
kp+ClWnHweMkAnwdMCR1jniq+Ni9O7g1AuU0uhMJbH9dh2INXQBy8ITB1L1xG3Xt
tiC5COVRQYdaKW1ADXTfejB2Z1F1zWioLbtxdc40eKYtKoWLSnk=
=mQcE
-----END PGP SIGNATURE-----

_______________________________________________
Sent through the Full Disclosure mailing list
https://nmap.org/mailman/listinfo/fulldisclosure
Web Archives & RSS: https://seclists.org/fulldisclosure/
```

---

[![Previous](/images/left-icon-16x16.png)](25)
[By Date](date.html#26)
[![Next](/images/right-icon-16x16.png)]...