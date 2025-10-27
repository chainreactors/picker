---
title: APPLE-SA-11-19-2024-3 iOS 18.1.1 and iPadOS 18.1.1
url: https://seclists.org/fulldisclosure/2024/Nov/13
source: Full Disclosure
date: 2024-11-22
fetch_date: 2025-10-06T19:22:30.250137
---

# APPLE-SA-11-19-2024-3 iOS 18.1.1 and iPadOS 18.1.1

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

[![Previous](/images/left-icon-16x16.png)](12)
[By Date](date.html#13)
[![Next](/images/right-icon-16x16.png)](14)

[![Previous](/images/left-icon-16x16.png)](12)
[By Thread](index.html#13)
[![Next](/images/right-icon-16x16.png)](14)

![](/shared/images/nst-icons.svg#search)

# APPLE-SA-11-19-2024-3 iOS 18.1.1 and iPadOS 18.1.1

---

*From*: Apple Product Security via Fulldisclosure <fulldisclosure () seclists org>
*Date*: Tue, 19 Nov 2024 17:41:27 -0700

---

```
-----BEGIN PGP SIGNED MESSAGE-----
Hash: SHA256

APPLE-SA-11-19-2024-3 iOS 18.1.1 and iPadOS 18.1.1

iOS 18.1.1 and iPadOS 18.1.1 addresses the following issues.
Information about the security content is also available at
https://support.apple.com/121752.

Apple maintains a Security Releases page at
https://support.apple.com/100100 which lists recent
software updates with security advisories.

JavaScriptCore
Available for: iPhone XS and later, iPad Pro 13-inch, iPad Pro 12.9-inch
3rd generation and later, iPad Pro 11-inch 1st generation and later,
iPad Air 3rd generation and later, iPad 7th generation and later, and
iPad mini 5th generation and later
Impact: Processing maliciously crafted web content may lead to arbitrary
code execution. Apple is aware of a report that this issue may have been
actively exploited on Intel-based Mac systems.
Description: The issue was addressed with improved checks.
WebKit Bugzilla: 283063
CVE-2024-44308: Clément Lecigne and Benoît Sevens of Google's Threat
Analysis Group

WebKit
Available for: iPhone XS and later, iPad Pro 13-inch, iPad Pro 12.9-inch
3rd generation and later, iPad Pro 11-inch 1st generation and later,
iPad Air 3rd generation and later, iPad 7th generation and later, and
iPad mini 5th generation and later
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
"iOS 18.1.1 and iPadOS 18.1.1".

All information is also posted on the Apple Security Releases
web site: https://support.apple.com/100100.

This message is signed with Apple's Product Security PGP key,
and details are available at:
https://www.apple.com/support/security/pgp/

-----BEGIN PGP SIGNATURE-----

iQIzBAEBCAAdFiEEsz9altA7uTI+rE/qX+5d1TXaIvoFAmc9JA8ACgkQX+5d1TXa
IvrGzw/+PXf2fGgzCN5of6OYK0sWiJRRLZoL0uSZ9dOaD7I0/CyAx91Mv4OyH9Vv
eo9k84ZABNk4IO401WWLM8XSRSVILTcskT+SdXZrtOMYvmtUHUPKI35OWf1GBFdk
gfnnFSRYf/B+WWb4PV0iO01lyFQVU5qDLcrUCAUQLwighfAX2yEn+Zml3NX6i2E5
o2Rhc93Nac5a2cIcOGOSKrwsor0sh8NkAl9DcyPW6i6K3t59lUjiUY9XZQtEi6Ay
rChA84mo6Hb8wLwVIY17b8LVuruOSn3xg+Cc5eO5bOXp1O5lnR3dhuiZ2bl5BKaw
rp8+MDRsBZuTPS0k2Di3rmzuZ/GnvaQdtQKhcbOQ7tWW6evk/8TnFwlULaCr26OV
buLj0NWJ7GJYWpPuRWO0lFy9z9Fjdk4n+ptA7qmSWrhbdl+/uwUxJA5X58pVRWeW
BExGP3S/ST/5YgAfZXBjHuDLiHKMOtQ3PktaMuEWhLFgGXNllXGQDihL4lS/XUQ1
/E+mpWyY+kAbjtmCYlpez5MgeLkVv66yEWhOhsBMNIM+jkkRjktJo2SfhJMSryNL
QlY37zn/VWf8Av+L60YoZhoMmx7DJLIr+HI257zbIE35CVZ+badn18d3eA+fq3RP
tsDD8nlUePyZeNhEvc30Y5hXsIyK+Z0Ny+JgJfP1E6BeAJjjci0=
=ifwz
-----END PGP SIGNATURE-----

_______________________________________________
Sent through the Full Disclosure mailing list
https://nmap.org/mailman/listinfo/fulldisclosure
Web Archives & RSS: https://seclists.org/fulldisclosure/
```

---

[![Previous](/images/left-icon-16x16.png)](12)
[By Date](date.html#13)
[![Next](/images/right-icon-16x16.png)](14)

[![Previous](/images/left-icon-16x16.png)](12)
[By Thread](index.html#13)
[![Next](/images/right-icon-16x16.png)](14)

### Current thread:

* **APPLE-SA-11-19-2024-3 iOS 18.1.1 and iPadOS 18.1.1** *Apple Product Security via Fulldisclosure (Nov 21)*

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