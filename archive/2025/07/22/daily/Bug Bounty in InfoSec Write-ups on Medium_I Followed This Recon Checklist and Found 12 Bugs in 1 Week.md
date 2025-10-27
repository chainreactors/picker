---
title: I Followed This Recon Checklist and Found 12 Bugs in 1 Week
url: https://infosecwriteups.com/i-followed-this-recon-checklist-and-found-12-bugs-in-1-week-1e546a0d8b2e?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2025-07-22
fetch_date: 2025-10-06T23:27:11.096117
---

# I Followed This Recon Checklist and Found 12 Bugs in 1 Week

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2F1e546a0d8b2e&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fi-followed-this-recon-checklist-and-found-12-bugs-in-1-week-1e546a0d8b2e&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fi-followed-this-recon-checklist-and-found-12-bugs-in-1-week-1e546a0d8b2e&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-1e546a0d8b2e---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-1e546a0d8b2e---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

Member-only story

# I Followed This Recon Checklist and Found 12 Bugs in 1 Week

## This Forgotten Recon Trick Doubled My Bug Bounty Valid Reports

[![Ibtissam hammadi](https://miro.medium.com/v2/resize:fill:64:64/1*UlSONScgC0yYgoSEJfzq_A.jpeg)](https://medium.com/%40ibtissamhammadi1?source=post_page---byline--1e546a0d8b2e---------------------------------------)

[Ibtissam hammadi](https://medium.com/%40ibtissamhammadi1?source=post_page---byline--1e546a0d8b2e---------------------------------------)

4 min read

·

Jul 21, 2025

--

11

Share

I was ready to quit bug bounty hunting. After weeks of zero valid reports, I felt like I was wasting time — until I stumbled upon a **forgotten recon trick** that flipped everything.

Press enter or click to view image in full size

![Recon Checklist]()

Photo by [Wai Yan Moe](https://unsplash.com/%40wy_m?utm_source=medium&utm_medium=referral) on [Unsplash](https://unsplash.com/?utm_source=medium&utm_medium=referral)

In just 7 days, I found **12 bugs** (3 XSS, 2 IDORs, 1 SSRF, and more).

Here’s the exact checklist that made it happen.

### The Pain Point: Why Most Beginners Fail at Recon

Most hunters jump straight into **automated tools** without a strategy. They miss **critical steps** like:

* **Skipping subdomain permutations** (missing hidden test.env.example.com).
* **Ignoring JavaScript files** (goldmines for API keys and endpoints).
* **Relying only on passive scans** (no active brute-forcing for params).

I learned the hard way — **recon isn’t about tools. It’s about workflow.** Let me break down mine.

### Step-by-Step Recon Checklist

**Step 1: Subdomain Enumeration (Passive + Active)**

**Tools:** Amass, crt.sh, FFUF

--

--

11

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:96:96/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--1e546a0d8b2e---------------------------------------)

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:128:128/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--1e546a0d8b2e---------------------------------------)

Follow

[## Published in InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---post_publication_info--1e546a0d8b2e---------------------------------------)

[71K followers](/followers?source=post_page---post_publication_info--1e546a0d8b2e---------------------------------------)

·[Last published 3 hours ago](/actuator-unleashed-a-guide-to-finding-and-exploiting-spring-boot-actuator-endpoints-29252dcd9d79?source=post_page---post_publication_info--1e546a0d8b2e---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow

[![Ibtissam hammadi](https://miro.medium.com/v2/resize:fill:96:96/1*UlSONScgC0yYgoSEJfzq_A.jpeg)](https://medium.com/%40ibtissamhammadi1?source=post_page---post_author_info--1e546a0d8b2e---------------------------------------)

[![Ibtissam hammadi](https://miro.medium.com/v2/resize:fill:128:128/1*UlSONScgC0yYgoSEJfzq_A.jpeg)](https://medium.com/%40ibtissamhammadi1?source=post_page---post_author_info--1e546a0d8b2e---------------------------------------)

[## Written by Ibtissam hammadi](https://medium.com/%40ibtissamhammadi1?source=post_page---post_author_info--1e546a0d8b2e---------------------------------------)

[4.2K followers](https://medium.com/%40ibtissamhammadi1/followers?source=post_page---post_author_info--1e546a0d8b2e---------------------------------------)

·[102 following](https://medium.com/%40ibtissamhammadi1/following?source=post_page---post_author_info--1e546a0d8b2e---------------------------------------)

I am a Senior Data Scientist exploring Cybersecurity, Infosec, Programming, and AI technologies.

## Responses (11)

See all responses

[Help](https://help.medium.com/hc/en-us?source=post_page-----1e546a0d8b2e---------------------------------------)

[Status](https://status.medium.com/?source=post_page-----1e546a0d8b2e---------------------------------------)

[About](https://medium.com/about?autoplay=1&source=post_page-----1e546a0d8b2e---------------------------------------)

[Careers](https://medium.com/jobs-at-medium/work-at-medium-959d1a85284e?source=post_page-----1e546a0d8b2e---------------------------------------)

Press

[Blog](https://blog.medium.com/?source=post_page-----1e546a0d8b2e---------------------------------------)

[Privacy](https://policy.medium.com/medium-privacy-policy-f03bf92035c9?source=post_page-----1e546a0d8b2e---------------------------------------)

[Rules](https://policy.medium.com/medium-rules-30e5502c4eb4?source=post_page-----1e546a0d8b2e---------------------------------------)

[Terms](https://policy.medium.com/medium-terms-of-service-9db0094a1e0f?source=post_page-----1e546a0d8b2e---------------------------------------)

[Text to speech](https://speechify.com/medium?source=post_page-----1e546a0d8b2e---------------------------------------)