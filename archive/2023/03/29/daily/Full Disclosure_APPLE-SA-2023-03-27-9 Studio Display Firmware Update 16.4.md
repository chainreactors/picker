---
title: APPLE-SA-2023-03-27-9 Studio Display Firmware Update 16.4
url: https://seclists.org/fulldisclosure/2023/Mar/24
source: Full Disclosure
date: 2023-03-29
fetch_date: 2025-10-04T11:03:20.581860
---

# APPLE-SA-2023-03-27-9 Studio Display Firmware Update 16.4

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

# APPLE-SA-2023-03-27-9 Studio Display Firmware Update 16.4

---

*From*: Apple Product Security via Fulldisclosure <fulldisclosure () seclists org>
*Date*: Mon, 27 Mar 2023 16:08:51 -0700

---

```
-----BEGIN PGP SIGNED MESSAGE-----
Hash: SHA256

APPLE-SA-2023-03-27-9 Studio Display Firmware Update 16.4

Studio Display Firmware Update 16.4 addresses the following issues.
Information about the security content is also available at
https://support.apple.com/HT213672.

Display
Available for: macOS Ventura 13.3 and later
Impact: An app may be able to execute arbitrary code with kernel
privileges
Description: A memory corruption issue was addressed with improved
state management.
CVE-2023-27965: Proteas of Pangu Lab

For more information about Studio Display Firmware updates,
please visit https://support.apple.com/HT213110.

All information is also posted on the Apple Security Updates
web site: https://support.apple.com/en-us/HT201222.

This message is signed with Apple's Product Security PGP key,
and details are available at:
https://www.apple.com/support/security/pgp/
-----BEGIN PGP SIGNATURE-----

iQIzBAEBCAAdFiEEBP+4DupqR5Sgt1DB4RjMIDkeNxkFAmQiIZwACgkQ4RjMIDke
Nxm/gg//WKOK5VTFA9xuq5Mg5TsMin22eCVxfJgh7Lafn/bOpi1zq5BI+j9t8itb
KkTu5V/iiiZG2jV6Sr2e3CC8WSilgjexoREoMpRkED74DgGr4HoWYA9EVxrdCMoT
2OF3ehSUKKWAOAKxB54C5STGXEDHoI6sx7wuMdDCJUnqDMOoVWlJnKaV6/AtAm8J
i731JzRLlaRdGSoMltfwfK+f8co1PWwZ2wK+ktNfJQYaQAc0dmED1/y28EOcxk3c
//qxiE/fkBr4BH5LOjf5VQ2B2rOoLWjiQTILbJwfYZLhBnCK6pUJgFk3490mbq4J
6sNoiAhzI6A4F8hFmfdOhYPzTWNqKuK5al/SoxyDrNqImrjZkrgCY/0aUPpm5BZy
Zge6KrS5Gkgezcwt5bI8BMuGSekZGmm32zO0lWOnVYpO8oWOkLTN5zcToMi+eort
h11UQGQtO0u+lSCxwmx6IAuStxGlMka7Jo+tTymMp4x85xkZ/y5d67TJVg41/tOd
sp66adZTY0vDzeVsXjFxKnLqc7QSdmWa7t5OkQyhBAj7SvJPNaHq5AT+O5GBYzgc
AklpeBbinVwepmGLBslXhgrRp6cPu1w7GsCZVR7mmFzwBASfWn9OtjXPeEiOONAd
Ix3/e6ZqU/n/K5JwmcA4r3RgzkZELzApKKhphicB/u+vlaVnmg4=
=M4UX
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

* **APPLE-SA-2023-03-27-9 Studio Display Firmware Update 16.4** *Apple Product Security via Fulldisclosure (Mar 27)*

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