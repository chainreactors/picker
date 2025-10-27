---
title: Apple web content filter bypass allows unrestricted access to blocked content (macOS/iOS/iPadOS/visionOS/watchOS)
url: https://seclists.org/fulldisclosure/2024/Nov/6
source: Full Disclosure
date: 2024-11-22
fetch_date: 2025-10-06T19:23:08.563161
---

# Apple web content filter bypass allows unrestricted access to blocked content (macOS/iOS/iPadOS/visionOS/watchOS)

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

# Apple web content filter bypass allows unrestricted access to blocked content (macOS/iOS/iPadOS/visionOS/watchOS)

---

*From*: Nosebeard Labs <labs () nosebeard co>
*Date*: Fri, 15 Nov 2024 22:17:54 +0100

---

```
Dear colleagues,
```

Nosebeard Labs is pleased to share its latest advisory, detailing a
bypass of Apple's system wide web content filter. The HTML version of
this advisory is also available at:

```
https://nosebeard.co/advisories/nbl-001.html

Warmest regards,
Nosebeard Labs

## Summary
Nosebeard Labs Security Advisory NBL-001
```

Title: Apple web content filter bypass allows unrestricted access to
blocked content (macOS/iOS/iPadOS/visionOS/watchOS)

```
Advisory ID: NBL-001
Date: 2024-11-15
Severity: Critical (CVSS 9.1)
Affected Product: Safari on any Apple device with Screen Time enabled
CVE ID: CVE-2024-44206

## Overview
```

Nosebeard Labs has identified a critical vulnerability in Apple’s system
wide web content filter that allows a full bypass of content
restrictions. This vulnerability, which occurs specifically when Screen
Time’s content filtering settings are enabled, permits users or
attackers to access restricted websites in Safari without detection. By
exploiting a misalignment between Screen Time’s Access Control List
(ACL) and WebKit’s URI validation, a specially crafted URI can
circumvent both layers of protection.
Apple has assigned CVE-2024-44206 to this issue and issued a fix for
macOS Sonoma 14.x, iOS/iPadOS 17.x, watchOS 10.x, visionOS 1.x, Safari
17.x and up.

```
However, a fix is still pending for the backport channels.

## Description
```

This vulnerability arises when the WebKit Cocoa layer in Safari ingests
a URI without performing comprehensive validation, combined with a
failure by the Screen Time ACL filter to recognize and block the
malformed URI. The flaw allows a crafted URI to bypass all Screen Time
content filtering settings, including deny/allow lists and parental
content filters, providing unrestricted access to blocked content.

```
## Affected Systems
```

This vulnerability affects all devices on macOS, iOS, iPadOS, watchOS
and visionOS platforms with Safari and Screen Time enabled, impacting an
estimated 250 million devices globally.

```
## Attack Scenarios
The vulnerability can be exploited both locally and remotely:
```

1. Local Exploitation: Users can manipulate the address bar to manually
enter a crafted URI, bypassing Screen Time restrictions.
2. Network-Based Exploitation: Attackers can load restricted content
remotely by embedding a crafted URI within an iframe, bypassing
restrictions without requiring user interaction.

```
## Impact
```

1. Confidentiality: Unrestricted access to restricted websites
compromises the confidentiality of content filtering controls,
potentially exposing sensitive or inappropriate material.
2. Scope and Integrity: This vulnerability spans across two separate
security mechanisms (Screen Time and WebKit), representing a critical
architecture-level issue. Additionally, accessing unsecured or unlogged
resources poses potential integrity risks.

```
## CVSS Score
Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:C/C:H/I:L/A:N
Score: 9.1 (Critical)

## Mitigations
```

Upgrade to the latest iOS/iPadOS 17.x or 18.x / macOS Sonoma 14.x /
visionOS 1.x / watchOS 10.x / Safari 17.6 respectively. Users who are
unable to apply a fix can contact us for more info.

```
## Vendor Response
```

Apple has issued CVE-2024-44206 and supplied a fix within WebKit;
however, a fix remains pending for iOS/iPadOS version 16.x. We recommend
that Apple undertake further review to address the issue comprehensively.

```
## Timeline
–
Milestone:
2020-11-24 Vulnerability discovered internally at NBL
–
Milestone:
2021-03-08 Initial disclosure to Apple Product Security
–
```

2021-03-09 Apple Product Security recommends to open a bug report on
Feedback Assistant
2021-03-10 We opened a bug report on Feedback Assistant as advised by
Apple Product Security
2021-03-15 We follow-up by adding additional info to the open bug report
on F.A.
2021-08-16 We follow-up again referring Apple Product Security to open
ticket, stressing that the issue can be also demonstrated in their EU
Apple Stores
2021-08-24 We follow-up again to Apple Product Security, referring to
the previous follow-up
2021-08-25 Rejected by Apple Security - “We do not see any actual
security implications. We recommended reporting this issue via Feedback
Assistant”
2024-03-18 NBL submits a second report 3 years later to appeal via Apple
Security Bounty Program, urging to re-evaluate, also providing PoC code
2024-03-19 Apple Security Research closes report - “We’re unable to
identify a security issue in your report” - “Screen Time is not intended
to protect a device against manipulation” - “We recommend reporting this
via Feedback Assistant”
2024-04-02 Status of Bug Report on F.A. from 2021-03-10 “Open, Similar
Reports None”
2024-04-03 We follow-up again asking Apple Security for a final
reassessment, providing a temporary workaround
2024-04-03 Apple Security recommends opening a bug report - “ST is not
intended to protect a device against manipulation” - “MDM profiles
provide configuration management but do not establish additional
security boundaries beyond what iOS and iPadOS have to offer.”

```
2024-05-05 Initial contact with Joanna Stern of WSJ
```

2024-05-06 Referring PSIRT ticket # directly to an Apple PSIRT contact
via undisclosed SOC - no response

```
2024-05-28 Joanna Stern/WSJ runs Apple through this
2024-05-29 Apple commits patches to Safari branch
–
Milestone:
```

2024-06-05 Wall Street Journal addresses our finding in their article “A
Bug Allowed Kids to Visit X-Rated Sites. Apple Took Three Years to Fix
It.” by Joanna Stern

```
–
```

2024-06-18 We follow-up again with Urgent request for re-evaluation to
Apple Product Security (“Addendum”)
2024-06-27 We follow-up on our follow-up Update Request Screen Time
Security Vulnerability Report (“Follow-Up”)

```
2024-07-23 Apple releases fix in iOS 17.6RC et al.
```

2024-07-26 Letter to Apple welcoming first fix, reiterating our
dedication to Responsible Disclosure, intended to coordinate further
disclosure process and close the affair asking them to give credit and
align to their SBP

```
–
Milestone:
```

2024-07-29 Apple releases fixes for macOS Sonoma 14.6, iOS/iPadOS 17.6,
watchOS 10.6, visionOS 1.3 and Safari 17.6, leaving iOS/iPadOS 16.x
still affected.

```
–
```

2024-07-31 Apple responds “ST is not intended to protect a device from
malicious manipulation, and bug reports on features like this are
therefore typically ineligible for credit or Apple Security Bounty
award. However, we’d like to make an exception and award you USD (...)\*
as a thank you for your report. Also, we’d like to credit you on our
security advisory under the ‘Additional recognition’ section of the
page.” \*We were offered the minimum possible amount.
2024-08-01 We inquire about the bounty amount asking Apple to “comment
on our proposed evaluation under the CVSS metrics, sharing with us their
transparent assessment of the vulnerability under the terms and broad
criteria of the bounty program.”
2024-08-01 Apple “appreciates our suggestions, but CVSS s...