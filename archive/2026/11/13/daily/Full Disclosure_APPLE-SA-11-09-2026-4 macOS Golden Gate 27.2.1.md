---
title: APPLE-SA-11-09-2026-4 macOS Golden Gate 27.2.1
url: https://seclists.org/fulldisclosure/2026/Nov/27
source: Full Disclosure
date: 2026-11-13
fetch_date: 2026-11-14T08:21:48.235208
---

# APPLE-SA-11-09-2026-4 macOS Golden Gate 27.2.1

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

[![Previous](/images/left-icon-16x16.png)](26)
[By Date](date.html#27)
[![Next](/images/right-icon-16x16.png)](28)

[![Previous](/images/left-icon-16x16.png)](26)
[By Thread](index.html#27)
[![Next](/images/right-icon-16x16.png)](28)

![](/shared/images/nst-icons.svg#search)

# APPLE-SA-11-09-2026-4 macOS Golden Gate 27.2.1

---

*From*: Apple Product Security via Fulldisclosure <fulldisclosure () seclists org>
*Date*: Mon, 09 Nov 2026 16:05:59 -0800

---

```
-----BEGIN PGP SIGNED MESSAGE-----
Hash: SHA256

APPLE-SA-11-09-2026-4 macOS Golden Gate 27.2.1

macOS Golden Gate 27.2.1 addresses the following issues.
Information about the security content is also available at
https://support.apple.com/149718.

Apple maintains a Security Releases page at
https://support.apple.com/100100 which lists recent
software updates with security advisories.

AirPlay
Available for: macOS Golden Gate
Impact: An attacker in Bluetooth range may be able to bypass the rate
limit on pairing code attempts
Description: A logic issue was addressed with improved state management.
CVE-2026-113968: Apple

Bluetooth
Available for: macOS Golden Gate
Impact: An attacker in Bluetooth range may be able to corrupt process
memory
Description: A use-after-free issue was addressed with improved memory
management.
CVE-2026-113970: Apple

brotli
Available for: macOS Golden Gate
Impact: Processing maliciously crafted input may lead to memory
corruption
Description: An out-of-bounds write issue was addressed with improved
input validation.
CVE-2026-111497

CoreUtils
Available for: macOS Golden Gate
Impact: A malicious Bluetooth device may be able to establish a pairing
without user interaction
Description: This issue was addressed with improved checks.
CVE-2026-113965: Apple

CoreUtils
Available for: macOS Golden Gate
Impact: An attacker in Bluetooth range may be able to bypass the rate
limit on pairing code attempts and pair with a device without user
interaction
Description: A logic issue was addressed with improved state management.
CVE-2026-113964: an anonymous researcher

Messages
Available for: macOS Golden Gate
Impact: A remote attacker may be able to join an iMessage group chat and
receive its messages
Description: An authorization issue was addressed with improved
validation.
CVE-2026-113961: an anonymous researcher

Messages
Available for: macOS Golden Gate
Impact: A user added to an iMessage group may be able to access messages
sent before they joined
Description: This issue was addressed by removing the vulnerable code.
CVE-2026-113960: an anonymous researcher

rapportd
Available for: macOS Golden Gate
Impact: An attacker on the same network may be able to bypass the rate
limit on AirPlay pairing code attempts
Description: A logic issue was addressed with improved state management.
CVE-2026-113969: Apple

macOS Golden Gate 27.2.1 may be obtained from the Mac App Store or
Apple's Software Downloads web site:
https://support.apple.com/downloads/

All information is also posted on the Apple Security Releases
web site: https://support.apple.com/100100.

This message is signed with Apple's Product Security PGP key,
and details are available at:
https://www.apple.com/support/security/pgp/

-----BEGIN PGP SIGNATURE-----

iQIzBAEBCAAdFiEEhjkl+zMLNwFiCT1o4Ifiq8DH7PUFAmryPE0ACgkQ4Ifiq8DH
7PUfWQ//arO0XEabYP1WhWDP4RETeF8Tr+A5rl7R16tiW2wXAryeD5AB8VT7OYR+
Uz7SDCxqDfndYYeVOQnW5zHgrQhshkbSHtxRVIhBviRaWVP4kzGBuCTzDu9xhvQv
V/Lv8XavAEgjW51/xeYpsUpnAn3YUoH3iuoHZAqmQtus9I6soqVfA+h1POGCW1zE
REp0mZm3Qtl6Zzv+XGCp9yyV161NwKzd+WYTwKWnPDrZ6mUQYuVeuwRF1WREcHXC
rZGja6d3yy3wsMvX9kYIi4M9ekPxkQ+73wbvc4ErtNmLjDDR/oyKMZ5lewCyy4vL
yuzxrgFDhqi6SgGISzsLTqCshr5boW7zEVhWdpU7hhT+bRr8q7hN96kSH1w8yGkF
T//Zbm+K7bSuUUQ1xQYU1P1zPWHQ3Nf51q48XqbDTYk4k3BO3rL087+t4UtgFJwu
NeMzWlI6mYS1I5gAgSKrUyMLbqJq+B+s7anqBh0A2mfQqVy1df++2PlgsrfJFpMF
ymjTAM+FWHmdIE30SWhlKnChJpE+oliB42ViSdJDrAmvBkkz/OjRRUlm5SQtcgAF
2QLeUM4CIxL7ehP6cgvzbMU/+kkV8TQJ8KDrKxEbpenhR5/wc8VNJ1bI6LeBpUSP
3TewAxE0R8RG/uVJgtcEaC2aiXg+oHC5T45ux8lWVKoQtik1Pnc=
=0wqb
-----END PGP SIGNATURE-----

_______________________________________________
Sent through the Full Disclosure mailing list
https://nmap.org/mailman/listinfo/fulldisclosure
Web Archives & RSS: https://seclists.org/fulldisclosure/
```

---

[![Previous](/images/left-icon-16x16.png)](26)
[By Date](date.html#27)
[![Next](/images/right-icon-16x16.png)](28)

[![Previous](/images/left-icon-16x16.png)](26)
[By Thread](index.html#27)
[![Next](/images/right-icon-16x16.png)](28)

### Current thread:

* **APPLE-SA-11-09-2026-4 macOS Golden Gate 27.2.1** *Apple Product Security via Fulldisclosure (Nov 12)*

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