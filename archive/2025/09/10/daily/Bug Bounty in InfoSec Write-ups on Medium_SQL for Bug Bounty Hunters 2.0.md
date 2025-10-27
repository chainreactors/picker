---
title: SQL for Bug Bounty Hunters 2.0
url: https://infosecwriteups.com/sql-for-bug-bounty-hunters-2-0-f7e136c0e5c9?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2025-09-10
fetch_date: 2025-10-02T19:54:12.265792
---

# SQL for Bug Bounty Hunters 2.0

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2Ff7e136c0e5c9&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fsql-for-bug-bounty-hunters-2-0-f7e136c0e5c9&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fsql-for-bug-bounty-hunters-2-0-f7e136c0e5c9&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-f7e136c0e5c9---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-f7e136c0e5c9---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

Member-only story

# SQL for Bug Bounty Hunters 2.0

[![Swetha](https://miro.medium.com/v2/resize:fill:64:64/1*SsOiUKPCAbg3qUYo2cbT_Q.jpeg)](https://medium.com/%40swethas274?source=post_page---byline--f7e136c0e5c9---------------------------------------)

[Swetha](https://medium.com/%40swethas274?source=post_page---byline--f7e136c0e5c9---------------------------------------)

3 min read

·

Sep 9, 2025

--

Share

This is the like to 1.0 version of this article <https://medium.com/bugbountywriteup/sql-for-bug-bounty-hunters-106a4c324049>

![]()

In the above link i have gone through the **basic SQL cmds** here we will dive into the depth for long lasting understanding.

![]()

### **Before that,**

Hi, Hello, Hola, Namaste, Bonjour, ….

I am Swetha. I’ve chosen to step into the world of **development, ethical hacking, and bug bounty hunting**. While I may still be on the path of learning and don’t yet have an official record to showcase, I’ve committed myself to this journey. For me, it’s not just about commands or tools — it’s about building the right mindset, understanding the “why” behind the “how,” and growing step by step into the career I’ve set my sights on……………..

![]()

Wokayyyyyyyyy, i get it you are here to learn about SQL and not me.

Let’s get started,

--

--

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:96:96/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--f7e136c0e5c9---------------------------------------)

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:128:128/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--f7e136c0e5c9---------------------------------------)

Follow

[## Published in InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---post_publication_info--f7e136c0e5c9---------------------------------------)

[71K followers](/followers?source=post_page---post_publication_info--f7e136c0e5c9---------------------------------------)

·[Last published 4 days ago](/how-to-find-p1-bugs-using-google-in-your-target-part-1-e37455324dc1?source=post_page---post_publication_info--f7e136c0e5c9---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow

[![Swetha](https://miro.medium.com/v2/resize:fill:96:96/1*SsOiUKPCAbg3qUYo2cbT_Q.jpeg)](https://medium.com/%40swethas274?source=post_page---post_author_info--f7e136c0e5c9---------------------------------------)

[![Swetha](https://miro.medium.com/v2/resize:fill:128:128/1*SsOiUKPCAbg3qUYo2cbT_Q.jpeg)](https://medium.com/%40swethas274?source=post_page---post_author_info--f7e136c0e5c9---------------------------------------)

[## Written by Swetha](https://medium.com/%40swethas274?source=post_page---post_author_info--f7e136c0e5c9---------------------------------------)

[84 followers](https://medium.com/%40swethas274/followers?source=post_page---post_author_info--f7e136c0e5c9---------------------------------------)

·[38 following](https://medium.com/%40swethas274/following?source=post_page---post_author_info--f7e136c0e5c9---------------------------------------)

Aspiring Bug Bounty Hunter 👩‍💻👾 | Part time Web developer 💻 | bibliophile

## No responses yet

[Help](https://help.medium.com/hc/en-us?source=post_page-----f7e136c0e5c9---------------------------------------)

[Status](https://status.medium.com/?source=post_page-----f7e136c0e5c9---------------------------------------)

[About](https://medium.com/about?autoplay=1&source=post_page-----f7e136c0e5c9---------------------------------------)

[Careers](https://medium.com/jobs-at-medium/work-at-medium-959d1a85284e?source=post_page-----f7e136c0e5c9---------------------------------------)

Press

[Blog](https://blog.medium.com/?source=post_page-----f7e136c0e5c9---------------------------------------)

[Privacy](https://policy.medium.com/medium-privacy-policy-f03bf92035c9?source=post_page-----f7e136c0e5c9---------------------------------------)

[Rules](https://policy.medium.com/medium-rules-30e5502c4eb4?source=post_page-----f7e136c0e5c9---------------------------------------)

[Terms](https://policy.medium.com/medium-terms-of-service-9db0094a1e0f?source=post_page-----f7e136c0e5c9---------------------------------------)

[Text to speech](https://speechify.com/medium?source=post_page-----f7e136c0e5c9---------------------------------------)