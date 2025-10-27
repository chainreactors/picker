---
title: APPLE-SA-09-15-2025-11 Safari 26
url: https://seclists.org/fulldisclosure/2025/Sep/59
source: Full Disclosure
date: 2025-09-17
fetch_date: 2025-10-02T20:16:42.034761
---

# APPLE-SA-09-15-2025-11 Safari 26

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

[![Previous](/images/left-icon-16x16.png)](58)
[By Date](date.html#59)
[![Next](/images/right-icon-16x16.png)](60)

[![Previous](/images/left-icon-16x16.png)](58)
[By Thread](index.html#59)
[![Next](/images/right-icon-16x16.png)](60)

![](/shared/images/nst-icons.svg#search)

# APPLE-SA-09-15-2025-11 Safari 26

---

*From*: Apple Product Security via Fulldisclosure <fulldisclosure () seclists org>
*Date*: Mon, 15 Sep 2025 16:37:47 -0700

---

```
-----BEGIN PGP SIGNED MESSAGE-----
Hash: SHA256

APPLE-SA-09-15-2025-11 Safari 26

Safari 26 addresses the following issues.
Information about the security content is also available at
https://support.apple.com/125113.

Apple maintains a Security Releases page at
https://support.apple.com/100100 which lists recent
software updates with security advisories.

Safari
Available for: macOS Sonoma and macOS Sequoia
Impact: Visiting a malicious website may lead to address bar spoofing
Description: The issue was addressed by adding additional logic.
CVE-2025-43327: @RenwaX23

Safari
Available for: macOS Sonoma and macOS Sequoia
Impact: Processing maliciously crafted web content may lead to
unexpected URL redirection
Description: This issue was addressed with improved URL validation.
CVE-2025-31254: Evan Waelde

WebKit
Available for: macOS Sonoma and macOS Sequoia
Impact: A website may be able to access sensor information without user
consent
Description: The issue was addressed with improved handling of caches.
WebKit Bugzilla: 296153
CVE-2025-43356: Jaydev Ahire

WebKit
Available for: macOS Sonoma and macOS Sequoia
Impact: Processing maliciously crafted web content may lead to an
unexpected Safari crash
Description: The issue was addressed with improved memory handling.
WebKit Bugzilla: 294550
CVE-2025-43272: Big Bear

WebKit
Available for: macOS Sonoma and macOS Sequoia
Impact: Processing maliciously crafted web content may lead to an
unexpected process crash
Description: The issue was addressed with improved memory handling.
WebKit Bugzilla: 296490
CVE-2025-43343: an anonymous researcher

WebKit
Available for: macOS Sonoma and macOS Sequoia
Impact: Processing maliciously crafted web content may lead to an
unexpected process crash
Description: A correctness issue was addressed with improved checks.
WebKit Bugzilla: 296042
CVE-2025-43342: an anonymous researcher

WebKit Process Model
Available for: macOS Sonoma and macOS Sequoia
Impact: Processing maliciously crafted web content may lead to an
unexpected Safari crash
Description: A use-after-free issue was addressed with improved memory
management.
WebKit Bugzilla: 296276
CVE-2025-43368: Pawel Wylecial of REDTEAM.PL working with Trend Micro
Zero Day Initiative

Additional recognition

libxml2
We would like to acknowledge Nathaniel Oh (@calysteon) for their
assistance.

Safari
We would like to acknowledge HitmanAlharbi (@HitmanF15), Jaydev Ahire,
Kenneth Chew for their assistance.

WebKit
We would like to acknowledge Bob Lord, Matthew Liang, Mike Cardwell of
grepular.com, Stanley Lee Linton, YiÄŸit Can YILMAZ (@yilmazcanyigit) for
their assistance.

Safari 26 may be obtained from the Mac App Store.

All information is also posted on the Apple Security Releases
web site: https://support.apple.com/100100.

This message is signed with Apple's Product Security PGP key,
and details are available at:
https://www.apple.com/support/security/pgp/

-----BEGIN PGP SIGNATURE-----

iQIzBAEBCAAdFiEEhjkl+zMLNwFiCT1o4Ifiq8DH7PUFAmjInPUACgkQ4Ifiq8DH
7PU5JA//Vb5YxJFWTN2hpfY53T0SoKS25AkdBrd8fLKHkSx37s8OhBdLgiShmwt2
qzHUJXtvl/LiyLqAE8Ovvp+TrVokioufTzYsu7F+ZPDAjD7rXDNjG1YuwnefgW6f
lGU/70YGmgxTT6IlwXgnsGUo11SH9NwLEJ4c8FVpK5Cwaa7DQoq3KjTgoew+Y1WA
0lNLrUcUMO4YlLXPEZ4qDQJ+GlL/VwNarpu9UifXk2WJBYjnr8jbT39e/a95/JpC
omgBHhBXcynranlhuYdQU3Ey9ZzBi75T96pWFHQ3pA/Bt2IRspzJUyHz2e5+rncm
hYaz432M3B61feBSkFao7F93L2J+dIAeVt9GKN4vwzgCPmcmiDV67yW2clJ52t2p
kx2jOkma4wOrlocLG3hxjx6YCanbMSDaXh9ckQeUjNADJKe8uGN9pgLaEAxIbB6t
kra8i1YzHIFZsEwrr7yGU7ZRV5mam12AiuRFmE4hQyXBzM7K9xzneyf0BhDNrlmY
oj8SMWeU/kjc50U2qno8SmhLjzdVCGsole7cVdBBeTLBCXtTfW1hztlbw0CWuAzN
AkmhS6C2jCyolfSp0b4OOaUXD44YzHcVCl5KElAviux6ubrI0YuZbqa+cxcm9iyh
6gu9L0YDE2m+EiKEqnfbE9Ofysi3i6/B63FGFaLJz3CZfChnKJA=
=KKUp
-----END PGP SIGNATURE-----

_______________________________________________
Sent through the Full Disclosure mailing list
https://nmap.org/mailman/listinfo/fulldisclosure
Web Archives & RSS: https://seclists.org/fulldisclosure/
```

---

[![Previous](/images/left-icon-16x16.png)](58)
[By Date](date.html#59)
[![Next](/images/right-icon-16x16.png)](60)

[![Previous](/images/left-icon-16x16.png)](58)
[By Thread](index.html#59)
[![Next](/images/right-icon-16x16.png)](60)

### Current thread:

* **APPLE-SA-09-15-2025-11 Safari 26** *Apple Product Security via Fulldisclosure (Sep 15)*

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