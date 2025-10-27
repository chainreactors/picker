---
title: APPLE-SA-01-27-2025-8 tvOS 18.3
url: https://seclists.org/fulldisclosure/2025/Jan/19
source: Full Disclosure
date: 2025-01-29
fetch_date: 2025-10-06T20:11:40.017131
---

# APPLE-SA-01-27-2025-8 tvOS 18.3

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

[![Previous](/images/left-icon-16x16.png)](18)
[By Date](date.html#19)
[![Next](/images/right-icon-16x16.png)](20)

[![Previous](/images/left-icon-16x16.png)](18)
[By Thread](index.html#19)
[![Next](/images/right-icon-16x16.png)](20)

![](/shared/images/nst-icons.svg#search)

# APPLE-SA-01-27-2025-8 tvOS 18.3

---

*From*: Apple Product Security via Fulldisclosure <fulldisclosure () seclists org>
*Date*: Mon, 27 Jan 2025 14:54:40 -0800

---

```
-----BEGIN PGP SIGNED MESSAGE-----
Hash: SHA256

APPLE-SA-01-27-2025-8 tvOS 18.3

tvOS 18.3 addresses the following issues.
Information about the security content is also available at
https://support.apple.com/122072.

Apple maintains a Security Releases page at
https://support.apple.com/100100 which lists recent
software updates with security advisories.

AirPlay
Available for: Apple TV HD and Apple TV 4K (all models)
Impact: An attacker on the local network may be able to cause unexpected
system termination or corrupt process memory
Description: An input validation issue was addressed.
CVE-2025-24126: Uri Katz (Oligo Security)

AirPlay
Available for: Apple TV HD and Apple TV 4K (all models)
Impact: A remote attacker may cause an unexpected app termination
Description: A type confusion issue was addressed with improved checks.
CVE-2025-24129: Uri Katz (Oligo Security)

AirPlay
Available for: Apple TV HD and Apple TV 4K (all models)
Impact: An attacker in a privileged position may be able to perform a
denial-of-service
Description: The issue was addressed with improved memory handling.
CVE-2025-24131: Uri Katz (Oligo Security)

AirPlay
Available for: Apple TV HD and Apple TV 4K (all models)
Impact: A remote attacker may cause an unexpected application
termination or arbitrary code execution
Description: A type confusion issue was addressed with improved checks.
CVE-2025-24137: Uri Katz (Oligo Security)

ARKit
Available for: Apple TV HD and Apple TV 4K (all models)
Impact: Parsing a file may lead to an unexpected app termination
Description: The issue was addressed with improved checks.
CVE-2025-24127: Minghao Lin (@Y1nKoc), babywu, and Xingwei Lin of
Zhejiang University

CoreAudio
Available for: Apple TV HD and Apple TV 4K (all models)
Impact: Parsing a file may lead to an unexpected app termination
Description: The issue was addressed with improved checks.
CVE-2025-24160: Google Threat Analysis Group
CVE-2025-24161: Google Threat Analysis Group
CVE-2025-24163: Google Threat Analysis Group

CoreMedia
Available for: Apple TV HD and Apple TV 4K (all models)
Impact: Parsing a file may lead to an unexpected app termination
Description: The issue was addressed with improved checks.
CVE-2025-24123: Desmond working with Trend Micro Zero Day Initiative
CVE-2025-24124: Pwn2car & Rotiple (HyeongSeok Jang) working with Trend
Micro Zero Day Initiative

CoreMedia
Available for: Apple TV HD and Apple TV 4K (all models)
Impact: A malicious application may be able to elevate privileges. Apple
is aware of a report that this issue may have been actively exploited
against versions of iOS before iOS 17.2.
Description: A use after free issue was addressed with improved memory
management.
CVE-2025-24085

ImageIO
Available for: Apple TV HD and Apple TV 4K (all models)
Impact: Processing an image may lead to a denial-of-service
Description: The issue was addressed with improved memory handling.
CVE-2025-24086: DongJun Kim (@smlijun) and JongSeong Kim (@nevul37) in
Enki WhiteHat, D4m0n

Kernel
Available for: Apple TV HD and Apple TV 4K (all models)
Impact: A malicious app may be able to gain root privileges
Description: A permissions issue was addressed with additional
restrictions.
CVE-2025-24107: an anonymous researcher

Kernel
Available for: Apple TV HD and Apple TV 4K (all models)
Impact: An app may be able to execute arbitrary code with kernel
privileges
Description: A validation issue was addressed with improved logic.
CVE-2025-24159: pattern-f (@pattern_F_)

libxslt
Available for: Apple TV HD and Apple TV 4K (all models)
Impact: Processing maliciously crafted web content may lead to an
unexpected process crash
Description: This issue was addressed through improved state management.
CVE-2025-24166: Ivan Fratric of Google Project Zero

SceneKit
Available for: Apple TV HD and Apple TV 4K (all models)
Impact: Parsing a file may lead to disclosure of user information
Description: An out-of-bounds read was addressed with improved bounds
checking.
CVE-2025-24149: Michael DePlante (@izobashi) of Trend Micro Zero Day
Initiative

WebKit
Available for: Apple TV HD and Apple TV 4K (all models)
Impact: Processing web content may lead to a denial-of-service
Description: The issue was addressed with improved memory handling.
WebKit Bugzilla: 283889
CVE-2025-24158: Q1IQ (@q1iqF) of NUS CuriOSity and P1umer (@p1umer) of
Imperial Global Singapore.

WebKit
Available for: Apple TV HD and Apple TV 4K (all models)
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

Apple TV will periodically check for software updates. Alternatively,
you may manually check for software updates by selecting
"Settings -> System -> Software Update -> Update Software."

To check the current version of software, select
"Settings -> General → About.“

All information is also posted on the Apple Security Releases
web site: https://support.apple.com/100100.

This message is signed with Apple's Product Security PGP key,
and details are available at:
https://www.apple.com/support/security/pgp/

-----BEGIN PGP SIGNATURE-----

iQIzBAEBCAAdFiEEsz9altA7uTI+rE/qX+5d1TXaIvoFAmeYAmYACgkQX+5d1TXa
IvpSZRAAj9rrhljvo23p4Yf41CsDnvAExs+ezpBUOIkNDUmdQ4sfVU81VYLnlLiY
hjf93GwuTXccXiHk2Q/wszpKASksc2Uh2xrpiGohzu5kmmoAyfjeDjWP+dYgihds
z5SSRHmDxDRonihyVd2PhXUU77O4cmPXoxr+BmG4fynlMLrviLW4KrTaWcZWrlwW
ierOYtBY49ksRZlzVlGDhJudRbzVFcsVTB3VVqFUo84LFpVeGJGCg8sk1kfvOS4o
F4hJyTW2xE0zz4OOt/vZ7fa2WKzMnhInl/SFWUMMaY8N2j4VKjeUrF2mNODGoIsf
ZhUpI+bF87czEtJMFplMyueZNn/A4v/irueoWjHi6Wmg4bAl5kmqMHgJh/GOykDZ
4CDGhb0t/OLrUzP9iooJumPj7W3ZSVZUPBfabYmEyyaFpEcqFIvdbylSLEosYwy4
/cvvD8p7vJy80V8pEVJI+/WEF6I8koHJrNcnLdoRql8U/Ai/VPnEWKGJZ9CE8YCU
PbGBi5TeGQ+74K9GnOc5kixfc0m5DWRg6AnyapWfycBl4KpaKQ1gWX0ntgj74g8r
BqCerO+g/PPVhf1wn8CyPveg96xGohv7fDjLtSqZa+CxWsiXqigLdh9hWIHxJhoQ
JaYLzi2T6Z+2e8KF0PIm4r6BVazAzuhboBcWTe74sW44dmuNrWI=
=3cVb
-----END PGP SIGNATURE-----

_______________________________________________
Sent through the Full Disclosure mailing list
https://nmap.org/mailman/listinfo/fulldisclosure
Web Archives & RSS: https://seclists.org/fulldisclosure/
```

---

[![Previous](/images/left-icon-16x16.png)](18)
[By Date](date.html#19)
[![Next](/images/right-icon-16x16.png)](20)

[![Previous](/images/left-icon-16x16.png)](18)
[By Thread](index.html#19)
[![Next](/images/right-icon-16x16.png)](20)

### Current thread:

* **APPLE-SA-01-27-...