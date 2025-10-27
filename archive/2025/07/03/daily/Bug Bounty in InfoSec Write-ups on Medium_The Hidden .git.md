---
title: The Hidden .git
url: https://infosecwriteups.com/the-hidden-git-b30afef0b462?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2025-07-03
fetch_date: 2025-10-06T23:50:32.161453
---

# The Hidden .git

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2Fb30afef0b462&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fthe-hidden-git-b30afef0b462&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fthe-hidden-git-b30afef0b462&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-b30afef0b462---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-b30afef0b462---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

Member-only story

# Unique way to find .git: Missed by Many

[![SIDDHANT SHUKLA](https://miro.medium.com/v2/resize:fill:64:64/1*8ZQ4ust4pThkatOZK2KniQ.jpeg)](https://ghostman01.medium.com/?source=post_page---byline--b30afef0b462---------------------------------------)

[SIDDHANT SHUKLA](https://ghostman01.medium.com/?source=post_page---byline--b30afef0b462---------------------------------------)

3 min read

·

Jul 1, 2025

--

7

Share

## 🐞 YO!!

Hey folks!
 I hope you’re enjoying my bug hunting stories as much as I enjoy writing them. I genuinely appreciate your support and hope I never disappoint you. Let’s jump into another bug tale — this one’s a mix of curiosity, luck, and persistence!

[**Free Article Link 👈**](https://ghostman01.medium.com/the-hidden-git-b30afef0b462?sk=eed8245f9da4580e1e7efcef72e7dc7f)

![]()

zoro

## 🔍 The Hunt Begins…

I was hacking on one of my regular targets. It’s been a while — no bugs, no leads, and to top it off, exams were knocking at the door. My brain was fried, and motivation was sinking. So I decided, *why not explore a fresh target in parallel?*

I picked a random target and started my recon as usual with the classic subfinder:

```
subfinder -d target.com --all --recursive --silent | httpx -sc -td
```

After a while, I had a list of all live subdomains thanks to `httpx`. I began scanning them randomly. Right off the bat, I noticed that many subdomains were hosted on IIS Windows servers — time to run **ShortScan**.

## 🤖 Then Came the Chatbot…

One subdomain caught my eye: an **AI chatbot** — interesting!

I opened it, checked the source code and JS files, but didn’t find anything juicy.

--

--

7

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:96:96/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--b30afef0b462---------------------------------------)

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:128:128/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--b30afef0b462---------------------------------------)

Follow

[## Published in InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---post_publication_info--b30afef0b462---------------------------------------)

[71K followers](/followers?source=post_page---post_publication_info--b30afef0b462---------------------------------------)

·[Last published 3 hours ago](/actuator-unleashed-a-guide-to-finding-and-exploiting-spring-boot-actuator-endpoints-29252dcd9d79?source=post_page---post_publication_info--b30afef0b462---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow

[![SIDDHANT SHUKLA](https://miro.medium.com/v2/resize:fill:96:96/1*8ZQ4ust4pThkatOZK2KniQ.jpeg)](https://ghostman01.medium.com/?source=post_page---post_author_info--b30afef0b462---------------------------------------)

[![SIDDHANT SHUKLA](https://miro.medium.com/v2/resize:fill:128:128/1*8ZQ4ust4pThkatOZK2KniQ.jpeg)](https://ghostman01.medium.com/?source=post_page---post_author_info--b30afef0b462---------------------------------------)

[## Written by SIDDHANT SHUKLA](https://ghostman01.medium.com/?source=post_page---post_author_info--b30afef0b462---------------------------------------)

[855 followers](https://ghostman01.medium.com/followers?source=post_page---post_author_info--b30afef0b462---------------------------------------)

·[424 following](https://medium.com/%40ghostman01/following?source=post_page---post_author_info--b30afef0b462---------------------------------------)

just a lazy hunter.

## Responses (7)

See all responses

[Help](https://help.medium.com/hc/en-us?source=post_page-----b30afef0b462---------------------------------------)

[Status](https://status.medium.com/?source=post_page-----b30afef0b462---------------------------------------)

[About](https://medium.com/about?autoplay=1&source=post_page-----b30afef0b462---------------------------------------)

[Careers](https://medium.com/jobs-at-medium/work-at-medium-959d1a85284e?source=post_page-----b30afef0b462---------------------------------------)

Press

[Blog](https://blog.medium.com/?source=post_page-----b30afef0b462---------------------------------------)

[Privacy](https://policy.medium.com/medium-privacy-policy-f03bf92035c9?source=post_page-----b30afef0b462---------------------------------------)

[Rules](https://policy.medium.com/medium-rules-30e5502c4eb4?source=post_page-----b30afef0b462---------------------------------------)

[Terms](https://policy.medium.com/medium-terms-of-service-9db0094a1e0f?source=post_page-----b30afef0b462---------------------------------------)

[Text to speech](https://speechify.com/medium?source=post_page-----b30afef0b462---------------------------------------)