---
title: APPLE-SA-09-16-2024-5 visionOS 2
url: https://seclists.org/fulldisclosure/2024/Sep/36
source: Full Disclosure
date: 2024-09-18
fetch_date: 2025-10-06T18:30:25.171785
---

# APPLE-SA-09-16-2024-5 visionOS 2

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

[![Previous](/images/left-icon-16x16.png)](35)
[By Date](date.html#36)
[![Next](/images/right-icon-16x16.png)](37)

[![Previous](/images/left-icon-16x16.png)](35)
[By Thread](index.html#36)
[![Next](/images/right-icon-16x16.png)](37)

![](/shared/images/nst-icons.svg#search)

# APPLE-SA-09-16-2024-5 visionOS 2

---

*From*: Apple Product Security via Fulldisclosure <fulldisclosure () seclists org>
*Date*: Mon, 16 Sep 2024 18:09:25 -0700

---

```
-----BEGIN PGP SIGNED MESSAGE-----
Hash: SHA256

APPLE-SA-09-16-2024-5 visionOS 2

visionOS 2 addresses the following issues.
Information about the security content is also available at
https://support.apple.com/121249.

Apple maintains a Security Releases page at
https://support.apple.com/100100 which lists recent
software updates with security advisories.

APFS
Available for: Apple Vision Pro
Impact: A malicious app with root privileges may be able to modify the
contents of system files
Description: The issue was addressed with improved checks.
CVE-2024-40825: Pedro Tôrres (@t0rr3sp3dr0)

Compression
Available for: Apple Vision Pro
Impact: Unpacking a maliciously crafted archive may allow an attacker to
write arbitrary files
Description: A race condition was addressed with improved locking.
CVE-2024-27876: Snoolie Keffaber (@0xilis)

Game Center
Available for: Apple Vision Pro
Impact: An app may be able to access user-sensitive data
Description: A file access issue was addressed with improved input
validation.
CVE-2024-40850: Denis Tokarev (@illusionofcha0s)

ImageIO
Available for: Apple Vision Pro
Impact: Processing a maliciously crafted file may lead to unexpected app
termination
Description: An out-of-bounds read issue was addressed with improved
input validation.
CVE-2024-27880: Junsung Lee

ImageIO
Available for: Apple Vision Pro
Impact: Processing an image may lead to a denial-of-service
Description: An out-of-bounds access issue was addressed with improved
bounds checking.
CVE-2024-44176: dw0r of ZeroPointer Lab working with Trend Micro Zero
Day Initiative and an anonymous researcher

IOSurfaceAccelerator
Available for: Apple Vision Pro
Impact: An app may be able to cause unexpected system termination
Description: The issue was addressed with improved memory handling.
CVE-2024-44169: Antonio Zekić

Kernel
Available for: Apple Vision Pro
Impact: Network traffic may leak outside a VPN tunnel
Description: A logic issue was addressed with improved checks.
CVE-2024-44165: Andrew Lytvynov

Kernel
Available for: Apple Vision Pro
Impact: An app may gain unauthorized access to Bluetooth
Description: This issue was addressed through improved state management.
CVE-2024-44191: Alexander Heinrich, SEEMOO, DistriNet, KU Leuven
(@vanhoefm), TU Darmstadt (@Sn0wfreeze) and Mathy Vanhoef

libxml2
Available for: Apple Vision Pro
Impact: Processing maliciously crafted web content may lead to an
unexpected process crash
Description: An integer overflow was addressed through improved input
validation.
CVE-2024-44198: OSS-Fuzz, Ned Williamson of Google Project Zero

mDNSResponder
Available for: Apple Vision Pro
Impact: An app may be able to cause a denial-of-service
Description: A logic error was addressed with improved error handling.
CVE-2024-44183: Olivier Levon

Model I/O
Available for: Apple Vision Pro
Impact: Processing a maliciously crafted image may lead to a denial-of-
service
Description: This is a vulnerability in open source code and Apple
Software is among the affected projects. The CVE-ID was assigned by a
third party. Learn more about the issue and CVE-ID at cve.org.
CVE-2023-5841

Notes
Available for: Apple Vision Pro
Impact: An app may be able to overwrite arbitrary files
Description: This issue was addressed by removing the vulnerable code.
CVE-2024-44167: ajajfxhj

Presence
Available for: Apple Vision Pro
Impact: An app may be able to read sensitive data from the GPU memory
Description: The issue was addressed with improved handling of caches.
CVE-2024-40790: Max Thomas

WebKit
Available for: Apple Vision Pro
Impact: Processing maliciously crafted web content may lead to universal
cross site scripting
Description: This issue was addressed through improved state management.
WebKit Bugzilla: 268724
CVE-2024-40857: Ron Masas

WebKit
Available for: Apple Vision Pro
Impact: A malicious website may exfiltrate data cross-origin
Description: A cross-origin issue existed with "iframe" elements. This
was addressed with improved tracking of security origins.
WebKit Bugzilla: 279452
CVE-2024-44187: Narendra Bhati, Manager of Cyber Security at Suma Soft
Pvt. Ltd, Pune (India)

Additional recognition

Kernel
We would like to acknowledge Braxton Anderson for their assistance.

Maps
We would like to acknowledge Kirin (@Pwnrin) for their assistance.

Passwords
We would like to acknowledge Richard Hyunho Im (@r1cheeta) for their
assistance.

TCC
We would like to acknowledge Vaibhav Prajapati for their assistance.

WebKit
We would like to acknowledge Avi Lumelsky, Uri Katz, (Oligo Security),
Johan Carlsson (joaxcar) for their assistance.

Instructions on how to update visionOS are available at
https://support.apple.com/HT214009 To check the software version
on your Apple Vision Pro, open the Settings app and choose General >
About.

All information is also posted on the Apple Security Releases
web site: https://support.apple.com/100100.

This message is signed with Apple's Product Security PGP key,
and details are available at:
https://www.apple.com/support/security/pgp/
-----BEGIN PGP SIGNATURE-----

iQIzBAEBCAAdFiEEsz9altA7uTI+rE/qX+5d1TXaIvoFAmboyKsACgkQX+5d1TXa
IvqFuxAAopj95HCodS5RObRJUENK6BWIMzT6ZZGjq3uSaglBxCsDWnnrPrhAwZAF
Xqe1eCauwXsl9lDJJ56dv0z2C84TZp5UP+nM+saBAZs9fzj037YSXXa8lriMBxMl
XNjF22l60+9s/5kwLZDackZI57et6mQbTEKrFf9ZzuaPpuMPuHgvPICEjDjUOhFN
noozxvy+D6jT8uTCLtAAk/4/B8sbOUJ5zRbyy1jmifLNtWgymxbSeoF5kHYedvdZ
r65m84Q0W6WuxfEa0syjrsPFbHaBKnhD0bPLYR/nd5d0DCv1e36nj4z4tTWkAMZz
jutBmHvawNAPJixppNOCME3p0agFxnBQBVsk5hPUEpKw7wlBmGjcK+tzfrNnivA7
kJrFOS3LAp9jtTY4E4JobrpYAvKOAwE2W1uby41iKjNcnNYiUmnUvCKwA/3EkB7W
atVnSHuZepKbB7RD9MNz+U/AASL9oGBocvvd/c2kln/RSnhAFGE+xxw+xgtqQzrs
VKlczIRaSB/Ryk8+uFHcLZ09SZziq8CX/nr1NZjI73IhwDD6x1YGUbUqV+mXsWTV
gwpqCyC9trJJ9Qxcz/pDBGRDCSNxG6x7iY4GTRVAjmmtDIPFxd1znjjVrF6bneV7
vKX/YadQpz7Pqem6I67GFQjQGDVOvlhJ0v35K8VCH0LlRWsl3CE=
=iu8f
-----END PGP SIGNATURE-----

_______________________________________________
Sent through the Full Disclosure mailing list
https://nmap.org/mailman/listinfo/fulldisclosure
Web Archives & RSS: https://seclists.org/fulldisclosure/
```

---

[![Previous](/images/left-icon-16x16.png)](35)
[By Date](date.html#36)
[![Next](/images/right-icon-16x16.png)](37)

[![Previous](/images/left-icon-16x16.png)](35)
[By Thread](index.html#36)
[![Next](/images/right-icon-16x16.png)](37)

### Current thread:

* **APPLE-SA-09-16-2024-5 visionOS 2** *Apple Product Security via Fulldisclosure (Sep 16)*

![](/shared/images/nst-icons.svg#search)

## [Nmap Security Scanner](https://nmap.org/)

* [Ref Guide](https://nmap.org/book/man.html)* [Install Guide](https://nmap.org/book/install.html)* [Docs](https://nmap.org/docs.html)* [Download](https://nmap.org/download.html)* [Nmap OEM](https://nmap.org/oem/)

## [Npcap packet capture](https://npcap.com/)

* [User's Guide](https://npcap.com/guide/)* [API docs](https://npcap.com/guide/npcap-devguide.html#npcap-api)* [Download](https://npcap.com/#download)* [Npcap OEM](https://npcap.com/oem/)

## [Security Lists](https://seclists.org/)

* [Nmap Announce](https://sec...