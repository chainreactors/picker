---
title: APPLE-SA-06-29-2026-3 Safari 26.5.2
url: https://seclists.org/fulldisclosure/2026/Jul/13
source: Full Disclosure
date: 2026-07-02
fetch_date: 2026-07-03T05:48:57.810431
---

# APPLE-SA-06-29-2026-3 Safari 26.5.2

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

[![Previous](/images/left-icon-16x16.png)](12)
[By Date](date.html#13)
[![Next](/images/right-icon-16x16.png)](14)

[![Previous](/images/left-icon-16x16.png)](12)
[By Thread](index.html#13)
[![Next](/images/right-icon-16x16.png)](14)

![](/shared/images/nst-icons.svg#search)

# APPLE-SA-06-29-2026-3 Safari 26.5.2

---

*From*: Apple Product Security via Fulldisclosure <fulldisclosure () seclists org>
*Date*: Mon, 29 Jun 2026 13:28:28 -0700

---

```
-----BEGIN PGP SIGNED MESSAGE-----
Hash: SHA256

APPLE-SA-06-29-2026-3 Safari 26.5.2

Safari 26.5.2 addresses the following issues.
Information about the security content is also available at
https://support.apple.com/en-us/127685.

Apple maintains a Security Releases page at
https://support.apple.com/100100 which lists recent
software updates with security advisories.

Web Extensions
Available for: macOS Sonoma and macOS Sequoia
Impact: A malicious web extension may be able to cause an unexpected
process crash
Description: A use-after-free issue was addressed with improved memory
management.
WebKit Bugzilla: 314642
CVE-2026-43704: dr3dd

WebKit
Available for: macOS Sonoma and macOS Sequoia
Impact: Processing maliciously crafted web content may disclose
sensitive user information
Description: A cross-origin issue was addressed with improved tracking
of security origins.
WebKit Bugzilla: 315368
CVE-2026-43700: Vitaly Simonovich, Christian Meurer Xavier

WebKit
Available for: macOS Sonoma and macOS Sequoia
Impact: A malicious website may exfiltrate data cross-origin
Description: The issue was addressed with improved checks.
WebKit Bugzilla: 313357
CVE-2026-43735: Merrick Hare, Drinor Selmanaj (Sentry), Khai Tran, John
Lussier, Rhyru9, Kwak Kiyong, Song Nuri

WebKit
Available for: macOS Sonoma and macOS Sequoia
Impact: Processing maliciously crafted web content may lead to an
unexpected process crash
Description: A use-after-free issue was addressed with improved memory
management.
WebKit Bugzilla: 313693
CVE-2026-43734: Jonathan Alush-Aben
WebKit Bugzilla: 313857
CVE-2026-43726: Josef Korbel (Citadelo), Tristan Madani (@TristanInSec)
from Talence Security, Gia Bui (@yabeow) from Calif.io, Narendra Singh
(@_3P1C)
WebKit Bugzilla: 314398
CVE-2026-43709
WebKit Bugzilla: 317227
CVE-2026-43699: Tommy DeVoss from Braze Security Team (@thedawgyg)
WebKit Bugzilla: 315161
CVE-2026-43742: Юлия Мерцалова

WebKit
Available for: macOS Sonoma and macOS Sequoia
Impact: Processing maliciously crafted web content may disclose
sensitive user information
Description: A path handling issue was addressed with improved
validation.
WebKit Bugzilla: 313085
CVE-2026-43732: Nan Wang (@eternalsakura13)

WebKit
Available for: macOS Sonoma and macOS Sequoia
Impact: Processing maliciously crafted web content may lead to memory
corruption
Description: A use-after-free issue was addressed with improved memory
management.
WebKit Bugzilla: 314115
CVE-2026-43731: dr3dd
WebKit Bugzilla: 313577
CVE-2026-43715: Milad Nasr and Nicholas Carlini with Claude, Anthropic

WebKit
Available for: macOS Sonoma and macOS Sequoia
Impact: Processing maliciously crafted web content may lead to an
unexpected Safari crash
Description: A use-after-free issue was addressed with improved memory
management.
WebKit Bugzilla: 313691
CVE-2026-43727: Tommy DeVoss from Braze Security Team (@thedawgyg), Gia
Bui (@yabeow) from Calif.io, Gurpreet Shergill

WebKit
Available for: macOS Sonoma and macOS Sequoia
Impact: A malicious website may be able to process restricted web
content outside the sandbox
Description: The issue was addressed with improved input validation.
WebKit Bugzilla: 312832
CVE-2026-43725: Luke Francis

WebKit
Available for: macOS Sonoma and macOS Sequoia
Impact: Processing maliciously crafted web content may lead to an
unexpected process crash
Description: The issue was addressed with improved memory handling.
WebKit Bugzilla: 312781
CVE-2026-43663: Soyeon Park, Amy Burnett, Khai Tran, sherkito, Kota
Toda, HexRabbit (@h3xr4bb1t) and NiNi (@terrynini38514) of DEVCORE
Research Team, Using GLM From Z.AI, Tristan Madani (@TristanInSec) from
Talence Security, Brian Carpenter
WebKit Bugzilla: 313528
CVE-2026-39872: Utkarsh Pal, Ignacio Sanmillan (@ulexec)
WebKit Bugzilla: 314235
CVE-2026-43712: Kwak Kiyong, Song Nuri, Tristan Madani (@TristanInSec)
from Talence Security

WebKit
Available for: macOS Sonoma and macOS Sequoia
Impact: Processing maliciously crafted web content may lead to an
unexpected Safari crash
Description: The issue was addressed with improved memory handling.
WebKit Bugzilla: 313473
CVE-2026-43716: Tuan and Duc from Calif.io, OpenAI Codex Security - Amy
Burnett, Evan Lambert

WebKit
Available for: macOS Sonoma and macOS Sequoia
Impact: Processing maliciously crafted web content may lead to an
unexpected Safari crash
Description: An out-of-bounds access issue was addressed with improved
bounds checking.
WebKit Bugzilla: 317231
CVE-2026-43676: Mateusz Krzywicki (iVerify.io), dr3dd, Tommy DeVoss from
Braze Security Team (@thedawgyg)

WebKit
Available for: macOS Sonoma and macOS Sequoia
Impact: Processing maliciously crafted web content may result in the
disclosure of process memory
Description: The issue was addressed with improved memory handling.
WebKit Bugzilla: 308046
CVE-2026-43740: Nathaniel Oh (@calysteon), Arni Hardarson

WebKit
Available for: macOS Sonoma and macOS Sequoia
Impact: Visiting a website may leak sensitive data
Description: A permissions issue was addressed with additional
restrictions.
WebKit Bugzilla: 314806
CVE-2026-43713: Jody Ritonga

WebKit
Available for: macOS Sonoma and macOS Sequoia
Impact: A malicious website may exfiltrate data cross-origin
Description: The issue was addressed with improved input validation.
WebKit Bugzilla: 315306
CVE-2026-43708: Behzad Najjarpour Jabbari (@_G4ru_)

WebKit
Available for: macOS Sonoma and macOS Sequoia
Impact: Processing maliciously crafted web content may lead to an
unexpected process crash
Description: A memory corruption issue was addressed with improved
memory handling.
WebKit Bugzilla: 315951
CVE-2026-43707: OpenAI Codex Security - Amy Burnett

WebKit
Available for: macOS Sonoma and macOS Sequoia
Impact: Processing maliciously crafted web content may lead to memory
corruption
Description: A type confusion issue was addressed with improved checks.
WebKit Bugzilla: 314528
CVE-2026-43705: dr3dd

WebKit
Available for: macOS Sonoma and macOS Sequoia
Impact: A malicious website may be able to process restricted web
content outside the sandbox
Description: The issue was addressed with improved checks.
WebKit Bugzilla: 315004
CVE-2026-43701: Aaron Grattafiori - NVIDIA AI Red Team

WebKit
Available for: macOS Sonoma and macOS Sequoia
Impact: Processing maliciously crafted web content may lead to an
unexpected Safari crash
Description: An out-of-bounds write issue was addressed with improved
input validation.
WebKit Bugzilla: 315365
CVE-2026-43745: OpenAI Codex Security - Amy Burnett, Khai Tran

WebKit Canvas
Available for: macOS Sonoma and macOS Sequoia
Impact: Processing maliciously crafted web content may lead to an
unexpected Safari crash
Description: A use-after-free issue was addressed with improved memory
management.
WebKit Bugzilla: 313175
CVE-2026-43720: Gia Bui (@yabeow) from Calif.io, Josef Korbel

WebKit Storage
Available for: macOS Sonoma and macOS Sequoia
Impact: A malicious website may be able to silently hijack clipboard
data
Description: This issue was addressed through improved stat...