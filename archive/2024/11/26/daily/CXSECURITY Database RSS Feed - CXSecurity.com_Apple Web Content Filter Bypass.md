---
title: Apple Web Content Filter Bypass
url: https://cxsecurity.com/issue/WLB-2024110035
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2024-11-26
fetch_date: 2025-10-06T19:17:07.127566
---

# Apple Web Content Filter Bypass

[![Home Page](https://cert.cx/cxstatic/images/12018/cxseci.png)](https://cxsecurity.com/)

* [Home](https://cxsecurity.com/)
* Bugtraq
  + [Full List](https://cxsecurity.com/wlb/)
  + [Only Bugs](https://cxsecurity.com/bugs/)
  + [Only Tricks](https://cxsecurity.com/tricks/)
  + [Only Exploits](https://cxsecurity.com/exploit/)
  + [Only Dorks](https://cxsecurity.com/dorks/)
  + [Only CVE](https://cxsecurity.com/cvelist/)
  + [Only CWE](https://cxsecurity.com/cwelist/)
  + [Fake Notes](https://cxsecurity.com/bogus/)
  + [Ranking](https://cxsecurity.com/best/1/)
* CVEMAP
  + [Full List](https://cxsecurity.com/cvemap/)
  + [Show Vendors](https://cxsecurity.com/cvevendors/)
  + [Show Products](https://cxsecurity.com/cveproducts/)
  + [CWE Dictionary](https://cxsecurity.com/allcwe/)
  + [Check CVE Id](https://cxsecurity.com/cve/)
  + [Check CWE Id](https://cxsecurity.com/cwe/)
* Search
  + [Bugtraq](https://cxsecurity.com/search/)
  + [CVEMAP](https://cxsecurity.com/search/cve/)
  + [By author](https://cxsecurity.com/search/author/)
  + [CVE Id](https://cxsecurity.com/cve/)
  + [CWE Id](https://cxsecurity.com/cwe/)
  + [By vendors](https://cxsecurity.com/cvevendors/)
  + [By products](https://cxsecurity.com/cveproducts/)
* RSS
  + [Bugtraq](https://cxsecurity.com/wlb/rss/all/)
  + [CVEMAP](https://cxsecurity.com/cverss/fullmap/)
  + [CVE Products](https://cxsecurity.com/cveproducts/)
  + [Bugs](https://cxsecurity.com/wlb/rss/vulnerabilities/)
  + [Exploits](https://cxsecurity.com/wlb/rss/exploit/)
  + [Dorks](https://cxsecurity.com/wlb/rss/dorks/)
* More
  + [cIFrex](http://cifrex.org/)
  + [Facebook](https://www.facebook.com/cxsec)
  + [Twitter](https://twitter.com/cxsecurity)
  + [Donate](https://cxsecurity.com/donate/)
  + [About](https://cxsecurity.com/wlb/about/)

* [Submit](https://cxsecurity.com/wlb/add/)

|  |  |  |  |
| --- | --- | --- | --- |
|  |  | |  | | --- | | **Apple Web Content Filter Bypass** **2024.11.25**  Credit:  **[Nosebeard](https://cxsecurity.com/author/Nosebeard/1/)**  Risk: **Low**  Local: **No**  Remote: ****Yes****  CVE: **[CVE-2024-44206](https://cxsecurity.com/cveshow/CVE-2024-44206/ "Click to see CVE-2024-44206")**  CWE: **N/A** | |

Dear colleagues,
Nosebeard Labs is pleased to share its latest advisory, detailing a
bypass of Apple's system wide web content filter. The HTML version of
this advisory is also available at:
https://nosebeard.co/advisories/nbl-001.html
Warmest regards,
Nosebeard Labs
## Summary
Nosebeard Labs Security Advisory NBL-001
Title: Apple web content filter bypass allows unrestricted access to
blocked content (macOS/iOS/iPadOS/visionOS/watchOS)
Advisory ID: NBL-001
Date: 2024-11-15
Severity: Critical (CVSS 9.1)
Affected Product: Safari on any Apple device with Screen Time enabled
CVE ID: CVE-2024-44206
## Overview
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
However, a fix is still pending for the backport channels.
## Description
This vulnerability arises when the WebKit Cocoa layer in Safari ingests
a URI without performing comprehensive validation, combined with a
failure by the Screen Time ACL filter to recognize and block the
malformed URI. The flaw allows a crafted URI to bypass all Screen Time
content filtering settings, including deny/allow lists and parental
content filters, providing unrestricted access to blocked content.
## Affected Systems
This vulnerability affects all devices on macOS, iOS, iPadOS, watchOS
and visionOS platforms with Safari and Screen Time enabled, impacting an
estimated 250 million devices globally.
## Attack Scenarios
The vulnerability can be exploited both locally and remotely:
1. Local Exploitation: Users can manipulate the address bar to manually
enter a crafted URI, bypassing Screen Time restrictions.
2. Network-Based Exploitation: Attackers can load restricted content
remotely by embedding a crafted URI within an iframe, bypassing
restrictions without requiring user interaction.
## Impact
1. Confidentiality: Unrestricted access to restricted websites
compromises the confidentiality of content filtering controls,
potentially exposing sensitive or inappropriate material.
2. Scope and Integrity: This vulnerability spans across two separate
security mechanisms (Screen Time and WebKit), representing a critical
architecture-level issue. Additionally, accessing unsecured or unlogged
resources poses potential integrity risks.
## CVSS Score
Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:C/C:H/I:L/A:N
Score: 9.1 (Critical)
## Mitigations
Upgrade to the latest iOS/iPadOS 17.x or 18.x / macOS Sonoma 14.x /
visionOS 1.x / watchOS 10.x / Safari 17.6 respectively. Users who are
unable to apply a fix can contact us for more info.
## Vendor Response
Apple has issued CVE-2024-44206 and supplied a fix within WebKit;
however, a fix remains pending for iOS/iPadOS version 16.x. We recommend
that Apple undertake further review to address the issue comprehensively.
## Timeline
–
Milestone:
2020-11-24 Vulnerability discovered internally at NBL
–
Milestone:
2021-03-08 Initial disclosure to Apple Product Security
–
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
2024-05-05 Initial contact with Joanna Stern of WSJ
2024-05-06 Referring PSIRT ticket # directly to an Apple PSIRT contact
via undisclosed SOC - no response
2024-05-28 Joanna Stern/WSJ runs Apple through this
2024-05-29 Apple commits patches to Safari branch
–
Milestone:
2024-06-05 Wall Street Journal addresses our finding in their article “A
Bug Allowed Kids to Visit X-Rated Sites. Apple Took Three Years to Fix
It.” by Joanna Stern
–
2024-06-18 We follow-up again with Urgent request for re-evaluation to
Apple Product Security (“Addendum”)
2024-06-27 We follow-up on our follow-up Update Request Screen Time
Security Vulnerability Report (“Follow-Up”)
2024-07-23 Apple releases fix in iOS 17.6RC et al.
2024-07-26 Letter to Apple welcoming first fix, reiterating our
dedication to Responsible Disclosure, inten...