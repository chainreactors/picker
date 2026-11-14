---
title: APPLE-SA-11-09-2026-9 visionOS 27.2.1
url: https://seclists.org/fulldisclosure/2026/Nov/32
source: Full Disclosure
date: 2026-11-13
fetch_date: 2026-11-14T08:21:47.621814
---

# APPLE-SA-11-09-2026-9 visionOS 27.2.1

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

[![Previous](/images/left-icon-16x16.png)](31)
[By Date](date.html#32)
[![Next](/images/right-icon-16x16.png)](33)

[![Previous](/images/left-icon-16x16.png)](31)
[By Thread](index.html#32)
[![Next](/images/right-icon-16x16.png)](33)

![](/shared/images/nst-icons.svg#search)

# APPLE-SA-11-09-2026-9 visionOS 27.2.1

---

*From*: Apple Product Security via Fulldisclosure <fulldisclosure () seclists org>
*Date*: Mon, 09 Nov 2026 16:22:14 -0800

---

```
-----BEGIN PGP SIGNED MESSAGE-----
Hash: SHA256

APPLE-SA-11-09-2026-9 visionOS 27.2.1

visionOS 27.2.1 addresses the following issues.
Information about the security content is also available at
https://support.apple.com/149724.

Apple maintains a Security Releases page at
https://support.apple.com/100100 which lists recent
software updates with security advisories.

AirPlay
Available for: Apple Vision Pro (all models)
Impact: An attacker in Bluetooth range may be able to bypass the rate
limit on pairing code attempts
Description: A logic issue was addressed with improved state management.
CVE-2026-113968: Apple

App Intents
Available for: Apple Vision Pro (all models)
Impact: An app may be able to access sensitive user data
Description: An authorization issue was addressed with improved state
management.
CVE-2026-113963: László Várady

Bluetooth
Available for: Apple Vision Pro (all models)
Impact: An attacker in Bluetooth range may be able to corrupt process
memory
Description: A use-after-free issue was addressed with improved memory
management.
CVE-2026-113970: Apple

brotli
Available for: Apple Vision Pro (all models)
Impact: Processing maliciously crafted input may lead to memory
corruption
Description: An out-of-bounds write issue was addressed with improved
input validation.
CVE-2026-111497

CoreUtils
Available for: Apple Vision Pro (all models)
Impact: A malicious Bluetooth device may be able to establish a pairing
without user interaction
Description: This issue was addressed with improved checks.
CVE-2026-113965: Apple

CoreUtils
Available for: Apple Vision Pro (all models)
Impact: An attacker in Bluetooth range may be able to bypass the rate
limit on pairing code attempts and pair with a device without user
interaction
Description: A logic issue was addressed with improved state management.
CVE-2026-113964: an anonymous researcher

Messages
Available for: Apple Vision Pro (all models)
Impact: A remote attacker may be able to join an iMessage group chat and
receive its messages
Description: An authorization issue was addressed with improved
validation.
CVE-2026-113961: an anonymous researcher

Messages
Available for: Apple Vision Pro (all models)
Impact: A user added to an iMessage group may be able to access messages
sent before they joined
Description: This issue was addressed by removing the vulnerable code.
CVE-2026-113960: an anonymous researcher

rapportd
Available for: Apple Vision Pro (all models)
Impact: An attacker on the same network may be able to bypass the rate
limit on AirPlay pairing code attempts
Description: A logic issue was addressed with improved state management.
CVE-2026-113969: Apple

Instructions on how to update visionOS are available
at https://support.apple.com/kb/HT214009

To check the software version on your Apple Vision Pro,
open the Settings app and choose General > About.

All information is also posted on the Apple Security Releases
web site: https://support.apple.com/100100.

This message is signed with Apple's Product Security PGP key,
and details are available at:
https://www.apple.com/support/security/pgp/

-----BEGIN PGP SIGNATURE-----

iQIzBAEBCAAdFiEEhjkl+zMLNwFiCT1o4Ifiq8DH7PUFAmryPNsACgkQ4Ifiq8DH
7PV7cw//XvsvQAHMfkXR35OLWtPJDXxcz0EXU+h8KhueWvnvpSX3HC/yzikobjcE
qC0hXySXbR51FmyucVfEkCqVmP4X1UHDNUUCW3OE/yCVGPKyoZtyVN0r2qbiZrDF
IkwIlNhbFy2FOlqsJcwwHCaMt5cwUeSkwxnkn0wgTpt33SEj2u98Vpqac4DZd+zk
BIXGtN8XvSQMgxDlxm/6NN76G5jdl4kIcBPPsOI9QISCYaTVby7ZfLwaRo8epphe
CtGLV7P9p4Hn5wSoZZeCtDSi3Qtmk3CkEOPDu+/pKQvGTXjFFDLtpfPadoo5aaGf
+wlSL5/4J+E0/QWQo9LoRBUb7N+cQ9ckbJPhdljWD8ug3npgfdAYz4HSpwisPc12
AE3LrsLPLyiP6EOp4QxVvaSkD3OlBqRIprZgeVQPCBpCg1STuY8atCgmnAgVzfiC
EuTvPrgngLED1yBZykWovVTAD6AFBlo7ldcUZC/k30A64rqf658bj2/TplPxYvxB
p0QZMbWVutDwaIViROjHo4djr706lVrNq8ZGBUyUc3DYi77/OMCXSYojb2/IVoFw
R8D0JImdBVb0MI+1EZ3q0TX6fZPnK6dD8daI9Kow7MIOGtkNRsJiCsbnkQKYS4ko
S+zCQ8GeuX244n5jO8Iunnk9j4dcgMj2AH/XRguaSSb3l0n1K2E=
=CIAD
-----END PGP SIGNATURE-----

_______________________________________________
Sent through the Full Disclosure mailing list
https://nmap.org/mailman/listinfo/fulldisclosure
Web Archives & RSS: https://seclists.org/fulldisclosure/
```

---

[![Previous](/images/left-icon-16x16.png)](31)
[By Date](date.html#32)
[![Next](/images/right-icon-16x16.png)](33)

[![Previous](/images/left-icon-16x16.png)](31)
[By Thread](index.html#32)
[![Next](/images/right-icon-16x16.png)](33)

### Current thread:

* **APPLE-SA-11-09-2026-9 visionOS 27.2.1** *Apple Product Security via Fulldisclosure (Nov 12)*

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