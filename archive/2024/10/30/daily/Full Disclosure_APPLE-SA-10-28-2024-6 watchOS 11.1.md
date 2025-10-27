---
title: APPLE-SA-10-28-2024-6 watchOS 11.1
url: https://seclists.org/fulldisclosure/2024/Oct/14
source: Full Disclosure
date: 2024-10-30
fetch_date: 2025-10-06T18:56:12.174619
---

# APPLE-SA-10-28-2024-6 watchOS 11.1

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

[![Previous](/images/left-icon-16x16.png)](13)
[By Date](date.html#14)
[![Next](/images/right-icon-16x16.png)](15)

[![Previous](/images/left-icon-16x16.png)](13)
[By Thread](index.html#14)
[![Next](/images/right-icon-16x16.png)](15)

![](/shared/images/nst-icons.svg#search)

# APPLE-SA-10-28-2024-6 watchOS 11.1

---

*From*: Apple Product Security via Fulldisclosure <fulldisclosure () seclists org>
*Date*: Mon, 28 Oct 2024 16:19:31 -0700

---

```
-----BEGIN PGP SIGNED MESSAGE-----
Hash: SHA256

APPLE-SA-10-28-2024-6 watchOS 11.1

watchOS 11.1 addresses the following issues.
Information about the security content is also available at
https://support.apple.com/121565.

Apple maintains a Security Releases page at
https://support.apple.com/100100 which lists recent
software updates with security advisories.

Accessibility
Available for: Apple Watch Series 6 and later
Impact: An attacker with physical access to a locked device may be able
to view sensitive user information
Description: The issue was addressed with improved authentication.
CVE-2024-44274: Rizki Maulana (rmrizki.my.id), Matthew Butler, Jake
Derouin

App Support
Available for: Apple Watch Series 6 and later
Impact: A malicious app may be able to run arbitrary shortcuts without
user consent
Description: A path handling issue was addressed with improved logic.
CVE-2024-44255: an anonymous researcher

CoreMedia Playback
Available for: Apple Watch Series 6 and later
Impact: A malicious app may be able to access private information
Description: This issue was addressed with improved handling of
symlinks.
CVE-2024-44273: pattern-f (@pattern_F_), Hikerell of Loadshine Lab

CoreText
Available for: Apple Watch Series 6 and later
Impact: Processing a maliciously crafted font may result in the
disclosure of process memory
Description: The issue was addressed with improved checks.
CVE-2024-44240: Hossein Lotfi (@hosselot) of Trend Micro Zero Day
Initiative
CVE-2024-44302: Hossein Lotfi (@hosselot) of Trend Micro Zero Day
Initiative

Foundation
Available for: Apple Watch Series 6 and later
Impact: Parsing a file may lead to disclosure of user information
Description: An out-of-bounds read was addressed with improved input
validation.
CVE-2024-44282: Hossein Lotfi (@hosselot) of Trend Micro Zero Day
Initiative

ImageIO
Available for: Apple Watch Series 6 and later
Impact: Processing an image may result in disclosure of process memory
Description: This issue was addressed with improved checks.
CVE-2024-44215: Junsung Lee working with Trend Micro Zero Day Initiative

ImageIO
Available for: Apple Watch Series 6 and later
Impact: Processing a maliciously crafted message may lead to a denial-
of-service
Description: The issue was addressed with improved bounds checks.
CVE-2024-44297: Jex Amro

IOSurface
Available for: Apple Watch Series 6 and later
Impact: An app may be able to cause unexpected system termination or
corrupt kernel memory
Description: A use-after-free issue was addressed with improved memory
management.
CVE-2024-44285: an anonymous researcher

Kernel
Available for: Apple Watch Series 6 and later
Impact: An app may be able to leak sensitive kernel state
Description: An information disclosure issue was addressed with improved
private data redaction for log entries.
CVE-2024-44239: Mateusz Krzywicki (@krzywix)

Shortcuts
Available for: Apple Watch Series 6 and later
Impact: An app may be able to access sensitive user data
Description: This issue was addressed with improved redaction of
sensitive information.
CVE-2024-44254: Kirin (@Pwnrin)

Shortcuts
Available for: Apple Watch Series 6 and later
Impact: A malicious app may use shortcuts to access restricted files
Description: A logic issue was addressed with improved checks.
CVE-2024-44269: an anonymous researcher

Siri
Available for: Apple Watch Series 6 and later
Impact: An app may be able to access sensitive user data
Description: This issue was addressed with improved redaction of
sensitive information.
CVE-2024-44194: Rodolphe Brunetti (@eisw0lf)

Siri
Available for: Apple Watch Series 6 and later
Impact: A sandboxed app may be able to access sensitive user data in
system logs
Description: An information disclosure issue was addressed with improved
private data redaction for log entries.
CVE-2024-44278: Kirin (@Pwnrin)

WebKit
Available for: Apple Watch Series 6 and later
Impact: Processing maliciously crafted web content may prevent Content
Security Policy from being enforced
Description: The issue was addressed with improved checks.
WebKit Bugzilla: 278765
CVE-2024-44296: Narendra Bhati, Manager of Cyber Security at Suma Soft
Pvt. Ltd, Pune (India)

WebKit
Available for: Apple Watch Series 6 and later
Impact: Processing maliciously crafted web content may lead to an
unexpected process crash
Description: A memory corruption issue was addressed with improved input
validation.
WebKit Bugzilla: 279780
CVE-2024-44244: an anonymous researcher, Q1IQ (@q1iqF) and P1umer
(@p1umer)

Additional recognition

Calculator
We would like to acknowledge Kenneth Chew for their assistance.

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

Security
We would like to acknowledge Bing Shi, Wenchao Li and Xiaolong Bai of
Alibaba Group for their assistance.

Siri
We would like to acknowledge Bistrit Dahal for their assistance.

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

iQIzBAEBCAAdFiEEsz9altA7uTI+rE/qX+5d1TXaIvoFAmcgAEsACgkQX+5d1TXa
IvpYqw//e5YtWRJMacUQbK4oainyrTgy1EkXT3mV7zHSmzfMYOrhfGVd/4yKMsaa
PSrREy9rcN/oQdLulbAhDfqzEmHSczIxWeP4J48xSR6Od/PY9KFdg4tUJ/DjWp62
LgvsxyOY6HFt5vvzh0Cguf7xjskHgHKAgX+PbByT/RNLEOk8Q4F3acKyq1D3oGH4
5yRBHkNyY2rpJtu/6wrxKrn5+H/OFDcO9ABp772nGm75pa1aaxuLlocVdOezZAod
uWmApZDfLns3wh5yBBuGd9XfXMlpKE0zl1i8y6bPDqe9DBYvS8j0fnZGKNURUaBV
yIPYJi1IH8V0jTYhnwUN0bTYE1IrEYU1sUSDEcq4vBmSxPxXZmY2sgcIjnEgJY8Q
d0f1tzd/C0qPYAIpRIFj8bpgbN22uDEVbT58dh+idhg6c+tckQnGEmadPg9c9H/m
/QxJcc5LdMMwOmyBTSNbwykvb6GKO5TLec1PhU/SImSXxAmtLwNWPk72tZpWEZiI
ASKal+XcCa/SO3Fyfh+VhhbjmJIdR9wki2R+DXUcwfktOVKb4GWMDWPv6KiRL4ls
cNudvcc409JBnIJpKAojXcmzPdqWlICbrPTHihyO9Vf7tIRcgxpBaX8YgYy+lyO4
3kzUGycxUi4kqHao38ag7xNANdHQxO1VTamYDJLYCEXi62kuxno=
=7KV0
-----END PGP SIGNATURE-----

_______________________________________________
Sent through the Full Disclosure mailing list
https://nmap.org/mailman/listinfo/fulldisclosure
Web Archives & RSS: https://seclists.org/fulldisclosure/
```

---

[![Previous](/images/left-icon-16x16.png)](13)
[By Date](date.html#14)
[![Next](/images/right-icon-16x16.png)](15)

[![Pr...