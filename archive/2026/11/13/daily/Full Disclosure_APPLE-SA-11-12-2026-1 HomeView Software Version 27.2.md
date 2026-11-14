---
title: APPLE-SA-11-12-2026-1 HomeView Software Version 27.2
url: https://seclists.org/fulldisclosure/2026/Nov/33
source: Full Disclosure
date: 2026-11-13
fetch_date: 2026-11-14T08:21:47.498021
---

# APPLE-SA-11-12-2026-1 HomeView Software Version 27.2

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

[![Previous](/images/left-icon-16x16.png)](32)
[By Date](date.html#33)
[![Next](/images/right-icon-16x16.png)](21)

[![Previous](/images/left-icon-16x16.png)](32)
[By Thread](index.html#33)
[![Next](/images/right-icon-16x16.png)](21)

![](/shared/images/nst-icons.svg#search)

# APPLE-SA-11-12-2026-1 HomeView Software Version 27.2

---

*From*: Apple Product Security via Fulldisclosure <fulldisclosure () seclists org>
*Date*: Thu, 12 Nov 2026 16:38:29 -0800

---

```
-----BEGIN PGP SIGNED MESSAGE-----
Hash: SHA256

APPLE-SA-11-12-2026-1 HomeView Software Version 27.2

HomeView Software Version 27.2 addresses the following issues.
Information about the security content is also available at
https://support.apple.com/149851.

Apple maintains a Security Releases page at
https://support.apple.com/100100 which lists recent
software updates with security advisories.

AirPlay
Available for: Apple HomeView
Impact: An attacker in Bluetooth range may be able to bypass the rate
limit on pairing code attempts
Description: A logic issue was addressed with improved state management.
CVE-2026-113968: Apple

App Intents
Available for: Apple HomeView
Impact: An app may be able to access sensitive user data
Description: An authorization issue was addressed with improved state
management.
CVE-2026-113963: László Várady

Bluetooth
Available for: Apple HomeView
Impact: An attacker in Bluetooth range may be able to corrupt process
memory
Description: A use-after-free issue was addressed with improved memory
management.
CVE-2026-113970: Apple

brotli
Available for: Apple HomeView
Impact: Processing maliciously crafted input may lead to memory
corruption
Description: An out-of-bounds write issue was addressed with improved
input validation.
CVE-2026-111497

CoreUtils
Available for: Apple HomeView
Impact: A malicious Bluetooth device may be able to establish a pairing
without user interaction
Description: This issue was addressed with improved checks.
CVE-2026-113965: Apple

CoreUtils
Available for: Apple HomeView
Impact: An attacker in Bluetooth range may be able to bypass the rate
limit on pairing code attempts and pair with a device without user
interaction
Description: A logic issue was addressed with improved state management.
CVE-2026-113964: an anonymous researcher

Messages
Available for: Apple HomeView
Impact: A remote attacker may be able to join an iMessage group chat and
receive its messages
Description: An authorization issue was addressed with improved
validation.
CVE-2026-113961: an anonymous researcher

Messages
Available for: Apple HomeView
Impact: A user added to an iMessage group may be able to access messages
sent before they joined
Description: This issue was addressed by removing the vulnerable code.
CVE-2026-113960: an anonymous researcher

rapportd
Available for: Apple HomeView
Impact: An attacker on the same network may be able to bypass the rate
limit on AirPlay pairing code attempts
Description: A logic issue was addressed with improved state management.
CVE-2026-113969: Apple

Apple HomeView automatically installs software updates by default.
Instructions on how to manually install Apple HomeView software
updates are available at https://support.apple.com/149085.

To check the software version on your Apple HomeView, open the
Settings app and choose General > About.

All information is also posted on the Apple Security Releases
web site: https://support.apple.com/100100.

This message is signed with Apple's Product Security PGP key,
and details are available at:
https://www.apple.com/support/security/pgp/

-----BEGIN PGP SIGNATURE-----

iQIzBAEBCAAdFiEEhjkl+zMLNwFiCT1o4Ifiq8DH7PUFAmr2VR4ACgkQ4Ifiq8DH
7PXqHA/9Ef7XNcYYv5FLb9sisFWQaoBXK3Ep1B0PQq7hY9bOSL9vAzJX0VoXGt5j
ju5d158WueSVKCzFcnsFp8FUpk0DlB+cABVGenZd4x2YO4gdSHK1d6QqMFCvwrwr
CheKrSRxvu2R+vBf1J9RzTg/zrSp//Svo2fWcVAsku44nGtLvDRPnR9cozxV84Tg
jgh6FQIVK/m7yFNWQeuOnMDhqaE35mqjXXYOo+6TAdZb89n0TUk2BG+OBk7j5bC9
+ZPc623+eA38O4aB9GB+U1ZvdDs+/UeZLEViTn/ei+BlAmRNoi8neej/siC6zU7j
Rk/m/u9XJJcMplw/WWFJZ38QLN+4SnGTZrTr9Mi7WN3CPIzFtc9V4n812lTapbpI
10S7y1PPsZsLMwQ2shdyn2vhYiJsTRfeHZkBirnA+ubDmKNzvDpkpidjCh4TdXNp
VhV9uE6m+meTXjSuQhavWp8D8qAYUveh2j9rd1nSqx8VPA5Dt6UshK7gEmFNn3Lc
M0oEXAgKZRF6/oihJJlVLbk7JtPyuidELWFAYYpyY2rUMwoEmjMhqaRrUp6YbCNf
XHOECOXADUAi4qcAgmFNKrzGu97BiOWxRIGksaTf18eQzgMFa2tWf1OPwjm2zNuS
KSdJ1urWakp7DkQ6vb9y9gnQ8MfqmgfFNggb+4raY2tOw+Uqvms=
=uLXd
-----END PGP SIGNATURE-----

_______________________________________________
Sent through the Full Disclosure mailing list
https://nmap.org/mailman/listinfo/fulldisclosure
Web Archives & RSS: https://seclists.org/fulldisclosure/
```

---

[![Previous](/images/left-icon-16x16.png)](32)
[By Date](date.html#33)
[![Next](/images/right-icon-16x16.png)](21)

[![Previous](/images/left-icon-16x16.png)](32)
[By Thread](index.html#33)
[![Next](/images/right-icon-16x16.png)](21)

### Current thread:

* **APPLE-SA-11-12-2026-1 HomeView Software Version 27.2** *Apple Product Security via Fulldisclosure (Nov 12)*

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