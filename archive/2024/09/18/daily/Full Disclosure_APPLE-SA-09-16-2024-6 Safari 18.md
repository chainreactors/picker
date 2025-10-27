---
title: APPLE-SA-09-16-2024-6 Safari 18
url: https://seclists.org/fulldisclosure/2024/Sep/37
source: Full Disclosure
date: 2024-09-18
fetch_date: 2025-10-06T18:30:23.191292
---

# APPLE-SA-09-16-2024-6 Safari 18

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

[![Previous](/images/left-icon-16x16.png)](36)
[By Date](date.html#37)
[![Next](/images/right-icon-16x16.png)](38)

[![Previous](/images/left-icon-16x16.png)](36)
[By Thread](index.html#37)
[![Next](/images/right-icon-16x16.png)](38)

![](/shared/images/nst-icons.svg#search)

# APPLE-SA-09-16-2024-6 Safari 18

---

*From*: Apple Product Security via Fulldisclosure <fulldisclosure () seclists org>
*Date*: Mon, 16 Sep 2024 18:10:50 -0700

---

```
-----BEGIN PGP SIGNED MESSAGE-----
Hash: SHA256

APPLE-SA-09-16-2024-6 Safari 18

Safari 18 addresses the following issues.
Information about the security content is also available at
https://support.apple.com/121241.

Apple maintains a Security Releases page at
https://support.apple.com/100100 which lists recent
software updates with security advisories.

WebKit
Available for: macOS Ventura and macOS Sonoma
Impact: Visiting a malicious website may lead to address bar spoofing
Description: The issue was addressed with improved UI.
WebKit Bugzilla: 279451
CVE-2024-40866: Hafiizh and YoKo Kho (@yokoacc) of HakTrak

WebKit
Available for: macOS Ventura and macOS Sonoma
Impact: A malicious website may exfiltrate data cross-origin
Description: A cross-origin issue existed with "iframe" elements. This
was addressed with improved tracking of security origins.
WebKit Bugzilla: 279452
CVE-2024-44187: Narendra Bhati, Manager of Cyber Security at Suma Soft
Pvt. Ltd, Pune (India)

WebKit
Available for: macOS Ventura and macOS Sonoma
Impact: Processing maliciously crafted web content may lead to universal
cross site scripting
Description: This issue was addressed through improved state management.
WebKit Bugzilla: 268724
CVE-2024-40857: Ron Masas

Additional recognition

Safari
We would like to acknowledge Hafiizh and YoKo Kho (@yokoacc) of HakTrak
for their assistance.

Safari 18 may be obtained from the Mac App Store.

All information is also posted on the Apple Security Releases
web site: https://support.apple.com/100100.

This message is signed with Apple's Product Security PGP key,
and details are available at:
https://www.apple.com/support/security/pgp/
-----BEGIN PGP SIGNATURE-----

iQIzBAEBCAAdFiEEsz9altA7uTI+rE/qX+5d1TXaIvoFAmboyScACgkQX+5d1TXa
Ivr5URAAqi3Km6vP17ccXkXlrcDJXrYE+HSdkDkqlpT0hNsfLCcpfbZME8R02efV
lzb8JZ7DdtWI4U0WKjvJvmIhm0Ik2S1stYCNaxAtEBJ6YUYIJE5lJS4J/D3J1QTd
5ygCi+zEzPnRjQx2BZ1Ju3VQdpDen50vTBY/cdqrujtbZ5s4wY2K2qV5SaPv7/zY
6KChB6ivmuEN/iEN5e/ppTr3lAC1Hw1GFsD6xqnxK+USyydYGryQHvCzoidYjoaB
7MkfwASZ/+RmdeCK+6pcN4NP8MRszViGas0GtZe+y7O/Pu6gc6PRrpD2s2LJKUta
id0ofA1EtL+IRav/wXvJbvTBQc2vWhOrFWL4rP/9znCW2wtO8neayKewWYal1ClZ
Jn75AOig5pfk6/aTtFFVXn/869PlolaVWe/jQuTVHvXX+N1nuDCriTRpVsz/XMdb
3kWqsgMMxKjJnFQoprKpJcAA+vc28L5WLBxhXgGkcb8DML70YNg96CsH3w+qUrJL
w9+AiGrgBECU3MhQOENtE8AmTmYMDCxjnEI8pYcsu5mKmLHkBnjRhYArLP+Se+3d
PLHvbAaZf/cmO7Vm4A2uu1bhqf+E3UJLIlkIGMcwp+vQBiSAT70hri8J6fcaCvLq
Hw7rhBt/najjjENdErB9REmqAjkJY3vP2K4pjE/1PNXmHd5tQu4=
=q+/h
-----END PGP SIGNATURE-----

_______________________________________________
Sent through the Full Disclosure mailing list
https://nmap.org/mailman/listinfo/fulldisclosure
Web Archives & RSS: https://seclists.org/fulldisclosure/
```

---

[![Previous](/images/left-icon-16x16.png)](36)
[By Date](date.html#37)
[![Next](/images/right-icon-16x16.png)](38)

[![Previous](/images/left-icon-16x16.png)](36)
[By Thread](index.html#37)
[![Next](/images/right-icon-16x16.png)](38)

### Current thread:

* **APPLE-SA-09-16-2024-6 Safari 18** *Apple Product Security via Fulldisclosure (Sep 16)*

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