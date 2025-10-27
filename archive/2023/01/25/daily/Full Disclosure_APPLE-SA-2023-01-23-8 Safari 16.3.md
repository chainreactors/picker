---
title: APPLE-SA-2023-01-23-8 Safari 16.3
url: https://seclists.org/fulldisclosure/2023/Jan/23
source: Full Disclosure
date: 2023-01-25
fetch_date: 2025-10-04T04:48:32.270981
---

# APPLE-SA-2023-01-23-8 Safari 16.3

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

[![Previous](/images/left-icon-16x16.png)](22)
[By Date](date.html#23)
[![Next](/images/right-icon-16x16.png)](24)

[![Previous](/images/left-icon-16x16.png)](22)
[By Thread](index.html#23)
[![Next](/images/right-icon-16x16.png)](18)

![](/shared/images/nst-icons.svg#search)

# APPLE-SA-2023-01-23-8 Safari 16.3

---

*From*: Apple Product Security via Fulldisclosure <fulldisclosure () seclists org>
*Date*: Mon, 23 Jan 2023 18:41:11 -0800

---

```
-----BEGIN PGP SIGNED MESSAGE-----
Hash: SHA256

APPLE-SA-2023-01-23-8 Safari 16.3

Safari 16.3 addresses the following issues.
Information about the security content is also available at
https://support.apple.com/HT213600.

WebKit
Available for: macOS Big Sur and macOS Monterey
Impact: Processing maliciously crafted web content may lead to
arbitrary code execution
Description: The issue was addressed with improved checks.
WebKit Bugzilla: 245464
CVE-2023-23496: ChengGang Wu, Yan Kang, YuHao Hu, Yue Sun, Jiming
Wang, JiKai Ren and Hang Shu of Institute of Computing Technology,
Chinese Academy of Sciences

WebKit
Available for: macOS Big Sur and macOS Monterey
Impact: Processing maliciously crafted web content may lead to
arbitrary code execution
Description: The issue was addressed with improved memory handling.
WebKit Bugzilla: 248268
CVE-2023-23518: YeongHyeon Choi (@hyeon101010), Hyeon Park
(@tree_segment), SeOk JEON (@_seokjeon), YoungSung Ahn (@_ZeroSung),
JunSeo Bae (@snakebjs0107), Dohyun Lee (@l33d0hyun) of Team ApplePIE
WebKit Bugzilla: 248268
CVE-2023-23517: YeongHyeon Choi (@hyeon101010), Hyeon Park
(@tree_segment), SeOk JEON (@_seokjeon), YoungSung Ahn (@_ZeroSung),
JunSeo Bae (@snakebjs0107), Dohyun Lee (@l33d0hyun) of Team ApplePIE

Additional recognition

WebKit
We would like to acknowledge Eliya Stein of Confiant for their
assistance.

Safari 16.3 may be obtained from the Mac App Store.
All information is also posted on the Apple Security Updates
web site: https://support.apple.com/en-us/HT201222.

This message is signed with Apple's Product Security PGP key,
and details are available at:
https://www.apple.com/support/security/pgp/
-----BEGIN PGP SIGNATURE-----

iQIzBAEBCAAdFiEEBP+4DupqR5Sgt1DB4RjMIDkeNxkFAmPPImAACgkQ4RjMIDke
NxmOtA/8C2w5NPXlcGH2m1GpCgxiEDQ/SreXYbyKbflivbXDwE1L+XAzTMhRIHF5
KjcqvjaoBh4oHN7IfQNq12/YE3+RMDF03J0sTefTT7SeLjN0wKM92jcqFWSGsLNI
UrsO3+jP89/2Di4IY3E07mu7iiZzgi8zGUPoMOxqJK8zpfYFXVe5LVyOfI3ETe2R
njH7et/tvW4KgVGyS4+tVHvC6Dts7efEKC10vgc4xdlWH69OHqUYT2eP7bX909MK
t8qnl5YW/W155rKWeZrngRP5gbwAWv6+Q5Jh6X/TZYi1S/5HEgBSUdn/8Cto9A2v
5FLZJLtYdoO137FqFMxH8ePWGGaL2JOVkeVYRZgkBnqZWMw4CUFgA6zW8i20e/aY
k1IaJsQzgrXzYEDjoXIq1MXgO5egY6pQNIyKtutRSpskWhoOFRXjKHLna0W1R+l6
YvfIpprHPlOae7koSwJJqQbq/XvD3XECtrf0xGqFiD5ntCNysFcy5hAEoswVpzkz
8368C6OU/bwOuryTlrImLDEsgJBozJk6CGhNgFMg81xzCMt7SzOqTR7u50P3VOki
9wt38tejRZyWTJiy3Tke/WlxrN0xl6vnBPsfDX7EW8+xC17mFAJlpnxy3f5Z1mdQ
q6mG51oZtFSgQR1cKUek/fnKpBNiauEk7A+Amm0nfzlpBT+4rKw=
=YCs8
-----END PGP SIGNATURE-----

_______________________________________________
Sent through the Full Disclosure mailing list
https://nmap.org/mailman/listinfo/fulldisclosure
Web Archives & RSS: https://seclists.org/fulldisclosure/
```

---

[![Previous](/images/left-icon-16x16.png)](22)
[By Date](date.html#23)
[![Next](/images/right-icon-16x16.png)](24)

[![Previous](/images/left-icon-16x16.png)](22)
[By Thread](index.html#23)
[![Next](/images/right-icon-16x16.png)](18)

### Current thread:

* **APPLE-SA-2023-01-23-8 Safari 16.3** *Apple Product Security via Fulldisclosure (Jan 23)*

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