---
title: APPLE-SA-2022-12-13-5 macOS Monterey 12.6.2
url: https://seclists.org/fulldisclosure/2022/Dec/24
source: Full Disclosure
date: 2022-12-22
fetch_date: 2025-10-04T02:15:06.525498
---

# APPLE-SA-2022-12-13-5 macOS Monterey 12.6.2

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

[![Previous](/images/left-icon-16x16.png)](23)
[By Date](date.html#24)
[![Next](/images/right-icon-16x16.png)](25)

[![Previous](/images/left-icon-16x16.png)](23)
[By Thread](index.html#24)
[![Next](/images/right-icon-16x16.png)](25)

![](/shared/images/nst-icons.svg#search)

# APPLE-SA-2022-12-13-5 macOS Monterey 12.6.2

---

*From*: Apple Product Security via Fulldisclosure <fulldisclosure () seclists org>
*Date*: Tue, 13 Dec 2022 16:34:58 -0800

---

```
-----BEGIN PGP SIGNED MESSAGE-----
Hash: SHA256

APPLE-SA-2022-12-13-5 macOS Monterey 12.6.2

macOS Monterey 12.6.2 addresses the following issues.
Information about the security content is also available at
https://support.apple.com/HT213533.

Bluetooth
Available for: macOS Monterey
Impact: An app may be able to disclose kernel memory
Description: The issue was addressed with improved memory handling.
CVE-2022-42854: Pan ZhenPeng (@Peterpan0927) of STAR Labs SG Pte.
Ltd. (@starlabs_sg)

BOM
Available for: macOS Monterey
Impact: An app may bypass Gatekeeper checks
Description: A logic issue was addressed with improved checks.
CVE-2022-42821: Jonathan Bar Or of Microsoft

DriverKit
Available for: macOS Monterey
Impact: An app may be able to execute arbitrary code with kernel
privileges
Description: The issue was addressed with improved memory handling.
CVE-2022-32942: Linus Henze of Pinauten GmbH (pinauten.de)

File System
Available for: macOS Monterey
Impact: An app may be able to break out of its sandbox
Description: This issue was addressed with improved checks.
CVE-2022-42861: pattern-f (@pattern_F_) of Ant Security Light-Year
Lab

IOHIDFamily
Available for: macOS Monterey
Impact: An app may be able to execute arbitrary code with kernel
privileges
Description: A race condition was addressed with improved state
handling.
CVE-2022-42864: Tommy Muir (@Muirey03)

Kernel
Available for: macOS Monterey
Impact: An app may be able to execute arbitrary code with kernel
privileges
Description: A race condition was addressed with additional
validation.
CVE-2022-46689: Ian Beer of Google Project Zero

Kernel
Available for: macOS Monterey
Impact: An app with root privileges may be able to execute arbitrary
code with kernel privileges
Description: The issue was addressed with improved memory handling.
CVE-2022-42845: Adam DoupÃ© of ASU SEFCOM

Kernel
Available for: macOS Monterey
Impact: A remote user may be able to cause kernel code execution
Description: The issue was addressed with improved memory handling.
CVE-2022-42842: pattern-f (@pattern_F_) of Ant Security Light-Year
Lab

libxml2
Available for: macOS Monterey
Impact: A remote user may be able to cause unexpected app termination
or arbitrary code execution
Description: An integer overflow was addressed through improved input
validation.
CVE-2022-40303: Maddie Stone of Google Project Zero

libxml2
Available for: macOS Monterey
Impact: A remote user may be able to cause unexpected app termination
or arbitrary code execution
Description: This issue was addressed with improved checks.
CVE-2022-40304: Ned Williamson and Nathan Wachholz of Google Project
Zero

ppp
Available for: macOS Monterey
Impact: An app may be able to execute arbitrary code with kernel
privileges
Description: The issue was addressed with improved memory handling.
CVE-2022-42840: an anonymous researcher

Preferences
Available for: macOS Monterey
Impact: An app may be able to use arbitrary entitlements
Description: A logic issue was addressed with improved state
management.
CVE-2022-42855: Ivan Fratric of Google Project Zero

xar
Available for: macOS Monterey
Impact: Processing a maliciously crafted package may lead to
arbitrary code execution
Description: A type confusion issue was addressed with improved
checks.
CVE-2022-42841: Thijs Alkemade (@xnyhps) of Computest Sector 7

macOS Monterey 12.6.2 may be obtained from the Mac App Store or
Apple's Software Downloads web site:
https://support.apple.com/downloads/
All information is also posted on the Apple Security Updates
web site: https://support.apple.com/en-us/HT201222.

This message is signed with Apple's Product Security PGP key,
and details are available at:
https://www.apple.com/support/security/pgp/
-----BEGIN PGP SIGNATURE-----

iQIzBAEBCAAdFiEEBP+4DupqR5Sgt1DB4RjMIDkeNxkFAmOZFX8ACgkQ4RjMIDke
NxmuDw/7B+dpr+R5V7L8iLPTeaWmYdo95V9eKbSoUaNMWy+zqAMTpjpybr8t04KE
SlKg1LGUBtE0Yu+Hk8XH5w9cp9EmthJlViaQj/ARhQnaJAb6d4c7fVE/b70aFlB2
LyGSwW7J2U7jJVT/DLNJRLPy57hql9hCONY0qZzGvF7cogjeyy3CKQx6JQoRcxP+
BkwSgXX1BxscWkjtQkNnDEDJYWj04MxmTj+EVeoOmkDlXcSypYCBEAKz7474Hnql
/lZYe8a+SupwOrXnJUusobAK8fUDN7tfmrr5Zg6F7mBGe6BDNX7E6BZ3hb8NH/sz
w0BBUU4aLCAVFbgllNLGQqsWif4/julEaSneEtStrJDgNWaXbrhrTWAYzMfJIGoF
nGWYmWUY8YR53zeC1egMvHoHnLFzIXGOWmKdWhahSMygHb1R5i8wdCcv+M1iL3BB
pthnd3XnZiOcEo4Z2XazFJV2YQ6juDPcXFgS0fBsNBS7LvMKBia/ax3CGwAxEagM
yLOgcgIIbdg6DM72siMOpfScB7EPcFIBb1H6IHBZMhRg0NRKMTB9tNE0rgQ+OYUN
Ze1wkPo8FH1lCunDcSZ1v6JzGZRN/o3woaR3LHVYEPWe3zJY2YvaqRrD/QfjqsMm
5o/94MyoeFn0WM6lXhqlBZvn8HtYDmFNu4VFt6ZjiL13CohaL2U=
=U7h6
-----END PGP SIGNATURE-----

_______________________________________________
Sent through the Full Disclosure mailing list
https://nmap.org/mailman/listinfo/fulldisclosure
Web Archives & RSS: https://seclists.org/fulldisclosure/
```

---

[![Previous](/images/left-icon-16x16.png)](23)
[By Date](date.html#24)
[![Next](/images/right-icon-16x16.png)](25)

[![Previous](/images/left-icon-16x16.png)](23)
[By Thread](index.html#24)
[![Next](/images/right-icon-16x16.png)](25)

### Current thread:

* **APPLE-SA-2022-12-13-5 macOS Monterey 12.6.2** *Apple Product Security via Fulldisclosure (Dec 20)*

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