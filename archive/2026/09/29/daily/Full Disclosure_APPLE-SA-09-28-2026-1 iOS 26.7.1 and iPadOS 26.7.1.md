---
title: APPLE-SA-09-28-2026-1 iOS 26.7.1 and iPadOS 26.7.1
url: https://seclists.org/fulldisclosure/2026/Sep/89
source: Full Disclosure
date: 2026-09-29
fetch_date: 2026-09-30T07:43:05.625133
---

# APPLE-SA-09-28-2026-1 iOS 26.7.1 and iPadOS 26.7.1

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

[![Previous](/images/left-icon-16x16.png)](88)
[By Date](date.html#89)
[![Next](/images/right-icon-16x16.png)](90)

[![Previous](/images/left-icon-16x16.png)](88)
[By Thread](index.html#89)
[![Next](/images/right-icon-16x16.png)](90)

![](/shared/images/nst-icons.svg#search)

# APPLE-SA-09-28-2026-1 iOS 26.7.1 and iPadOS 26.7.1

---

*From*: Apple Product Security via Fulldisclosure <fulldisclosure () seclists org>
*Date*: Mon, 28 Sep 2026 15:13:06 -0700

---

```
-----BEGIN PGP SIGNED MESSAGE-----
Hash: SHA256

APPLE-SA-09-28-2026-1 iOS 26.7.1 and iPadOS 26.7.1

iOS 26.7.1 and iPadOS 26.7.1 addresses the following issues.
Information about the security content is also available at
https://support.apple.com/149226.

Apple maintains a Security Releases page at
https://support.apple.com/100100 which lists recent
software updates with security advisories.

CoreGraphics
Available for: iPhone 11 and later, iPad Pro 12.9-inch 3rd generation
and later, iPad Pro 11-inch 1st generation and later, iPad Air 3rd
generation and later, iPad 8th generation and later, and iPad mini 5th
generation and later
Impact: Processing a maliciously crafted file may lead to arbitrary code
execution. Apple is aware of a report that this issue may have been
exploited in an extremely sophisticated attack against specific targeted
individuals on versions of iOS before iOS 27.
Description: An out-of-bounds write issue was addressed with improved
bounds checking.
CVE-2026-86950: Meta Product Security

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
* The version after applying this update will be "iOS 26.7.1 and iPadOS
26.7.1".

All information is also posted on the Apple Security Releases
web site: https://support.apple.com/100100.

This message is signed with Apple's Product Security PGP key,
and details are available at:
https://www.apple.com/support/security/pgp/

-----BEGIN PGP SIGNATURE-----

iQIzBAEBCAAdFiEEhjkl+zMLNwFiCT1o4Ifiq8DH7PUFAmq62rYACgkQ4Ifiq8DH
7PVSthAAhRcLo1fmZS6vcpSPRNrXhkv6mf6tRi93Lmps8ltcrq9HjzjerrEpFt0M
Oy7yUy4RTmvfHw5BWaAupPqDlDnlp3+mEXM7aVayiCSXWBgww3CkqfyrHGoXPOsy
3gBGHZg/7KIigFa1m3vaB4DXcpaNqOy02FjLajlaxUIm0T1qyJ4ifYkG4Dz8S+4E
rf/XSL/TW3ZHPQmPRFk6EX53FKbAIGPpa3dKccEINVrH8UPxotQKKFGGitPQCXsY
HWVzZ2+S0Uec0Nbmon3JP4DukBm1szs6nqfVTplIwkY0wyT5bOFBPylGb7WBfPWR
5Dsqi1YSvZ2Fg0/4GsbVPUjgckQ5lpK22owTfBiUjQqBAJlE+QSZyBx0gSlXDnvG
vhlletENEnv4Gpk2DjumNIXEFoAjj+TKzEuodWB0yhlYVHzLaXLgGlxY/PmpOst4
LUtHySdshhaeIWTrLizGVB9MwEF5jwR2KP1XgpNdPvnmNoMhl7hRdAuULEOHYE6M
ABO9KyYzXomfr5Hf5O+Im7H9i9jcHyyg3+RGf+5Uh+GphskT5ydkuFLm18uvefAA
u7mN5Ct0EH7emXXJXOXgu65L0punzGb4ev5bpribfCCBroY28BBayM4KUuLbKCoe
qBIMH5kyZM+1NiMEbVHSSAEPtX+9/wY50Q8sx0Rdg9zuSwb/Ae0=
=/ORp
-----END PGP SIGNATURE-----

_______________________________________________
Sent through the Full Disclosure mailing list
https://nmap.org/mailman/listinfo/fulldisclosure
Web Archives & RSS: https://seclists.org/fulldisclosure/
```

---

[![Previous](/images/left-icon-16x16.png)](88)
[By Date](date.html#89)
[![Next](/images/right-icon-16x16.png)](90)

[![Previous](/images/left-icon-16x16.png)](88)
[By Thread](index.html#89)
[![Next](/images/right-icon-16x16.png)](90)

### Current thread:

* **APPLE-SA-09-28-2026-1 iOS 26.7.1 and iPadOS 26.7.1** *Apple Product Security via Fulldisclosure (Sep 28)*

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