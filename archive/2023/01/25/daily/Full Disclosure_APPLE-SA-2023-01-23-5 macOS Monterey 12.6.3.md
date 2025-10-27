---
title: APPLE-SA-2023-01-23-5 macOS Monterey 12.6.3
url: https://seclists.org/fulldisclosure/2023/Jan/20
source: Full Disclosure
date: 2023-01-25
fetch_date: 2025-10-04T04:48:35.758389
---

# APPLE-SA-2023-01-23-5 macOS Monterey 12.6.3

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

[![Previous](/images/left-icon-16x16.png)](19)
[By Date](date.html#20)
[![Next](/images/right-icon-16x16.png)](21)

[![Previous](/images/left-icon-16x16.png)](19)
[By Thread](index.html#20)
[![Next](/images/right-icon-16x16.png)](21)

![](/shared/images/nst-icons.svg#search)

# APPLE-SA-2023-01-23-5 macOS Monterey 12.6.3

---

*From*: Apple Product Security via Fulldisclosure <fulldisclosure () seclists org>
*Date*: Mon, 23 Jan 2023 18:40:57 -0800

---

```
-----BEGIN PGP SIGNED MESSAGE-----
Hash: SHA256

APPLE-SA-2023-01-23-5 macOS Monterey 12.6.3

macOS Monterey 12.6.3 addresses the following issues.
Information about the security content is also available at
https://support.apple.com/HT213604.

AppleMobileFileIntegrity
Available for: macOS Monterey
Impact: An app may be able to access user-sensitive data
Description: This issue was addressed by enabling hardened runtime.
CVE-2023-23499: Wojciech Reguła (@_r3ggi) of SecuRing
(wojciechregula.blog)

curl
Available for: macOS Monterey
Impact: Multiple issues in curl
Description: Multiple issues were addressed by updating to curl
version 7.86.0.
CVE-2022-42915
CVE-2022-42916
CVE-2022-32221
CVE-2022-35260

curl
Available for: macOS Monterey
Impact: Multiple issues in curl
Description: Multiple issues were addressed by updating to curl
version 7.85.0.
CVE-2022-35252

dcerpc
Available for: macOS Monterey
Impact: Mounting a maliciously crafted Samba network share may lead
to arbitrary code execution
Description: A buffer overflow issue was addressed with improved
memory handling.
CVE-2023-23513: Dimitrios Tatsis and Aleksandar Nikolic of Cisco
Talos

DiskArbitration
Available for: macOS Monterey
Impact: An encrypted volume may be unmounted and remounted by a
different user without prompting for the password
Description: A logic issue was addressed with improved state
management.
CVE-2023-23493: Oliver Norpoth (@norpoth) of KLIXX GmbH (klixx.com)

DriverKit
Available for: macOS Monterey
Impact: An app may be able to execute arbitrary code with kernel
privileges
Description: A type confusion issue was addressed with improved
checks.
CVE-2022-32915: Tommy Muir (@Muirey03)

Intel Graphics Driver
Available for: macOS Monterey
Impact: An app may be able to execute arbitrary code with kernel
privileges
Description: The issue was addressed with improved bounds checks.
CVE-2023-23507: an anonymous researcher

Kernel
Available for: macOS Monterey
Impact: An app may be able to execute arbitrary code with kernel
privileges
Description: The issue was addressed with improved memory handling.
CVE-2023-23504: Adam Doupé of ASU SEFCOM

Kernel
Available for: macOS Monterey
Impact: An app may be able to determine kernel memory layout
Description: An information disclosure issue was addressed by
removing the vulnerable code.
CVE-2023-23502: Pan ZhenPeng (@Peterpan0927) of STAR Labs SG Pte.
Ltd. (@starlabs_sg)

PackageKit
Available for: macOS Monterey
Impact: An app may be able to gain root privileges
Description: A logic issue was addressed with improved state
management.
CVE-2023-23497: Mickey Jin (@patch1t)

Screen Time
Available for: macOS Monterey
Impact: An app may be able to access information about a user’s
contacts
Description: A privacy issue was addressed with improved private data
redaction for log entries.
CVE-2023-23505: Wojciech Regula of SecuRing (wojciechregula.blog)

Weather
Available for: macOS Monterey
Impact: An app may be able to bypass Privacy preferences
Description: The issue was addressed with improved memory handling.
CVE-2023-23511: Wojciech Regula of SecuRing (wojciechregula.blog), an
anonymous researcher

WebKit
Available for: macOS Monterey
Impact: Processing maliciously crafted web content may lead to
arbitrary code execution
Description: The issue was addressed with improved memory handling.
WebKit Bugzilla: 248268
CVE-2023-23518: YeongHyeon Choi (@hyeon101010), Hyeon Park
(@tree_segment), SeOk JEON (@_seokjeon), YoungSung Ahn (@_ZeroSung),
JunSeo Bae (@snakebjs0107), Dohyun Lee (@l33d0hyun) of Team ApplePIE
WebKit Bugzilla: 248268
CVE-2023-23517: YeongHyeon Choi (@hyeon101010), Hyeon Park
(@tree_segment), SeOk JEON (@_seokjeon), YoungSung Ahn (@_ZeroSung),
JunSeo Bae (@snakebjs0107), Dohyun Lee (@l33d0hyun) of Team ApplePIE

Windows Installer
Available for: macOS Monterey
Impact: An app may be able to bypass Privacy preferences
Description: The issue was addressed with improved memory handling.
CVE-2023-23508: Mickey Jin (@patch1t)

Additional recognition

Kernel
We would like to acknowledge Nick Stenning of Replicate for their
assistance.

macOS Monterey 12.6.3 may be obtained from the Mac App Store or
Apple's Software Downloads web site:
https://support.apple.com/downloads/
All information is also posted on the Apple Security Updates
web site: https://support.apple.com/en-us/HT201222.

This message is signed with Apple's Product Security PGP key,
and details are available at:
https://www.apple.com/support/security/pgp/
-----BEGIN PGP SIGNATURE-----

iQIzBAEBCAAdFiEEBP+4DupqR5Sgt1DB4RjMIDkeNxkFAmPPIl8ACgkQ4RjMIDke
NxlXeg/+JwvCu4zHuDTptxkKw1gxht0hTTVJvNjgNWj2XFtnOz9kCIupGj/xPTMl
P9vABQWRbpEJfCJE31FbUcxRCMcr/jm8dDb1ocx4qsGLlY5iGLQ/M1G6OLxQVajg
gGaCSMjW9Zk7l7sXztKj4XcirsB3ft9tiRJwgPUE0znaT70970usFdg+q95CzODm
DHVoa5VNLi0zA4178CIiq4WayAZe90cRYYQQ1+Okjhab/U/blfGgEPhA/rrdjQ85
J4NKTXyGBIWl+Ix4HpLikYpnwm/TKyYiY+MogZ6xUmFwnUgXkPCc4gYdPANQk064
KNjy90yq3Os9IBjfDpw+Pqs6I3GMZ0oNYUKWO+45/0NVp5/qjDFt5K7ZS+Xz5Py7
YrodbwaYiESzsdfLja9ILf8X7taDLHxxfHEvWcXnhcMD1XNKU6mpsb8SOLicWYzp
8maZarjhzQl3dQi4Kz3vQk0hKHTIE6/04fRdDpqhM9WXljayLLO7bsryW8u98Y/b
fR3BXgfsll+QjdLDeW3nfuY+q2JsW0a2lhJZnxuRQPC+wUGDoCY7vcCbv8zkx0oo
y1w8VDBdUjj7vyVSAqoZNlpgl1ebKgciVhTvrgTsyVxuOA94VzDCeI5/6RkjDAJ+
WL2Em8qc4aqXvGEwimKdNkETbyqIRcNVXWhXLVGLsmHvDViVjGQ=
=BbMS
-----END PGP SIGNATURE-----

_______________________________________________
Sent through the Full Disclosure mailing list
https://nmap.org/mailman/listinfo/fulldisclosure
Web Archives & RSS: https://seclists.org/fulldisclosure/
```

---

[![Previous](/images/left-icon-16x16.png)](19)
[By Date](date.html#20)
[![Next](/images/right-icon-16x16.png)](21)

[![Previous](/images/left-icon-16x16.png)](19)
[By Thread](index.html#20)
[![Next](/images/right-icon-16x16.png)](21)

### Current thread:

* **APPLE-SA-2023-01-23-5 macOS Monterey 12.6.3** *Apple Product Security via Fulldisclosure (Jan 23)*

![](/shared/images/nst-icons.svg#search)

## [Nmap Security Scanner](https://nmap.org/)

* [Ref Guide](https://nmap.org/book/man.html)* [Install Guide](https://nmap.org/book/install.html)* [Docs](https://nmap.org/docs.html)* [Download](https://nmap.org/download.html)* [Nmap OEM](https://nmap.org/oem/)

## [Npcap packet capture](https://npcap.com/)

* [User's Guide](https://npcap.com/guide/)* [API docs](https://npcap.com/guide/npcap-devguide.html#npcap-api)* [Download](https://npcap.com/#download)* [Npcap OEM](https://npcap.com/oem/)

## [Security Lists](https://seclists.org/)

* [Nmap Announce](https://seclists.org/nmap-announce/)* [Nmap Dev](https://seclists.org/nmap-dev/)* [Full Disclosure](https://seclists.org/fulldisclosure/)* [Open Source Security](https://seclists.org/oss-sec/)* [BreachExchange](https://seclists.org/dataloss/)

## [Security Tools](https://sectools.org)

* [Vuln scanners](https://sectools.org/tag/vuln-scanners/)* [Password audit](https://sectools.org/tag/pass-audit/)* [Web scanners](https://sectools.org/tag/web-scanners/)* [Wireless](https://sectools.org/tag/wireless/)* [Exploitation](https://se...