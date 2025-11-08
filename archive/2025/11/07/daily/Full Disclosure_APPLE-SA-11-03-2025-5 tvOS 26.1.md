---
title: APPLE-SA-11-03-2025-5 tvOS 26.1
url: https://seclists.org/fulldisclosure/2025/Nov/6
source: Full Disclosure
date: 2025-11-07
fetch_date: 2025-11-08T03:06:38.570275
---

# APPLE-SA-11-03-2025-5 tvOS 26.1

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

[![Previous](/images/left-icon-16x16.png)](5)
[By Date](date.html#6)
[![Next](/images/right-icon-16x16.png)](7)

[![Previous](/images/left-icon-16x16.png)](5)
[By Thread](index.html#6)
[![Next](/images/right-icon-16x16.png)](7)

![](/shared/images/nst-icons.svg#search)

# APPLE-SA-11-03-2025-5 tvOS 26.1

---

*From*: Apple Product Security via Fulldisclosure <fulldisclosure () seclists org>
*Date*: Mon, 03 Nov 2025 17:32:32 -0800

---

```
-----BEGIN PGP SIGNED MESSAGE-----
Hash: SHA256

APPLE-SA-11-03-2025-5 tvOS 26.1

tvOS 26.1 addresses the following issues.
Information about the security content is also available at
https://support.apple.com/125637.

Apple maintains a Security Releases page at
https://support.apple.com/100100 which lists recent
software updates with security advisories.

Apple Neural Engine
Available for: Apple TV 4K (2nd generation and later)
Impact: An app may be able to cause unexpected system termination or
corrupt kernel memory
Description: The issue was addressed with improved memory handling.
CVE-2025-43462: an anonymous researcher

AppleMobileFileIntegrity
Available for: Apple TV HD and Apple TV 4K (all models)
Impact: An app may be able to access protected user data
Description: This issue was addressed with improved validation of
symlinks.
CVE-2025-43379: Gergely Kalman (@gergely_kalman)

Assets
Available for: Apple TV HD and Apple TV 4K (all models)
Impact: An app may be able to break out of its sandbox
Description: This issue was addressed with improved entitlements.
CVE-2025-43407: JZ

CloudKit
Available for: Apple TV HD and Apple TV 4K (all models)
Impact: An app may be able to break out of its sandbox
Description: This issue was addressed with improved validation of
symlinks.
CVE-2025-43448: Hikerell (Loadshine Lab)

CoreServices
Available for: Apple TV HD and Apple TV 4K (all models)
Impact: An app may be able to enumerate a user's installed apps
Description: A permissions issue was addressed with additional
restrictions.
CVE-2025-43436: Zhongcheng Li from IES Red Team of ByteDance

CoreText
Available for: Apple TV HD and Apple TV 4K (all models)
Impact: Processing a maliciously crafted media file may lead to
unexpected app termination or corrupt process memory
Description: An out-of-bounds read was addressed with improved input
validation.
CVE-2025-43445: Hossein Lotfi (@hosselot) of Trend Micro Zero Day
Initiative

FontParser
Available for: Apple TV HD and Apple TV 4K (all models)
Impact: Processing a maliciously crafted font may lead to unexpected app
termination or corrupt process memory
Description: An out-of-bounds write issue was addressed with improved
bounds checking.
CVE-2025-43400: Apple

Installer
Available for: Apple TV HD and Apple TV 4K (all models)
Impact: An app may be able to fingerprint the user
Description: A permissions issue was addressed with additional
restrictions.
CVE-2025-43444: Zhongcheng Li from IES Red Team of ByteDance

Kernel
Available for: Apple TV HD and Apple TV 4K (all models)
Impact: An app may be able to cause unexpected system termination
Description: The issue was addressed with improved memory handling.
CVE-2025-43398: Cristian Dinca (icmd.tech)

libxpc
Available for: Apple TV HD and Apple TV 4K (all models)
Impact: A sandboxed app may be able to observe system-wide network
connections
Description: An access issue was addressed with additional sandbox
restrictions.
CVE-2025-43413: Dave G. and Alex Radocea of supernetworks.org

MallocStackLogging
Available for: Apple TV HD and Apple TV 4K (all models)
Impact: An app may be able to access sensitive user data
Description: An issue existed in the handling of environment variables.
This issue was addressed with improved validation.
CVE-2025-43294: Gergely Kalman (@gergely_kalman)

Model I/O
Available for: Apple TV HD and Apple TV 4K (all models)
Impact: Processing a maliciously crafted media file may lead to
unexpected app termination or corrupt process memory
Description: An out-of-bounds access issue was addressed with improved
bounds checking.
CVE-2025-43386: Michael DePlante (@izobashi) of Trend Micro Zero Day
Initiative
CVE-2025-43385: Michael DePlante (@izobashi) of Trend Micro Zero Day
Initiative
CVE-2025-43384: Michael DePlante (@izobashi) of Trend Micro Zero Day
Initiative
CVE-2025-43383: Michael DePlante (@izobashi) of Trend Micro Zero Day
Initiative

WebKit
Available for: Apple TV HD and Apple TV 4K (all models)
Impact: A malicious website may exfiltrate data cross-origin
Description: The issue was addressed with improved checks.
WebKit Bugzilla: 276208
CVE-2025-43480: Aleksejs Popovs

WebKit
Available for: Apple TV HD and Apple TV 4K (all models)
Impact: Processing maliciously crafted web content may lead to an
unexpected process crash
Description: This issue was addressed through improved state management.
WebKit Bugzilla: 296693
CVE-2025-43458: Phil Beauvoir
WebKit Bugzilla: 298196
CVE-2025-43430: Google Big Sleep
WebKit Bugzilla: 298628
CVE-2025-43427: Gary Kwong, rheza (@ginggilBesel)

WebKit
Available for: Apple TV HD and Apple TV 4K (all models)
Impact: Processing maliciously crafted web content may lead to an
unexpected process crash
Description: This issue was addressed with improved checks.
WebKit Bugzilla: 299843
CVE-2025-43443: an anonymous researcher

WebKit
Available for: Apple TV HD and Apple TV 4K (all models)
Impact: Processing maliciously crafted web content may lead to an
unexpected process crash
Description: The issue was addressed with improved memory handling.
WebKit Bugzilla: 298496
CVE-2025-43441: rheza (@ginggilBesel)
WebKit Bugzilla: 299391
CVE-2025-43435: Justin Cohen of Google
WebKit Bugzilla: 298851
CVE-2025-43425: an anonymous researcher

WebKit
Available for: Apple TV HD and Apple TV 4K (all models)
Impact: Processing maliciously crafted web content may lead to an
unexpected process crash
Description: This issue was addressed with improved checks
WebKit Bugzilla: 298126
CVE-2025-43440: Nan Wang (@eternalsakura13)

WebKit
Available for: Apple TV HD and Apple TV 4K (all models)
Impact: Processing maliciously crafted web content may lead to memory
corruption
Description: The issue was addressed with improved memory handling.
WebKit Bugzilla: 298093
CVE-2025-43433: Google Big Sleep
WebKit Bugzilla: 298194
CVE-2025-43431: Google Big Sleep

WebKit
Available for: Apple TV HD and Apple TV 4K (all models)
Impact: Processing maliciously crafted web content may lead to an
unexpected process crash
Description: A use-after-free issue was addressed with improved memory
management.
WebKit Bugzilla: 299313
CVE-2025-43432: Hossein Lotfi (@hosselot) of Trend Micro Zero Day
Initiative

WebKit
Available for: Apple TV HD and Apple TV 4K (all models)
Impact: Processing maliciously crafted web content may lead to an
unexpected process crash
Description: A buffer overflow was addressed with improved bounds
checking.
WebKit Bugzilla: 298232
CVE-2025-43429: Google Big Sleep

WebKit Canvas
Available for: Apple TV HD and Apple TV 4K (all models)
Impact: A website may exfiltrate image data cross-origin
Description: The issue was addressed with improved handling of caches.
WebKit Bugzilla: 297566
CVE-2025-43392: Tom Van Goethem

Additional recognition

MobileInstallation
We would like to acknowledge Bubble Zhang for their assistance.

WebKit
We would like to acknowledge Enis Maholli (enismaholli.com), Google Big
Sleep for their assistance.

Apple TV will periodically check for software updates. Alternatively,
you may manually check f...