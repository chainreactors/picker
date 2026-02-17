---
title: APPLE-SA-02-11-2026-1 iOS 26.3 and iPadOS 26.3
url: https://seclists.org/fulldisclosure/2026/Feb/21
source: Full Disclosure
date: 2026-02-16
fetch_date: 2026-02-17T04:21:56.703595
---

# APPLE-SA-02-11-2026-1 iOS 26.3 and iPadOS 26.3

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

[![Previous](/images/left-icon-16x16.png)](20)
[By Date](date.html#21)
[![Next](/images/right-icon-16x16.png)](22)

[![Previous](/images/left-icon-16x16.png)](20)
[By Thread](index.html#21)
[![Next](/images/right-icon-16x16.png)](22)

![](/shared/images/nst-icons.svg#search)

# APPLE-SA-02-11-2026-1 iOS 26.3 and iPadOS 26.3

---

*From*: Apple Product Security via Fulldisclosure <fulldisclosure () seclists org>
*Date*: Wed, 11 Feb 2026 16:02:49 -0800

---

```
-----BEGIN PGP SIGNED MESSAGE-----
Hash: SHA256

APPLE-SA-02-11-2026-1 iOS 26.3 and iPadOS 26.3

iOS 26.3 and iPadOS 26.3 addresses the following issues.
Information about the security content is also available at
https://support.apple.com/126346.

Apple maintains a Security Releases page at
https://support.apple.com/100100 which lists recent
software updates with security advisories.

Accessibility
Available for: iPhone 11 and later, iPad Pro 12.9-inch 3rd generation
and later, iPad Pro 11-inch 1st generation and later, iPad Air 3rd
generation and later, iPad 8th generation and later, and iPad mini 5th
generation and later
Impact: An attacker with physical access to a locked device may be able
to view sensitive user information
Description: An inconsistent user interface issue was addressed with
improved state management.
CVE-2026-20645: Loh Boon Keat

Accessibility
Available for: iPhone 11 and later, iPad Pro 12.9-inch 3rd generation
and later, iPad Pro 11-inch 1st generation and later, iPad Air 3rd
generation and later, iPad 8th generation and later, and iPad mini 5th
generation and later
Impact: An attacker with physical access to a locked device may be able
to view sensitive user information
Description: A privacy issue was addressed by removing sensitive data.
CVE-2026-20674: Jacob Prezant (prezant.us)

Bluetooth
Available for: iPhone 11 and later, iPad Pro 12.9-inch 3rd generation
and later, iPad Pro 11-inch 1st generation and later, iPad Air 3rd
generation and later, iPad 8th generation and later, and iPad mini 5th
generation and later
Impact: An attacker in a privileged network position may be able to
perform denial-of-service attack using crafted Bluetooth packets
Description: A denial-of-service issue was addressed with improved
validation.
CVE-2026-20650: jioundai

Call History
Available for: iPhone 11 and later, iPad Pro 12.9-inch 3rd generation
and later, iPad Pro 11-inch 1st generation and later, iPad Air 3rd
generation and later, iPad 8th generation and later, and iPad mini 5th
generation and later
Impact: A user with Live Caller ID app extensions turned off could have
identifying information leaked to the extensions
Description: A logic issue was addressed with improved checks.
CVE-2026-20638: Nils Hanff (@nils1729@chaos.social) of Hasso Plattner
Institute

CFNetwork
Available for: iPhone 11 and later, iPad Pro 12.9-inch 3rd generation
and later, iPad Pro 11-inch 1st generation and later, iPad Air 3rd
generation and later, iPad 8th generation and later, and iPad mini 5th
generation and later
Impact: A remote user may be able to write arbitrary files
Description: A path handling issue was addressed with improved logic.
CVE-2026-20660: Amy (amys.website)

CoreAudio
Available for: iPhone 11 and later, iPad Pro 12.9-inch 3rd generation
and later, iPad Pro 11-inch 1st generation and later, iPad Air 3rd
generation and later, iPad 8th generation and later, and iPad mini 5th
generation and later
Impact: Processing a maliciously crafted media file may lead to
unexpected app termination or corrupt process memory
Description: An out-of-bounds access issue was addressed with improved
bounds checking.
CVE-2026-20611: Anonymous working with Trend Micro Zero Day Initiative

CoreMedia
Available for: iPhone 11 and later, iPad Pro 12.9-inch 3rd generation
and later, iPad Pro 11-inch 1st generation and later, iPad Air 3rd
generation and later, iPad 8th generation and later, and iPad mini 5th
generation and later
Impact: Processing a maliciously crafted file may lead to a denial-of-
service or potentially disclose memory contents
Description: The issue was addressed with improved memory handling.
CVE-2026-20609: Yiğit Can YILMAZ (@yilmazcanyigit)

CoreServices
Available for: iPhone 11 and later, iPad Pro 12.9-inch 3rd generation
and later, iPad Pro 11-inch 1st generation and later, iPad Air 3rd
generation and later, iPad 8th generation and later, and iPad mini 5th
generation and later
Impact: An app may be able to gain root privileges
Description: A race condition was addressed with improved state
handling.
CVE-2026-20617: Gergely Kalman (@gergely_kalman), Csaba Fitzl
(@theevilbit) of Iru

CoreServices
Available for: iPhone 11 and later, iPad Pro 12.9-inch 3rd generation
and later, iPad Pro 11-inch 1st generation and later, iPad Air 3rd
generation and later, iPad 8th generation and later, and iPad mini 5th
generation and later
Impact: An app may be able to gain root privileges
Description: A path handling issue was addressed with improved
validation.
CVE-2026-20615: Csaba Fitzl (@theevilbit) of Iru and Gergely Kalman
(@gergely_kalman)

CoreServices
Available for: iPhone 11 and later, iPad Pro 12.9-inch 3rd generation
and later, iPad Pro 11-inch 1st generation and later, iPad Air 3rd
generation and later, iPad 8th generation and later, and iPad mini 5th
generation and later
Impact: An app may be able to access sensitive user data
Description: An issue existed in the handling of environment variables.
This issue was addressed with improved validation.
CVE-2026-20627: an anonymous researcher

dyld
Available for: iPhone 11 and later, iPad Pro 12.9-inch 3rd generation
and later, iPad Pro 11-inch 1st generation and later, iPad Air 3rd
generation and later, iPad 8th generation and later, and iPad mini 5th
generation and later
Impact: An attacker with memory write capability may be able to execute
arbitrary code. Apple is aware of a report that this issue may have been
exploited in an extremely sophisticated attack against specific targeted
individuals on versions of iOS before iOS 26. CVE-2025-14174 and
CVE-2025-43529 were also issued in response to this report.
Description: A memory corruption issue was addressed with improved state
management.
CVE-2026-20700: Google Threat Analysis Group

Game Center
Available for: iPhone 11 and later, iPad Pro 12.9-inch 3rd generation
and later, iPad Pro 11-inch 1st generation and later, iPad Air 3rd
generation and later, iPad 8th generation and later, and iPad mini 5th
generation and later
Impact: A user may be able to view sensitive user information
Description: A logging issue was addressed with improved data redaction.
CVE-2026-20649: Asaf Cohen

ImageIO
Available for: iPhone 11 and later, iPad Pro 12.9-inch 3rd generation
and later, iPad Pro 11-inch 1st generation and later, iPad Air 3rd
generation and later, iPad 8th generation and later, and iPad mini 5th
generation and later
Impact: Processing a maliciously crafted image may lead to disclosure of
user information
Description: The issue was addressed with improved bounds checks.
CVE-2026-20675: George Karchemsky (@gkarchemsky) working with Trend
Micro Zero Day Initiative

ImageIO
Available for: iPhone 11 and later, iPad Pro 12.9-inch 3rd generation
and later, iPad Pro 11-inch 1st generation and later, iPad Air 3rd
generation and later, iPad 8th generation and later, and iPad mini 5th
generation and later
Impact: Processing a maliciously crafted image may result in disclosure
of process memory
Description: The issue was addresse...