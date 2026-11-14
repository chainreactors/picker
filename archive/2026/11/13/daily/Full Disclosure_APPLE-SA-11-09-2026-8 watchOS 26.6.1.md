---
title: APPLE-SA-11-09-2026-8 watchOS 26.6.1
url: https://seclists.org/fulldisclosure/2026/Nov/31
source: Full Disclosure
date: 2026-11-13
fetch_date: 2026-11-14T08:21:47.746107
---

# APPLE-SA-11-09-2026-8 watchOS 26.6.1

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

[![Previous](/images/left-icon-16x16.png)](30)
[By Date](date.html#31)
[![Next](/images/right-icon-16x16.png)](32)

[![Previous](/images/left-icon-16x16.png)](30)
[By Thread](index.html#31)
[![Next](/images/right-icon-16x16.png)](32)

![](/shared/images/nst-icons.svg#search)

# APPLE-SA-11-09-2026-8 watchOS 26.6.1

---

*From*: Apple Product Security via Fulldisclosure <fulldisclosure () seclists org>
*Date*: Mon, 09 Nov 2026 16:21:36 -0800

---

```
-----BEGIN PGP SIGNED MESSAGE-----
Hash: SHA256

APPLE-SA-11-09-2026-8 watchOS 26.6.1

watchOS 26.6.1 addresses the following issues.
Information about the security content is also available at
https://support.apple.com/149723.

Apple maintains a Security Releases page at
https://support.apple.com/100100 which lists recent
software updates with security advisories.

AirPlay
Available for: Apple Watch Series 6, Apple Watch Series 7, Apple Watch
Series 8, Apple Watch SE (2nd generation), and Apple Watch Ultra
Impact: An attacker in Bluetooth range may be able to bypass the rate
limit on pairing code attempts
Description: A logic issue was addressed with improved state management.
CVE-2026-113968: Apple

Bluetooth
Available for: Apple Watch Series 6, Apple Watch Series 7, Apple Watch
Series 8, Apple Watch SE (2nd generation), and Apple Watch Ultra
Impact: An attacker in Bluetooth range may be able to corrupt process
memory
Description: A use-after-free issue was addressed with improved memory
management.
CVE-2026-113970: Apple

CoreUtils
Available for: Apple Watch Series 6, Apple Watch Series 7, Apple Watch
Series 8, Apple Watch SE (2nd generation), and Apple Watch Ultra
Impact: A malicious Bluetooth device may be able to establish a pairing
without user interaction
Description: This issue was addressed with improved checks.
CVE-2026-113965: Apple

CoreUtils
Available for: Apple Watch Series 6, Apple Watch Series 7, Apple Watch
Series 8, Apple Watch SE (2nd generation), and Apple Watch Ultra
Impact: An attacker in Bluetooth range may be able to bypass the rate
limit on pairing code attempts and pair with a device without user
interaction
Description: A logic issue was addressed with improved state management.
CVE-2026-113964: an anonymous researcher

rapportd
Available for: Apple Watch Series 6, Apple Watch Series 7, Apple Watch
Series 8, Apple Watch SE (2nd generation), and Apple Watch Ultra
Impact: An attacker on the same network may be able to bypass the rate
limit on AirPlay pairing code attempts
Description: A logic issue was addressed with improved state management.
CVE-2026-113969: Apple

Instructions on how to update your Apple Watch software are
available at https://support.apple.com/kb/HT204641

To check the version on your Apple Watch, open the Apple Watch app
on your iPhone and select "My Watch > General > About".

Alternatively, on your watch, select "My Watch > General > About".

All information is also posted on the Apple Security Releases
web site: https://support.apple.com/100100.

This message is signed with Apple's Product Security PGP key,
and details are available at:
https://www.apple.com/support/security/pgp/

-----BEGIN PGP SIGNATURE-----

iQIzBAEBCAAdFiEEhjkl+zMLNwFiCT1o4Ifiq8DH7PUFAmryYmsACgkQ4Ifiq8DH
7PUIZg//d2qdsd9FczlHYGX+r0EcVh7ODCRFN7k53cyBhMnY8MQRf0jZD7cXms/n
y5cSB3ihdcq6F+lrnASQtA3wtrtuqNdlbtoMuim9y25n4ipLpIdqGgWFQvTrTo1u
ZCRG/Sc6BnK65B47CwpkPSSt92TyV5LQhM9scyW4dsOCAdZMUuaj8Zcw6hLVxefd
KSClkNwRoglVg578VKxWHDU4HD2SZcLj9jKlN4m7FBG9+2dc59CSOFZ3+7xo19Q1
Rn3ZF1PXDc2AUQS+eiA5P0nOlB1sjKofIVwuXchSQ/Ulmo6m4IGij++qK+8tU1N7
N6Z6SQhjEy+MMa/7V/QvpZTSyP4Jnjoj2+bkRNt6Tf7TMIHqcybfg1OHyqUhSdyB
8PsUrT8cOJEneiKXOgbdDRwf8PMHiIszm+w8XYriYIEDWBtCkJsZQTUgVGp2B15W
qhZdVniwkz11avlMYyWVZUOofag6gI8LfWHBkWEVmiGURiQAyT7eLp1Wf5yaeGXj
E2bU3KcO5b8HQeVNtDw2JeRMZ91SxLEav3q7Ac7HzHBtZZfM6z6yqcJdzLdft+4C
imCemy7syDVZOpze6v+3v+9300EqdKSRSBXhlsDDAusNDg9vy7CHLWTN+JDqguMW
SvFsoP1K2Zfx9s1PGoS77aAqbPXAgUa4E00OEpjbKZbu0AwZEyI=
=FTiO
-----END PGP SIGNATURE-----

_______________________________________________
Sent through the Full Disclosure mailing list
https://nmap.org/mailman/listinfo/fulldisclosure
Web Archives & RSS: https://seclists.org/fulldisclosure/
```

---

[![Previous](/images/left-icon-16x16.png)](30)
[By Date](date.html#31)
[![Next](/images/right-icon-16x16.png)](32)

[![Previous](/images/left-icon-16x16.png)](30)
[By Thread](index.html#31)
[![Next](/images/right-icon-16x16.png)](32)

### Current thread:

* **APPLE-SA-11-09-2026-8 watchOS 26.6.1** *Apple Product Security via Fulldisclosure (Nov 12)*

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