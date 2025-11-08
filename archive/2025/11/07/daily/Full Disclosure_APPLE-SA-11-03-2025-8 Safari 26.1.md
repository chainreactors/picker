---
title: APPLE-SA-11-03-2025-8 Safari 26.1
url: https://seclists.org/fulldisclosure/2025/Nov/9
source: Full Disclosure
date: 2025-11-07
fetch_date: 2025-11-08T03:06:37.668622
---

# APPLE-SA-11-03-2025-8 Safari 26.1

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

[![Previous](/images/left-icon-16x16.png)](8)
[By Date](date.html#9)
[![Next](/images/right-icon-16x16.png)](10)

[![Previous](/images/left-icon-16x16.png)](8)
[By Thread](index.html#9)
[![Next](/images/right-icon-16x16.png)](10)

![](/shared/images/nst-icons.svg#search)

# APPLE-SA-11-03-2025-8 Safari 26.1

---

*From*: Apple Product Security via Fulldisclosure <fulldisclosure () seclists org>
*Date*: Mon, 03 Nov 2025 17:35:13 -0800

---

```
-----BEGIN PGP SIGNED MESSAGE-----
Hash: SHA256

APPLE-SA-11-03-2025-8 Safari 26.1

Safari 26.1 addresses the following issues.
Information about the security content is also available at
https://support.apple.com/125640.

Apple maintains a Security Releases page at
https://support.apple.com/100100 which lists recent
software updates with security advisories.

Safari
Available for: macOS Sonoma and macOS Sequoia
Impact: Visiting a malicious website may lead to address bar spoofing
Description: The issue was addressed with improved checks.
CVE-2025-43493: @RenwaX23

Safari
Available for: macOS Sonoma and macOS Sequoia
Impact: Visiting a malicious website may lead to user interface spoofing
Description: An inconsistent user interface issue was addressed with
improved state management.
CVE-2025-43503: @RenwaX23

Safari
Available for: macOS Sonoma and macOS Sequoia
Impact: An app may be able to bypass certain Privacy preferences
Description: A privacy issue was addressed by removing sensitive data.
CVE-2025-43502: an anonymous researcher

WebKit
Available for: macOS Sonoma and macOS Sequoia
Impact: A malicious website may exfiltrate data cross-origin
Description: The issue was addressed with improved checks.
WebKit Bugzilla: 276208
CVE-2025-43480: Aleksejs Popovs

WebKit
Available for: macOS Sonoma and macOS Sequoia
Impact: Processing maliciously crafted web content may lead to an
unexpected process crash
Description: This issue was addressed through improved state management.
WebKit Bugzilla: 296693
CVE-2025-43458: Phil Beauvoir
WebKit Bugzilla: 298196
CVE-2025-43430: Google Big Sleep
WebKit Bugzilla: 298628
CVE-2025-43427: Gary Kwong, rheza (@ginggilBesel)

WebKit
Available for: macOS Sonoma and macOS Sequoia
Impact: Processing maliciously crafted web content may lead to an
unexpected process crash
Description: This issue was addressed with improved checks.
WebKit Bugzilla: 299843
CVE-2025-43443: an anonymous researcher

WebKit
Available for: macOS Sonoma and macOS Sequoia
Impact: Processing maliciously crafted web content may lead to an
unexpected process crash
Description: The issue was addressed with improved memory handling.
WebKit Bugzilla: 298496
CVE-2025-43441: rheza (@ginggilBesel)
WebKit Bugzilla: 299391
CVE-2025-43435: Justin Cohen of Google
WebKit Bugzilla: 298851
CVE-2025-43425: an anonymous researcher

WebKit
Available for: macOS Sonoma and macOS Sequoia
Impact: Processing maliciously crafted web content may lead to an
unexpected process crash
Description: This issue was addressed with improved checks
WebKit Bugzilla: 298126
CVE-2025-43440: Nan Wang (@eternalsakura13)

WebKit
Available for: macOS Sonoma and macOS Sequoia
Impact: Processing maliciously crafted web content may lead to an
unexpected Safari crash
Description: A use-after-free issue was addressed with improved memory
management.
WebKit Bugzilla: 297662
CVE-2025-43438: shandikri working with Trend Micro Zero Day Initiative
WebKit Bugzilla: 298606
CVE-2025-43457: Gary Kwong, Hossein Lotfi (@hosselot) of Trend Micro
Zero Day Initiative
WebKit Bugzilla: 297958
CVE-2025-43434: Google Big Sleep

WebKit
Available for: macOS Sonoma and macOS Sequoia
Impact: Processing maliciously crafted web content may lead to memory
corruption
Description: The issue was addressed with improved memory handling.
WebKit Bugzilla: 298093
CVE-2025-43433: Google Big Sleep
WebKit Bugzilla: 298194
CVE-2025-43431: Google Big Sleep

WebKit
Available for: macOS Sonoma and macOS Sequoia
Impact: Processing maliciously crafted web content may lead to an
unexpected process crash
Description: A use-after-free issue was addressed with improved memory
management.
WebKit Bugzilla: 299313
CVE-2025-43432: Hossein Lotfi (@hosselot) of Trend Micro Zero Day
Initiative

WebKit
Available for: macOS Sonoma and macOS Sequoia
Impact: Processing maliciously crafted web content may lead to an
unexpected process crash
Description: A buffer overflow was addressed with improved bounds
checking.
WebKit Bugzilla: 298232
CVE-2025-43429: Google Big Sleep

WebKit
Available for: macOS Sonoma and macOS Sequoia
Impact: Processing maliciously crafted web content may lead to an
unexpected process crash
Description: Multiple issues were addressed by disabling array
allocation sinking.
WebKit Bugzilla: 300718
CVE-2025-43421: Nan Wang (@eternalsakura13)

WebKit Canvas
Available for: macOS Sonoma and macOS Sequoia
Impact: A website may exfiltrate image data cross-origin
Description: The issue was addressed with improved handling of caches.
WebKit Bugzilla: 297566
CVE-2025-43392: Tom Van Goethem

Additional recognition

Safari
We would like to acknowledge Barath Stalin K for their assistance.

Safari Downloads
We would like to acknowledge Saello Puza for their assistance.

WebKit
We would like to acknowledge Enis Maholli (enismaholli.com), Google Big
Sleep for their assistance.

Safari 26.1 may be obtained from the Mac App Store.

All information is also posted on the Apple Security Releases
web site: https://support.apple.com/100100.

This message is signed with Apple's Product Security PGP key,
and details are available at:
https://www.apple.com/support/security/pgp/

-----BEGIN PGP SIGNATURE-----

iQIzBAEBCAAdFiEEhjkl+zMLNwFiCT1o4Ifiq8DH7PUFAmkJTeQACgkQ4Ifiq8DH
7PU7fw//TLFemkruZb9vOnhfvX3jmvIEwzvFE6RYXSn8i4eCHdZdl7weMBhWzeOS
NZ/zTDeqhOLebBDpwZHt0rlPE/mt+OHS9aLsyL89DYTalNkTXG5LXWSgsxDzQwg/
+Uzem1q6W7Yv8hWiAMAL4d6cy3Swt5TsZGtbMfGiALMG0E/R/EMNknBoFxHLp0AZ
IPlYNYN33aLqk7PCosiPurkyI3eAS7QHpx9WIfBjQMljGQyo7c4+M5pvzrWte0ck
t4yxbOMD9i+PiX6h6Qtq21H62AeP4n55cENkvwhU/VAdoHfa49g6MqzMpiJD3CT7
s28kSeHZ7rzsw1nJHMNPkV9TxLdPk+gBqeQm/njvdvWNhCjVoruX1Et8Z/jz6xTr
KPXi5e609mRXpauOLrjpY1gFOoC15UC/PYGF2E7peiChMvRGD8hA+wm+rFCE3aum
tzv1MxkBZVROsCk9YyWIRTEsGAQBqqU4wf5DMO5vUD9ltSLNT4yJP6ZM4WTE8OAE
jzb6O2TN8aSEDv26RISFnyVE3nDLLOmYNwi0nHtjO1y2ZLdVHSLS++axNn18wuvl
/uZM8NLNwcEsKAcRF2KMqcEfGO1XOAMiaFxkAoHdnxgWpT3AN02pUcQJsuflQlO0
aW/f0joWpxiHhw9cANB7nVcwbB1UdBa3pFw5NlG1bFd5aVvRa4M=
=91eP
-----END PGP SIGNATURE-----

_______________________________________________
Sent through the Full Disclosure mailing list
https://nmap.org/mailman/listinfo/fulldisclosure
Web Archives & RSS: https://seclists.org/fulldisclosure/
```

---

[![Previous](/images/left-icon-16x16.png)](8)
[By Date](date.html#9)
[![Next](/images/right-icon-16x16.png)](10)

[![Previous](/images/left-icon-16x16.png)](8)
[By Thread](index.html#9)
[![Next](/images/right-icon-16x16.png)](10)

### Current thread:

* **APPLE-SA-11-03-2025-8 Safari 26.1** *Apple Product Security via Fulldisclosure (Nov 07)*

![](/shared/images/nst-icons.svg#search)

## [Nmap Security Scanner](https://nmap.org/)

* [Ref Guide](https://nmap.org/book/man.html)* [Install Guide](https://nmap.org/book/install.html)* [Docs](https://nmap.org/docs.html)* [Download](https://nmap.org/download.html)* [Nmap OEM](https://nmap.org/oem/)

## [Npcap packet capture](https://npcap.com/)

* [User's Guide](https://npcap.com/guide/)* [API docs](https://npcap.com/guide/npcap-devguide.html#npcap-api)* [Download](https://npcap.com/#download)*...