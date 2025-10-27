---
title: APPLE-SA-2023-01-23-7 watchOS 9.3
url: https://seclists.org/fulldisclosure/2023/Jan/22
source: Full Disclosure
date: 2023-01-25
fetch_date: 2025-10-04T04:48:33.492145
---

# APPLE-SA-2023-01-23-7 watchOS 9.3

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

[![Previous](/images/left-icon-16x16.png)](21)
[By Date](date.html#22)
[![Next](/images/right-icon-16x16.png)](23)

[![Previous](/images/left-icon-16x16.png)](21)
[By Thread](index.html#22)
[![Next](/images/right-icon-16x16.png)](23)

![](/shared/images/nst-icons.svg#search)

# APPLE-SA-2023-01-23-7 watchOS 9.3

---

*From*: Apple Product Security via Fulldisclosure <fulldisclosure () seclists org>
*Date*: Mon, 23 Jan 2023 18:41:05 -0800

---

```
-----BEGIN PGP SIGNED MESSAGE-----
Hash: SHA256

APPLE-SA-2023-01-23-7 watchOS 9.3

watchOS 9.3 addresses the following issues.
Information about the security content is also available at
https://support.apple.com/HT213599.

AppleMobileFileIntegrity
Available for: Apple Watch Series 4 and later
Impact: An app may be able to access user-sensitive data
Description: This issue was addressed by enabling hardened runtime.
CVE-2023-23499: Wojciech Regula of SecuRing (wojciechregula.blog)

ImageIO
Available for: Apple Watch Series 4 and later
Impact: Processing an image may lead to a denial-of-service
Description: A memory corruption issue was addressed with improved
state management.
CVE-2023-23519: Yiğit Can YILMAZ (@yilmazcanyigit)

Kernel
Available for: Apple Watch Series 4 and later
Impact: An app may be able to leak sensitive kernel state
Description: The issue was addressed with improved memory handling.
CVE-2023-23500: Pan ZhenPeng (@Peterpan0927) of STAR Labs SG Pte.
Ltd. (@starlabs_sg)

Kernel
Available for: Apple Watch Series 4 and later
Impact: An app may be able to determine kernel memory layout
Description: An information disclosure issue was addressed by
removing the vulnerable code.
CVE-2023-23502: Pan ZhenPeng (@Peterpan0927) of STAR Labs SG Pte.
Ltd. (@starlabs_sg)

Kernel
Available for: Apple Watch Series 4 and later
Impact: An app may be able to execute arbitrary code with kernel
privileges
Description: The issue was addressed with improved memory handling.
CVE-2023-23504: Adam Doupé of ASU SEFCOM

Maps
Available for: Apple Watch Series 4 and later
Impact: An app may be able to bypass Privacy preferences
Description: A logic issue was addressed with improved state
management.
CVE-2023-23503: an anonymous researcher

Safari
Available for: Apple Watch Series 4 and later
Impact: Visiting a website may lead to an app denial-of-service
Description: The issue was addressed with improved handling of
caches.
CVE-2023-23512: Adriatik Raci

Screen Time
Available for: Apple Watch Series 4 and later
Impact: An app may be able to access information about a user’s
contacts
Description: A privacy issue was addressed with improved private data
redaction for log entries.
CVE-2023-23505: Wojciech Reguła of SecuRing (wojciechregula.blog)

Weather
Available for: Apple Watch Series 4 and later
Impact: An app may be able to bypass Privacy preferences
Description: The issue was addressed with improved memory handling.
CVE-2023-23511: Wojciech Regula of SecuRing (wojciechregula.blog), an
anonymous researcher

WebKit
Available for: Apple Watch Series 4 and later
Impact: Processing maliciously crafted web content may lead to
arbitrary code execution
Description: The issue was addressed with improved checks.
WebKit Bugzilla: 245464
CVE-2023-23496: ChengGang Wu, Yan Kang, YuHao Hu, Yue Sun, Jiming
Wang, JiKai Ren and Hang Shu of Institute of Computing Technology,
Chinese Academy of Sciences

WebKit
Available for: Apple Watch Series 4 and later
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

Kernel
We would like to acknowledge Nick Stenning of Replicate for their
assistance.

WebKit
We would like to acknowledge Eliya Stein of Confiant for their
assistance.

Instructions on how to update your Apple Watch software are available
at https://support.apple.com/kb/HT204641  To check the version on
your Apple Watch, open the Apple Watch app on your iPhone and select
"My Watch > General > About".  Alternatively, on your watch, select
"My Watch > General > About".
All information is also posted on the Apple Security Updates
web site: https://support.apple.com/en-us/HT201222.

This message is signed with Apple's Product Security PGP key,
and details are available at:
https://www.apple.com/support/security/pgp/
-----BEGIN PGP SIGNATURE-----

iQIzBAEBCAAdFiEEBP+4DupqR5Sgt1DB4RjMIDkeNxkFAmPPImAACgkQ4RjMIDke
NxlPXQ//eXfTfjIg6Y/1b0u3+Ht29Qjn7kw6Gh296lh6jlGatQ8zXyk1dGl6MKcp
ZTc7DFfL1VUN6MovOqW5qcR+MIV6hDiUd54ncDgjCXdHrtTG+bYchX5CJf5IIb67
gZP/2bBt4PQ+PHm3KqXPp7QauJWYD1d7AHChwqEbYchHxvgedB7Pu6nJvG3bnFmh
8ny/xrFEhtIDahw4MbicvK847aVpXyH6NxEoRY+8b9/4VocttfUPwMkGZTkVt/tz
9qfmKgjWpX2mTP9iaLlZdCUV/I4HcjTW0/nkDoaTBVDLW96DSeIo4nMM3qkcygRl
TPVlvm+3Nenib1b6PZ71B26IJbmGdwR02SEpUPDDXbTGZeWmcyXe7ncvwSIbcGRI
sPGMq6mEPi+rKTXKZeqPSDFnUlZJna2aNg9fPL9AZ1gwfNSbuhh5ZKQ9AAWA+k51
4QtoReAKUXinl8vr7BNVQSJSiZLMdgph4nCTYk1RA/VHDPjwaAJehDFUqKKKTuvp
h59J8OSw0HaWP2NcMEglO4/EXj09E3gfveQ74KtG+eDbBMKa+RArIgOZZaDOk2F1
6Fs316bNBI9tMxP34gFEvexTTBuQpoR/76pSQajlaSdas5Jeub2QeJVHkBPMdatD
HBbjpZhu4JcYqDVSDt58Ra5IsaM+OLkhvvCfi+UYxOiyZis3gn8=
=/vLS
-----END PGP SIGNATURE-----

_______________________________________________
Sent through the Full Disclosure mailing list
https://nmap.org/mailman/listinfo/fulldisclosure
Web Archives & RSS: https://seclists.org/fulldisclosure/
```

---

[![Previous](/images/left-icon-16x16.png)](21)
[By Date](date.html#22)
[![Next](/images/right-icon-16x16.png)](23)

[![Previous](/images/left-icon-16x16.png)](21)
[By Thread](index.html#22)
[![Next](/images/right-icon-16x16.png)](23)

### Current thread:

* **APPLE-SA-2023-01-23-7 watchOS 9.3** *Apple Product Security via Fulldisclosure (Jan 23)*

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

* [About/Contact](https://insecure.org/fyodor/)* [Privacy](https://insecure.org/privacy.html)* [Advertising](https://insecure.org/advertisin...