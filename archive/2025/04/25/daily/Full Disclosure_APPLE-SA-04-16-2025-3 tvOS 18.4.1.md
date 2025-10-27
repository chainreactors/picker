---
title: APPLE-SA-04-16-2025-3 tvOS 18.4.1
url: https://seclists.org/fulldisclosure/2025/Apr/25
source: Full Disclosure
date: 2025-04-25
fetch_date: 2025-10-06T22:07:43.558469
---

# APPLE-SA-04-16-2025-3 tvOS 18.4.1

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

[![Previous](/images/left-icon-16x16.png)](24)
[By Date](date.html#25)
[![Next](/images/right-icon-16x16.png)](26)

[![Previous](/images/left-icon-16x16.png)](24)
[By Thread](index.html#25)
[![Next](/images/right-icon-16x16.png)](26)

![](/shared/images/nst-icons.svg#search)

# APPLE-SA-04-16-2025-3 tvOS 18.4.1

---

*From*: Apple Product Security via Fulldisclosure <fulldisclosure () seclists org>
*Date*: Wed, 16 Apr 2025 13:53:47 -0700

---

```
-----BEGIN PGP SIGNED MESSAGE-----
Hash: SHA256

APPLE-SA-04-16-2025-3 tvOS 18.4.1

tvOS 18.4.1 addresses the following issues.
Information about the security content is also available at
https://support.apple.com/122401.

Apple maintains a Security Releases page at
https://support.apple.com/100100 which lists recent
software updates with security advisories.

CoreAudio
Available for: Apple TV HD and Apple TV 4K (all models)
Impact: Processing an audio stream in a maliciously crafted media file
may result in code execution. Apple is aware of a report that this issue
may have been exploited in an extremely sophisticated attack against
specific targeted individuals on iOS.
Description: A memory corruption issue was addressed with improved
bounds checking.
CVE-2025-31200: Apple and Google Threat Analysis Group

RPAC
Available for: Apple TV HD and Apple TV 4K (all models)
Impact: An attacker with arbitrary read and write capability may be able
to bypass Pointer Authentication. Apple is aware of a report that this
issue may have been exploited in an extremely sophisticated attack
against specific targeted individuals on iOS.
Description: This issue was addressed by removing the vulnerable code.
CVE-2025-31201: Apple

Apple TV will periodically check for software updates. Alternatively,
you may manually check for software updates by selecting
"Settings -> System -> Software Update -> Update Software."

To check the current version of software, select
"Settings -> General -> About.â€œ

All information is also posted on the Apple Security Releases
web site: https://support.apple.com/100100.

This message is signed with Apple's Product Security PGP key,
and details are available at:
https://www.apple.com/support/security/pgp/

-----BEGIN PGP SIGNATURE-----

iQIzBAEBCAAdFiEEsz9altA7uTI+rE/qX+5d1TXaIvoFAmgABnMACgkQX+5d1TXa
IvrBPxAAwsR/u23qMtnS+WtGXrNHF8i1Ibx2QzFq5+6FlBBuOB2JJG++y0CBkiRI
TueqJpmorYoi3lmH7DME4kvHZv+ch70yEsadwFOVAav6bzixng0Zdk+I16xR6PqA
6ay1+4MBNqmUa3ZEpla1RyUGHQ0RyiF1XxVEjH5iTTNdDLFDumtz1gX5Q70O3iDw
aGZZ3JyRvWXOvZMcb+pPfpEcNKK80n7W3g1bl9EIWlewuZJDLNWjych0tPGPsKUz
tX7Q5kN/TUyiatULPznKUpp1wafetJbHsOg6kEjOnQyxBxWw9BQjNj9wPZhOjTUa
VdG6NVKHNKw1FsRA0U/DIMiSTtcLCiX8g4RApcaIb0/HpvuoSHwC4DCQ4PaY88bV
59LQ2RGetjvJjCAxB6ENGQkxoJtIuOXIYU/TxY8qG98dcLRm14g/JrsMC5B+6nCz
D6/Y9axottqgvm5E/hRKOsMgSscb9aU9jhf65l3C1aHRIdQM7xNhLF93CgXTw/Wt
AKWSn6gO7RxwybVRBZqdOA39oeqomWZapoluy9PYKwF7bvHbKqsKTePuYJUjrzaI
qIWR0nTPxMkYRGeWkPkFhSfLnlDZs/zB4RLQY8lEpxR6WblercddUeusFjiN+zsR
2Jxo5vYgjH1Zd2ytcmq2uKkfOmHLA7R8ts88pUYo2mtpNGgtTZc=
=42zN
-----END PGP SIGNATURE-----

_______________________________________________
Sent through the Full Disclosure mailing list
https://nmap.org/mailman/listinfo/fulldisclosure
Web Archives & RSS: https://seclists.org/fulldisclosure/
```

---

[![Previous](/images/left-icon-16x16.png)](24)
[By Date](date.html#25)
[![Next](/images/right-icon-16x16.png)](26)

[![Previous](/images/left-icon-16x16.png)](24)
[By Thread](index.html#25)
[![Next](/images/right-icon-16x16.png)](26)

### Current thread:

* **APPLE-SA-04-16-2025-3 tvOS 18.4.1** *Apple Product Security via Fulldisclosure (Apr 23)*

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