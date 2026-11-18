---
title: APPLE-SA-11-13-2026-1 tvOS 27.2.1
url: https://seclists.org/fulldisclosure/2026/Nov/35
source: Full Disclosure
date: 2026-11-17
fetch_date: 2026-11-18T09:22:47.889143
---

# APPLE-SA-11-13-2026-1 tvOS 27.2.1

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

[![Previous](/images/left-icon-16x16.png)](34)
[By Date](date.html#35)
[![Next](/images/right-icon-16x16.png)](36)

[![Previous](/images/left-icon-16x16.png)](34)
[By Thread](index.html#35)
[![Next](/images/right-icon-16x16.png)](36)

![](/shared/images/nst-icons.svg#search)

# APPLE-SA-11-13-2026-1 tvOS 27.2.1

---

*From*: Apple Product Security via Fulldisclosure <fulldisclosure () seclists org>
*Date*: Fri, 13 Nov 2026 13:04:26 -0800

---

```
-----BEGIN PGP SIGNED MESSAGE-----
Hash: SHA256

APPLE-SA-11-13-2026-1 tvOS 27.2.1

tvOS 27.2.1 addresses the following issues.
Information about the security content is also available at
https://support.apple.com/149721.

Apple maintains a Security Releases page at
https://support.apple.com/100100 which lists recent
software updates with security advisories.

AirPlay
Available for: Apple TV 4K 2nd generation and later
Impact: An attacker in Bluetooth range may be able to bypass the rate
limit on pairing code attempts
Description: A logic issue was addressed with improved state management.
CVE-2026-113968: Apple

App Intents
Available for: Apple TV 4K 2nd generation and later
Impact: An app may be able to access sensitive user data
Description: An authorization issue was addressed with improved state
management.
CVE-2026-113963: László Várady

Bluetooth
Available for: Apple TV 4K 2nd generation and later
Impact: An attacker in Bluetooth range may be able to corrupt process
memory
Description: A use-after-free issue was addressed with improved memory
management.
CVE-2026-113970: Apple

brotli
Available for: Apple TV 4K 2nd generation and later
Impact: Processing maliciously crafted input may lead to memory
corruption
Description: An out-of-bounds write issue was addressed with improved
input validation.
CVE-2026-111497

CoreUtils
Available for: Apple TV 4K 2nd generation and later
Impact: A malicious Bluetooth device may be able to establish a pairing
without user interaction
Description: This issue was addressed with improved checks.
CVE-2026-113965: Apple

CoreUtils
Available for: Apple TV 4K 2nd generation and later
Impact: An attacker in Bluetooth range may be able to bypass the rate
limit on pairing code attempts and pair with a device without user
interaction
Description: A logic issue was addressed with improved state management.
CVE-2026-113964: an anonymous researcher

rapportd
Available for: Apple TV 4K 2nd generation and later
Impact: An attacker on the same network may be able to bypass the rate
limit on AirPlay pairing code attempts
Description: A logic issue was addressed with improved state management.
CVE-2026-113969: Apple

Apple TV will periodically check for software updates. Alternatively,
you may manually check for software updates by selecting
"Settings -> System -> Software Update -> Update Software."

To check the current version of software, select
"Settings -> General -> About."

All information is also posted on the Apple Security Releases
web site: https://support.apple.com/100100.

This message is signed with Apple's Product Security PGP key,
and details are available at:
https://www.apple.com/support/security/pgp/

-----BEGIN PGP SIGNATURE-----

iQIzBAEBCAAdFiEEhjkl+zMLNwFiCT1o4Ifiq8DH7PUFAmr3dWYACgkQ4Ifiq8DH
7PViARAAuNc2qlV+XHOsoPk0Zr3unXxh5G8s2uasQwENUHJ2hH/blA9eb7QoDmsF
brtc9OnaVVFR7hePKXamzxF+BsZtdsNSr0o8bBKkOB1C0+0ODi8QN/RJnW1I2fV4
GTxCozFMB+2mXHgeZLEwpv++gPK/0mVpxzC7xBRIJf8L769wVmelxDwF4SASWT63
pGunJ4MPrL2yJovvpR/UYFnm8vhPs3RpKDFZ4wROahfZhCQpcpVBMRHRcCKdeQXE
O41Wp5B8AJPohYsnAWzTNCe4DOCxeDsav13XZulcErCFqf5fvvFJf/LDLON2kcIF
KHXPmmk+78xFPtx/CHsG5fnfYP/z6Evt2byKAE0nZxAICtamfarormY9LTwoAZzd
XD1t8BmdvupBvYQ1Hc33GCbc627K4qlZosuyLkTOOsGT0PR+DzDlcIb/T+LOxJaM
9ve+8mIXUYqo8pkNIhThP6joJRxzvwLvMbv2GP3c59JtEMBEaa5ZQQCbVftOqQNf
sDwtjubvzWUj5WxUu5S+VaFgROJkVq3FFJC5c6nUPsJBwuuYl6w0bOyjrQu2ytpI
Ewy4KGE1RQFw8lHQZxcrk47g5H63qdfZFU48GyLk+vdNBKCus4fCf+J8u4zFnFAd
CP5BI6zg/KwW7l/4ctLF5eTWMP/B6jPLPtGCdrA8XWXAOtWKhWU=
=ijyD
-----END PGP SIGNATURE-----

_______________________________________________
Sent through the Full Disclosure mailing list
https://nmap.org/mailman/listinfo/fulldisclosure
Web Archives & RSS: https://seclists.org/fulldisclosure/
```

---

[![Previous](/images/left-icon-16x16.png)](34)
[By Date](date.html#35)
[![Next](/images/right-icon-16x16.png)](36)

[![Previous](/images/left-icon-16x16.png)](34)
[By Thread](index.html#35)
[![Next](/images/right-icon-16x16.png)](36)

### Current thread:

* **APPLE-SA-11-13-2026-1 tvOS 27.2.1** *Apple Product Security via Fulldisclosure (Nov 17)*

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