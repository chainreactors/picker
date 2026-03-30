---
title: APPLE-SA-03-24-2026-10 Xcode 26.4
url: https://seclists.org/fulldisclosure/2026/Mar/25
source: Full Disclosure
date: 2026-03-29
fetch_date: 2026-03-30T04:46:56.620823
---

# APPLE-SA-03-24-2026-10 Xcode 26.4

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

[![Previous](/images/left-icon-16x16.png)](24)
[By Date](date.html#25)
![Next](/images/right-icon-16x16.png)

[![Previous](/images/left-icon-16x16.png)](24)
[By Thread](index.html#25)
![Next](/images/right-icon-16x16.png)

![](/shared/images/nst-icons.svg#search)

# APPLE-SA-03-24-2026-10 Xcode 26.4

---

*From*: Apple Product Security via Fulldisclosure <fulldisclosure () seclists org>
*Date*: Tue, 24 Mar 2026 17:06:07 -0700

---

```
-----BEGIN PGP SIGNED MESSAGE-----
Hash: SHA256

APPLE-SA-03-24-2026-10 Xcode 26.4

Xcode 26.4 addresses the following issues.
Information about the security content is also available at
https://support.apple.com/126801.

Apple maintains a Security Releases page at
https://support.apple.com/100100 which lists recent
software updates with security advisories.

otool
Available for: macOS Tahoe 26.2 and later
Impact: An app may be able to cause unexpected system termination
Description: An out-of-bounds read was addressed with improved bounds
checking.
CVE-2026-28890: Nathaniel Oh (@calysteon)

Simulator
Available for: macOS Tahoe 26.2 and later
Impact: An app may be able to read arbitrary files as root
Description: A permissions issue was addressed with additional
restrictions.
CVE-2026-28889: Mihai Marin

Additional recognition

Dev Tools
We would like to acknowledge Nathaniel Oh (@calysteon) for their
assistance.

otool
We would like to acknowledge Eddy T for their assistance.

Swift
We would like to acknowledge Banavath Aravind for their assistance.

Xcode 26.4 may be obtained from:

https://developer.apple.com/xcode/downloads/

To check that the Xcode has been updated:

* Select Xcode in the menu bar
* Select About Xcode
* The version after applying this update will be "Xcode 26.4".

All information is also posted on the Apple Security Releases
web site: https://support.apple.com/100100.

This message is signed with Apple's Product Security PGP key,
and details are available at:
https://www.apple.com/support/security/pgp/

-----BEGIN PGP SIGNATURE-----

iQIzBAEBCAAdFiEEhjkl+zMLNwFiCT1o4Ifiq8DH7PUFAmnDI48ACgkQ4Ifiq8DH
7PUtRg/+K3DU37tAHl9h/wfU7fO6J/I8YhzMGU6tcLK4b/9UG/16/qOwIUVLd9ML
mCrEQY3hevwMyA+ki0HRmE0aiNTtGiFlpxNxhsyo3p6QDMXR4xyPjyFFdOcjUfKI
kDHTg0NoCZWi63+hpGHhP3emCAr9/rDnOwtbUDrl57UaCc05HPydZ40ggNxz9S2/
wh6ZrXPKlQHDBYQcmRV1TkqcdpyCJqNNIG2N+SBH489easlDXfQf5AS1Go3otDbU
MwviuKhN4DDPbcV+SXVJjJR/NQzmWFO5RuFvjkFTh/Z7Xi9HQY1Ytkekwl/LfNDw
OdC1aMu7CxKe4ZmC3fcOEOoriVDXVqORm3fmu1h5e9q/aJgJJy/0Rsu6hvec0yqJ
SJOv+oVAlQalZF23XYDm71vM0GdFS6jXkjAcDyeUIgK4a1xSNCln0fH/TEW4V+2f
plLWU8xirJ2vB+DO8+E6+Kg9WYDr63a8Tr0sNV0J42SwSbk3FLvsStEIgFIcm6HI
9SOyFWp3Jc8bFBmuOjiXFn9IBtkX6FT6TSWdDCIisdeilIcXHLRNa6Iljzn2kGqP
LmdGIbsSlggvy9thXIQ/t0ri2CL22aV6vV1Qjl1UW/i/vTtBA75ydroiyUhvo+If
dbSuto6QwxoTbULDd+lyHgRmJ4irQcOsJerFDI0k7Ju03n0hvdQ=
=YITA
-----END PGP SIGNATURE-----

_______________________________________________
Sent through the Full Disclosure mailing list
https://nmap.org/mailman/listinfo/fulldisclosure
Web Archives & RSS: https://seclists.org/fulldisclosure/
```

---

[![Previous](/images/left-icon-16x16.png)](24)
[By Date](date.html#25)
![Next](/images/right-icon-16x16.png)

[![Previous](/images/left-icon-16x16.png)](24)
[By Thread](index.html#25)
![Next](/images/right-icon-16x16.png)

### Current thread:

* **APPLE-SA-03-24-2026-10 Xcode 26.4** *Apple Product Security via Fulldisclosure (Mar 28)*

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