---
title: APPLE-SA-2023-03-27-6 tvOS 16.4
url: https://seclists.org/fulldisclosure/2023/Mar/22
source: Full Disclosure
date: 2023-03-29
fetch_date: 2025-10-04T11:03:22.829866
---

# APPLE-SA-2023-03-27-6 tvOS 16.4

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

[![Previous](/images/left-icon-16x16.png)](21)
[By Date](date.html#22)
[![Next](/images/right-icon-16x16.png)](23)

[![Previous](/images/left-icon-16x16.png)](21)
[By Thread](index.html#22)
[![Next](/images/right-icon-16x16.png)](23)

![](/shared/images/nst-icons.svg#search)

# APPLE-SA-2023-03-27-6 tvOS 16.4

---

*From*: Apple Product Security via Fulldisclosure <fulldisclosure () seclists org>
*Date*: Mon, 27 Mar 2023 16:08:37 -0700

---

```
-----BEGIN PGP SIGNED MESSAGE-----
Hash: SHA256

APPLE-SA-2023-03-27-6 tvOS 16.4

tvOS 16.4 addresses the following issues.
Information about the security content is also available at
https://support.apple.com/HT213674.

AppleMobileFileIntegrity
Available for: Apple TV 4K (all models) and Apple TV HD
Impact: A user may gain access to protected parts of the file system
Description: The issue was addressed with improved checks.
CVE-2023-23527: Mickey Jin (@patch1t)

Core Bluetooth
Available for: Apple TV 4K (all models) and Apple TV HD
Impact: Processing a maliciously crafted Bluetooth packet may result
in disclosure of process memory
Description: An out-of-bounds read was addressed with improved bounds
checking.
CVE-2023-23528: Jianjun Dai and Guang Gong of 360 Vulnerability
Research Institute

CoreCapture
Available for: Apple TV 4K (all models) and Apple TV HD
Impact: An app may be able to execute arbitrary code with kernel
privileges
Description: The issue was addressed with improved memory handling.
CVE-2023-28181: Tingting Yin of Tsinghua University

FontParser
Available for: Apple TV 4K (all models) and Apple TV HD
Impact: Processing a maliciously crafted image may result in
disclosure of process memory
Description: The issue was addressed with improved memory handling.
CVE-2023-27956: Ye Zhang of Baidu Security

Foundation
Available for: Apple TV 4K (all models) and Apple TV HD
Impact: Parsing a maliciously crafted plist may lead to an unexpected
app termination or arbitrary code execution
Description: An integer overflow was addressed with improved input
validation.
CVE-2023-27937: an anonymous researcher

Identity Services
Available for: Apple TV 4K (all models) and Apple TV HD
Impact: An app may be able to access information about a user’s
contacts
Description: A privacy issue was addressed with improved private data
redaction for log entries.
CVE-2023-27928: Csaba Fitzl (@theevilbit) of Offensive Security

ImageIO
Available for: Apple TV 4K (all models) and Apple TV HD
Impact: Processing a maliciously crafted image may result in
disclosure of process memory
Description: The issue was addressed with improved memory handling.
CVE-2023-23535: ryuzaki

ImageIO
Available for: Apple TV 4K (all models) and Apple TV HD
Impact: Processing a maliciously crafted image may result in
disclosure of process memory
Description: An out-of-bounds read was addressed with improved input
validation.
CVE-2023-27929: Meysam Firouzi (@R00tkitSMM) of Mbition Mercedes-Benz
Innovation Lab and  jzhu working with Trend Micro Zero Day Initiative

Kernel
Available for: Apple TV 4K (all models) and Apple TV HD
Impact: An app may be able to execute arbitrary code with kernel
privileges
Description: A use after free issue was addressed with improved
memory management.
CVE-2023-27969: Adam Doupé of ASU SEFCOM

Kernel
Available for: Apple TV 4K (all models) and Apple TV HD
Impact: An app with root privileges may be able to execute arbitrary
code with kernel privileges
Description: The issue was addressed with improved memory handling.
CVE-2023-27933: sqrtpwn

Podcasts
Available for: Apple TV 4K (all models) and Apple TV HD
Impact: An app may be able to access user-sensitive data
Description: The issue was addressed with improved checks.
CVE-2023-27942: Mickey Jin (@patch1t)

TCC
Available for: Apple TV 4K (all models) and Apple TV HD
Impact: An app may be able to access user-sensitive data
Description: This issue was addressed by removing the vulnerable
code.
CVE-2023-27931: Mickey Jin (@patch1t)

WebKit
Available for: Apple TV 4K (all models) and Apple TV HD
Impact: Processing maliciously crafted web content may bypass Same
Origin Policy
Description: This issue was addressed with improved state management.
WebKit Bugzilla: 248615
CVE-2023-27932: an anonymous researcher

WebKit
Available for: Apple TV 4K (all models) and Apple TV HD
Impact: A website may be able to track sensitive user information
Description: The issue was addressed by removing origin information.
WebKit Bugzilla: 250837
CVE-2023-27954: an anonymous researcher

Additional recognition

CFNetwork
We would like to acknowledge an anonymous researcher for their
assistance.

CoreServices
We would like to acknowledge Mickey Jin (@patch1t) for their
assistance.

ImageIO
We would like to acknowledge Meysam Firouzi @R00tkitSMM for their
assistance.

WebKit
We would like to acknowledge an anonymous researcher for their
assistance.

Apple TV will periodically check for software updates. Alternatively,
you may manually check for software updates by selecting "Settings ->
System -> Software Update -> Update Software."  To check the current
version of software, select "Settings -> General -> About."
All information is also posted on the Apple Security Updates
web site: https://support.apple.com/en-us/HT201222.

This message is signed with Apple's Product Security PGP key,
and details are available at:
https://www.apple.com/support/security/pgp/
-----BEGIN PGP SIGNATURE-----

iQIzBAEBCAAdFiEEBP+4DupqR5Sgt1DB4RjMIDkeNxkFAmQiHn0ACgkQ4RjMIDke
Nxlyyg//ePQb9FK6kVxRCnemA/ohDVERRj4NgAV7wlwaD5S/JiB2J1udvO6PJtMK
WR70cDcxOyEWwS45ejP/QhkzpEMRQr0Xhgr9E/BRFm8cltHmPbrVLqBXkIYYDYOT
GfLTgzEPHkHnByJySHr8DfNHxDib7oABRaNWHN5Jlr9c7+acpZokOPk7EXcnwojd
yZjxkbiSkOmfizS+hIQvrSXQl+squ1Lva8v4KyygWqnCqbnq+9SVKVAFchWTnXqD
LvODlXEb5a8TwCapcWLQKtrn3oK84tzI9iIDVrY0qhg5Y3Igu0ZrKF6pIcAk2jiA
MFS6rrgRzOk3nEGCYAIhVY8pt989oE5euC9OK/pT1gOUBzXPAiN3/MmvRqRNkNmJ
waNaVw/ITLVWbAN7HlwOZCft1qv+jCdtI7w5U/GwTXWR/ZcFeTFq93RNRw3pbhqZ
dXhJAEbqAxFIgkobmAX7jTnXThs8WJUPIhs3aPFLRrpmVpR+s3XanvGxyXK4gj6/
9ziqm2HQCCYxz654R65Dh97bRhZRD5vtf9ygtuAbQwQnP61df4MDN3hsQAUyhriT
vu0TYdd7yg1oG3mqJxybx9eMQOLB8PBGAR3/pXcD+gLiLATRyH6i4QP43uoQCExE
1hCVqZBIMG/vq8M0XEKT+85/RdaLBdlDKES3N4QLq4UztsWT4bY=
=P2oh
-----END PGP SIGNATURE-----

_______________________________________________
Sent through the Full Disclosure mailing list
https://nmap.org/mailman/listinfo/fulldisclosure
Web Archives & RSS: https://seclists.org/fulldisclosure/
```

---

[![Previous](/images/left-icon-16x16.png)](21)
[By Date](date.html#22)
[![Next](/images/right-icon-16x16.png)](23)

[![Previous](/images/left-icon-16x16.png)](21)
[By Thread](index.html#22)
[![Next](/images/right-icon-16x16.png)](23)

### Current thread:

* **APPLE-SA-2023-03-27-6 tvOS 16.4** *Apple Product Security via Fulldisclosure (Mar 27)*

![](/shared/images/nst-icons.svg#search)

## [Nmap Security Scanner](https://nmap.org/)

* [Ref Guide](https://nmap.org/book/man.html)* [Install Guide](https://nmap.org/book/install.html)* [Docs](https://nmap.org/docs.html)* [Download](https://nmap.org/download.html)* [Nmap OEM](https://nmap.org/oem/)

## [Npcap packet capture](https://npcap.com/)

* [User's Guide](https://npcap.com/guide/)* [API docs](https://npcap.com/guide/npcap-devguide.html#npcap-api)* [Download](https://npcap.com/#download)* [Npcap OEM](https://npcap.com/oem/)

## [Security Lists](https://seclists.org/)

* [Nmap Announce](https://seclists.org/nmap-announce/)* [Nmap Dev](https://seclists.org/nmap-dev/)* [Full Disclosure](h...