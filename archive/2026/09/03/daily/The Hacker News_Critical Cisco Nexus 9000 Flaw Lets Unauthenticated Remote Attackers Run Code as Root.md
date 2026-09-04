---
title: Critical Cisco Nexus 9000 Flaw Lets Unauthenticated Remote Attackers Run Code as Root
url: https://thehackernews.com/2026/09/critical-cisco-nexus-9000-flaw-lets.html
source: The Hacker News
date: 2026-09-03
fetch_date: 2026-09-04T06:44:14.056157
---

# Critical Cisco Nexus 9000 Flaw Lets Unauthenticated Remote Attackers Run Code as Root

#1 Trusted Cybersecurity News Platform

Followed by 5.70+ million[**](https://twitter.com/thehackersnews)
[**](https://www.linkedin.com/company/thehackernews/)
[**](https://www.facebook.com/thehackernews)

[![The Hacker News Logo](data:image/png;base64...)](/)

**

**

[** Get the Latest News](#email-outer)

* [Home](/)
* [Newsletter](#email-outer)
* [Webinars](/p/upcoming-hacker-news-webinars.html)

* [Home](/)
* [Threat Intelligence](/search/label/Threat%20Intelligence)
* [Vulnerabilities](/search/label/Vulnerability)
* [Cyber Attacks](/search/label/Cyber%20Attack)
* [Webinars](/p/upcoming-hacker-news-webinars.html)
* [Expert Insights](https://thehackernews.com/expert-insights/)
* [Awards](https://awards.thehackernews.com/)

**

**

**

Resources

* [Webinars](/p/upcoming-hacker-news-webinars.html)
* [Awards](https://awards.thehackernews.com/)
* [Free eBooks](https://thehackernews.tradepub.com)

About Site

* [About THN](/p/about-us.html)
* [Jobs](/p/careers-technical-writer-designer-and.html)
* [Advertise with us](/p/advertising-with-hacker-news.html)

Contact/Tip Us

[**

Reach out to get featured—contact us to send your exclusive story idea, research, hacks, or ask us a question or leave a comment/feedback!](/p/submit-news.html)

Follow Us On Social Media

[**](https://www.facebook.com/thehackernews)
[**](https://twitter.com/thehackersnews)
[**](https://www.linkedin.com/company/thehackernews/)
[**](https://www.youtube.com/c/thehackernews?sub_confirmation=1)
[**](https://www.instagram.com/thehackernews/)

[** RSS Feeds](https://feeds.feedburner.com/TheHackersNews)
[** Email Alerts](#email-outer)

[![cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiHP9KRFkaxKFUKQNRU3CkfxCyJLEuIfmo6ov7iWHHRBE1ShJKfXdPvozMZMVuvOJipQ8Qbap3UBmtjKvZh-xBqLeUartPWmRuQj2W8nqdCk2_XlYLXpj15R4Du2oJ1nNVPqIuR-TwbMyPQe4gxxCcMYvUMbFO_Nin2OdhyzkJvX8Sn83aEbM1C5sgaaCqI/s728-nu-rw-lo-l85-e365/wiz-sep-d.png)](https://thehackernews.uk/claude-security-guide-d)

# [Critical Cisco Nexus 9000 Flaw Lets Unauthenticated Remote Attackers Run Code as Root](https://thehackernews.com/2026/09/critical-cisco-nexus-9000-flaw-lets.html)

**Swati Khandelwal**Sep 03, 2026Vulnerability / Network Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgj9su2Wd6Yb88IvMpg5v1P8IyPg4KWKTeBXjerFgxz0U5WLKO2U50jymR-fKujsKeMFZ3q1VEupMRFZUz5gD47JRzVceagYJJ3bCTT8t532rY63po54kanBCPX4_hmKsxe-1b52IGrYc__TH5Y2F13G6L32HNKPQxL34iqzEPuBGynDCu6xFdKHplXvdY/s1700-nu-rw-lo-l85-e365/cisco-flaws.jpg)

Cisco has released patches to address a critical security flaw affecting 10 Silicon One-based Nexus 9000 switches that could allow an unauthenticated, remote attacker to execute code as root, alongside an IOS XR hardening release bundling 7 umbrella CVEs, 2 of which are rated 9.8, with no workaround for any IOS XR version.

The Nexus vulnerability, tracked as **CVE-2026-20212** (CVSS score: 9.8), is a case of binding to an unrestricted IP address that leaves TCP ports 43210 and 43211 reachable in the default Layer 3 virtual routing and forwarding (VRF) instance.

An attacker who can reach a switch's address on either port can connect directly to the service. Crafted input sent to that service is then executed as code with root privileges. An exploitation attempt can also crash the S1HAL process and reload the device.

Cisco said it's not aware of any malicious use of the flaw as of its September 2 disclosure. It has published no fixed-release table and directs customers to its Software Checker, with an infrastructure access control list (iACL) blocking the two ports and a temporary Live Protect shield as stopgaps.

Cisco tells IOS XR customers, including those on IOS XR7 (LNT), to upgrade to a release that includes software maintenance updates (SMUs), then apply them.

"At the same time, the window between disclosure and exploitation has effectively closed," Russ Smoak, vice president of information security at Cisco, said in [a June blog post](https://blogs.cisco.com/security/strengthening-the-foundation-a-predictable-customer-focused-response-to-ai-accelerated-vulnerability-discovery) announcing the twice-monthly disclosure model that groups internally found bugs into umbrella CVEs.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/trust-world-update-d)

Cisco lists the following affected product identifiers (PIDs) in [its Nexus 9000 advisory](https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-n9k-s1-rce-EH8dEtr), checkable against the output of the show module command -

* N9324C-SE1U (Nexus Smart Switch)
* N9348Y2C6D-SE1U (Nexus Smart Switch)
* N9364E-SG2-O
* N9364E-SG2-Q
* N9396T12C-SE1
* N9348Y12C-SE1
* N9396Y12C-SE1
* N9336C-SE1
* N9K-C9804
* N9K-C9808

Other Nexus 9000 models, Nexus 9000 fabric switches running in Application Centric Infrastructure (ACI) mode, and the Nexus 3000 and 7000 lines are unaffected.

The Hacker News confirmed via [the CVE Program's record](https://www.cve.org/CVERecord?id=CVE-2026-20212) on September 3 that Cisco lists 45 NX-OS releases, from 10.3(1) through 10.6(3s), as affected, a range the advisory itself leaves to the Software Checker.

Until a fixed release is confirmed, Cisco offers the following -

* **Upgrade** to the release named by [Cisco's Software Checker](https://sec.cloudapps.cisco.com/security/center/softwarechecker.x); [the shield's release notes](https://www.cisco.com/c/en/us/td/docs/dcn/nx-os/nexus9000/106x/release-notes/release-notes-nxos-live-protect-shield-1063.html) state that its operational mode transitions to N/A on upgrade to NX-OS 10.6(4) or higher.
* **iACL** permitting only required management and control-plane traffic, or explicitly denying TCP packets to a locally configured IP address on destination port 43210 or 43211, proven in a test environment.
* **Live Protect shield** lp00031, a temporary mitigation described in [Cisco's Live Protect documentation](https://www.cisco.com/c/en/us/td/docs/dcn/nx-os/nexus9000/106x/configuration/security/cisco-nexus-9000-series-nx-os-security-configuration-guide-release-106x/m-secure-nxos-with-cisco-live-protect.html), supported only on NX-OS 10.6(3) and, via [a second shield package](https://www.cisco.com/c/en/us/td/docs/dcn/nx-os/nexus9000/106x/release-notes/release-notes-nxos-live-protect-shield-1063s.html), on 10.6(3s) for the two Smart Switches; it's unsupported on the Nexus 9804 and 9808 and needs SSH, Telnet, or NX-API access.

### IOS XR Hardening Release Reaches Every Version

The IOS XR release assigns one CVE to each Common Weakness Enumeration (CWE) bucket of fixed bugs and scores it at the most severe defect in that bucket, per the rules in [its risk-based disclosure FAQ](https://sec.cloudapps.cisco.com/security/center/resources/risk-based-disclosure).

**CVE-2026-20274**, which covers memory-safety and resource-lifetime bugs, and **CVE-2026-20279**, which covers access-control bugs including missing authentication for critical functions and improper certificate validation, each carry a 9.8 ceiling in [the record for CVE-2026-20274](https://www.cve.org/CVERecord?id=CVE-2026-20274) and [that for CVE-2026-20279](https://www.cve.org/CVERecord?id=CVE-2026-20279).

The remaining five, CVE-2026-20275 through 20278 and CVE-2026-20280, top out between 8.2 and 8.8.

The vulnerabilities affect all releases regardless of device configuration, [the IOS XR hardening advisory](https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-hardening-iosxr-qg64NcM) said.

The XR7 (LNT) platforms, which include the Cisco 8000 Series, NCS 1010, NCS 540L, and NCS 5700 Series, have a dedicated SMU that applies across all releases.

Cisco said there may be "approximately 16 SMUs available for each release," that future releases 26.2.2 and 26.3.1 will be the first fixed releases needing no SMUs, and that customers running a release outside its table should open a T...