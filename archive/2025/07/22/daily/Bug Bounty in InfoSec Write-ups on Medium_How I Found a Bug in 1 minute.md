---
title: How I Found a Bug in 1 minute
url: https://infosecwriteups.com/how-i-found-a-bug-in-1-minute-c81dc179d0aa?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2025-07-22
fetch_date: 2025-10-06T23:26:50.274999
---

# How I Found a Bug in 1 minute

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2Fc81dc179d0aa&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fhow-i-found-a-bug-in-1-minute-c81dc179d0aa&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fhow-i-found-a-bug-in-1-minute-c81dc179d0aa&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-c81dc179d0aa---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-c81dc179d0aa---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

Member-only story

# How I Found a Bug in 1 minute

[![RivuDon](https://miro.medium.com/v2/resize:fill:64:64/1*GgVWlQkhYQwCNeI5neIaVA.png)](https://rivudon.medium.com/?source=post_page---byline--c81dc179d0aa---------------------------------------)

[RivuDon](https://rivudon.medium.com/?source=post_page---byline--c81dc179d0aa---------------------------------------)

5 min read

·

Jul 21, 2025

--

12

Share

How you can too.

Press enter or click to view image in full size

![]()

📩 Read for Free [**CLICK HERE.**](https://rivudon.medium.com/c81dc179d0aa?sk=c1dbffe278c85ce406bcaa5390f69525)

> Hi, I’m **Rivek Raj Tamang (RivuDon)**, a Security Researcher, Bug Hunter, and Ethical Hacker currently pursuing a Master’s in Cybersecurity from Sikkim, India. I have secured many companies, received bounties, and numerous Hall of Fames mentions and Letter of Appreciation / Recognition.
>
> Feel free to connect with me! You can find out more about me on my [**LinkedIn**,](https://www.linkedin.com/in/rivektamang/) I am active there.

**Hi readers**, this write-up is on How I found a bug in just under 1 minute and how you could too.

So without further ado, let’s get straight to it!

## **The Target**

One fine day, I came to know about this neat target, with the help of my **not-so-secret recon technique** of finding **good targets every time**.

*(Specially for people who still struggle to find good targets, please read the below article.)*

[## Unique ways to Recon for Bug Hunters: Short series [Part 1]

### Unique ways to recon for bug hunting

osintteam.blog](https://osintteam.blog/unique-ways-to-recon-for-bug-hunters-short-series-part-1-7e91f3fcfe25?source=post_page-----c81dc179d0aa---------------------------------------)

Like any initial recon, I started by finding and enumerating subdomains because the larger the attack surface the…

--

--

12

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:96:96/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--c81dc179d0aa---------------------------------------)

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:128:128/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--c81dc179d0aa---------------------------------------)

Follow

[## Published in InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---post_publication_info--c81dc179d0aa---------------------------------------)

[71K followers](/followers?source=post_page---post_publication_info--c81dc179d0aa---------------------------------------)

·[Last published 3 hours ago](/actuator-unleashed-a-guide-to-finding-and-exploiting-spring-boot-actuator-endpoints-29252dcd9d79?source=post_page---post_publication_info--c81dc179d0aa---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow

[![RivuDon](https://miro.medium.com/v2/resize:fill:96:96/1*GgVWlQkhYQwCNeI5neIaVA.png)](https://rivudon.medium.com/?source=post_page---post_author_info--c81dc179d0aa---------------------------------------)

[![RivuDon](https://miro.medium.com/v2/resize:fill:128:128/1*GgVWlQkhYQwCNeI5neIaVA.png)](https://rivudon.medium.com/?source=post_page---post_author_info--c81dc179d0aa---------------------------------------)

[## Written by RivuDon](https://rivudon.medium.com/?source=post_page---post_author_info--c81dc179d0aa---------------------------------------)

[630 followers](https://rivudon.medium.com/followers?source=post_page---post_author_info--c81dc179d0aa---------------------------------------)

·[110 following](https://medium.com/%40rivudon/following?source=post_page---post_author_info--c81dc179d0aa---------------------------------------)

Security Researcher | Bug Hunter | Hacker | Tech | Lifestyle LinkedIn: @RivekRajTamang

## Responses (12)

See all responses

[Help](https://help.medium.com/hc/en-us?source=post_page-----c81dc179d0aa---------------------------------------)

[Status](https://status.medium.com/?source=post_page-----c81dc179d0aa---------------------------------------)

[About](https://medium.com/about?autoplay=1&source=post_page-----c81dc179d0aa---------------------------------------)

[Careers](https://medium.com/jobs-at-medium/work-at-medium-959d1a85284e?source=post_page-----c81dc179d0aa---------------------------------------)

Press

[Blog](https://blog.medium.com/?source=post_page-----c81dc179d0aa---------------------------------------)

[Privacy](https://policy.medium.com/medium-privacy-policy-f03bf92035c9?source=post_page-----c81dc179d0aa---------------------------------------)

[Rules](https://policy.medium.com/medium-rules-30e5502c4eb4?source=post_page-----c81dc179d0aa---------------------------------------)

[Terms](https://policy.medium.com/medium-terms-of-service-9db0094a1e0f?source=post_page-----c81dc179d0aa---------------------------------------)

[Text to speech](https://speechify.com/medium?source=post_page-----c81dc179d0aa---------------------------------------)