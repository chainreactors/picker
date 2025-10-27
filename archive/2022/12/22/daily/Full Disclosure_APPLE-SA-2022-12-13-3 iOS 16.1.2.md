---
title: APPLE-SA-2022-12-13-3 iOS 16.1.2
url: https://seclists.org/fulldisclosure/2022/Dec/22
source: Full Disclosure
date: 2022-12-22
fetch_date: 2025-10-04T02:15:08.875502
---

# APPLE-SA-2022-12-13-3 iOS 16.1.2

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

[![Previous](/images/left-icon-16x16.png)](21)
[By Date](date.html#22)
[![Next](/images/right-icon-16x16.png)](23)

[![Previous](/images/left-icon-16x16.png)](21)
[By Thread](index.html#22)
[![Next](/images/right-icon-16x16.png)](23)

![](/shared/images/nst-icons.svg#search)

# APPLE-SA-2022-12-13-3 iOS 16.1.2

---

*From*: Apple Product Security via Fulldisclosure <fulldisclosure () seclists org>
*Date*: Tue, 13 Dec 2022 16:34:39 -0800

---

```
-----BEGIN PGP SIGNED MESSAGE-----
Hash: SHA256

APPLE-SA-2022-12-13-3 iOS 16.1.2

iOS 16.1.2 addresses the following issues.
Information about the security content is also available at
https://support.apple.com/HT213516.

WebKit
Available for: iPhone 8 and later
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
after applying this update will be "iOS 16.1.2".
All information is also posted on the Apple Security Updates
web site: https://support.apple.com/en-us/HT201222.

This message is signed with Apple's Product Security PGP key,
and details are available at:
https://www.apple.com/support/security/pgp/
-----BEGIN PGP SIGNATURE-----

iQIzBAEBCAAdFiEEBP+4DupqR5Sgt1DB4RjMIDkeNxkFAmOZFYEACgkQ4RjMIDke
Nxll4hAAolqnH+W3gE3w2Xri3wUchwkj6WPhfWcwwc+l0cxUxiDqzhGSkW4kNTVI
eCjENaJ4WfsK7COfxx8qnmQtcqV8P406XtDomeE96Rm/euCEzkSpVPSs4S8+YwvO
qRNWVbWmWQ1gKFSqkuZb2Y5IAnA+KI3Fw1M1iq8Cbs/bkUVjNfrIrrPgl19BercE
Ojsjq+BQS15dIq84GUiSv/KTU31NKMeSQLB8O9+u91tuBex2b+1mdwb15K1R17OI
e/exVA2qnQFctfhWu2uh2izckATylQjtvQHMr0pAwdEoLyRl1xXrW62DeVwWBsn0
bxUhjSfS/clmXyN/hL1ocgUrHrI9yAVST5oug/LqR8RjTkgTBcGF9C0YMXaexvA0
y2AhF70pl67UESleBSRddayFAW2lZkV/YdJosxGLsRviy8jdiiQ4VJ5xI9TAECbU
GgF2qHVSz4gnlyyDUfUqHUmjLej48qCMbadY4IQQmvW30yiCW+shHfaLzCBYZ2cL
hUCD7IqU7C1+KE+bJ1Y/k7EXOkLWhZ9go7kKUF6OfpVd6OPIYd4R38eghUXU4Zvi
QwYQlkXm1Q+DZrwaOvMf0kMkCA/10ktuzhKSpiCI/47BqcE8VYi0CCbOUaSZSPi6
P0jlpuIsxCd1UKkGaTsfdJIyeNY1VPHkiOl2BYpIelCqqhOiNHc=
=wMpD
-----END PGP SIGNATURE-----

_______________________________________________
Sent through the Full Disclosure mailing list
https://nmap.org/mailman/listinfo/fulldisclosure
Web Archives & RSS: https://seclists.org/fulldisclosure/
```

---

[![Previous](/images/left-icon-16x16.png)](21)
[By Date](date.html#22)
[![Next](/images/right-icon-16x16.png)](23)

[![Previous](/images/left-icon-16x16.png)](21)
[By Thread](index.html#22)
[![Next](/images/right-icon-16x16.png)](23)

### Current thread:

* **APPLE-SA-2022-12-13-3 iOS 16.1.2** *Apple Product Security via Fulldisclosure (Dec 20)*

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