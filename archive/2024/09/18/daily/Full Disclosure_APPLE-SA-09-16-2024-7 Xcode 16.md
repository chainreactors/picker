---
title: APPLE-SA-09-16-2024-7 Xcode 16
url: https://seclists.org/fulldisclosure/2024/Sep/38
source: Full Disclosure
date: 2024-09-18
fetch_date: 2025-10-06T18:30:22.056411
---

# APPLE-SA-09-16-2024-7 Xcode 16

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

[![Previous](/images/left-icon-16x16.png)](37)
[By Date](date.html#38)
[![Next](/images/right-icon-16x16.png)](39)

[![Previous](/images/left-icon-16x16.png)](37)
[By Thread](index.html#38)
[![Next](/images/right-icon-16x16.png)](39)

![](/shared/images/nst-icons.svg#search)

# APPLE-SA-09-16-2024-7 Xcode 16

---

*From*: Apple Product Security via Fulldisclosure <fulldisclosure () seclists org>
*Date*: Mon, 16 Sep 2024 18:13:18 -0700

---

```
-----BEGIN PGP SIGNED MESSAGE-----
Hash: SHA256

APPLE-SA-09-16-2024-7 Xcode 16

Xcode 16 addresses the following issues.
Information about the security content is also available at
https://support.apple.com/121239.

Apple maintains a Security Releases page at
https://support.apple.com/100100 which lists recent
software updates with security advisories.

IDE Documentation
Available for: macOS Sonoma 14.5 and later
Impact: A malicious application may gain access to a user's Keychain
items
Description: This issue was addressed by enabling hardened runtime.
CVE-2024-44162: Mickey Jin (@patch1t)

IDE Tools
Available for: macOS Sonoma 14.5 and later
Impact: An attacker may be able to determine the Apple ID of the owner
of the computer
Description: A privacy issue was addressed by removing sensitive data.
CVE-2024-40862: Guilherme Rambo of Best Buddy Apps (rambo.codes)

Kernel
Available for: macOS Sonoma 14.5 and later
Impact: An app may gain unauthorized access to Bluetooth
Description: This issue was addressed through improved state management.
CVE-2024-44191: Alexander Heinrich, SEEMOO, DistriNet, KU Leuven
(@vanhoefm), TU Darmstadt (@Sn0wfreeze) and Mathy Vanhoef

Additional recognition

Reality Composer Pro
We would like to acknowledge Ron Masas of BreakPoint.sh for their
assistance.

Swift
We would like to acknowledge Banavath Aravind for their assistance.

Xcode 16 may be obtained from:
https://developer.apple.com/xcode/downloads/  To check that the Xcode
has been updated:  * Select Xcode in the menu bar * Select About
Xcode * The version after applying this update will be "Xcode 16".

All information is also posted on the Apple Security Releases
web site: https://support.apple.com/100100.

This message is signed with Apple's Product Security PGP key,
and details are available at:
https://www.apple.com/support/security/pgp/
-----BEGIN PGP SIGNATURE-----

iQIzBAEBCAAdFiEEsz9altA7uTI+rE/qX+5d1TXaIvoFAmboyXkACgkQX+5d1TXa
IvqCRxAAg1rkAKtcgeWhSMqBPcPT8p3dpGm0gm6f5bIIJHefxwmHcNjS6GJh7Doi
g3Dv+MJiGLOa/B0fqdDlAuimxAyW5KrMKl4oXHmo0Hl0D8SHi2f+NL3JI91SmZts
rs1L4VpbR9uUJTCoXeZOXVH+LnXDN6jfUpD5+23kFJtuRBGw8a7BHRD1H0sl7yi9
sS8n6zvYujiQyS8zP1NWkpxVMaLwTqFuE4gLR7Whjod70cPkQOzUpa2pmvA/xSXQ
hpT8jhV1EVXVCGySkOmks3sdOxMg2PTTJ0l1r/hsLZSOhvbG6XyLPp1Y79uGLsnn
aZIIHdHg9DWyoy8KNbgMsyjQC5/ZMkcEQloIgdx/vH3L0WDEa+/sZObrkERAKhZi
qJneaBWmasy/I6QuoBihyo1EJhXRcDgw/7wjJaTPxJVJEAEVXMnwhz4UokvAE6CU
Jo4qH1Yi6LLbCFuSUKUzJTq6OC0kssVp6Se2WAaqIm+5+374BgW/x2diaS1eLgYo
e6db73koL1apAgP4vMvg3GUTA0/e4siZ9rAKYnRTghPWaKMX93Yeab9xHh5tNKb7
INav09fDLuGBs97oe9pBfDFajYACaGdmYDA/mtoKchMt5gkgcovysjfV51KXdz8L
dMGDYdOAtf0Lg0YkyuKEPzfYIoeTBKhWq1hZYS+ZQVULd5gkysM=
=o+oG
-----END PGP SIGNATURE-----

_______________________________________________
Sent through the Full Disclosure mailing list
https://nmap.org/mailman/listinfo/fulldisclosure
Web Archives & RSS: https://seclists.org/fulldisclosure/
```

---

[![Previous](/images/left-icon-16x16.png)](37)
[By Date](date.html#38)
[![Next](/images/right-icon-16x16.png)](39)

[![Previous](/images/left-icon-16x16.png)](37)
[By Thread](index.html#38)
[![Next](/images/right-icon-16x16.png)](39)

### Current thread:

* **APPLE-SA-09-16-2024-7 Xcode 16** *Apple Product Security via Fulldisclosure (Sep 16)*

![](/shared/images/nst-icons.svg#search)

## [Nmap Security Scanner](https://nmap.org/)

* [Ref Guide](https://nmap.org/book/man.html)* [Install Guide](https://nmap.org/book/install.html)* [Docs](https://nmap.org/docs.html)* [Download](https://nmap.org/download.html)* [Nmap OEM](https://nmap.org/oem/)

## [Npcap packet capture](https://npcap.com/)

* [User's Guide](https://npcap.com/guide/)* [API docs](https://npcap.com/guide/npcap-devguide.html#npcap-api)* [Download](https://npcap.com/#download)* [Npcap OEM](https://npcap.com/oem/)

## [Security Lists](https://seclists.org/)

* [Nmap Announce](https://seclists.org/nmap-announce/)* [Nmap Dev](https://seclists.org/nmap-dev/)* [Full Disclosure](https://seclists.org/fulldisclosure/)* [Open Source Security](https://seclists.org/oss-sec/)* [BreachExchange](https://seclists.org/dataloss/)

## [Security Tools](https://sectools.org)

* [Vuln scanners](https://sectools.org/tag/vuln-scanners/)* [Password audit](https://sectools.org/tag/pass-audit/)* [Web scanners](https://sectools.org/tag/web-scanners/)* [Wireless](https://sectools.org/tag/wireless/)* [Exploitation](https://sectools.org/tag/sploits/)

## [About](https://insecure.org/)

* [About/Contact](https://insecure.org/fyodor/)* [Privacy](https://insecure.org/privacy.html)* [Advertising](https://insecure.org/advertising.html)* [Nmap Public Source License](https://nmap.org/npsl/)

[![](/shared/images/nst-icons.svg#twitter)](https://twitter.com/nmap "Visit us on Twitter")
[![](/shared/images/nst-icons.svg#facebook)](https://facebook.com/nmap "Visit us on Facebook")
[![](/shared/images/nst-icons.svg#github)](https://github.com/nmap/ "Visit us on Github")
[![](/shared/images/nst-icons.svg#reddit)](https://reddit.com/r/nmap/ "Discuss Nmap on Reddit")