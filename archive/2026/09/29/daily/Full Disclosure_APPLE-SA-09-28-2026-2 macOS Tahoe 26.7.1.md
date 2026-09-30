---
title: APPLE-SA-09-28-2026-2 macOS Tahoe 26.7.1
url: https://seclists.org/fulldisclosure/2026/Sep/90
source: Full Disclosure
date: 2026-09-29
fetch_date: 2026-09-30T07:43:05.561601
---

# APPLE-SA-09-28-2026-2 macOS Tahoe 26.7.1

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

[![Previous](/images/left-icon-16x16.png)](89)
[By Date](date.html#90)
[![Next](/images/right-icon-16x16.png)](91)

[![Previous](/images/left-icon-16x16.png)](89)
[By Thread](index.html#90)
[![Next](/images/right-icon-16x16.png)](91)

![](/shared/images/nst-icons.svg#search)

# APPLE-SA-09-28-2026-2 macOS Tahoe 26.7.1

---

*From*: Apple Product Security via Fulldisclosure <fulldisclosure () seclists org>
*Date*: Mon, 28 Sep 2026 15:13:29 -0700

---

```
-----BEGIN PGP SIGNED MESSAGE-----
Hash: SHA256

APPLE-SA-09-28-2026-2 macOS Tahoe 26.7.1

macOS Tahoe 26.7.1 addresses the following issues.
Information about the security content is also available at
https://support.apple.com/149228.

Apple maintains a Security Releases page at
https://support.apple.com/100100 which lists recent
software updates with security advisories.

CoreGraphics
Available for: macOS Tahoe
Impact: Processing a maliciously crafted file may lead to arbitrary code
execution. Apple is aware of a report that this issue may have been
exploited in an extremely sophisticated attack against specific targeted
individuals on versions of iOS before iOS 27.
Description: An out-of-bounds write issue was addressed with improved
bounds checking.
CVE-2026-86950: Meta Product Security

macOS Tahoe 26.7.1 may be obtained from the Mac App Store or
Apple's Software Downloads web site:
https://support.apple.com/downloads/

All information is also posted on the Apple Security Releases
web site: https://support.apple.com/100100.

This message is signed with Apple's Product Security PGP key,
and details are available at:
https://www.apple.com/support/security/pgp/

-----BEGIN PGP SIGNATURE-----

iQIzBAEBCAAdFiEEhjkl+zMLNwFiCT1o4Ifiq8DH7PUFAmq62tkACgkQ4Ifiq8DH
7PW9ehAArJ/eLh9DDNyANMqDrBPnJJAsv+nkLEU7mhFhMGwCxaRJJ5FidwZWLbqK
7ZtP4+7ggey1mb1MU/gkAVClkM2jGzizbQSfMqnnMmHWkHrIiHV16KTnXCUvxBiU
XbA0pPpLMtudscS7EumH9phCwMIDMdESSRC12OQcExqeZ2QCxkMZ8k8nvkpMA/SH
inRklHdBoTcCUMNw6c354mVO/GpeyCbjScwg35DTabqwgxlH7eDTjAlw+0zHcxpc
rHawS2lUvjVNIenl7/j4fQgYr1g6UPYiPB5xb31vncDmWcx/y5JFJUSgyQde0Q51
VOH58EplvBuAIY8/otFqYiTX0IsWMn5C7NVY5Yt+biRE7fLgPgTo8GblQi6KMEzt
dmUaCXV0/XuOXvJFr6jiCxkjmH3c+oTB63feSoX2tywUApLgIUSD9gYfA6Gu8TMy
IT20xrcf61ffcc+pstKI5MY2P2mI1YVpZ142aDe0n0M7x0lMLddcVfm4QAp+v4Lt
/Bpap7EFrAa3+r1k/L68c2Ui/c5sFyvjQI2Gg3x6NViHIOhlKSwvGytj8DL5YivJ
OsNT8PtvdmaFwLTo+41dy7+vTfP28OKwAlJFxDe+qWhylXfjPXSDni5HPUpc77mG
lzj/fuXRmIDT79u0uQYq+BhWdIbhHjH0f4xGl14ELrf66ZuRPtY=
=yI+o
-----END PGP SIGNATURE-----

_______________________________________________
Sent through the Full Disclosure mailing list
https://nmap.org/mailman/listinfo/fulldisclosure
Web Archives & RSS: https://seclists.org/fulldisclosure/
```

---

[![Previous](/images/left-icon-16x16.png)](89)
[By Date](date.html#90)
[![Next](/images/right-icon-16x16.png)](91)

[![Previous](/images/left-icon-16x16.png)](89)
[By Thread](index.html#90)
[![Next](/images/right-icon-16x16.png)](91)

### Current thread:

* **APPLE-SA-09-28-2026-2 macOS Tahoe 26.7.1** *Apple Product Security via Fulldisclosure (Sep 28)*

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