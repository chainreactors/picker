---
title: APPLE-SA-09-28-2026-3 macOS Sequoia 15.8.1
url: https://seclists.org/fulldisclosure/2026/Sep/91
source: Full Disclosure
date: 2026-09-29
fetch_date: 2026-09-30T07:43:05.495028
---

# APPLE-SA-09-28-2026-3 macOS Sequoia 15.8.1

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

[![Previous](/images/left-icon-16x16.png)](90)
[By Date](date.html#91)
![Next](/images/right-icon-16x16.png)

[![Previous](/images/left-icon-16x16.png)](90)
[By Thread](index.html#91)
![Next](/images/right-icon-16x16.png)

![](/shared/images/nst-icons.svg#search)

# APPLE-SA-09-28-2026-3 macOS Sequoia 15.8.1

---

*From*: Apple Product Security via Fulldisclosure <fulldisclosure () seclists org>
*Date*: Mon, 28 Sep 2026 15:13:55 -0700

---

```
-----BEGIN PGP SIGNED MESSAGE-----
Hash: SHA256

APPLE-SA-09-28-2026-3 macOS Sequoia 15.8.1

macOS Sequoia 15.8.1 addresses the following issues.
Information about the security content is also available at
https://support.apple.com/149229.

Apple maintains a Security Releases page at
https://support.apple.com/100100 which lists recent
software updates with security advisories.

CoreGraphics
Available for: macOS Sequoia
Impact: Processing a maliciously crafted file may lead to arbitrary code
execution. Apple is aware of a report that this issue may have been
exploited in an extremely sophisticated attack against specific targeted
individuals on versions of iOS before iOS 27.
Description: An out-of-bounds write issue was addressed with improved
bounds checking.
CVE-2026-86950: Meta Product Security

macOS Sequoia 15.8.1 may be obtained from the Mac App Store or
Apple's Software Downloads web site:
https://support.apple.com/downloads/

All information is also posted on the Apple Security Releases
web site: https://support.apple.com/100100.

This message is signed with Apple's Product Security PGP key,
and details are available at:
https://www.apple.com/support/security/pgp/

-----BEGIN PGP SIGNATURE-----

iQIzBAEBCAAdFiEEhjkl+zMLNwFiCT1o4Ifiq8DH7PUFAmq62u0ACgkQ4Ifiq8DH
7PX9EA//e/Qc6ZrztZtDMNq4xfGbKbIgzNz09jLjIcp0nLU//UWcW3JejP71nu8W
IFV9hR77huzaia1Er7nIyt0UGEWLZqHECVhFJNhD4cN+A5tiYSnUk7XWnFWAZz+S
sWOrddC3A5rb6IsoiHCuZ1fZOI9nNPda3xw/KGZ56FWSy+hsoFC0c1yMSj3gZ7jC
tT1y1qF5UU4B0VbbZKG9w3z3J2smYmgtHzoOp/lRUrbQQ90tuPKEaVJWiqkLBR2P
OUfKoSRXLPQ/GjRpo1AwEEZeS0r4MVkCm8uedhF3mdTkpH2sgYWQtM74FEKe6N1a
/48B8Tn/CpgdhIWNP6VEpJC4p0RG2X2Gt2mvuedDwqR3EId3HGiSUTIaPI++xRWL
f0rBFVJeLHZLJQphzEwFHXk6xK7XE8g+xQuImTchwY2JQjWpFY85yTMD/vZt16k7
MYyEsoGC9Cg5nIvlFfrPRSJM0aShEPmX6s1T1zx1UQ5AASbSiW6BtX7CIeXVPwCW
Gla6vrseGwk6UoxOjqtEHiXaSkpSMb70du5DJBftkWHTPIIEF3XNOggcZfLPqxKw
aRYdNDHPFmOALhviZpcuNMyN1ALIOfw07sD2XawXD+JE8BPYqzvDJXU2WOYSjc1C
2iNeM38fbJbpvHpE+KcxaJ2lC2BqKRIDyrZcF6ZGeVO7v3sLuIE=
=uNAH
-----END PGP SIGNATURE-----

_______________________________________________
Sent through the Full Disclosure mailing list
https://nmap.org/mailman/listinfo/fulldisclosure
Web Archives & RSS: https://seclists.org/fulldisclosure/
```

---

[![Previous](/images/left-icon-16x16.png)](90)
[By Date](date.html#91)
![Next](/images/right-icon-16x16.png)

[![Previous](/images/left-icon-16x16.png)](90)
[By Thread](index.html#91)
![Next](/images/right-icon-16x16.png)

### Current thread:

* **APPLE-SA-09-28-2026-3 macOS Sequoia 15.8.1** *Apple Product Security via Fulldisclosure (Sep 28)*

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