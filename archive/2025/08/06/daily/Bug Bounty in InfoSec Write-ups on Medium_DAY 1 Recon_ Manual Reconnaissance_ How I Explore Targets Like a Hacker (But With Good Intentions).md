---
title: DAY 1 Recon: Manual Reconnaissance: How I Explore Targets Like a Hacker (But With Good Intentions)
url: https://infosecwriteups.com/day-1-recon-manual-reconnaissance-how-i-explore-targets-like-a-hacker-but-with-good-intentions-04b61864d1ea?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2025-08-06
fetch_date: 2025-10-07T00:47:46.754470
---

# DAY 1 Recon: Manual Reconnaissance: How I Explore Targets Like a Hacker (But With Good Intentions)

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2F04b61864d1ea&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fday-1-recon-manual-reconnaissance-how-i-explore-targets-like-a-hacker-but-with-good-intentions-04b61864d1ea&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fday-1-recon-manual-reconnaissance-how-i-explore-targets-like-a-hacker-but-with-good-intentions-04b61864d1ea&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-04b61864d1ea---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-04b61864d1ea---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

Member-only story

# DAY 1 Recon: **Manual Reconnaissance: How I Explore Targets Like a Hacker (But With Good Intentions)**

[![Ayush Kumar](https://miro.medium.com/v2/resize:fill:64:64/1*02Ex2WoqjL8muk2ApxE_mA.jpeg)](https://3xabyt3.medium.com/?source=post_page---byline--04b61864d1ea---------------------------------------)

[Ayush Kumar](https://3xabyt3.medium.com/?source=post_page---byline--04b61864d1ea---------------------------------------)

3 min read

·

Aug 4, 2025

--

Share

Before the tools come out, I like to get my hands dirty — and here’s why that matters.

Press enter or click to view image in full size

![]()

When I first got into ethical hacking, I thought all the magic came from tools. Nmap, Burp Suite, Nikto — the usual suspects. But after a few real-world tests, I realized something weird:

**The best stuff doesn’t come from tools. It comes from curiosity.**

Let me explain.

## Why Manual Recon Matters

Imagine trying to understand a new city just by reading reviews and looking at maps. You’d miss the smell of the streets, the vibe of the neighborhood, the places only locals know.

Manual reconnaissance is kinda like that. It’s when you pause the scanning tools for a bit and **explore the target like a real human would** — observing, clicking around, poking at things.

That’s what real attackers do. They don’t start with tools. They **start by thinking**.

## What I Look For First (Before Scanning Anything)

When I hit a new target, especially a web app or site, I start with the browser. Yep, plain old Chrome or Firefox.

--

--

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:96:96/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--04b61864d1ea---------------------------------------)

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:128:128/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--04b61864d1ea---------------------------------------)

Follow

[## Published in InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---post_publication_info--04b61864d1ea---------------------------------------)

[71K followers](/followers?source=post_page---post_publication_info--04b61864d1ea---------------------------------------)

·[Last published 4 hours ago](/actuator-unleashed-a-guide-to-finding-and-exploiting-spring-boot-actuator-endpoints-29252dcd9d79?source=post_page---post_publication_info--04b61864d1ea---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow

[![Ayush Kumar](https://miro.medium.com/v2/resize:fill:96:96/1*02Ex2WoqjL8muk2ApxE_mA.jpeg)](https://3xabyt3.medium.com/?source=post_page---post_author_info--04b61864d1ea---------------------------------------)

[![Ayush Kumar](https://miro.medium.com/v2/resize:fill:128:128/1*02Ex2WoqjL8muk2ApxE_mA.jpeg)](https://3xabyt3.medium.com/?source=post_page---post_author_info--04b61864d1ea---------------------------------------)

[## Written by Ayush Kumar](https://3xabyt3.medium.com/?source=post_page---post_author_info--04b61864d1ea---------------------------------------)

[681 followers](https://3xabyt3.medium.com/followers?source=post_page---post_author_info--04b61864d1ea---------------------------------------)

·[16 following](https://medium.com/%403xabyt3/following?source=post_page---post_author_info--04b61864d1ea---------------------------------------)

Hello eveyone , this is Ayush from India. I write about DevOps, Cloud, Cyber Security, Programming

## No responses yet

[Help](https://help.medium.com/hc/en-us?source=post_page-----04b61864d1ea---------------------------------------)

[Status](https://status.medium.com/?source=post_page-----04b61864d1ea---------------------------------------)

[About](https://medium.com/about?autoplay=1&source=post_page-----04b61864d1ea---------------------------------------)

[Careers](https://medium.com/jobs-at-medium/work-at-medium-959d1a85284e?source=post_page-----04b61864d1ea---------------------------------------)

Press

[Blog](https://blog.medium.com/?source=post_page-----04b61864d1ea---------------------------------------)

[Privacy](https://policy.medium.com/medium-privacy-policy-f03bf92035c9?source=post_page-----04b61864d1ea---------------------------------------)

[Rules](https://policy.medium.com/medium-rules-30e5502c4eb4?source=post_page-----04b61864d1ea---------------------------------------)

[Terms](https://policy.medium.com/medium-terms-of-service-9db0094a1e0f?source=post_page-----04b61864d1ea---------------------------------------)

[Text to speech](https://speechify.com/medium?source=post_page-----04b61864d1ea---------------------------------------)