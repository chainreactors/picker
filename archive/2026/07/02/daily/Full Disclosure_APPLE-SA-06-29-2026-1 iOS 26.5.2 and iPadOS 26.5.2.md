---
title: APPLE-SA-06-29-2026-1 iOS 26.5.2 and iPadOS 26.5.2
url: https://seclists.org/fulldisclosure/2026/Jul/11
source: Full Disclosure
date: 2026-07-02
fetch_date: 2026-07-03T05:48:58.421872
---

# APPLE-SA-06-29-2026-1 iOS 26.5.2 and iPadOS 26.5.2

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

[![Previous](/images/left-icon-16x16.png)](10)
[By Date](date.html#11)
[![Next](/images/right-icon-16x16.png)](12)

[![Previous](/images/left-icon-16x16.png)](10)
[By Thread](index.html#11)
[![Next](/images/right-icon-16x16.png)](12)

![](/shared/images/nst-icons.svg#search)

# APPLE-SA-06-29-2026-1 iOS 26.5.2 and iPadOS 26.5.2

---

*From*: Apple Product Security via Fulldisclosure <fulldisclosure () seclists org>
*Date*: Mon, 29 Jun 2026 13:27:27 -0700

---

```
-----BEGIN PGP SIGNED MESSAGE-----
Hash: SHA256

APPLE-SA-06-29-2026-1 iOS 26.5.2 and iPadOS 26.5.2

iOS 26.5.2 and iPadOS 26.5.2 addresses the following issues.
Information about the security content is also available at
https://support.apple.com/en-us/127594.

Apple maintains a Security Releases page at
https://support.apple.com/100100 which lists recent
software updates with security advisories.

IOGPUFamily
Available for: iPhone 11 and later, iPad Pro 12.9-inch 3rd generation
and later, iPad Pro 11-inch 1st generation and later, iPad Air 3rd
generation and later, iPad 8th generation and later, and iPad mini 5th
generation and later
Impact: An app may be able to cause unexpected system termination
Description: A race condition was addressed with improved state
handling.
CVE-2026-43743: Lyutoon, Dun

Kernel
Available for: iPhone 11 and later, iPad Pro 12.9-inch 3rd generation
and later, iPad Pro 11-inch 1st generation and later, iPad Air 3rd
generation and later, iPad 8th generation and later, and iPad mini 5th
generation and later
Impact: An app may be able to cause unexpected system termination or
write kernel memory
Description: The issue was addressed with improved input sanitization.
CVE-2026-43724: Hyunwoo Kim (@v4bel)

Kernel
Available for: iPhone 11 and later, iPad Pro 12.9-inch 3rd generation
and later, iPad Pro 11-inch 1st generation and later, iPad Air 3rd
generation and later, iPad 8th generation and later, and iPad mini 5th
generation and later
Impact: An app may be able to leak sensitive kernel state
Description: The issue was addressed with improved input sanitization.
CVE-2026-43722: Feng Xue and XGPT of ThreatBook, Hyunwoo Kim (@v4bel)

Kernel
Available for: iPhone 11 and later, iPad Pro 12.9-inch 3rd generation
and later, iPad Pro 11-inch 1st generation and later, iPad Air 3rd
generation and later, iPad 8th generation and later, and iPad mini 5th
generation and later
Impact: An app may be able to cause unexpected system termination or
corrupt kernel memory
Description: This issue was addressed with improved input validation.
CVE-2026-39868: Vladislav Shevchenko (Positive Technologies), Ye Zhang
(@VAR10CK) of Baidu Security, Billy Jheng Bing Jhong and Pan Zhenpeng
(@Peterpan0927) of STAR Labs SG Pte. Ltd.

libxslt
Available for: iPhone 11 and later, iPad Pro 12.9-inch 3rd generation
and later, iPad Pro 11-inch 1st generation and later, iPad Air 3rd
generation and later, iPad 8th generation and later, and iPad mini 5th
generation and later
Impact: Processing maliciously crafted web content may lead to an
unexpected process crash
Description: A double free issue was addressed with improved memory
management.
CVE-2026-43706: Tristan Madani (@TristanInSec) from Talence Security

libxslt
Available for: iPhone 11 and later, iPad Pro 12.9-inch 3rd generation
and later, iPad Pro 11-inch 1st generation and later, iPad Air 3rd
generation and later, iPad 8th generation and later, and iPad mini 5th
generation and later
Impact: Processing maliciously crafted web content may lead to an
unexpected process crash
Description: The issue was addressed with improved memory handling.
CVE-2026-43703: Tristan Madani (@TristanInSec) from Talence Security

Web Extensions
Available for: iPhone 11 and later, iPad Pro 12.9-inch 3rd generation
and later, iPad Pro 11-inch 1st generation and later, iPad Air 3rd
generation and later, iPad 8th generation and later, and iPad mini 5th
generation and later
Impact: A malicious web extension may be able to cause an unexpected
process crash
Description: A use-after-free issue was addressed with improved memory
management.
WebKit Bugzilla: 314642
CVE-2026-43704: dr3dd

WebKit
Available for: iPhone 11 and later, iPad Pro 12.9-inch 3rd generation
and later, iPad Pro 11-inch 1st generation and later, iPad Air 3rd
generation and later, iPad 8th generation and later, and iPad mini 5th
generation and later
Impact: Processing maliciously crafted web content may disclose
sensitive user information
Description: A cross-origin issue was addressed with improved tracking
of security origins.
WebKit Bugzilla: 315368
CVE-2026-43700: Vitaly Simonovich, Christian Meurer Xavier

WebKit
Available for: iPhone 11 and later, iPad Pro 12.9-inch 3rd generation
and later, iPad Pro 11-inch 1st generation and later, iPad Air 3rd
generation and later, iPad 8th generation and later, and iPad mini 5th
generation and later
Impact: A malicious website may exfiltrate data cross-origin
Description: The issue was addressed with improved checks.
WebKit Bugzilla: 313357
CVE-2026-43735: Merrick Hare, Drinor Selmanaj (Sentry), Khai Tran, John
Lussier, Rhyru9, Kwak Kiyong, Song Nuri

WebKit
Available for: iPhone 11 and later, iPad Pro 12.9-inch 3rd generation
and later, iPad Pro 11-inch 1st generation and later, iPad Air 3rd
generation and later, iPad 8th generation and later, and iPad mini 5th
generation and later
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
Available for: iPhone 11 and later, iPad Pro 12.9-inch 3rd generation
and later, iPad Pro 11-inch 1st generation and later, iPad Air 3rd
generation and later, iPad 8th generation and later, and iPad mini 5th
generation and later
Impact: Processing maliciously crafted web content may disclose
sensitive user information
Description: A path handling issue was addressed with improved
validation.
WebKit Bugzilla: 313085
CVE-2026-43732: Nan Wang (@eternalsakura13)

WebKit
Available for: iPhone 11 and later, iPad Pro 12.9-inch 3rd generation
and later, iPad Pro 11-inch 1st generation and later, iPad Air 3rd
generation and later, iPad 8th generation and later, and iPad mini 5th
generation and later
Impact: Processing maliciously crafted web content may lead to memory
corruption
Description: A use-after-free issue was addressed with improved memory
management.
WebKit Bugzilla: 314115
CVE-2026-43731: dr3dd
WebKit Bugzilla: 313577
CVE-2026-43715: Milad Nasr and Nicholas Carlini with Claude, Anthropic

WebKit
Available for: iPhone 11 and later, iPad Pro 12.9-inch 3rd generation
and later, iPad Pro 11-inch 1st generation and later, iPad Air 3rd
generation and later, iPad 8th generation and later, and iPad mini 5th
generation and later
Impact: Processing maliciously crafted web content may lead to an
unexpected Safari crash
Description: A use-after-free issue was addressed with improved memory
management.
WebKit Bugzilla: 313691
CVE-2026-43727: Tommy DeVoss from Braze Security Team (@thedawgyg), Gia
Bui (@yabeow) from Calif.io,...