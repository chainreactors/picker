---
title: APPLE-SA-12-11-2024-9 Safari 18.2
url: https://seclists.org/fulldisclosure/2024/Dec/13
source: Full Disclosure
date: 2024-12-13
fetch_date: 2025-10-06T19:40:19.386086
---

# APPLE-SA-12-11-2024-9 Safari 18.2

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

# APPLE-SA-12-11-2024-9 Safari 18.2

---

*From*: Apple Product Security via Fulldisclosure <fulldisclosure () seclists org>
*Date*: Wed, 11 Dec 2024 16:41:02 -0700

---

```
-----BEGIN PGP SIGNED MESSAGE-----
Hash: SHA256

APPLE-SA-12-11-2024-9 Safari 18.2

Safari 18.2 addresses the following issues.
Information about the security content is also available at
https://support.apple.com/121846.

Apple maintains a Security Releases page at
https://support.apple.com/100100 which lists recent
software updates with security advisories.

Safari
Available for: macOS Ventura and macOS Sonoma
Impact: On a device with Private Relay enabled, adding a website to the
Safari Reading List may reveal the originating IP address to the website
Description: The issue was addressed with improved routing of Safari-
originated requests.
CVE-2024-44246: Jacob Braun

WebKit
Available for: macOS Ventura and macOS Sonoma
Impact: Processing maliciously crafted web content may lead to an
unexpected process crash
Description: The issue was addressed with improved checks.
WebKit Bugzilla: 278497
CVE-2024-54479: Seunghyun Lee
WebKit Bugzilla: 281912
CVE-2024-54502: Brendon Tiszka of Google Project Zero

WebKit
Available for: macOS Ventura and macOS Sonoma
Impact: Processing maliciously crafted web content may lead to an
unexpected process crash
Description: The issue was addressed with improved memory handling.
WebKit Bugzilla: 282180
CVE-2024-54508: linjy of HKUS3Lab and chluo of WHUSecLab, Xiangwei Zhang
of Tencent Security YUNDING LAB

WebKit
Available for: macOS Ventura and macOS Sonoma
Impact: Processing maliciously crafted web content may lead to memory
corruption
Description: A type confusion issue was addressed with improved memory
handling.
WebKit Bugzilla: 282661
CVE-2024-54505: Gary Kwong

WebKit
Available for: macOS Ventura and macOS Sonoma
Impact: Processing maliciously crafted web content may lead to memory
corruption
Description: The issue was addressed with improved memory handling.
WebKit Bugzilla: 277967
CVE-2024-54534: Tashita Software Security

Additional recognition

Safari
We would like to acknowledge Jaydev Ahire for their assistance.

WebKit
We would like to acknowledge Hafiizh for their assistance.

Safari 18.2 may be obtained from the Mac App Store.

All information is also posted on the Apple Security Releases
web site: https://support.apple.com/100100.

This message is signed with Apple's Product Security PGP key,
and details are available at:
https://www.apple.com/support/security/pgp/

-----BEGIN PGP SIGNATURE-----

iQIzBAEBCAAdFiEEsz9altA7uTI+rE/qX+5d1TXaIvoFAmdaCisACgkQX+5d1TXa
IvpmaQ/+OPSH0RBZvHFbjuWyMO9Lpl6Zm2tb714ZDP0aPkvo+ONGhUo6vIGv+aDr
k0CvPw3PMLNWM/6t1s2rAasokmsOJCrm+OnxuYnLXmDQqG2noWw2wH4xWe7hcoJo
gH6/tWeT1vB0JCIDIz0jGwlvKLNBkZKsWn8/GwOyx0hCX5SIVkjrd7+TXM5liaYQ
hjdSCrXp5gTzGorXkcbOVeobAMMMgnVSkJ5yUul9wFZ52f/4eY7q6oSXpRZT5ddD
VQmi3UvQlSaXyDhmFiZ0/POwk4uN0TpqaIXxeucH1gTaAV80sUNoBjgyaUIOPnOf
sYFz5oOt6QTF6H+wnT6LckLuUXZiozvqOdjaqDsD15AF3Kju6a/0Se2ojpFxSwze
o8lQ/3gniyTNHGEH1SghLKFdNUnXzF+lQVIn5YW8OqBeS6CHpkRZbak3tajyG+NJ
+4tCj840uYP8KpmD8mZq5SzQHif2Io9SAyZ+i7Y9EXTjWLoZsEY77sDC/FEvhK44
2anshc7Q1b6FvQpUUQBA32mlhyDNl2uWhcrOKRBOrSZKykXAxi0ptcSg7xxsHq48
yVT/+hJIr4XQgdeq2oGUThZJk8JcJfTpH0HnN4t+yi+3cygpl1DCEQKlIK+l+EQ5
uGT54Nt36yS9GtSbvpaCGGQWiibfKP9d0R3xH9xbWqFpeUm311w=
=9HgJ
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

* **APPLE-SA-12-11-2024-9 Safari 18.2** *Apple Product Security via Fulldisclosure (Dec 12)*

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