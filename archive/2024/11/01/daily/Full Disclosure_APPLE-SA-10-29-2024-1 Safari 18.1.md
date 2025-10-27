---
title: APPLE-SA-10-29-2024-1 Safari 18.1
url: https://seclists.org/fulldisclosure/2024/Oct/19
source: Full Disclosure
date: 2024-11-01
fetch_date: 2025-10-06T19:21:08.161716
---

# APPLE-SA-10-29-2024-1 Safari 18.1

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

[![Previous](/images/left-icon-16x16.png)](18)
[By Date](date.html#19)
[![Next](/images/right-icon-16x16.png)](20)

[![Previous](/images/left-icon-16x16.png)](18)
[By Thread](index.html#19)
[![Next](/images/right-icon-16x16.png)](20)

![](/shared/images/nst-icons.svg#search)

# APPLE-SA-10-29-2024-1 Safari 18.1

---

*From*: Apple Product Security via Fulldisclosure <fulldisclosure () seclists org>
*Date*: Tue, 29 Oct 2024 16:29:03 -0700

---

```
-----BEGIN PGP SIGNED MESSAGE-----
Hash: SHA256

APPLE-SA-10-29-2024-1 Safari 18.1

Safari 18.1 addresses the following issues.
Information about the security content is also available at
https://support.apple.com/121571.

Apple maintains a Security Releases page at
https://support.apple.com/100100 which lists recent
software updates with security advisories.

Safari Downloads
Available for: macOS Ventura and macOS Sonoma
Impact: An attacker may be able to misuse a trust relationship to
download malicious content
Description: This issue was addressed through improved state management.
CVE-2024-44259: Narendra Bhati, Manager of Cyber Security at Suma Soft
Pvt. Ltd, Pune (India)

Safari Private Browsing
Available for: macOS Ventura and macOS Sonoma
Impact: Private browsing may leak some browsing history
Description: An information leakage was addressed with additional
validation.
CVE-2024-44229: Lucas Di Tomase

WebKit
Available for: macOS Ventura and macOS Sonoma
Impact: Processing maliciously crafted web content may prevent Content
Security Policy from being enforced
Description: The issue was addressed with improved checks.
WebKit Bugzilla: 278765
CVE-2024-44296: Narendra Bhati, Manager of Cyber Security at Suma Soft
Pvt. Ltd, Pune (India)

WebKit
Available for: macOS Ventura and macOS Sonoma
Impact: Processing maliciously crafted web content may lead to an
unexpected process crash
Description: A memory corruption issue was addressed with improved input
validation.
WebKit Bugzilla: 279780
CVE-2024-44244: an anonymous researcher, Q1IQ (@q1iqF) and P1umer
(@p1umer)

Additional recognition

Safari Private Browsing
We would like to acknowledge an anonymous researcher, r00tdaddy for
their assistance.

Safari Tabs
We would like to acknowledge Jaydev Ahire for their assistance.

Safari 18.1 may be obtained from the Mac App Store.

All information is also posted on the Apple Security Releases
web site: https://support.apple.com/100100.

This message is signed with Apple's Product Security PGP key,
and details are available at:
https://www.apple.com/support/security/pgp/

-----BEGIN PGP SIGNATURE-----

iQIzBAEBCAAdFiEEsz9altA7uTI+rE/qX+5d1TXaIvoFAmchbpEACgkQX+5d1TXa
Ivr5gBAAk50bIQ2NvoHDWo1ss9TLbGh9aa2RAHRPS0HqbBmnolc5tcrB1wKorkaf
FF6lACO/OOti2KjAX44zfLl+9zHMsEFzDkmrY8VosFkYAaLUOly/xYaCUcQcuhLC
VZy4Moviip3ImFDvR/EjO8vI/7GAjt3XafvRf1k5+w5xzmCuM8mhzLSfs1s4/lxd
EThQBB7oA18grjnxJqAh9tBwquUkfmGuY9twsNH5qccv+wgw9gYvCIr0jbtCn2vz
K5FHY/RDmMOfoLZ3am0JqrWd/7uO3bWHYQzS5H501x2tsLJw6Hwy9u+P2NxvRzXd
pu6WJ22Adei85x5o34W+K42iannlzpgMnMeT81khVzVTY1HKPBikZ1wS13kZ9UyY
j9dnW0NReyKhDYzFPiTehgC2mErmFWzLtRzxzs/Af7iVadAXw+6evBtP5FIzEqFX
FfbhS+0icaU3FGklxcD+5++T+OKvo5hDAVjp7lGbBv5C2WvlpuNfmdIXkqYbzpdv
mIujHNTWNYArlIkXr7vUVOHdB//BtfbIGZdjddYpZbx7q6KxX+z8q+NQ/8ESEUXZ
KIF0cOAI1P2nVdALfpMaqKVFJa+BfwhWklscDDgPOpVQy0I5cIFJj7MVves534js
sR+tn4B5jKfe6tmLy1xkgqpTYcdPe/TzW0tc6IRidvYVk3zhpMA=
=9Fs5
-----END PGP SIGNATURE-----

_______________________________________________
Sent through the Full Disclosure mailing list
https://nmap.org/mailman/listinfo/fulldisclosure
Web Archives & RSS: https://seclists.org/fulldisclosure/
```

---

[![Previous](/images/left-icon-16x16.png)](18)
[By Date](date.html#19)
[![Next](/images/right-icon-16x16.png)](20)

[![Previous](/images/left-icon-16x16.png)](18)
[By Thread](index.html#19)
[![Next](/images/right-icon-16x16.png)](20)

### Current thread:

* **APPLE-SA-10-29-2024-1 Safari 18.1** *Apple Product Security via Fulldisclosure (Oct 31)*

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