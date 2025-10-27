---
title: APPLE-SA-2023-03-27-8 Safari 16.4
url: https://seclists.org/fulldisclosure/2023/Mar/23
source: Full Disclosure
date: 2023-03-29
fetch_date: 2025-10-04T11:03:21.593526
---

# APPLE-SA-2023-03-27-8 Safari 16.4

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
[![Next](/images/right-icon-16x16.png)](24)

[![Previous](/images/left-icon-16x16.png)](22)
[By Thread](index.html#23)
[![Next](/images/right-icon-16x16.png)](24)

![](/shared/images/nst-icons.svg#search)

# APPLE-SA-2023-03-27-8 Safari 16.4

---

*From*: Apple Product Security via Fulldisclosure <fulldisclosure () seclists org>
*Date*: Mon, 27 Mar 2023 16:08:48 -0700

---

```
-----BEGIN PGP SIGNED MESSAGE-----
Hash: SHA256

APPLE-SA-2023-03-27-8 Safari 16.4

Safari 16.4 addresses the following issues.
Information about the security content is also available at
https://support.apple.com/HT213671.

WebKit
Available for: macOS Big Sur and macOS Monterey
Impact: Processing maliciously crafted web content may bypass Same
Origin Policy
Description: This issue was addressed with improved state management.
WebKit Bugzilla: 248615
CVE-2023-27932: an anonymous researcher

WebKit
Available for: macOS Big Sur and macOS Monterey
Impact: A website may be able to track sensitive user information
Description: The issue was addressed by removing origin information.
WebKit Bugzilla: 250837
CVE-2023-27954: an anonymous researcher

Additional recognition

CFNetwork
We would like to acknowledge an anonymous researcher for their
assistance.

WebKit
We would like to acknowledge an anonymous researcher for their
assistance.

WebKit Web Inspector
We would like to acknowledge Dohyun Lee (@l33d0hyun) and crixer
(@pwning_me) of SSD Labs for their assistance.

Safari 16.4 may be obtained from the Mac App Store.
All information is also posted on the Apple Security Updates
web site: https://support.apple.com/en-us/HT201222.

This message is signed with Apple's Product Security PGP key,
and details are available at:
https://www.apple.com/support/security/pgp/
-----BEGIN PGP SIGNATURE-----

iQIzBAEBCAAdFiEEBP+4DupqR5Sgt1DB4RjMIDkeNxkFAmQiHn4ACgkQ4RjMIDke
NxnzuA//R6r9YrqrgdWro+Why6ihvWKdVIBgEVu93nNfgd34+HLkRKsr00xH0hNw
kDvjtfPpCeuQB61VtVO6dCEPHLJICqEyOeqHoIDYvKwAoH830u3S4vWA6ozJpBmd
CCI+5tF9qAZWb+O0ED+hyU31z/+0s+gTGUjp7dhAnKJ6jKQOjSwWG4+YEgJA6wGG
oOC8dXGTWMHQJsDyxliGC/FQVo6cyWtbZiwWB9QYKP48yIldrRWJz75xOUWYOjWe
GYZ+vNDaOIi+/YHRHRYf/RY7Fdigur5rsWtzK/0v1T/n3t2kwe6WZkF4HdKFHRXL
KSw1fogSQh1BncUXlVfkn3BMPoEOUxHkhtawdKkewK+W8ZTC2mq+YwrJ26YZMTmU
5Nvgua4gxm2gb8LupcaXxt+o/nIbbTWyNx6rEyskWMxw6jZksBwgdDk2pSrUtmWh
d2VnkbUjoLXbP7uqSrf2gqd6drAVrHUlmEHLVAXCG60mhWNzCxr2M+DG2RZ0RLgJ
DMy2O4zxdzWZxkRJE86LchYz8zToQD7eQXm3zMQTGdSZoJXr3NxVGwdCaCGdhGAA
ckJV7nHybrVGQXdo5EeNuxKeiyJMimGGIDpQmHrrf+PgeL7zKi9e4KwyyobAmvZn
lw86QALA/97AKbSQthqHlDnv+inUrdwH1TWcurtCkjeRHgkhif8=
=o24C
-----END PGP SIGNATURE-----

_______________________________________________
Sent through the Full Disclosure mailing list
https://nmap.org/mailman/listinfo/fulldisclosure
Web Archives & RSS: https://seclists.org/fulldisclosure/
```

---

[![Previous](/images/left-icon-16x16.png)](22)
[By Date](date.html#23)
[![Next](/images/right-icon-16x16.png)](24)

[![Previous](/images/left-icon-16x16.png)](22)
[By Thread](index.html#23)
[![Next](/images/right-icon-16x16.png)](24)

### Current thread:

* **APPLE-SA-2023-03-27-8 Safari 16.4** *Apple Product Security via Fulldisclosure (Mar 27)*

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