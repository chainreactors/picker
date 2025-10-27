---
title: APPLE-SA-04-16-2025-2 macOS Sequoia 15.4.1
url: https://seclists.org/fulldisclosure/2025/Apr/24
source: Full Disclosure
date: 2025-04-25
fetch_date: 2025-10-06T22:07:44.659407
---

# APPLE-SA-04-16-2025-2 macOS Sequoia 15.4.1

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

[![Previous](/images/left-icon-16x16.png)](23)
[By Date](date.html#24)
[![Next](/images/right-icon-16x16.png)](25)

[![Previous](/images/left-icon-16x16.png)](23)
[By Thread](index.html#24)
[![Next](/images/right-icon-16x16.png)](25)

![](/shared/images/nst-icons.svg#search)

# APPLE-SA-04-16-2025-2 macOS Sequoia 15.4.1

---

*From*: Apple Product Security via Fulldisclosure <fulldisclosure () seclists org>
*Date*: Wed, 16 Apr 2025 13:53:17 -0700

---

```
-----BEGIN PGP SIGNED MESSAGE-----
Hash: SHA256

APPLE-SA-04-16-2025-2 macOS Sequoia 15.4.1

macOS Sequoia 15.4.1 addresses the following issues.
Information about the security content is also available at
https://support.apple.com/122400.

Apple maintains a Security Releases page at
https://support.apple.com/100100 which lists recent
software updates with security advisories.

CoreAudio
Available for: macOS Sequoia
Impact: Processing an audio stream in a maliciously crafted media file
may result in code execution. Apple is aware of a report that this issue
may have been exploited in an extremely sophisticated attack against
specific targeted individuals on iOS.
Description: A memory corruption issue was addressed with improved
bounds checking.
CVE-2025-31200: Apple and Google Threat Analysis Group

RPAC
Available for: macOS Sequoia
Impact: An attacker with arbitrary read and write capability may be able
to bypass Pointer Authentication. Apple is aware of a report that this
issue may have been exploited in an extremely sophisticated attack
against specific targeted individuals on iOS.
Description: This issue was addressed by removing the vulnerable code.
CVE-2025-31201: Apple

macOS Sequoia 15.4.1 may be obtained from the Mac App Store or
Apple's Software Downloads web site:
https://support.apple.com/downloads/

All information is also posted on the Apple Security Releases
web site: https://support.apple.com/100100.

This message is signed with Apple's Product Security PGP key,
and details are available at:
https://www.apple.com/support/security/pgp/

-----BEGIN PGP SIGNATURE-----

iQIzBAEBCAAdFiEEsz9altA7uTI+rE/qX+5d1TXaIvoFAmgABakACgkQX+5d1TXa
Ivo32BAAsAmKz2o5MrqyXxxDiPp4VBQWEKrVvrjMoPoYZf4z9vOG3YYBlJOFQJKL
kFw4vxF9ie4mXc5YXkqdOYPMh09A7EadmpeBhChAjGs2nXfNE3Or6RnJ5b9fMuzs
wyXJQ2897lSd4mm3NxaXAnL1rxazAkqcVn3Wgw1oFEStT6FXZCB0zTfGJ/ok+Jzj
L9w/27uDJ3SZP2kgQBk0qGqd2Y3Asj06Mt9dmkuDBc36qyYDdGJCFqpVBTYDObpD
QrKKc5GKbLCVxe27qLoYdPng2M/vCKMN5hUytWh6e8oeZPM61PcQvVB+cbGXVrfB
A+6rRzVMSqHStusbukgEhMsUqSvZxRANAlcepbT/BiD5aaduxAtK3Ipr23T1JN3W
x2Dl8cAkijM8wnLQsd2zO24GiXX79eyGlhMV0GYZW+5MGn0N5IVLkOJ9RNE9AL5B
12Z2L77ZXdDpZ3MEaCqZ+PGMgBMTqs84MOW9IVs4Gpoy72laU8O4TMRm4MlbnPgi
5ikjjT9GUVzWxWnGVOZfgRwFPegk1kaPy3r0A1RAWSWMG9fqDj9wwUbtzSEBiUsE
xjYMADJZatP2xKLgZOOsigqa4jZe2DeKWO+S9Pio6nydZA+Orv6VRBH0P83MCm16
TPVfnZRQyARc0dscsJHlP/pGIjLXJpxUn2OxYIciJcIdiwmTkIc=
=lJtP
-----END PGP SIGNATURE-----

_______________________________________________
Sent through the Full Disclosure mailing list
https://nmap.org/mailman/listinfo/fulldisclosure
Web Archives & RSS: https://seclists.org/fulldisclosure/
```

---

[![Previous](/images/left-icon-16x16.png)](23)
[By Date](date.html#24)
[![Next](/images/right-icon-16x16.png)](25)

[![Previous](/images/left-icon-16x16.png)](23)
[By Thread](index.html#24)
[![Next](/images/right-icon-16x16.png)](25)

### Current thread:

* **APPLE-SA-04-16-2025-2 macOS Sequoia 15.4.1** *Apple Product Security via Fulldisclosure (Apr 23)*

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