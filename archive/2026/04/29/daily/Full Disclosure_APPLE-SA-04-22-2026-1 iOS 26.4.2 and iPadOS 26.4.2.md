---
title: APPLE-SA-04-22-2026-1 iOS 26.4.2 and iPadOS 26.4.2
url: https://seclists.org/fulldisclosure/2026/Apr/14
source: Full Disclosure
date: 2026-04-29
fetch_date: 2026-04-30T05:30:39.436899
---

# APPLE-SA-04-22-2026-1 iOS 26.4.2 and iPadOS 26.4.2

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

# APPLE-SA-04-22-2026-1 iOS 26.4.2 and iPadOS 26.4.2

---

*From*: Apple Product Security via Fulldisclosure <fulldisclosure () seclists org>
*Date*: Wed, 22 Apr 2026 12:12:40 -0700

---

```
-----BEGIN PGP SIGNED MESSAGE-----
Hash: SHA256

APPLE-SA-04-22-2026-1 iOS 26.4.2 and iPadOS 26.4.2

iOS 26.4.2 and iPadOS 26.4.2 addresses the following issues.
Information about the security content is also available at
https://support.apple.com/en-us/127002.

Apple maintains a Security Releases page at
https://support.apple.com/100100 which lists recent
software updates with security advisories.

Notification Services
Available for: iPhone 11 and later, iPad Pro 12.9-inch 3rd generation
and later, iPad Pro 11-inch 1st generation and later, iPad Air 3rd
generation and later, iPad 8th generation and later, and iPad mini 5th
generation and later
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
will be "iOS 26.4.2 and iPadOS 26.4.2".

All information is also posted on the Apple Security Releases
web site: https://support.apple.com/100100.

This message is signed with Apple's Product Security PGP key,
and details are available at:
https://www.apple.com/support/security/pgp/

-----BEGIN PGP SIGNATURE-----

iQIzBAEBCAAdFiEEhjkl+zMLNwFiCT1o4Ifiq8DH7PUFAmnpFo0ACgkQ4Ifiq8DH
7PVSQBAAjbA6lYBHbEIJXSngMTp+m6QEC0dgPn7w9Yt6ne3baKi43YlJdZ95gCnu
ecYwAWeser5Nh7IMpH6kUUFXlq+Gaa78BwJa79MRnFJRZaGa85RwuD1wwizqvcje
sEWlgQpPnl6Ny4aNFzbTDm9nK1PqZvG/MbPXf8GcnBnKGY2iqHGpAvVVNVf9asEO
GACsZQLGi+R/of46KgRnYZB+JUAe/K9Q5hRVFU+MbXJKTKb0cCWPpAQJqf/+Vmmt
viduFxtnMvR/Ft7SLgpqRnrCe3HOPaocxNIPIefyaI6Qtkjqx5LeAHuCnlICXX+P
34uPpU3oggQLlyeUqHviIOtk4FDCnkYUp4AHcdKXO2cByuOqZmmX7xZUfkA9FsMr
C/y+UsVbECn4hJtqbuFxEKjVcfhX6YT1gZULOP1xnbzkk0wF/YNdyCNXAREerNdp
8mWxRhVlCDOghbeB2p0cWdqeixSjk7NjJgEUwtXXmXPiY4DdnZ7Te0iGdnUyrqrs
kJqMP7/GK3kvm2OwXYFKSF5+jimSUH8jeKpunpliyx/qW3gtx1yRIzoC8t0vYn7s
lhzORwKAEfoNg1NiPN1onvtmckVPQUE/5wFt9Z7hxc+SSWMaFsCUQuW7OMHNzxcl
kpmVzJxNy1xLYyNGrAaZtYqIzQUfcfmi0zkxwCFsWz8VnDWggvI=
=VCOl
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

* **APPLE-SA-04-22-2026-1 iOS 26.4.2 and iPadOS 26.4.2** *Apple Product Security via Fulldisclosure (Apr 29)*

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