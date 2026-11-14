---
title: APPLE-SA-11-09-2026-3 iOS 18.7.12 and iPadOS 18.7.12
url: https://seclists.org/fulldisclosure/2026/Nov/26
source: Full Disclosure
date: 2026-11-13
fetch_date: 2026-11-14T08:21:48.360464
---

# APPLE-SA-11-09-2026-3 iOS 18.7.12 and iPadOS 18.7.12

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

[![Previous](/images/left-icon-16x16.png)](25)
[By Date](date.html#26)
[![Next](/images/right-icon-16x16.png)](27)

[![Previous](/images/left-icon-16x16.png)](25)
[By Thread](index.html#26)
[![Next](/images/right-icon-16x16.png)](27)

![](/shared/images/nst-icons.svg#search)

# APPLE-SA-11-09-2026-3 iOS 18.7.12 and iPadOS 18.7.12

---

*From*: Apple Product Security via Fulldisclosure <fulldisclosure () seclists org>
*Date*: Mon, 09 Nov 2026 16:05:42 -0800

---

```
-----BEGIN PGP SIGNED MESSAGE-----
Hash: SHA256

APPLE-SA-11-09-2026-3 iOS 18.7.12 and iPadOS 18.7.12

iOS 18.7.12 and iPadOS 18.7.12 addresses the following issues.
Information about the security content is also available at
https://support.apple.com/149717.

Apple maintains a Security Releases page at
https://support.apple.com/100100 which lists recent
software updates with security advisories.

AirPlay
Available for: iPhone XS, iPhone XS Max, iPhone XR, iPad 7th generation
Impact: An attacker in Bluetooth range may be able to bypass the rate
limit on pairing code attempts
Description: A logic issue was addressed with improved state management.
CVE-2026-113968: Apple

Bluetooth
Available for: iPhone XS, iPhone XS Max, iPhone XR, iPad 7th generation
Impact: An attacker in Bluetooth range may be able to corrupt process
memory
Description: A use-after-free issue was addressed with improved memory
management.
CVE-2026-113970: Apple

CoreUtils
Available for: iPhone XS, iPhone XS Max, iPhone XR, iPad 7th generation
Impact: A malicious Bluetooth device may be able to establish a pairing
without user interaction
Description: This issue was addressed with improved checks.
CVE-2026-113965: Apple

CoreUtils
Available for: iPhone XS, iPhone XS Max, iPhone XR, iPad 7th generation
Impact: An attacker in Bluetooth range may be able to bypass the rate
limit on pairing code attempts and pair with a device without user
interaction
Description: A logic issue was addressed with improved state management.
CVE-2026-113964: an anonymous researcher

MediaRemote
Available for: iPhone XS, iPhone XS Max, iPhone XR, iPad 7th generation
Impact: An attacker with physical access may be able to pair a device
with an AirPlay receiver from the lock screen
Description: This issue was addressed by restricting options offered on
a locked device.
CVE-2026-113971: Apple

rapportd
Available for: iPhone XS, iPhone XS Max, iPhone XR, iPad 7th generation
Impact: An attacker on the same network may be able to bypass the rate
limit on AirPlay pairing code attempts
Description: A logic issue was addressed with improved state management.
CVE-2026-113969: Apple

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
* The version after applying this update will be "iOS 18.7.12 and iPadOS
18.7.12".

All information is also posted on the Apple Security Releases
web site: https://support.apple.com/100100.

This message is signed with Apple's Product Security PGP key,
and details are available at:
https://www.apple.com/support/security/pgp/

-----BEGIN PGP SIGNATURE-----

iQIzBAEBCAAdFiEEhjkl+zMLNwFiCT1o4Ifiq8DH7PUFAmryPDkACgkQ4Ifiq8DH
7PVhZA//VV+arSHm61SLwWBMjIiaVULq68Jo6WkOD8rJ8Tgzh/L03HXDz52GsXMU
+piR4Yv09DUjewc0IsRLQckszCSHxfCMZXs2PrjmAQPK8KnzhW61qEATt7GRJpbI
ApzHRxhyMEy6IQYVeYZt6fhPYAZoqS1vDD5hWqdCXvxbM+sYnDe/AZae1h2qQgWx
AL+iovST2fZ8187otSd9gTE1QeDcDRGIw2dlRQMbdQAQ4+EO2hJKGvfy3I920uwU
hW+ZnWzOggVjHAWqx78wyN5a0QZBVNEowOMREuEZd7aMIobp4vQx62J9fL1K8/8P
ww15xpq1lpjtcxuk9fesfFS4hB/rbRW280q2LXFLiiEwHTlD7+kGZHNzm2ZkTHUU
1cFztIDsSsxiBjoyE89HJ3SBlN/cHPdmCVDm5xLl9sMnqNSmWhlSc0am3KuudYTC
fgeoSebA2qhiNNcpnTcuEjhNAqi5/xhXAmn1UKN2AWFBAfMnBUk+4aS72Z602kM2
ELqI2ThvIA0UjiKxFyEZc4MP7NsHVfi8Kv3acOqacmp2/QRIhPGkzbpI0NQ8L9ul
znNt8y6Zj7Qo2lqHPwpsysGiXvuQjAYyWcV19LXOnn26qOUl07ukg3hvGAk3GJwg
DbmIsXlvDOshlWALBMTid2HEpDAaHPnRPBh+RqrF+45w/SAzZ+8=
=mnGs
-----END PGP SIGNATURE-----

_______________________________________________
Sent through the Full Disclosure mailing list
https://nmap.org/mailman/listinfo/fulldisclosure
Web Archives & RSS: https://seclists.org/fulldisclosure/
```

---

[![Previous](/images/left-icon-16x16.png)](25)
[By Date](date.html#26)
[![Next](/images/right-icon-16x16.png)](27)

[![Previous](/images/left-icon-16x16.png)](25)
[By Thread](index.html#26)
[![Next](/images/right-icon-16x16.png)](27)

### Current thread:

* **APPLE-SA-11-09-2026-3 iOS 18.7.12 and iPadOS 18.7.12** *Apple Product Security via Fulldisclosure (Nov 12)*

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