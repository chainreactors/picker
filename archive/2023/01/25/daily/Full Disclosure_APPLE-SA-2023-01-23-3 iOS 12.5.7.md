---
title: APPLE-SA-2023-01-23-3 iOS 12.5.7
url: https://seclists.org/fulldisclosure/2023/Jan/17
source: Full Disclosure
date: 2023-01-25
fetch_date: 2025-10-04T04:48:38.160209
---

# APPLE-SA-2023-01-23-3 iOS 12.5.7

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

[![Previous](/images/left-icon-16x16.png)](16)
[By Date](date.html#17)
[![Next](/images/right-icon-16x16.png)](19)

[![Previous](/images/left-icon-16x16.png)](16)
[By Thread](index.html#17)
[![Next](/images/right-icon-16x16.png)](19)

![](/shared/images/nst-icons.svg#search)

# APPLE-SA-2023-01-23-3 iOS 12.5.7

---

*From*: Apple Product Security via Fulldisclosure <fulldisclosure () seclists org>
*Date*: Mon, 23 Jan 2023 18:40:45 -0800

---

```
-----BEGIN PGP SIGNED MESSAGE-----
Hash: SHA256

APPLE-SA-2023-01-23-3 iOS 12.5.7

iOS 12.5.7 addresses the following issues.
Information about the security content is also available at
https://support.apple.com/HT213597.

WebKit
Available for: iPhone 5s, iPhone 6, iPhone 6 Plus, iPad Air, iPad
mini 2, iPad mini 3, and iPod touch (6th generation)
Impact: Processing maliciously crafted web content may lead to
arbitrary code execution. Apple is aware of a report that this issue
may have been actively exploited against versions of iOS released
before iOS 15.1.
Description: A type confusion issue was addressed with improved state
handling.
WebKit Bugzilla: 248266
CVE-2022-42856: ClÃ©ment Lecigne of Google's Threat Analysis Group

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
after applying this update will be "iOS 12.5.7".
All information is also posted on the Apple Security Updates
web site: https://support.apple.com/en-us/HT201222.

This message is signed with Apple's Product Security PGP key,
and details are available at:
https://www.apple.com/support/security/pgp/
-----BEGIN PGP SIGNATURE-----

iQIzBAEBCAAdFiEEBP+4DupqR5Sgt1DB4RjMIDkeNxkFAmPPIl4ACgkQ4RjMIDke
Nxk+Gw//TvgmHpZaxvWNFgNweQ3WivIf4JesoYk2EkUMLU04+HcPm+0cPQqG9fBX
kFtmRYvbkb2i3Bhf9NSy5rA5kJ+XRdRalnQCoQ7A1YppUZvjgrOzjf5AsWcFJDB1
cjuIcKhyhqPlyIHGM2/O57WUhYrkDWTybvNiD2s6V9B8sWhiOdMJ4U4eUXl0mR14
KF8OauxIoZsaxAd1XIch8W8GffjTi+Kd2uDji59JYJndKakdNmy793bKrJWRUrGa
keKttpBKMr1U834+x0pOcMkUwpY/Yo5DECKGLkpZlFHW0kZpFAckhvpEXYF5yrEW
wURiMx1+3G6GgNQeoAj0DhVZMu+FtkpzjZVtZIm1KWWUhIQklUpsyxg612CukSxZ
oQYkjkWhYIH6vlrPvlc1nnZJd2vsV6xyhGk0a1ZCwMr8mRvAzy6S2wHnfoyBrqy/
yHa7PnsGlmRt2Y7qyOJ+UO47AgvM8M0or9BJwyGVhj9sqeKFDC0Yjs1XWB8pg9W9
KGf+3Kb4oxth6asxlI9IRiIYeGYD/zKftuCZ+Pc2suwZqWaTAJR1wk1tXCdTgFjy
u9z7dfRAJyrc5lPbOOPLxyG1evtvtGXmj7zcSJVAHRH4MUxgbu/KxbkkRXTGmBqX
CFu26QnzxFpEJYV/j2w9pmmKT7JjCFDw2G5wYJtbzTX+lLP1o+E=
=j70k
-----END PGP SIGNATURE-----

_______________________________________________
Sent through the Full Disclosure mailing list
https://nmap.org/mailman/listinfo/fulldisclosure
Web Archives & RSS: https://seclists.org/fulldisclosure/
```

---

[![Previous](/images/left-icon-16x16.png)](16)
[By Date](date.html#17)
[![Next](/images/right-icon-16x16.png)](19)

[![Previous](/images/left-icon-16x16.png)](16)
[By Thread](index.html#17)
[![Next](/images/right-icon-16x16.png)](19)

### Current thread:

* **APPLE-SA-2023-01-23-3 iOS 12.5.7** *Apple Product Security via Fulldisclosure (Jan 23)*

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