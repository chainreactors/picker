---
title: APPLE-SA-01-27-2025-9 Safari 18.3
url: https://seclists.org/fulldisclosure/2025/Jan/20
source: Full Disclosure
date: 2025-01-29
fetch_date: 2025-10-06T20:11:38.213732
---

# APPLE-SA-01-27-2025-9 Safari 18.3

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

[![Previous](/images/left-icon-16x16.png)](19)
[By Date](date.html#20)
[![Next](/images/right-icon-16x16.png)](21)

[![Previous](/images/left-icon-16x16.png)](19)
[By Thread](index.html#20)
[![Next](/images/right-icon-16x16.png)](21)

![](/shared/images/nst-icons.svg#search)

# APPLE-SA-01-27-2025-9 Safari 18.3

---

*From*: Apple Product Security via Fulldisclosure <fulldisclosure () seclists org>
*Date*: Mon, 27 Jan 2025 14:55:14 -0800

---

```
-----BEGIN PGP SIGNED MESSAGE-----
Hash: SHA256

APPLE-SA-01-27-2025-9 Safari 18.3

Safari 18.3 addresses the following issues.
Information about the security content is also available at
https://support.apple.com/122074.

Apple maintains a Security Releases page at
https://support.apple.com/100100 which lists recent
software updates with security advisories.

Passwords
Available for: macOS Ventura and macOS Sonoma
Impact: A malicious app may be able to bypass browser extension
authentication
Description: A logging issue was addressed with improved data redaction.
CVE-2025-24169: Josh Parnham (@joshparnham)

Safari
Available for: macOS Ventura and macOS Sonoma
Impact: Visiting a malicious website may lead to user interface spoofing
Description: The issue was addressed with improved UI.
CVE-2025-24113: @RenwaX23

Safari
Available for: macOS Ventura and macOS Sonoma
Impact: Visiting a malicious website may lead to address bar spoofing
Description: The issue was addressed by adding additional logic.
CVE-2025-24128: @RenwaX23

WebKit
Available for: macOS Ventura and macOS Sonoma
Impact: A maliciously crafted webpage may be able to fingerprint the
user
Description: The issue was addressed with improved access restrictions
to the file system.
WebKit Bugzilla: 283117
CVE-2025-24143: an anonymous researcher

WebKit
Available for: macOS Ventura and macOS Sonoma
Impact: Processing web content may lead to a denial-of-service
Description: The issue was addressed with improved memory handling.
WebKit Bugzilla: 283889
CVE-2025-24158: Q1IQ (@q1iqF) of NUS CuriOSity and P1umer (@p1umer) of
Imperial Global Singapore

WebKit
Available for: macOS Ventura and macOS Sonoma
Impact: Processing maliciously crafted web content may lead to an
unexpected process crash
Description: This issue was addressed through improved state management.
WebKit Bugzilla: 284159
CVE-2025-24162: linjy of HKUS3Lab and chluo of WHUSecLab

WebKit Web Inspector
Available for: macOS Ventura and macOS Sonoma
Impact: Copying a URL from Web Inspector may lead to command injection
Description: A privacy issue was addressed with improved handling of
files.
WebKit Bugzilla: 283718
CVE-2025-24150: Johan Carlsson (joaxcar)

Safari 18.3 may be obtained from the Mac App Store.

All information is also posted on the Apple Security Releases
web site: https://support.apple.com/100100.

This message is signed with Apple's Product Security PGP key,
and details are available at:
https://www.apple.com/support/security/pgp/

-----BEGIN PGP SIGNATURE-----

iQIzBAEBCAAdFiEEsz9altA7uTI+rE/qX+5d1TXaIvoFAmeYApcACgkQX+5d1TXa
IvoQCw//TqhKnj3d2kyDG0N5s9Fk9/U3VT0A3v6rHKsw2R1pgJNNcKXq6hiPB9TG
e51XUpMXll5OtsyrgfEh0raf8BTFPXqVdkt3bhSpgDWVidE3uWxbgzh9HVCA4boH
CAIJMZ5xNTvC9q7wIMuZrWp7Jyt0gS/shXjmBfEPpbse3uXmErGvZJZo4PUqe/NP
ua0s+ThPtGRxTi40LfdubrJoVYeI1M351PDZn1alkhlnCQuytrLg2k7LGxf44dvD
9ziYmHaKrKI6DYFRv/6kIwyD5pt9URrF35ICZ33YoKoogSFGdhtQFOZxub/RU6P8
Fvga7ffGgmVd3KWWjFOHVRUrahnuIJxdp+qvQ0PyEjJ617zhzpoI9sjsABrwCkDR
ZJ+wsx0GAhyNyRvKqqiLVOQMK3U3oMcRavc7cUtv0gisiDI3wOnJWy9xCBSM1V8X
C5XoWSwUPDOxWt5lWXONMoR4JHTd1Ehdw9vkgKqXSPTzYldqh407NvT+S2FcnU7e
yySlElGFZHh30URlwVNksDoqFexmaPQyuNK3OgVifNZ514BMCmA1X16IoJ/6KOOi
YNCTv6m3lE+hIWVhdOhpGxNyqVTVVRlu7cFM4xhKy4E7hdvDixG6Mb8jWqinZrZj
fEObcCWeShBuPYYpxee1Ol8DtlV8p0fio4aCvKYDCPxcf56BPoo=
=0F3E
-----END PGP SIGNATURE-----

_______________________________________________
Sent through the Full Disclosure mailing list
https://nmap.org/mailman/listinfo/fulldisclosure
Web Archives & RSS: https://seclists.org/fulldisclosure/
```

---

[![Previous](/images/left-icon-16x16.png)](19)
[By Date](date.html#20)
[![Next](/images/right-icon-16x16.png)](21)

[![Previous](/images/left-icon-16x16.png)](19)
[By Thread](index.html#20)
[![Next](/images/right-icon-16x16.png)](21)

### Current thread:

* **APPLE-SA-01-27-2025-9 Safari 18.3** *Apple Product Security via Fulldisclosure (Jan 27)*

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