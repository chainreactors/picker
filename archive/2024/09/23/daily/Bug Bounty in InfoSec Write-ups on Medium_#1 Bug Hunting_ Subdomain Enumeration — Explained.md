---
title: #1 Bug Hunting: Subdomain Enumeration — Explained
url: https://infosecwriteups.com/1-bug-hunting-subdomain-enumeration-explained-389e6fcb3f62?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2024-09-23
fetch_date: 2025-10-06T18:22:54.506667
---

# #1 Bug Hunting: Subdomain Enumeration — Explained

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2F389e6fcb3f62&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2F1-bug-hunting-subdomain-enumeration-explained-389e6fcb3f62&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2F1-bug-hunting-subdomain-enumeration-explained-389e6fcb3f62&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[Mastodon](https://me.dm/%40ommaniya)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-389e6fcb3f62---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-389e6fcb3f62---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

Member-only story

# #1 Bug Hunting: Subdomain Enumeration — Explained

[![Om Maniya](https://miro.medium.com/v2/resize:fill:64:64/1*_O0rR5KNt1fvXaY3SF35dg.jpeg)](https://ommaniya.site/?source=post_page---byline--389e6fcb3f62---------------------------------------)

[Om Maniya](https://ommaniya.site/?source=post_page---byline--389e6fcb3f62---------------------------------------)

4 min read

·

Sep 21, 2024

--

2

Share

Press enter or click to view image in full size

![]()

Photo by Christopher Gower on Unsplash

## Subdomain Enumeration

Subdomain enumeration is the process of identifying all possible subdomains associated with a given domain. It is a critical part of information gathering in cybersecurity, as it broadens the attack surface, uncovers hidden applications, and reveals forgotten subdomains. This can help security professionals or ethical hackers find potential vulnerabilities that would otherwise remain unnoticed.

In this blog post, we will explore how to perform subdomain enumeration and retrieve active subdomains efficiently. **Important:** Always ensure that you have permission to perform this process on any domain or application, as overloading the server could lead to crashes or other issues.

Let’s dive into the tools commonly used for subdomain enumeration.

## Tools for Subdomain Enumeration

1. [Subfinder:](https://github.com/projectdiscovery/subfinder) Subfinder is a subdomain discovery tool that helps find valid subdomains for a given domain by utilizing digital sources like Censys, Chaos, Recon.dev, Shodan, Spyse, VirusTotal, and many others. It relies on passive subdomain enumeration techniques.

**Example:**

Below is an example of scanning for subdomains under `*.nasa.gov`, which currently has a Vulnerability Disclosure…

--

--

2

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:96:96/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--389e6fcb3f62---------------------------------------)

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:128:128/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--389e6fcb3f62---------------------------------------)

Follow

[## Published in InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---post_publication_info--389e6fcb3f62---------------------------------------)

[71K followers](/followers?source=post_page---post_publication_info--389e6fcb3f62---------------------------------------)

·[Last published 3 hours ago](/baby-dfc2547dc387?source=post_page---post_publication_info--389e6fcb3f62---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow

[![Om Maniya](https://miro.medium.com/v2/resize:fill:96:96/1*_O0rR5KNt1fvXaY3SF35dg.jpeg)](https://ommaniya.site/?source=post_page---post_author_info--389e6fcb3f62---------------------------------------)

[![Om Maniya](https://miro.medium.com/v2/resize:fill:128:128/1*_O0rR5KNt1fvXaY3SF35dg.jpeg)](https://ommaniya.site/?source=post_page---post_author_info--389e6fcb3f62---------------------------------------)

[## Written by Om Maniya](https://ommaniya.site/?source=post_page---post_author_info--389e6fcb3f62---------------------------------------)

[89 followers](https://ommaniya.site/followers?source=post_page---post_author_info--389e6fcb3f62---------------------------------------)

·[37 following](https://medium.com/%40ommaniya/following?source=post_page---post_author_info--389e6fcb3f62---------------------------------------)

## Responses (2)

See all responses

[Help](https://help.medium.com/hc/en-us?source=post_page-----389e6fcb3f62---------------------------------------)

[Status](https://status.medium.com/?source=post_page-----389e6fcb3f62---------------------------------------)

[About](https://medium.com/about?autoplay=1&source=post_page-----389e6fcb3f62---------------------------------------)

[Careers](https://medium.com/jobs-at-medium/work-at-medium-959d1a85284e?source=post_page-----389e6fcb3f62---------------------------------------)

Press

[Blog](https://blog.medium.com/?source=post_page-----389e6fcb3f62---------------------------------------)

[Privacy](https://policy.medium.com/medium-privacy-policy-f03bf92035c9?source=post_page-----389e6fcb3f62---------------------------------------)

[Rules](https://policy.medium.com/medium-rules-30e5502c4eb4?source=post_page-----389e6fcb3f62---------------------------------------)

[Terms](https://policy.medium.com/medium-terms-of-service-9db0094a1e0f?source=post_page-----389e6fcb3f62---------------------------------------)

[Text to speech](https://speechify.com/medium?source=post_page-----389e6fcb3f62---------------------------------------)