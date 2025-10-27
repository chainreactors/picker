---
title: How I Found Bugs on Adobe
url: https://infosecwriteups.com/how-i-found-bugs-on-adobe-16cedb79e830?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2025-05-01
fetch_date: 2025-10-06T22:24:55.191274
---

# How I Found Bugs on Adobe

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2F16cedb79e830&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fhow-i-found-bugs-on-adobe-16cedb79e830&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fhow-i-found-bugs-on-adobe-16cedb79e830&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-16cedb79e830---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-16cedb79e830---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

Member-only story

# How I Found Bugs on Adobe

[![RivuDon](https://miro.medium.com/v2/resize:fill:64:64/1*GgVWlQkhYQwCNeI5neIaVA.png)](https://rivudon.medium.com/?source=post_page---byline--16cedb79e830---------------------------------------)

[RivuDon](https://rivudon.medium.com/?source=post_page---byline--16cedb79e830---------------------------------------)

6 min read

·

Apr 30, 2025

--

7

Share

A tale of hacking Adobe Inc.

Press enter or click to view image in full size

![]()

> Hi, I’m **Rivek Raj Tamang (RivuDon)**, a Security Researcher, Bug Hunter, and an Ethical Hacker currently pursuing a Master’s in Cybersecurity. I have secured many companies, received bounty and numerous Hall of Fames and Letter of Appreciation / Recognition.
>
> Feel free to connect and get in touch with me. You can find out more about me on my [LinkedIn,](https://www.linkedin.com/in/rivektamang/) I am active there.

**📩 Read for Free** [**CLICK HERE.**](https://rivudon.medium.com/16cedb79e830?sk=b517f49c05033f6831e79d9ed3c430b6)

Hi readers, this write-up is about how I found multiple bugs on **Adobe Inc via HackerOne,** this is going to be a fun read, packed with insights, and will hopefully inspire you to find bugs with the same mindset.

Here’s **How I found bugs on Adobe Inc …**

## The Start of a Journey

Before starting the tale let me tell you how my hunt was going on, I usually hunted on **self-hosted programs and Bugcrowd**, I did’nt hunt that much on **Hackerone** because It’s quite difficult to find bugs on **Hackerone** if you know what I mean, however this changed soon.

The day starts by following the usual ritual: wake up, open LinkedIn and Twitter, and check out security and bug bounty related stuff, and then suddenly a brother sends an article on how he found bugs on **Adobe**, like the curious mind I was, I quickly hopped on…

--

--

7

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:96:96/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--16cedb79e830---------------------------------------)

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:128:128/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--16cedb79e830---------------------------------------)

Follow

[## Published in InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---post_publication_info--16cedb79e830---------------------------------------)

[71K followers](/followers?source=post_page---post_publication_info--16cedb79e830---------------------------------------)

·[Last published 2 hours ago](/actuator-unleashed-a-guide-to-finding-and-exploiting-spring-boot-actuator-endpoints-29252dcd9d79?source=post_page---post_publication_info--16cedb79e830---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow

[![RivuDon](https://miro.medium.com/v2/resize:fill:96:96/1*GgVWlQkhYQwCNeI5neIaVA.png)](https://rivudon.medium.com/?source=post_page---post_author_info--16cedb79e830---------------------------------------)

[![RivuDon](https://miro.medium.com/v2/resize:fill:128:128/1*GgVWlQkhYQwCNeI5neIaVA.png)](https://rivudon.medium.com/?source=post_page---post_author_info--16cedb79e830---------------------------------------)

[## Written by RivuDon](https://rivudon.medium.com/?source=post_page---post_author_info--16cedb79e830---------------------------------------)

[630 followers](https://rivudon.medium.com/followers?source=post_page---post_author_info--16cedb79e830---------------------------------------)

·[110 following](https://medium.com/%40rivudon/following?source=post_page---post_author_info--16cedb79e830---------------------------------------)

Security Researcher | Bug Hunter | Hacker | Tech | Lifestyle LinkedIn: @RivekRajTamang

## Responses (7)

See all responses

[Help](https://help.medium.com/hc/en-us?source=post_page-----16cedb79e830---------------------------------------)

[Status](https://status.medium.com/?source=post_page-----16cedb79e830---------------------------------------)

[About](https://medium.com/about?autoplay=1&source=post_page-----16cedb79e830---------------------------------------)

[Careers](https://medium.com/jobs-at-medium/work-at-medium-959d1a85284e?source=post_page-----16cedb79e830---------------------------------------)

Press

[Blog](https://blog.medium.com/?source=post_page-----16cedb79e830---------------------------------------)

[Privacy](https://policy.medium.com/medium-privacy-policy-f03bf92035c9?source=post_page-----16cedb79e830---------------------------------------)

[Rules](https://policy.medium.com/medium-rules-30e5502c4eb4?source=post_page-----16cedb79e830---------------------------------------)

[Terms](https://policy.medium.com/medium-terms-of-service-9db0094a1e0f?source=post_page-----16cedb79e830---------------------------------------)

[Text to speech](https://speechify.com/medium?source=post_page-----16cedb79e830---------------------------------------)