---
title: Comprehensive Bug Bounty Hunting Methodology (2024 Edition)
url: https://infosecwriteups.com/comprehensive-bug-bounty-hunting-checklist-2024-edition-4abb3a9cbe66?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2024-11-15
fetch_date: 2025-10-06T19:17:56.435054
---

# Comprehensive Bug Bounty Hunting Methodology (2024 Edition)

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2F4abb3a9cbe66&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fcomprehensive-bug-bounty-hunting-checklist-2024-edition-4abb3a9cbe66&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fcomprehensive-bug-bounty-hunting-checklist-2024-edition-4abb3a9cbe66&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-4abb3a9cbe66---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-4abb3a9cbe66---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

Member-only story

# Comprehensive Bug Bounty Hunting Methodology (2024 Edition)

[![Krishna Kumar](https://miro.medium.com/v2/resize:fill:64:64/1*BZbDP0Rryv1evj1rWveHPA.jpeg)](https://xalgord.medium.com/?source=post_page---byline--4abb3a9cbe66---------------------------------------)

[Krishna Kumar](https://xalgord.medium.com/?source=post_page---byline--4abb3a9cbe66---------------------------------------)

11 min read

·

Oct 31, 2024

--

5

Share

Welcome to your complete bug bounty guide! 🕵️ This is designed for beginners, but even if you’re experienced, there’s always something new to learn or tools to discover. With this checklist, you’ll not only understand the “what” but also the “how” and “why.” Each section is filled with tools, commands, and examples to make your bug bounty journey smooth and productive. For non-premium medium members, you can read it for free using this link: [https://infosecwriteups.com/comprehensive-bug-bounty-hunting-checklist-2024-edition-4abb3a9cbe66?source=friends\_link&sk=8a71eca24d629fda5cb8a2dbcc6a27b5](/comprehensive-bug-bounty-hunting-checklist-2024-edition-4abb3a9cbe66?sk=8a71eca24d629fda5cb8a2dbcc6a27b5)

## 1. Reconnaissance: The First Step to Success

The recon phase is all about gathering information. The more data you have on your target, the higher your chances of finding vulnerabilities. This stage sets the foundation for everything that follows.

### 1.1 Subdomain Enumeration

Subdomains often hide forgotten features, admin panels, or unpatched vulnerabilities. Use multiple tools for better coverage.

### Passive Subdomain Enumeration

Passive enumeration relies on third-party sources and APIs, such as certificate transparency logs, search engines, and public DNS databases.

* **Tools**: `Subfinder`, `Findomain`, `Amass`, `Assetfinder`, `Sublist3r`, `Shuffledns`
* **Subfinder Example:**

--

--

5

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:96:96/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--4abb3a9cbe66---------------------------------------)

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:128:128/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--4abb3a9cbe66---------------------------------------)

Follow

[## Published in InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---post_publication_info--4abb3a9cbe66---------------------------------------)

[71K followers](/followers?source=post_page---post_publication_info--4abb3a9cbe66---------------------------------------)

·[Last published 4 hours ago](/baby-dfc2547dc387?source=post_page---post_publication_info--4abb3a9cbe66---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow

[![Krishna Kumar](https://miro.medium.com/v2/resize:fill:96:96/1*BZbDP0Rryv1evj1rWveHPA.jpeg)](https://xalgord.medium.com/?source=post_page---post_author_info--4abb3a9cbe66---------------------------------------)

[![Krishna Kumar](https://miro.medium.com/v2/resize:fill:128:128/1*BZbDP0Rryv1evj1rWveHPA.jpeg)](https://xalgord.medium.com/?source=post_page---post_author_info--4abb3a9cbe66---------------------------------------)

[## Written by Krishna Kumar](https://xalgord.medium.com/?source=post_page---post_author_info--4abb3a9cbe66---------------------------------------)

[264 followers](https://xalgord.medium.com/followers?source=post_page---post_author_info--4abb3a9cbe66---------------------------------------)

·[13 following](https://medium.com/%40xalgord/following?source=post_page---post_author_info--4abb3a9cbe66---------------------------------------)

Penetration tester | Bug Bounty Hunter

## Responses (5)

See all responses

[Help](https://help.medium.com/hc/en-us?source=post_page-----4abb3a9cbe66---------------------------------------)

[Status](https://status.medium.com/?source=post_page-----4abb3a9cbe66---------------------------------------)

[About](https://medium.com/about?autoplay=1&source=post_page-----4abb3a9cbe66---------------------------------------)

[Careers](https://medium.com/jobs-at-medium/work-at-medium-959d1a85284e?source=post_page-----4abb3a9cbe66---------------------------------------)

Press

[Blog](https://blog.medium.com/?source=post_page-----4abb3a9cbe66---------------------------------------)

[Privacy](https://policy.medium.com/medium-privacy-policy-f03bf92035c9?source=post_page-----4abb3a9cbe66---------------------------------------)

[Rules](https://policy.medium.com/medium-rules-30e5502c4eb4?source=post_page-----4abb3a9cbe66---------------------------------------)

[Terms](https://policy.medium.com/medium-terms-of-service-9db0094a1e0f?source=post_page-----4abb3a9cbe66---------------------------------------)

[Text to speech](https://speechify.com/medium?source=post_page-----4abb3a9cbe66---------------------------------------)