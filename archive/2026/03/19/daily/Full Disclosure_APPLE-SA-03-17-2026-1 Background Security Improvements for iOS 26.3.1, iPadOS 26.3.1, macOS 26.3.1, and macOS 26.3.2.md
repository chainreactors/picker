---
title: APPLE-SA-03-17-2026-1 Background Security Improvements for iOS 26.3.1, iPadOS 26.3.1, macOS 26.3.1, and macOS 26.3.2
url: https://seclists.org/fulldisclosure/2026/Mar/10
source: Full Disclosure
date: 2026-03-19
fetch_date: 2026-03-20T04:09:29.432657
---

# APPLE-SA-03-17-2026-1 Background Security Improvements for iOS 26.3.1, iPadOS 26.3.1, macOS 26.3.1, and macOS 26.3.2

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

# APPLE-SA-03-17-2026-1 Background Security Improvements for iOS 26.3.1, iPadOS 26.3.1, macOS 26.3.1, and macOS 26.3.2

---

*From*: Apple Product Security via Fulldisclosure <fulldisclosure () seclists org>
*Date*: Tue, 17 Mar 2026 16:43:52 -0700

---

```
-----BEGIN PGP SIGNED MESSAGE-----
Hash: SHA256

APPLE-SA-03-17-2026-1 Background Security Improvements for iOS 26.3.1,
iPadOS 26.3.1, macOS 26.3.1, and macOS 26.3.2

Background Security Improvements for iOS 26.3.1, iPadOS 26.3.1, macOS
26.3.1, and macOS 26.3.2 addresses the following issues.
Information about the security content is also available at
https://support.apple.com/126604.

Apple maintains a Security Releases page at
https://support.apple.com/100100 which lists recent
software updates with security advisories.

iOS 26.3.1 (a), iPadOS 26.3.1 (a), macOS 26.3.1 (a), macOS 26.3.2 (a)

WebKit
Available for: iOS 26.3.1, iPadOS 26.3.1, macOS 26.3.1, macOS 26.3.2
Impact: Processing maliciously crafted web content may bypass Same
Origin Policy
Description: A cross-origin issue in the Navigation API was addressed
with improved input validation.
WebKit Bugzilla: 306050
CVE-2026-20643: Thomas Espach

All information is also posted on the Apple Security Releases
web site: https://support.apple.com/100100.

This message is signed with Apple's Product Security PGP key,
and details are available at:
https://www.apple.com/support/security/pgp/

-----BEGIN PGP SIGNATURE-----

iQIzBAEBCAAdFiEEhjkl+zMLNwFiCT1o4Ifiq8DH7PUFAmm54C8ACgkQ4Ifiq8DH
7PUGUw//S0SC2lJmp6tTNVubRojkwa1ppYTX/UXyJimhlpefU0mkxE4dRlqKzQP7
WA4VRAbKwCZMSoIMrsh+xAkk5noy70jKthNGRpWTi+YIVmxzxChmjbAjrueugiwJ
CZWUyhshmbbFVIMB5agDx6OIvNm4J+eazERM8FHuqKFBkb2V4gcEuzsGd0LQa3BO
EN0UYoU5vBDK7OaEYy7yYYTAcjQgLBW2A799ospesduvz9LY3R6ewenowAQAoxjF
oxz426lRYkuOQ/cFNn1ejrBYBPadgDN4MkIiBmayU0fRqJHMBUZwjde4osJnHKz0
OKbVAlklfLExqtD3W5McOsNUbdncgLz/AL/gSE+Mi2SfK3gyE0ER5KF4ZaSfIBzM
OeZm7jqkr+NORFf3BgoYmbzA4+J5UJ/FVN4aLoKQCLCYS8zq+lG1QNLSBkd3RWHW
V3ieTzyI40SIVH/nFtPwxpcus0ckfrJkDqcEEpfFVadaenuw4QF6mW5ctdAOu1Zf
DvluADw/kXnNRI4ENFMz5qctTQbCOCodmaA0jO46UekXFMpe/emOteA3yTMsIZXq
C4WDFQDwaPqB6SRZoUw2l87bE3liHoS1mKKtb+YcPP0/MJLlU5N4YMLLHhaiz3DJ
AV0gg/q7dGv0l2TJocWybRReTRhXuwVBaCCt9RKjjyUdD79vw0w=
=dtpg
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

* **APPLE-SA-03-17-2026-1 Background Security Improvements for iOS 26.3.1, iPadOS 26.3.1, macOS 26.3.1, and macOS 26.3.2** *Apple Product Security via Fulldisclosure (Mar 19)*

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