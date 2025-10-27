---
title: APPLE-SA-2022-10-27-8 Additional information for APPLE-SA-2022-10-24-4 macOS Big Sur 11.7.1
url: https://seclists.org/fulldisclosure/2022/Oct/44
source: Full Disclosure
date: 2022-10-31
fetch_date: 2025-10-03T21:22:00.772619
---

# APPLE-SA-2022-10-27-8 Additional information for APPLE-SA-2022-10-24-4 macOS Big Sur 11.7.1

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

[![Previous](/images/left-icon-16x16.png)](43)
[By Date](date.html#44)
[![Next](/images/right-icon-16x16.png)](45)

[![Previous](/images/left-icon-16x16.png)](43)
[By Thread](index.html#44)
[![Next](/images/right-icon-16x16.png)](45)

![](/shared/images/nst-icons.svg#search)

# APPLE-SA-2022-10-27-8 Additional information for APPLE-SA-2022-10-24-4 macOS Big Sur 11.7.1

---

*From*: Apple Product Security via Fulldisclosure <fulldisclosure () seclists org>
*Date*: Thu, 27 Oct 2022 18:23:40 -0700

---

```
-----BEGIN PGP SIGNED MESSAGE-----
Hash: SHA256

APPLE-SA-2022-10-27-8 Additional information for APPLE-SA-2022-10-24-4 macOS Big Sur 11.7.1

macOS Big Sur 11.7.1 addresses the following issues.
Information about the security content is also available at
https://support.apple.com/HT213493.

AppleMobileFileIntegrity
Available for: macOS Big Sur
Impact: An app may be able to modify protected parts of the file
system
Description: This issue was addressed by removing additional
entitlements.
CVE-2022-42825: Mickey Jin (@patch1t)

Audio
Available for: macOS Big Sur
Impact: Parsing a maliciously crafted audio file may lead to
disclosure of user information
Description: The issue was addressed with improved memory handling.
CVE-2022-42798: Anonymous working with Trend Micro Zero Day
Initiative
Entry added October 27, 2022

Kernel
Available for: macOS Big Sur
Impact: An app may be able to execute arbitrary code with kernel
privileges
Description: A memory corruption issue was addressed with improved
state management.
CVE-2022-32944: Tim Michaud (@TimGMichaud) of Moveworks.ai
Entry added October 27, 2022

ppp
Available for: macOS Big Sur
Impact: A buffer overflow may result in arbitrary code execution
Description: The issue was addressed with improved bounds checks.
CVE-2022-32941: an anonymous researcher
Entry added October 27, 2022

Ruby
Available for: macOS Big Sur
Impact: A remote user may be able to cause unexpected app termination
or arbitrary code execution
Description: A memory corruption issue was addressed by updating Ruby
to version 2.6.10.
CVE-2022-28739

Sandbox
Available for: macOS Big Sur
Impact: An app with root privileges may be able to access private
information
Description: This issue was addressed with improved data protection.
CVE-2022-32862: an anonymous researcher

zlib
Available for: macOS Big Sur
Impact: A user may be able to cause unexpected app termination or
arbitrary code execution
Description: This issue was addressed with improved checks.
CVE-2022-37434: Evgeny Legerov
CVE-2022-42800: Evgeny Legerov
Entry added October 27, 2022

macOS Big Sur 11.7.1 may be obtained from the Mac App Store or
Apple's Software Downloads web site:
https://support.apple.com/downloads/
All information is also posted on the Apple Security Updates
web site: https://support.apple.com/en-us/HT201222.

This message is signed with Apple's Product Security PGP key,
and details are available at:
https://www.apple.com/support/security/pgp/
-----BEGIN PGP SIGNATURE-----

iQIzBAEBCAAdFiEEBP+4DupqR5Sgt1DB4RjMIDkeNxkFAmNbKpcACgkQ4RjMIDke
Nxm0fxAA1SrPLykU4CHK4xqNKClIMeYiTBEmS55x9GD/n79iH4VDOyeq+Z/Id0u/
AJab2VTWkMfd8FJv1l4VK/mH2gkmfbEOww0oCsoUoX2GNKXbHR7ob01i8oHYZRVU
ehECiEME262zsmxb5q7qf/debKbnTPimtZ9QKGeHbQX6oKziWQHXov44eDfOQLY/
n8A2Qh49eQO8qsGTAIUBJ9gAeUSU5PzGpys47FRf4+HE7j39VvDPknkvngR4KtWY
61Wd7H8yhnUSkXr0lxMEl/xl5fIUAupIE1R1a2cdFXEMQLIaCO5KCZahCIm2y2Mi
hzhHuhYTbKJEmCyvnwhcrw5kj4vVRbuTYFXnu1hUB5WWvQrIH//KDqtzcObT+IxK
XC8okr1aw9w0whny/Xjo+6ahD8o3kvNyU2bbkcAryvhVICXRNNXaylkRB6Ffrprz
766HoJ2OOhdT0XS2ETNNqPiG5v4PmsrgzHfH/drT0LEx+N8ju8NC9moNYHnVxtnE
S8ZTqXgJnlexdnsXPOOkj/bMZDY3mrqGsGrNX6VQ7o1C6n6zyQ9uCLccn16csFkM
jG2fNgFAeLQM/AabfxDgdJSJYoaXhGgu+Dt0aCQ9EUEGDLJrU+ii9dUsrTA2W0ME
XxDWQI+NWYfiZkmIJzPtROlMVcqWHd4I0Xo8HpTpZh+h0xlsANw=
=rV2j
-----END PGP SIGNATURE-----

_______________________________________________
Sent through the Full Disclosure mailing list
https://nmap.org/mailman/listinfo/fulldisclosure
Web Archives & RSS: https://seclists.org/fulldisclosure/
```

---

[![Previous](/images/left-icon-16x16.png)](43)
[By Date](date.html#44)
[![Next](/images/right-icon-16x16.png)](45)

[![Previous](/images/left-icon-16x16.png)](43)
[By Thread](index.html#44)
[![Next](/images/right-icon-16x16.png)](45)

### Current thread:

* **APPLE-SA-2022-10-27-8 Additional information for APPLE-SA-2022-10-24-4 macOS Big Sur 11.7.1** *Apple Product Security via Fulldisclosure (Oct 30)*

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