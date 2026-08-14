---
title: APPLE-SA-08-06-2026-3 macOS Sonoma 14.8.9
url: https://seclists.org/fulldisclosure/2026/Aug/36
source: Full Disclosure
date: 2026-08-13
fetch_date: 2026-08-14T04:01:04.139124
---

# APPLE-SA-08-06-2026-3 macOS Sonoma 14.8.9

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

[![Previous](/images/left-icon-16x16.png)](35)
[By Date](date.html#36)
[![Next](/images/right-icon-16x16.png)](37)

[![Previous](/images/left-icon-16x16.png)](35)
[By Thread](index.html#36)
[![Next](/images/right-icon-16x16.png)](37)

![](/shared/images/nst-icons.svg#search)

# APPLE-SA-08-06-2026-3 macOS Sonoma 14.8.9

---

*From*: Apple Product Security via Fulldisclosure <fulldisclosure () seclists org>
*Date*: Thu, 06 Aug 2026 14:40:59 -0700

---

```
-----BEGIN PGP SIGNED MESSAGE-----
Hash: SHA256

APPLE-SA-08-06-2026-3 macOS Sonoma 14.8.9

macOS Sonoma 14.8.9 addresses the following issues.
Information about the security content is also available at
https://support.apple.com/en-us/148172.

Apple maintains a Security Releases page at
https://support.apple.com/100100 which lists recent
software updates with security advisories.

Screen Sharing
Available for: macOS Sonoma
Impact: An attacker on the network may be able to authenticate to Screen
Sharing without valid credentials
Description: An authentication issue was addressed with improved state
management.
CVE-2026-65400: Alfredo Pesoli (@__rev) via Bynario Atlas (bynar.io)

macOS Sonoma 14.8.9 may be obtained from the Mac App Store or Apple's
Software Downloads web site: https://support.apple.com/downloads/

All information is also posted on the Apple Security Releases
web site: https://support.apple.com/100100.

This message is signed with Apple's Product Security PGP key,
and details are available at:
https://www.apple.com/support/security/pgp/

-----BEGIN PGP SIGNATURE-----

iQIzBAEBCAAdFiEEhjkl+zMLNwFiCT1o4Ifiq8DH7PUFAmp0398ACgkQ4Ifiq8DH
7PWKMBAAvu5xxYJxYrHC6Oj94mG6HrnUKB65O7T36D022gyXCWYCyQW1zeMRPpNZ
6UlYiVQ4VJ211Ycgk8DWMqe3Z/slaoyF1sBk7kchBDu4Uu+cNB1YpvCskYFkVSJu
CS0CekYlsAjedz69+Q9OfwtccVyfg1pECt8SiTN1aGJwqyD1WamJt+/cxWD3Vwby
xnsjk8/7balvtsNihbGgrt63145pCBNd5h/51731cLv1c5AOA5Yj3uShbRcnDf/f
WyKl2ADehEaRd0Fm/Curc5d2h2Ca6LNtpKcsvTPvCzudqW/UItJ+E+b4LJTDmY/P
H5/Vgwv2O9cxZDE7hc4i8HomhPAgIMceqv/Of+qA49Nee6ksxvsaUPketxQ59XVS
jm3ZNOasRohb4puIKKbS3kAyo0+3CTAPMWG8a/mwSo0vdBfue9wk3Mfr0tNiW2dP
8VeBueXF4aMfxXqy8TFruo3eO68XwsE7Qzt5TX8kKlHmq7j76CO6ewohzPES8AYS
5tjPWVHKBIzT7qhO7IqVqNl1WlDlxHs8sROxT9/s9GAZctxzI7oonmChXVTECwN1
TXHc5jd1QlwY7zKN5sBN84xMv43bzf19/h2IPJdmYGX5aBs8WyteGFvQQSxOCOlf
pLlLXhaWg0eBom3v9H/+vhkmEBU1ax9gMhxbmqS68PK3r2swecE=
=XrU0
-----END PGP SIGNATURE-----

_______________________________________________
Sent through the Full Disclosure mailing list
https://nmap.org/mailman/listinfo/fulldisclosure
Web Archives & RSS: https://seclists.org/fulldisclosure/
```

---

[![Previous](/images/left-icon-16x16.png)](35)
[By Date](date.html#36)
[![Next](/images/right-icon-16x16.png)](37)

[![Previous](/images/left-icon-16x16.png)](35)
[By Thread](index.html#36)
[![Next](/images/right-icon-16x16.png)](37)

### Current thread:

* **APPLE-SA-08-06-2026-3 macOS Sonoma 14.8.9** *Apple Product Security via Fulldisclosure (Aug 13)*

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