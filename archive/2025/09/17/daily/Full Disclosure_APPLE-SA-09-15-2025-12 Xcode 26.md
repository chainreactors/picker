---
title: APPLE-SA-09-15-2025-12 Xcode 26
url: https://seclists.org/fulldisclosure/2025/Sep/60
source: Full Disclosure
date: 2025-09-17
fetch_date: 2025-10-02T20:16:40.995757
---

# APPLE-SA-09-15-2025-12 Xcode 26

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

[![Previous](/images/left-icon-16x16.png)](59)
[By Date](date.html#60)
[![Next](/images/right-icon-16x16.png)](61)

[![Previous](/images/left-icon-16x16.png)](59)
[By Thread](index.html#60)
[![Next](/images/right-icon-16x16.png)](61)

![](/shared/images/nst-icons.svg#search)

# APPLE-SA-09-15-2025-12 Xcode 26

---

*From*: Apple Product Security via Fulldisclosure <fulldisclosure () seclists org>
*Date*: Mon, 15 Sep 2025 16:38:13 -0700

---

```
-----BEGIN PGP SIGNED MESSAGE-----
Hash: SHA256

APPLE-SA-09-15-2025-12 Xcode 26

Xcode 26 addresses the following issues.
Information about the security content is also available at
https://support.apple.com/125117.

Apple maintains a Security Releases page at
https://support.apple.com/100100 which lists recent
software updates with security advisories.

Dev Tools
Available for: macOS Sequoia 15.6 and later
Impact: Processing an overly large path value may crash a process
Description: A path handling issue was addressed with improved
validation.
CVE-2025-43370: Nathaniel Oh (@calysteon)

Dev Tools
Available for: macOS Sequoia 15.6 and later
Impact: Processing an overly large path value may crash a process
Description: The issue was addressed with improved checks.
CVE-2025-43375: Nathaniel Oh (@calysteon)

Git
Available for: macOS Sequoia 15.6 and later
Impact: Cloning a maliciously crafted repository may result in remote
code execution
Description: This is a vulnerability in open source code and Apple
Software is among the affected projects. The CVE-ID was assigned by a
third party. Learn more about the issue and CVE-ID at cve.org.
CVE-2025-48384

IDE CoreML
Available for: macOS Sequoia 15.6 and later
Impact: An app may be able to read and write files outside of its
sandbox
Description: The issue was addressed with improved checks.
CVE-2025-43263: Mickey Jin (@patch1t)

Xcode
Available for: macOS Sequoia 15.6 and later
Impact: An app may be able to break out of its sandbox
Description: This issue was addressed with improved checks.
CVE-2025-43371: Mickey Jin (@patch1t)

Additional recognition

Playgrounds
We would like to acknowledge Wojciech Regula of SecuRing
(wojciechregula.blog) for their assistance.

Xcode 26 may be obtained from:
https://developer.apple.com/xcode/downloads/.  To check that the Xcode
has been updated:  * Select Xcode in the menu bar * Select About
Xcode * The version after applying this update will be "Xcode 26".

All information is also posted on the Apple Security Releases
web site: https://support.apple.com/100100.

This message is signed with Apple's Product Security PGP key,
and details are available at:
https://www.apple.com/support/security/pgp/

-----BEGIN PGP SIGNATURE-----

iQIzBAEBCAAdFiEEhjkl+zMLNwFiCT1o4Ifiq8DH7PUFAmjInQgACgkQ4Ifiq8DH
7PVaEA//TRXJnXHFbkQn4dObasnHUTx5zJRyDmyJNAn9DoYiyxrcaWZZKiI9BjGr
uslUeFCFMrKYU93mVQQEWKbovNOGYE0F74a1wEFzqBQjR5NAVTHYZwHg//sLmZ9X
KjXetJQTkMEGUBgCoCNq5kaVojnwCYchTIJUQQLm60TY547gp4iMR9QFzN2glJ8j
DVapQdtkXJuh37rQ3u+4fxk6BpX6CoFFa2etvN6QVS+luhPanzv1XDQ1iqNcCPjv
6OV1GcbJuhuw0HVag9ZfTzqdh0MpXNqZ4rmn7TDX7S1mJKCQJw7C7GCb0NYsXSQG
XZes61/sdzZgjV9ZBjG1tqxyg+A6TO+4Qpzc71QhwO9DK4CI/lKfQkxoxb68Rvn9
U8V5AKKgFBKDIexU2B/kyftdCyYLj2daZX9kSA9DrLoneEe12APViyWeX0orTR06
pdIzCnctIK6zoFFvB/G0zQBzrYzRvEZOZxgjg9urHSeg2sQdMU1rfntDHbya/kz3
ttyDzwcNAK9IaKdS9+JRQqvtQZ/fJX6aaOAqyGNyCI8yC4Lhs6iSuEm+3WG1fkri
jecHdFKVPs5o+6Ao4epICtr4tE9i+i69zXCGOAm0rxrCkiwibsEoEUCW+n7+iyBq
0LdH9awqTf4vVV1X0yY4Ssnm0uLgPUcCVd6dgDWNXo+z3mZ3++k=
=NVSo
-----END PGP SIGNATURE-----

_______________________________________________
Sent through the Full Disclosure mailing list
https://nmap.org/mailman/listinfo/fulldisclosure
Web Archives & RSS: https://seclists.org/fulldisclosure/
```

---

[![Previous](/images/left-icon-16x16.png)](59)
[By Date](date.html#60)
[![Next](/images/right-icon-16x16.png)](61)

[![Previous](/images/left-icon-16x16.png)](59)
[By Thread](index.html#60)
[![Next](/images/right-icon-16x16.png)](61)

### Current thread:

* **APPLE-SA-09-15-2025-12 Xcode 26** *Apple Product Security via Fulldisclosure (Sep 15)*

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