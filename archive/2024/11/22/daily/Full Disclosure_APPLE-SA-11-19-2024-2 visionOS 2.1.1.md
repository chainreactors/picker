---
title: APPLE-SA-11-19-2024-2 visionOS 2.1.1
url: https://seclists.org/fulldisclosure/2024/Nov/12
source: Full Disclosure
date: 2024-11-22
fetch_date: 2025-10-06T19:22:32.095380
---

# APPLE-SA-11-19-2024-2 visionOS 2.1.1

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

[![Previous](/images/left-icon-16x16.png)](11)
[By Date](date.html#12)
[![Next](/images/right-icon-16x16.png)](13)

[![Previous](/images/left-icon-16x16.png)](11)
[By Thread](index.html#12)
[![Next](/images/right-icon-16x16.png)](13)

![](/shared/images/nst-icons.svg#search)

# APPLE-SA-11-19-2024-2 visionOS 2.1.1

---

*From*: Apple Product Security via Fulldisclosure <fulldisclosure () seclists org>
*Date*: Tue, 19 Nov 2024 17:40:23 -0700

---

```
-----BEGIN PGP SIGNED MESSAGE-----
Hash: SHA256

APPLE-SA-11-19-2024-2 visionOS 2.1.1

visionOS 2.1.1 addresses the following issues.
Information about the security content is also available at
https://support.apple.com/121755.

Apple maintains a Security Releases page at
https://support.apple.com/100100 which lists recent
software updates with security advisories.

JavaScriptCore
Available for: Apple Vision Pro
Impact: Processing maliciously crafted web content may lead to arbitrary
code execution. Apple is aware of a report that this issue may have been
actively exploited on Intel-based Mac systems.
Description: The issue was addressed with improved checks.
WebKit Bugzilla: 283063
CVE-2024-44308: Clément Lecigne and Benoît Sevens of Google's Threat
Analysis Group

WebKit
Available for: Apple Vision Pro
Impact: Processing maliciously crafted web content may lead to a cross
site scripting attack. Apple is aware of a report that this issue may
have been actively exploited on Intel-based Mac systems.
Description: A cookie management issue was addressed with improved state
management.
WebKit Bugzilla: 283095
CVE-2024-44309: Clément Lecigne and Benoît Sevens of Google's Threat
Analysis Group

Instructions on how to update visionOS are available at
https://support.apple.com/118481. To check the software version
on your Apple Vision Pro, open the Settings app and choose General >
About.

All information is also posted on the Apple Security Releases
web site: https://support.apple.com/100100.

This message is signed with Apple's Product Security PGP key,
and details are available at:
https://www.apple.com/support/security/pgp/

-----BEGIN PGP SIGNATURE-----

iQIzBAEBCAAdFiEEsz9altA7uTI+rE/qX+5d1TXaIvoFAmc9I6MACgkQX+5d1TXa
IvrozQ//XVZryii8/3UFGmSvaAOBz3TwiSq0L1Od20kVvOZUUZEET0r52Y1RcQkt
sYltOgPj/Ea9L2xXUkLv8TcjWA6GkeaDWclVi9OdhNYewLXMBxwE0rDvIRVgkAwu
Dg7McdcBO0079b+9sYzMSYQFnZXgfdWImKHAhHIHjUzNDWi7n3rB19QbGJwwyTsy
lXKYKKRMxuscopPlB7Fxmtl66SWdHth0KKZj13vWNY0ZikUKNcZizgWzojWbdiKw
ozL/gJKJTLnSTMETl09q2Dy51Nk5QJ+IINXDsgqkXuy1XwlDssTHg+aQkBgn16aQ
w17rluBZ3UDm9yqtXSJOan/MQR7wvMTZzk67Rp0bBBs+SgGQ24O/H7wTrPCQiwHm
tj2HoKCCNIM3yLWJwJzn7+fB24pPL7y7adX/+mPVfiNvVIOHU5ExxrcXi70ROVky
hxzrxw6Hz01QuT8q3LZ701iPdmdp/Rcb5Vn5xhWDSac9OohGTo9Rds8li801VQR1
ZReGbo4tTs50LYQa1gu4b5nkQRWnATeeF2BdLkw6hbdCybquuHe4dvJ+Jg6cMjGS
vaRpbdrA/odPE2hfJItCaxpotCLAtpgGj+tQahHyZISYSrXrZdoWZiKBjiLWxjik
Pr+NGIs/CzXI6kwxBtLmUkJLikU1oxTiFKAA8V1mTuUCfh64lsc=
=ZhBy
-----END PGP SIGNATURE-----
_______________________________________________
Sent through the Full Disclosure mailing list
https://nmap.org/mailman/listinfo/fulldisclosure
Web Archives & RSS: https://seclists.org/fulldisclosure/
```

---

[![Previous](/images/left-icon-16x16.png)](11)
[By Date](date.html#12)
[![Next](/images/right-icon-16x16.png)](13)

[![Previous](/images/left-icon-16x16.png)](11)
[By Thread](index.html#12)
[![Next](/images/right-icon-16x16.png)](13)

### Current thread:

* **APPLE-SA-11-19-2024-2 visionOS 2.1.1** *Apple Product Security via Fulldisclosure (Nov 21)*

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