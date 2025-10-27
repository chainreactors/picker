---
title: APPLE-SA-2023-01-24-1 tvOS 16.3
url: https://seclists.org/fulldisclosure/2023/Jan/27
source: Full Disclosure
date: 2023-01-28
fetch_date: 2025-10-04T05:06:00.318590
---

# APPLE-SA-2023-01-24-1 tvOS 16.3

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

[![Previous](/images/left-icon-16x16.png)](26)
[By Date](date.html#27)
[![Next](/images/right-icon-16x16.png)](28)

[![Previous](/images/left-icon-16x16.png)](26)
[By Thread](index.html#27)
[![Next](/images/right-icon-16x16.png)](28)

![](/shared/images/nst-icons.svg#search)

# APPLE-SA-2023-01-24-1 tvOS 16.3

---

*From*: Apple Product Security via Fulldisclosure <fulldisclosure () seclists org>
*Date*: Tue, 24 Jan 2023 13:24:07 -0800

---

```
-----BEGIN PGP SIGNED MESSAGE-----
Hash: SHA256

APPLE-SA-2023-01-24-1 tvOS 16.3

tvOS 16.3 addresses the following issues.
Information about the security content is also available at
https://support.apple.com/HT213601.

AppleMobileFileIntegrity
Available for: Apple TV 4K (all models) and Apple TV HD
Impact: An app may be able to access user-sensitive data
Description: This issue was addressed by enabling hardened runtime.
CVE-2023-23499: Wojciech Reguła (@_r3ggi) of SecuRing
(wojciechregula.blog)

ImageIO
Available for: Apple TV 4K (all models) and Apple TV HD
Impact: Processing an image may lead to a denial-of-service
Description: A memory corruption issue was addressed with improved
state management.
CVE-2023-23519: Yiğit Can YILMAZ (@yilmazcanyigit)

Kernel
Available for: Apple TV 4K (all models) and Apple TV HD
Impact: An app may be able to leak sensitive kernel state
Description: The issue was addressed with improved memory handling.
CVE-2023-23500: Pan ZhenPeng (@Peterpan0927) of STAR Labs SG Pte.
Ltd. (@starlabs_sg)

Kernel
Available for: Apple TV 4K (all models) and Apple TV HD
Impact: An app may be able to determine kernel memory layout
Description: An information disclosure issue was addressed by
removing the vulnerable code.
CVE-2023-23502: Pan ZhenPeng (@Peterpan0927) of STAR Labs SG Pte.
Ltd. (@starlabs_sg)

Kernel
Available for: Apple TV 4K (all models) and Apple TV HD
Impact: An app may be able to execute arbitrary code with kernel
privileges
Description: The issue was addressed with improved memory handling.
CVE-2023-23504: Adam Doupé of ASU SEFCOM

Maps
Available for: Apple TV 4K (all models) and Apple TV HD
Impact: An app may be able to bypass Privacy preferences
Description: A logic issue was addressed with improved state
management.
CVE-2023-23503: an anonymous researcher

Safari
Available for: Apple TV 4K (all models) and Apple TV HD
Impact: Visiting a website may lead to an app denial-of-service
Description: The issue was addressed with improved handling of
caches.
CVE-2023-23512: Adriatik Raci

Weather
Available for: Apple TV 4K (all models) and Apple TV HD
Impact: An app may be able to bypass Privacy preferences
Description: The issue was addressed with improved memory handling.
CVE-2023-23511: Wojciech Regula of SecuRing (wojciechregula.blog), an
anonymous researcher

WebKit
Available for: Apple TV 4K (all models) and Apple TV HD
Impact: Processing maliciously crafted web content may lead to
arbitrary code execution
Description: The issue was addressed with improved checks.
WebKit Bugzilla: 245464
CVE-2023-23496: ChengGang Wu, Yan Kang, YuHao Hu, Yue Sun, Jiming
Wang, JiKai Ren and Hang Shu of Institute of Computing Technology,
Chinese Academy of Sciences

WebKit
Available for: Apple TV 4K (all models) and Apple TV HD
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

Apple TV will periodically check for software updates. Alternatively,
you may manually check for software updates by selecting "Settings ->
System -> Software Update -> Update Software."  To check the current
version of software, select "Settings -> General -> About."
All information is also posted on the Apple Security Updates
web site: https://support.apple.com/en-us/HT201222.

This message is signed with Apple's Product Security PGP key,
and details are available at:
https://www.apple.com/support/security/pgp/
-----BEGIN PGP SIGNATURE-----

iQIzBAEBCAAdFiEEBP+4DupqR5Sgt1DB4RjMIDkeNxkFAmPQS+MACgkQ4RjMIDke
Nxl2xhAAu5swycPjzTAolynfVnOR8FvGiVeCUFfn2JpEFVXRiIMcZgQga7bb7cEk
0Abcm9FfLAq4z7SBTXh9csi1erT0bbT2/DK8PhEDsZz9MInzxXUTN9+ZrWlN/PLJ
ZIQZh1gwUGkf31DAaBQ15QYo6XukzwV++t1AkeY5CQsTEXf/rJhYH7E3kNWsqj+5
B6vAw0Xw7hLsZwfAv7W2khhLtiBa5sxtuJKRPJ/4xjBKfWZaeVjjgsTC0LLUN/3l
qxFI8H4QxQPxXtAt2O2wPGnR3WhfmDlGqgnYkj4IM8FlRnGedpD5O/kPoZNzRtKt
z7pRORoHD+o3KOY3UkRZ19sJEWEkeWJxHO6htRf/IsgbX1/eQJnIqSuOeLRJ3EDY
xCTUfiTU0NU3Iy/iDgpwllq4oU8rYeFJiPU4RNzndX+Z3+V/Tu9mc3rBax3A8gGi
bN5dKB0bGNCV2MnOlpuy5E7u56cfMlH04Gtj0j8L05t9yxYKiCuBVNBL0KjJB/cF
wjAl0ZoK8auWTDFKPJHGRGWtqR0svrV4qw5lPpQc+w26+xh8LHL8HzHr+pxHEZ75
4CUxi9L7w4hWieZgHNyWUj4xIlqhrefk+M6QqwxwwKSB/z2eiaOBHSCaKDOvg9JU
6w6VML1ezs/zpC5H0//PXTqK2o8XkaBNKQ0Ljx6zejIVwFbwHVQ=
=WvwW
-----END PGP SIGNATURE-----

_______________________________________________
Sent through the Full Disclosure mailing list
https://nmap.org/mailman/listinfo/fulldisclosure
Web Archives & RSS: https://seclists.org/fulldisclosure/
```

---

[![Previous](/images/left-icon-16x16.png)](26)
[By Date](date.html#27)
[![Next](/images/right-icon-16x16.png)](28)

[![Previous](/images/left-icon-16x16.png)](26)
[By Thread](index.html#27)
[![Next](/images/right-icon-16x16.png)](28)

### Current thread:

* **APPLE-SA-2023-01-24-1 tvOS 16.3** *Apple Product Security via Fulldisclosure (Jan 26)*

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
[![](/shared/images/nst-icons.svg#facebook)](https://facebook.com/nmap "...