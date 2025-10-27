---
title: APPLE-SA-2022-10-27-6 Additional information for APPLE-SA-2022-10-24-3 macOS Monterey 12.6.1
url: https://seclists.org/fulldisclosure/2022/Oct/42
source: Full Disclosure
date: 2022-10-31
fetch_date: 2025-10-03T21:22:03.419502
---

# APPLE-SA-2022-10-27-6 Additional information for APPLE-SA-2022-10-24-3 macOS Monterey 12.6.1

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

[![Previous](/images/left-icon-16x16.png)](41)
[By Date](date.html#42)
[![Next](/images/right-icon-16x16.png)](43)

[![Previous](/images/left-icon-16x16.png)](41)
[By Thread](index.html#42)
[![Next](/images/right-icon-16x16.png)](43)

![](/shared/images/nst-icons.svg#search)

# APPLE-SA-2022-10-27-6 Additional information for APPLE-SA-2022-10-24-3 macOS Monterey 12.6.1

---

*From*: Apple Product Security via Fulldisclosure <fulldisclosure () seclists org>
*Date*: Thu, 27 Oct 2022 18:23:35 -0700

---

```
-----BEGIN PGP SIGNED MESSAGE-----
Hash: SHA256

APPLE-SA-2022-10-27-6 Additional information for APPLE-SA-2022-10-24-3 macOS Monterey 12.6.1

macOS Monterey 12.6.1 addresses the following issues.
Information about the security content is also available at
https://support.apple.com/HT213494.

AppleMobileFileIntegrity
Available for: macOS Monterey
Impact: An app may be able to modify protected parts of the file
system
Description: This issue was addressed by removing additional
entitlements.
CVE-2022-42825: Mickey Jin (@patch1t)

Audio
Available for: macOS Monterey
Impact: Parsing a maliciously crafted audio file may lead to
disclosure of user information
Description: The issue was addressed with improved memory handling.
CVE-2022-42798: Anonymous working with Trend Micro Zero Day
Initiative
Entry added October 27, 2022

Kernel
Available for: macOS Monterey
Impact: An app may be able to execute arbitrary code with kernel
privileges
Description: A memory corruption issue was addressed with improved
state management.
CVE-2022-32944: Tim Michaud (@TimGMichaud) of Moveworks.ai
Entry added October 27, 2022

Kernel
Available for: macOS Monterey
Impact: An app may be able to execute arbitrary code with kernel
privileges
Description: A race condition was addressed with improved locking.
CVE-2022-42803: Xinru Chi of Pangu Lab, John Aakerblom (@jaakerblom)
Entry added October 27, 2022

Kernel
Available for: macOS Monterey
Impact: An app may be able to execute arbitrary code with kernel
privileges
Description: A logic issue was addressed with improved checks.
CVE-2022-42801: Ian Beer of Google Project Zero
Entry added October 27, 2022

ppp
Available for: macOS Monterey
Impact: A buffer overflow may result in arbitrary code execution
Description: The issue was addressed with improved bounds checks.
CVE-2022-32941: an anonymous researcher
Entry added October 27, 2022

Ruby
Available for: macOS Monterey
Impact: A remote user may be able to cause unexpected app termination
or arbitrary code execution
Description: A memory corruption issue was addressed by updating Ruby
to version 2.6.10.
CVE-2022-28739

Sandbox
Available for: macOS Monterey
Impact: An app with root privileges may be able to access private
information
Description: This issue was addressed with improved data protection.
CVE-2022-32862: an anonymous researcher

zlib
Available for: macOS Monterey
Impact: A user may be able to cause unexpected app termination or
arbitrary code execution
Description: This issue was addressed with improved checks.
CVE-2022-37434: Evgeny Legerov
CVE-2022-42800: Evgeny Legerov
Entry added October 27, 2022

Additional recognition

Calendar
We would like to acknowledge an anonymous researcher for their
assistance.

macOS Monterey 12.6.1 may be obtained from the Mac App Store or
Apple's Software Downloads web site:
https://support.apple.com/downloads/
All information is also posted on the Apple Security Updates
web site: https://support.apple.com/en-us/HT201222.

This message is signed with Apple's Product Security PGP key,
and details are available at:
https://www.apple.com/support/security/pgp/
-----BEGIN PGP SIGNATURE-----

iQIzBAEBCAAdFiEEBP+4DupqR5Sgt1DB4RjMIDkeNxkFAmNbKpgACgkQ4RjMIDke
NxkmrA//QkiOI5QLiYQv5mGLd0ATWIuBRLVgzxTZY1iguC1IUlDXExGXPd9FeS/n
M7kFNZ/tp1i/XgHogq6d+kyBxZSlM+Jp2TfTBr4H/3I3xzFSx4fwEqqmBYiG8XSR
DXWKJCcbmYLdQGgHUcKHTMtSWsjRWJjIm88+lJMGdeQGo6NzqcsCKs0Tprf85Noq
nr0YTzPAUURmZtrivSLXtpek7S4E1MhzJZZ4IXjI7FiHHzFg7KnlBkESrAamLHgz
ephVZA7BsRDZtb5fh10+t7Ky42SIuy5TMd9UU4viNxd/mn6NP2N4shd95ywcrR5/
o6ywAHQxnkL3apOi0BVcwyR9PzrOxkzhZj74iEwgGu/hci1HvwHHPFUkErPqRO1f
m1MAz3Q3E+0cXTmjnxZzmrqFgXRauyLaxXNyCMlQVNPw/YBKQLHiaZnbBmt00k0j
f++ahogNR07V9LfcZ4YZnK3P5jN20/KNUhtouT/V9mS66lbWz+oQdiRJCVHuW2Ur
UkNbgc6mBFq81t3vhWrJlv158OLogWykFzTdPUbJvJw61AKXO/BxNZjv53XL1+D1
2NqnribpyIluIZxwYIo5HVYEMKYLObhcZJDVFXR2gue9hgwEENtiY7SpwOwo+GvE
kFAs/FBoLs6cCxATcYCxxuhXG7MYzkjNLPCexskSY7zncFiTHyM=
=Fcqo
-----END PGP SIGNATURE-----

_______________________________________________
Sent through the Full Disclosure mailing list
https://nmap.org/mailman/listinfo/fulldisclosure
Web Archives & RSS: https://seclists.org/fulldisclosure/
```

---

[![Previous](/images/left-icon-16x16.png)](41)
[By Date](date.html#42)
[![Next](/images/right-icon-16x16.png)](43)

[![Previous](/images/left-icon-16x16.png)](41)
[By Thread](index.html#42)
[![Next](/images/right-icon-16x16.png)](43)

### Current thread:

* **APPLE-SA-2022-10-27-6 Additional information for APPLE-SA-2022-10-24-3 macOS Monterey 12.6.1** *Apple Product Security via Fulldisclosure (Oct 30)*

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