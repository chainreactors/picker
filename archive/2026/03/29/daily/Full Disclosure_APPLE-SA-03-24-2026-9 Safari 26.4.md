---
title: APPLE-SA-03-24-2026-9 Safari 26.4
url: https://seclists.org/fulldisclosure/2026/Mar/24
source: Full Disclosure
date: 2026-03-29
fetch_date: 2026-03-30T04:46:56.917491
---

# APPLE-SA-03-24-2026-9 Safari 26.4

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

# APPLE-SA-03-24-2026-9 Safari 26.4

---

*From*: Apple Product Security via Fulldisclosure <fulldisclosure () seclists org>
*Date*: Tue, 24 Mar 2026 17:04:55 -0700

---

```
-----BEGIN PGP SIGNED MESSAGE-----
Hash: SHA256

APPLE-SA-03-24-2026-9 Safari 26.4

Safari 26.4 addresses the following issues.
Information about the security content is also available at
https://support.apple.com/126800.

Apple maintains a Security Releases page at
https://support.apple.com/100100 which lists recent
software updates with security advisories.

WebKit
Available for: macOS Sonoma and macOS Sequoia
Impact: Processing maliciously crafted web content may prevent Content
Security Policy from being enforced
Description: This issue was addressed through improved state management.
WebKit Bugzilla: 304951
CVE-2026-20665: webb

WebKit
Available for: macOS Sonoma and macOS Sequoia
Impact: Processing maliciously crafted web content may bypass Same
Origin Policy
Description: A cross-origin issue in the Navigation API was addressed
with improved input validation.
WebKit Bugzilla: 306050
CVE-2026-20643: Thomas Espach

WebKit
Available for: macOS Sonoma and macOS Sequoia
Impact: Visiting a maliciously crafted website may lead to a cross-site
scripting attack
Description: A logic issue was addressed with improved checks.
WebKit Bugzilla: 305859
CVE-2026-28871: @hamayanhamayan

WebKit
Available for: macOS Sonoma and macOS Sequoia
Impact: Processing maliciously crafted web content may lead to an
unexpected process crash
Description: The issue was addressed with improved memory handling.
WebKit Bugzilla: 306136
CVE-2026-20664: Daniel Rhea, Söhnke Benedikt Fischedick (Tripton),
Emrovsky & Switch, Yevhen Pervushyn
WebKit Bugzilla: 307723
CVE-2026-28857: Narcis Oliveras Fontàs, Söhnke Benedikt Fischedick
(Tripton), Daniel Rhea, Nathaniel Oh (@calysteon)

WebKit
Available for: macOS Sonoma and macOS Sequoia
Impact: A malicious website may be able to access script message
handlers intended for other origins
Description: A logic issue was addressed with improved state management.
WebKit Bugzilla: 307014
CVE-2026-28861: Hongze Wu and Shuaike Dong from Ant Group Infrastructure
Security Team

WebKit
Available for: macOS Sonoma and macOS Sequoia
Impact: A malicious website may be able to process restricted web
content outside the sandbox
Description: The issue was addressed with improved memory handling.
WebKit Bugzilla: 308248
CVE-2026-28859: greenbynox, Arni Hardarson

WebKit Sandboxing
Available for: macOS Sonoma and macOS Sequoia
Impact: A maliciously crafted webpage may be able to fingerprint the
user
Description: An authorization issue was addressed with improved state
management.
WebKit Bugzilla: 306827
CVE-2026-20691: Gongyu Ma (@Mezone0)

Additional recognition

Safari
We would like to acknowledge @RenwaX23, Bikesh Parajuli, Farras Givari,
Syarif Muhammad Sajjad, Yair for their assistance.

Web Extensions
We would like to acknowledge Carlos Jeurissen, Rob Wu (robwu.nl) for
their assistance.

WebKit
We would like to acknowledge Vamshi Paili for their assistance.

WebKit Process Model
We would like to acknowledge Joseph Semaan for their assistance.

Safari 26.4 may be obtained from the Mac App Store.

All information is also posted on the Apple Security Releases
web site: https://support.apple.com/100100.

This message is signed with Apple's Product Security PGP key,
and details are available at:
https://www.apple.com/support/security/pgp/

-----BEGIN PGP SIGNATURE-----

iQIzBAEBCAAdFiEEhjkl+zMLNwFiCT1o4Ifiq8DH7PUFAmnDI3cACgkQ4Ifiq8DH
7PVxbhAAjKhMueqDcKyrInphYGj1a8Sop8rkiE/udJoWVtHMqalM9dRZ4xFdwgyC
smpY8Zo3oGJpU52GAaXETErpRlreGc+SOjnEYiZBUphEgbYSDFsVS+n5+MJZPUq1
yNrpTl+UWrtQtAM8brKmhGGsalZpB23MgkhnpXe44iKEqfBui3KAOXBLcS/QX7Le
hjQAJ7tTVuMQQR5FzQpEV0l3IOUfXtqTIc7MuNpBvZS39B3LOoECmyQ+Z3FXIFxR
1w+TKXURjPTF9Z5jGjONdTHMT2UCMfnE2ddXN5s+/sIfy9U0LZBx46YeX+OSbkkt
+cSBKY/YIR+qmd/gQUy0taP5D1IPmhHpG35krvkG0/BCLoNeErXFoJ7xHrmRy+G2
FNpj1IevWYCx5oMw/3Nqd9iZ4fnORbPFvQhNwNYB2EUPsmVha6GZfN42YKir82SH
jJi/OexQqcgTbiVdRj8IIYTGFeZWp+5ZBJTlRzq/nSJfOn92Y2mqEBPMkJRog0Qj
0HF5AyBBd2jDHxbHAn9C1xWnzDVQxtl4Hc/V8RFDrpBsRXLbonhtW3oPb6smY0de
bqkch7wqyz9rSB1bcuHYlD8j2xUB8ssFT9A6+r0cpia+E2ZHyBXuw1NlBUgqTw3Z
Ev3BI+dfPIL/EmJp2N9At0MEt4wIGUefuFlgAnINHj9DRroFktk=
=5McV
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

* **APPLE-SA-03-24-2026-9 Safari 26.4** *Apple Product Security via Fulldisclosure (Mar 28)*

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