---
title: APPLE-SA-05-11-2026-5 iOS 15.8.8 and iPadOS 15.8.8
url: https://seclists.org/fulldisclosure/2026/May/10
source: Full Disclosure
date: 2026-05-17
fetch_date: 2026-05-18T06:10:47.966192
---

# APPLE-SA-05-11-2026-5 iOS 15.8.8 and iPadOS 15.8.8

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

[![Previous](/images/left-icon-16x16.png)](9)
[By Date](date.html#10)
[![Next](/images/right-icon-16x16.png)](11)

[![Previous](/images/left-icon-16x16.png)](9)
[By Thread](index.html#10)
[![Next](/images/right-icon-16x16.png)](11)

![](/shared/images/nst-icons.svg#search)

# APPLE-SA-05-11-2026-5 iOS 15.8.8 and iPadOS 15.8.8

---

*From*: Apple Product Security via Fulldisclosure <fulldisclosure () seclists org>
*Date*: Mon, 11 May 2026 15:31:55 -0700

---

```
-----BEGIN PGP SIGNED MESSAGE-----
Hash: SHA256

APPLE-SA-05-11-2026-5 iOS 15.8.8 and iPadOS 15.8.8

iOS 15.8.8 and iPadOS 15.8.8 addresses the following issues.
Information about the security content is also available at
https://support.apple.com/en-us/127114.

Apple maintains a Security Releases page at
https://support.apple.com/100100 which lists recent
software updates with security advisories.

Notification Services
Available for: iPhone 6s (all models), iPhone 7 (all models), iPhone SE
(1st generation), iPad Air 2, iPad mini (4th generation), and iPod touch
(7th generation)
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
* Select About. The version
after applying this update will be "iOS 15.8.8 and iPadOS 15.8.8".

All information is also posted on the Apple Security Releases
web site: https://support.apple.com/100100.

This message is signed with Apple's Product Security PGP key,
and details are available at:
https://www.apple.com/support/security/pgp/

-----BEGIN PGP SIGNATURE-----

iQIzBAEBCAAdFiEEhjkl+zMLNwFiCT1o4Ifiq8DH7PUFAmoCVgYACgkQ4Ifiq8DH
7PVrBg/+OqcPYDR0LcHnmP5cF1p9dkmnmVX2RfMRmFtM/ExO5LTqhngmcpX0GiOh
KsuZ7MsMTHS1/p0hCO9AL0ggdCxOuITVxNmnwaTzxVOwupRZPTcz4YzutO2DRH1L
xvgbX7egx4Xs5yJHS1SPu0Msbrkq0I1J8G6vXuxNiUhMsrUbiuRMNDEUJ4A86nxD
yUX+/cuS8uD5TjRU14bAdzsvOlnWr+Taxs9AOKGjr0FUPKuqweGVCXK9ec8elxES
4pAlJotXl7vPSWcDXMVKssoHws2W2dCfIvcRQbK40tFNf9qiv6W9Xm7bOztiHuAJ
XxslXx7ETvc6PKngKEEQA6U3g+Qvgg4xFdtxNTcDkUkkv985oS+DD3jXVNq61zbj
bK/9bodLh60+NPdm9WNuhW4a9EqDMBNl4WOHVS0KADis1iMJS1o61hQiySRpwYJB
vRKY3Y0i8hM++wyL/oYyG6K8xyUVbCX8Pm4IjXZ7yc2QXshRWrTSKl+2fLjHLW+E
BfQ+DYExOWX3GOc/gSQXsJSDRtneRzajUUaP1kx1knSl3OXPfIN+4o/xIaPeqQqI
efH4ZpSpsgbP/rQFVqqKYqaZzgbGoZ4NbA5eTU5gHIe9yVbcP3bIf0QnL+/S0WV/
Z9+bEbD7ZVH/w4Gin43PmxZiKQCxMfk2hFdvvaDPjnY5Y9Ee+e8=
=rWDE
-----END PGP SIGNATURE-----

_______________________________________________
Sent through the Full Disclosure mailing list
https://nmap.org/mailman/listinfo/fulldisclosure
Web Archives & RSS: https://seclists.org/fulldisclosure/
```

---

[![Previous](/images/left-icon-16x16.png)](9)
[By Date](date.html#10)
[![Next](/images/right-icon-16x16.png)](11)

[![Previous](/images/left-icon-16x16.png)](9)
[By Thread](index.html#10)
[![Next](/images/right-icon-16x16.png)](11)

### Current thread:

* **APPLE-SA-05-11-2026-5 iOS 15.8.8 and iPadOS 15.8.8** *Apple Product Security via Fulldisclosure (May 17)*

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