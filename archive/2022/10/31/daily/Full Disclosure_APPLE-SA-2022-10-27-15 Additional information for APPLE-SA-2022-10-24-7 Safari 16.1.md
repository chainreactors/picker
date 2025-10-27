---
title: APPLE-SA-2022-10-27-15 Additional information for APPLE-SA-2022-10-24-7 Safari 16.1
url: https://seclists.org/fulldisclosure/2022/Oct/51
source: Full Disclosure
date: 2022-10-31
fetch_date: 2025-10-03T21:21:51.986119
---

# APPLE-SA-2022-10-27-15 Additional information for APPLE-SA-2022-10-24-7 Safari 16.1

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

[![Previous](/images/left-icon-16x16.png)](50)
[By Date](date.html#51)
![Next](/images/right-icon-16x16.png)

[![Previous](/images/left-icon-16x16.png)](50)
[By Thread](index.html#51)
![Next](/images/right-icon-16x16.png)

![](/shared/images/nst-icons.svg#search)

# APPLE-SA-2022-10-27-15 Additional information for APPLE-SA-2022-10-24-7 Safari 16.1

---

*From*: Apple Product Security via Fulldisclosure <fulldisclosure () seclists org>
*Date*: Thu, 27 Oct 2022 18:23:53 -0700

---

```
-----BEGIN PGP SIGNED MESSAGE-----
Hash: SHA256

APPLE-SA-2022-10-27-15 Additional information for APPLE-SA-2022-10-24-7 Safari 16.1

Safari 16.1 addresses the following issues.
Information about the security content is also available at
https://support.apple.com/HT213495.

WebKit
Available for: macOS Big Sur and macOS Monterey
Impact: Visiting a malicious website may lead to user interface
spoofing
Description: The issue was addressed with improved UI handling.
WebKit Bugzilla: 243693
CVE-2022-42799: Jihwan Kim (@gPayl0ad), Dohyun Lee (@l33d0hyun)

WebKit
Available for: macOS Big Sur and macOS Monterey
Impact: Processing maliciously crafted web content may lead to
arbitrary code execution
Description: A type confusion issue was addressed with improved
memory handling.
WebKit Bugzilla: 244622
CVE-2022-42823: Dohyun Lee (@l33d0hyun) of SSD Labs

WebKit
Available for: macOS Big Sur and macOS Monterey
Impact: Processing maliciously crafted web content may disclose
sensitive user information
Description: A logic issue was addressed with improved state
management.
WebKit Bugzilla: 245058
CVE-2022-42824: Abdulrahman Alqabandi of Microsoft Browser
Vulnerability Research, Ryan Shin of IAAI SecLab at Korea University,
Dohyun Lee (@l33d0hyun) of DNSLab at Korea University

WebKit
Available for: macOS Big Sur and macOS Monterey
Impact: Processing maliciously crafted web content may disclose
internal states of the app
Description: A correctness issue in the JIT was addressed with
improved checks.
WebKit Bugzilla: 242964
CVE-2022-32923: Wonyoung Jung (@nonetype_pwn) of KAIST Hacking Lab
Entry added October 27, 2022

WebKit PDF
Available for: macOS Big Sur and macOS Monterey
Impact: Processing maliciously crafted web content may lead to
arbitrary code execution
Description: A use after free issue was addressed with improved
memory management.
WebKit Bugzilla: 242781
CVE-2022-32922: Yonghwi Jin (@jinmo123) at Theori working with Trend
Micro Zero Day Initiative

Additional recognition

WebKit
We would like to acknowledge Maddie Stone of Google Project Zero,
Narendra Bhati (@imnarendrabhati) of Suma Soft Pvt. Ltd., an
anonymous researcher for their assistance.

Safari 16.1 may be obtained from the Mac App Store.
All information is also posted on the Apple Security Updates
web site: https://support.apple.com/en-us/HT201222.

This message is signed with Apple's Product Security PGP key,
and details are available at:
https://www.apple.com/support/security/pgp/
-----BEGIN PGP SIGNATURE-----

iQIzBAEBCAAdFiEEBP+4DupqR5Sgt1DB4RjMIDkeNxkFAmNbKowACgkQ4RjMIDke
NxlhOg/+I94LgMI7No4xw6dub1rdzNTbMV6A0R14HXwA7PoMzXgXJotYFyAfGUY4
zd2fE9ixEuXqt+OsVrQ0/ZU4HcLEJLQk2ZkULoDfNeGiuJpi6k9VhPp6995XtLNb
zGZgMu5dOPBkYsSaM5XaVwLQPtsIbac3u/Uoo6l2TyyN1B2clsI1dS2IXS8DEHkr
2fCImTAcFfqIW7TZ6xqAdYOL5QLoJ8qXTcjSMaWtPpPzkfpZCTTwV8ifauK5rTQd
JsFf49RFWMNdZ3qHNRaENsFMh1Y+bMRIW6Xt41WKXhSPdNXonv93N472YGhMtt7Z
k+IuibGRVlwzc5Ri4AnQspBjhint6vo4vbJ39h1FoSzqTm3PruH+HGrhlfMTGR8/
0s/QDBLQbA+UlM5r6uinQ5pI771rRyHTCWOxLUVVopDOV9ImV36Y+INakc3pTXL1
420Wg31lCMO3cwwXyVYq/zDbCpJ2gDptSWTqlubli+omxMG7LRs0Vn9P4NTosVzk
jN49FHJE2moD8O0D+sia6+lhyVhcP8UIA3WtcXegVngrwL6sAoFa5SCp49wmbb/O
Ye1eysxuMR2xu7piVbUpGh0wRY50MbwwSWX0vRt0CwxcoiQK90lQFbqy2RFX4eN8
k/jjh3nPUl20WxgOfQfLfiY/9aPcQSzvcOzba2bSovdgyk8xH+o=
=3IzG
-----END PGP SIGNATURE-----

_______________________________________________
Sent through the Full Disclosure mailing list
https://nmap.org/mailman/listinfo/fulldisclosure
Web Archives & RSS: https://seclists.org/fulldisclosure/
```

---

[![Previous](/images/left-icon-16x16.png)](50)
[By Date](date.html#51)
![Next](/images/right-icon-16x16.png)

[![Previous](/images/left-icon-16x16.png)](50)
[By Thread](index.html#51)
![Next](/images/right-icon-16x16.png)

### Current thread:

* **APPLE-SA-2022-10-27-15 Additional information for APPLE-SA-2022-10-24-7 Safari 16.1** *Apple Product Security via Fulldisclosure (Oct 30)*

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