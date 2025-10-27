---
title: APPLE-SA-2023-01-23-1 iOS 16.3 and iPadOS 16.3
url: https://seclists.org/fulldisclosure/2023/Jan/15
source: Full Disclosure
date: 2023-01-25
fetch_date: 2025-10-04T04:48:40.630994
---

# APPLE-SA-2023-01-23-1 iOS 16.3 and iPadOS 16.3

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

[![Previous](/images/left-icon-16x16.png)](14)
[By Date](date.html#15)
[![Next](/images/right-icon-16x16.png)](16)

[![Previous](/images/left-icon-16x16.png)](14)
[By Thread](index.html#15)
[![Next](/images/right-icon-16x16.png)](16)

![](/shared/images/nst-icons.svg#search)

# APPLE-SA-2023-01-23-1 iOS 16.3 and iPadOS 16.3

---

*From*: Apple Product Security via Fulldisclosure <fulldisclosure () seclists org>
*Date*: Mon, 23 Jan 2023 18:40:27 -0800

---

```
-----BEGIN PGP SIGNED MESSAGE-----
Hash: SHA256

APPLE-SA-2023-01-23-1 iOS 16.3 and iPadOS 16.3

iOS 16.3 and iPadOS 16.3 addresses the following issues.
Information about the security content is also available at
https://support.apple.com/HT213606.

AppleMobileFileIntegrity
Available for: iPhone 8 and later, iPad Pro (all models), iPad Air
3rd generation and later, iPad 5th generation and later, and iPad
mini 5th generation and later
Impact: An app may be able to access user-sensitive data
Description: This issue was addressed by enabling hardened runtime.
CVE-2023-23499: Wojciech Reguła (@_r3ggi) of SecuRing
(wojciechregula.blog)

ImageIO
Available for: iPhone 8 and later, iPad Pro (all models), iPad Air
3rd generation and later, iPad 5th generation and later, and iPad
mini 5th generation and later
Impact: Processing an image may lead to a denial-of-service
Description: A memory corruption issue was addressed with improved
state management.
CVE-2023-23519: Yiğit Can YILMAZ (@yilmazcanyigit)

Kernel
Available for: iPhone 8 and later, iPad Pro (all models), iPad Air
3rd generation and later, iPad 5th generation and later, and iPad
mini 5th generation and later
Impact: An app may be able to leak sensitive kernel state
Description: The issue was addressed with improved memory handling.
CVE-2023-23500: Pan ZhenPeng (@Peterpan0927) of STAR Labs SG Pte.
Ltd. (@starlabs_sg)

Kernel
Available for: iPhone 8 and later, iPad Pro (all models), iPad Air
3rd generation and later, iPad 5th generation and later, and iPad
mini 5th generation and later
Impact: An app may be able to determine kernel memory layout
Description: An information disclosure issue was addressed by
removing the vulnerable code.
CVE-2023-23502: Pan ZhenPeng (@Peterpan0927) of STAR Labs SG Pte.
Ltd. (@starlabs_sg)

Kernel
Available for: iPhone 8 and later, iPad Pro (all models), iPad Air
3rd generation and later, iPad 5th generation and later, and iPad
mini 5th generation and later
Impact: An app may be able to execute arbitrary code with kernel
privileges
Description: The issue was addressed with improved memory handling.
CVE-2023-23504: Adam Doupé of ASU SEFCOM

Mail Drafts
Available for: iPhone 8 and later, iPad Pro (all models), iPad Air
3rd generation and later, iPad 5th generation and later, and iPad
mini 5th generation and later
Impact: The quoted original message may be selected from the wrong
email when forwarding an email from an Exchange account
Description: A logic issue was addressed with improved state
management.
CVE-2023-23498: an anonymous researcher

Maps
Available for: iPhone 8 and later, iPad Pro (all models), iPad Air
3rd generation and later, iPad 5th generation and later, and iPad
mini 5th generation and later
Impact: An app may be able to bypass Privacy preferences
Description: A logic issue was addressed with improved state
management.
CVE-2023-23503: an anonymous researcher

Safari
Available for: iPhone 8 and later, iPad Pro (all models), iPad Air
3rd generation and later, iPad 5th generation and later, and iPad
mini 5th generation and later
Impact: Visiting a website may lead to an app denial-of-service
Description: The issue was addressed with improved handling of
caches.
CVE-2023-23512: Adriatik Raci

Screen Time
Available for: iPhone 8 and later, iPad Pro (all models), iPad Air
3rd generation and later, iPad 5th generation and later, and iPad
mini 5th generation and later
Impact: An app may be able to access information about a user’s
contacts
Description: A privacy issue was addressed with improved private data
redaction for log entries.
CVE-2023-23505: Wojciech Reguła of SecuRing (wojciechregula.blog)

Weather
Available for: iPhone 8 and later, iPad Pro (all models), iPad Air
3rd generation and later, iPad 5th generation and later, and iPad
mini 5th generation and later
Impact: An app may be able to bypass Privacy preferences
Description: The issue was addressed with improved memory handling.
CVE-2023-23511: Wojciech Regula of SecuRing (wojciechregula.blog), an
anonymous researcher

WebKit
Available for: iPhone 8 and later, iPad Pro (all models), iPad Air
3rd generation and later, iPad 5th generation and later, and iPad
mini 5th generation and later
Impact: Processing maliciously crafted web content may lead to
arbitrary code execution
Description: The issue was addressed with improved checks.
WebKit Bugzilla: 245464
CVE-2023-23496: ChengGang Wu, Yan Kang, YuHao Hu, Yue Sun, Jiming
Wang, JiKai Ren and Hang Shu of Institute of Computing Technology,
Chinese Academy of Sciences

WebKit
Available for: iPhone 8 and later, iPad Pro (all models), iPad Air
3rd generation and later, iPad 5th generation and later, and iPad
mini 5th generation and later
Impact: Processing maliciously crafted web content may lead to
arbitrary code execution
Description: The issue was addressed with improved memory handling.
WebKit Bugzilla: 248268
CVE-2023-23518: YeongHyeon Choi (@hyeon101010), Hyeon Park
(@tree_segment), SeOk JEON (@_seokjeon), YoungSung Ahn (@_ZeroSung),
JunSeo Bae (@snakebjs0107), Dohyun Lee (@l33d0hyun) of Team ApplePIE
WebKit Bugzilla: 248268
CVE-2023-23517: YeongHyeon Choi (@hyeon101010), Hyeon Park
(@tree_segment), SeOk JEON (@_seokjeon), YoungSung Ahn (@_ZeroSung),
JunSeo Bae (@snakebjs0107), Dohyun Lee (@l33d0hyun) of Team ApplePIE

Additional recognition

Kernel
We would like to acknowledge Nick Stenning of Replicate for their
assistance.

Shortcuts
We would like to acknowledge Baibhav Anand Jha from ReconWithMe and
Cristian Dinca of Tudor Vianu National High School of Computer
Science, Romania for their assistance.

WebKit
We would like to acknowledge Eliya Stein of Confiant for their
assistance.

This update is available through iTunes and Software Update on your
iOS device, and will not appear in your computer's Software Update
application, or in the Apple Downloads site. Make sure you have an
Internet connection and have installed the latest version of iTunes
from https://www.apple.com/itunes/  iTunes and Software Update on the
device will automatically check Apple's update server on its weekly
schedule. When an update is detected, it is downloaded and the option
to be installed is presented to the user when the iOS device is
docked. We recommend applying the update immediately if possible.
Selecting Don't Install will present the option the next time you
connect your iOS device.  The automatic update process may take up to
a week depending on the day that iTunes or the device checks for
updates. You may manually obtain the update via the Check for Updates
button within iTunes, or the Software Update on your device.  To
check that the iPhone, iPod touch, or iPad has been updated:  *
Navigate to Settings * Select General * Select About. The version
after applying this update will be "iOS 16.3 and iPadOS 16.3".
All information is also posted on the Apple Security Updates
web site: https://support.apple.com/en-us/HT201222.

This message is signed with Apple's Product Security PGP key,
and details are available at:
https://ww...