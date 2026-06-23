---
title: New OXLOADER Loader Uses Malicious Google Ads to Deliver CastleStealer
url: https://thehackernews.com/2026/06/new-oxloader-loader-uses-malicious.html
source: The Hacker News
date: 2026-06-22
fetch_date: 2026-06-23T06:08:25.941575
---

# New OXLOADER Loader Uses Malicious Google Ads to Deliver CastleStealer

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

# [New OXLOADER Loader Uses Malicious Google Ads to Deliver CastleStealer](https://thehackernews.com/2026/06/new-oxloader-loader-uses-malicious.html)

**Ravie Lakshmanan**Jun 22, 2026Malvertising / Endpoint Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi8sz7SHbQd4E8HNEKbvGGSYhPpJrUydP_gCRt_mWYYTr6QHLmChyphenhyphenca6BXhLBXA4OyKw-eS9xbqRqpKcYWFqDp4HoLBYKjVdWzhF0K1pqjX2bPtB91y1P1PZ8gh5r7Bpp-PIeUJVi_Hki91Qf6YjFAtFmf-qh7V9gNzmbEh_A2lISCvCDnNMALAuiqAlkL_/s1700-e365/loader.jpg)

Cybersecurity researchers have disclosed details of a new campaign that delivers CastleStealer by means of a previously unreported malware loader dubbed **OXLOADER**.

According to Elastic Security Labs, the campaign leverages malicious Google Ads as a starting point to distribute the malware. Evidence indicates that the threat actor is likely Russian-speaking and financially motivated, owing to the presence of explicit exclusions to prevent infecting machines located in the Commonwealth of Independent States (CIS) region. The campaign has been codenamed REF8372.

"The loader uses several obfuscation layers (control-flow flattening, opaque predicates, mixed Boolean-Arithmetic), self-modifying decryption stubs, and abuses the Windows .reloc section to stage shellcode," researchers Daniel Stepanic and Jia Yu Chan [said](https://www.elastic.co/security-labs/oxloader-malware-loader-infostealer) in a technical breakdown.

The attack begins when unsuspecting users enter queries such as "lts version of node.js" on search engines like Google, redirecting them to a fake website ("node-js[.]prentiva99[.]info") surfaced via bogus ads published under the verified name "ВОЛОДИМИР ТЕРЕЩЕНКО" that's purportedly based in Ukraine.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/ai-cant-stop-d)

It's currently unknown if the advertiser account is linked to the actual threat actor, or if it's a front account or a purchased identity. The advertiser account, along with its ad campaigns, was removed from Google on May 14, 2026.

Users who end up interacting with the site are served a batch script hosted on Storj, a decentralized, open-source cloud storage platform. The abuse of Storj once again illustrates how threat actors continue to leverage legitimate services to evade domain-based reputation filters.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjAVWPTrityiUYPWfWAkZIGqBYY9xdlKUC_bU827p6qZda1IwqdAFR612_AOX2iR-Sc1uhe4KNmUVKn3JFz4v2JOuHPf7ZRiIcQJ-WhW4GVyK1PLXHnRWDqsZgvxiMeppgccfUY2eimyYUOBZXAGwB3e6d8Ns_wbe8Z0cze-Toaq4GtI4OeXKiFtLZTLuUi/s1700-e365/elastic.jpg)

Running the batch script displays a bogus installation wizard user interface (UI), while stealthily downloading a next-stage payload, a [Storj-hosted executable](https://www.virustotal.com/gui/file/9a9939dff297997732aaade9b243d695632cbd64033c5fbcb9de3d09b7e6c28d/detection) dubbed OXLOADER through a PowerShell command and executing it with -Verb RunAs to trigger a Windows User Account Control (UAC) prompt.

The attack then employs DLL side-loading to launch a rogue DLL, which then proceeds to decrypt and execute the CastleStealer payload. OXLOADER also makes use of techniques like control-flow flattening (CFF) and mixed Boolean-Arithmetic (MBA) to evade static detection, while also taking steps to ensure it's not run on sandboxed environments.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/vpn-threat-report-m)

CastleStealer is a .NET information stealer that was recently distributed alongside CastleLoader through a ClickFix-style lure masquerading as a free image-editing tool as part of a campaign codenamed [BackgroundFix](https://thehackernews.com/2026/06/threatsday-bulletin-ai-agents-gone.html#fake-image-tools-deliver-malware). CastleLoader is [attributed](https://thehackernews.com/2025/12/four-threat-clusters-using-castleloader.html) to a threat activity cluster known as GrayBravo.

"OXLOADER is in an early operational phase, but the engineering behind it suggests this family is worth watching," Elastic said. "The code obfuscation, anti-VM measures, benign-looking code used to masquerade its binaries, and unique staging techniques reflect deliberate engineering choices to evade analysis."

"That investment is paying off, resulting in low detection rates across static engines and detonation runs, giving OXLOADER a window to operate before it gets hunted down."

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

[DLL side-loading](https://thehackernews.com/search/label/DLL%20side-loading), [Elastic Security Labs](https://thehackernews.com/search/label/Elastic%20Security%20Labs), [Google Ads](https://thehackernews.com/search/label/Google%20Ads), [Information Stealer](https://thehackernews.com/search/label/Information%20Stealer), [malvertising](https://thehackernews.com/search/label/malvertising), [Malware](https://thehackernews.com/search/label/Malware), [powershell](https://thehackernews.com/search/label/powershell)

⚡ Top Stories This Week

[![Chrome V8 Zero-Day CVE-2026-11645 Exploited in the Wild - Patch Now](data:image/svg+xml;base64... "Chrome V8 Zero-Da...