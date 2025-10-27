---
title: APPLE-SA-10-28-2024-8 visionOS 2.1
url: https://seclists.org/fulldisclosure/2024/Oct/16
source: Full Disclosure
date: 2024-10-30
fetch_date: 2025-10-06T18:56:07.121026
---

# APPLE-SA-10-28-2024-8 visionOS 2.1

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

[![Previous](/images/left-icon-16x16.png)](15)
[By Date](date.html#16)
[![Next](/images/right-icon-16x16.png)](17)

[![Previous](/images/left-icon-16x16.png)](15)
[By Thread](index.html#16)
[![Next](/images/right-icon-16x16.png)](17)

![](/shared/images/nst-icons.svg#search)

# APPLE-SA-10-28-2024-8 visionOS 2.1

---

*From*: Apple Product Security via Fulldisclosure <fulldisclosure () seclists org>
*Date*: Mon, 28 Oct 2024 16:21:09 -0700

---

```
-----BEGIN PGP SIGNED MESSAGE-----
Hash: SHA256

APPLE-SA-10-28-2024-8 visionOS 2.1

visionOS 2.1 addresses the following issues.
Information about the security content is also available at
https://support.apple.com/121566.

Apple maintains a Security Releases page at
https://support.apple.com/100100 which lists recent
software updates with security advisories.

App Support
Available for: Apple Vision Pro
Impact: A malicious app may be able to run arbitrary shortcuts without
user consent
Description: A path handling issue was addressed with improved logic.
CVE-2024-44255: an anonymous researcher

CoreMedia Playback
Available for: Apple Vision Pro
Impact: A malicious app may be able to access private information
Description: This issue was addressed with improved handling of
symlinks.
CVE-2024-44273: pattern-f (@pattern_F_), Hikerell of Loadshine Lab

CoreText
Available for: Apple Vision Pro
Impact: Processing a maliciously crafted font may result in the
disclosure of process memory
Description: The issue was addressed with improved checks.
CVE-2024-44240: Hossein Lotfi (@hosselot) of Trend Micro Zero Day
Initiative
CVE-2024-44302: Hossein Lotfi (@hosselot) of Trend Micro Zero Day
Initiative

Foundation
Available for: Apple Vision Pro
Impact: Parsing a file may lead to disclosure of user information
Description: An out-of-bounds read was addressed with improved input
validation.
CVE-2024-44282: Hossein Lotfi (@hosselot) of Trend Micro Zero Day
Initiative

ImageIO
Available for: Apple Vision Pro
Impact: Processing an image may result in disclosure of process memory
Description: This issue was addressed with improved checks.
CVE-2024-44215: Junsung Lee working with Trend Micro Zero Day Initiative

ImageIO
Available for: Apple Vision Pro
Impact: Processing a maliciously crafted message may lead to a denial-
of-service
Description: The issue was addressed with improved bounds checks.
CVE-2024-44297: Jex Amro

IOSurface
Available for: Apple Vision Pro
Impact: An app may be able to cause unexpected system termination or
corrupt kernel memory
Description: A use-after-free issue was addressed with improved memory
management.
CVE-2024-44285: an anonymous researcher

Kernel
Available for: Apple Vision Pro
Impact: An app may be able to leak sensitive kernel state
Description: An information disclosure issue was addressed with improved
private data redaction for log entries.
CVE-2024-44239: Mateusz Krzywicki (@krzywix)

Lock Screen
Available for: Apple Vision Pro
Impact: A user may be able to view sensitive user information
Description: This issue was addressed with improved redaction of
sensitive information.
CVE-2024-44262: Justin Saboo

Managed Configuration
Available for: Apple Vision Pro
Impact: Restoring a maliciously crafted backup file may lead to
modification of protected system files
Description: This issue was addressed with improved handling of
symlinks.
CVE-2024-44258: Hichem Maloufi, Christian Mina, Ismail Amzdak

MobileBackup
Available for: Apple Vision Pro
Impact: Restoring a maliciously crafted backup file may lead to
modification of protected system files
Description: A logic issue was addressed with improved file handling.
CVE-2024-44252: Nimrat Khalsa, Davis Dai, James Gill
(@jjtech@infosec.exchange)

Pro Res
Available for: Apple Vision Pro
Impact: An app may be able to cause unexpected system termination or
corrupt kernel memory
Description: The issue was addressed with improved memory handling.
CVE-2024-44277: an anonymous researcher and Yinyi Wu(@_3ndy1) from Dawn
Security Lab of JD.com, Inc.

Safari Downloads
Available for: Apple Vision Pro
Impact: An attacker may be able to misuse a trust relationship to
download malicious content
Description: This issue was addressed through improved state management.
CVE-2024-44259: Narendra Bhati, Manager of Cyber Security at Suma Soft
Pvt. Ltd, Pune (India)

Safari Private Browsing
Available for: Apple Vision Pro
Impact: Private browsing may leak some browsing history
Description: An information leakage was addressed with additional
validation.
CVE-2024-44229: Lucas Di Tomase

Shortcuts
Available for: Apple Vision Pro
Impact: A malicious app may use shortcuts to access restricted files
Description: A logic issue was addressed with improved checks.
CVE-2024-44269: an anonymous researcher

Siri
Available for: Apple Vision Pro
Impact: An app may be able to access sensitive user data
Description: This issue was addressed with improved redaction of
sensitive information.
CVE-2024-44194: Rodolphe Brunetti (@eisw0lf)

Siri
Available for: Apple Vision Pro
Impact: A sandboxed app may be able to access sensitive user data in
system logs
Description: An information disclosure issue was addressed with improved
private data redaction for log entries.
CVE-2024-44278: Kirin (@Pwnrin)

WebKit
Available for: Apple Vision Pro
Impact: Processing maliciously crafted web content may lead to an
unexpected process crash
Description: A memory corruption issue was addressed with improved input
validation.
WebKit Bugzilla: 279780
CVE-2024-44244: an anonymous researcher, Q1IQ (@q1iqF) and P1umer
(@p1umer)

WebKit
Available for: Apple Vision Pro
Impact: Processing maliciously crafted web content may prevent Content
Security Policy from being enforced
Description: The issue was addressed with improved checks.
WebKit Bugzilla: 278765
CVE-2024-44296: Narendra Bhati, Manager of Cyber Security at Suma Soft
Pvt. Ltd, Pune (India)

Additional recognition

Calendar
We would like to acknowledge  K宝(@Pwnrin) for their assistance.

ImageIO
We would like to acknowledge Amir Bazine and Karsten König of
CrowdStrike Counter Adversary Operations, an anonymous researcher for
their assistance.

Messages
We would like to acknowledge Collin Potter, an anonymous researcher for
their assistance.

NetworkExtension
We would like to acknowledge Patrick Wardle of DoubleYou & the
Objective-See Foundation for their assistance.

Photos
We would like to acknowledge James Robertson for their assistance.

Safari Private Browsing
We would like to acknowledge an anonymous researcher, r00tdaddy for
their assistance.

Safari Tabs
We would like to acknowledge Jaydev Ahire for their assistance.

Security
We would like to acknowledge Bing Shi, Wenchao Li and Xiaolong Bai of
Alibaba Group for their assistance.

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

iQIzBAEBCAAdFiEEsz9altA7uTI+rE/qX+5d1TXaIvoFAmcgAfIACgkQX+5d1TXa
IvpPzw/+OkUnfZKbUwCJy+p9jbg/ZO5i/RRbW4Tk3E6kDx0idc+p/MLRP+Guy3n+
hJOBSf0cEcebnpu8HYJx4FnkTef0SYWfE2qhEES2Rs8kro5lA+Rr/o3yJjhE9tUN
rWr3ZqGptThOsFiC7AxIieBlNGJAXI8J7PdtcIuN1anzF/decUf6mf9xO90nk1JH
Feof4/Mxcks...