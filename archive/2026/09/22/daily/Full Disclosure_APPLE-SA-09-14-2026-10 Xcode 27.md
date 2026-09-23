---
title: APPLE-SA-09-14-2026-10 Xcode 27
url: https://seclists.org/fulldisclosure/2026/Sep/62
source: Full Disclosure
date: 2026-09-22
fetch_date: 2026-09-23T06:55:23.799957
---

# APPLE-SA-09-14-2026-10 Xcode 27

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

[![Previous](/images/left-icon-16x16.png)](61)
[By Date](date.html#62)
[![Next](/images/right-icon-16x16.png)](63)

[![Previous](/images/left-icon-16x16.png)](61)
[By Thread](index.html#62)
[![Next](/images/right-icon-16x16.png)](63)

![](/shared/images/nst-icons.svg#search)

# APPLE-SA-09-14-2026-10 Xcode 27

---

*From*: Apple Product Security via Fulldisclosure <fulldisclosure () seclists org>
*Date*: Mon, 14 Sep 2026 15:10:08 -0700

---

```
-----BEGIN PGP SIGNED MESSAGE-----
Hash: SHA256

APPLE-SA-09-14-2026-10 Xcode 27

Xcode 27 addresses the following issues.
Information about the security content is also available at
https://support.apple.com/149040.

Apple maintains a Security Releases page at
https://support.apple.com/100100 which lists recent
software updates with security advisories.

Xcode IDE
Available for: macOS Tahoe 26.6 and later
Impact: An app may be able to access user-sensitive data
Description: A permissions issue was addressed with improved validation.
CVE-2026-65393: Mickey Jin (@patch1t)

Additional recognition

otool
We would like to acknowledge Eddy T for their assistance.

Swift
We would like to acknowledge Owais Lone (thesecguy), Yuval Fradkin for
their assistance.

tapi
We would like to acknowledge Jian Lee (@speedyfriend433) for their
assistance.

Xcode IDE
We would like to acknowledge Yiğit Can YILMAZ (@yilmazcanyigit) for
their assistance.

Xcode 27 may be obtained from:

https://developer.apple.com/xcode/downloads/

To check that the Xcode has been updated:

* Select Xcode in the menu bar
* Select About Xcode
* The version after applying this update will be "Xcode 27".

All information is also posted on the Apple Security Releases
web site: https://support.apple.com/100100.

This message is signed with Apple's Product Security PGP key,
and details are available at:
https://www.apple.com/support/security/pgp/

-----BEGIN PGP SIGNATURE-----

iQIzBAEBCAAdFiEEhjkl+zMLNwFiCT1o4Ifiq8DH7PUFAmqoZgMACgkQ4Ifiq8DH
7PVAMhAAj9ptC0BpUmk5jd55EREexCAl6SHEEeKE0aTwfSVShLoMOejlDgvTdldX
sUo89DfGvxug0FzpsUB7+EeqikVzPX/D3jxKzXO4u6bzL3eKA7vzZZfYoK4GHwdu
WdTus4bWiiKfkNbYTzezWoGOqMwnrQkXam5sCwmMSBQiXhfsN0nsqNyTBupOlRtZ
LQSHRJOfCS94uMAFZldieRWec+gR1kwbJM11nRHlAg4KT3BwsKZs3KJvrz6otbiQ
BRvKvttfLc1Z6mkrtNuZ0EmsZ933qkugtBFD7dulKLUVH+5UVtVXi2Tnc1Dg+RvC
qHVvyueuEqnzK5Pwr71j0jSSxsGgrnnaNWbZ0dI8zjOvWlvUm0HNru8fNtrl8q2Z
KmxI4MPrgCwnMP0SDXrX6ehRmT/FsXWP5D+Wr0Tc/RTDL5Bp8oDIQkqwKRpzGDBr
8WTsUsDmDOtd0cI4VltRPM38bDV7mLAqn7pzG+Bd6sUhgBfZx3dJjBamc0Famdkd
qH5DykKoiUc4VXNGq4ezm4n2aN1KGp17hEhQQArwVYhLcK9DIBBVCemkd8iYe71L
GSy+AE/IkGyi5Gd2jsL5qvk1you5OsQXyrqhsFeonfDMgJ7JXeVW4qxDHgf2NwiM
IRY/ZcOOda5lgxQCNfP+VJgqX1y2+URWXj2nKH8cr11vaPZ+Quw=
=NmyZ
-----END PGP SIGNATURE-----
_______________________________________________
Sent through the Full Disclosure mailing list
https://nmap.org/mailman/listinfo/fulldisclosure
Web Archives & RSS: https://seclists.org/fulldisclosure/
```

---

[![Previous](/images/left-icon-16x16.png)](61)
[By Date](date.html#62)
[![Next](/images/right-icon-16x16.png)](63)

[![Previous](/images/left-icon-16x16.png)](61)
[By Thread](index.html#62)
[![Next](/images/right-icon-16x16.png)](63)

### Current thread:

* **APPLE-SA-09-14-2026-10 Xcode 27** *Apple Product Security via Fulldisclosure (Sep 22)*

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