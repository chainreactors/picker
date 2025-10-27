---
title: APPLE-SA-07-29-2025-6 watchOS 11.6
url: https://seclists.org/fulldisclosure/2025/Jul/35
source: Full Disclosure
date: 2025-07-31
fetch_date: 2025-10-06T23:56:35.931574
---

# APPLE-SA-07-29-2025-6 watchOS 11.6

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

[![Previous](/images/left-icon-16x16.png)](34)
[By Date](date.html#35)
[![Next](/images/right-icon-16x16.png)](36)

[![Previous](/images/left-icon-16x16.png)](34)
[By Thread](index.html#35)
[![Next](/images/right-icon-16x16.png)](36)

![](/shared/images/nst-icons.svg#search)

# APPLE-SA-07-29-2025-6 watchOS 11.6

---

*From*: Apple Product Security via Fulldisclosure <fulldisclosure () seclists org>
*Date*: Tue, 29 Jul 2025 16:30:25 -0700

---

```
-----BEGIN PGP SIGNED MESSAGE-----
Hash: SHA256

APPLE-SA-07-29-2025-6 watchOS 11.6

watchOS 11.6 addresses the following issues.
Information about the security content is also available at
https://support.apple.com/124155.

Apple maintains a Security Releases page at
https://support.apple.com/100100 which lists recent
software updates with security advisories.

afclip
Available for: Apple Watch Series 6 and later
Impact: Parsing a file may lead to an unexpected app termination
Description: The issue was addressed with improved memory handling.
CVE-2025-43186: Hossein Lotfi (@hosselot) of Trend Micro Zero Day
Initiative

CFNetwork
Available for: Apple Watch Series 6 and later
Impact: A non-privileged user may be able to modify restricted network
settings
Description: A denial-of-service issue was addressed with improved input
validation.
CVE-2025-43223: Andreas Jaegersberger & Ro Achterberg of Nosebeard Labs

CoreAudio
Available for: Apple Watch Series 6 and later
Impact: Processing a maliciously crafted audio file may lead to memory
corruption
Description: The issue was addressed with improved memory handling.
CVE-2025-43277: Google's Threat Analysis Group

CoreMedia
Available for: Apple Watch Series 6 and later
Impact: Processing a maliciously crafted media file may lead to
unexpected app termination or corrupt process memory
Description: An out-of-bounds access issue was addressed with improved
bounds checking.
CVE-2025-43210: Hossein Lotfi (@hosselot) of Trend Micro Zero Day
Initiative

CoreMedia Playback
Available for: Apple Watch Series 6 and later
Impact: An app may be able to access user-sensitive data
Description: The issue was addressed with additional permissions checks.
CVE-2025-43230: Chi Yuan Chang of ZUSO ART and taikosoup

ICU
Available for: Apple Watch Series 6 and later
Impact: Processing maliciously crafted web content may lead to an
unexpected Safari crash
Description: An out-of-bounds access issue was addressed with improved
bounds checking.
CVE-2025-43209: Gary Kwong working with Trend Micro Zero Day Initiative

ImageIO
Available for: Apple Watch Series 6 and later
Impact: Processing a maliciously crafted image may result in disclosure
of process memory
Description: An out-of-bounds read was addressed with improved input
validation.
CVE-2025-43226

libxml2
Available for: Apple Watch Series 6 and later
Impact: Processing a file may lead to memory corruption
Description: This is a vulnerability in open source code and Apple
Software is among the affected projects. The CVE-ID was assigned by a
third party. Learn more about the issue and CVE-ID at cve.org.
CVE-2025-7425: Sergei Glazunov of Google Project Zero

libxslt
Available for: Apple Watch Series 6 and later
Impact: Processing maliciously crafted web content may lead to memory
corruption
Description: This is a vulnerability in open source code and Apple
Software is among the affected projects. The CVE-ID was assigned by a
third party. Learn more about the issue and CVE-ID at cve.org.
CVE-2025-7424: Ivan Fratric of Google Project Zero

Metal
Available for: Apple Watch Series 6 and later
Impact: Processing a maliciously crafted texture may lead to unexpected
app termination
Description: Multiple memory corruption issues were addressed with
improved input validation.
CVE-2025-43234: Vlad Stolyarov of Google's Threat Analysis Group

WebKit
Available for: Apple Watch Series 6 and later
Impact: Processing maliciously crafted web content may disclose
sensitive user information
Description: This issue was addressed through improved state management.
WebKit Bugzilla: 292888
CVE-2025-43227: Gilad Moav

WebKit
Available for: Apple Watch Series 6 and later
Impact: Processing maliciously crafted web content may lead to memory
corruption
Description: The issue was addressed with improved memory handling.
WebKit Bugzilla: 291742
CVE-2025-31278: Yuhao Hu, Yan Kang, Chenggang Wu, and Xiaojie Wei
WebKit Bugzilla: 291745
CVE-2025-31277: Yuhao Hu, Yan Kang, Chenggang Wu, and Xiaojie Wei
WebKit Bugzilla: 293579
CVE-2025-31273: Yuhao Hu, Yan Kang, Chenggang Wu, and Xiaojie Wei

WebKit
Available for: Apple Watch Series 6 and later
Impact: Processing maliciously crafted web content may lead to an
unexpected Safari crash
Description: The issue was addressed with improved memory handling.
WebKit Bugzilla: 292599
CVE-2025-43214: shandikri working with Trend Micro Zero Day Initiative,
Google V8 Security Team
WebKit Bugzilla: 292621
CVE-2025-43213: Google V8 Security Team
WebKit Bugzilla: 293197
CVE-2025-43212: Nan Wang (@eternalsakura13) and Ziling Chen

WebKit
Available for: Apple Watch Series 6 and later
Impact: Processing web content may lead to a denial-of-service
Description: The issue was addressed with improved memory handling.
WebKit Bugzilla: 293730
CVE-2025-43211: Yuhao Hu, Yan Kang, Chenggang Wu, and Xiaojie Wei

WebKit
Available for: Apple Watch Series 6 and later
Impact: Processing maliciously crafted web content may disclose internal
states of the app
Description: An out-of-bounds read was addressed with improved input
validation.
WebKit Bugzilla: 294182
CVE-2025-43265: HexRabbit (@h3xr4bb1t) from DEVCORE Research Team

WebKit
Available for: Apple Watch Series 6 and later
Impact: Processing maliciously crafted web content may lead to an
unexpected Safari crash
Description: A use-after-free issue was addressed with improved memory
management.
WebKit Bugzilla: 295382
CVE-2025-43216: Ignacio Sanmillan (@ulexec)

WebKit
Available for: Apple Watch Series 6 and later
Impact: Processing maliciously crafted web content may lead to an
unexpected Safari crash
Description: This is a vulnerability in open source code and Apple
Software is among the affected projects. The CVE-ID was assigned by a
third party. Learn more about the issue and CVE-ID at cve.org.
WebKit Bugzilla: 296459
CVE-2025-6558: ClÃ©ment Lecigne and Vlad Stolyarov of Google's Threat
Analysis Group

Additional recognition

Bluetooth
We would like to acknowledge LIdong LI, Xiao Wang, Shao Dong Chen, and
Chao Tan of Source Guard for their assistance.

CoreAudio
We would like to acknowledge Noah Weinberg for their assistance.

libxml2
We would like to acknowledge Sergei Glazunov of Google Project Zero for
their assistance.

libxslt
We would like to acknowledge Ivan Fratric of Google Project Zero for
their assistance.

Shortcuts
We would like to acknowledge Dennis Kniep for their assistance.

WebKit
We would like to acknowledge Google V8 Security Team, Yuhao Hu, Yan
Kang, Chenggang Wu, and Xiaojie Wei, rheza (@ginggilBesel) for their
assistance.

Instructions on how to update your Apple Watch software are
available at https://support.apple.com/108926

To check the version on your Apple Watch, open the Apple Watch app
on your iPhone and select "My Watch > General > About".

Alternatively, on your watch, select "My Watch > General > About".

All information is also posted on the Apple Security Releases
web site: https://support.apple.com/100100.

This message is signed with Apple's Product Security PGP key,
and deta...