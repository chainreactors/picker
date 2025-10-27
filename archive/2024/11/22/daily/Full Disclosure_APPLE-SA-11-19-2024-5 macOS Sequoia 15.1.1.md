---
title: APPLE-SA-11-19-2024-5 macOS Sequoia 15.1.1
url: https://seclists.org/fulldisclosure/2024/Nov/16
source: Full Disclosure
date: 2024-11-22
fetch_date: 2025-10-06T19:22:23.571426
---

# APPLE-SA-11-19-2024-5 macOS Sequoia 15.1.1

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

[![Previous](/images/left-icon-16x16.png)](15)
[By Date](date.html#16)
[![Next](/images/right-icon-16x16.png)](17)

[![Previous](/images/left-icon-16x16.png)](17)
[By Thread](index.html#16)
[![Next](/images/right-icon-16x16.png)](18)

![](/shared/images/nst-icons.svg#search)

# APPLE-SA-11-19-2024-5 macOS Sequoia 15.1.1

---

*From*: Apple Product Security via Fulldisclosure <fulldisclosure () seclists org>
*Date*: Tue, 19 Nov 2024 17:42:54 -0700

---

```
-----BEGIN PGP SIGNED MESSAGE-----
Hash: SHA256

APPLE-SA-11-19-2024-5 macOS Sequoia 15.1.1

macOS Sequoia 15.1.1 addresses the following issues.
Information about the security content is also available at
https://support.apple.com/121753.

Apple maintains a Security Releases page at
https://support.apple.com/100100 which lists recent
software updates with security advisories.

JavaScriptCore
Available for: macOS Sequoia
Impact: Processing maliciously crafted web content may lead to arbitrary
code execution. Apple is aware of a report that this issue may have been
actively exploited on Intel-based Mac systems.
Description: The issue was addressed with improved checks.
WebKit Bugzilla: 283063
CVE-2024-44308: Clément Lecigne and Benoît Sevens of Google's Threat
Analysis Group

WebKit
Available for: macOS Sequoia
Impact: Processing maliciously crafted web content may lead to a cross
site scripting attack. Apple is aware of a report that this issue may
have been actively exploited on Intel-based Mac systems.
Description: A cookie management issue was addressed with improved state
management.
WebKit Bugzilla: 283095
CVE-2024-44309: Clément Lecigne and Benoît Sevens of Google's Threat
Analysis Group

macOS Sequoia 15.1.1 may be obtained from the Mac App Store or Apple's
Software Downloads web site: https://support.apple.com/downloads/

All information is also posted on the Apple Security Releases
web site: https://support.apple.com/100100.

This message is signed with Apple's Product Security PGP key,
and details are available at:
https://www.apple.com/support/security/pgp/

-----BEGIN PGP SIGNATURE-----

iQIzBAEBCAAdFiEEsz9altA7uTI+rE/qX+5d1TXaIvoFAmc9JSQACgkQX+5d1TXa
Ivo92g/8Dm9sVuOeQTu56JLi2yAlbu9NK8Udb4ByFIsi63HWksJ6rK9LzZfTF8Yd
Z3SBk7aIHl9tMj2gJ6QJ71SwCdN/fTnAC9na5fZwUjdsjuH1uoPmiMSA48MDwmQC
vf6grIhskLNi0bQrpcKR1C79fmGlO7Nua3zmbvdvs41/3g3A7udvf2KpZTkkDrP4
+zwsVCJCu4xHTo5bU0NrM/Cbon+TO01/gyhnngZzl65bIPkhyeEDiVHW3K6aKDA8
XpClgMGe7ZIRao0hmqqK+YYPso/yDdUDpHlfEFL/YYseVThd+t6EPn4irWFPCPTv
usiMVUpOpqmMHfPaVO/uzwDR/wgpB8ws4BsBjytQ2q5ZZgyxsIUx6cEJazgbRXtI
UIJWgodel8AClhWrRo8c14rIuUH1jqMh8EcbimFdC62vSivuNgwNdBd5U2wRnELr
w1I65s3u7f3Qly8himbl+41ueYcgInsVld7206tk8Ygmm7zA4kupLBEH+EeK43c3
2P0NF7CMQCnJcwbEqusIUi8AOSN2VgGi9E6BjjJGnLhbbieX/ssKTTbv+mt0ctyq
5uB3WUZBDbhJKj8p/0+iBAlzZUJDkrudmy8No9Zc2ImTcZ61gP2Zbh/5lcI8hZu+
SKOrc+1s5nRW1FcGXL2ZzjtnmXnU6DGFfN7stVtTmVAg4dEWzeo=
=IY5p
-----END PGP SIGNATURE-----

_______________________________________________
Sent through the Full Disclosure mailing list
https://nmap.org/mailman/listinfo/fulldisclosure
Web Archives & RSS: https://seclists.org/fulldisclosure/
```

---

[![Previous](/images/left-icon-16x16.png)](15)
[By Date](date.html#16)
[![Next](/images/right-icon-16x16.png)](17)

[![Previous](/images/left-icon-16x16.png)](17)
[By Thread](index.html#16)
[![Next](/images/right-icon-16x16.png)](18)

### Current thread:

* **APPLE-SA-11-19-2024-5 macOS Sequoia 15.1.1** *Apple Product Security via Fulldisclosure (Nov 21)*

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