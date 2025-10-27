---
title: APPLE-SA-06-25-2024-1 AirPods Firmware Update 6A326, AirPods Firmware Update 6F8, and Beats Firmware Update 6F8
url: https://seclists.org/fulldisclosure/2024/Jul/2
source: Full Disclosure
date: 2024-07-05
fetch_date: 2025-10-06T17:51:37.981191
---

# APPLE-SA-06-25-2024-1 AirPods Firmware Update 6A326, AirPods Firmware Update 6F8, and Beats Firmware Update 6F8

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

[![Previous](/images/left-icon-16x16.png)](1)
[By Date](date.html#2)
[![Next](/images/right-icon-16x16.png)](3)

[![Previous](/images/left-icon-16x16.png)](1)
[By Thread](index.html#2)
[![Next](/images/right-icon-16x16.png)](3)

![](/shared/images/nst-icons.svg#search)

# APPLE-SA-06-25-2024-1 AirPods Firmware Update 6A326, AirPods Firmware Update 6F8, and Beats Firmware Update 6F8

---

*From*: Apple Product Security via Fulldisclosure <fulldisclosure () seclists org>
*Date*: Tue, 25 Jun 2024 20:53:52 -0700

---

```
-----BEGIN PGP SIGNED MESSAGE-----
Hash: SHA256

APPLE-SA-06-25-2024-1 AirPods Firmware Update 6A326, AirPods
Firmware Update 6F8, and Beats Firmware Update 6F8

AirPods Firmware Update 6A326, AirPods Firmware Update 6F8, and
Beats Firmware Update 6F8 addresses the following issues.
Information about the security content is also available at
https://support.apple.com/HT214111.

Apple maintains a Security Releases page at
https://support.apple.com/HT201222 which lists recent
software updates with security advisories.

Bluetooth
Available for: AirPods (2nd generation and later), AirPods Pro (all
models), AirPods Max, Powerbeats Pro, and Beats Fit Pro
Impact: When your headphones are seeking a connection request to one
of your previously paired devices, an attacker in Bluetooth range
might be able to spoof the intended source device and gain access
to your headphones
Description: An authentication issue was addressed with improved
state management.
CVE-2024-27867: Jonas DreÃŸler

Firmware updates are automatically delivered while your headphones
are paired with and in Bluetooth range of your iPhone, iPad, or Mac.

You can check the firmware version of your wireless headphones in
Bluetooth settings on your device. On iPhone or iPad, go to
Settings > Bluetooth. On Mac, go to System Settings > Bluetooth.
Then tap the info button next to your headphones.

Learn more about firmware updates for AirPods at
https://support.apple.com/106340

Learn more about firmware updates for Beats at
https://support.apple.com/102368

All information is also posted on the Apple Security Releases
web site: https://support.apple.com/HT201222.

This message is signed with Apple's Product Security PGP key,
and details are available at:
https://www.apple.com/support/security/pgp/
-----BEGIN PGP SIGNATURE-----

iQIzBAEBCAAdFiEEsz9altA7uTI+rE/qX+5d1TXaIvoFAmZ7kCwACgkQX+5d1TXa
IvqORhAAsEgfOmEzguP2GofB8A1mvP7Mz8qwG8vVhlmc3Z7XhH0yQegpN13aQ9g3
kEsu5KAeUJuId8sSgLwVZlNfLD/UVhR4xRdNQaJ5gVs0HydPUxr95tU2zAMQz/1w
dJvST6tBcd0mEw9Rsqh4L8YATkuicy2Rctc8aKcXoqKLDop3J1H7/htv6t8vPtgw
r59IyfzGWKuiNSeOArWwtbv2pbi6angogTJ3a8NwDBFzLg4stqCnAqgzIeBO32Tm
+JwSknrElCRzcACQmcGDEElaI6A3ZFA6lP78gCXtW48dosHv/SC9J9TXOLK5JIWC
WNHjFr+R/8w4ZoPYs0JJ/KlP2o++wEA8ew4cd7JTIIpV8oMRkHfJUzgRnkSM+5s8
ZKULVvinzrBn5BnINXhYcWNms4hHgUGuFqTeNWRrVpy3vDKidFFFZh0c4bbbWaIK
RFDmZop4NpucgoOka9h+dbrm8/LLTd0KK+IF0dfFArn+zo5UbeDu3dao38pP6qwO
6U+1lFco5HodFzLAmECbIlE6VPUfwPHDoB+BApuehkka/qB2gZFIm4qIGRSzrQgQ
3OGyI/RqUKfHigTxrxo1GUtXeTnLLbhIfPv9MvMwgvgRqt36liMYvksl+I17mWdR
iNihwvsfpV6VliBCQm05nPJkp25g0h8j+aZfg0IdXFgzYMq7PmI=
=DvD4
-----END PGP SIGNATURE-----
_______________________________________________
Sent through the Full Disclosure mailing list
https://nmap.org/mailman/listinfo/fulldisclosure
Web Archives & RSS: https://seclists.org/fulldisclosure/
```

---

[![Previous](/images/left-icon-16x16.png)](1)
[By Date](date.html#2)
[![Next](/images/right-icon-16x16.png)](3)

[![Previous](/images/left-icon-16x16.png)](1)
[By Thread](index.html#2)
[![Next](/images/right-icon-16x16.png)](3)

### Current thread:

* **APPLE-SA-06-25-2024-1 AirPods Firmware Update 6A326, AirPods Firmware Update 6F8, and Beats Firmware Update 6F8** *Apple Product Security via Fulldisclosure (Jul 03)*

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