---
title: APPLE-SA-08-06-2026-2 macOS Sequoia 15.7.9
url: https://seclists.org/fulldisclosure/2026/Aug/37
source: Full Disclosure
date: 2026-08-13
fetch_date: 2026-08-14T04:01:03.883485
---

# APPLE-SA-08-06-2026-2 macOS Sequoia 15.7.9

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
![Next](/images/right-icon-16x16.png)

[![Previous](/images/left-icon-16x16.png)](36)
[By Thread](index.html#37)
![Next](/images/right-icon-16x16.png)

![](/shared/images/nst-icons.svg#search)

# APPLE-SA-08-06-2026-2 macOS Sequoia 15.7.9

---

*From*: Apple Product Security via Fulldisclosure <fulldisclosure () seclists org>
*Date*: Thu, 06 Aug 2026 14:40:26 -0700

---

```
-----BEGIN PGP SIGNED MESSAGE-----
Hash: SHA256

APPLE-SA-08-06-2026-2 macOS Sequoia 15.7.9

macOS Sequoia 15.7.9 addresses the following issues.
Information about the security content is also available at
https://support.apple.com/en-us/148171.

Apple maintains a Security Releases page at
https://support.apple.com/100100 which lists recent
software updates with security advisories.

Screen Sharing
Available for: macOS Sequoia
Impact: An attacker on the network may be able to authenticate to Screen
Sharing without valid credentials
Description: An authentication issue was addressed with improved state
management.
CVE-2026-65400: Alfredo Pesoli (@__rev) via Bynario Atlas (bynar.io)

macOS Sequoia 15.7.9 may be obtained from the Mac App Store or Apple's
Software Downloads web site: https://support.apple.com/downloads/

All information is also posted on the Apple Security Releases
web site: https://support.apple.com/100100.

This message is signed with Apple's Product Security PGP key,
and details are available at:
https://www.apple.com/support/security/pgp/

-----BEGIN PGP SIGNATURE-----

iQIzBAEBCAAdFiEEhjkl+zMLNwFiCT1o4Ifiq8DH7PUFAmp038cACgkQ4Ifiq8DH
7PX5Lw/9GAmAP1eJuNJBxT5p4fvJjE3OltPezGlm65h7YURbVkA8+HOhDWUsL2Ky
MafnodYGetgUbp8+6pJAC/cUJRPwV7UvUq64PGzAZK95+k4bwOMrsbehGZggsvxU
9fvt+hx/hDZc8hflIYEYLsgpM9/RloUUFyp3jG3/MvR7zStaE2AlPahKfKs6BtvK
UxJTNpo35dVMoFbv/OVxjcBrUnauC9hJnf/UwLAWIYhuDB0sojIWbkIRmpYmBDST
DqdeEV9GJeF113ryzQV+xdoUxyEQVIKDCMfejgbuxVdRn6Q72SaJPrWPf2t9G86L
dEW8jjISA5ZQfSezIq21Rj8LmYnyo0DOAZEdQOoCQa2McGsiT8KAsJDjY2+FB3H0
8WVW+VQUWGIGHKY3Hjal7ytvNIeWIWTd6M3nYHHkqNPnQKCSM1bbqi6Qj0NHO/vL
HcYiwMuBIlu970SgFNMttmrdZvks8JG1KI2GD18nNHRA2DC7eXqXiGPcK5QMX3ZB
WpovpwHa1s15Sdx1pGM8LeWC5+6Qxo0zAkozKM440O58Z2N02ETFLUENQ6s8Q4Ah
rCqdMCNP+IP3stoqfk5sFJq75bjfMruGqC4DfBJdDLmRIg7YZ7NaR3j9WZOMQfyO
1dIV5ILTaIow0TeBFb6n9iC3SxvGvQQArtcIQkxO+LEBwakKj5M=
=6Ozt
-----END PGP SIGNATURE-----

_______________________________________________
Sent through the Full Disclosure mailing list
https://nmap.org/mailman/listinfo/fulldisclosure
Web Archives & RSS: https://seclists.org/fulldisclosure/
```

---

[![Previous](/images/left-icon-16x16.png)](36)
[By Date](date.html#37)
![Next](/images/right-icon-16x16.png)

[![Previous](/images/left-icon-16x16.png)](36)
[By Thread](index.html#37)
![Next](/images/right-icon-16x16.png)

### Current thread:

* **APPLE-SA-08-06-2026-2 macOS Sequoia 15.7.9** *Apple Product Security via Fulldisclosure (Aug 13)*

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