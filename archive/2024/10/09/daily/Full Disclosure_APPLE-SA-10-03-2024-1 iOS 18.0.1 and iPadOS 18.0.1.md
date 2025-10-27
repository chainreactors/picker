---
title: APPLE-SA-10-03-2024-1 iOS 18.0.1 and iPadOS 18.0.1
url: https://seclists.org/fulldisclosure/2024/Oct/1
source: Full Disclosure
date: 2024-10-09
fetch_date: 2025-10-06T19:10:30.664723
---

# APPLE-SA-10-03-2024-1 iOS 18.0.1 and iPadOS 18.0.1

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

[![Previous](/images/left-icon-16x16.png)](0)
[By Date](date.html#1)
[![Next](/images/right-icon-16x16.png)](2)

[![Previous](/images/left-icon-16x16.png)](0)
[By Thread](index.html#1)
[![Next](/images/right-icon-16x16.png)](2)

![](/shared/images/nst-icons.svg#search)

# APPLE-SA-10-03-2024-1 iOS 18.0.1 and iPadOS 18.0.1

---

*From*: Apple Product Security via Fulldisclosure <fulldisclosure () seclists org>
*Date*: Thu, 03 Oct 2024 16:50:41 -0700

---

```
-----BEGIN PGP SIGNED MESSAGE-----
Hash: SHA256

APPLE-SA-10-03-2024-1 iOS 18.0.1 and iPadOS 18.0.1

iOS 18.0.1 and iPadOS 18.0.1 addresses the following issues.
Information about the security content is also available at
https://support.apple.com/121373.

Apple maintains a Security Releases page at
https://support.apple.com/100100 which lists recent
software updates with security advisories.

Media Session
Available for: iPhone 16 (all models)
Impact: Audio messages in Messages may be able to capture a few seconds
of audio before the microphone indicator is activated
Description: This issue was addressed with improved checks.
CVE-2024-44207: Michael Jimenez and an anonymous researcher

Passwords
Available for: iPhone XS and later, iPad Pro 13-inch, iPad Pro 12.9-inch
3rd generation and later, iPad Pro 11-inch 1st generation and later,
iPad Air 3rd generation and later, iPad 7th generation and later, and
iPad mini 5th generation and later
Impact: A user's saved passwords may be read aloud by VoiceOver
Description: A logic issue was addressed with improved validation.
CVE-2024-44204: Bistrit Dahal

This update is available through iTunes and Software Update on your
iOS device, and will not appear in your computer's Software Update
application, or in the Apple Downloads site. Make sure you have an
Internet connection and have installed the latest version of iTunes
from https://www.apple.com/itunes/

iTunes and Software Update on the device will automatically check
Apple's update server on its weekly schedule. When an update is
detected, it is downloaded and the option to be installed is
presented to the user when the iOS device is docked. We recommend
applying the update immediately if possible. Selecting
Don't Install will present the option the next time you connect
your iOS device.

The automatic update process may take up to a week depending on
the day that iTunes or the device checks for updates. You may
manually obtain the update via the Check for Updates button
within iTunes, or the Software Update on your device.

To check that the iPhone, iPod touch, or iPad has been updated:

* Navigate to Settings
* Select General
* Select About. The version after applying this update will be
"iOS 18.0.1 and iPadOS 18.0.1".

All information is also posted on the Apple Security Releases
web site: https://support.apple.com/100100.

This message is signed with Apple's Product Security PGP key,
and details are available at:
https://www.apple.com/support/security/pgp/

-----BEGIN PGP SIGNATURE-----

iQIzBAEBCAAdFiEEsz9altA7uTI+rE/qX+5d1TXaIvoFAmb/LLMACgkQX+5d1TXa
Ivp/oBAAtCfF765M4s/Iwi15gaFUFbOe5Droq7gCJEvtwSsfYFESbM5eCiGZjn4y
Na+d9SrlgymDhIz5j6ZDZdSHKjCLhlkYc+JxpjgUM7rPxJtpn1QBGdDcjUfhpesV
sPxIaQk3lok4uLdBt9tbDT1a+pI67vKa2hm3FmZHsj5MZLSUJaR3d5rq2MWo3RjD
dfVsDhdCvnhk0vSA7ro8/EXVX1W6Jq8UQRGMjXcZgTiSWIx4TLdx6cNGD53dPuzl
ffP6M4XHi247tolr8gs0+EBBlnwUVF1DGgx5MZGuxO++MNLo0SF25HTZN6bmuEQy
zcQjuOHUzEazRzs9lO6IqAoY+YFQKW/UN3+Fj0RNKl2OXloRf2DTgl1C53V+uVyB
MdtJtYCJ1YxwKnhzGsmjclk5oqUrtEKL4Yeri1TxbfXBgoFflNLNRgRrwqkIoPKy
XURcpZ7/yD62Y4uMDIXFWV6FlEPZ/lPnM9Yh7Nh3ocJwJFlsHItuhJrwgyjLkfCZ
Lnerb7en4FbxEfewnjbdCh06P58e5c3XVVSVGNwIyIxeoTO7lT7E7V9tcaSi1L9s
QYN5+zcssTumEdbns6mwivpES16Z+4LuQZfgcfynreLZA6B7LHgqXEmSDcujF8SC
P4hiBFqyccXGrvTR47fGf8+6JPnErrFKOBEcfEu7NUYW8smtxM0=
=n+NZ
-----END PGP SIGNATURE-----
_______________________________________________
Sent through the Full Disclosure mailing list
https://nmap.org/mailman/listinfo/fulldisclosure
Web Archives & RSS: https://seclists.org/fulldisclosure/
```

---

[![Previous](/images/left-icon-16x16.png)](0)
[By Date](date.html#1)
[![Next](/images/right-icon-16x16.png)](2)

[![Previous](/images/left-icon-16x16.png)](0)
[By Thread](index.html#1)
[![Next](/images/right-icon-16x16.png)](2)

### Current thread:

* **APPLE-SA-10-03-2024-1 iOS 18.0.1 and iPadOS 18.0.1** *Apple Product Security via Fulldisclosure (Oct 07)*

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