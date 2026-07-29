---
title: Critical OpenWrt DHCPv6 Flaw Could Let Unauthenticated Attackers Run Code as Root
url: https://thehackernews.com/2026/07/critical-openwrt-dhcpv6-flaw-could-let.html
source: The Hacker News
date: 2026-07-28
fetch_date: 2026-07-29T05:04:27.157299
---

# Critical OpenWrt DHCPv6 Flaw Could Let Unauthenticated Attackers Run Code as Root

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

[![cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgrKWHErc__Wn0forfQ5eJ5sIR1hVKCHCTeNQOaAX4lbygJ8S1Xpemx6JXl78dpwiT65DDBGURp48A3EemKzmli-jXPI3v1928MnJm-1j2ZPUaFXCvuySFhyphenhyphenKR-Li6fAinFT2bhLgsqUSNUR_ggMAnOHi3jD1qYWHXvueX8WdtxAd6GYety9cBGYABo18hX/s728-e100/tt-d.jpg)](https://thehackernews.uk/ai-zero-trust-h-d)

# [Critical OpenWrt DHCPv6 Flaw Could Let Unauthenticated Attackers Run Code as Root](https://thehackernews.com/2026/07/critical-openwrt-dhcpv6-flaw-could-let.html)

**Swati Khandelwal**Jul 28, 2026Network Security / Vulnerability

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhDmz4Rv-IWcHYP4Y_-WINLECGsPviBOTJXEPhvz2mO671_s8c1Rao7iErkNghWYtomczRf82scnXyzrBTAIc4urvwSlv3j4AK1XaEw75WVsIfXLfNDQd1JGUoVRWW50H48KA3VxzAbL1KTuf3sKCgzmSE3toXbqcIA-N5vwN4A_wcmRdwDLBSJbBpmmME/s1700-e365/OpenWrt.jpg)

**OpenWrt** has shipped version 24.10.8 to close a critical DHCPv6 stack overflow and a wider set of remotely triggerable flaws in network services enabled by default.

The critical issue, tracked as **CVE-2026-53921** and rated 9.8 on CVSS 3.1 in OpenWrt's GitHub advisory, lets an unauthenticated attacker able to reach the DHCPv6 server overwrite a stack buffer in odhcpd through a crafted DHCPv6 REQUEST.

odhcpd runs as root, and the advisory notes that embedded hardware commonly lacks stack canaries and address space layout randomization (ASLR), making code execution a realistic outcome on typical devices.

The advisory includes public Python proof-of-concept code for both documented overflow paths. Users on the 24.10 branch should install 24.10.8, while users on 25.12 should install 25.12.5; firmware images are available through the OpenWrt Firmware Selector.

As of July 28, the reviewed OpenWrt materials did not report exploitation in the wild. The flaw was also absent from CISA's Known Exploited Vulnerabilities (KEV) catalog [version 2026.07.27](https://github.com/cisagov/kev-data/blob/develop/known_exploited_vulnerabilities.json), although absence from KEV does not establish that exploitation has not occurred.

The release arrived alongside a separate AI-assisted audit by [Hacker House](https://hacker.house/blog/inference-fuzzing-with-recursive-prompting-a-practical-methodology-for-llm-driven-code-audits) that identified command-injection, path-traversal and cross-site scripting (XSS) weaknesses in optional LuCI components. OpenWrt found a separate stored-XSS issue and missing cross-site request forgery (CSRF) protection while preparing the fixes.

These separate LuCI fixes were not part of OpenWrt 24.10.8 and remained under review on July 28.

## A Packet to the Default DHCP Server

The [advisory associated with CVE-2026-53921](https://github.com/openwrt/odhcpd/security/advisories/GHSA-7fwx-hhrg-3496) documents two independent overflow sites in the DHCPv6 request-processing path. In both, crafted IA options leave insufficient space in a fixed 512-byte stack buffer before the code appends additional reply data without a sufficient bounds check.

The final trigger is an unauthenticated DHCPv6 REQUEST sent to UDP port 547. The first path's proof of concept creates five IA\_NA bindings with an earlier SOLICIT; the second is triggered by a single crafted REQUEST.

The advisory lists odhcpd master at commit e432dd6 and all earlier versions containing dhcpv6\_ia\_handle\_IAs() and build\_ia() as affected. OpenWrt lists 24.10.8 and 25.12.5 as the supported releases carrying the relevant odhcpd security update.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/ai-vuln-protection-d)

The advisory associates its two documented sites with CVE-2026-53921, but the 24.10.8 release notes list the RECONF\_ACCEPT overflow separately as a high-severity issue without a CVE. OpenWrt fixed the underlying writes by checking the remaining response-buffer capacity before appending the affected data.

OpenWrt's advisory groups both overflow sites under CVE-2026-53921, while the release notes list RECONF\_ACCEPT separately without a CVE. The exact mapping remains unclear.

OpenWrt's release notes describe the flaw as reachable by a network-adjacent, unauthenticated attacker. The advisory's CVSS 3.1 vector uses [AV:N](https://www.first.org/cvss/v3.1/specification-document) (Network), not AV:A (Adjacent), and neither source explains the difference. An attacker still needs network access to the DHCPv6 service. Successful exploitation could give the attacker control of the router rather than merely crash the service.

The [24.10.8 release](https://github.com/openwrt/openwrt/releases/tag/v24.10.8) also addresses other pre-authentication weaknesses in odhcpd, including an out-of-bounds write, use-after-free, memory disclosure, denial of service, stack over-read and neighbour-discovery proxy spoofing. Other default-service fixes cover three HTTP request-smuggling bugs in uhttpd and a DHCPv6 hostname-injection flaw, tracked as CVE-2026-62948, that can produce stored XSS when an administrator opens the LuCI leases page.

The same release includes [CVE-2026-62947](https://github.com/openwrt/openwrt/security/advisories/GHSA-jw5r-xhf5-2xcq) in cgi-io, which can expose arbitrary root-readable files through path traversal. That issue requires an authenticated session with the cgi-io download permission and an applicable wildcard file-read grant. It is not an anonymous file-read flaw.

OpenWrt 24.10 is under security maintenance, with end of life projected for September 2026. The project recommends migrating to the [25.12 series](https://github.com/openwrt/openwrt/releases/tag/v25.12.5) before then. Packages installed separately from the firmware image may also require separate updates.

## The Patches Still in Review

Matthew Hickey, also known as Hacker Fantastic and CTO and Co-Founder of Hacker House, [said publicly](https://x.com/hackerfantastic/status/2081726741408583980) that fixes had been released for remote-code-execution and path-traversal issues he reported to OpenWrt.

OpenWrt maintainer Hauke Mehrtens published [LuCI pull request #8878](https://github.com/openwrt/luci/pull/8878) on July 26, explicitly crediting Hickey and Hacker House. A check by The Hacker News on July 28 found the pull request still open and unmerged.

|  |
| --- |
| [![](data:image/png;base64...)](ht...