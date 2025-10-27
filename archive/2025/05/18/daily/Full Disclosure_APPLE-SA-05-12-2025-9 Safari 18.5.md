---
title: APPLE-SA-05-12-2025-9 Safari 18.5
url: https://seclists.org/fulldisclosure/2025/May/13
source: Full Disclosure
date: 2025-05-18
fetch_date: 2025-10-06T22:27:47.567986
---

# APPLE-SA-05-12-2025-9 Safari 18.5

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

[![Previous](/images/left-icon-16x16.png)](12)
[By Date](date.html#13)
[![Next](/images/right-icon-16x16.png)](14)

[![Previous](/images/left-icon-16x16.png)](12)
[By Thread](index.html#13)
[![Next](/images/right-icon-16x16.png)](14)

![](/shared/images/nst-icons.svg#search)

# APPLE-SA-05-12-2025-9 Safari 18.5

---

*From*: Apple Product Security via Fulldisclosure <fulldisclosure () seclists org>
*Date*: Mon, 12 May 2025 15:46:17 -0700

---

```
-----BEGIN PGP SIGNED MESSAGE-----
Hash: SHA256

APPLE-SA-05-12-2025-9 Safari 18.5

Safari 18.5 addresses the following issues.
Information about the security content is also available at
https://support.apple.com/122719.

Apple maintains a Security Releases page at
https://support.apple.com/100100 which lists recent
software updates with security advisories.

WebKit
Available for: macOS Ventura and macOS Sonoma
Impact: A type confusion issue could lead to memory corruption
Description: This issue was addressed with improved handling of floats.
WebKit Bugzilla: 286694
CVE-2025-24213: Google V8 Security Team

WebKit
Available for: macOS Ventura and macOS Sonoma
Impact: Processing maliciously crafted web content may lead to memory
corruption
Description: The issue was addressed with improved checks.
WebKit Bugzilla: 289387
CVE-2025-31223: Andreas Jaegersberger & Ro Achterberg of Nosebeard Labs
WebKit Bugzilla: 289653
CVE-2025-31238: wac working with Trend Micro Zero Day Initiative

WebKit
Available for: macOS Ventura and macOS Sonoma
Impact: Processing maliciously crafted web content may lead to memory
corruption
Description: The issue was addressed with improved memory handling.
WebKit Bugzilla: 287577
CVE-2025-24223: rheza (@ginggilBesel) and an anonymous researcher
WebKit Bugzilla: 291506
CVE-2025-31204: Nan Wang(@eternalsakura13)

WebKit
Available for: macOS Ventura and macOS Sonoma
Impact: Processing maliciously crafted web content may lead to an
unexpected Safari crash
Description: The issue was addressed with improved input validation.
WebKit Bugzilla: 289677
CVE-2025-31217: Ignacio Sanmillan (@ulexec)

WebKit
Available for: macOS Ventura and macOS Sonoma
Impact: Processing maliciously crafted web content may lead to an
unexpected process crash
Description: The issue was addressed with improved checks.
WebKit Bugzilla: 288814
CVE-2025-31215: Jiming Wang and Jikai Ren

WebKit
Available for: macOS Ventura and macOS Sonoma
Impact: Processing maliciously crafted web content may lead to an
unexpected Safari crash
Description: A type confusion issue was addressed with improved state
handling.
WebKit Bugzilla: 290834
CVE-2025-31206: an anonymous researcher

WebKit
Available for: macOS Ventura and macOS Sonoma
Impact: A malicious website may exfiltrate data cross-origin
Description: The issue was addressed with improved checks.
WebKit Bugzilla: 290992
CVE-2025-31205: Ivan Fratric of Google Project Zero

WebKit
Available for: macOS Ventura and macOS Sonoma
Impact: Processing maliciously crafted web content may lead to an
unexpected Safari crash
Description: This issue was addressed with improved memory handling.
WebKit Bugzilla: 290985
CVE-2025-31257: Juergen Schmied of Lynck GmbH

Additional recognition

Safari
We would like to acknowledge @RenwaX23, Akash Labade, Narendra Bhati,
Manager of Cyber Security at Suma Soft Pvt. Ltd, Pune (India) for their
assistance.

WebKit
We would like to acknowledge Mike Dougherty and Daniel White of Google
Chrome and an anonymous researcher for their assistance.

Safari 18.5 may be obtained from the Mac App Store.

All information is also posted on the Apple Security Releases
web site: https://support.apple.com/100100.

This message is signed with Apple's Product Security PGP key,
and details are available at:
https://www.apple.com/support/security/pgp/

-----BEGIN PGP SIGNATURE-----

iQIzBAEBCAAdFiEEsz9altA7uTI+rE/qX+5d1TXaIvoFAmgicyIACgkQX+5d1TXa
IvqKbQ/8Ccj2m4snrZPcCnOs75L9lAuJejO/amAr14Ag5bK17LIkWQKGXf/BLsss
30aqxjhz1gOO+g+9W/AD8dOu4MSeAhtaQQPck8U4PtJ+gtvnObjznycMwkQ9NdF9
ZknYBW/+LNM/sy/2h2hYJQ/YyBCZ65+7iJSvhH/HPiDzgbtJRQaJabkmzcbb2Kv4
i7R8tRnZPMHLGIgtT6nNCn/8sUHxJnZEGrcYUI3yQOYmUce5WkhF8Cf7GAZJ9eXQ
zoW73Vrfo+pjvqShWtAfMKoW9DRVTmGCzkv5L43ENE/sNfSo1y/Ohgq7l7i3I5hw
qIiQ31O1RDGYDWrS4QCOs9jJRZ0LmSPklWn42vHK509EcFuYHOTTK+MTI/DTRiCJ
a/ksWkRetyihlIOXHkjSjMlZkI1V7LX2hXzNWHAroL05kNWVu0kTE80t+szFPJec
ICR8Y2qru/sHL6iLtdxE290f4wM4k+LZsvyBAJ6Eq+XV/UGFU6n5Hm99W5ZqH2iA
g7KFiBZrPlrXXGPzV+bnEWNWpNg8FfNkhTJX5U83/Y8zxTtKw7oOcXak6Az3btAg
ZdDbiiEV/yg1rGHBSFCq4uttI3Uribav4bFb3EYMA4lCAWSFs/l4g7/rwGFg0Pjx
BQv5VYSfhbRfqiiLYgRUqjJ4U4lIU4hZ9EvHu9WptTQKuC5oS3E=
=o/LL
-----END PGP SIGNATURE-----

_______________________________________________
Sent through the Full Disclosure mailing list
https://nmap.org/mailman/listinfo/fulldisclosure
Web Archives & RSS: https://seclists.org/fulldisclosure/
```

---

[![Previous](/images/left-icon-16x16.png)](12)
[By Date](date.html#13)
[![Next](/images/right-icon-16x16.png)](14)

[![Previous](/images/left-icon-16x16.png)](12)
[By Thread](index.html#13)
[![Next](/images/right-icon-16x16.png)](14)

### Current thread:

* **APPLE-SA-05-12-2025-9 Safari 18.5** *Apple Product Security via Fulldisclosure (May 16)*

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