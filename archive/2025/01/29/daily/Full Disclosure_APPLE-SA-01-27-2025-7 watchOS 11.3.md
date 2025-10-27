---
title: APPLE-SA-01-27-2025-7 watchOS 11.3
url: https://seclists.org/fulldisclosure/2025/Jan/18
source: Full Disclosure
date: 2025-01-29
fetch_date: 2025-10-06T20:11:41.540092
---

# APPLE-SA-01-27-2025-7 watchOS 11.3

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

[![Previous](/images/left-icon-16x16.png)](17)
[By Date](date.html#18)
[![Next](/images/right-icon-16x16.png)](19)

[![Previous](/images/left-icon-16x16.png)](17)
[By Thread](index.html#18)
[![Next](/images/right-icon-16x16.png)](19)

![](/shared/images/nst-icons.svg#search)

# APPLE-SA-01-27-2025-7 watchOS 11.3

---

*From*: Apple Product Security via Fulldisclosure <fulldisclosure () seclists org>
*Date*: Mon, 27 Jan 2025 14:54:20 -0800

---

```
-----BEGIN PGP SIGNED MESSAGE-----
Hash: SHA256

APPLE-SA-01-27-2025-7 watchOS 11.3

watchOS 11.3 addresses the following issues.
Information about the security content is also available at
https://support.apple.com/122071.

Apple maintains a Security Releases page at
https://support.apple.com/100100 which lists recent
software updates with security advisories.

AirPlay
Available for: Apple Watch Series 6 and later
Impact: An attacker on the local network may be able to cause unexpected
system termination or corrupt process memory
Description: An input validation issue was addressed.
CVE-2025-24126: Uri Katz (Oligo Security)

AirPlay
Available for: Apple Watch Series 6 and later
Impact: A remote attacker may cause an unexpected app termination
Description: A type confusion issue was addressed with improved checks.
CVE-2025-24129: Uri Katz (Oligo Security)

AirPlay
Available for: Apple Watch Series 6 and later
Impact: An attacker in a privileged position may be able to perform a
denial-of-service
Description: The issue was addressed with improved memory handling.
CVE-2025-24131: Uri Katz (Oligo Security)

AirPlay
Available for: Apple Watch Series 6 and later
Impact: A remote attacker may cause an unexpected application
termination or arbitrary code execution
Description: A type confusion issue was addressed with improved checks.
CVE-2025-24137: Uri Katz (Oligo Security)

CoreAudio
Available for: Apple Watch Series 6 and later
Impact: Parsing a file may lead to an unexpected app termination
Description: The issue was addressed with improved checks.
CVE-2025-24160: Google Threat Analysis Group
CVE-2025-24161: Google Threat Analysis Group
CVE-2025-24163: Google Threat Analysis Group

CoreMedia
Available for: Apple Watch Series 6 and later
Impact: Parsing a file may lead to an unexpected app termination
Description: The issue was addressed with improved checks.
CVE-2025-24123: Desmond working with Trend Micro Zero Day Initiative
CVE-2025-24124: Pwn2car & Rotiple (HyeongSeok Jang) working with Trend
Micro Zero Day Initiative

CoreMedia
Available for: Apple Watch Series 6 and later
Impact: A malicious application may be able to elevate privileges. Apple
is aware of a report that this issue may have been actively exploited
against versions of iOS before iOS 17.2.
Description: A use after free issue was addressed with improved memory
management.
CVE-2025-24085

ImageIO
Available for: Apple Watch Series 6 and later
Impact: Processing an image may lead to a denial-of-service
Description: The issue was addressed with improved memory handling.
CVE-2025-24086: DongJun Kim (@smlijun) and JongSeong Kim (@nevul37) in
Enki WhiteHat, D4m0n

Kernel
Available for: Apple Watch Series 6 and later
Impact: A malicious app may be able to gain root privileges
Description: A permissions issue was addressed with additional
restrictions.
CVE-2025-24107: an anonymous researcher

Kernel
Available for: Apple Watch Series 6 and later
Impact: An app may be able to execute arbitrary code with kernel
privileges
Description: A validation issue was addressed with improved logic.
CVE-2025-24159: pattern-f (@pattern_F_)

LaunchServices
Available for: Apple Watch Series 6 and later
Impact: An app may be able to fingerprint the user
Description: This issue was addressed with improved redaction of
sensitive information.
CVE-2025-24117: Michael (Biscuit) Thomas (@biscuit () social lol)

libxslt
Available for: Apple Watch Series 6 and later
Impact: Processing maliciously crafted web content may lead to an
unexpected process crash
Description: This issue was addressed through improved state management.
CVE-2025-24166: Ivan Fratric of Google Project Zero

SceneKit
Available for: Apple Watch Series 6 and later
Impact: Parsing a file may lead to disclosure of user information
Description: An out-of-bounds read was addressed with improved bounds
checking.
CVE-2025-24149: Michael DePlante (@izobashi) of Trend Micro Zero Day
Initiative

WebKit
Available for: Apple Watch Series 6 and later
Impact: Processing web content may lead to a denial-of-service
Description: The issue was addressed with improved memory handling.
WebKit Bugzilla: 283889
CVE-2025-24158: Q1IQ (@q1iqF) of NUS CuriOSity and P1umer (@p1umer) of
Imperial Global Singapore.

WebKit
Available for: Apple Watch Series 6 and later
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

Passwords
We would like to acknowledge Talal Haj Bakry and Tommy Mysk of Mysk Inc.
@mysk_co for their assistance.

Static Linker
We would like to acknowledge Holger Fuhrmannek for their assistance.

Instructions on how to update your Apple Watch software are
available at https://support.apple.com/108926

To check the version on your Apple Watch, open the Apple Watch app
on your iPhone and select "My Watch > General > About".

Alternatively, on your watch, select "My Watch > General > About".

All information is also posted on the Apple Security Releases
web site: https://support.apple.com/100100.

This message is signed with Apple's Product Security PGP key,
and details are available at:
https://www.apple.com/support/security/pgp/

-----BEGIN PGP SIGNATURE-----

iQIzBAEBCAAdFiEEsz9altA7uTI+rE/qX+5d1TXaIvoFAmeYAjUACgkQX+5d1TXa
IvrFTA/9FkQizjNQG+09priJHVXeZ0SjJZLwRFClm9xG//Fes9nEpxy0+6FBZgKO
DVd2NfhBAOF6NjCO6JTCj7PHwwMvbPMmWUMaernw5sElw8qhQq8XPI2WyJzsuhAK
sUvVlaR9vFshC48m9CdswOR8B9vSaBpDNOHASQnt4b1t8OCrStcOTVv78FUKXV5H
VCrYmNC5roigswe18BxwQ9voeMyyo16NS4vGR2Buq8OoKdQ0ZLTmr/uK0yhlOdrM
6WkzG2pc9fgnIqgnsvAIzHIGJUvLYz5NOcSygkozZewJTiczckKUbR1q/7w10bkC
WQsd6hqh0PaUnkwpQpOhxQOX/R90+6J/zWtEysLIWA4HYFKQuK0TXIKdaoWymxBj
cF3MBLXYHpQ4JEGYpQRPoS7RTf8EZOgZwhL1xqMxKZCuAmJi5nHjH5cFKmgbvn5e
5H2BE6vWsG9DIF1lv6UxlOWS/VNgOCPaZwGhr5Bs9J0pyhGOStvVg+Vs3JLaFlJ2
2hKwJ85Vk2VqAT2zS2+SafIQlDEf/BIdpQSJaSfBJNo3d/Kt2of8mMejpqktfEmx
ffBcijsM8JEFPv1ZLkndcQfAuD/yjDCuk3n4MVoHA+cPtS8Dmmu69QFMPZurEVJH
HASEsBsx+XbxZsvYiGlmqF/s5EaNdID0poZ7z8uPRbp2Y/hMom0=
=zfSu
-----END PGP SIGNATURE-----

_______________________________________________
Sent through the Full Disclosure mailing list
https://nmap.org/mailman/listinfo/fulldisclosure
Web Archives & RSS: https://seclists.org/fulldisclosure/
```

---

[![Previous](/images/left-icon-16x16.png)](17)
[By Date](date.html#18)
[![Next](/images/right-icon-16x16.png)](19)

[![Previous](/images/left-icon-16x16.png)](17)
[By Thread](index.html#18)
[![Next](/images/right-icon-16x16.png)](19)

### Current thread:

* **APPLE-SA-01-27-2025-7 watchOS 11.3** *Apple Product Security via Fulldisclosure (Jan 27)*

![](/shared/images/nst-icons.sv...