---
title: APPLE-SA-11-03-2025-9 Xcode 26.1
url: https://seclists.org/fulldisclosure/2025/Nov/10
source: Full Disclosure
date: 2025-11-07
fetch_date: 2025-11-08T03:06:37.378661
---

# APPLE-SA-11-03-2025-9 Xcode 26.1

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

[![Previous](/images/left-icon-16x16.png)](9)
[By Date](date.html#10)
[![Next](/images/right-icon-16x16.png)](11)

[![Previous](/images/left-icon-16x16.png)](9)
[By Thread](index.html#10)
[![Next](/images/right-icon-16x16.png)](11)

![](/shared/images/nst-icons.svg#search)

# APPLE-SA-11-03-2025-9 Xcode 26.1

---

*From*: Apple Product Security via Fulldisclosure <fulldisclosure () seclists org>
*Date*: Mon, 03 Nov 2025 17:35:45 -0800

---

```
-----BEGIN PGP SIGNED MESSAGE-----
Hash: SHA256

APPLE-SA-11-03-2025-9 Xcode 26.1

Xcode 26.1 addresses the following issues.
Information about the security content is also available at
https://support.apple.com/125641.

Apple maintains a Security Releases page at
https://support.apple.com/100100 which lists recent
software updates with security advisories.

GNU
Available for: macOS Sequoia 15.6 and later
Impact: Processing a maliciously crafted file may lead to heap
corruption
Description: An out-of-bounds write issue was addressed with improved
input validation.
CVE-2025-43505: Nathaniel Oh (@calysteon)

lldb
Available for: macOS Sequoia 15.6 and later
Impact: A user in a privileged network position may be able to cause a
denial-of-service
Description: A buffer overflow was addressed with improved bounds
checking.
CVE-2025-43504: Nathaniel Oh (@calysteon)

Xcode 26.1 may be obtained from:
https://developer.apple.com/xcode/downloads/.  To check that the Xcode
has been updated:  * Select Xcode in the menu bar * Select About
Xcode * The version after applying this update will be "Xcode 26.1".

All information is also posted on the Apple Security Releases
web site: https://support.apple.com/100100.

This message is signed with Apple's Product Security PGP key,
and details are available at:
https://www.apple.com/support/security/pgp/

-----BEGIN PGP SIGNATURE-----

iQIzBAEBCAAdFiEEhjkl+zMLNwFiCT1o4Ifiq8DH7PUFAmkJTf4ACgkQ4Ifiq8DH
7PW4Lg//Uh2XAlBJDaLyrM+ZBiY4pi1/axxGtD/si573Mx94+yCThTAMUBPN8f+G
OfxtLzfiKscw/NDnZY6Y2jiO6E3MCFVoMAhWVYBP72jtJtM1AhlD5RTLinqClJ6N
A23DgTzvNx49F4TJZbNZeGgbZueUjJECGZV3DzbnZ8lZamXpqyJaFHx2JSe45AXO
b1aJGR33LJeOQ/AqjuYPrbUQZMuzt8++4LN1GyZtv7BomfuMuuWizGA68mWUsj4h
Pi4vjdMfGGzdjTEtFuy+vcSp/b/uaaDq1f5RpzE6c89NLlhk2e+0l03RlGSqnHjo
H2w/mMwuQXU9Czs/uptlSvW4DLMmDuLROqDvywoeiyIhG7GfOq4B0fcsJA5n7Qmn
oM3N7BDSkrddDznLA7FHDJCrRpF7LPtSCEDMH9xLeYuqetPKJH3YpsqMof537CWb
QJIHuP6pqrNsCibySu34kpPgZxby1EYIXw81R5vy4hosnp6MDNXXo5aFz2sKag/M
Pufdit/9+ZpBIiu7bY/rlQxdcehguTwMNrjECGEk5cP2h9YVWq6l4tzc2u1K/yjC
dovQ+PGCTCuLc0uqCymDGlTj4hd/PgASLyZeH2X+y3zCy9c/ZEiNxP0qkKX9Q7pa
gpkg0t69YJPU1gKMnGOfUdq00Y++SRgg6FP4n/UNLwIt5kSpHvE=
=X7ne
-----END PGP SIGNATURE-----

_______________________________________________
Sent through the Full Disclosure mailing list
https://nmap.org/mailman/listinfo/fulldisclosure
Web Archives & RSS: https://seclists.org/fulldisclosure/
```

---

[![Previous](/images/left-icon-16x16.png)](9)
[By Date](date.html#10)
[![Next](/images/right-icon-16x16.png)](11)

[![Previous](/images/left-icon-16x16.png)](9)
[By Thread](index.html#10)
[![Next](/images/right-icon-16x16.png)](11)

### Current thread:

* **APPLE-SA-11-03-2025-9 Xcode 26.1** *Apple Product Security via Fulldisclosure (Nov 07)*

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