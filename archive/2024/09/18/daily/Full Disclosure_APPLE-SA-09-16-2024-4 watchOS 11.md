---
title: APPLE-SA-09-16-2024-4 watchOS 11
url: https://seclists.org/fulldisclosure/2024/Sep/35
source: Full Disclosure
date: 2024-09-18
fetch_date: 2025-10-06T18:30:26.623664
---

# APPLE-SA-09-16-2024-4 watchOS 11

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

[![Previous](/images/left-icon-16x16.png)](34)
[By Date](date.html#35)
[![Next](/images/right-icon-16x16.png)](36)

[![Previous](/images/left-icon-16x16.png)](34)
[By Thread](index.html#35)
[![Next](/images/right-icon-16x16.png)](36)

![](/shared/images/nst-icons.svg#search)

# APPLE-SA-09-16-2024-4 watchOS 11

---

*From*: Apple Product Security via Fulldisclosure <fulldisclosure () seclists org>
*Date*: Mon, 16 Sep 2024 18:08:12 -0700

---

```
-----BEGIN PGP SIGNED MESSAGE-----
Hash: SHA256

APPLE-SA-09-16-2024-4 watchOS 11

watchOS 11 addresses the following issues.
Information about the security content is also available at
https://support.apple.com/121240.

Apple maintains a Security Releases page at
https://support.apple.com/100100 which lists recent
software updates with security advisories.

Accessibility
Available for: Apple Watch Series 6 and later
Impact: An attacker with physical access to a locked device may be able
to Control Nearby Devices via accessibility features
Description: This issue was addressed through improved state management.
CVE-2024-44171: Jake Derouin

Game Center
Available for: Apple Watch Series 6 and later
Impact: An app may be able to access user-sensitive data
Description: A file access issue was addressed with improved input
validation.
CVE-2024-40850: Denis Tokarev (@illusionofcha0s)

ImageIO
Available for: Apple Watch Series 6 and later
Impact: Processing a maliciously crafted file may lead to unexpected app
termination
Description: An out-of-bounds read issue was addressed with improved
input validation.
CVE-2024-27880: Junsung Lee

ImageIO
Available for: Apple Watch Series 6 and later
Impact: Processing an image may lead to a denial-of-service
Description: An out-of-bounds access issue was addressed with improved
bounds checking.
CVE-2024-44176: dw0r of ZeroPointer Lab working with Trend Micro Zero
Day Initiative, an anonymous researcher

IOSurfaceAccelerator
Available for: Apple Watch Series 6 and later
Impact: An app may be able to cause unexpected system termination
Description: The issue was addressed with improved memory handling.
CVE-2024-44169: Antonio Zekić

Kernel
Available for: Apple Watch Series 6 and later
Impact: An app may gain unauthorized access to Bluetooth
Description: This issue was addressed through improved state management.
CVE-2024-44191: Alexander Heinrich, SEEMOO, DistriNet, KU Leuven
(@vanhoefm), TU Darmstadt (@Sn0wfreeze) and Mathy Vanhoef

libxml2
Available for: Apple Watch Series 6 and later
Impact: Processing maliciously crafted web content may lead to an
unexpected process crash
Description: An integer overflow was addressed through improved input
validation.
CVE-2024-44198: OSS-Fuzz, Ned Williamson of Google Project Zero

mDNSResponder
Available for: Apple Watch Series 6 and later
Impact: An app may be able to cause a denial-of-service
Description: A logic error was addressed with improved error handling.
CVE-2024-44183: Olivier Levon

Siri
Available for: Apple Watch Series 6 and later
Impact: An app may be able to access user-sensitive data
Description: A privacy issue was addressed by moving sensitive data to a
more secure location.
CVE-2024-44170: K宝, LFY (@secsys), Smi1e, yulige, Cristian Dinca
(icmd.tech), Rodolphe BRUNETTI (@eisw0lf)

WebKit
Available for: Apple Watch Series 6 and later
Impact: Processing maliciously crafted web content may lead to universal
cross site scripting
Description: This issue was addressed through improved state management.
WebKit Bugzilla: 268724
CVE-2024-40857: Ron Masas

WebKit
Available for: Apple Watch Series 6 and later
Impact: A malicious website may exfiltrate data cross-origin
Description: A cross-origin issue existed with "iframe" elements. This
was addressed with improved tracking of security origins.
WebKit Bugzilla: 279452
CVE-2024-44187: Narendra Bhati, Manager of Cyber Security at Suma Soft
Pvt. Ltd, Pune (India)

Additional recognition

Kernel
We would like to acknowledge Braxton Anderson, Fakhri Zulkifli
(@d0lph1n98) of PixiePoint Security for their assistance.

Maps
We would like to acknowledge Kirin (@Pwnrin) for their assistance.

Shortcuts
We would like to acknowledge Cristian Dinca of "Tudor Vianu" National
High School of Computer Science, Romania, Jacob Braun, an anonymous
researcher for their assistance.

Siri
We would like to acknowledge Rohan Paudel, an anonymous researcher for
their assistance.

Voice Memos
We would like to acknowledge Lisa B for their assistance.

WebKit
We would like to acknowledge Avi Lumelsky, Uri Katz, (Oligo Security),
Johan Carlsson (joaxcar) for their assistance.

Instructions on how to update your Apple Watch software are
available at https://support.apple.com/108926 To check the version
on your Apple Watch, open the Apple Watch app on your iPhone and
select "My Watch > General > About".

Alternatively, on your watch, select "My Watch > General > About".

All information is also posted on the Apple Security Releases
web site: https://support.apple.com/100100.

This message is signed with Apple's Product Security PGP key,
and details are available at:
https://www.apple.com/support/security/pgp/

-----BEGIN PGP SIGNATURE-----

iQIzBAEBCAAdFiEEsz9altA7uTI+rE/qX+5d1TXaIvoFAmbo03YACgkQX+5d1TXa
Ivo7dQ/+J6BOLeRrnBR7yFbMd/uxddsdHtDYNXgxQ6GxD7RIC+iSrwsdgpd2eqX9
jCiWMz84k0K24oLgzhW7WpDU9si0wShDdxR1Lpnr9Cr4je+7kZ8bauqBAYhiJntl
FtyoHtz4pXW4/US/aLtqSLNmoptf8cJU2zEn90uwJ5rAWx5NILuG8d/8ajwB/u/G
PZP8ip1RXHiAysk7qFK+Dl3quxyQLvSIgiUU0aejTSDgjKpmxtwFaMheQ5TZmU90
U0Xec15kmkRDKtnCioJreC31RhMsDuZbvp90OQj5MxrNvM/mLZqHa1S3xxCN6ZlG
Iqs/JR/o5t7v03K055wjqs27VwuxxysLoT4ospbHF3sLpycnjboHj6BgLKrfr3nr
0UOPpQdMmSsftevVb0z/mzUIblw8fM7ChWWPbLF8e1TlUCrEyw116I6fNDpp0kl9
Q29Nn74oF69wDeLpdF0Pm+zPGfYYpFuQRew0jDtHS11xKWLN79ZdCyTJ2A2p7KRL
O3k7HN5fpEKg0Q9kpC8UsPx6F7vHrH2mKV+MUoEj7EP5YbRltV+9s0Nw24HK8j17
gF7T3FOrYCEzIQ3+BzgTtzViwMSP7EjmEo7mA3Ward3DIj207Wkwfit8FS/9TpaI
DjzlZoxUcMrC60SlDyG6RJWoiCH460xjFrzqefBb+Bphn4Pj7AE=
=bEDj
-----END PGP SIGNATURE-----

_______________________________________________
Sent through the Full Disclosure mailing list
https://nmap.org/mailman/listinfo/fulldisclosure
Web Archives & RSS: https://seclists.org/fulldisclosure/
```

---

[![Previous](/images/left-icon-16x16.png)](34)
[By Date](date.html#35)
[![Next](/images/right-icon-16x16.png)](36)

[![Previous](/images/left-icon-16x16.png)](34)
[By Thread](index.html#35)
[![Next](/images/right-icon-16x16.png)](36)

### Current thread:

* **APPLE-SA-09-16-2024-4 watchOS 11** *Apple Product Security via Fulldisclosure (Sep 16)*

![](/shared/images/nst-icons.svg#search)

## [Nmap Security Scanner](https://nmap.org/)

* [Ref Guide](https://nmap.org/book/man.html)* [Install Guide](https://nmap.org/book/install.html)* [Docs](https://nmap.org/docs.html)* [Download](https://nmap.org/download.html)* [Nmap OEM](https://nmap.org/oem/)

## [Npcap packet capture](https://npcap.com/)

* [User's Guide](https://npcap.com/guide/)* [API docs](https://npcap.com/guide/npcap-devguide.html#npcap-api)* [Download](https://npcap.com/#download)* [Npcap OEM](https://npcap.com/oem/)

## [Security Lists](https://seclists.org/)

* [Nmap Announce](https://seclists.org/nmap-announce/)* [Nmap Dev](https://seclists.org/nmap-dev/)* [Full Disclosure](https://seclists.org/fulldisclosure/)* [Open Source Security](https://seclists.org/oss-sec/)* [BreachExchange](https://seclists.org/dataloss/)

## [Security Tools](https://sectools.org)

* [Vuln scanners](https://sectools.org/tag/vuln-scanners/)* [Password audit](htt...