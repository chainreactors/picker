---
title: APPLE-SA-10-26-2026-3 iOS 18.7.11 and iPadOS 18.7.11
url: https://seclists.org/fulldisclosure/2026/Oct/41
source: Full Disclosure
date: 2026-10-27
fetch_date: 2026-10-28T07:49:42.178424
---

# APPLE-SA-10-26-2026-3 iOS 18.7.11 and iPadOS 18.7.11

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

[![Previous](/images/left-icon-16x16.png)](40)
[By Date](date.html#41)
[![Next](/images/right-icon-16x16.png)](42)

[![Previous](/images/left-icon-16x16.png)](40)
[By Thread](index.html#41)
[![Next](/images/right-icon-16x16.png)](42)

![](/shared/images/nst-icons.svg#search)

# APPLE-SA-10-26-2026-3 iOS 18.7.11 and iPadOS 18.7.11

---

*From*: Apple Product Security via Fulldisclosure <fulldisclosure () seclists org>
*Date*: Mon, 26 Oct 2026 14:41:05 -0700

---

```
-----BEGIN PGP SIGNED MESSAGE-----
Hash: SHA256

APPLE-SA-10-26-2026-3 iOS 18.7.11 and iPadOS 18.7.11

iOS 18.7.11 and iPadOS 18.7.11 addresses the following issues.
Information about the security content is also available at
https://support.apple.com/149225.

Apple maintains a Security Releases page at
https://support.apple.com/100100 which lists recent
software updates with security advisories.

Audio
Available for: iPhone XS, iPhone XS Max, iPhone XR, iPad 7th
generationAir 4th generation and later, iPad 9th generation and later,
and iPad mini 6th generation and later
Impact: An app may be able to leak sensitive user information
Description: A logic issue was addressed with improved checks.
CVE-2026-65339: Mustafa Calap (@ordinal0, dbg.re), Meta Red Team X - Nik
Tsytsarkin

CoreGraphics
Available for: iPhone XS, iPhone XS Max, iPhone XR, iPad 7th
generationAir 4th generation and later, iPad 9th generation and later,
and iPad mini 6th generation and later
Impact: Processing a maliciously crafted file may lead to arbitrary code
execution. Apple is aware of a report that this issue may have been
exploited in an extremely sophisticated attack against specific targeted
individuals on versions of iOS before iOS 27.
Description: An out-of-bounds write issue was addressed with improved
bounds checking.
CVE-2026-86950: Meta Product Security

CoreMedia
Available for: iPhone XS, iPhone XS Max, iPhone XR, iPad 7th
generationAir 4th generation and later, iPad 9th generation and later,
and iPad mini 6th generation and later
Impact: A malicious app may be able to access the camera without user
permission
Description: An access issue was addressed with improved access
restrictions.
CVE-2026-86990: Mustafa Calap (@ordinal0, dbg.re)

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

The automatic update process may take up to a week depending on the
day that iTunes or the device checks for updates. You may manually
obtain the update via the Check for Updates button within iTunes, or
the Software Update on your device.

To check that the iPhone, iPod touch, or iPad has been updated:

* Navigate to Settings
* Select General
* Select About.
* The version after applying this update will be "iOS 18.7.11 and iPadOS
18.7.11".

All information is also posted on the Apple Security Releases
web site: https://support.apple.com/100100.

This message is signed with Apple's Product Security PGP key,
and details are available at:
https://www.apple.com/support/security/pgp/

-----BEGIN PGP SIGNATURE-----

iQIzBAEBCAAdFiEEhjkl+zMLNwFiCT1o4Ifiq8DH7PUFAmrfvLQACgkQ4Ifiq8DH
7PWbphAAuvTfoY9oqnKSiTdILV7Y9cN7MluSTQWgr292dJaIgSCdaeDZl1liUcE3
5VG8kFU6ynsxlPm1bHEUzxj+2uTaOpNcvrVw876YES7S6v/TQ73PLncQDQ8aviQ3
P6+FWGfui2mWNTshGeSbCJIp8k68ew+sJP8S+qr8F1E3fHMGxXaDx6wYjuTf68Sf
+rBfpn0trEQpyO7xPGLTgOi6Cv28rnAXzX5iMYL3yCpXWZ0F4FqKpTw0cKUbPpQb
fCQA33bgmTWtWeynLSxAOX91Sm3AGRchpeKkf7SU4saj3pDcjU8iHPDjpFWo/E3J
vBT6vWjR95s+6hEFEoKvP48ezjnsD6Mz5Hrkq6KbWzBs5GgB0ySg1S4rbgDADPVp
aDsEz6qbF5NB+aExc6F7/eFcJHDo31lGbmxUreTBgyUkUQ32tztttMmKRyQ3Teyt
1XSxM6ajFldpDlNN8hJJ8Q3zvmurwRI/pAKQxs+VhquxKS2ZpVE2WD3Df4EAqIWd
8Tbt1FH7pA7hqAN9wOcrs3/aNGNFEK3weTMQiRzgmfTJ5/pLHBXAHOeahTEfnCmX
/6WuGviJHrrrWzQjcTmqh2ZH8jjC7moU5bBAYelH7LmCsvo1eBMJ6p+N1vGt2N5G
d1PtmpFWz0zoqdiKBjoiKAP55yzYWh4YHSvzBIQPLBgtGnR/pl8=
=aO7b
-----END PGP SIGNATURE-----

_______________________________________________
Sent through the Full Disclosure mailing list
https://nmap.org/mailman/listinfo/fulldisclosure
Web Archives & RSS: https://seclists.org/fulldisclosure/
```

---

[![Previous](/images/left-icon-16x16.png)](40)
[By Date](date.html#41)
[![Next](/images/right-icon-16x16.png)](42)

[![Previous](/images/left-icon-16x16.png)](40)
[By Thread](index.html#41)
[![Next](/images/right-icon-16x16.png)](42)

### Current thread:

* **APPLE-SA-10-26-2026-3 iOS 18.7.11 and iPadOS 18.7.11** *Apple Product Security via Fulldisclosure (Oct 27)*

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