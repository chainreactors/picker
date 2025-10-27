---
title: APPLE-SA-09-15-2025-3 iOS 16.7.12 and iPadOS 16.7.12
url: https://seclists.org/fulldisclosure/2025/Sep/51
source: Full Disclosure
date: 2025-09-17
fetch_date: 2025-10-02T20:16:53.604386
---

# APPLE-SA-09-15-2025-3 iOS 16.7.12 and iPadOS 16.7.12

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
[![Next](/images/right-icon-16x16.png)](52)

[![Previous](/images/left-icon-16x16.png)](50)
[By Thread](index.html#51)
[![Next](/images/right-icon-16x16.png)](52)

![](/shared/images/nst-icons.svg#search)

# APPLE-SA-09-15-2025-3 iOS 16.7.12 and iPadOS 16.7.12

---

*From*: Apple Product Security via Fulldisclosure <fulldisclosure () seclists org>
*Date*: Mon, 15 Sep 2025 16:33:02 -0700

---

```
-----BEGIN PGP SIGNED MESSAGE-----
Hash: SHA256

APPLE-SA-09-15-2025-3 iOS 16.7.12 and iPadOS 16.7.12

iOS 16.7.12 and iPadOS 16.7.12 addresses the following issues.
Information about the security content is also available at
https://support.apple.com/125141.

Apple maintains a Security Releases page at
https://support.apple.com/100100 which lists recent
software updates with security advisories.

ImageIO
Available for: iPhone 8, iPhone 8 Plus, iPhone X, iPad 5th generation,
iPad Pro 9.7-inch, and iPad Pro 12.9-inch 1st generation
Impact: Processing a malicious image file may result in memory
corruption. Apple is aware of a report that this issue may have been
exploited in an extremely sophisticated attack against specific targeted
individuals.
Description: An out-of-bounds write issue was addressed with improved
bounds checking.
CVE-2025-43300: Apple

This update is available through iTunes and Software Update on your
iOS device, and will not appear in your computer's Software Update
application, or in the Apple Downloads site. Make sure you have an
Internet connection and have installed the latest version of iTunes
from https://www.apple.com/itunes/

iTunes and Software Update on the device will automatically check
Apple's update server on its weekly schedule. When an update is
detected, it is downloaded and the option to be installed is
presented to the user when the iOS device is docked. We recommend
applying the update immediately if possible. Selecting Don't Install
will present the option the next time you connect your iOS device.

The automatic update process may take up to a week depending on the
day that iTunes or the device checks for updates. You may manually
obtain the update via the Check for Updates button within iTunes, or
the Software Update on your device.

To check that the iPhone, iPod touch, or iPad has been updated:

* Navigate to Settings
* Select General
* Select About. The version after applying this update
will be "iOS 16.7.12 and iPadOS 16.7.12".

All information is also posted on the Apple Security Releases
web site: https://support.apple.com/100100.

This message is signed with Apple's Product Security PGP key,
and details are available at:
https://www.apple.com/support/security/pgp/

-----BEGIN PGP SIGNATURE-----

iQIzBAEBCAAdFiEEhjkl+zMLNwFiCT1o4Ifiq8DH7PUFAmjIm6cACgkQ4Ifiq8DH
7PWiOBAAqFv9J+AqoJfp4fPimTRa+sFuL1khUtyYCRM9+mJT0T8c6WMW0KFLbaGG
KkbsVxK5lfQnHvAKbr0y/8DIWFy2s3iDItavwwb3AyajjNXwLl8Nr96h6p7Ozzfw
9zWNbi9dVMNiMaaZYOe6QuPtBA/3dAyhN49pJfHQrV7wPrnP8WrtpPbFFEvxnQjM
cvnZDkcGAAjYYQDMnIAOcb8Jud/HOkzrBGSsS0sJJxjm+DXrMQnGD6C9LN6VZBYx
GwCJCHTUxlIoAnRlXF9Finn9qDNDteECJjiJ2SkxoyXcLhIk1xLWx71+uzUMhGRM
oONnjI7rha5IexMGP2WG6QN3PYRs2GCS+KIfWvfS13HQ3UOFJ79McmjVmKApv9eE
plOi6ScgA9Ug1xkan+1hX2gSBYD3cqcnvyHb+9EdL0A1XENIaYSmyeJ7rrQ6X4Fw
kMqe/Yi+JTrlxd1DwFerq/IlMZrhaiklpLkcjhIypI0GEHN1N3bBRfbs3H1wpUT0
g971iYptFYolMccu06cxUYIlEiYpapZQwGIEEiKxxcL03Jlg5qSL42uG0f3vQuIm
tnVodEmXAKHqDrSvhD5sMKKPoFMFxJjq3Pmj6NrFGmAq/Fi1FZPm60sYg075GWiE
L3A5UvQhYM+avqYoda33kFnvscd5h35CVOidGmnaNcBDAW3NODg=
=Bcyn
-----END PGP SIGNATURE-----

_______________________________________________
Sent through the Full Disclosure mailing list
https://nmap.org/mailman/listinfo/fulldisclosure
Web Archives & RSS: https://seclists.org/fulldisclosure/
```

---

[![Previous](/images/left-icon-16x16.png)](50)
[By Date](date.html#51)
[![Next](/images/right-icon-16x16.png)](52)

[![Previous](/images/left-icon-16x16.png)](50)
[By Thread](index.html#51)
[![Next](/images/right-icon-16x16.png)](52)

### Current thread:

* **APPLE-SA-09-15-2025-3 iOS 16.7.12 and iPadOS 16.7.12** *Apple Product Security via Fulldisclosure (Sep 15)*

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