---
title: APPLE-SA-11-03-2025-6 watchOS 26.1
url: https://seclists.org/fulldisclosure/2025/Nov/7
source: Full Disclosure
date: 2025-11-07
fetch_date: 2025-11-08T03:06:38.274218
---

# APPLE-SA-11-03-2025-6 watchOS 26.1

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

[![Previous](/images/left-icon-16x16.png)](6)
[By Date](date.html#7)
[![Next](/images/right-icon-16x16.png)](8)

[![Previous](/images/left-icon-16x16.png)](6)
[By Thread](index.html#7)
[![Next](/images/right-icon-16x16.png)](8)

![](/shared/images/nst-icons.svg#search)

# APPLE-SA-11-03-2025-6 watchOS 26.1

---

*From*: Apple Product Security via Fulldisclosure <fulldisclosure () seclists org>
*Date*: Mon, 03 Nov 2025 17:33:14 -0800

---

```
-----BEGIN PGP SIGNED MESSAGE-----
Hash: SHA256

APPLE-SA-11-03-2025-6 watchOS 26.1

watchOS 26.1 addresses the following issues.
Information about the security content is also available at
https://support.apple.com/125639.

Apple maintains a Security Releases page at
https://support.apple.com/100100 which lists recent
software updates with security advisories.

Apple Account
Available for: Apple Watch Series 6 and later
Impact: A malicious app may be able to take a screenshot of sensitive
information in embedded views
Description: A privacy issue was addressed with improved checks.
CVE-2025-43455: Ron Masas of BreakPoint.SH, Pinak Oza

Apple Neural Engine
Available for: Apple Watch Series 9 and later, Apple Watch SE 2nd
generation, Apple Watch Ultra (all models)
Impact: An app may be able to cause unexpected system termination or
corrupt kernel memory
Description: The issue was addressed with improved memory handling.
CVE-2025-43447: an anonymous researcher
CVE-2025-43462: an anonymous researcher

AppleMobileFileIntegrity
Available for: Apple Watch Series 6 and later
Impact: An app may be able to access protected user data
Description: This issue was addressed with improved validation of
symlinks.
CVE-2025-43379: Gergely Kalman (@gergely_kalman)

CloudKit
Available for: Apple Watch Series 6 and later
Impact: An app may be able to break out of its sandbox
Description: This issue was addressed with improved validation of
symlinks.
CVE-2025-43448: Hikerell (Loadshine Lab)

CoreServices
Available for: Apple Watch Series 6 and later
Impact: An app may be able to enumerate a user's installed apps
Description: A permissions issue was addressed with additional
restrictions.
CVE-2025-43436: Zhongcheng Li from IES Red Team of ByteDance

CoreText
Available for: Apple Watch Series 6 and later
Impact: Processing a maliciously crafted media file may lead to
unexpected app termination or corrupt process memory
Description: An out-of-bounds read was addressed with improved input
validation.
CVE-2025-43445: Hossein Lotfi (@hosselot) of Trend Micro Zero Day
Initiative

Find My
Available for: Apple Watch Series 6 and later
Impact: An app may be able to fingerprint the user
Description: A privacy issue was addressed by moving sensitive data.
CVE-2025-43507: iisBuri

FontParser
Available for: Apple Watch Series 6 and later
Impact: Processing a maliciously crafted font may lead to unexpected app
termination or corrupt process memory
Description: An out-of-bounds write issue was addressed with improved
bounds checking.
CVE-2025-43400: Apple

Installer
Available for: Apple Watch Series 6 and later
Impact: An app may be able to fingerprint the user
Description: A permissions issue was addressed with additional
restrictions.
CVE-2025-43444: Zhongcheng Li from IES Red Team of ByteDance

Kernel
Available for: Apple Watch Series 6 and later
Impact: An app may be able to cause unexpected system termination
Description: The issue was addressed with improved memory handling.
CVE-2025-43398: Cristian Dinca (icmd.tech)

libxpc
Available for: Apple Watch Series 6 and later
Impact: A sandboxed app may be able to observe system-wide network
connections
Description: An access issue was addressed with additional sandbox
restrictions.
CVE-2025-43413: Dave G. and Alex Radocea of supernetworks.org

Mail Drafts
Available for: Apple Watch Series 6 and later
Impact: Remote content may be loaded even when the 'Load Remote Images'
setting is turned off
Description: The issue was addressed by adding additional logic.
CVE-2025-43496: Romain Lebesle, Himanshu Bharti @Xpl0itme From Khatima

MallocStackLogging
Available for: Apple Watch Series 6 and later
Impact: An app may be able to access sensitive user data
Description: An issue existed in the handling of environment variables.
This issue was addressed with improved validation.
CVE-2025-43294: Gergely Kalman (@gergely_kalman)

Phone
Available for: Apple Watch Series 6 and later
Impact: An attacker with physical access to a locked Apple Watch may be
able to view Live Voicemail
Description: An authentication issue was addressed with improved state
management.
CVE-2025-43459: Dalibor Milanovic

Safari
Available for: Apple Watch Series 6 and later
Impact: Visiting a malicious website may lead to user interface spoofing
Description: An inconsistent user interface issue was addressed with
improved state management.
CVE-2025-43503: @RenwaX23

Sandbox Profiles
Available for: Apple Watch Series 6 and later
Impact: An app may be able to access sensitive user data
Description: A privacy issue was addressed with improved handling of
user preferences.
CVE-2025-43500: Stanislav Jelezoglo

WebKit
Available for: Apple Watch Series 6 and later
Impact: A malicious website may exfiltrate data cross-origin
Description: The issue was addressed with improved checks.
WebKit Bugzilla: 276208
CVE-2025-43480: Aleksejs Popovs

WebKit
Available for: Apple Watch Series 6 and later
Impact: Processing maliciously crafted web content may lead to an
unexpected process crash
Description: This issue was addressed through improved state management.
WebKit Bugzilla: 296693
CVE-2025-43458: Phil Beauvoir
WebKit Bugzilla: 298196
CVE-2025-43430: Google Big Sleep

WebKit
Available for: Apple Watch Series 6 and later
Impact: Processing maliciously crafted web content may lead to an
unexpected process crash
Description: This issue was addressed with improved checks.
WebKit Bugzilla: 299843
CVE-2025-43443: an anonymous researcher

WebKit
Available for: Apple Watch Series 6 and later
Impact: Processing maliciously crafted web content may lead to an
unexpected process crash
Description: This issue was addressed with improved checks
WebKit Bugzilla: 298126
CVE-2025-43440: Nan Wang (@eternalsakura13)

WebKit
Available for: Apple Watch Series 6 and later
Impact: Processing maliciously crafted web content may lead to an
unexpected Safari crash
Description: A use-after-free issue was addressed with improved memory
management.
WebKit Bugzilla: 297662
CVE-2025-43438: shandikri working with Trend Micro Zero Day Initiative
WebKit Bugzilla: 298606
CVE-2025-43457: Gary Kwong, Hossein Lotfi (@hosselot) of Trend Micro
Zero Day Initiative
WebKit Bugzilla: 297958
CVE-2025-43434: Google Big Sleep

WebKit
Available for: Apple Watch Series 6 and later
Impact: Processing maliciously crafted web content may lead to an
unexpected process crash
Description: The issue was addressed with improved memory handling.
WebKit Bugzilla: 299391
CVE-2025-43435: Justin Cohen of Google
WebKit Bugzilla: 298851
CVE-2025-43425: an anonymous researcher

WebKit
Available for: Apple Watch Series 6 and later
Impact: Processing maliciously crafted web content may lead to memory
corruption
Description: The issue was addressed with improved memory handling.
WebKit Bugzilla: 298093
CVE-2025-43433: Google Big Sleep
WebKit Bugzilla: 298194
CVE-2025-43431: Google Big Sleep

WebKit
Available for: Apple Watch Series 6 and later
Impact: Processing maliciously crafted web content may lead to an
unexpected process crash
Des...