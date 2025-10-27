---
title: APPLE-SA-2022-12-13-9 Safari 16.2
url: https://seclists.org/fulldisclosure/2022/Dec/28
source: Full Disclosure
date: 2022-12-22
fetch_date: 2025-10-04T02:15:01.710723
---

# APPLE-SA-2022-12-13-9 Safari 16.2

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

[![Previous](/images/left-icon-16x16.png)](27)
[By Date](date.html#28)
[![Next](/images/right-icon-16x16.png)](29)

[![Previous](/images/left-icon-16x16.png)](27)
[By Thread](index.html#28)
[![Next](/images/right-icon-16x16.png)](29)

![](/shared/images/nst-icons.svg#search)

# APPLE-SA-2022-12-13-9 Safari 16.2

---

*From*: Apple Product Security via Fulldisclosure <fulldisclosure () seclists org>
*Date*: Tue, 13 Dec 2022 16:35:25 -0800

---

```
-----BEGIN PGP SIGNED MESSAGE-----
Hash: SHA256

APPLE-SA-2022-12-13-9 Safari 16.2

Safari 16.2 addresses the following issues.
Information about the security content is also available at
https://support.apple.com/HT213537.

WebKit
Available for: macOS Big Sur and macOS Monterey
Impact: Processing maliciously crafted web content may lead to
arbitrary code execution
Description: A use after free issue was addressed with improved
memory management.
WebKit Bugzilla: 245521
CVE-2022-42867: Maddie Stone of Google Project Zero

WebKit
Available for: macOS Big Sur and macOS Monterey
Impact: Processing maliciously crafted web content may lead to
arbitrary code execution
Description: A memory consumption issue was addressed with improved
memory handling.
WebKit Bugzilla: 245466
CVE-2022-46691: an anonymous researcher

WebKit
Available for: macOS Big Sur and macOS Monterey
Impact: Processing maliciously crafted web content may bypass Same
Origin Policy
Description: A logic issue was addressed with improved state
management.
WebKit Bugzilla: 246783
CVE-2022-46692: KirtiKumar Anandrao Ramchandani

WebKit
Available for: macOS Big Sur and macOS Monterey
Impact: Processing maliciously crafted web content may result in the
disclosure of process memory
Description: The issue was addressed with improved memory handling.
CVE-2022-42852: hazbinhotel working with Trend Micro Zero Day
Initiative

WebKit
Available for: macOS Big Sur and macOS Monterey
Impact: Processing maliciously crafted web content may lead to
arbitrary code execution
Description: A memory corruption issue was addressed with improved
input validation.
WebKit Bugzilla: 246942
CVE-2022-46696: Samuel Groß of Google V8 Security
WebKit Bugzilla: 247562
CVE-2022-46700: Samuel Groß of Google V8 Security

WebKit
Available for: macOS Big Sur and macOS Monterey
Impact: Processing maliciously crafted web content may disclose
sensitive user information
Description: A logic issue was addressed with improved checks.
CVE-2022-46698: Dohyun Lee (@l33d0hyun) of SSD Secure Disclosure Labs
& DNSLab, Korea Univ.

WebKit
Available for: macOS Big Sur and macOS Monterey
Impact: Processing maliciously crafted web content may lead to
arbitrary code execution
Description: A memory corruption issue was addressed with improved
state management.
WebKit Bugzilla: 247420
CVE-2022-46699: Samuel Groß of Google V8 Security
WebKit Bugzilla: 244622
CVE-2022-42863: an anonymous researcher

WebKit
Available for: macOS Big Sur and macOS Monterey
Impact: Processing maliciously crafted web content may lead to
arbitrary code execution. Apple is aware of a report that this issue
may have been actively exploited against versions of iOS released
before iOS 15.1.
Description: A type confusion issue was addressed with improved state
handling.
WebKit Bugzilla: 248266
CVE-2022-42856: Clément Lecigne of Google's Threat Analysis Group

Additional recognition

WebKit
We would like to acknowledge an anonymous researcher, scarlet for
their assistance.

Safari 16.2 may be obtained from the Mac App Store.
All information is also posted on the Apple Security Updates
web site: https://support.apple.com/en-us/HT201222.

This message is signed with Apple's Product Security PGP key,
and details are available at:
https://www.apple.com/support/security/pgp/
-----BEGIN PGP SIGNATURE-----

iQIzBAEBCAAdFiEEBP+4DupqR5Sgt1DB4RjMIDkeNxkFAmOZFX0ACgkQ4RjMIDke
NxniRQ/+LTObFcBEWogS56q3+7wjz2BgzBZYn4gwNGfvXf0zZfmXnTE0WXUolVa1
8/glHt7Tu5/KKfy6JDqmQvrF6fo2YpBgH0wrux/j4VPVCeaaOa2gXRAw0CBa4e4E
OabGVEXEsgJjyE4MSMKh8Hn1VD4ANTPPKn5jWmDsCsSS2zEo94gD7Mkqh81CeFoV
Yhmbv87nZAdEz2nHUkoM6PmN8SPAY5VtRp6i1rbkpcmMfs3VyA/ehnkfBGQK2xH7
vHpx2yyoXlqwR0zc7uHEge13e8kZ1Zh8UdIecgJuoyOvvmRR5DcchMFUYpUq8JcZ
JOqN2lsRBu52WvoEGCkD80/PWamhD+CJWeMvgbvEZSOiNKKOSY1qO0w0NsGMPXCh
6xdcjfeTpslNn4zNUfaAwnUGIyxbIsNNHIgw3VX5GnFihpEsknBqbjxTLCBrDdFE
T5xuHPBj7vXEW3V2ZXVt2MctWCr0GQdHt66C2m3gAEhL9xoN6YMEXLI0RVgUHmaf
hOY/EZMIGm1cL33OvMKuvWCJuGW81+2+LJSwoscguhrj7Jb2qTOL2w06VDyNftuY
F876pPWZgEj1O7DAtL9OP8IdrpSmQnAkvVUIZA6Sx3MaxTdl4f6lG4NlcsMGz+se
PxxMCYWi8f/sPNxSdfoYardNkQcPsKm13UFu+Q9nSuV0A+x0qgA=
=F0qN
-----END PGP SIGNATURE-----

_______________________________________________
Sent through the Full Disclosure mailing list
https://nmap.org/mailman/listinfo/fulldisclosure
Web Archives & RSS: https://seclists.org/fulldisclosure/
```

---

[![Previous](/images/left-icon-16x16.png)](27)
[By Date](date.html#28)
[![Next](/images/right-icon-16x16.png)](29)

[![Previous](/images/left-icon-16x16.png)](27)
[By Thread](index.html#28)
[![Next](/images/right-icon-16x16.png)](29)

### Current thread:

* **APPLE-SA-2022-12-13-9 Safari 16.2** *Apple Product Security via Fulldisclosure (Dec 20)*

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