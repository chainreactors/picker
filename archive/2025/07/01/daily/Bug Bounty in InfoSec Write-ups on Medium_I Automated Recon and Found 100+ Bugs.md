---
title: I Automated Recon and Found 100+ Bugs
url: https://infosecwriteups.com/i-automated-recon-and-found-100-bugs-a6c68b6360eb?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2025-07-01
fetch_date: 2025-10-06T23:52:20.062537
---

# I Automated Recon and Found 100+ Bugs

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2Fa6c68b6360eb&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fi-automated-recon-and-found-100-bugs-a6c68b6360eb&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fi-automated-recon-and-found-100-bugs-a6c68b6360eb&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-a6c68b6360eb---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-a6c68b6360eb---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

Member-only story

# I Automated Recon and Found 100+ Bugs

## This One Strategy 10X’d My Bug Bounty Earnings

[![Ibtissam hammadi](https://miro.medium.com/v2/resize:fill:64:64/1*UlSONScgC0yYgoSEJfzq_A.jpeg)](https://medium.com/%40ibtissamhammadi1?source=post_page---byline--a6c68b6360eb---------------------------------------)

[Ibtissam hammadi](https://medium.com/%40ibtissamhammadi1?source=post_page---byline--a6c68b6360eb---------------------------------------)

3 min read

·

Jun 30, 2025

--

11

Share

I found a **critical SSRF flaw in a Fortune 500 company** — **$10,000 payout** — using a **recon method most hackers ignore**.

Press enter or click to view image in full size

![]()

*The exact recon dashboard that found the $10K SSRF flaw (full setup in Phase 5)*

But here’s the truth: **90% of hackers fail at recon**. They jump straight into scanning, missing **hidden subdomains, forgotten APIs, and leaked credentials** that could’ve been **easy bugs**.

*Most hackers skip these 3 recon phases — here’s why they’re wrong.*

### Who Am I? (Why Should You Listen?)

I’m not a “guru.” Just a hacker who:

* **Ranked Top 50 on** [**HackerOne**](https://www.hackerone.com/) (200+ Hall of Fame entries).
* **Built ARWAD** (an open-source **automated recon tool**).
* **Found 100+ bugs** in companies like Google, Uber, and Shopify.

Tools won’t save you if your recon mindset is broken.

### Recon Mindset > Tools

**The best hackers spend 70% of their time on recon.**

**Passive Recon** (Silent, no direct interaction):

* **Shodan** (Find exposed databases).
* **Wayback Machine** (Discover deleted pages with vulnerabilities).
* **GitHub Leaks** (Search for exposed API keys).

--

--

11

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:96:96/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--a6c68b6360eb---------------------------------------)

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:128:128/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--a6c68b6360eb---------------------------------------)

Follow

[## Published in InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---post_publication_info--a6c68b6360eb---------------------------------------)

[71K followers](/followers?source=post_page---post_publication_info--a6c68b6360eb---------------------------------------)

·[Last published 3 hours ago](/actuator-unleashed-a-guide-to-finding-and-exploiting-spring-boot-actuator-endpoints-29252dcd9d79?source=post_page---post_publication_info--a6c68b6360eb---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow

[![Ibtissam hammadi](https://miro.medium.com/v2/resize:fill:96:96/1*UlSONScgC0yYgoSEJfzq_A.jpeg)](https://medium.com/%40ibtissamhammadi1?source=post_page---post_author_info--a6c68b6360eb---------------------------------------)

[![Ibtissam hammadi](https://miro.medium.com/v2/resize:fill:128:128/1*UlSONScgC0yYgoSEJfzq_A.jpeg)](https://medium.com/%40ibtissamhammadi1?source=post_page---post_author_info--a6c68b6360eb---------------------------------------)

[## Written by Ibtissam hammadi](https://medium.com/%40ibtissamhammadi1?source=post_page---post_author_info--a6c68b6360eb---------------------------------------)

[4.2K followers](https://medium.com/%40ibtissamhammadi1/followers?source=post_page---post_author_info--a6c68b6360eb---------------------------------------)

·[102 following](https://medium.com/%40ibtissamhammadi1/following?source=post_page---post_author_info--a6c68b6360eb---------------------------------------)

I am a Senior Data Scientist exploring Cybersecurity, Infosec, Programming, and AI technologies.

## Responses (11)

See all responses

[Help](https://help.medium.com/hc/en-us?source=post_page-----a6c68b6360eb---------------------------------------)

[Status](https://status.medium.com/?source=post_page-----a6c68b6360eb---------------------------------------)

[About](https://medium.com/about?autoplay=1&source=post_page-----a6c68b6360eb---------------------------------------)

[Careers](https://medium.com/jobs-at-medium/work-at-medium-959d1a85284e?source=post_page-----a6c68b6360eb---------------------------------------)

Press

[Blog](https://blog.medium.com/?source=post_page-----a6c68b6360eb---------------------------------------)

[Privacy](https://policy.medium.com/medium-privacy-policy-f03bf92035c9?source=post_page-----a6c68b6360eb---------------------------------------)

[Rules](https://policy.medium.com/medium-rules-30e5502c4eb4?source=post_page-----a6c68b6360eb---------------------------------------)

[Terms](https://policy.medium.com/medium-terms-of-service-9db0094a1e0f?source=post_page-----a6c68b6360eb---------------------------------------)

[Text to speech](https://speechify.com/medium?source=post_page-----a6c68b6360eb---------------------------------------)