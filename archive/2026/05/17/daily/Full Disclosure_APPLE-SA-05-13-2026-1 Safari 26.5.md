---
title: APPLE-SA-05-13-2026-1 Safari 26.5
url: https://seclists.org/fulldisclosure/2026/May/16
source: Full Disclosure
date: 2026-05-17
fetch_date: 2026-05-18T06:10:45.812073
---

# APPLE-SA-05-13-2026-1 Safari 26.5

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
![Next](/images/right-icon-16x16.png)

[![Previous](/images/left-icon-16x16.png)](15)
[By Thread](index.html#16)
![Next](/images/right-icon-16x16.png)

![](/shared/images/nst-icons.svg#search)

# APPLE-SA-05-13-2026-1 Safari 26.5

---

*From*: Apple Product Security via Fulldisclosure <fulldisclosure () seclists org>
*Date*: Wed, 13 May 2026 14:39:47 -0700

---

```
-----BEGIN PGP SIGNED MESSAGE-----
Hash: SHA256

APPLE-SA-05-13-2026-1 Safari 26.5

Safari 26.5 addresses the following issues.
Information about the security content is also available at
https://support.apple.com/en-us/127121.

Apple maintains a Security Releases page at
https://support.apple.com/100100 which lists recent
software updates with security advisories.

WebKit
Available for: macOS Sonoma and macOS Sequoia
Impact: Processing maliciously crafted web content may prevent Content
Security Policy from being enforced
Description: A validation issue was addressed with improved logic.
WebKit Bugzilla: 308906
CVE-2026-43660: Cantina

WebKit
Available for: macOS Sonoma and macOS Sequoia
Impact: Processing maliciously crafted web content may prevent Content
Security Policy from being enforced
Description: The issue was addressed with improved input validation.
WebKit Bugzilla: 308675
CVE-2026-28907: Cantina

WebKit
Available for: macOS Sonoma and macOS Sequoia
Impact: Processing maliciously crafted web content may disclose
sensitive user information
Description: This issue was addressed with improved access restrictions.
WebKit Bugzilla: 309698
CVE-2026-28962: Luke Francis, Vaagn Vardanian, kwak kiyong / kakaogames,
Vitaly Simonovich, Adel Bouachraoui, greenbynox

WebKit
Available for: macOS Sonoma and macOS Sequoia
Impact: Processing maliciously crafted web content may lead to an
unexpected Safari crash
Description: The issue was addressed with improved memory handling.
WebKit Bugzilla: 307669
CVE-2026-43658: Do Young Park

WebKit
Available for: macOS Sonoma and macOS Sequoia
Impact: Processing maliciously crafted web content may lead to an
unexpected process crash
Description: The issue was addressed with improved memory handling.
WebKit Bugzilla: 308545
CVE-2026-28905: Yuhao Hu, Yuanming Lai, Chenggang Wu, and Zhe Wang
WebKit Bugzilla: 308707
CVE-2026-28847: DARKNAVY (@DarkNavyOrg), Anonymous working with TrendAI
Zero Day Initiative, Daniel Rhea
WebKit Bugzilla: 309601
CVE-2026-28904: Luka Rački
WebKit Bugzilla: 310880
CVE-2026-28955: wac and Kookhwan Lee working with TrendAI Zero Day
Initiative
WebKit Bugzilla: 310303
CVE-2026-28903: Mateusz Krzywicki (iVerify.io)
WebKit Bugzilla: 309628
CVE-2026-28953: Maher Azzouzi
WebKit Bugzilla: 309861
CVE-2026-28902: Tristan Madani (@TristanInSec) from Talence Security,
Nathaniel Oh (@calysteon)
WebKit Bugzilla: 310207
CVE-2026-28901: Aisle offensive security research team (Joshua Rogers,
Luigino Camastra, Igor Morgenstern, and Guido Vranken), Maher Azzouzi,
Ngan Nguyen of Calif.io
WebKit Bugzilla: 311631
CVE-2026-28913: an anonymous researcher

WebKit
Available for: macOS Sonoma and macOS Sequoia
Impact: Processing maliciously crafted web content may lead to an
unexpected process crash
Description: A use-after-free issue was addressed with improved memory
management.
WebKit Bugzilla: 313939
CVE-2026-28883: kwak kiyong / kakaogames

WebKit
Available for: macOS Sonoma and macOS Sequoia
Impact: An app may be able to access sensitive user data
Description: This issue was addressed with improved data protection.
WebKit Bugzilla: 311228
CVE-2026-28958: Cantina

WebKit
Available for: macOS Sonoma and macOS Sequoia
Impact: Processing maliciously crafted web content may lead to an
unexpected process crash
Description: The issue was addressed with improved input validation.
WebKit Bugzilla: 310527
CVE-2026-28917: Vitaly Simonovich

WebKit
Available for: macOS Sonoma and macOS Sequoia
Impact: Processing maliciously crafted web content may lead to an
unexpected Safari crash
Description: A use-after-free issue was addressed with improved memory
management.
WebKit Bugzilla: 310234
CVE-2026-28947: dr3dd
WebKit Bugzilla: 310544
CVE-2026-28946: Gia Bui (@yabeow) from Calif.io, dr3dd, w0wbox
WebKit Bugzilla: 312180
CVE-2026-28942: Milad Nasr and Nicholas Carlini with Claude, Anthropic

WebKit
Available for: macOS Sonoma and macOS Sequoia
Impact: A malicious iframe may use another website’s download settings
Description: The issue was addressed with improved UI handling.
CVE-2026-28971: Khiem Tran
WebKit Bugzilla: 311288

WebRTC
Available for: macOS Sonoma and macOS Sequoia
Impact: Processing maliciously crafted web content may lead to an
unexpected process crash
Description: The issue was addressed with improved memory handling.
WebKit Bugzilla: 311131
CVE-2026-28944: Kenneth Hsu of Palo Alto Networks, Jérôme DJOUDER, dr3dd

Additional recognition

Safari
We would like to acknowledge sean mutuku for their assistance.

Safari Push Notifications
We would like to acknowledge Robert Mindo for their assistance.

WebKit
We would like to acknowledge Muhammad Zaid Ghifari (Mr.ZheeV),
Kalimantan Utara, Qadhafy Muhammad Tera, Vitaly Simonovich for their
assistance.

WebRTC
We would like to acknowledge Hyeonji Son (@jir4vv1t) of Demon Team for
their assistance.

Safari 26.5 may be obtained from the Mac App Store.

All information is also posted on the Apple Security Releases
web site: https://support.apple.com/100100.

This message is signed with Apple's Product Security PGP key,
and details are available at:
https://www.apple.com/support/security/pgp/

-----BEGIN PGP SIGNATURE-----

iQIzBAEBCAAdFiEEhjkl+zMLNwFiCT1o4Ifiq8DH7PUFAmoE52oACgkQ4Ifiq8DH
7PV9tw/8C759AP/3NbUY9aGa7CjwMsAcI+/Y3Gt1NpNpOiTqBO9fVzFR5rzkPELk
TGhNZ8fbGOMZji8i7tizeEbHzdZXaaVAvmBdFlhx8mmBtOMi1f8vFUQh+FeWiMDn
1BhlLMF2VigV8FcoyFiYIkcfaNYFnd3/QpDzQ4M0W7Wb/+xztzvqkgcTxQrhsNkN
WfxUkSzsZlcv6XOb/P9KqAr66Y1NRhVNeYFuEd3rcJYnL6nap4p0HlwgGmyU1Grs
PW0hOBmWo2HSFWOxOQ2akMtkOqpCiSjcI3FPwlMAagyhjieaZXT5/HrfCs0SelI2
kJVGpDiySNYxtKPbHYvDwjhVBRv2NaX6LFaNqVm20CaaFQGdF5sRGgTBJC7LtfCs
1PKnLcv2ov+isEYPEUsWjIWemFEi8nO+p9NkpqY6rMoOWbGKsi2IELbC5QNjgKVA
8/LEsQXW2Qf0RKQqlWk35Zv7ZWD2+ezjP/jNHYHvZJAN0IHR7HZOqfCm+V8uGndx
8iQDQ3R38mcsIUOYIMjuVP1PfVnMqyFSAVFkE/qtyTUk5TqsO4vdsQ/MKoxNXoW+
lHZT2q7ijQBGSteuax6XhH2r7hGxAXMols59EaJM3LZecDiqvOUloPC40hCItxEL
0VO4Cjuoz0UR2n4oafNs+AldAyuNnhlWEpYhgKbzkuySObOQ6TE=
=5v8r
-----END PGP SIGNATURE-----

_______________________________________________
Sent through the Full Disclosure mailing list
https://nmap.org/mailman/listinfo/fulldisclosure
Web Archives & RSS: https://seclists.org/fulldisclosure/
```

---

[![Previous](/images/left-icon-16x16.png)](15)
[By Date](date.html#16)
![Next](/images/right-icon-16x16.png)

[![Previous](/images/left-icon-16x16.png)](15)
[By Thread](index.html#16)
![Next](/images/right-icon-16x16.png)

### Current thread:

* **APPLE-SA-05-13-2026-1 Safari 26.5** *Apple Product Security via Fulldisclosure (May 17)*

![](/shared/images/nst-icons.svg#search)

## [Nmap Security Scanner](https://nmap.org/)

* [Ref Guide](https://nmap.org/book/man.html)* [Install Guide](https://nmap.org/book/install.html)* [Docs](https://nmap.org/docs.html)* [Download](https://nmap.org/download.html)* [Nmap OEM](https://nmap.org/oem/)

## [Npcap packet capture](https://npcap.com/)

* [User's Guide](https://npcap.com/guide/)* [API docs](https://npcap.com/guide/npcap-devguide.html#npcap-api)* [Download](https://npcap.com/#download)* [Npcap OEM](https...