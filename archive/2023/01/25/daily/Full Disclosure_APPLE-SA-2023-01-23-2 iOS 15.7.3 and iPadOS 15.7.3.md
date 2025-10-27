---
title: APPLE-SA-2023-01-23-2 iOS 15.7.3 and iPadOS 15.7.3
url: https://seclists.org/fulldisclosure/2023/Jan/16
source: Full Disclosure
date: 2023-01-25
fetch_date: 2025-10-04T04:48:39.396354
---

# APPLE-SA-2023-01-23-2 iOS 15.7.3 and iPadOS 15.7.3

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

[![Previous](/images/left-icon-16x16.png)](15)
[By Date](date.html#16)
[![Next](/images/right-icon-16x16.png)](17)

[![Previous](/images/left-icon-16x16.png)](15)
[By Thread](index.html#16)
[![Next](/images/right-icon-16x16.png)](17)

![](/shared/images/nst-icons.svg#search)

# APPLE-SA-2023-01-23-2 iOS 15.7.3 and iPadOS 15.7.3

---

*From*: Apple Product Security via Fulldisclosure <fulldisclosure () seclists org>
*Date*: Mon, 23 Jan 2023 18:40:33 -0800

---

```
-----BEGIN PGP SIGNED MESSAGE-----
Hash: SHA256

APPLE-SA-2023-01-23-2 iOS 15.7.3 and iPadOS 15.7.3

iOS 15.7.3 and iPadOS 15.7.3 addresses the following issues.
Information about the security content is also available at
https://support.apple.com/HT213598.

Kernel
Available for: iPhone 6s (all models), iPhone 7 (all models), iPhone
SE (1st generation), iPad Air 2, iPad mini (4th generation), and iPod
touch (7th generation)
Impact: An app may be able to leak sensitive kernel state
Description: The issue was addressed with improved memory handling.
CVE-2023-23500: Pan ZhenPeng (@Peterpan0927) of STAR Labs SG Pte.
Ltd. (@starlabs_sg)

Kernel
Available for: iPhone 6s (all models), iPhone 7 (all models), iPhone
SE (1st generation), iPad Air 2, iPad mini (4th generation), and iPod
touch (7th generation)
Impact: An app may be able to execute arbitrary code with kernel
privileges
Description: The issue was addressed with improved memory handling.
CVE-2023-23504: Adam Doupé of ASU SEFCOM

Mail Exchange
Available for: iPhone 6s (all models), iPhone 7 (all models), iPhone
SE (1st generation), iPad Air 2, iPad mini (4th generation), and iPod
touch (7th generation)
Impact: The quoted original message may be selected from the wrong
email when forwarding an email from an Exchange account
Description: A logic issue was addressed with improved state
management.
CVE-2023-23498: an anonymous researcher

Maps
Available for: iPhone 6s (all models), iPhone 7 (all models), iPhone
SE (1st generation), iPad Air 2, iPad mini (4th generation), and iPod
touch (7th generation)
Impact: An app may be able to bypass Privacy preferences
Description: A logic issue was addressed with improved state
management.
CVE-2023-23503: an anonymous researcher

Screen Time
Available for: iPhone 6s (all models), iPhone 7 (all models), iPhone
SE (1st generation), iPad Air 2, iPad mini (4th generation), and iPod
touch (7th generation)
Impact: An app may be able to access information about a user’s
contacts
Description: A privacy issue was addressed with improved private data
redaction for log entries.
CVE-2023-23505: Wojciech Reguła of SecuRing (wojciechregula.blog)

Additional recognition

Kernel
We would like to acknowledge Nick Stenning of Replicate for their
assistance.

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
after applying this update will be "iOS 15.7.3 and iPadOS 15.7.3".
All information is also posted on the Apple Security Updates
web site: https://support.apple.com/en-us/HT201222.

This message is signed with Apple's Product Security PGP key,
and details are available at:
https://www.apple.com/support/security/pgp/
-----BEGIN PGP SIGNATURE-----

iQIzBAEBCAAdFiEEBP+4DupqR5Sgt1DB4RjMIDkeNxkFAmPPIl4ACgkQ4RjMIDke
NxnTgBAA397wEr120zYgAsNrT8yO2jK4jPy8ieRFcXDPRzFB/6nvt282CdqRaN5P
+b3WqRzo6WvBrYhzIeIE2pIl6meHzqP2WQZxtdb4DMNKEaVqr4ybisiYi2ItGp1g
E+nPKERMMvOngteQt+DVqowW1NjU+soujaOrjHdJaR7gPKokankuQz23Wot+s7cA
mcPXtuSoHQPfs7OMiqi9h2GLN4+gnzEJuBdGkVfIozRS6WJeKGs1sf/UUcShUqhg
L19OAID8E8envhBSp8qBuqvF91PcHnAfIIV83CR9BZ0nxF/qG0IPA49MUM+2lW+l
rpa3rNdznUK5AvYyYgdypnu3KzzerKL7eVR5Z1yzK7ZXVi7e9pdJ0KkSSuezCwYE
DdqlmTdahe0zpcQU7SK/Ij6XAMmdbLBpDQLneWqwOrDLmgrU8nPl/cECiqd+FPuS
9i60uDfaEy8liVZrojuKKShdt6Yy+seXJo1THHUN76atpR0CNUYDevnVlW+7Z25c
1Hk403i7NDNE+aT+oEhpdESHH49xSoA2a0JZuOK4qEovWCcztz6zOx/extokdmIk
I7XuKd0wlsxh1wflptadSAsjk12AF3D2PXffGuS2qZ2sr4KamLvvoGfkYZqf+uRO
Q+8i8fjUUHXWQsHs7+lE87QS+CazMka9H5tOupsJFXdsd6dIHUE=
=gSV7
-----END PGP SIGNATURE-----

_______________________________________________
Sent through the Full Disclosure mailing list
https://nmap.org/mailman/listinfo/fulldisclosure
Web Archives & RSS: https://seclists.org/fulldisclosure/
```

---

[![Previous](/images/left-icon-16x16.png)](15)
[By Date](date.html#16)
[![Next](/images/right-icon-16x16.png)](17)

[![Previous](/images/left-icon-16x16.png)](15)
[By Thread](index.html#16)
[![Next](/images/right-icon-16x16.png)](17)

### Current thread:

* **APPLE-SA-2023-01-23-2 iOS 15.7.3 and iPadOS 15.7.3** *Apple Product Security via Fulldisclosure (Jan 23)*

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