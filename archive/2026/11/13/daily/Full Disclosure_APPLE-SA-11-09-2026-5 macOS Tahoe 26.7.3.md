---
title: APPLE-SA-11-09-2026-5 macOS Tahoe 26.7.3
url: https://seclists.org/fulldisclosure/2026/Nov/28
source: Full Disclosure
date: 2026-11-13
fetch_date: 2026-11-14T08:21:48.109811
---

# APPLE-SA-11-09-2026-5 macOS Tahoe 26.7.3

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

[![Previous](/images/left-icon-16x16.png)](27)
[By Date](date.html#28)
[![Next](/images/right-icon-16x16.png)](29)

[![Previous](/images/left-icon-16x16.png)](27)
[By Thread](index.html#28)
[![Next](/images/right-icon-16x16.png)](29)

![](/shared/images/nst-icons.svg#search)

# APPLE-SA-11-09-2026-5 macOS Tahoe 26.7.3

---

*From*: Apple Product Security via Fulldisclosure <fulldisclosure () seclists org>
*Date*: Mon, 09 Nov 2026 16:06:27 -0800

---

```
-----BEGIN PGP SIGNED MESSAGE-----
Hash: SHA256

APPLE-SA-11-09-2026-5 macOS Tahoe 26.7.3

macOS Tahoe 26.7.3 addresses the following issues.
Information about the security content is also available at
https://support.apple.com/149719.

Apple maintains a Security Releases page at
https://support.apple.com/100100 which lists recent
software updates with security advisories.

AirPlay
Available for: macOS Tahoe
Impact: An attacker in Bluetooth range may be able to bypass the rate
limit on pairing code attempts
Description: A logic issue was addressed with improved state management.
CVE-2026-113968: Apple

Bluetooth
Available for: macOS Tahoe
Impact: An attacker in Bluetooth range may be able to corrupt process
memory
Description: A use-after-free issue was addressed with improved memory
management.
CVE-2026-113970: Apple

brotli
Available for: macOS Tahoe
Impact: Processing maliciously crafted input may lead to memory
corruption
Description: An out-of-bounds write issue was addressed with improved
input validation.
CVE-2026-111497

CoreUtils
Available for: macOS Tahoe
Impact: A malicious Bluetooth device may be able to establish a pairing
without user interaction
Description: This issue was addressed with improved checks.
CVE-2026-113965: Apple

CoreUtils
Available for: macOS Tahoe
Impact: An attacker in Bluetooth range may be able to bypass the rate
limit on pairing code attempts and pair with a device without user
interaction
Description: A logic issue was addressed with improved state management.
CVE-2026-113964: an anonymous researcher

Messages
Available for: macOS Tahoe
Impact: A user added to an iMessage group may be able to access messages
sent before they joined
Description: This issue was addressed by removing the vulnerable code.
CVE-2026-113960: an anonymous researcher

Messages
Available for: macOS Tahoe
Impact: A remote attacker may be able to join an iMessage group chat and
receive its messages
Description: An authorization issue was addressed with improved
validation.
CVE-2026-113961: an anonymous researcher

rapportd
Available for: macOS Tahoe
Impact: An attacker on the same network may be able to bypass the rate
limit on AirPlay pairing code attempts
Description: A logic issue was addressed with improved state management.
CVE-2026-113969: Apple

macOS Tahoe 26.7.3 may be obtained from the Mac App Store or
Apple's Software Downloads web site:
https://support.apple.com/downloads/

All information is also posted on the Apple Security Releases
web site: https://support.apple.com/100100.

This message is signed with Apple's Product Security PGP key,
and details are available at:
https://www.apple.com/support/security/pgp/

-----BEGIN PGP SIGNATURE-----

iQIzBAEBCAAdFiEEhjkl+zMLNwFiCT1o4Ifiq8DH7PUFAmryPGsACgkQ4Ifiq8DH
7PX0RhAAgCxbkOSlvX+HM53rlKreDXsbyKKa2Uo4eBmJxZJq2xa/c1MmEjtmGy7x
EtjZKmmgdjzul60yfUo6U4tMHSFBkxHAzNqXT4fPnWWNuCHXVoPijkPAeJpMdSj1
5Ph5faMKhkJI8XYylVhGTTnCk8R0tyAn4lbb22Hq+PJiJmmZt3j76C+JwwAjzBNS
kgfTjEKqN7QeEADqX8UuH01szer9vcPoOw3LhgKavE5r07j1o8y26gKuQuQBcDwn
+tJft6/HCHw+BVnPv+2Fr2k8aRxUod/7VDinv0WFdPic3GkgVeCKVUxh9awVCgTc
/isuj1OQ9plvXhHhxb9IL97nZDjtfu5Ukfrmtpbyvw+V+mBLOWS9fZJP8nMDTfFu
RcybFMC8hMObjVpG2RBDbplKJqCf/blAwgjmom9H8C7g8Do4KiJO9T7TjNms9vfg
V7SGoXdfTfTQ4sDUIYqi9fntxVWDOQ6AytGiAuFwcWVKZtNutv9laUphz+u3PsV6
TDOI4nLxkj0rRj7x4nzLKX+eO11xSZEdKrMUX/2ba1/iuGHIOElqLBkXwJ/Un18t
VR4P9qqKz4oaGnRyNePeas4qUdyaZSfpqq/vv963qMOTx4tPXvkXaLb2CGKJjIoW
jW7hpIqBp+DweBqHIigNl9glj9F/ogJBdEYz6wovmGDnIvXDzhE=
=Shzn
-----END PGP SIGNATURE-----

_______________________________________________
Sent through the Full Disclosure mailing list
https://nmap.org/mailman/listinfo/fulldisclosure
Web Archives & RSS: https://seclists.org/fulldisclosure/
```

---

[![Previous](/images/left-icon-16x16.png)](27)
[By Date](date.html#28)
[![Next](/images/right-icon-16x16.png)](29)

[![Previous](/images/left-icon-16x16.png)](27)
[By Thread](index.html#28)
[![Next](/images/right-icon-16x16.png)](29)

### Current thread:

* **APPLE-SA-11-09-2026-5 macOS Tahoe 26.7.3** *Apple Product Security via Fulldisclosure (Nov 12)*

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