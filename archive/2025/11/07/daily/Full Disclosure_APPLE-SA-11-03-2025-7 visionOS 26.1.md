---
title: APPLE-SA-11-03-2025-7 visionOS 26.1
url: https://seclists.org/fulldisclosure/2025/Nov/8
source: Full Disclosure
date: 2025-11-07
fetch_date: 2025-11-08T03:06:37.980942
---

# APPLE-SA-11-03-2025-7 visionOS 26.1

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

[![Previous](/images/left-icon-16x16.png)](7)
[By Date](date.html#8)
[![Next](/images/right-icon-16x16.png)](9)

[![Previous](/images/left-icon-16x16.png)](7)
[By Thread](index.html#8)
[![Next](/images/right-icon-16x16.png)](9)

![](/shared/images/nst-icons.svg#search)

# APPLE-SA-11-03-2025-7 visionOS 26.1

---

*From*: Apple Product Security via Fulldisclosure <fulldisclosure () seclists org>
*Date*: Mon, 03 Nov 2025 17:33:59 -0800

---

```
-----BEGIN PGP SIGNED MESSAGE-----
Hash: SHA256

APPLE-SA-11-03-2025-7 visionOS 26.1

visionOS 26.1 addresses the following issues.
Information about the security content is also available at
https://support.apple.com/125638.

Apple maintains a Security Releases page at
https://support.apple.com/100100 which lists recent
software updates with security advisories.

Apple Account
Available for: Apple Vision Pro (all models)
Impact: A malicious app may be able to take a screenshot of sensitive
information in embedded views
Description: A privacy issue was addressed with improved checks.
CVE-2025-43455: Ron Masas of BreakPoint.SH, Pinak Oza

Apple Neural Engine
Available for: Apple Vision Pro (all models)
Impact: An app may be able to cause unexpected system termination or
corrupt kernel memory
Description: The issue was addressed with improved memory handling.
CVE-2025-43447: an anonymous researcher
CVE-2025-43462: an anonymous researcher

AppleMobileFileIntegrity
Available for: Apple Vision Pro (all models)
Impact: An app may be able to access protected user data
Description: This issue was addressed with improved validation of
symlinks.
CVE-2025-43379: Gergely Kalman (@gergely_kalman)

Assets
Available for: Apple Vision Pro (all models)
Impact: An app may be able to break out of its sandbox
Description: This issue was addressed with improved entitlements.
CVE-2025-43407: JZ

Audio
Available for: Apple Vision Pro (all models)
Impact: An attacker with physical access to an unlocked device paired
with a Mac may be able to view sensitive user information in system
logging
Description: A logging issue was addressed with improved data redaction.
CVE-2025-43423: Duy Trần (@khanhduytran0)

CloudKit
Available for: Apple Vision Pro (all models)
Impact: An app may be able to break out of its sandbox
Description: This issue was addressed with improved validation of
symlinks.
CVE-2025-43448: Hikerell (Loadshine Lab)

CoreServices
Available for: Apple Vision Pro (all models)
Impact: An app may be able to enumerate a user's installed apps
Description: A permissions issue was addressed with additional
restrictions.
CVE-2025-43436: Zhongcheng Li from IES Red Team of ByteDance

CoreText
Available for: Apple Vision Pro (all models)
Impact: Processing a maliciously crafted media file may lead to
unexpected app termination or corrupt process memory
Description: An out-of-bounds read was addressed with improved input
validation.
CVE-2025-43445: Hossein Lotfi (@hosselot) of Trend Micro Zero Day
Initiative

FileProvider
Available for: Apple Vision Pro (all models)
Impact: An app may be able to access sensitive user data
Description: An authorization issue was addressed with improved state
management.
CVE-2025-43498: pattern-f (@pattern_F_)

Find My
Available for: Apple Vision Pro (all models)
Impact: An app may be able to fingerprint the user
Description: A privacy issue was addressed by moving sensitive data.
CVE-2025-43507: iisBuri

Installer
Available for: Apple Vision Pro (all models)
Impact: An app may be able to fingerprint the user
Description: A permissions issue was addressed with additional
restrictions.
CVE-2025-43444: Zhongcheng Li from IES Red Team of ByteDance

Kernel
Available for: Apple Vision Pro (all models)
Impact: An app may be able to cause unexpected system termination
Description: The issue was addressed with improved memory handling.
CVE-2025-43398: Cristian Dinca (icmd.tech)

libxpc
Available for: Apple Vision Pro (all models)
Impact: A sandboxed app may be able to observe system-wide network
connections
Description: An access issue was addressed with additional sandbox
restrictions.
CVE-2025-43413: Dave G. and Alex Radocea of supernetworks.org

Mail Drafts
Available for: Apple Vision Pro (all models)
Impact: Remote content may be loaded even when the 'Load Remote Images'
setting is turned off
Description: The issue was addressed by adding additional logic.
CVE-2025-43496: Romain Lebesle, Himanshu Bharti @Xpl0itme From Khatima

Model I/O
Available for: Apple Vision Pro (all models)
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

Notes
Available for: Apple Vision Pro (all models)
Impact: An app may be able to access sensitive user data
Description: A privacy issue was addressed by removing the vulnerable
code.
CVE-2025-43389: Kirin (@Pwnrin)

On-device Intelligence
Available for: Apple Vision Pro (all models)
Impact: An app may be able to fingerprint the user
Description: A privacy issue was addressed by removing sensitive data.
CVE-2025-43439: Zhongcheng Li from IES Red Team of ByteDance

Safari
Available for: Apple Vision Pro (all models)
Impact: Visiting a malicious website may lead to address bar spoofing
Description: The issue was addressed with improved checks.
CVE-2025-43493: @RenwaX23

Safari
Available for: Apple Vision Pro (all models)
Impact: Visiting a malicious website may lead to user interface spoofing
Description: An inconsistent user interface issue was addressed with
improved state management.
CVE-2025-43503: @RenwaX23

Safari
Available for: Apple Vision Pro (all models)
Impact: An app may be able to bypass certain Privacy preferences
Description: A privacy issue was addressed by removing sensitive data.
CVE-2025-43502: an anonymous researcher

Sandbox Profiles
Available for: Apple Vision Pro (all models)
Impact: An app may be able to access sensitive user data
Description: A privacy issue was addressed with improved handling of
user preferences.
CVE-2025-43500: Stanislav Jelezoglo

WebKit
Available for: Apple Vision Pro (all models)
Impact: A malicious website may exfiltrate data cross-origin
Description: The issue was addressed with improved checks.
WebKit Bugzilla: 276208
CVE-2025-43480: Aleksejs Popovs

WebKit
Available for: Apple Vision Pro (all models)
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
Available for: Apple Vision Pro (all models)
Impact: Processing maliciously crafted web content may lead to an
unexpected process crash
Description: This issue was addressed with improved checks.
WebKit Bugzilla: 299843
CVE-2025-43443: an anonymous researcher

WebKit
Available for: Apple Vision Pro (all models)
Impact: Processing maliciously crafted web content may lead to an
unexpected process crash
Description: The issue was addressed wi...