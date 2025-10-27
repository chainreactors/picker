---
title: APPLE-SA-2023-01-23-6 macOS Big Sur 11.7.3
url: https://seclists.org/fulldisclosure/2023/Jan/21
source: Full Disclosure
date: 2023-01-25
fetch_date: 2025-10-04T04:48:34.562779
---

# APPLE-SA-2023-01-23-6 macOS Big Sur 11.7.3

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

[![Previous](/images/left-icon-16x16.png)](20)
[By Date](date.html#21)
[![Next](/images/right-icon-16x16.png)](22)

[![Previous](/images/left-icon-16x16.png)](20)
[By Thread](index.html#21)
[![Next](/images/right-icon-16x16.png)](22)

![](/shared/images/nst-icons.svg#search)

# APPLE-SA-2023-01-23-6 macOS Big Sur 11.7.3

---

*From*: Apple Product Security via Fulldisclosure <fulldisclosure () seclists org>
*Date*: Mon, 23 Jan 2023 18:41:01 -0800

---

```
-----BEGIN PGP SIGNED MESSAGE-----
Hash: SHA256

APPLE-SA-2023-01-23-6 macOS Big Sur 11.7.3

macOS Big Sur 11.7.3 addresses the following issues.
Information about the security content is also available at
https://support.apple.com/HT213603.

AppleMobileFileIntegrity
Available for: macOS Big Sur
Impact: An app may be able to access user-sensitive data
Description: This issue was addressed by enabling hardened runtime.
CVE-2023-23499: Wojciech Reguła (@_r3ggi) of SecuRing
(wojciechregula.blog)

curl
Available for: macOS Big Sur
Impact: Multiple issues in curl
Description: Multiple issues were addressed by updating to curl
version 7.85.0.
CVE-2022-35252

dcerpc
Available for: macOS Big Sur
Impact: Mounting a maliciously crafted Samba network share may lead
to arbitrary code execution
Description: A buffer overflow issue was addressed with improved
memory handling.
CVE-2023-23513: Dimitrios Tatsis and Aleksandar Nikolic of Cisco
Talos

PackageKit
Available for: macOS Big Sur
Impact: An app may be able to gain root privileges
Description: A logic issue was addressed with improved state
management.
CVE-2023-23497: Mickey Jin (@patch1t)

Screen Time
Available for: macOS Big Sur
Impact: An app may be able to access information about a user’s
contacts
Description: A privacy issue was addressed with improved private data
redaction for log entries.
CVE-2023-23505: Wojciech Reguła of SecuRing (wojciechregula.blog)

WebKit
Available for: macOS Big Sur
Impact: Processing maliciously crafted web content may lead to
arbitrary code execution
Description: The issue was addressed with improved memory handling.
WebKit Bugzilla: 248268
CVE-2023-23518: YeongHyeon Choi (@hyeon101010), Hyeon Park
(@tree_segment), SeOk JEON (@_seokjeon), YoungSung Ahn (@_ZeroSung),
JunSeo Bae (@snakebjs0107), Dohyun Lee (@l33d0hyun) of Team ApplePIE
WebKit Bugzilla: 248268
CVE-2023-23517: YeongHyeon Choi (@hyeon101010), Hyeon Park
(@tree_segment), SeOk JEON (@_seokjeon), YoungSung Ahn (@_ZeroSung),
JunSeo Bae (@snakebjs0107), Dohyun Lee (@l33d0hyun) of Team ApplePIE

Windows Installer
Available for: macOS Big Sur
Impact: An app may be able to bypass Privacy preferences
Description: The issue was addressed with improved memory handling.
CVE-2023-23508: Mickey Jin (@patch1t)

macOS Big Sur 11.7.3 may be obtained from the Mac App Store or
Apple's Software Downloads web site:
https://support.apple.com/downloads/
All information is also posted on the Apple Security Updates
web site: https://support.apple.com/en-us/HT201222.

This message is signed with Apple's Product Security PGP key,
and details are available at:
https://www.apple.com/support/security/pgp/
-----BEGIN PGP SIGNATURE-----

iQIzBAEBCAAdFiEEBP+4DupqR5Sgt1DB4RjMIDkeNxkFAmPPIl8ACgkQ4RjMIDke
NxmcTxAA5RgSSuSbRaEzLzDYMXICkEWJLRFDxirCePXlty57qxD+Edl/f7rZhvxx
nt5f0TTSVV2D4j+bb1MC/qFgINJ2SV31UY3nQXg+k85QeCyjEMXQDgIk5QBJd40E
gcPXFOQULvHJAhyKAvNexGqyRTUk4GqifPZNwXFxKC/tsPahr/Bh6OP+l7CkhG7Y
XiDuKLpL7ssAMl6sf7Lg5H114P/6pPwKM949mYzUz+0CH6uXQ7oWSx/KirbR3HD8
W3FQY/iS3hzG6EALUbFWKjxXPHRv/59TQElizLVqfxLQCjSokxyDiW5OehMeefQs
8dFDCMbpbQFC0RBVFVCS3fzhCNu24LfihyUmz9//Azguv3HJhbuZ/kz70JhsLW9F
6mGlbXA/w2rAWXpJ2fRsHSqpZw9jiX1FlfUH+h3T8cmtnfZDduV0AEvCIK8Zp/nq
S6+sZ3i5VtQyUGZc3FKTQVTeMPrXhyLCXlfiCXMfo04P11AJNxOqSHgBH43N8pNp
drRKydDb+u8QpxUzuaxbyn2dgoEaxwRke6jspkPFPZ/ipj8eNLIn2FqQx8CGXCDL
2k/+/a4M/zsGcr39kuGjcXNba6YbXnA8HwWqmKeMwQ+3VTMwf6C2x0h6OBQGIGcv
MyrKHkVVE9KyPk9AULiw4BJYX7MMBmSbpf2OEDP3d06d6e1ljv8=
=hYz5
-----END PGP SIGNATURE-----

_______________________________________________
Sent through the Full Disclosure mailing list
https://nmap.org/mailman/listinfo/fulldisclosure
Web Archives & RSS: https://seclists.org/fulldisclosure/
```

---

[![Previous](/images/left-icon-16x16.png)](20)
[By Date](date.html#21)
[![Next](/images/right-icon-16x16.png)](22)

[![Previous](/images/left-icon-16x16.png)](20)
[By Thread](index.html#21)
[![Next](/images/right-icon-16x16.png)](22)

### Current thread:

* **APPLE-SA-2023-01-23-6 macOS Big Sur 11.7.3** *Apple Product Security via Fulldisclosure (Jan 23)*

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