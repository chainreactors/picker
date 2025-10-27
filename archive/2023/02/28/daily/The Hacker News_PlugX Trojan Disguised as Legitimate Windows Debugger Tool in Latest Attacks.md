---
title: PlugX Trojan Disguised as Legitimate Windows Debugger Tool in Latest Attacks
url: https://thehackernews.com/2023/02/plugx-trojan-disguised-as-legitimate.html
source: The Hacker News
date: 2023-02-28
fetch_date: 2025-10-04T08:16:26.666717
---

# PlugX Trojan Disguised as Legitimate Windows Debugger Tool in Latest Attacks

#1 Trusted Cybersecurity News Platform

Followed by 5.20+ million[**](https://twitter.com/thehackersnews)
[**](https://www.linkedin.com/company/thehackernews/)
[**](https://www.facebook.com/thehackernews)

[![The Hacker News Logo](data:image/png;base64...)](/)

**

**

[** Subscribe – Get Latest News](#email-outer)

* [** Home](/)
* [** Newsletter](#email-outer)
* [** Webinars](/p/upcoming-hacker-news-webinars.html)

* [Home](/)
* [Data Breaches](/search/label/data%20breach)
* [Cyber Attacks](/search/label/Cyber%20Attack)
* [Vulnerabilities](/search/label/Vulnerability)
* [Webinars](/p/upcoming-hacker-news-webinars.html)
* [Expert Insights](https://thehackernews.com/expert-insights/)
* [Contact](/p/submit-news.html)

**

**

**

Resources

* [Webinars](/p/upcoming-hacker-news-webinars.html)
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

[![Salesforce Security Handbook](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjWa8tsMNqlevi1HGF1ALQRGIq7hROPFAbHd3R1RTEOe73T8_Q2xW_-91t2jSGjU5peiPb8QYblGp4igNW-u2Qmlxbp2BKzTVMSvyXDZJmC-BYpiiJHrcnG5drmSP97iZ9PVIf1DeEr7U-7vWpe4HXwfMjt8FGNgq5mOycOJluYr9wF7YOKrQY9MfArwgjt/s728-e100/ai-agent-security-d.png)](https://thehackernews.uk/ai-agent-security-d)

# [PlugX Trojan Disguised as Legitimate Windows Debugger Tool in Latest Attacks](https://thehackernews.com/2023/02/plugx-trojan-disguised-as-legitimate.html)

**Feb 27, 2023**Ravie LakshmananMalware / Cyber Attack

[![PlugX Trojan](data:image/png;base64... "PlugX Trojan")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgw9G_A8t0Hm-JbSh3N8OOINj4q3DTeBAhfN1WXfpMr_xBtW5AnBiIeVLcqF1m1LZMuwmQOR2HrFx44tkgh7NPd1JvwWX4AgMpm8vzj_IM0dMU9JWH3SjKe-MpPLhdb7RivH4R6L-0lCqlkDH02QZa94GjgflijowfSbGCEqhjij37dMMMxRgX60FtO/s790-rw-e365/plugx.png)

The **PlugX** remote access trojan has been observed masquerading as an open source Windows debugger tool called x64dbg in an attempt to circumvent security protections and gain control of a target system.

"This file is a legitimate open-source debugger tool for Windows that is generally used to examine kernel-mode and user-mode code, crash dumps, or CPU registers," Trend Micro researchers Buddy Tancio, Jed Valderama, and Catherine Loveria [said](https://www.trendmicro.com/en_us/research/23/b/investigating-the-plugx-trojan-disguised-as-a-legitimate-windows.html) in a report published last week.

PlugX, also known as [Korplug](https://www.cybereason.com/blog/threat-analysis-report-plugx-rat-loader-evolution), is a post-exploitation [modular implant](https://logrhythm.com/blog/deep-dive-into-plugx-malware/), which, among other things, is known for its multiple functionalities such as data exfiltration and its ability to use the compromised machine for nefarious purposes.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

Although first documented a decade ago in 2012, early samples of the malware date as far as February 2008, according to a [Trend Micro report](https://web.archive.org/web/20121026140131/https%3A//blog.trendmicro.com/trendlabs-security-intelligence/plugx-new-tool-for-a-not-so-new-campaign/) at the time. Over the years, PlugX has been used by threat actors with a Chinese nexus as well as cybercrime groups.

One of the key methods the malware employs is a technique called [DLL side-loading](https://attack.mitre.org/techniques/T1574/002/) to load a [malicious DLL](https://www.cybereason.com/blog/threat-analysis-report-dll-side-loading-widely-abused) from a digitally signed software application, in this case the [x64dbg](https://x64dbg.com/) debugging tool (x32dbg.exe).

It's worth noting here that DLL side-loading attacks leverage the [DLL search order mechanism](https://learn.microsoft.com/en-us/windows/win32/dlls/dynamic-link-library-search-order) in Windows to plant and then invoke a legitimate application that executes a rogue payload.

"Being a legitimate application, x32dbg.exe's valid digital signature can confuse some security tools, enabling threat actors to fly under the radar, maintain persistence, escalate privileges, and bypass file execution restrictions," the researchers said.

The hijacking of x64dbg to load PlugX was disclosed last month by Palo Alto Networks Unit 42, which [discovered](https://thehackernews.com/2023/01/researchers-discover-new-plugx-malware.html) a new variant of the malware that hides malicious files on removable USB devices to propagate the infection to other Windows hosts.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

Persistence is achieved via Windows Registry modifications and the creation of scheduled tasks to ensure continued access even after system restarts.

Trend Micro's analysis of the attack chain also revealed the use of x32dbg.exe to deploy a backdoor, a UDP shell client that collects system information and awaits additional instructions from a remote server.

"Despite advances in security technology, attackers continue to use [DLL side-loading] since it exploits a fundamental trust in legitimate applications," the researchers said.

"This technique will remain viable for attackers to deliver malware and gain access to sensitive information as long as systems and applications continue to trust and load dynamic libraries."

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
[**Share on Email](#link_share)
[**Share on WhatsApp](#link_share)
[![Facebook Messenger](data:image/png;base64...)Share on Facebook Messenger](#link_share)
[**Share on Telegram](#link_share)

SHARE **

[Cyber Attack](https://thehackernews.com/search/label/Cyber%20Attack)[hacking news](https://thehackernews.com/search/label/hacking%20news)[Malware](https://thehackernews.com/search/label/Malware)[PlugX](https://thehackernews.com/search/label/PlugX)

[![c](data:image/svg+xml;base64...)](https://thehackernews.uk/cloud-defense)

Trending News

[![SolarWinds Releases Hotfix for Critical CVE-2025-26399 Remote Code Execution Flaw](data:image/svg+xml;base64... "SolarWinds Releases Hotfix for Critical CVE-2025-26399 Remote Code Execution Flaw")

SolarWinds Releases Hotfix for Critical CVE-2025-26399 Remote Code Execution Flaw](https://thehackernews.com/2025/09/solarwinds-releases-hotfix-for-critical.html)

[![Microsoft Patches Critical Entra ID Flaw Enabling Global Admin Impersonation Across Tenants](data:image/svg+xml;base64... "Microsoft Patches Critical Entra ID Flaw Enabling Global Admin Impersonation Across Tenants")

Microsoft Patches Critical Entra ID Flaw Enabling Global Admin Impersonation Across Tenants](https://thehackernews.com/2025/09/microsoft-patches-critical-entra-id.ht...