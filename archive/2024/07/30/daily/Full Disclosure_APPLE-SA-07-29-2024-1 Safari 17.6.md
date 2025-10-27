---
title: APPLE-SA-07-29-2024-1 Safari 17.6
url: https://seclists.org/fulldisclosure/2024/Jul/15
source: Full Disclosure
date: 2024-07-30
fetch_date: 2025-10-06T17:47:13.015594
---

# APPLE-SA-07-29-2024-1 Safari 17.6

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

[![Previous](/images/left-icon-16x16.png)](14)
[By Date](date.html#15)
[![Next](/images/right-icon-16x16.png)](16)

[![Previous](/images/left-icon-16x16.png)](14)
[By Thread](index.html#15)
[![Next](/images/right-icon-16x16.png)](16)

![](/shared/images/nst-icons.svg#search)

# APPLE-SA-07-29-2024-1 Safari 17.6

---

*From*: Apple Product Security via Fulldisclosure <fulldisclosure () seclists org>
*Date*: Mon, 29 Jul 2024 16:11:25 -0700

---

```
-----BEGIN PGP SIGNED MESSAGE-----
Hash: SHA256

APPLE-SA-07-29-2024-1 Safari 17.6

Safari 17.6 addresses the following issues.
Information about the security content is also available at
https://support.apple.com/HT214121.

Apple maintains a Security Releases page at
https://support.apple.com/HT201222 which lists recent
software updates with security advisories.

Safari
Available for: macOS Monterey and macOS Ventura
Impact: Visiting a website that frames malicious content may lead to UI
spoofing
Description: The issue was addressed with improved UI handling.
CVE-2024-40817: Yadhu Krishna M and Narendra Bhati, Manager of Cyber
Security At Suma Soft Pvt. Ltd, Pune (India)

WebKit
Available for: macOS Monterey and macOS Ventura
Impact: Processing maliciously crafted web content may lead to an
unexpected process crash
Description: A use-after-free issue was addressed with improved memory
management.
WebKit Bugzilla: 273176
CVE-2024-40776: Huang Xilin of Ant Group Light-Year Security Lab
WebKit Bugzilla: 268770
CVE-2024-40782: Maksymilian Motyl

WebKit
Available for: macOS Monterey and macOS Ventura
Impact: Processing maliciously crafted web content may lead to an
unexpected process crash
Description: An out-of-bounds read was addressed with improved bounds
checking.
WebKit Bugzilla: 275431
CVE-2024-40779: Huang Xilin of Ant Group Light-Year Security Lab
WebKit Bugzilla: 275273
CVE-2024-40780: Huang Xilin of Ant Group Light-Year Security Lab

WebKit
Available for: macOS Monterey and macOS Ventura
Impact: Processing maliciously crafted web content may lead to a cross
site scripting attack
Description: This issue was addressed with improved checks.
WebKit Bugzilla: 273805
CVE-2024-40785: Johan Carlsson (joaxcar)

WebKit
Available for: macOS Monterey and macOS Ventura
Impact: Processing maliciously crafted web content may lead to an
unexpected process crash
Description: An out-of-bounds access issue was addressed with improved
bounds checking.
CVE-2024-40789: Seunghyun Lee (@0x10n) of KAIST Hacking Lab working with
Trend Micro Zero Day Initiative

WebKit
Available for: macOS Monterey and macOS Ventura
Impact: Processing maliciously crafted web content may lead to an
unexpected process crash
Description: This is a vulnerability in open source code and Apple
Software is among the affected projects. The CVE-ID was assigned by a
third party. Learn more about the issue and CVE-ID at cve.org.
WebKit Bugzilla: 274165
CVE-2024-4558

WebKit
Available for: macOS Monterey and macOS Ventura
Impact: Private Browsing tabs may be accessed without authentication
Description: This issue was addressed through improved state management.
WebKit Bugzilla: 275272
CVE-2024-40794: Matthew Butler

Additional recognition

WebKit
We would like to acknowledge an anonymous researcher for their
assistance.

Safari 17.6 may be obtained from the Mac App Store.
All information is also posted on the Apple Security Releases
web site: https://support.apple.com/HT201222.

This message is signed with Apple's Product Security PGP key,
and details are available at:
https://www.apple.com/support/security/pgp/
-----BEGIN PGP SIGNATURE-----

iQIzBAEBCAAdFiEEsz9altA7uTI+rE/qX+5d1TXaIvoFAmaoHvUACgkQX+5d1TXa
Ivqp7g//W0X1OTp1Vy3a1AlxeI62Kc4NwkPOVolrJHbKx+NRWkoh8MGi+nC63x22
aMekxuerqrptlmdX9wIYnrLbwbZC2nC4U1TJtzeVnsj3K8qDzc6WHEGol8hLR8F7
fK8YdfwDHT1VZedVKOarSB9PvXcomnAp63AS3qUwctnwglQZ+mrR18xAoFpIhdLT
uaUWJCq3bY4aD7fmU42ji1uLSPfcjLcfvWjavB5kcLEGHDFMUx3WJNtIR+/iBqjm
/0o2DzFW91N+IYwRC0m7Cus2gsFgzKWRkDUEeOV/UDsXiNfRVlCBl55hPAT+yg/y
iUvarlPYrGR8hPlFJpuy6mFHaiR/EWquxWMVasZwIchBxq69eM79ezu3quE6Eztz
nkSvi9uJuqMv6PWp2YrG3yXzgvnUyxITKftK5CnJnDKjhucqUT9zWr58or22NzO8
Qswy0eILPCHwzRYWkhvA3guQh/DaUeaBycFrQlgJRcfdTgLXXsBp6LTX+H9h7G2F
IN1fP6o9AR7kSkrNZAXi1ek3UoZBWtoCiQCD2ITjAAaam5UueI8ZmHPpyIjTOyeI
+QGBa7rNZ5vbOU4ojQGWC93iCxrNuFgcB2wshr9Uz8YujY0vJAoKSJruY71tODaL
WDvvLa4GQ+um3pXAewqay83rn1e3X9GClc89Q9LScdGVugdzEB0=
=+Uon
-----END PGP SIGNATURE-----
_______________________________________________
Sent through the Full Disclosure mailing list
https://nmap.org/mailman/listinfo/fulldisclosure
Web Archives & RSS: https://seclists.org/fulldisclosure/
```

---

[![Previous](/images/left-icon-16x16.png)](14)
[By Date](date.html#15)
[![Next](/images/right-icon-16x16.png)](16)

[![Previous](/images/left-icon-16x16.png)](14)
[By Thread](index.html#15)
[![Next](/images/right-icon-16x16.png)](16)

### Current thread:

* **APPLE-SA-07-29-2024-1 Safari 17.6** *Apple Product Security via Fulldisclosure (Jul 29)*

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