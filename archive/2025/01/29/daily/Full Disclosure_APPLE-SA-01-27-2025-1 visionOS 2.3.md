---
title: APPLE-SA-01-27-2025-1 visionOS 2.3
url: https://seclists.org/fulldisclosure/2025/Jan/12
source: Full Disclosure
date: 2025-01-29
fetch_date: 2025-10-06T20:11:54.295032
---

# APPLE-SA-01-27-2025-1 visionOS 2.3

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

[![Previous](/images/left-icon-16x16.png)](11)
[By Date](date.html#12)
[![Next](/images/right-icon-16x16.png)](13)

[![Previous](/images/left-icon-16x16.png)](11)
[By Thread](index.html#12)
[![Next](/images/right-icon-16x16.png)](13)

![](/shared/images/nst-icons.svg#search)

# APPLE-SA-01-27-2025-1 visionOS 2.3

---

*From*: Apple Product Security via Fulldisclosure <fulldisclosure () seclists org>
*Date*: Mon, 27 Jan 2025 14:51:36 -0800

---

```
-----BEGIN PGP SIGNED MESSAGE-----
Hash: SHA256

APPLE-SA-01-27-2025-1 visionOS 2.3

visionOS 2.3 addresses the following issues.
Information about the security content is also available at
https://support.apple.com/122073.

Apple maintains a Security Releases page at
https://support.apple.com/100100 which lists recent
software updates with security advisories.

AirPlay
Available for: Apple Vision Pro
Impact: An attacker on the local network may be able to cause unexpected
system termination or corrupt process memory
Description: An input validation issue was addressed.
CVE-2025-24126: Uri Katz (Oligo Security)

AirPlay
Available for: Apple Vision Pro
Impact: A remote attacker may cause an unexpected app termination
Description: A type confusion issue was addressed with improved checks.
CVE-2025-24129: Uri Katz (Oligo Security)

AirPlay
Available for: Apple Vision Pro
Impact: An attacker in a privileged position may be able to perform a
denial-of-service
Description: The issue was addressed with improved memory handling.
CVE-2025-24131: Uri Katz (Oligo Security)

AirPlay
Available for: Apple Vision Pro
Impact: A remote attacker may cause an unexpected application
termination or arbitrary code execution
Description: A type confusion issue was addressed with improved checks.
CVE-2025-24137: Uri Katz (Oligo Security)

ARKit
Available for: Apple Vision Pro
Impact: Parsing a file may lead to an unexpected app termination
Description: The issue was addressed with improved checks.
CVE-2025-24127: Minghao Lin (@Y1nKoc), babywu, and Xingwei Lin of
Zhejiang University

CoreAudio
Available for: Apple Vision Pro
Impact: Parsing a file may lead to an unexpected app termination
Description: The issue was addressed with improved checks.
CVE-2025-24160: Google Threat Analysis Group
CVE-2025-24161: Google Threat Analysis Group
CVE-2025-24163: Google Threat Analysis Group

CoreMedia
Available for: Apple Vision Pro
Impact: Parsing a file may lead to an unexpected app termination
Description: The issue was addressed with improved checks.
CVE-2025-24123: Desmond working with Trend Micro Zero Day Initiative
CVE-2025-24124: Pwn2car & Rotiple (HyeongSeok Jang) working with Trend
Micro Zero Day Initiative

CoreMedia
Available for: Apple Vision Pro
Impact: A malicious application may be able to elevate privileges. Apple
is aware of a report that this issue may have been actively exploited
against versions of iOS before iOS 17.2.
Description: A use after free issue was addressed with improved memory
management.
CVE-2025-24085

ImageIO
Available for: Apple Vision Pro
Impact: Processing an image may lead to a denial-of-service
Description: The issue was addressed with improved memory handling.
CVE-2025-24086: DongJun Kim (@smlijun) and JongSeong Kim (@nevul37) in
Enki WhiteHat, D4m0n

Kernel
Available for: Apple Vision Pro
Impact: An app may be able to execute arbitrary code with kernel
privileges
Description: A validation issue was addressed with improved logic.
CVE-2025-24159: pattern-f (@pattern_F_)

LaunchServices
Available for: Apple Vision Pro
Impact: An app may be able to fingerprint the user
Description: This issue was addressed with improved redaction of
sensitive information.
CVE-2025-24117: Michael (Biscuit) Thomas (@biscuit () social lol)

libxslt
Available for: Apple Vision Pro
Impact: Processing maliciously crafted web content may lead to an
unexpected process crash
Description: This issue was addressed through improved state management.
CVE-2025-24166: Ivan Fratric of Google Project Zero

Safari
Available for: Apple Vision Pro
Impact: Visiting a malicious website may lead to user interface spoofing
Description: The issue was addressed with improved UI.
CVE-2025-24113: @RenwaX23

SceneKit
Available for: Apple Vision Pro
Impact: Parsing a file may lead to disclosure of user information
Description: An out-of-bounds read was addressed with improved bounds
checking.
CVE-2025-24149: Michael DePlante (@izobashi) of Trend Micro Zero Day
Initiative

WebContentFilter
Available for: Apple Vision Pro
Impact: An attacker may be able to cause unexpected system termination
or corrupt kernel memory
Description: An out-of-bounds write was addressed with improved input
validation.
CVE-2025-24154: an anonymous researcher

WebKit
Available for: Apple Vision Pro
Impact: A maliciously crafted webpage may be able to fingerprint the
user
Description: The issue was addressed with improved access restrictions
to the file system.
WebKit Bugzilla: 283117
CVE-2025-24143: an anonymous researcher

WebKit
Available for: Apple Vision Pro
Impact: Processing web content may lead to a denial-of-service
Description: The issue was addressed with improved memory handling.
WebKit Bugzilla: 283889
CVE-2025-24158: Q1IQ (@q1iqF) of NUS CuriOSity and P1umer (@p1umer) of
Imperial Global Singapore

WebKit
Available for: Apple Vision Pro
Impact: Processing maliciously crafted web content may lead to an
unexpected process crash
Description: This issue was addressed through improved state management.
WebKit Bugzilla: 284159
CVE-2025-24162: linjy of HKUS3Lab and chluo of WHUSecLab

Additional recognition

Audio
We would like to acknowledge Google Threat Analysis Group for their
assistance.

CoreAudio
We would like to acknowledge Google Threat Analysis Group for their
assistance.

CoreMedia Playback
We would like to acknowledge Song Hyun Bae (@bshyuunn) and Lee Dong Ha
(Who4mI) for their assistance.

Files
We would like to acknowledge Chi Yuan Chang of ZUSO ART and taikosoup
for their assistance.

Guest User
We would like to acknowledge Jake Derouin for their assistance.

Passwords
We would like to acknowledge Talal Haj Bakry and Tommy Mysk of Mysk Inc.
@mysk_co for their assistance.

Static Linker
We would like to acknowledge Holger Fuhrmannek for their assistance.

Instructions on how to update visionOS are available at
https://support.apple.com/118481. To check the software version
on your Apple Vision Pro, open the Settings app and choose General >
About.

All information is also posted on the Apple Security Releases
web site: https://support.apple.com/100100.

This message is signed with Apple's Product Security PGP key,
and details are available at:
https://www.apple.com/support/security/pgp/

-----BEGIN PGP SIGNATURE-----

iQIzBAEBCAAdFiEEsz9altA7uTI+rE/qX+5d1TXaIvoFAmeX//YACgkQX+5d1TXa
IvrEZA/8Cn3RRkSN4Mmp18nse6wH2MYcSUrEy9UAPqxR+/pnK3QnEXYSOx1MfABL
sbwaqneZYK51OFGmRe/BQCR8eNHg11qQOsUI0OtVoAJy5KuE/euUvstHFnkOtTFr
LA738wAPmx81LhLHKoXt0cEejDZYGqNR/P0z81YzlKhiUTCsOyEj4dkOKiV4RA+U
p1wNdW+v7JtxEelM7LemfjNLP+C05o63KjNI/dyGntvMKsI0gzxodnpgsA8Xa+nK
kfGJwCpBsniE6Ew0gIW7xwYr4UMljGz/TzV0m+TvLM9alV9QODD7GnlgmRhgVEh/
ItVxi46hCy+/GEpMtfAU9GFRPE2UmeMRP7E08seQrHeOoJlZ5vDYVzwcpmXR+j4P
9cktk5U2WhQd7Q3Jnr1wmswwjkiTd/g/ZBzQlQCbzwnlq0P9MXLug1xokmNP4uDl
dRUVnChhmjyXQut4bAbudJEdVDF8u2wjsh1zXVhs6nhgo21kYzr4SAzPkA57iMEj
ngYLyFBTrkJ9jQhBntVA2s3xQu/0T67I7wWLheW9PrxFAxUhr51w+byXhi93ajYD
dC0QZE4YS3pGgvuXvBKPVz+rGYsdRakPOL27SUy7yhEWQiCU3haUjbgC+Iz4bfD3
LXlqTHjxQOk7ZUIP+kPLYEQ3qjcAqUWKtVjmaRoBV5a56UgX/t0=
=k...