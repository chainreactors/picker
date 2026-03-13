---
title: APPLE-SA-03-11-2026-2 iOS 15.8.7 and iPadOS 15.8.7
url: https://seclists.org/fulldisclosure/2026/Mar/2
source: Full Disclosure
date: 2026-03-12
fetch_date: 2026-03-13T04:08:11.058417
---

# APPLE-SA-03-11-2026-2 iOS 15.8.7 and iPadOS 15.8.7

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

# APPLE-SA-03-11-2026-2 iOS 15.8.7 and iPadOS 15.8.7

---

*From*: Apple Product Security via Fulldisclosure <fulldisclosure () seclists org>
*Date*: Wed, 11 Mar 2026 19:10:30 -0700

---

```
-----BEGIN PGP SIGNED MESSAGE-----
Hash: SHA256

APPLE-SA-03-11-2026-2 iOS 15.8.7 and iPadOS 15.8.7

iOS 15.8.7 and iPadOS 15.8.7 addresses the following issues.
Information about the security content is also available at
https://support.apple.com/126632.

Apple maintains a Security Releases page at
https://support.apple.com/100100 which lists recent
software updates with security advisories.

Kernel
Available for: iPhone 6s (all models), iPhone 7 (all models), iPhone SE
(1st generation), iPad Air 2, iPad mini (4th generation), and iPod touch
(7th generation)
Impact: An app may be able to execute arbitrary code with kernel
privileges. This fix associated with the Coruna exploit was shipped in
iOS 17 on September 18, 2023. This update brings that fix to devices
that cannot update to the latest iOS version.
Description: A use-after-free issue was addressed with improved memory
management.
CVE-2023-41974: Félix Poulin-Bélanger

WebKit
Available for: iPhone 6s (all models), iPhone 7 (all models), iPhone SE
(1st generation), iPad Air 2, iPad mini (4th generation), and iPod touch
(7th generation)
Impact: Processing maliciously crafted web content may lead to arbitrary
code execution. This fix associated with the Coruna exploit was shipped
in iOS 17.3 on January 22, 2024. This update brings that fix to devices
that cannot update to the latest iOS version.
Description: A type confusion issue was addressed with improved checks.
WebKit Bugzilla: 267134
CVE-2024-23222

WebKit
Available for: iPhone 6s (all models), iPhone 7 (all models), iPhone SE
(1st generation), iPad Air 2, iPad mini (4th generation), and iPod touch
(7th generation)
Impact: Processing maliciously crafted web content may lead to memory
corruption. This fix associated with the Coruna exploit was shipped in
iOS 16.6 on July 24, 2023. This update brings that fix to devices that
cannot update to the latest iOS version.
Description: A use-after-free issue was addressed with improved memory
management.
WebKit Bugzilla: 255951
CVE-2023-43000: Apple

WebKit
Available for: iPhone 6s (all models), iPhone 7 (all models), iPhone SE
(1st generation), iPad Air 2, iPad mini (4th generation), and iPod touch
(7th generation)
Impact: Processing maliciously crafted web content may lead to memory
corruption. This fix associated with the Coruna exploit was shipped in
iOS 17.2 on December 11th, 2023. This update brings that fix to devices
that cannot update to the latest iOS version.
Description: The issue was addressed with improved memory handling.
WebKit Bugzilla: 260913
CVE-2023-43010: Apple

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
will be "iOS 15.8.7 and iPadOS 15.8.7".

All information is also posted on the Apple Security Releases
web site: https://support.apple.com/100100.

This message is signed with Apple's Product Security PGP key,
and details are available at:
https://www.apple.com/support/security/pgp/

-----BEGIN PGP SIGNATURE-----

iQIzBAEBCAAdFiEEhjkl+zMLNwFiCT1o4Ifiq8DH7PUFAmmyENEACgkQ4Ifiq8DH
7PUQNw//ZgXEOg3VGIhzmsh/7SXOGSZhxoTKwWZGWNc+TlBUYPWqLyoGX2uXulna
WxJtKJJxcpYNesdEjBWAlPnJwJCd7Fe6+/NJekz1iH35U3KwhTvUWDBBo9gZUnId
OvBCZSwXAHiCJJ8uhUkCjhpZnx+u29SQyWPiYPwcrjMkI4H3oQ0eyrZ4sdQyUeA1
5ZdwFfVaDNKhpOYaoEXLbuYI4fPsnIiHs31djdzUTZKL5lnPUlKWJ4eVzJ7P/BSB
PgI7TUP9VNRzt5PJvVB1efWIEJtOWAB2splo2ASmNorBKdcjdBNUbRo6NE+vqwlZ
OjoguusrMS9wNu/iHJgnJzMit3ZToLauat3wuPxF7O8UNyfF1Ybvfg4auQGYo1Bj
PuHaOVtYSRhr0q+JF6htpoURjXp6nmEsmh4Wjs4q307RVqDuhwMGAJcwO/2Y30ow
H4nmEq3L4rCvu7Le2OgzsI311PU06vvbVfY6SznfG97pwsLeNZz6d91Z/aHxmAYm
iQqUZjaRyvs9jlD5Y526CFn3x5Sw1AgJX9WZdr4WcCwHE6JsxCu+J8DhG85RVlWJ
HXqd+sSloPmtagwrW9gPag4zA7wUwhJxa6wgLOC5V+P0DsZ81NwmUtppHaONM0qY
M4upJMdLHrXf/Sh8Csnevl5FX+dvwpn9vZodbYJyhsQ3L/PnwT8=
=x1N5
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

* **APPLE-SA-03-11-2026-2 iOS 15.8.7 and iPadOS 15.8.7** *Apple Product Security via Fulldisclosure (Mar 12)*

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
[!...