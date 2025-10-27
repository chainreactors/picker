---
title: APPLE-SA-2023-02-13-1 iOS 16.3.1 and iPadOS 16.3.1
url: https://seclists.org/fulldisclosure/2023/Feb/4
source: Full Disclosure
date: 2023-02-15
fetch_date: 2025-10-04T06:42:01.789370
---

# APPLE-SA-2023-02-13-1 iOS 16.3.1 and iPadOS 16.3.1

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

[![Previous](/images/left-icon-16x16.png)](3)
[By Date](date.html#4)
[![Next](/images/right-icon-16x16.png)](5)

[![Previous](/images/left-icon-16x16.png)](3)
[By Thread](index.html#4)
[![Next](/images/right-icon-16x16.png)](5)

![](/shared/images/nst-icons.svg#search)

# APPLE-SA-2023-02-13-1 iOS 16.3.1 and iPadOS 16.3.1

---

*From*: Apple Product Security via Fulldisclosure <fulldisclosure () seclists org>
*Date*: Mon, 13 Feb 2023 17:43:40 -0800

---

```
-----BEGIN PGP SIGNED MESSAGE-----
Hash: SHA256

APPLE-SA-2023-02-13-1 iOS 16.3.1 and iPadOS 16.3.1

iOS 16.3.1 and iPadOS 16.3.1 addresses the following issues.
Information about the security content is also available at
https://support.apple.com/HT213635.

Kernel
Available for: iPhone 8 and later, iPad Pro (all models), iPad Air
3rd generation and later, iPad 5th generation and later, and iPad
mini 5th generation and later
Impact: An app may be able to execute arbitrary code with kernel
privileges
Description: A use after free issue was addressed with improved
memory management.
CVE-2023-23514: Xinru Chi of Pangu Lab, Ned Williamson of Google
Project Zero

WebKit
Available for: iPhone 8 and later, iPad Pro (all models), iPad Air
3rd generation and later, iPad 5th generation and later, iPad mini
5th generation and later
Impact: Processing maliciously crafted web content may lead to
arbitrary code execution. Apple is aware of a report that this issue
may have been actively exploited.
Description: A type confusion issue was addressed with improved
checks.
WebKit Bugzilla: 251944
CVE-2023-23529: an anonymous researcher

Additional recognition
We would like to acknowledge The Citizen Lab at The University of
Torontoâ€™s Munk School for their assistance.

This update is available through iTunes and Software Update on your
iOS device, and will not appear in your computer's Software Update
application, or in the Apple Downloads site. Make sure you have an
Internet connection and have installed the latest version of iTunes
from https://www.apple.com/itunes/  iTunes and Software Update on the
device will automatically check Apple's update server on its weekly
schedule. When an update is detected, it is downloaded and the option
to be installed is presented to the user when the iOS device is
docked. We recommend applying the update immediately if possible.
Selecting Don't Install will present the option the next time you
connect your iOS device.  The automatic update process may take up to
a week depending on the day that iTunes or the device checks for
updates. You may manually obtain the update via the Check for Updates
button within iTunes, or the Software Update on your device.  To
check that the iPhone, iPod touch, or iPad has been updated:  *
Navigate to Settings * Select General * Select About. The version
after applying this update will be "iOS 16.3.1 and iPadOS 16.3.1".
All information is also posted on the Apple Security Updates
web site: https://support.apple.com/en-us/HT201222.

This message is signed with Apple's Product Security PGP key,
and details are available at:
https://www.apple.com/support/security/pgp/
-----BEGIN PGP SIGNATURE-----

iQIzBAEBCAAdFiEEBP+4DupqR5Sgt1DB4RjMIDkeNxkFAmPq5PIACgkQ4RjMIDke
Nxk00xAA6vBGZD0tv5wi0q4B8jiJ3oz5/Om05bfUPLziPG1MvWzcFZYpQmdS+OJW
q219S6uDt0m0ojPLkUgcxQ5OmQ/ViwMbawZaVOpe6aIem33iGkWFyGhvgU7EDLwJ
cIaXd7pMxfkI28AZUgd8Brf/UXnt1Ja13+ixDnrGT2C+3G+kst17+PZZ0bZj+Mwt
xDuPW6uLDegjTmjNXzWuo/mSm2MChzoygsbUOPa0Y29OhmgRCbLu/nOCcPcWRk5i
YlSZU5efZ7yqpjMdIt36TCD/yAd0uttebgnKMMLNjQjDAbPj0j+5NiAmYx75DYks
YCnbs+LRMJ9Fik7lA6ihCavJwgq/PZ5NKR/xA6utkpxQatpT4Swmh2mDabJJK08G
T+UsTfnxRgwPnyOEcSBAg7IaMc6BxIUiVrosp4u+ZYO0QnR6z0CgI+2zqTb+HcCj
OpmCYwDz8pvyO7zZF1SdZZpc6GXsxX/Aq5FahSeWQY1x4i0qbiy0AsP7JBcMbAOS
tKPV14Q9UJ1iTbxI1aaLYxwWmawhN2iCnfjOc+nTC6X5gNtXSF+TRtgGUO8Wr039
PgF7MqJ+24UYjf0IdD9tCRaIHBGpUwFKsHhSk/hRsGi4Yov9U5Bu1BKGvTHwx714
vW6p/vjKajjiP6ljtr7TDwkq1SRPSecX3jrrAGkNoJOw+0xOW5s=
=RxGI
-----END PGP SIGNATURE-----

_______________________________________________
Sent through the Full Disclosure mailing list
https://nmap.org/mailman/listinfo/fulldisclosure
Web Archives & RSS: https://seclists.org/fulldisclosure/
```

---

[![Previous](/images/left-icon-16x16.png)](3)
[By Date](date.html#4)
[![Next](/images/right-icon-16x16.png)](5)

[![Previous](/images/left-icon-16x16.png)](3)
[By Thread](index.html#4)
[![Next](/images/right-icon-16x16.png)](5)

### Current thread:

* **APPLE-SA-2023-02-13-1 iOS 16.3.1 and iPadOS 16.3.1** *Apple Product Security via Fulldisclosure (Feb 14)*

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