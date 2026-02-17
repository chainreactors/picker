---
title: APPLE-SA-02-11-2026-2 iOS 18.7.5 and iPadOS 18.7.5
url: https://seclists.org/fulldisclosure/2026/Feb/22
source: Full Disclosure
date: 2026-02-16
fetch_date: 2026-02-17T04:21:56.530844
---

# APPLE-SA-02-11-2026-2 iOS 18.7.5 and iPadOS 18.7.5

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

# APPLE-SA-02-11-2026-2 iOS 18.7.5 and iPadOS 18.7.5

---

*From*: Apple Product Security via Fulldisclosure <fulldisclosure () seclists org>
*Date*: Wed, 11 Feb 2026 16:03:21 -0800

---

```
-----BEGIN PGP SIGNED MESSAGE-----
Hash: SHA256

APPLE-SA-02-11-2026-2 iOS 18.7.5 and iPadOS 18.7.5

iOS 18.7.5 and iPadOS 18.7.5 addresses the following issues.
Information about the security content is also available at
https://support.apple.com/126347.

Apple maintains a Security Releases page at
https://support.apple.com/100100 which lists recent
software updates with security advisories.

Accessibility
Available for: iPhone XS, iPhone XS Max, iPhone XR, iPad 7th generation
Impact: An attacker with physical access to a locked device may be able
to view sensitive user information
Description: An inconsistent user interface issue was addressed with
improved state management.
CVE-2026-20645: Loh Boon Keat

Books
Available for: iPhone XS, iPhone XS Max, iPhone XR, iPad 7th generation
Impact: Restoring a maliciously crafted backup file may lead to
modification of protected system files
Description: A path handling issue was addressed with improved
validation.
CVE-2025-43537: piffz, Daniel Nurkin, Sadman Adib, Mohamed Hamdadou &
Mahran Alhazmi, Hichem Maloufi, Christian Mina, Gerson Aldaz, qwerty j0y
& Ricardo Garcia, Dorian Del Valle

CFNetwork
Available for: iPhone XS, iPhone XS Max, iPhone XR, iPad 7th generation
Impact: A remote user may be able to write arbitrary files
Description: A path handling issue was addressed with improved logic.
CVE-2026-20660: Amy (amys.website)

CoreAudio
Available for: iPhone XS, iPhone XS Max, iPhone XR, iPad 7th generation
Impact: Processing a maliciously crafted media file may lead to
unexpected app termination or corrupt process memory
Description: An out-of-bounds access issue was addressed with improved
bounds checking.
CVE-2026-20611: Anonymous working with Trend Micro Zero Day Initiative

CoreMedia
Available for: iPhone XS, iPhone XS Max, iPhone XR, iPad 7th generation
Impact: Processing a maliciously crafted file may lead to a denial-of-
service or potentially disclose memory contents
Description: The issue was addressed with improved memory handling.
CVE-2026-20609: Yiğit Can YILMAZ (@yilmazcanyigit)

ImageIO
Available for: iPhone XS, iPhone XS Max, iPhone XR, iPad 7th generation
Impact: Processing a maliciously crafted image may result in disclosure
of process memory
Description: The issue was addressed with improved memory handling.
CVE-2026-20634: George Karchemsky (@gkarchemsky) working with Trend
Micro Zero Day Initiative

ImageIO
Available for: iPhone XS, iPhone XS Max, iPhone XR, iPad 7th generation
Impact: Processing a maliciously crafted image may lead to disclosure of
user information
Description: The issue was addressed with improved bounds checks.
CVE-2026-20675: George Karchemsky (@gkarchemsky) working with Trend
Micro Zero Day Initiative

Kernel
Available for: iPhone XS, iPhone XS Max, iPhone XR, iPad 7th generation
Impact: An attacker in a privileged network position may be able to
intercept network traffic
Description: A logic issue was addressed with improved checks.
CVE-2026-20671: Xin'an Zhou, Juefei Pu, Zhutian Liu, Zhiyun Qian,
Zhaowei Tan, Srikanth V. Krishnamurthy, Mathy Vanhoef

LaunchServices
Available for: iPhone XS, iPhone XS Max, iPhone XR, iPad 7th generation
Impact: An app may be able to enumerate a user's installed apps
Description: The issue was resolved by sanitizing logging.
CVE-2026-20663: Zhongcheng Li from IES Red Team

libexpat
Available for: iPhone XS, iPhone XS Max, iPhone XR, iPad 7th generation
Impact: Processing a maliciously crafted file may lead to a denial-of-
service
Description: This is a vulnerability in open source code and Apple
Software is among the affected projects. The CVE-ID was assigned by a
third party. Learn more about the issue and CVE-ID at cve.org.
CVE-2025-59375

libnetcore
Available for: iPhone XS, iPhone XS Max, iPhone XR, iPad 7th generation
Impact: An attacker in a privileged network position may be able to
intercept network traffic
Description: A logic issue was addressed with improved checks.
CVE-2026-20671: Xin'an Zhou, Juefei Pu, Zhutian Liu, Zhiyun Qian,
Zhaowei Tan, Srikanth V. Krishnamurthy, Mathy Vanhoef

Live Captions
Available for: iPhone XS, iPhone XS Max, iPhone XR, iPad 7th generation
Impact: An attacker with physical access to a locked device may be able
to view sensitive user information
Description: An authorization issue was addressed with improved state
management.
CVE-2026-20655: Richard Hyunho Im (@richeeta) at Route Zero Security
(routezero.security)

Mail
Available for: iPhone XS, iPhone XS Max, iPhone XR, iPad 7th generation
Impact: Turning off "Load remote content in messages” may not apply to
all mail previews
Description: A logic issue was addressed with improved checks.
CVE-2026-20673: an anonymous researcher

Messages
Available for: iPhone XS, iPhone XS Max, iPhone XR, iPad 7th generation
Impact: A shortcut may be able to bypass sandbox restrictions
Description: A race condition was addressed with improved handling of
symbolic links.
CVE-2026-20677: Ron Masas of BreakPoint.SH

Model I/O
Available for: iPhone XS, iPhone XS Max, iPhone XR, iPad 7th generation
Impact: Processing a maliciously crafted USD file may lead to unexpected
app termination
Description: An out-of-bounds write issue was addressed with improved
bounds checking.
CVE-2026-20616: Michael DePlante (@izobashi) of Trend Micro Zero Day
Initiative

Multi-Touch
Available for: iPhone XS, iPhone XS Max, iPhone XR, iPad 7th generation
Impact: A malicious HID device may cause an unexpected process crash
Description: The issue was addressed with improved bounds checks.
CVE-2025-43533: Google Threat Analysis Group
CVE-2025-46300: Google Threat Analysis Group
CVE-2025-46301: Google Threat Analysis Group
CVE-2025-46302: Google Threat Analysis Group
CVE-2025-46303: Google Threat Analysis Group
CVE-2025-46304: Google Threat Analysis Group
CVE-2025-46305: Google Threat Analysis Group

Safari
Available for: iPhone XS, iPhone XS Max, iPhone XR, iPad 7th generation
Impact: An app may be able to access a user's Safari history
Description: A logic issue was addressed with improved validation.
CVE-2026-20656: Mickey Jin (@patch1t)

Sandbox
Available for: iPhone XS, iPhone XS Max, iPhone XR, iPad 7th generation
Impact: An app may be able to break out of its sandbox
Description: A permissions issue was addressed with additional
restrictions.
CVE-2026-20628: Noah Gregory (wts.dev)

Sandbox Profiles
Available for: iPhone XS, iPhone XS Max, iPhone XR, iPad 7th generation
Impact: An app may be able to access sensitive user data
Description: An authorization issue was addressed with improved state
management.
CVE-2026-20678: Óscar García Pérez, Stanislav Jelezoglo

Screenshots
Available for: iPhone XS, iPhone XS Max, iPhone XR, iPad 7th generation
Impact: An attacker may be able to discover a user’s deleted notes
Description: A logic issue was addressed with improved state management.
CVE-2026-20682: Viktor Lord Härringtón

Shortcuts
Available for: iPhone XS, iPhone XS Max, iPhone XR, iPad 7th generation
Impact: An app may be able to ac...