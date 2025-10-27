---
title: APPLE-SA-2023-03-27-7 watchOS 9.4
url: https://seclists.org/fulldisclosure/2023/Mar/25
source: Full Disclosure
date: 2023-03-29
fetch_date: 2025-10-04T11:03:19.504318
---

# APPLE-SA-2023-03-27-7 watchOS 9.4

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

[![Previous](/images/left-icon-16x16.png)](24)
[By Date](date.html#25)
[![Next](/images/right-icon-16x16.png)](26)

[![Previous](/images/left-icon-16x16.png)](24)
[By Thread](index.html#25)
[![Next](/images/right-icon-16x16.png)](26)

![](/shared/images/nst-icons.svg#search)

# APPLE-SA-2023-03-27-7 watchOS 9.4

---

*From*: Apple Product Security via Fulldisclosure <fulldisclosure () seclists org>
*Date*: Mon, 27 Mar 2023 16:08:46 -0700

---

```
-----BEGIN PGP SIGNED MESSAGE-----
Hash: SHA256

APPLE-SA-2023-03-27-7 watchOS 9.4

watchOS 9.4 addresses the following issues.
Information about the security content is also available at
https://support.apple.com/HT213678.

AppleMobileFileIntegrity
Available for: Apple Watch Series 4 and later
Impact: A user may gain access to protected parts of the file system
Description: The issue was addressed with improved checks.
CVE-2023-23527: Mickey Jin (@patch1t)

Calendar
Available for: Apple Watch Series 4 and later
Impact: Importing a maliciously crafted calendar invitation may
exfiltrate user information
Description: Multiple validation issues were addressed with improved
input sanitization.
CVE-2023-27961: Rıza Sabuncu (@rizasabuncu)

CoreCapture
Available for: Apple Watch Series 4 and later
Impact: An app may be able to execute arbitrary code with kernel
privileges
Description: The issue was addressed with improved memory handling.
CVE-2023-28181: Tingting Yin of Tsinghua University

Find My
Available for: Apple Watch Series 4 and later
Impact: An app may be able to read sensitive location information
Description: A privacy issue was addressed with improved private data
redaction for log entries.
CVE-2023-23537: an anonymous researcher

FontParser
Available for: Apple Watch Series 4 and later
Impact: Processing a maliciously crafted image may result in
disclosure of process memory
Description: The issue was addressed with improved memory handling.
CVE-2023-27956: Ye Zhang of Baidu Security

Foundation
Available for: Apple Watch Series 4 and later
Impact: Parsing a maliciously crafted plist may lead to an unexpected
app termination or arbitrary code execution
Description: An integer overflow was addressed with improved input
validation.
CVE-2023-27937: an anonymous researcher

Identity Services
Available for: Apple Watch Series 4 and later
Impact: An app may be able to access information about a user’s
contacts
Description: A privacy issue was addressed with improved private data
redaction for log entries.
CVE-2023-27928: Csaba Fitzl (@theevilbit) of Offensive Security

ImageIO
Available for: Apple Watch Series 4 and later
Impact: Processing a maliciously crafted image may result in
disclosure of process memory
Description: The issue was addressed with improved memory handling.
CVE-2023-23535: ryuzaki

ImageIO
Available for: Apple Watch Series 4 and later
Impact: Processing a maliciously crafted image may result in
disclosure of process memory
Description: An out-of-bounds read was addressed with improved input
validation.
CVE-2023-27929: Meysam Firouzi (@R00tkitSMM) of Mbition Mercedes-Benz
Innovation Lab and jzhu working with Trend Micro Zero Day Initiative

Kernel
Available for: Apple Watch Series 4 and later
Impact: An app may be able to execute arbitrary code with kernel
privileges
Description: A use after free issue was addressed with improved
memory management.
CVE-2023-27969: Adam Doupé of ASU SEFCOM

Kernel
Available for: Apple Watch Series 4 and later
Impact: An app with root privileges may be able to execute arbitrary
code with kernel privileges
Description: The issue was addressed with improved memory handling.
CVE-2023-27933: sqrtpwn

Podcasts
Available for: Apple Watch Series 4 and later
Impact: An app may be able to access user-sensitive data
Description: The issue was addressed with improved checks.
CVE-2023-27942: Mickey Jin (@patch1t)

Shortcuts
Available for: Apple Watch Series 4 and later
Impact: A shortcut may be able to use sensitive data with certain
actions without prompting the user
Description: The issue was addressed with additional permissions
checks.
CVE-2023-27963: Jubaer Alnazi Jabin of TRS Group Of Companies and
Wenchao Li and Xiaolong Bai of Alibaba Group

TCC
Available for: Apple Watch Series 4 and later
Impact: An app may be able to access user-sensitive data
Description: This issue was addressed by removing the vulnerable
code.
CVE-2023-27931: Mickey Jin (@patch1t)

WebKit
Available for: Apple Watch Series 4 and later
Impact: Processing maliciously crafted web content may bypass Same
Origin Policy
Description: This issue was addressed with improved state management.
WebKit Bugzilla: 248615
CVE-2023-27932: an anonymous researcher

WebKit
Available for: Apple Watch Series 4 and later
Impact: A website may be able to track sensitive user information
Description: The issue was addressed by removing origin information.
WebKit Bugzilla: 250837
CVE-2023-27954: an anonymous researcher

Additional recognition

Activation Lock
We would like to acknowledge Christian Mina for their assistance.

CFNetwork
We would like to acknowledge an anonymous researcher for their
assistance.

CoreServices
We would like to acknowledge Mickey Jin (@patch1t) for their
assistance.

ImageIO
We would like to acknowledge Meysam Firouzi @R00tkitSMM for their
assistance.

Mail
We would like to acknowledge Chen Zhang, Fabian Ising of FH Münster
University of Applied Sciences, Damian Poddebniak of FH Münster
University of Applied Sciences, Tobias Kappert of Münster University
of Applied Sciences, Christoph Saatjohann of Münster University of
Applied Sciences, Sebast, and Merlin Chlosta of CISPA Helmholtz
Center for Information Security for their assistance.

Safari Downloads
We would like to acknowledge Andrew Gonzalez for their assistance.

WebKit
We would like to acknowledge an anonymous researcher for their
assistance.

Instructions on how to update your Apple Watch software are available
at https://support.apple.com/kb/HT204641  To check the version on
your Apple Watch, open the Apple Watch app on your iPhone and select
"My Watch > General > About".  Alternatively, on your watch, select
"My Watch > General > About".
All information is also posted on the Apple Security Updates
web site: https://support.apple.com/en-us/HT201222.

This message is signed with Apple's Product Security PGP key,
and details are available at:
https://www.apple.com/support/security/pgp/
-----BEGIN PGP SIGNATURE-----

iQIzBAEBCAAdFiEEBP+4DupqR5Sgt1DB4RjMIDkeNxkFAmQiHn4ACgkQ4RjMIDke
NxlR6A/+IfL/Ox8qSL2VCsB8vlkddkF4dX5NK6hHzLqZIBq0LmLS8/iEK21+MKP3
F3OwkeM/dgPJwTrXyLiMqDrn/Qh9HPUD1j2iNbPIYCZRBd7O4iHgbwhlT7UAZyMu
JzAMFRokr4tRDJJvDjXHL5dPtk/YliTZSynjeJNqEGG5+rNUW6jjPoqEp5w+aPYG
HwsxZCvySyaOxdB9mWIKJMPUf+uz/HtAn60CA59UeIxliHbco5yZZdqVwTjEwcz4
EJockj5dnK7dDa6yIHnGGlv8Owx2wvtUU3bRMSQ712Zqek+qYxS7Bcp3ywwf5OQM
mIIdLFDaDktNFXMMxsB9IgTuyAziUnjWuJ18NaYPy1lJRBZW/SHblPUoGObRrfoe
JFa33R8lsW9G9ItvLGdXVB73FyfeKnFI1WkeBTPNk4bhkAbTYzPK7IOdHQ6GYSPi
DpVJvZqiD6tgIpngqrMjkOVXoM9OhJVct3G81CrqZdSkUrVeBqHrmw7D8FE08xkF
eqZAnuEDF/muUP49n2RiaIAfw9wFX8wVYbWEziC+DZU5QHqpogHPzn3RJF2yZ3cl
jhLaY3BEibgE/ISyzQ08JysDWeGHwpyRwhr6FVTlEOuHqMCWfGQ/+WSKF0GigXMD
itrkUpyaSJdLn+oc2N3hmDGdyPKwWMmRP9Qa4/nAFaPV+CJedbA=
=KG/z
-----END PGP SIGNATURE-----

_______________________________________________
Sent through the Full Disclosure mailing list
https://nmap.org/mailman/listinfo/fulldisclosure
Web Archives & RSS: https://seclists.org/fulldisclosure/
```

---

[![Previous](/images/left-icon-16x16....