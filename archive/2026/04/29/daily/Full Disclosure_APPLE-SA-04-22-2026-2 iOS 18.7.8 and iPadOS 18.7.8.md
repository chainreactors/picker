---
title: APPLE-SA-04-22-2026-2 iOS 18.7.8 and iPadOS 18.7.8
url: https://seclists.org/fulldisclosure/2026/Apr/15
source: Full Disclosure
date: 2026-04-29
fetch_date: 2026-04-30T05:30:39.107693
---

# APPLE-SA-04-22-2026-2 iOS 18.7.8 and iPadOS 18.7.8

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

[![Previous](/images/left-icon-16x16.png)](14)
[By Date](date.html#15)
[![Next](/images/right-icon-16x16.png)](16)

[![Previous](/images/left-icon-16x16.png)](14)
[By Thread](index.html#15)
[![Next](/images/right-icon-16x16.png)](16)

![](/shared/images/nst-icons.svg#search)

# APPLE-SA-04-22-2026-2 iOS 18.7.8 and iPadOS 18.7.8

---

*From*: Apple Product Security via Fulldisclosure <fulldisclosure () seclists org>
*Date*: Wed, 22 Apr 2026 12:13:49 -0700

---

```
-----BEGIN PGP SIGNED MESSAGE-----
Hash: SHA256

APPLE-SA-04-22-2026-2 iOS 18.7.8 and iPadOS 18.7.8

iOS 18.7.8 and iPadOS 18.7.8 addresses the following issues.
Information about the security content is also available at
https://support.apple.com/en-us/127003.

Apple maintains a Security Releases page at
https://support.apple.com/100100 which lists recent
software updates with security advisories.

Notification Services
Available for: iPhone XR, iPhone XS, iPhone XS Max, iPhone 11 (all
models), iPhone SE (2nd generation), iPhone 12 (all models), iPhone 13
(all models), iPhone SE (3rd generation), iPhone 14 (all models), iPhone
15 (all models), iPhone 16 (all models), iPhone 16e, iPad mini (5th
generation - A17 Pro), iPad (7th generation - A16), iPad Air (3rd - 5th
generation), iPad Air 11-inch (M2 - M3), iPad Air 13-inch (M2 - M3),
iPad Pro 11-inch (1st generation - M4), iPad Pro 12.9-inch (3rd - 6th
generation), and iPad Pro 13-inch (M4)
Impact: Notifications marked for deletion could be unexpectedly retained
on the device
Description: A logging issue was addressed with improved data redaction.
CVE-2026-28950

This update is available through iTunes and Software Update on your iOS
device, and will not appear in your computer's Software Update
application, or in the Apple Downloads site. Make sure you have an
Internet connection and have installed the latest version of iTunes from
https://www.apple.com/itunes/

iTunes and Software Update on the device will automatically check
Apple's update server on its weekly schedule. When an update is
detected, it is downloaded and the option to be installed is presented
to the user when the iOS device is docked. We recommend applying the
update immediately if possible. Selecting Don't Install will present the
option the next time you connect your iOS device.

The automatic update process may take up to a week depending on the day
that iTunes or the device checks for updates. You may manually obtain
the update via the Check for Updates button within iTunes, or the
Software Update on your device.

To check that the iPhone, iPod touch, or iPad has been updated:

* Navigate to Settings
* Select General
* Select About. The version after applying this update
will be "iOS 18.7.8 and iPadOS 18.7.8".

All information is also posted on the Apple Security Releases
web site: https://support.apple.com/100100.

This message is signed with Apple's Product Security PGP key,
and details are available at:
https://www.apple.com/support/security/pgp/

-----BEGIN PGP SIGNATURE-----

iQIzBAEBCAAdFiEEhjkl+zMLNwFiCT1o4Ifiq8DH7PUFAmnpFugACgkQ4Ifiq8DH
7PViuQ/6A7fJLlPcOq4KCj9px9/OoFv6mVVDd1JIyll7ybiekv1JJ89aHY85mPCV
aSChn/cEC3g/HS9d6dtYUINqQ1CWTLsQ6Ic7qW94+e0H2wlw/MzQpp+0BzqR1v7L
H4loAeBJjcWfLTs1GMi4TonLPmDFJRvqPlPeowaStqOnhYRF5EygILSMQug0vfAt
l8QJE3+ul1cssWuxUDO4RGmEeHcGZXyqg+adR5FG/K7r3FKIfE7xql5wxqjdYCO3
kfyg9phS1n0o9Wei6RUe5TzP7t0sBH68zcqrpHfr5WY4KtuMSil3qlqaok+KlA5k
bst7vN643+ilEqp2hnkc0mKpj7QdEUn/F30xl6NUoW45s1oK9qZRrQpaQnDzrYt+
3cCEnjpY9RTiobvE6U1PmriObIQwKxDTxQcRNeus/6hN8qHsowvW0AGrFm8HyhRC
R6bdyXZPpyAtPa5NZmml9T3cj3ZAa1qhceamgBfGwpB96kebCShoErpa+e56Uy6z
Rjbdz8J9Y+n3ogfNegiV8IFCo/x08x63xAqIMh+hKn786i04VCuGchfSI7PS8zMf
t33BElZ4LeSWzjYvwWFzK2jyMJKaARA6gNP1QXcka3tdnMBw4O28iW4E3vZ2r6B8
AJdh0BSUP0APnwhVLmTYO7k/XUuQ3R6Xq2MpjU0yJ/XSWei62hU=
=ETWt
-----END PGP SIGNATURE-----

_______________________________________________
Sent through the Full Disclosure mailing list
https://nmap.org/mailman/listinfo/fulldisclosure
Web Archives & RSS: https://seclists.org/fulldisclosure/
```

---

[![Previous](/images/left-icon-16x16.png)](14)
[By Date](date.html#15)
[![Next](/images/right-icon-16x16.png)](16)

[![Previous](/images/left-icon-16x16.png)](14)
[By Thread](index.html#15)
[![Next](/images/right-icon-16x16.png)](16)

### Current thread:

* **APPLE-SA-04-22-2026-2 iOS 18.7.8 and iPadOS 18.7.8** *Apple Product Security via Fulldisclosure (Apr 29)*

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