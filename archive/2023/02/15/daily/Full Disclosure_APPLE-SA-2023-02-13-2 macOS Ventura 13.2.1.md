---
title: APPLE-SA-2023-02-13-2 macOS Ventura 13.2.1
url: https://seclists.org/fulldisclosure/2023/Feb/5
source: Full Disclosure
date: 2023-02-15
fetch_date: 2025-10-04T06:42:00.641518
---

# APPLE-SA-2023-02-13-2 macOS Ventura 13.2.1

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

[![Previous](/images/left-icon-16x16.png)](4)
[By Date](date.html#5)
[![Next](/images/right-icon-16x16.png)](6)

[![Previous](/images/left-icon-16x16.png)](4)
[By Thread](index.html#5)
[![Next](/images/right-icon-16x16.png)](6)

![](/shared/images/nst-icons.svg#search)

# APPLE-SA-2023-02-13-2 macOS Ventura 13.2.1

---

*From*: Apple Product Security via Fulldisclosure <fulldisclosure () seclists org>
*Date*: Mon, 13 Feb 2023 17:44:41 -0800

---

```
-----BEGIN PGP SIGNED MESSAGE-----
Hash: SHA256

APPLE-SA-2023-02-13-2 macOS Ventura 13.2.1

macOS Ventura 13.2.1 addresses the following issues.
Information about the security content is also available at
https://support.apple.com/HT213633.

Kernel
Available for: macOS Ventura
Impact: An app may be able to execute arbitrary code with kernel
privileges
Description: A use after free issue was addressed with improved
memory management.
CVE-2023-23514: Xinru Chi of Pangu Lab, Ned Williamson of Google
Project Zero

Shortcuts
Available for: macOS Ventura
Impact: An app may be able to observe unprotected user data
Description: A privacy issue was addressed with improved handling of
temporary files.
CVE-2023-23522: Wenchao Li and Xiaolong Bai of Alibaba Group

WebKit
Available for: macOS Ventura
Impact: Processing maliciously crafted web content may lead to
arbitrary code execution. Apple is aware of a report that this issue
may have been actively exploited.
Description: A type confusion issue was addressed with improved
checks.
WebKit Bugzilla: 251944
CVE-2023-23529: an anonymous researcher

macOS Ventura 13.2.1 may be obtained from the Mac App Store or
Apple's Software Downloads web site:
https://support.apple.com/downloads/
All information is also posted on the Apple Security Updates
web site: https://support.apple.com/en-us/HT201222.

This message is signed with Apple's Product Security PGP key,
and details are available at:
https://www.apple.com/support/security/pgp/
-----BEGIN PGP SIGNATURE-----

iQIzBAEBCAAdFiEEBP+4DupqR5Sgt1DB4RjMIDkeNxkFAmPq5PIACgkQ4RjMIDke
NxkM2hAApRo7JQlaNxVVpw1y96PG2oAVygFVw+N1cpEO72L4gDjvAb7+tOBqUTkz
Az+IizQfC2gapw9g/csghk+s+/gt16Q0iX4jDDEDypZ5So/LoaucFVTbGCy9Hns0
T0PTS4a0KIFBHbRQ3ktrhkUp49ykqDWwWdnvM1QgtUe3HfAZQWHVnYpdsj26CTaz
5ihA0chuzAGnx2lUZbyz8nl6f9kdqx1x8uSF0P7AkIp6L7IcZOLLO8tXnKApeC7S
HSbafe7JKxVNPtzaI/ZuxQe9/9Kr8VUiezVCK+WvJ9akRsy4CQ022yirIOlFIEhF
32mFq+BaQ77YTULP2us7BG8oMJ3tPxfmlykhqD4P0p4JRW6ZFoQmVKyUEPdsaALG
NYilSR3CRSpaCbh+dunGMJshNSHRJO6NluLq1mPVB7xFSiypgJADjS95zBSINtC9
JrKusbpICiAm8VqVC4GNltG+djft0NjbSiJXPo409X7j01Bt1ZJpk2UWTUfZbHMU
hW90JFySoHLRcVt3Af1mbBkyaHv0GSKG+Fjul/XyBlG3U8eJVXJhWCrhMjm17GK0
6j4HEUsAYzAg0j+Ss7QQKhwxlW3BPd+3D2kGwbPzBx/rcyVjbc456fyCLSYP58cf
EIYmmOwF9QcH939TCxoIglHOsdAuuIilGApd2on9QWOj8QSaUFw=
=2kFu
-----END PGP SIGNATURE-----

_______________________________________________
Sent through the Full Disclosure mailing list
https://nmap.org/mailman/listinfo/fulldisclosure
Web Archives & RSS: https://seclists.org/fulldisclosure/
```

---

[![Previous](/images/left-icon-16x16.png)](4)
[By Date](date.html#5)
[![Next](/images/right-icon-16x16.png)](6)

[![Previous](/images/left-icon-16x16.png)](4)
[By Thread](index.html#5)
[![Next](/images/right-icon-16x16.png)](6)

### Current thread:

* **APPLE-SA-2023-02-13-2 macOS Ventura 13.2.1** *Apple Product Security via Fulldisclosure (Feb 14)*

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