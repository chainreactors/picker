---
title: APPLE-SA-2023-07-10-1 Safari 16.5.2
url: https://seclists.org/fulldisclosure/2023/Jul/19
source: Full Disclosure
date: 2023-07-12
fetch_date: 2025-10-04T11:56:50.399592
---

# APPLE-SA-2023-07-10-1 Safari 16.5.2

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

[![Previous](/images/left-icon-16x16.png)](18)
[By Date](date.html#19)
[![Next](/images/right-icon-16x16.png)](20)

[![Previous](/images/left-icon-16x16.png)](18)
[By Thread](index.html#19)
[![Next](/images/right-icon-16x16.png)](20)

![](/shared/images/nst-icons.svg#search)

# APPLE-SA-2023-07-10-1 Safari 16.5.2

---

*From*: Apple Product Security via Fulldisclosure <fulldisclosure () seclists org>
*Date*: Mon, 10 Jul 2023 15:50:04 -0700

---

```
-----BEGIN PGP SIGNED MESSAGE-----
Hash: SHA256

APPLE-SA-2023-07-10-1 Safari 16.5.2

Safari 16.5.2 addresses the following issues.
Information about the security content is also available at
https://support.apple.com/kb/HT213826.

Apple maintains a Security Updates page at
https://support.apple.com/HT201222 which lists recent
software updates with security advisories.

WebKit
Available for: macOS Big Sur and macOS Monterey
Impact: Processing web content may lead to arbitrary code execution.
Apple is aware of a report that this issue may have been actively
exploited.
Description: The issue was addressed with improved checks.
CVE-2023-37450: an anonymous researcher

All information is also posted on the Apple Security Updates
web site: https://support.apple.com/en-us/HT201222.

This message is signed with Apple's Product Security PGP key,
and details are available at:
https://www.apple.com/support/security/pgp/
-----BEGIN PGP SIGNATURE-----

iQIzBAEBCAAdFiEEBP+4DupqR5Sgt1DB4RjMIDkeNxkFAmSsimYACgkQ4RjMIDke
NxktKw//XTdOMjrL6+jeIBhiSBRp49DGZhSov0uPboSFrDz1Do6A/Ylg+WEHRRJP
wrmlqbAtyziNvMK64FX9mqTjR7nXJRG+Nhp21AlkvM931y47cb+eF2sPddqgJAWs
HYI9PR2ilLALHYdjsCczcqAjoUtE5qU+B8CGngWnvHF8AM29ayonKPh1CJtiAYlU
ELhyYHpV26RbhIdIN7DVd3Cpw8WfwTxQIhkDCea72s16L6uflhREyUI2tucyy5cB
p1nImy1Q8k14tusmgePU7f9nj8hwaxx3duXAyTJRuTdu3rTqhtdlBrhk58H0hKk7
4p3TQcQGg4O5Nr39OJeO40LnHp1yhO3AgtilWchhC9vsKgaoavkGBF5HjGEA3IXN
aHvrI6g5imR+6kk2Dfdg4WNux/OUHMG/vL50UsAxdXue4UVO7CIBeBE40cYmNQfH
nG5stDH0Ozq1yeYedwuDvnJF4h+3v1CJWUqRRNcjSi8FhuvxZRKKydEulVfg1iEh
wMZcloRrxb0BTwqT2w1hYxgX07I62veM5XK2f99gJfMaUknJ6z3Y2eig4yBOvK4e
7Xm22to/qa5PXIiNd47JM6gpcTxVYmtlb/qfr8PR21M+6fWNFsu/JcLJ/v7pWYqR
csyNF9fWPdhtHXPzNHpzrkBbp3qgO4funU5gSxZKIT3fLLIulaQ=
=XKqq
-----END PGP SIGNATURE-----

_______________________________________________
Sent through the Full Disclosure mailing list
https://nmap.org/mailman/listinfo/fulldisclosure
Web Archives & RSS: https://seclists.org/fulldisclosure/
```

---

[![Previous](/images/left-icon-16x16.png)](18)
[By Date](date.html#19)
[![Next](/images/right-icon-16x16.png)](20)

[![Previous](/images/left-icon-16x16.png)](18)
[By Thread](index.html#19)
[![Next](/images/right-icon-16x16.png)](20)

### Current thread:

* **APPLE-SA-2023-07-10-1 Safari 16.5.2** *Apple Product Security via Fulldisclosure (Jul 11)*

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