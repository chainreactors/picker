---
title: New Threat Cluster OP-512 Targets Microsoft IIS Servers with Custom Web Shell Framework
url: https://thehackernews.com/2026/06/new-threat-cluster-op-512-targets.html
source: The Hacker News
date: 2026-06-05
fetch_date: 2026-06-06T05:51:38.521553
---

# New Threat Cluster OP-512 Targets Microsoft IIS Servers with Custom Web Shell Framework

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

[![cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjQl2axNwsfhbXOFynrg_uAZsvHi3OvNGSA8KJO-BKR8Xm3x7yjKV3EvfY4v5mwXx6LF0uWFb9h9d9iAV_Pi-YYhqimX9wx4OaLdDJEdR215Xrxq_PAtXkaLfQso4pTSjbj6fvh_ZTliLpzWZSZfcoZgyXtKwhN-SSDDlmbtUqGLshc0KqYQGWYHMN52Sl1/s728-e100/zz-d.jpg)](https://thehackernews.uk/ai-vuln-protection-d)

# [New Threat Cluster OP-512 Targets Microsoft IIS Servers with Custom Web Shell Framework](https://thehackernews.com/2026/06/new-threat-cluster-op-512-targets.html)

**Ravie Lakshmanan**Jun 05, 2026Cyber Espionage / Threat Intelligence

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiab_7FEmO4woH_bG4spUNJRFCFvvmpF9ggnhOlkIf7f0Ma7z4oEwL0MxFSe4CstBBQRLFsYxObArJESQWOkwOPIQgO7m17DQFE997ZPe9hBnUPWiY-rabco7Q_OE2LYgp5UuqDfSxk8jvCJvLriBKb6OQAN9ovQbqSTOGD13SWnU3P12FTLgfvMe5sTgPN/s1700-e365/chinese.jpg)

Cybersecurity researchers have discovered a previously unreported threat cluster dubbed OP-512 (where "OP" stands for "opponent") that has been observed targeting Microsoft Internet Information Services (IIS) servers to deploy a bespoke web shell framework.

ReliaQuest has assessed with moderate to high confidence that the espionage-focused activity is linked to China.

"OP-512 was highly likely conducting espionage through a compromised Internet Information Services (IIS) web server on an organization whose sector and geography align with China-linked intelligence priorities," the company [said](https://reliaquest.com/blog/threat-spotlight-reliaquests-agentic-ai-uncovers-new-china-linked-cluster-op-512) in a report shared with The Hacker News.

Although no overlaps have been found between OP-512 and other known China-aligned adversaries, it's the fourth such threat group after [CL-STA-0048](https://thehackernews.com/2025/05/china-linked-apts-exploit-sap-cve-2025.html), [DragonRank](https://thehackernews.com/2025/10/chinese-cybercrime-group-runs-global.html), and [GhostRedirector](https://thehackernews.com/2025/09/ghostredirector-hacks-65-windows.html) to single out IIS web servers over the past 12 months. As recently as last month, Cisco Talos [revealed](https://thehackernews.com/2026/05/webworm-deploys-echocreep-and-graphworm.html) that multiple Chinese-speaking cybercrime groups are sharing a variant of malware called BadIIS to infect IIS servers.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/ai-cant-stop-d)

IIS servers have also been targeted by [SHADOW-EARTH-053](https://thehackernews.com/2026/05/china-linked-hackers-target-asian.html) as part of a new China-aligned espionage campaign targeting government and defense sectors across South, East, and Southeast Asia.

Central to the operations of OP-512 is a custom web shell framework consisting of three web shells that grant the attackers remote access to the compromised host, while taking steps to evade signature-based detection and complicate forensic timelines using techniques like [timestomping](https://attack.mitre.org/techniques/T1099/) to intentionally manipulate the timestamps when the web shell artifacts are created or modified.

Specifically, this entails scanning every file and sub-folder around where the web shells are placed, calculating the median last-modified timestamp, and overwriting their own creation and modification times to match that value, thus giving the impression that they have been present for some time.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEh2ut_d0AWToZxAQTTMjXzD68y9p4rQxf7p8ZjbgEt5OG0xSk0RUU3KagyjR9OFCHoSOu49eNtP9wpi36oueQH7L-7gbpbB6gaSd4CUn02Ml2Ppx0sHQoiuNWFejCKubgMBBuV4QjcMyIxUHYnn4K0F3S_yw_RT-1KzcHGbj53eV9zejiaoL5Hrlq9qTne0/s1700-e365/rr.jpg)

"This framework combines capabilities we rarely see together: each deployment is uniquely generated, access is restricted to the attacker through cryptographic controls, and compromised servers automatically report back for centralized management at scale," ReliaQuest said.

OP-512 shares close tactical proximity to CL-STA-0048, which has raised the possibility that it either represents an existing cluster that has completely revamped its toolset or developed these capabilities independently on its own. Regardless of its origins, the hacking group is said to be a distinct cluster operating in an autonomous manner.

In the attack observed by the cybersecurity company, the threat actor has been found to target a legacy IIS server running Windows Server 2016 with end-of-life .NET Framework 4.0. There is evidence of prior activity on the same host, about 75 days before the main incident took place. This involved DNS queries to a different attacker-controlled domain ("ashx.lhlsjcb[.]com").

The sequence of actions that unfolded weeks later has been described as a "sprint," with the attacker using the web server's worker process ("w3wp.exe") to drop one of the web shells to the application's upload directory. This, in turn, triggers a self-reporting mechanism that uses a DNS query or an HTTP request as a fallback to transmit the web shell's location to an attacker-controlled domain.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/vpn-threat-report-m)

"Together, the three web shells gave the attacker file management, authenticated command execution through two independent access paths, and automated reporting of the compromise, all before anyone had time to respond," ReliaQuest researchers explained.

With the web shells deployed, OP-512 is said to have attempted to escalate privileges to the SYSTEM level using the [Potato Suite,](https://assets.sentinelone.com/labs/rise-of-potatoes) followed by running commands like "whoami /priv" to confirm their system rights.

"Four China-linked clusters targeting the same technology in under a year is unlikely to be a coincidence," ReliaQuest said. "Internet-facing IIS servers running legacy, unsupported software remain a preferred entry point across this threat ecosystem and show no signs of slowing down."

"What should concern defenders most is what makes OP-512 different. This threat cluster isn't using commodity tooling and recycling it across campaigns. It's using a purpose-built framework designed to defeat the detection methods that work against the other three clusters. Organizations that have tuned the...