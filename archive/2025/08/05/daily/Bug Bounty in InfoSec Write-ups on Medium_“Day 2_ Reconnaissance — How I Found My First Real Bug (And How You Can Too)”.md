---
title: “Day 2: Reconnaissance — How I Found My First Real Bug (And How You Can Too)”
url: https://infosecwriteups.com/day-2-reconnaissance-how-i-found-my-first-real-bug-and-how-you-can-too-dbf81cb44069?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2025-08-05
fetch_date: 2025-10-07T00:17:55.290216
---

# “Day 2: Reconnaissance — How I Found My First Real Bug (And How You Can Too)”

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2Fdbf81cb44069&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fday-2-reconnaissance-how-i-found-my-first-real-bug-and-how-you-can-too-dbf81cb44069&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fday-2-reconnaissance-how-i-found-my-first-real-bug-and-how-you-can-too-dbf81cb44069&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-dbf81cb44069---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-dbf81cb44069---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

Member-only story

# “Day 2: Reconnaissance — How I Found My First Real Bug (And How You Can Too)”

[![Aman Sharma](https://miro.medium.com/v2/da:true/resize:fill:64:64/0*gTsmBWudIxLcZoel)](https://amannsharmaa.medium.com/?source=post_page---byline--dbf81cb44069---------------------------------------)

[Aman Sharma](https://amannsharmaa.medium.com/?source=post_page---byline--dbf81cb44069---------------------------------------)

4 min read

·

Aug 3, 2025

--

1

Share

On Day 1, I learned the basics. On Day 2, I got real. I remember staring at a company’s website, completely lost — where do I even start? Then I discovered reconnaissance, and everything changed. That’s when I found my first real-world bug: an exposed admin panel that shouldn’t have been public. Here’s exactly how I did it — step by step.

[free link](https://amannsharmaa.medium.com/day-2-reconnaissance-how-i-found-my-first-real-bug-and-how-you-can-too-dbf81cb44069?sk=030f12d9097b0ea7bf0bf736c4c4f95a)

Press enter or click to view image in full size

![]()

## Step 1: Why Recon Matters (The $15,000 Lesson)

Most beginners (including me) jump straight into hacking forms and inputs. Big mistake.

### Real-World Example:

A hacker named @TomNomNom once found a subdomain takeover on a Fortune 500 company. How? He simply listed all their subdomains and checked for misconfigurations. Payout? $15,000.

Lesson: 90% of hacking is finding the right target.

## Step 2: The 3 Recon Tools I Actually Use (No BS)

Forget complicated setups. Here’s what I use daily:

### 1. Sublist3r (The Subdomain Finder)

* What it does: Finds hidden subdomains (like `admin.example.com`, `dev.example.com`).
* How to use:

--

--

1

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:96:96/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--dbf81cb44069---------------------------------------)

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:128:128/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--dbf81cb44069---------------------------------------)

Follow

[## Published in InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---post_publication_info--dbf81cb44069---------------------------------------)

[71K followers](/followers?source=post_page---post_publication_info--dbf81cb44069---------------------------------------)

·[Last published 3 hours ago](/actuator-unleashed-a-guide-to-finding-and-exploiting-spring-boot-actuator-endpoints-29252dcd9d79?source=post_page---post_publication_info--dbf81cb44069---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow

[![Aman Sharma](https://miro.medium.com/v2/resize:fill:96:96/0*gTsmBWudIxLcZoel)](https://amannsharmaa.medium.com/?source=post_page---post_author_info--dbf81cb44069---------------------------------------)

[![Aman Sharma](https://miro.medium.com/v2/resize:fill:128:128/0*gTsmBWudIxLcZoel)](https://amannsharmaa.medium.com/?source=post_page---post_author_info--dbf81cb44069---------------------------------------)

[## Written by Aman Sharma](https://amannsharmaa.medium.com/?source=post_page---post_author_info--dbf81cb44069---------------------------------------)

[779 followers](https://amannsharmaa.medium.com/followers?source=post_page---post_author_info--dbf81cb44069---------------------------------------)

·[14 following](https://medium.com/%40amannsharmaa/following?source=post_page---post_author_info--dbf81cb44069---------------------------------------)

| Data Enthusiast | SQL | Python | Power BI | ML | Exploring Cybersecurity & Bug Bounty | Sharing real-world analytics, dashboards & security insights.

## Responses (1)

See all responses

[Help](https://help.medium.com/hc/en-us?source=post_page-----dbf81cb44069---------------------------------------)

[Status](https://status.medium.com/?source=post_page-----dbf81cb44069---------------------------------------)

[About](https://medium.com/about?autoplay=1&source=post_page-----dbf81cb44069---------------------------------------)

[Careers](https://medium.com/jobs-at-medium/work-at-medium-959d1a85284e?source=post_page-----dbf81cb44069---------------------------------------)

Press

[Blog](https://blog.medium.com/?source=post_page-----dbf81cb44069---------------------------------------)

[Privacy](https://policy.medium.com/medium-privacy-policy-f03bf92035c9?source=post_page-----dbf81cb44069---------------------------------------)

[Rules](https://policy.medium.com/medium-rules-30e5502c4eb4?source=post_page-----dbf81cb44069---------------------------------------)

[Terms](https://policy.medium.com/medium-terms-of-service-9db0094a1e0f?source=post_page-----dbf81cb44069---------------------------------------)

[Text to speech](https://speechify.com/medium?source=post_page-----dbf81cb44069---------------------------------------)