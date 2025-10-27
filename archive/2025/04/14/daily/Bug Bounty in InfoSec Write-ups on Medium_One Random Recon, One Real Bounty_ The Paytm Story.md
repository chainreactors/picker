---
title: One Random Recon, One Real Bounty: The Paytm Story
url: https://infosecwriteups.com/ghost-paytm-xss-bounty-4f5efe6a643b?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2025-04-14
fetch_date: 2025-10-06T22:03:36.383177
---

# One Random Recon, One Real Bounty: The Paytm Story

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2F4f5efe6a643b&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fghost-paytm-xss-bounty-4f5efe6a643b&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fghost-paytm-xss-bounty-4f5efe6a643b&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-4f5efe6a643b---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-4f5efe6a643b---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

Member-only story

# One Random Recon, One Real Bounty

[![SIDDHANT SHUKLA](https://miro.medium.com/v2/resize:fill:64:64/1*8ZQ4ust4pThkatOZK2KniQ.jpeg)](https://ghostman01.medium.com/?source=post_page---byline--4f5efe6a643b---------------------------------------)

[SIDDHANT SHUKLA](https://ghostman01.medium.com/?source=post_page---byline--4f5efe6a643b---------------------------------------)

4 min read

·

Apr 13, 2025

--

5

Share

[**Click here to read this Awesome article for Freeeeeeeeeee….👈**](https://ghostman01.medium.com/ghost-paytm-xss-bounty-4f5efe6a643b?sk=47e1350d27102daa7a1e3dd21263feb6)

![]()

obito

I started bug hunting back in **2022**, probably during my second year of college. Since then, I had only one goal in mind — **to report a single bug to one of my most used payment app**, even if it was a low-severity issue.
 It wasn’t about recognition or rewards; I just wanted to prove to myself that I could do it — like the other hunters I saw posting their wins on X (*formerly Twitter*).

But no matter how hard I tried, I couldn’t find even a single bug.
 I was **obsessed** with the idea of reporting something to target.
 Honestly, I don’t even know why I chose to make that one app my sole target for such a long time — maybe it was personal.

But finally, I did it.
 I reported a bug to target through their Bug Bounty Program.
 Deep down, I knew it wasn’t some groundbreaking, high-severity vulnerability.
 But it was real.
 **And for me, it meant everything.**

Press enter or click to view image in full size

![]()

Security Team Response

## The “Not-So-Valid” Bug That Sparked It All

--

--

5

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:96:96/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--4f5efe6a643b---------------------------------------)

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:128:128/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--4f5efe6a643b---------------------------------------)

Follow

[## Published in InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---post_publication_info--4f5efe6a643b---------------------------------------)

[71K followers](/followers?source=post_page---post_publication_info--4f5efe6a643b---------------------------------------)

·[Last published 1 hour ago](/actuator-unleashed-a-guide-to-finding-and-exploiting-spring-boot-actuator-endpoints-29252dcd9d79?source=post_page---post_publication_info--4f5efe6a643b---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow

[![SIDDHANT SHUKLA](https://miro.medium.com/v2/resize:fill:96:96/1*8ZQ4ust4pThkatOZK2KniQ.jpeg)](https://ghostman01.medium.com/?source=post_page---post_author_info--4f5efe6a643b---------------------------------------)

[![SIDDHANT SHUKLA](https://miro.medium.com/v2/resize:fill:128:128/1*8ZQ4ust4pThkatOZK2KniQ.jpeg)](https://ghostman01.medium.com/?source=post_page---post_author_info--4f5efe6a643b---------------------------------------)

[## Written by SIDDHANT SHUKLA](https://ghostman01.medium.com/?source=post_page---post_author_info--4f5efe6a643b---------------------------------------)

[855 followers](https://ghostman01.medium.com/followers?source=post_page---post_author_info--4f5efe6a643b---------------------------------------)

·[424 following](https://medium.com/%40ghostman01/following?source=post_page---post_author_info--4f5efe6a643b---------------------------------------)

just a lazy hunter.

## Responses (5)

See all responses

[Help](https://help.medium.com/hc/en-us?source=post_page-----4f5efe6a643b---------------------------------------)

[Status](https://status.medium.com/?source=post_page-----4f5efe6a643b---------------------------------------)

[About](https://medium.com/about?autoplay=1&source=post_page-----4f5efe6a643b---------------------------------------)

[Careers](https://medium.com/jobs-at-medium/work-at-medium-959d1a85284e?source=post_page-----4f5efe6a643b---------------------------------------)

Press

[Blog](https://blog.medium.com/?source=post_page-----4f5efe6a643b---------------------------------------)

[Privacy](https://policy.medium.com/medium-privacy-policy-f03bf92035c9?source=post_page-----4f5efe6a643b---------------------------------------)

[Rules](https://policy.medium.com/medium-rules-30e5502c4eb4?source=post_page-----4f5efe6a643b---------------------------------------)

[Terms](https://policy.medium.com/medium-terms-of-service-9db0094a1e0f?source=post_page-----4f5efe6a643b---------------------------------------)

[Text to speech](https://speechify.com/medium?source=post_page-----4f5efe6a643b---------------------------------------)