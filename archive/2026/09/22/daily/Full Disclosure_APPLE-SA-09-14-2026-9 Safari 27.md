---
title: APPLE-SA-09-14-2026-9 Safari 27
url: https://seclists.org/fulldisclosure/2026/Sep/61
source: Full Disclosure
date: 2026-09-22
fetch_date: 2026-09-23T06:55:24.078347
---

# APPLE-SA-09-14-2026-9 Safari 27

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

[![Previous](/images/left-icon-16x16.png)](60)
[By Date](date.html#61)
[![Next](/images/right-icon-16x16.png)](62)

[![Previous](/images/left-icon-16x16.png)](60)
[By Thread](index.html#61)
[![Next](/images/right-icon-16x16.png)](62)

![](/shared/images/nst-icons.svg#search)

# APPLE-SA-09-14-2026-9 Safari 27

---

*From*: Apple Product Security via Fulldisclosure <fulldisclosure () seclists org>
*Date*: Mon, 14 Sep 2026 15:09:41 -0700

---

```
-----BEGIN PGP SIGNED MESSAGE-----
Hash: SHA256

APPLE-SA-09-14-2026-9 Safari 27

Safari 27 addresses the following issues.
Information about the security content is also available at
https://support.apple.com/149039.

Apple maintains a Security Releases page at
https://support.apple.com/100100 which lists recent
software updates with security advisories.

Safari
Available for: macOS Sequoia and macOS Tahoe
Impact: A malicious website may be able to determine what apps a user
has installed
Description: This issue was addressed through improved state management.
CVE-2026-84518: Bálint Magyar (balintmagyar.com)

Safe Browsing
Available for: macOS Sequoia and macOS Tahoe
Impact: An app may be able to access sensitive user data
Description: This issue was addressed with additional entitlement
checks.
CVE-2026-86897: Stuart Wallace

WebKit
Available for: macOS Sequoia and macOS Tahoe
Impact: Processing maliciously crafted web content may lead to an
unexpected process termination
Description: A logic issue was addressed with improved state management.
WebKit Bugzilla: 310457
CVE-2026-84635: Souta Sugiyama

WebKit
Available for: macOS Sequoia and macOS Tahoe
Impact: Processing maliciously crafted web content may disclose
sensitive user information
Description: A permissions issue was addressed by removing the
vulnerable code.
WebKit Bugzilla: 315121
CVE-2026-64753: Viggo Lekdorf

WebKit
Available for: macOS Sequoia and macOS Tahoe
Impact: Opening a maliciously crafted webarchive file may lead to
universal cross-site scripting
Description: A logic issue was addressed with improved state management.
WebKit Bugzilla: 3182711
CVE-2026-86898: Tomi Garcia (archyxsec)

WebKit Canvas
Available for: macOS Sequoia and macOS Tahoe
Impact: Processing maliciously crafted web content may lead to an
unexpected Safari crash
Description: A use-after-free issue was addressed with improved memory
management.
WebKit Bugzilla: 313935
CVE-2026-64718: Niels Hofmans, OGINOME Tomohito, an anonymous researcher

Additional recognition

Safari
We would like to acknowledge Dem0ns @天府简易信工作室 for their assistance.

Safari Downloads
We would like to acknowledge Barath Stalin K
(linkedin.com/in/barathstalin), Exell Nakano, Manojkumar Jaganathan
(linkedin.com/in/manojkumar-j-7ba35b202/) with HackerBro Technologies,
Praditya Fajar Ramadhan, Zhiyang Zeng (@Wester), shobhit srivastav for
their assistance.

WebKit
We would like to acknowledge @TristanInSec, Behzad Najjarpour Jabbari
(@_G4ru_), Big Bear, Eddy Tsalolikhin, Henock Habte, Kenneth Hsu, Maher
Azzouzi, Meridian Miftari, N13S, OpenAI Codex Security - Amy Burnett,
Souta Sugiyama, Vitaly Simonovich, an anonymous researcher,
hamayanhamayan, lattice, lebr0nli of National Yang Ming Chiao Tung
University, Security and Systems Lab, ret2happy, wwwlk for their
assistance.

WebKit Canvas
We would like to acknowledge Utkarsh Pal for their assistance.

WebKit JavaScript Bindings
We would like to acknowledge hamayanhamayan for their assistance.

Safari 27 may be obtained from the Mac App Store.

All information is also posted on the Apple Security Releases
web site: https://support.apple.com/100100.

This message is signed with Apple's Product Security PGP key,
and details are available at:
https://www.apple.com/support/security/pgp/

-----BEGIN PGP SIGNATURE-----

iQIzBAEBCAAdFiEEhjkl+zMLNwFiCT1o4Ifiq8DH7PUFAmqoYtAACgkQ4Ifiq8DH
7PVIahAAuV156HhzFODrPZh3bAOjuSXNvTNysYfs/wL+GLASjJ9wg1wiKQZ9HQBx
d24Zs6y9JCQ4B2QmLfh2ahEpOJJCShkMX+o0l1blm1pX1leRCSXl/Ege1u5YvF6j
B6ZNCAda3Mrv0fSIwxpGZ2/jI1GtUUoJ2CJEKNhas5o4AfRkF42yfr0HkcK6AYCS
0xC5EMmT8g+OVWdKx8/bfT6OW4BoxirW3ApFkgnySXWnq2aqyNZWPKXIwGq4AeCZ
siEm2ncjsntfbILVmVfsDdBoRVyrcqu+Kc7quiw4hrXS7sL43aVw8Wi6FXEcXWVp
2L8M/NrGo3ZrWaqDTwjXQ09aVkxqkWHBqs2bSYMcdJNK4eVHfAQcaNPGzF1Pppso
E/HvBzmas6wT4ecekS5zqvmgH67MfIJnmWtAyWtNrfeEPhm/AF8L9zMcQdzjmtRi
LdxfV5wJrboSMegfhuTDgmVN4so6aVsXkDbMZhrkDuJVB7n2aQp6OnhuUwHCGIdV
0dXR9cptSaG47hz6E/NEFnyWG/7hpCtUgGI8mnFqJLgfRCHhGrMWSc4Ryu7q2Chl
wfIuvHDI0TnhOfZJ8ZAqO0oospzK457r+dwkGAKm3ok/EL0zZuvUNi1p0goO5Xox
+we6JHCyUBoEK8ioVEwLWbw2jdH62PRUlQmdiPAriJgFIen9x5c=
=J8zV
-----END PGP SIGNATURE-----

_______________________________________________
Sent through the Full Disclosure mailing list
https://nmap.org/mailman/listinfo/fulldisclosure
Web Archives & RSS: https://seclists.org/fulldisclosure/
```

---

[![Previous](/images/left-icon-16x16.png)](60)
[By Date](date.html#61)
[![Next](/images/right-icon-16x16.png)](62)

[![Previous](/images/left-icon-16x16.png)](60)
[By Thread](index.html#61)
[![Next](/images/right-icon-16x16.png)](62)

### Current thread:

* **APPLE-SA-09-14-2026-9 Safari 27** *Apple Product Security via Fulldisclosure (Sep 22)*

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