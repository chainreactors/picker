---
title: APPLE-SA-02-11-2026-9 Safari 26.3
url: https://seclists.org/fulldisclosure/2026/Feb/29
source: Full Disclosure
date: 2026-02-16
fetch_date: 2026-02-17T04:21:55.374226
---

# APPLE-SA-02-11-2026-9 Safari 26.3

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

[![Previous](/images/left-icon-16x16.png)](28)
[By Date](date.html#29)
[![Next](/images/right-icon-16x16.png)](16)

[![Previous](/images/left-icon-16x16.png)](28)
[By Thread](index.html#29)
[![Next](/images/right-icon-16x16.png)](16)

![](/shared/images/nst-icons.svg#search)

# APPLE-SA-02-11-2026-9 Safari 26.3

---

*From*: Apple Product Security via Fulldisclosure <fulldisclosure () seclists org>
*Date*: Wed, 11 Feb 2026 16:06:52 -0800

---

```
-----BEGIN PGP SIGNED MESSAGE-----
Hash: SHA256

APPLE-SA-02-11-2026-9 Safari 26.3

Safari 26.3 addresses the following issues.
Information about the security content is also available at
https://support.apple.com/126354.

Apple maintains a Security Releases page at
https://support.apple.com/100100 which lists recent
software updates with security advisories.

CFNetwork
Available for: macOS Sonoma and macOS Sequoia
Impact: A remote user may be able to write arbitrary files
Description: A path handling issue was addressed with improved logic.
CVE-2026-20660: Amy (amys.website)

Safari
Available for: macOS Sonoma and macOS Sequoia
Impact: An app may be able to access a user's Safari history
Description: A logic issue was addressed with improved validation.
CVE-2026-20656: Mickey Jin (@patch1t)

WebKit
Available for: macOS Sonoma and macOS Sequoia
Impact: A remote attacker may be able to cause a denial-of-service
Description: The issue was addressed with improved memory handling.
WebKit Bugzilla: 303959
CVE-2026-20652: Nathaniel Oh (@calysteon)

WebKit
Available for: macOS Sonoma and macOS Sequoia
Impact: Processing maliciously crafted web content may lead to an
unexpected process crash
Description: This issue was addressed through improved state management.
WebKit Bugzilla: 303357
CVE-2026-20608: HanQing from TSDubhe and Nan Wang (@eternalsakura13)

WebKit
Available for: macOS Sonoma and macOS Sequoia
Impact: A website may be able to track users through Safari web
extensions
Description: This issue was addressed through improved state management.
WebKit Bugzilla: 305020
CVE-2026-20676: Tom Van Goethem

WebKit
Available for: macOS Sonoma and macOS Sequoia
Impact: Processing maliciously crafted web content may lead to an
unexpected process crash
Description: The issue was addressed with improved memory handling.
WebKit Bugzilla: 303444
CVE-2026-20644: HanQing from TSDubhe and Nan Wang (@eternalsakura13)
WebKit Bugzilla: 304657
CVE-2026-20636: EntryHi
WebKit Bugzilla: 304661
CVE-2026-20635: EntryHi

Additional recognition

WebKit
We would like to acknowledge David Wood, EntryHi, Luigino Camastra of
Aisle Research, Stanislav Fort of Aisle Research, Vsevolod Kokorin
(Slonser) of Solidlab and Jorian Woltjer for their assistance.

Safari 26.3 may be obtained from the Mac App Store.

All information is also posted on the Apple Security Releases
web site: https://support.apple.com/100100.

This message is signed with Apple's Product Security PGP key,
and details are available at:
https://www.apple.com/support/security/pgp/

-----BEGIN PGP SIGNATURE-----

iQIzBAEBCAAdFiEEhjkl+zMLNwFiCT1o4Ifiq8DH7PUFAmmND7oACgkQ4Ifiq8DH
7PVR4Q//dqRTn1jkGTKX6nBZPJSyVizdP9clKnd6CSvTUrYbTzw0/53Kw17n6etD
MV/KVu4NyuZIV/qPdGcjqAgNAnG4VVWsLOyMKIgE2ccTXf/DWsWAnsKqc+S1HUk3
NHmwu+OHbsgQ+8yWOOEYg6nsZEXR/1WTLEqCJCJOAVNF+ORCcx0fLik+KUkw//+W
K60gCR/RnxtFnI8GJvvgOe8Vz1ddkMb8TXQfvkjg/mB+C6r/Z35g5EqWZIMhO09H
kQ6KX/CEr3FDqvh5bVC7kyzDc2WFtrU+syynpLmvb2NLeaeOr4ZW0OX+CpTGXm2O
WjWxZTSvWJBJkGp8SzE6PimRkFirj9VdHcQk16XV/zGnnBx2dd9R2dVeuWxpjNO5
sfKCkwW1Xr7b0pnMEsG6NB+SQL3GTm9FD8zcFjh62zZig9+BB59KyMNwkXTtSrwB
mjBU9ORc3tfwcH8Vdk/2vQFvyio//eP3CwDDkDo1ujI1srjWaojrneBWApLwtbIp
Z8ojnNVIzHt0o2ViuxXQ+uH82s0RrJBTSYgss/pGB113aAKMoqBexfqqkFwPq1JU
mHgEXjgQPNGTgocUBYsDO2C4+zrExK+oiBL5sjaQDIS6tyydPLtoRQa8QAq7KQ/B
nS69vbgZ81xhxqj0PpoBnCII65Hg3STeLTF08fcvG5VmdhWD0kQ=
=Z1wf
-----END PGP SIGNATURE-----

_______________________________________________
Sent through the Full Disclosure mailing list
https://nmap.org/mailman/listinfo/fulldisclosure
Web Archives & RSS: https://seclists.org/fulldisclosure/
```

---

[![Previous](/images/left-icon-16x16.png)](28)
[By Date](date.html#29)
[![Next](/images/right-icon-16x16.png)](16)

[![Previous](/images/left-icon-16x16.png)](28)
[By Thread](index.html#29)
[![Next](/images/right-icon-16x16.png)](16)

### Current thread:

* **APPLE-SA-02-11-2026-9 Safari 26.3** *Apple Product Security via Fulldisclosure (Feb 16)*

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