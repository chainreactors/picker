---
title: APPLE-SA-07-27-2026-8 Safari 26.6
url: https://seclists.org/fulldisclosure/2026/Aug/23
source: Full Disclosure
date: 2026-08-06
fetch_date: 2026-08-07T04:30:05.238443
---

# APPLE-SA-07-27-2026-8 Safari 26.6

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
[![Next](/images/right-icon-16x16.png)](24)

![](/shared/images/nst-icons.svg#search)

# APPLE-SA-07-27-2026-8 Safari 26.6

---

*From*: Apple Product Security via Fulldisclosure <fulldisclosure () seclists org>
*Date*: Mon, 27 Jul 2026 17:27:54 -0700

---

```
-----BEGIN PGP SIGNED MESSAGE-----
Hash: SHA256

APPLE-SA-07-27-2026-8 Safari 26.6

Safari 26.6 addresses the following issues.
Information about the security content is also available at
https://support.apple.com/en-us/128073.

Apple maintains a Security Releases page at
https://support.apple.com/100100 which lists recent
software updates with security advisories.

Safari
Available for: macOS Sonoma and macOS Sequoia
Impact: An app may be able to access sensitive user data
Description: An authorization issue was addressed with improved state
management.
CVE-2026-43792: Ilya Andr (andrd3v)

WebKit
Available for: macOS Sonoma and macOS Sequoia
Impact: Processing maliciously crafted web content may result in the
disclosure of process memory
Description: The issue was addressed with improved memory handling.
WebKit Bugzilla: 308046
CVE-2026-43740: Arni Hardarson, Nathaniel Oh (@calysteon)

WebKit
Available for: macOS Sonoma and macOS Sequoia
Impact: Websites may know if the user has visited a given link
Description: This issue was addressed with improved checks.
WebKit Bugzilla: 316827
CVE-2026-64713: Kwak Kiyong, Song Nuri

WebKit
Available for: macOS Sonoma and macOS Sequoia
Impact: Visiting a website that frames malicious content may lead to UI
spoofing
Description: The issue was addressed with improved UI.
WebKit Bugzilla: 311660
CVE-2026-64730: Kagami Rosylight of Mozilla

WebKit
Available for: macOS Sonoma and macOS Sequoia
Impact: Maliciously crafted web content may violate iframe sandboxing
policy
Description: A permissions issue was addressed with improved validation.
WebKit Bugzilla: 313220
CVE-2026-64728: an anonymous researcher

WebKit
Available for: macOS Sonoma and macOS Sequoia
Impact: Processing maliciously crafted web content may lead to an
unexpected Safari crash
Description: A use-after-free issue was addressed with improved memory
management.
WebKit Bugzilla: 313521
CVE-2026-64783: 杉山 壮太, lattice, Behzad Najjarpour Jabbari (@_G4ru_),
Junyeong Lee, Mooth.ai, OGINOME Tomohito, Using GLM From Z.AI, Gia Bui
(@yabeow) from Calif.io

WebKit
Available for: macOS Sonoma and macOS Sequoia
Impact: Processing maliciously crafted web content may lead to an
unexpected Safari crash
Description: A memory corruption issue was addressed with improved state
management.
WebKit Bugzilla: 315082
CVE-2026-64757: Milad Nasr and Nicholas Carlini with Claude, Anthropic

WebKit
Available for: macOS Sonoma and macOS Sequoia
Impact: Visiting a website may lead to an app denial-of-service
Description: This issue was addressed through improved state management.
WebKit Bugzilla: 316816
CVE-2026-43804: Heiko Kiesel of SEEMOO, TU Darmstadt

WebKit
Available for: macOS Sonoma and macOS Sequoia
Impact: An app may be able to read files outside of its sandbox
Description: An access issue was addressed with improved access
restrictions.
WebKit Bugzilla: 314867
CVE-2026-43821: Brian Carpenter

WebKit Canvas
Available for: macOS Sonoma and macOS Sequoia
Impact: Processing maliciously crafted web content may lead to an
unexpected Safari crash
Description: A use-after-free issue was addressed with improved memory
management.
WebKit Bugzilla: 313935
CVE-2026-64718: OGINOME Tomohito, an anonymous researcher

WebRTC
Available for: macOS Sonoma and macOS Sequoia
Impact: Processing maliciously crafted web content may lead to an
unexpected Safari crash
Description: An out-of-bounds access issue was addressed with improved
bounds checking.
WebKit Bugzilla: 319404
CVE-2026-64719: Shaheen Fazim

Additional recognition

Safari Downloads
We would like to acknowledge Alfaz Hossain for their assistance.

WebKit
We would like to acknowledge Jaya Surya Kommireddy, Jaya surya
Kommireddy, Lukas Knittel (@kunte_ctf) of Ruhr-University Bochum, Nikos
Fanourakis of Technical University of Crete, Sotiris Ioannidis of
Technical University of Crete, Panagiotis Ilia of Cyprus University of
Technology, and Kostas Drakonakis of Technical University of Crete, Tony
Gorez (@tonygo_) for Reverse Society, Vitaly Simonovich, Youngjoon Kim
of Team-Atlanta & sslab at Georgia Tech, s3zer0 for their assistance.

WebKit Canvas
We would like to acknowledge Codex Security - Khai Tran, Daisuke
Hatakeyama and Ryohei Ueki (@SYZD Research), David Bors at Snyk Security
Labs, Giovanni Vignone and Robert van Eijk of Octane Security
(octane.security), Kwak Kiyong, Song nuri, Luat Nguyen (CyberJutsu
Academy), Tom Van Goethem, an anonymous researcher, dr3dd for their
assistance.

WebKit Storage
We would like to acknowledge Gurpreet Shergill, Luke Francis, Milad Nasr
and Nicholas Carlini with Claude, Anthropic, Oleh Konko of 1seal
(1seal.org), Vitaly Simonovich for their assistance.

Safari 26.6 may be obtained from the Mac App Store.

All information is also posted on the Apple Security Releases
web site: https://support.apple.com/100100.

This message is signed with Apple's Product Security PGP key,
and details are available at:
https://www.apple.com/support/security/pgp/

-----BEGIN PGP SIGNATURE-----

iQIzBAEBCAAdFiEEhjkl+zMLNwFiCT1o4Ifiq8DH7PUFAmpn4iMACgkQ4Ifiq8DH
7PUTig//dN43HRyvQWDfL6xMYj1NvUVLsWy8KXyMy33uJ4A3K+7H0lsFPpVusN5R
TAPd6SOjmrMAH04dveKIy6isyZUxG6P6Ez7nLZXkalw8UCRt0QDzFZJQT2dgPzrY
n57bQLrkw5HXAStWcviCbQCU9OjZVg44kWOHkI18AngBnpgF6Xcdn2KsO8A1UVj6
MLtFMg9AArwT+FMC1mqJv5IYGQZaDmcCNjz9+dm4ryHeOBpHm5t3stPr8fiOLgM8
nYuzKQc0ABsS+ne8/Ivter+iLDYM2ZH/EhswBDeIWuS7RTwAAsOwwMi6HGJAkpJU
WNrPz+yMY+oO1M/+6KRDP+3L6H1P4hSxgCRcreokE1JnjuvGgDEiq2s1r7GGJL2L
+RCnKAnL0c+B0EEedYH6Yi3jcLzaqKXnlfJBdVu7IKW7VjRcr07IwmemeIMfFF+O
ctCTvHUGT723b63D131qqCcnUgiprijhJ02Sw/IaHQckxUeNt/USY0eYuQbhfC+y
X1olXowGzDRXznuCze2L33jCjYy9MFJp/8K2s2ap4yTAR9jlohdP1GrxQcDj1NUu
XaDKOq3VUF2Z+S1OpEOVn8pgax4evoHyu8Nh7AsuwiTw07VKq3qfg/0SZbuOcnLq
aKYx+4St5AyBVKlzR489dL3V9fRkov1dwA3iPVLR35vCan8E83w=
=3nQh
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
[![Next](/images/right-icon-16x16.png)](24)

### Current thread:

* **APPLE-SA-07-27-2026-8 Safari 26.6** *Apple Product Security via Fulldisclosure (Aug 06)*

![](/shared/images/nst-icons.svg#search)

## [Nmap Security Scanner](https://nmap.org/)

* [Ref Guide](https://nmap.org/book/man.html)* [Install Guide](https://nmap.org/book/install.html)* [Docs](https://nmap.org/docs.html)* [Download](https://nmap.org/download.html)* [Nmap OEM](https://nmap.org/oem/)

## [Npcap packet capture](https://npcap.com/)

* [User's Guide](https://npcap.com/guide/)* [API docs](https://npcap.com/guide/npcap-devguide.html#npcap-api)* [Download](https://npcap.com/#download)* [Npcap OEM](https://npcap.com/oem/)

## [Security Lists](https://seclists.org/)

* [Nmap Announce](https://seclists.org/nmap-announce/)* [Nmap Dev](https://seclists.o...