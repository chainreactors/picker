---
title: APPLE-SA-2022-11-01-1 Xcode 14.1
url: https://seclists.org/fulldisclosure/2022/Nov/1
source: Full Disclosure
date: 2022-11-09
fetch_date: 2025-10-03T22:08:48.734668
---

# APPLE-SA-2022-11-01-1 Xcode 14.1

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

[![Previous](/images/left-icon-16x16.png)](0)
[By Date](date.html#1)
[![Next](/images/right-icon-16x16.png)](2)

[![Previous](/images/left-icon-16x16.png)](0)
[By Thread](index.html#1)
[![Next](/images/right-icon-16x16.png)](2)

![](/shared/images/nst-icons.svg#search)

# APPLE-SA-2022-11-01-1 Xcode 14.1

---

*From*: Apple Product Security via Fulldisclosure <fulldisclosure () seclists org>
*Date*: Tue, 01 Nov 2022 11:30:49 -0700

---

```
-----BEGIN PGP SIGNED MESSAGE-----
Hash: SHA256

APPLE-SA-2022-11-01-1 Xcode 14.1

Xcode 14.1 addresses the following issues.
Information about the security content is also available at
https://support.apple.com/HT213496.

Git
Available for: macOS Monterey 12.5 and later
Impact: Multiple issues in git
Description: Multiple issues were addressed by updating to git
version 2.32.3.
CVE-2022-29187: Carlo Marcelo Arenas BelÃ³n and Johannes Schindelin

Git
Available for: macOS Monterey 12.5 and later
Impact: Cloning a malicious repository may result in the disclosure
of sensitive information
Description: This issue was addressed with improved checks.
CVE-2022-39253: Cory Snider of Mirantis

Git
Available for: macOS Monterey 12.5 and later
Impact: A remote user may cause an unexpected app termination or
arbitrary code execution if git shell is allowed as a login shell
Description: This issue was addressed with improved checks.
CVE-2022-39260: Kevin Backhouse of the GitHub Security Lab

IDE Xcode Server
Available for: macOS Monterey 12.5 and later
Impact: An app may be able to gain root privileges
Description: An injection issue was addressed with improved input
validation.
CVE-2022-42797: Tim Michaud (@TimGMichaud) of Moveworks.ai

Xcode 14.1 may be obtained from:
https://developer.apple.com/xcode/downloads/  To check that the Xcode
has been updated:  * Select Xcode in the menu bar * Select About
Xcode * The version after applying this update will be "Xcode 14.1".
All information is also posted on the Apple Security Updates
web site: https://support.apple.com/en-us/HT201222.

This message is signed with Apple's Product Security PGP key,
and details are available at:
https://www.apple.com/support/security/pgp/

All information is also posted on the Apple Security Updates
web site: https://support.apple.com/en-us/HT201222.

This message is signed with Apple's Product Security PGP key,
and details are available at:
https://www.apple.com/support/security/pgp/

-----BEGIN PGP SIGNATURE-----

iQIzBAEBCAAdFiEEBP+4DupqR5Sgt1DB4RjMIDkeNxkFAmNhY28ACgkQ4RjMIDke
NxkOOA/7BZu2PQGUMUbfn1Xz1WKUpJou+FUuBfDYlicI3H+ESpTzAcptcpEU8tuF
Iz9tG9ROTFkf/XHUm/+MX+Xmpet4hjkq0K5oySFGnhBqa8vPJBsGdT1y48ZT57zg
r3HQHgOlik+94Y1V/r2rxn8UEKLlRgS9zjqgjzUBs34OTxLuvRGWQIJD92Vh6qoH
oFf4/D5lvU5QEVm0SXhZFq2vD9GevxNDSv9PXm6V9ZYjuZ7RWVI9FMAUVo2K6EiA
jnZ7OIWW68e2DtkEBouyb3E7x/GOWvNBKKevuflD5WDPpw2y/MCi1nsX/TW0FMrB
iYaiS5y/wk8gWMXB9ADi1SMmN1bhBiHUJ/c0G8NJtGuc7oRUA1SerC/cdP5aQMcF
1JRSm30h3mK/V2r0lYDPsP+0bkg4ibNuTpJfZC2nzPffUZlRbgmVKSFqj+bYqQUi
WuZSEvNPOZHmLl9HzzilTSplQ9YzViqOPj9pn38W5LcKoStByS0yvuB1k91+szdY
pZQPWt+M1cvPIkpIjpq5BKa1lMYjkkRTLWUPrqjCkerOF9uI8YLIlJ+rEms2jtvv
eOWMU3d4H9/5xKYuuM3CvKenBYb+MCesN2DhppVlbGHxvlOUAMRjRtLc41tY96G+
BrZdYFXbjW9dMuWcO/IPIR17UAXpVN4IZasbNEfjQZsOZ9n+61Y=
=rHwp
-----END PGP SIGNATURE-----
_______________________________________________
Sent through the Full Disclosure mailing list
https://nmap.org/mailman/listinfo/fulldisclosure
Web Archives & RSS: https://seclists.org/fulldisclosure/
```

---

[![Previous](/images/left-icon-16x16.png)](0)
[By Date](date.html#1)
[![Next](/images/right-icon-16x16.png)](2)

[![Previous](/images/left-icon-16x16.png)](0)
[By Thread](index.html#1)
[![Next](/images/right-icon-16x16.png)](2)

### Current thread:

* **APPLE-SA-2022-11-01-1 Xcode 14.1** *Apple Product Security via Fulldisclosure (Nov 07)*

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