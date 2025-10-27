---
title: APPLE-SA-07-30-2025-1 Safari 18.6
url: https://seclists.org/fulldisclosure/2025/Aug/0
source: Full Disclosure
date: 2025-08-04
fetch_date: 2025-10-07T00:47:45.453342
---

# APPLE-SA-07-30-2025-1 Safari 18.6

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

![Previous](/images/left-icon-16x16.png)
[By Date](date.html#0)
[![Next](/images/right-icon-16x16.png)](1)

![Previous](/images/left-icon-16x16.png)
[By Thread](index.html#0)
[![Next](/images/right-icon-16x16.png)](1)

![](/shared/images/nst-icons.svg#search)

# APPLE-SA-07-30-2025-1 Safari 18.6

---

*From*: Apple Product Security via Fulldisclosure <fulldisclosure () seclists org>
*Date*: Wed, 30 Jul 2025 12:51:16 -0700

---

```
-----BEGIN PGP SIGNED MESSAGE-----
Hash: SHA256

APPLE-SA-07-30-2025-1 Safari 18.6

Safari 18.6 addresses the following issues.
Information about the security content is also available at
https://support.apple.com/124152.

Apple maintains a Security Releases page at
https://support.apple.com/100100 which lists recent
software updates with security advisories.

libxml2
Available for: macOS Ventura and macOS Sonoma
Impact: Processing a file may lead to memory corruption
Description: This is a vulnerability in open source code and Apple
Software is among the affected projects. The CVE-ID was assigned by a
third party. Learn more about the issue and CVE-ID at cve.org.
CVE-2025-7425: Sergei Glazunov of Google Project Zero

libxslt
Available for: macOS Ventura and macOS Sonoma
Impact: Processing maliciously crafted web content may lead to memory
corruption
Description: This is a vulnerability in open source code and Apple
Software is among the affected projects. The CVE-ID was assigned by a
third party. Learn more about the issue and CVE-ID at cve.org.
CVE-2025-7424: Ivan Fratric of Google Project Zero

Safari
Available for: macOS Ventura and macOS Sonoma
Impact: Processing maliciously crafted web content may lead to an
unexpected Safari crash
Description: A logic issue was addressed with improved checks.
CVE-2025-24188: Andreas Jaegersberger & Ro Achterberg of Nosebeard Labs

WebKit
Available for: macOS Ventura and macOS Sonoma
Impact: Processing maliciously crafted web content may lead to universal
cross site scripting
Description: This issue was addressed through improved state management.
WebKit Bugzilla: 285927
CVE-2025-43229: Martin Bajanik of Fingerprint, Ammar Askar

WebKit
Available for: macOS Ventura and macOS Sonoma
Impact: Visiting a malicious website may lead to address bar spoofing
Description: The issue was addressed with improved UI.
WebKit Bugzilla: 294374
CVE-2025-43228: Jaydev Ahire

WebKit
Available for: macOS Ventura and macOS Sonoma
Impact: Processing maliciously crafted web content may disclose
sensitive user information
Description: This issue was addressed through improved state management.
WebKit Bugzilla: 292888
CVE-2025-43227: Gilad Moav

WebKit
Available for: macOS Ventura and macOS Sonoma
Impact: Processing maliciously crafted web content may lead to memory
corruption
Description: The issue was addressed with improved memory handling.
WebKit Bugzilla: 291742
CVE-2025-31278: Yuhao Hu, Yan Kang, Chenggang Wu, and Xiaojie Wei
WebKit Bugzilla: 291745
CVE-2025-31277: Yuhao Hu, Yan Kang, Chenggang Wu, and Xiaojie Wei
WebKit Bugzilla: 293579
CVE-2025-31273: Yuhao Hu, Yan Kang, Chenggang Wu, and Xiaojie Wei

WebKit
Available for: macOS Ventura and macOS Sonoma
Impact: A download's origin may be incorrectly associated
Description: A logic issue was addressed with improved checks.
WebKit Bugzilla: 293994
CVE-2025-43240: Syarif Muhammad Sajjad

WebKit
Available for: macOS Ventura and macOS Sonoma
Impact: Processing maliciously crafted web content may lead to an
unexpected Safari crash
Description: The issue was addressed with improved memory handling.
WebKit Bugzilla: 292599
CVE-2025-43214: shandikri working with Trend Micro Zero Day Initiative,
Google V8 Security Team
WebKit Bugzilla: 292621
CVE-2025-43213: Google V8 Security Team
WebKit Bugzilla: 293197
CVE-2025-43212: Nan Wang (@eternalsakura13) and Ziling Chen

WebKit
Available for: macOS Ventura and macOS Sonoma
Impact: Processing web content may lead to a denial-of-service
Description: The issue was addressed with improved memory handling.
WebKit Bugzilla: 293730
CVE-2025-43211: Yuhao Hu, Yan Kang, Chenggang Wu, and Xiaojie Wei

WebKit
Available for: macOS Ventura and macOS Sonoma
Impact: Processing maliciously crafted web content may disclose internal
states of the app
Description: An out-of-bounds read was addressed with improved input
validation.
WebKit Bugzilla: 294182
CVE-2025-43265: HexRabbit (@h3xr4bb1t) from DEVCORE Research Team

WebKit
Available for: macOS Ventura and macOS Sonoma
Impact: Processing maliciously crafted web content may lead to an
unexpected Safari crash
Description: A use-after-free issue was addressed with improved memory
management.
WebKit Bugzilla: 295382
CVE-2025-43216: Ignacio Sanmillan (@ulexec)

WebKit
Available for: macOS Ventura and macOS Sonoma
Impact: Processing maliciously crafted web content may lead to an
unexpected Safari crash
Description: This is a vulnerability in open source code and Apple
Software is among the affected projects. The CVE-ID was assigned by a
third party. Learn more about the issue and CVE-ID at cve.org.
WebKit Bugzilla: 296459
CVE-2025-6558: ClÃ©ment Lecigne and Vlad Stolyarov of Google's Threat
Analysis Group

Additional recognition

libxml2
We would like to acknowledge Sergei Glazunov of Google Project Zero for
their assistance.

libxslt
We would like to acknowledge Ivan Fratric of Google Project Zero for
their assistance.

Safari
We would like to acknowledge Ameen Basha M K for their assistance.

WebKit
We would like to acknowledge Google V8 Security Team, Yuhao Hu, Yan
Kang, Chenggang Wu, and Xiaojie Wei, rheza (@ginggilBesel) for their
assistance.

Safari 18.6 may be obtained from the Mac App Store.

All information is also posted on the Apple Security Releases
web site: https://support.apple.com/100100.

This message is signed with Apple's Product Security PGP key,
and details are available at:
https://www.apple.com/support/security/pgp/

-----BEGIN PGP SIGNATURE-----

iQIzBAEBCAAdFiEEsz9altA7uTI+rE/qX+5d1TXaIvoFAmiKdYYACgkQX+5d1TXa
IvpU4BAAgIpa8SR7Tw92Ys50ooY+OcDFgOC/kLEQCLmOkkkIksCPSU1P9eGplHNl
rqug6dP7pqBy/jaSbw9NjKWkg2u5+n+qgXPJBo5Y1CqsC24hQjSTWNcllSANXAvu
mQ2yQjaImq0nNJalziLPx3CtvtH1G2xFMqQ9evVmpuMPiGqeIH7DF6lx/QydR8mD
QKJrzWH9SxOJasOXL0PYynNMCWAQh0LUHQIjIGpuc9DtLgts9OkHo2+TDTjGkmxI
i4Elsx7A0z6ZkV0EN1fqM2I4x0hpzYfWI7ylehgeJrKzoa/zhrN3iEL/19ZWs75c
SpE5j/aPjO9Q89gcOin98XkeWHp7nrmD2biFJ2cG2X8kQELSH7kF7oqKGBLBd0eE
Bh+CbfAdutu/942yHHdsQtz2PbiPSZQaXt+gaVNbKjLH9ubcm3pG9gL+YkV1iUUj
OOtRdF6HfH3yAMKeF4DL/g1nUl2CIZ3WHl4/Jyw+ud1uuAOpBwk7+d9SFDrRJD7g
eB1u+B9xf8xnR3+5hSjEWpEPrwnKAEdNZ+fu1qYIQQdiOwoLowAjrGPzzI25eunh
K1CU+p6pmy8b/6zmhxzkgA48MgMkwlQ76L5U8a8/o9SLYxP3ZG1lf95ojG43REHs
9yhyALyxMA41ieBgKwmYVIAPF6FRbrxPeqWfa/CmxoxTP0FiC1I=
=ePnH
-----END PGP SIGNATURE-----

_______________________________________________
Sent through the Full Disclosure mailing list
https://nmap.org/mailman/listinfo/fulldisclosure
Web Archives & RSS: https://seclists.org/fulldisclosure/
```

---

![Previous](/images/left-icon-16x16.png)
[By Date](date.html#0)
[![Next](/images/right-icon-16x16.png)](1)

![Previous](/images/left-icon-16x16.png)
[By Thread](index.html#0)
[![Next](/images/right-icon-16x16.png)](1)

### Current thread:

* **APPLE-SA-07-30-2025-1 Safari 18.6** *Apple Product Security via Fulldisclosure (Aug 02)*

![](/shared/images/nst-icons.svg#search)

## [Nmap Security Scanner](https://nmap.org/)

* [Ref Guide](https://nmap.org/book/man.html)* [Install Guide](https://nmap.org/book/install.html)* [Docs](https://nmap.org/docs....