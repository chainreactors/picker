---
title: How a Single HTTP Redirect Bypassed SSRF Filters on 4 Programs Over 8 Years
url: https://infosecwriteups.com/how-a-single-http-redirect-bypassed-ssrf-filters-on-4-programs-over-8-years-4f67437ba6c7?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2026-08-26
fetch_date: 2026-08-27T12:12:35.785738
---

# How a Single HTTP Redirect Bypassed SSRF Filters on 4 Programs Over 8 Years

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://play.google.com/store/apps/details?id=com.medium.reader&referrer=utm_source%3DmobileNavBar&source=---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fhow-a-single-http-redirect-bypassed-ssrf-filters-on-4-programs-over-8-years-4f67437ba6c7&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=---top_nav_layout_nav-----------------------------------------)

Get app

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fhow-a-single-http-redirect-bypassed-ssrf-filters-on-4-programs-over-8-years-4f67437ba6c7&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![Unknown user](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-4f67437ba6c7---------------------------------------)

·

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-4f67437ba6c7---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Member-only story

[Cybersecurity](https://medium.com/tag/cybersecurity?source=post_page---header_tags--4f67437ba6c7---------------------------------------)

[Ethical Hacking](https://medium.com/tag/ethical-hacking?source=post_page---header_tags--4f67437ba6c7---------------------------------------)

[Ssrf](https://medium.com/tag/ssrf?source=post_page---header_tags--4f67437ba6c7---------------------------------------)

[Web Security](https://medium.com/tag/web-security?source=post_page---header_tags--4f67437ba6c7---------------------------------------)

[Bug Bounty](https://medium.com/tag/bug-bounty?source=post_page---header_tags--4f67437ba6c7---------------------------------------)

# How a Single HTTP Redirect Bypassed SSRF Filters on 4 Programs Over 8 Years

[![Raj Namdev](https://miro.medium.com/v2/resize:fill:64:64/1*qKc3NlEudBR8LvTVmc0eBA.jpeg)](https://medium.com/%40rajnamdev?source=post_page---byline--4f67437ba6c7---------------------------------------)

[Raj Namdev](https://medium.com/%40rajnamdev?source=post_page---byline--4f67437ba6c7---------------------------------------)

8 min read

·

Aug 14, 2026

--

[Listen](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2Fplans%3Fdimension%3Dpost_audio_button%26postId%3D4f67437ba6c7&operation=register&redirect=https%3A%2F%2Finfosecwriteups.com%2Fhow-a-single-http-redirect-bypassed-ssrf-filters-on-4-programs-over-8-years-4f67437ba6c7&source=---header_actions--4f67437ba6c7---------------------post_audio_button------------------)

Share

Press enter or click to view image in full size

![]()

> ***30-Second Version:*** *One SSRF bypass technique — a single HTTP redirect — worked against Infogram (2017), Slack (2018), Bitwarden (2020), and Rocket.Chat (2025). Four unrelated companies, eight years apart, the exact same root cause every time: the filter checks the URL you submit, never the URL the redirect actually sends you to.*

8 years.

That’s the gap between the earliest disclosed report using this exact technique and the most recent one. Same bypass. Same missing check. Four completely unrelated companies never learned from each other’s mistake, because the mistake never got treated as a pattern — just four separate bugs, four separate fixes, four separate teams that had no reason to know about the other three.

The simplest SSRF bypass in this dataset doesn’t use NAT64 IPv6 prefixes, DNS rebinding, or URL parser inconsistencies. It uses a 301 redirect. The server validates the URL it receives. It never validates the URL it follows.

## Why This Matters

SSRF filters are everywhere now. Most programs handling user-supplied URLs have some form of protection — IP blocklists, DNS resolution checks, protocol restrictions. If the obvious payloads get blocked during testing, the natural assumption is that SSRF is…

--

--

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:96:96/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--4f67437ba6c7---------------------------------------)

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:128:128/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--4f67437ba6c7---------------------------------------)

[## Published in InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---post_publication_info--4f67437ba6c7---------------------------------------)

[88K followers](/followers?source=post_page---post_publication_info--4f67437ba6c7---------------------------------------)

·[Last published 1 day ago](/one-email-one-click-one-enterprise-wide-ransomware-incident-995808f1150a?source=post_page---post_publication_info--4f67437ba6c7---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

[![Raj Namdev](https://miro.medium.com/v2/resize:fill:96:96/1*qKc3NlEudBR8LvTVmc0eBA.jpeg)](https://medium.com/%40rajnamdev?source=post_page---post_author_info--4f67437ba6c7---------------------------------------)

[![Raj Namdev](https://miro.medium.com/v2/resize:fill:128:128/1*qKc3NlEudBR8LvTVmc0eBA.jpeg)](https://medium.com/%40rajnamdev?source=post_page---post_author_info--4f67437ba6c7---------------------------------------)

[## Written by Raj Namdev](https://medium.com/%40rajnamdev?source=post_page---post_author_info--4f67437ba6c7---------------------------------------)

[36 followers](https://medium.com/%40rajnamdev/followers?source=post_page---post_author_info--4f67437ba6c7---------------------------------------)

·[5 following](https://medium.com/%40rajnamdev/following?source=post_page---post_author_info--4f67437ba6c7---------------------------------------)

Cybersecurity Writer · Breaking down real vulnerabilities, exploits & attack surfaces · Hands-on labs, real code, no fluff

[Help](https://help.medium.com/hc/en-us?source=post_page-----4f67437ba6c7---------------------------------------)

[Status](https://status.medium.com/?source=post_page-----4f67437ba6c7---------------------------------------)

[About](https://medium.com/about?autoplay=1&source=post_page-----4f67437ba6c7---------------------------------------)

[Careers](https://medium.com/jobs-at-medium/work-at-medium-959d1a85284e?source=post_page-----4f67437ba6c7---------------------------------------)

Press

[Blog](https://blog.medium.com/?source=post_page-----4f67437ba6c7---------------------------------------)

[Store](https://medium.com/store)

[Privacy](https://policy.medium.com/medium-privacy-policy-f03bf92035c9?source=post_page-----4f67437ba6c7---------------------------------------)

[Rules](https://policy.medium.com/medium-rules-30e5502c4eb4?source=post_page-----4f67437ba6c7---------------------------------------)

[Terms](https://policy.medium.com/medium-terms-of-service-9...