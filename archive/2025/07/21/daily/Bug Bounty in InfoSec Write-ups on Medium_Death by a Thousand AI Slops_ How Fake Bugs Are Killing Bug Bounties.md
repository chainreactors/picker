---
title: Death by a Thousand AI Slops: How Fake Bugs Are Killing Bug Bounties
url: https://infosecwriteups.com/death-by-a-thousand-ai-slops-how-fake-bugs-are-killing-bug-bounties-e4a8803edab7?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2025-07-21
fetch_date: 2025-10-06T23:21:27.143894
---

# Death by a Thousand AI Slops: How Fake Bugs Are Killing Bug Bounties

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2Fe4a8803edab7&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fdeath-by-a-thousand-ai-slops-how-fake-bugs-are-killing-bug-bounties-e4a8803edab7&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fdeath-by-a-thousand-ai-slops-how-fake-bugs-are-killing-bug-bounties-e4a8803edab7&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-e4a8803edab7---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-e4a8803edab7---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

Member-only story

# Death by a Thousand AI Slops: How Fake Bugs Are Killing Bug Bounties

[![Aaron](https://miro.medium.com/v2/resize:fill:64:64/1*hRBr6DPK7xBp4wXLReIN6A.jpeg)](https://medium.com/%40AT24?source=post_page---byline--e4a8803edab7---------------------------------------)

[Aaron](https://medium.com/%40AT24?source=post_page---byline--e4a8803edab7---------------------------------------)

4 min read

·

Jul 19, 2025

--

Share

> “If this continues, we’ll drown. Not in bugs — but in nonsense.”

Press enter or click to view image in full size

![]()

When AI Hunts Bugs That Don’t Exist: The Rising Tide of Hallucinated Vulnerabilities in Security Research

💡 Not a Medium member? You can still read this article in full with [[Click here]](https://medium.com/%40AT24/death-by-a-thousand-ai-slops-how-fake-bugs-are-killing-bug-bounties-e4a8803edab7?sk=2a14c9b6573114915cd38a5d04c37b89)

That’s not the rant of a burned-out developer. That’s **Daniel Stenberg**, the creator and lead maintainer of curl —a tiny command-line utility you’ve probably never thought about, but one that quietly moves the internet every second of every day.

**curl** is everywhere. It’s in your terminal, your Docker containers, your apps, your APIs. It’s used by Google, Apple, Facebook, and thousands more. It's one of the quiet backbones of the internet.

So why is its maintainer sounding the alarm?

Because in 2025, something wild is happening: **AI-generated bug reports are flooding open source projects** — and it’s not helpful, it’s harmful.

## The War Zone: HackerOne and the AI Slop Flood

If you haven’t heard of it before, **HackerOne** is a bug bounty platform. It’s a place where security researchers get paid to find vulnerabilities in real-world software. Companies use it to outsource some of their security testing to ethical hackers.

--

--

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:96:96/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--e4a8803edab7---------------------------------------)

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:128:128/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--e4a8803edab7---------------------------------------)

Follow

[## Published in InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---post_publication_info--e4a8803edab7---------------------------------------)

[71K followers](/followers?source=post_page---post_publication_info--e4a8803edab7---------------------------------------)

·[Last published 2 hours ago](/actuator-unleashed-a-guide-to-finding-and-exploiting-spring-boot-actuator-endpoints-29252dcd9d79?source=post_page---post_publication_info--e4a8803edab7---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow

[![Aaron](https://miro.medium.com/v2/resize:fill:96:96/1*hRBr6DPK7xBp4wXLReIN6A.jpeg)](https://medium.com/%40AT24?source=post_page---post_author_info--e4a8803edab7---------------------------------------)

[![Aaron](https://miro.medium.com/v2/resize:fill:128:128/1*hRBr6DPK7xBp4wXLReIN6A.jpeg)](https://medium.com/%40AT24?source=post_page---post_author_info--e4a8803edab7---------------------------------------)

[## Written by Aaron](https://medium.com/%40AT24?source=post_page---post_author_info--e4a8803edab7---------------------------------------)

[100 followers](https://medium.com/%40AT24/followers?source=post_page---post_author_info--e4a8803edab7---------------------------------------)

·[20 following](https://medium.com/%40AT24/following?source=post_page---post_author_info--e4a8803edab7---------------------------------------)

Curious mind writing across tech, business, hacking, and big conversations. One story, one lesson at a time.

## No responses yet

[Help](https://help.medium.com/hc/en-us?source=post_page-----e4a8803edab7---------------------------------------)

[Status](https://status.medium.com/?source=post_page-----e4a8803edab7---------------------------------------)

[About](https://medium.com/about?autoplay=1&source=post_page-----e4a8803edab7---------------------------------------)

[Careers](https://medium.com/jobs-at-medium/work-at-medium-959d1a85284e?source=post_page-----e4a8803edab7---------------------------------------)

Press

[Blog](https://blog.medium.com/?source=post_page-----e4a8803edab7---------------------------------------)

[Privacy](https://policy.medium.com/medium-privacy-policy-f03bf92035c9?source=post_page-----e4a8803edab7---------------------------------------)

[Rules](https://policy.medium.com/medium-rules-30e5502c4eb4?source=post_page-----e4a8803edab7---------------------------------------)

[Terms](https://policy.medium.com/medium-terms-of-service-9db0094a1e0f?source=post_page-----e4a8803edab7---------------------------------------)

[Text to speech](https://speechify.com/medium?source=post_page-----e4a8803edab7---------------------------------------)