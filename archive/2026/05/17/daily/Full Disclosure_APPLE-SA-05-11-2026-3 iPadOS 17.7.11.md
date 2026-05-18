---
title: APPLE-SA-05-11-2026-3 iPadOS 17.7.11
url: https://seclists.org/fulldisclosure/2026/May/8
source: Full Disclosure
date: 2026-05-17
fetch_date: 2026-05-18T06:10:48.491998
---

# APPLE-SA-05-11-2026-3 iPadOS 17.7.11

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

[![Previous](/images/left-icon-16x16.png)](6)
[By Date](date.html#8)
[![Next](/images/right-icon-16x16.png)](9)

[![Previous](/images/left-icon-16x16.png)](6)
[By Thread](index.html#8)
[![Next](/images/right-icon-16x16.png)](9)

![](/shared/images/nst-icons.svg#search)

# APPLE-SA-05-11-2026-3 iPadOS 17.7.11

---

*From*: Apple Product Security via Fulldisclosure <fulldisclosure () seclists org>
*Date*: Mon, 11 May 2026 15:30:46 -0700

---

```
-----BEGIN PGP SIGNED MESSAGE-----
Hash: SHA256

APPLE-SA-05-11-2026-3 iPadOS 17.7.11

iPadOS 17.7.11 addresses the following issues.
Information about the security content is also available at
https://support.apple.com/en-us/127112.

Apple maintains a Security Releases page at
https://support.apple.com/100100 which lists recent
software updates with security advisories.

Notification Services
Available for: iPad Pro 12.9-inch 2nd generation, iPad Pro 10.5-inch,
and iPad 6th generation
Impact: Notifications marked for deletion could be unexpectedly retained
on the device
Description: A logging issue was addressed with improved data redaction.
CVE-2026-28950

This update is available through iTunes and Software Update on your iOS
device, and will not appear in your computer's Software Update
application, or in the Apple Downloads site. Make sure you have an
Internet connection and have installed the latest version of iTunes from
https://www.apple.com/itunes/

iTunes and Software Update on the device will automatically check
Apple's update server on its weekly schedule. When an update is
detected, it is downloaded and the option to be installed is presented
to the user when the iOS device is docked. We recommend applying the
update immediately if possible. Selecting Don't Install will present the
option the next time you connect your iOS device.

The automatic update process may take up to a week depending on the day
that iTunes or the device checks for updates. You may manually obtain
the update via the Check for Updates button within iTunes, or the
Software Update on your device.

To check that the iPhone, iPod touch, or iPad has been updated:

* Navigate to Settings
* Select General
* Select About. The version
after applying this update will be "iPadOS 17.7.11".

All information is also posted on the Apple Security Releases
web site: https://support.apple.com/100100.

This message is signed with Apple's Product Security PGP key,
and details are available at:
https://www.apple.com/support/security/pgp/

-----BEGIN PGP SIGNATURE-----

iQIzBAEBCAAdFiEEhjkl+zMLNwFiCT1o4Ifiq8DH7PUFAmoCVdUACgkQ4Ifiq8DH
7PVKVRAAlTdoPhZ0g/B6f5/zMxR62jWpuC1UyDMviQccbJNapl8c9QHsvMNG04Av
HyUp2JbiVh+g4jfBlUn31gMoGttzjrEgJrgx6unfxOGny6YtkTwQbXOJ1XWIdXWg
akLRZ9ENHqVVk252uiotdZd1Trvba6zaBkoUBfYrbB3v0R1bP8ZUvdQ51KwqFsYh
gMO1txKvAmdkFRce9Zj9kYYg/+TyI0QQDhy9J2s5RPeanCT7DOwslsHxNUux6T+A
8Eo8x5nXzfLrBKlMJ01OBpMDijhW/cXZ+tTqe9vPkplcRoTKVqq9ssskk6YdgzZT
qfbvZ2BbB82t/toPzN58PvhmJlzijIG83Xo9KdxZG1Y3BHSYimMXSOfBeT6qIieP
Pr398aMI4o0HEVinY8Ymrl34sqgLuIeaFTengLSN0B4hmG3sVaNDMuwY/Ya5DFhv
9l2MzZwyxkl2IbgVHXrlzsJOq6PtmMt3x2H01wqRlESSU4Q2haNsa9BxZNMyNOoI
vABAX85zrhricVJ3rBpNgUhwK3Ir2qpB5uhkb9JxI0jqmcerUBvIrrSJU5qQRf1M
ZlL+iWX3X04rChzhOiB6cSLXNWgoPm08gbX5Cj6RDyDOJlcGaxEQ64IqwRlg3Hzc
YXWET09wCwl/g//jZk9xTcZuR/mSGXDbKosV6RkeIqASMLfXgzE=
=YlQb
-----END PGP SIGNATURE-----

_______________________________________________
Sent through the Full Disclosure mailing list
https://nmap.org/mailman/listinfo/fulldisclosure
Web Archives & RSS: https://seclists.org/fulldisclosure/
```

---

[![Previous](/images/left-icon-16x16.png)](6)
[By Date](date.html#8)
[![Next](/images/right-icon-16x16.png)](9)

[![Previous](/images/left-icon-16x16.png)](6)
[By Thread](index.html#8)
[![Next](/images/right-icon-16x16.png)](9)

### Current thread:

* **APPLE-SA-05-11-2026-3 iPadOS 17.7.11** *Apple Product Security via Fulldisclosure (May 17)*

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