---
title: APPLE-SA-10-28-2024-7 tvOS 18.1
url: https://seclists.org/fulldisclosure/2024/Oct/15
source: Full Disclosure
date: 2024-10-30
fetch_date: 2025-10-06T18:56:09.160688
---

# APPLE-SA-10-28-2024-7 tvOS 18.1

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

[![Previous](/images/left-icon-16x16.png)](14)
[By Date](date.html#15)
[![Next](/images/right-icon-16x16.png)](16)

[![Previous](/images/left-icon-16x16.png)](14)
[By Thread](index.html#15)
[![Next](/images/right-icon-16x16.png)](16)

![](/shared/images/nst-icons.svg#search)

# APPLE-SA-10-28-2024-7 tvOS 18.1

---

*From*: Apple Product Security via Fulldisclosure <fulldisclosure () seclists org>
*Date*: Mon, 28 Oct 2024 16:20:25 -0700

---

```
-----BEGIN PGP SIGNED MESSAGE-----
Hash: SHA256

APPLE-SA-10-28-2024-7 tvOS 18.1

tvOS 18.1 addresses the following issues.
Information about the security content is also available at
https://support.apple.com/121569.

Apple maintains a Security Releases page at
https://support.apple.com/100100 which lists recent
software updates with security advisories.

App Support
Available for: Apple TV HD and Apple TV 4K (all models)
Impact: A malicious app may be able to run arbitrary shortcuts without
user consent
Description: A path handling issue was addressed with improved logic.
CVE-2024-44255: an anonymous researcher

CoreMedia Playback
Available for: Apple TV HD and Apple TV 4K (all models)
Impact: A malicious app may be able to access private information
Description: This issue was addressed with improved handling of
symlinks.
CVE-2024-44273: pattern-f (@pattern_F_), Hikerell of Loadshine Lab

CoreText
Available for: Apple TV HD and Apple TV 4K (all models)
Impact: Processing a maliciously crafted font may result in the
disclosure of process memory
Description: The issue was addressed with improved checks.
CVE-2024-44240: Hossein Lotfi (@hosselot) of Trend Micro Zero Day
Initiative
CVE-2024-44302: Hossein Lotfi (@hosselot) of Trend Micro Zero Day
Initiative

Foundation
Available for: Apple TV HD and Apple TV 4K (all models)
Impact: Parsing a file may lead to disclosure of user information
Description: An out-of-bounds read was addressed with improved input
validation.
CVE-2024-44282: Hossein Lotfi (@hosselot) of Trend Micro Zero Day
Initiative

ImageIO
Available for: Apple TV HD and Apple TV 4K (all models)
Impact: Processing an image may result in disclosure of process memory
Description: This issue was addressed with improved checks.
CVE-2024-44215: Junsung Lee working with Trend Micro Zero Day Initiative

ImageIO
Available for: Apple TV HD and Apple TV 4K (all models)
Impact: Processing a maliciously crafted message may lead to a denial-
of-service
Description: The issue was addressed with improved bounds checks.
CVE-2024-44297: Jex Amro

IOSurface
Available for: Apple TV HD and Apple TV 4K (all models)
Impact: An app may be able to cause unexpected system termination or
corrupt kernel memory
Description: A use-after-free issue was addressed with improved memory
management.
CVE-2024-44285: an anonymous researcher

Kernel
Available for: Apple TV HD and Apple TV 4K (all models)
Impact: An app may be able to leak sensitive kernel state
Description: An information disclosure issue was addressed with improved
private data redaction for log entries.
CVE-2024-44239: Mateusz Krzywicki (@krzywix)

Managed Configuration
Available for: Apple TV HD and Apple TV 4K (all models)
Impact: Restoring a maliciously crafted backup file may lead to
modification of protected system files
Description: This issue was addressed with improved handling of
symlinks.
CVE-2024-44258: Hichem Maloufi, Christian Mina, Ismail Amzdak

MobileBackup
Available for: Apple TV HD and Apple TV 4K (all models)
Impact: Restoring a maliciously crafted backup file may lead to
modification of protected system files
Description: A logic issue was addressed with improved file handling.
CVE-2024-44252: Nimrat Khalsa, Davis Dai, James Gill
(@jjtech@infosec.exchange)

Pro Res
Available for: Apple TV HD and Apple TV 4K (all models)
Impact: An app may be able to cause unexpected system termination or
corrupt kernel memory
Description: The issue was addressed with improved memory handling.
CVE-2024-44277: an anonymous researcher and Yinyi Wu(@_3ndy1) from Dawn
Security Lab of JD.com, Inc.

WebKit
Available for: Apple TV HD and Apple TV 4K (all models)
Impact: Processing maliciously crafted web content may prevent Content
Security Policy from being enforced
Description: The issue was addressed with improved checks.
WebKit Bugzilla: 278765
CVE-2024-44296: Narendra Bhati, Manager of Cyber Security at Suma Soft
Pvt. Ltd, Pune (India)

WebKit
Available for: Apple TV HD and Apple TV 4K (all models)
Impact: Processing maliciously crafted web content may lead to an
unexpected process crash
Description: A memory corruption issue was addressed with improved input
validation.
WebKit Bugzilla: 279780
CVE-2024-44244: an anonymous researcher, Q1IQ (@q1iqF) and P1umer
(@p1umer)

Additional recognition

ImageIO
We would like to acknowledge Amir Bazine and Karsten König of
CrowdStrike Counter Adversary Operations, an anonymous researcher for
their assistance.

NetworkExtension
We would like to acknowledge Patrick Wardle of DoubleYou & the
Objective-See Foundation for their assistance.

Photos
We would like to acknowledge James Robertson for their assistance.

Security
We would like to acknowledge Bing Shi, Wenchao Li and Xiaolong Bai of
Alibaba Group for their assistance.

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

iQIzBAEBCAAdFiEEsz9altA7uTI+rE/qX+5d1TXaIvoFAmcgAScACgkQX+5d1TXa
IvpzYBAAoCN0SuujtunAgU1eUmXrdnRze4Jf5Wwz23Qra51OgKehUlK2n1DuToJM
Gs3Bw6inMGX+kizS4vhInhoJ7Z4kArROvKooV6qBtJw5lq7Imxr3E7305dWU230s
HRjaMamEE3llDflvOo5fiKiKBYihuH+qOZ/jrdzdPSaw4zpw5gDA6za5pfAnW58U
2tzwM0zSkAXiAIBrzYlNVcmL7EYdLgullxsSK6KI26qWRAWsN9u5PljzfCBOr1vo
5geJY3EFSjdcrWm1s3AKYCPJQgiL3UwcGFIQqyKsrtwRaFUuM0l/nOIdvP8SW2BY
8wC06REVN2yV29qECsBhtaqXwybBDdwZiBaJ7BaAnHTZzrd0Vc00LC2UgMhT+Qb8
9EtcgsrImVqVKFXsdYvQlqxuWGYJRjkpMuWF2aCtqgjPvUfipzB0HDMhqgFpzeet
EIMFYEV+IqoNYg6AfrsBA+ok4IHaVSyTWHB0k5rQM0YVaVF6MHqZYhKj/lbiHax9
sJbEaDkiFF+xHSKc3LnoG+KTlXboHaaNDyD4/uyEsrcS1S9y4Ni+WnZi2ufluItW
Wl7aRYr+UMR6qc7zWL2mY5cafT/hfNVu6tUbfIWyN5LE9imT27IIVZfzsQ299PCF
Kmi61d0fwS9AuJrxic1TnMbNEGS2g0NLcmTEMeIWFatzhpurglA=
=zC9Y
-----END PGP SIGNATURE-----

_______________________________________________
Sent through the Full Disclosure mailing list
https://nmap.org/mailman/listinfo/fulldisclosure
Web Archives & RSS: https://seclists.org/fulldisclosure/
```

---

[![Previous](/images/left-icon-16x16.png)](14)
[By Date](date.html#15)
[![Next](/images/right-icon-16x16.png)](16)

[![Previous](/images/left-icon-16x16.png)](14)
[By Thread](index.html#15)
[![Next](/images/right-icon-16x16.png)](16)

### Current thread:

* **APPLE-SA-10-28-2024-7 tvOS 18.1** *Apple Product Security via Fulldisclosure (Oct 28)*

![](/shared/images/nst-icons.svg#search)

## [Nmap Security Scanner](https://nmap.org/)

* [Ref Guide](https://nmap.org/book/man.html)* [Install Guide](https://nmap.org/book/install.html)* [Docs](https://nmap.org/docs.html)* [Download](https://nmap.org/download.html)* [Nmap OEM](https://nmap.org/oem/)

## [Npcap packet capture](https://npcap.com/)

* [User's ...