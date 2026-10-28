---
title: APPLE-SA-10-26-2026-10 Safari 27.2
url: https://seclists.org/fulldisclosure/2026/Oct/47
source: Full Disclosure
date: 2026-10-27
fetch_date: 2026-10-28T07:49:40.019027
---

# APPLE-SA-10-26-2026-10 Safari 27.2

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

[![Previous](/images/left-icon-16x16.png)](46)
[By Date](date.html#47)
[![Next](/images/right-icon-16x16.png)](48)

[![Previous](/images/left-icon-16x16.png)](46)
[By Thread](index.html#47)
![Next](/images/right-icon-16x16.png)

![](/shared/images/nst-icons.svg#search)

# APPLE-SA-10-26-2026-10 Safari 27.2

---

*From*: Apple Product Security via Fulldisclosure <fulldisclosure () seclists org>
*Date*: Mon, 26 Oct 2026 14:43:33 -0700

---

```
-----BEGIN PGP SIGNED MESSAGE-----
Hash: SHA256

APPLE-SA-10-26-2026-10 Safari 27.2

Safari 27.2 addresses the following issues.
Information about the security content is also available at
https://support.apple.com/149527.

Apple maintains a Security Releases page at
https://support.apple.com/100100 which lists recent
software updates with security advisories.

LinkPresentation
Available for: macOS Sequoia and macOS Tahoe
Impact: Processing a maliciously crafted image may result in memory
corruption
Description: An out-of-bounds write issue was addressed with improved
bounds checking.
CVE-2026-112621: Vinay Kumar Rasala (Xplo8E) from Appknox, an anonymous
researcher

WebKit
Available for: macOS Sequoia and macOS Tahoe
Impact: Processing maliciously crafted web content may lead to an
unexpected process crash
Description: A use-after-free issue was addressed with improved memory
management.
WebKit Bugzilla: 328114
CVE-2026-113904: Lily Cohl (@GenericCoding), Do Young Park (adawn),
MYUNGYONG LEE, Luke Francis (@lukefr09), Shubham Chaskar, Kwak Kiyong,
Song Nuri
WebKit Bugzilla: 317465
CVE-2026-112599: Avinash Kumar Thapa & Jay Kaushik Patel

WebKit
Available for: macOS Sequoia and macOS Tahoe
Impact: Processing maliciously crafted web content may lead to memory
corruption
Description: A type confusion issue was addressed with improved checks.
WebKit Bugzilla: 321609
CVE-2026-86974: Hossein Lotfi (@hosselot) of TrendAI Zero Day Initiative

WebKit
Available for: macOS Sequoia and macOS Tahoe
Impact: Processing maliciously crafted web content may lead to an
unexpected Safari crash
Description: A use-after-free issue was addressed with improved memory
management.
WebKit Bugzilla: 318331
CVE-2026-86986: an anonymous researcher
WebKit Bugzilla: 328131
CVE-2026-112693: 은태 장

WebKit
Available for: macOS Sequoia and macOS Tahoe
Impact: Processing maliciously crafted web content may lead to an
unexpected process crash
Description: This issue was addressed with improved input validation.
WebKit Bugzilla: 318522
CVE-2026-86985: Pasquale Scola

WebKit
Available for: macOS Sequoia and macOS Tahoe
Impact: Processing maliciously crafted web content may result in the
disclosure of process memory
Description: An out-of-bounds read was addressed with improved bounds
checking.
WebKit Bugzilla: 323130
CVE-2026-112699: an anonymous researcher
WebKit Bugzilla: 323148
CVE-2026-112680: Franz Bettag, Kwak Kiyong, Song Nuri

WebKit
Available for: macOS Sequoia and macOS Tahoe
Impact: Processing maliciously crafted web content may lead to arbitrary
code execution
Description: A use-after-free issue was addressed with improved memory
management.
WebKit Bugzilla: 322916
CVE-2026-112697: OpenAI Codex Security - Amy Burnett, 은태 장
WebKit Bugzilla: 324150
CVE-2026-112655: Euntae Jang
WebKit Bugzilla: 322120
CVE-2026-112651: Euntae Jang
WebKit Bugzilla: 323265
CVE-2026-112623: pwn2addr, Lily Cohl (@GenericCoding)

WebKit
Available for: macOS Sequoia and macOS Tahoe
Impact: Processing maliciously crafted web content may lead to an
unexpected process termination
Description: A race condition was addressed with improved locking.
WebKit Bugzilla: 323986
CVE-2026-112686: an anonymous researcher

WebKit
Available for: macOS Sequoia and macOS Tahoe
Impact: Processing maliciously crafted web content may lead to an
unexpected process crash
Description: This issue was addressed through improved state management.
WebKit Bugzilla: 328132
CVE-2026-112684: Gia Bui (@yabeow) from Calif.io

WebKit
Available for: macOS Sequoia and macOS Tahoe
Impact: Processing maliciously crafted web content may lead to an
unexpected process termination
Description: A type confusion issue was addressed with improved state
handling.
WebKit Bugzilla: 322033
CVE-2026-112673: Myungyong Lee

WebKit
Available for: macOS Sequoia and macOS Tahoe
Impact: Processing maliciously crafted web content may lead to an
unexpected Safari crash
Description: A race condition was addressed with improved state
handling.
WebKit Bugzilla: 323173
CVE-2026-112669: remanone (@remanone_)

WebKit
Available for: macOS Sequoia and macOS Tahoe
Impact: Processing maliciously crafted web content may lead to an
unexpected process termination
Description: A use-after-free issue was addressed with improved memory
management.
WebKit Bugzilla: 322671
CVE-2026-112695: Josef Korbel (Citadelo), Luke Francis (@lukefr09)
WebKit Bugzilla: 321669
CVE-2026-112666: Luke Francis (@lukefr09)
WebKit Bugzilla: 321934
CVE-2026-112654: Charles Kern
WebKit Bugzilla: 323227
CVE-2026-112653: Malik M. (@m411k_)
WebKit Bugzilla: 324735
CVE-2026-112615: Chris Rohlf with Anthropic Research

WebKit
Available for: macOS Sequoia and macOS Tahoe
Impact: Processing maliciously crafted web content may lead to arbitrary
code execution
Description: A type confusion issue was addressed with improved memory
handling.
WebKit Bugzilla: 321982
CVE-2026-112659: OpenAI Codex Security - Amy Burnett, Chris Rohlf with
Anthropic Research

WebKit
Available for: macOS Sequoia and macOS Tahoe
Impact: Processing maliciously crafted web content may lead to memory
corruption
Description: A use-after-free issue was addressed with improved memory
management.
WebKit Bugzilla: 324262
CVE-2026-112640: an anonymous researcher

WebKit
Available for: macOS Sequoia and macOS Tahoe
Impact: A website may be able to use a media format that should be
restricted in Lockdown Mode
Description: A logic issue was addressed with improved checks.
WebKit Bugzilla: 324004
CVE-2026-113952: Drinor Selmanaj (Sentry)

WebKit
Available for: macOS Sequoia and macOS Tahoe
Impact: Processing maliciously crafted web content may lead to memory
corruption
Description: A type confusion issue was addressed with improved state
management.
WebKit Bugzilla: 323097
CVE-2026-113949: an anonymous researcher

WebKit
Available for: macOS Sequoia and macOS Tahoe
Impact: Processing maliciously crafted web content may lead to
unexpected memory modification
Description: A use-after-free issue was addressed with improved memory
management.
WebKit Bugzilla: 321652
CVE-2026-113903: Eddy Tsalolikhin, OpenAI Codex Security - Amy Burnett,
Lily Cohl (@GenericCoding)

WebKit Canvas
Available for: macOS Sequoia and macOS Tahoe
Impact: Processing maliciously crafted web content may lead to arbitrary
code execution
Description: A use-after-free issue was addressed with improved memory
management.
WebKit Bugzilla: 323377
CVE-2026-112637: Chris Rohlf with Anthropic Research, 은태 장

WebKit JavaScript Bindings
Available for: macOS Sequoia and macOS Tahoe
Impact: Processing maliciously crafted web content may lead to arbitrary
code execution
Description: A use-after-free issue was addressed with improved memory
management.
WebKit Bugzilla: 328141
CVE-2026-112626: Euntae Jang, Luke Francis (@lukefr09), Shubham Chaskar,
Josef Korbel (Citadelo)

WebKit Process Model
Available for: macOS Sequoia and macOS Tahoe
Impact: A remote attacker may be able to break out of Web Content
sandbox
Description: This issue was addressed by removing the vulnerable c...