---
title: APPLE-SA-09-16-2024-3 tvOS 18
url: https://seclists.org/fulldisclosure/2024/Sep/34
source: Full Disclosure
date: 2024-09-18
fetch_date: 2025-10-06T18:30:29.614050
---

# APPLE-SA-09-16-2024-3 tvOS 18

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

[![Previous](/images/left-icon-16x16.png)](33)
[By Date](date.html#34)
[![Next](/images/right-icon-16x16.png)](35)

[![Previous](/images/left-icon-16x16.png)](33)
[By Thread](index.html#34)
[![Next](/images/right-icon-16x16.png)](35)

![](/shared/images/nst-icons.svg#search)

# APPLE-SA-09-16-2024-3 tvOS 18

---

*From*: Apple Product Security via Fulldisclosure <fulldisclosure () seclists org>
*Date*: Mon, 16 Sep 2024 18:07:33 -0700

---

```
-----BEGIN PGP SIGNED MESSAGE-----
Hash: SHA256

APPLE-SA-09-16-2024-3 tvOS 18

tvOS 18 addresses the following issues.
Information about the security content is also available at
https://support.apple.com/121248.

Apple maintains a Security Releases page at
https://support.apple.com/100100 which lists recent
software updates with security advisories.

Game Center
Available for: Apple TV HD and Apple TV 4K (all models)
Impact: An app may be able to access user-sensitive data
Description: A file access issue was addressed with improved input
validation.
CVE-2024-40850: Denis Tokarev (@illusionofcha0s)

ImageIO
Available for: Apple TV HD and Apple TV 4K (all models)
Impact: Processing a maliciously crafted file may lead to unexpected app
termination
Description: An out-of-bounds read issue was addressed with improved
input validation.
CVE-2024-27880: Junsung Lee

ImageIO
Available for: Apple TV HD and Apple TV 4K (all models)
Impact: Processing an image may lead to a denial-of-service
Description: An out-of-bounds access issue was addressed with improved
bounds checking.
CVE-2024-44176: dw0r of ZeroPointer Lab working with Trend Micro Zero
Day Initiative, an anonymous researcher

IOSurfaceAccelerator
Available for: Apple TV HD and Apple TV 4K (all models)
Impact: An app may be able to cause unexpected system termination
Description: The issue was addressed with improved memory handling.
CVE-2024-44169: Antonio ZekiÄ‡

Kernel
Available for: Apple TV HD and Apple TV 4K (all models)
Impact: An app may gain unauthorized access to Bluetooth
Description: This issue was addressed through improved state management.
CVE-2024-44191: Alexander Heinrich, SEEMOO, DistriNet, KU Leuven
(@vanhoefm), TU Darmstadt (@Sn0wfreeze) and Mathy Vanhoef

libxml2
Available for: Apple TV HD and Apple TV 4K (all models)
Impact: Processing maliciously crafted web content may lead to an
unexpected process crash
Description: An integer overflow was addressed through improved input
validation.
CVE-2024-44198: OSS-Fuzz, Ned Williamson of Google Project Zero

mDNSResponder
Available for: Apple TV HD and Apple TV 4K (all models)
Impact: An app may be able to cause a denial-of-service
Description: A logic error was addressed with improved error handling.
CVE-2024-44183: Olivier Levon

Model I/O
Available for: Apple TV HD and Apple TV 4K (all models)
Impact: Processing a maliciously crafted image may lead to a denial-of-
service
Description: This is a vulnerability in open source code and Apple
Software is among the affected projects. The CVE-ID was assigned by a
third party. Learn more about the issue and CVE-ID at cve.org <http://cve.org/>.
CVE-2023-5841

WebKit
Available for: Apple TV HD and Apple TV 4K (all models)
Impact: Processing maliciously crafted web content may lead to universal
cross site scripting
Description: This issue was addressed through improved state management.
WebKit Bugzilla: 268724
CVE-2024-40857: Ron Masas

WebKit
Available for: Apple TV HD and Apple TV 4K (all models)
Impact: A malicious website may exfiltrate data cross-origin
Description: A cross-origin issue existed with "iframe" elements. This
was addressed with improved tracking of security origins.
WebKit Bugzilla: 279452
CVE-2024-44187: Narendra Bhati, Manager of Cyber Security at Suma Soft
Pvt. Ltd, Pune (India)

Wi-Fi
Available for: Apple TV HD and Apple TV 4K (all models)
Impact: An attacker may be able to force a device to disconnect from a
secure network
Description: An integrity issue was addressed with Beacon Protection.
CVE-2024-40856: Domien Schepers

Additional recognition

Kernel
We would like to acknowledge Braxton Anderson, Fakhri Zulkifli
(@d0lph1n98) of PixiePoint Security for their assistance.

WebKit
We would like to acknowledge Avi Lumelsky, Uri Katz, (Oligo Security),
Johan Carlsson (joaxcar) for their assistance.

Wi-Fi
We would like to acknowledge Antonio Zekic (@antoniozekic) and
ant4g0nist, Tim Michaud (@TimGMichaud) of Moveworks.ai for their
assistance.

Apple TV will periodically check for software updates. Alternatively,
you may manually check for software updates by selecting "Settings ->
System -> Software Update -> Update Software."  To check the current
version of software, select "Settings -> General -> About."

All information is also posted on the Apple Security Releases
web site: https://support.apple.com/100100.

This message is signed with Apple's Product Security PGP key,
and details are available at:
https://www.apple.com/support/security/pgp/
-----BEGIN PGP SIGNATURE-----

iQIzBAEBCAAdFiEEsz9altA7uTI+rE/qX+5d1TXaIvoFAmbow38ACgkQX+5d1TXa
IvoDTg/+Py7WMXJYiLZKriQUA/dhuDcFErLcW/FEiYQkklmbY44C2ibgxnryNEkP
GLuo570iTRgQ/f15wi3OM6BpdPz2VjivAF20IwExQ8q76bhqjvUMCw8nmBolzxBo
cDDfWWqpoEMIAraDvPaqKcUzCs4PhmrPfC7KZx23qJje55j+Frnk55QrCG52AHgj
ByZCqzickgE9YFxav5Y72+WR9Tg/3Rb4RHByIh1K7E3gx/8bpvprW8Bh3ZsSKt86
ZwhahqJATTgOx+IgAE/oaLadNql+2GW2gV6/o25MjlWU47aptDr7fFNGUSeOBLvS
kE35kSmBLTQrXWz3dbUBVhJgYUeLwJM0NrTlXXTlOUZjgrb5hKinH8Pf4ER3M4XT
zvnH6qGZvr9UkMg+3MvDOD+j9kEgLsjMR5Kz/60XEH1lTjwU05Fu562ehDb+WQ/a
MZTmP3oUQgDRc7Mxifl/pwiYj0U919ZM2IKOFRyEQ/zh6P20U5uazsCGeiCbI4Ap
bMTiDOHhJ29Rx1K+7PJ4tUGoXYcYM/U2ZX63GHY3zx47EYhG5nDpn8SnZexEaGGA
it6mHDGUPxysu3PUCDlvDqkP2bVvGo1N/agW9uCT+mqrMzuLPQE2TytG8Qw3yEyL
PgkkwUrUHJ6ySatl/alIBK49Xqx3bktRNZ0FJsT4DtNHb7XUoQU=
=zB4q
-----END PGP SIGNATURE-----
_______________________________________________
Sent through the Full Disclosure mailing list
https://nmap.org/mailman/listinfo/fulldisclosure
Web Archives & RSS: https://seclists.org/fulldisclosure/
```

---

[![Previous](/images/left-icon-16x16.png)](33)
[By Date](date.html#34)
[![Next](/images/right-icon-16x16.png)](35)

[![Previous](/images/left-icon-16x16.png)](33)
[By Thread](index.html#34)
[![Next](/images/right-icon-16x16.png)](35)

### Current thread:

* **APPLE-SA-09-16-2024-3 tvOS 18** *Apple Product Security via Fulldisclosure (Sep 16)*

![](/shared/images/nst-icons.svg#search)

## [Nmap Security Scanner](https://nmap.org/)

* [Ref Guide](https://nmap.org/book/man.html)* [Install Guide](https://nmap.org/book/install.html)* [Docs](https://nmap.org/docs.html)* [Download](https://nmap.org/download.html)* [Nmap OEM](https://nmap.org/oem/)

## [Npcap packet capture](https://npcap.com/)

* [User's Guide](https://npcap.com/guide/)* [API docs](https://npcap.com/guide/npcap-devguide.html#npcap-api)* [Download](https://npcap.com/#download)* [Npcap OEM](https://npcap.com/oem/)

## [Security Lists](https://seclists.org/)

* [Nmap Announce](https://seclists.org/nmap-announce/)* [Nmap Dev](https://seclists.org/nmap-dev/)* [Full Disclosure](https://seclists.org/fulldisclosure/)* [Open Source Security](https://seclists.org/oss-sec/)* [BreachExchange](https://seclists.org/dataloss/)

## [Security Tools](https://sectools.org)

* [Vuln scanners](https://sectools.org/tag/vuln-scanners/)* [Password audit](https://sectools.org/tag/pass-audit/)* [Web scanners](https://sectools.org/tag/web-scanners/)* [Wireless](https://sectools.org/tag/wireless/)* [Exploitation](https://sectools.org/tag/sploits/)

## ...