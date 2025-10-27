---
title: APPLE-SA-11-19-2024-4 iOS 17.7.2 and iPadOS 17.7.2
url: https://seclists.org/fulldisclosure/2024/Nov/14
source: Full Disclosure
date: 2024-11-22
fetch_date: 2025-10-06T19:22:27.516728
---

# APPLE-SA-11-19-2024-4 iOS 17.7.2 and iPadOS 17.7.2

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

[![Previous](/images/left-icon-16x16.png)](13)
[By Date](date.html#14)
[![Next](/images/right-icon-16x16.png)](15)

[![Previous](/images/left-icon-16x16.png)](13)
[By Thread](index.html#14)
[![Next](/images/right-icon-16x16.png)](15)

![](/shared/images/nst-icons.svg#search)

# APPLE-SA-11-19-2024-4 iOS 17.7.2 and iPadOS 17.7.2

---

*From*: Apple Product Security via Fulldisclosure <fulldisclosure () seclists org>
*Date*: Tue, 19 Nov 2024 17:42:08 -0700

---

```
-----BEGIN PGP SIGNED MESSAGE-----
Hash: SHA256

APPLE-SA-11-19-2024-4 iOS 17.7.2 and iPadOS 17.7.2

iOS 17.7.2 and iPadOS 17.7.2 addresses the following issues.
Information about the security content is also available at
https://support.apple.com/121754.

Apple maintains a Security Releases page at
https://support.apple.com/100100 which lists recent
software updates with security advisories.

JavaScriptCore
Available for: iPhone XS and later, iPad Pro 13-inch, iPad Pro 12.9-inch
2nd generation and later, iPad Pro 10.5-inch, iPad Pro 11-inch 1st
generation and later, iPad Air 3rd generation and later, iPad 6th
generation and later, and iPad mini 5th generation and later
Impact: Processing maliciously crafted web content may lead to arbitrary
code execution. Apple is aware of a report that this issue may have been
actively exploited on Intel-based Mac systems.
Description: The issue was addressed with improved checks.
WebKit Bugzilla: 283063
CVE-2024-44308: Clément Lecigne and Benoît Sevens of Google's Threat
Analysis Group

WebKit
Available for: iPhone XS and later, iPad Pro 13-inch, iPad Pro 12.9-inch
2nd generation and later, iPad Pro 10.5-inch, iPad Pro 11-inch 1st
generation and later, iPad Air 3rd generation and later, iPad 6th
generation and later, and iPad mini 5th generation and later
Impact: Processing maliciously crafted web content may lead to a cross
site scripting attack. Apple is aware of a report that this issue may
have been actively exploited on Intel-based Mac systems.
Description: A cookie management issue was addressed with improved state
management.
WebKit Bugzilla: 283095
CVE-2024-44309: Clément Lecigne and Benoît Sevens of Google's Threat
Analysis Group

This update is available through iTunes and Software Update on your
iOS device, and will not appear in your computer's Software Update
application, or in the Apple Downloads site. Make sure you have an
Internet connection and have installed the latest version of iTunes
from https://www.apple.com/itunes/

iTunes and Software Update on the device will automatically check
Apple's update server on its weekly schedule. When an update is
detected, it is downloaded and the option to be installed is
presented to the user when the iOS device is docked. We recommend
applying the update immediately if possible. Selecting
Don't Install will present the option the next time you connect
your iOS device.

The automatic update process may take up to a week depending on
the day that iTunes or the device checks for updates. You may
manually obtain the update via the Check for Updates button
within iTunes, or the Software Update on your device.

To check that the iPhone, iPod touch, or iPad has been updated:

* Navigate to Settings
* Select General
* Select About. The version after applying this update will be
"iOS 17.7.2 and iPadOS 17.7.2".

All information is also posted on the Apple Security Releases
web site: https://support.apple.com/100100.

This message is signed with Apple's Product Security PGP key,
and details are available at:
https://www.apple.com/support/security/pgp/

-----BEGIN PGP SIGNATURE-----

iQIzBAEBCAAdFiEEsz9altA7uTI+rE/qX+5d1TXaIvoFAmc9JGcACgkQX+5d1TXa
IvqaMhAArOKmA61hgLNGofjznuKQo6Jc42iPl7a/ZiB2Tq5ynZKPIGmGiM3HdJQ8
bbifOgpkmNcA3h1OUlXnnkbdehq6d8MzI9WSn6uHdgWZ5LqLMXOWgsEF5Hwwmm7z
aqTaqMv4fV2J6w2wTcoL5XptxGXiEi37/GzcureD3hvL+nRAAzR6c/gRXmcEjGL7
pVTNJA0C8VyY9kG+Uc7ia2m5Riux2jsYzWYppPfCwUFeo3bQDexG7WsiHa00OZN+
HkNS5/1t/7hftJZ+w/PbVnEK23Dm962NQgCrcFKGnbjNGJQlIjl+xfbi6BuQ6lJJ
ZAI+3WqPHXLAMCcae/DfERqXWnJu8fTMfCwCbQVx185Cih+mtH0oc4MtPtiZdhi8
TxZpVGZHYjLJa9VANTrNzkAmFflnhAC4tAG2FXx3ld3t/8u9Fhv0oyTa5HlzVYJ/
WJgK32eT7I1h7Oqrp49KZcMIM8H6ZwNXYOI+Rf7GXdEN2y9Qhb+IOvdilTrCTpzR
l6Gu6fBwH0G0UGHRktnBPlryJdOg26J1iVBZg6/K/CSjQizWdDXN/Nq4YwI17Eq4
HtFdtOtrs5n0bDz+fsfGbsieTyUz1BUet2xLzPECfD4nYEKmckD1d/dRylc3vK9Y
GOCp1nWDoPSKnmkU9Il2SFAIuEM9o60lCN7PMWBrC9zYXMAxFmY=
=+VKC
-----END PGP SIGNATURE-----
_______________________________________________
Sent through the Full Disclosure mailing list
https://nmap.org/mailman/listinfo/fulldisclosure
Web Archives & RSS: https://seclists.org/fulldisclosure/
```

---

[![Previous](/images/left-icon-16x16.png)](13)
[By Date](date.html#14)
[![Next](/images/right-icon-16x16.png)](15)

[![Previous](/images/left-icon-16x16.png)](13)
[By Thread](index.html#14)
[![Next](/images/right-icon-16x16.png)](15)

### Current thread:

* **APPLE-SA-11-19-2024-4 iOS 17.7.2 and iPadOS 17.7.2** *Apple Product Security via Fulldisclosure (Nov 21)*

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