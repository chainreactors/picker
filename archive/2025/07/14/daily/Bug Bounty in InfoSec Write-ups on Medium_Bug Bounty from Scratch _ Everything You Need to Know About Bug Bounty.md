---
title: Bug Bounty from Scratch | Everything You Need to Know About Bug Bounty
url: https://infosecwriteups.com/bug-bounty-from-scratch-everything-you-need-to-know-about-bug-bounty-7188d57d36f2?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2025-07-14
fetch_date: 2025-10-06T23:21:34.695479
---

# Bug Bounty from Scratch | Everything You Need to Know About Bug Bounty

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2F7188d57d36f2&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fbug-bounty-from-scratch-everything-you-need-to-know-about-bug-bounty-7188d57d36f2&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fbug-bounty-from-scratch-everything-you-need-to-know-about-bug-bounty-7188d57d36f2&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-7188d57d36f2---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-7188d57d36f2---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

Member-only story

# 🐞Bug Bounty from Scratch | Everything You Need to Know About Bug Bounty

[![Abhijeet kumawat](https://miro.medium.com/v2/resize:fill:64:64/1*lwXXZkQ5xsjHJniXHn-9Tw.jpeg)](https://medium.com/%40kumawatabhijeet2002?source=post_page---byline--7188d57d36f2---------------------------------------)

[Abhijeet kumawat](https://medium.com/%40kumawatabhijeet2002?source=post_page---byline--7188d57d36f2---------------------------------------)

5 min read

·

Jul 13, 2025

--

24

Share

📌Free Article [Link](https://medium.com/%40kumawatabhijeet2002/7188d57d36f2?sk=3638ae73b5dab364943cf119efcdb5af)

> *“Bug bounty changed my life… and it might change yours too.”*

Hey hackers 👋

I’m **Abhijeet Kumawat** — a passionate cybersecurity enthusiast, ethical hacker, and someone who once thought, *“I’ll never find a real bug.”*

Fast forward a bit… and now I’ve reported bugs on platforms like **NASA, Sony, US Gov.., etc. A**nd many private programs or Self-Hosted Programs. This isn’t to brag. I’m still learning. I still feel the same thrill every time I spot something suspicious.

But one thing I realized, what?

> *The hardest part is just getting started.*

So I created this **“Bug Bounty from Scratch”** series — for people like YOU. Whether you’re a total beginner or someone who’s heard the word “bug bounty” floating around on Twitter or LinkedIn, I promise you: **this series will be your guidebook.**

![]()

Created by Gemini

[## Deep Recon Methodology for Bug Bounty Hunters | Part-1

### Hello, everyone! 👋

osintteam.blog](https://osintteam.blog/deep-recon-methodology-for-bug-bounty-hunters-part-1-54bdac09dcf4?source=post_page-----7188d57d36f2---------------------------------------)

--

--

24

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:96:96/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--7188d57d36f2---------------------------------------)

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:128:128/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--7188d57d36f2---------------------------------------)

Follow

[## Published in InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---post_publication_info--7188d57d36f2---------------------------------------)

[71K followers](/followers?source=post_page---post_publication_info--7188d57d36f2---------------------------------------)

·[Last published 2 hours ago](/actuator-unleashed-a-guide-to-finding-and-exploiting-spring-boot-actuator-endpoints-29252dcd9d79?source=post_page---post_publication_info--7188d57d36f2---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow

[![Abhijeet kumawat](https://miro.medium.com/v2/resize:fill:96:96/1*lwXXZkQ5xsjHJniXHn-9Tw.jpeg)](https://medium.com/%40kumawatabhijeet2002?source=post_page---post_author_info--7188d57d36f2---------------------------------------)

[![Abhijeet kumawat](https://miro.medium.com/v2/resize:fill:128:128/1*lwXXZkQ5xsjHJniXHn-9Tw.jpeg)](https://medium.com/%40kumawatabhijeet2002?source=post_page---post_author_info--7188d57d36f2---------------------------------------)

[## Written by Abhijeet kumawat](https://medium.com/%40kumawatabhijeet2002?source=post_page---post_author_info--7188d57d36f2---------------------------------------)

[2.4K followers](https://medium.com/%40kumawatabhijeet2002/followers?source=post_page---post_author_info--7188d57d36f2---------------------------------------)

·[33 following](https://medium.com/%40kumawatabhijeet2002/following?source=post_page---post_author_info--7188d57d36f2---------------------------------------)

Radhe Radhe ✨ || Security Researcher || Bug Hunter || Web Application Penetration Tester || Ethical Hacker ||

## Responses (24)

See all responses

[Help](https://help.medium.com/hc/en-us?source=post_page-----7188d57d36f2---------------------------------------)

[Status](https://status.medium.com/?source=post_page-----7188d57d36f2---------------------------------------)

[About](https://medium.com/about?autoplay=1&source=post_page-----7188d57d36f2---------------------------------------)

[Careers](https://medium.com/jobs-at-medium/work-at-medium-959d1a85284e?source=post_page-----7188d57d36f2---------------------------------------)

Press

[Blog](https://blog.medium.com/?source=post_page-----7188d57d36f2---------------------------------------)

[Privacy](https://policy.medium.com/medium-privacy-policy-f03bf92035c9?source=post_page-----7188d57d36f2---------------------------------------)

[Rules](https://policy.medium.com/medium-rules-30e5502c4eb4?source=post_page-----7188d57d36f2---------------------------------------)

[Terms](https://policy.medium.com/medium-terms-of-service-9db0094a1e0f?source=post_page-----7188d57d36f2---------------------------------------)

[Text to speech](https://speechify.com/medium?source=post_page-----7188d57d36f2---------------------------------------)