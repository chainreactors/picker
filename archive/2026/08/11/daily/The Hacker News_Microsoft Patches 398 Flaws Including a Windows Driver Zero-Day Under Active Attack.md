---
title: Microsoft Patches 398 Flaws Including a Windows Driver Zero-Day Under Active Attack
url: https://thehackernews.com/2026/08/microsoft-patches-398-flaws-including.html
source: The Hacker News
date: 2026-08-11
fetch_date: 2026-08-12T04:02:48.748246
---

# Microsoft Patches 398 Flaws Including a Windows Driver Zero-Day Under Active Attack

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

![cybersecurity](data:image/svg+xml;base64...)

# [Microsoft Patches 398 Flaws Including a Windows Driver Zero-Day Under Active Attack](https://thehackernews.com/2026/08/microsoft-patches-398-flaws-including.html)

**Swati Khandelwal**Aug 11, 2026Vulnerability / Windows Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEg4HtkIdWjqoYaSkO4edq9d5ZotqTE-LNMM14UlVoPaVKw2hwBahFYrPkB3jttURH0gcBXxCDtyHhiGMAIrxCX74gYCb_ivX4INmfRzt7HRb-bPTNt1lV-nUQm_pHQQHrhUwx4JWS7DtAzOZ1etx-yjPAVrNJXGBltqXjHPSI5NcfnWQqYurz0LK-dRRMo/s1700-e365/aug-ms-patch.jpg)

Microsoft released its monthly security updates on Tuesday, and one of the flaws it closed is already being used in attacks.

The bug sits in a core Windows kernel driver that handles network socket operations. An attacker with code already running on a machine can use it to escalate to SYSTEM. That patch goes out first.

The flaw is tracked as **CVE-2026-68820** (CVSS score: 7.0) and is the only one in this month's release Microsoft flags as under active exploitation. Exploitation depends on triggering a race condition in the driver. Microsoft has not publicly attributed the exploitation. Check Point Research says Lazarus used the zero-day in its Operation Dream Job campaign.

Four other flaws in the release need nothing at all from the victim: no account, no password, no click. They affect Windows DNS Server, Windows Deployment Services, Microsoft's implementation of the QUIC transport protocol, and High Performance Computing (HPC) Pack, and each carries a CVSS score of 9.8. None was flagged as exploited when the updates shipped.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/zero-trust-claude-d)

Counting independently, the Zero Day Initiative puts the release at 398 new CVEs, 62 of them rated Critical. The count shows the size of the release; exploit status and reach decide the patch order.

The release also closes the RCE half of a SharePoint chain whose authentication bypass was fixed in July. On-premises SharePoint farms should have both updates installed.

[Check Point Research](https://research.checkpoint.com/2026/shattering-the-dream-when-a-job-offer-becomes-a-zero-day-attack/) said CVE-2026-68820 is a use-after-free in afd.sys, the [Ancillary Function Driver for WinSock](https://thehackernews.com/2024/08/microsoft-patches-zero-day-flaw.html) and a kernel-side component of Windows networking.

The bug is privilege escalation: an attacker needs code running on the machine first, then can use it to reach SYSTEM. Microsoft flags it as actively exploited, which puts it ahead of the four 9.8 server RCEs here despite the lower score.

## Nothing required from the victim

The four unauthenticated remote code execution flaws are the ones to queue behind the exploited driver bug because they can give an attacker code on a server without first needing an account or a user action.

* **CVE-2026-62878, Windows DNS Server.** A stack-based buffer overflow reachable remotely with no authentication and no user interaction. The Zero Day Initiative describes the condition as wormable despite Microsoft rating exploitation as less likely. ZDI's “wormable” label describes the technical condition; it does not establish that a worm exists.
* **CVE-2026-62893, Windows Deployment Services.** A remote flaw reachable through the service's TFTP handling without authentication or user interaction.
* **CVE-2026-62815, Microsoft QUIC.** A remote, unauthenticated code execution flaw requiring no user interaction.
* **CVE-2026-59124, HPC Pack.** It carries the same 9.8 score but is rated Important rather than Critical because HPC Pack is not installed by default. Microsoft rates exploitation as more likely.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/corelight-d)

HPC Pack is not installed by default, and the practical priority of the other three likewise depends on whether the vulnerable service is present and reachable in a given environment. So service inventory and reachability matter alongside exploit status when setting patch priority.

## A SharePoint chain closes

August also completes a two-part SharePoint fix that started in July.

Rapid7 Labs reported an exploit chain to Microsoft on May 18 that combined an authentication bypass with a separate code execution vulnerability to [reach unauthenticated RCE against on-premises SharePoint](https://thehackernews.com/2026/08/researchers-disclose-ai-assisted.html). Microsoft confirmed two days later that it planned to split the remediation across the July and August update cycles.

July fixed the first half, **CVE-2026-55040**, a Critical authentication bypass scored at 9.1. Rapid7 found that the flaw lets a remote unauthenticated attacker assume the identity of a SharePoint site user or administrator if the attacker knows the identity to impersonate. August supplies the fix for the RCE component, identified as **CVE-2026-63520**.

The distinction matters: CVE-2026-63520 is the code execution half of the chain, not by itself the unauthenticated condition. Chaining the RCE with CVE-2026-55040 is what produced Rapid7's unauthenticated RCE.

Rapid7 says patching CVE-2026-55040 breaks the demonstrated chain, so once the July fix was applied, that route was already closed; the August update now closes the RCE component as well.

Put CVE-2026-68820 at the top for Windows systems where an attacker already has code running and could use the flaw to reach SYSTEM. Prioritize exposed DNS, WDS, QUIC, and HPC services behind it, then confirm on-premises SharePoint farms have the July authentication-bypass fix and the August RCE fix.

Found this article interesting? Follow us on [Google News](https://news.google.com/publications/CAAqLQgKIidDQklTRndnTWFoTUtFWFJvWldoaFkydGxjbTVsZDNNdVkyOXRLQUFQAQ), [Twitter](https://twitter.com/thehackersnews) and [LinkedIn](https://www.linkedin.com/company/thehackernews/) to read more exclusive content we post.

SHARE
[**](#link_share)
[**](#link_share)
[**](#link_share)
**

[**Tweet](#link_share)

[**Share](#link_share)

[**Share](#link_share)

**Share

**
[**Share on Facebook](#link_share)
[**Share on Twitter](#link_share)
[**Share on Linkedin](#link_share)
[**Share on Reddit](#link_share)
[**Share on Hacker News](#link_share)
[**Share on...