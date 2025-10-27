---
title: How AI Helped Me Turn a Sneaky SQL Param into a Full-Blown RFI Madness
url: https://infosecwriteups.com/how-ai-helped-me-turn-a-sneaky-sql-param-into-a-full-blown-rfi-madness-31837311f6bd?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2025-04-08
fetch_date: 2025-10-06T22:04:43.625352
---

# How AI Helped Me Turn a Sneaky SQL Param into a Full-Blown RFI Madness

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2F31837311f6bd&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fhow-ai-helped-me-turn-a-sneaky-sql-param-into-a-full-blown-rfi-madness-31837311f6bd&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fhow-ai-helped-me-turn-a-sneaky-sql-param-into-a-full-blown-rfi-madness-31837311f6bd&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-31837311f6bd---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-31837311f6bd---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

Member-only story

# How AI Helped Me Turn a Sneaky SQL Param into a Full-Blown RFI Madness 🤯💻

[![Iski](https://miro.medium.com/v2/resize:fill:64:64/1*PpvkjPQ1lY6aTYHT9kDX5w.png)](https://medium.com/%40iski?source=post_page---byline--31837311f6bd---------------------------------------)

[Iski](https://medium.com/%40iski?source=post_page---byline--31837311f6bd---------------------------------------)

3 min read

·

Apr 7, 2025

--

1

Share

Free [Link](https://medium.com/%40iski/how-ai-helped-me-turn-a-sneaky-sql-param-into-a-full-blown-rfi-madness-31837311f6bd?sk=4492116a90610a9cb9addc4137a8122d)🎈

Hey there!🙌

Press enter or click to view image in full size

![]()

“When life gave me semicolons, I turned them into shell access.”

While most folks used AI to write poems or pass exams, I weaponized it. 😎 My friends were busy asking ChatGPT how to get a girlfriend (spoiler: even AI gave up), and I was asking it how to escalate an SQLi to a critical RFI bug. And guess what? And oh mannn… it delivered better than Amazon Prime. 📦

Let me take you on a rollercoaster ride of how AI turned my recon into revenue — all from one overlooked parameter.

## The Recon Phase: More URLs, More Pain 😩

I was doing mass recon like any bug bounty hunter — chaos, httpx, waybackurls, and gau screaming in my terminal like a death metal band. After a few hours of digital dumpster diving, I stumbled across an endpoint like this:

```
https://example.com/products/details?itemRef=412C9EFD&lang=en
```

Nothing fancy, right? But I saw that weird `itemRef` parameter and something about the value screamed, “I’m hiding something!”

I copied it into Burp Suite and the real game began.

--

--

1

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:96:96/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--31837311f6bd---------------------------------------)

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:128:128/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--31837311f6bd---------------------------------------)

Follow

[## Published in InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---post_publication_info--31837311f6bd---------------------------------------)

[71K followers](/followers?source=post_page---post_publication_info--31837311f6bd---------------------------------------)

·[Last published 1 hour ago](/actuator-unleashed-a-guide-to-finding-and-exploiting-spring-boot-actuator-endpoints-29252dcd9d79?source=post_page---post_publication_info--31837311f6bd---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow

[![Iski](https://miro.medium.com/v2/resize:fill:96:96/1*PpvkjPQ1lY6aTYHT9kDX5w.png)](https://medium.com/%40iski?source=post_page---post_author_info--31837311f6bd---------------------------------------)

[![Iski](https://miro.medium.com/v2/resize:fill:128:128/1*PpvkjPQ1lY6aTYHT9kDX5w.png)](https://medium.com/%40iski?source=post_page---post_author_info--31837311f6bd---------------------------------------)

[## Written by Iski](https://medium.com/%40iski?source=post_page---post_author_info--31837311f6bd---------------------------------------)

[1.8K followers](https://medium.com/%40iski/followers?source=post_page---post_author_info--31837311f6bd---------------------------------------)

·[7 following](https://medium.com/%40iski/following?source=post_page---post_author_info--31837311f6bd---------------------------------------)

Cybersecurity Researcher | Penetration Tester | Bug Bounty Hunter | Web security| Passionate about cyber security, security automation

## Responses (1)

See all responses

[Help](https://help.medium.com/hc/en-us?source=post_page-----31837311f6bd---------------------------------------)

[Status](https://status.medium.com/?source=post_page-----31837311f6bd---------------------------------------)

[About](https://medium.com/about?autoplay=1&source=post_page-----31837311f6bd---------------------------------------)

[Careers](https://medium.com/jobs-at-medium/work-at-medium-959d1a85284e?source=post_page-----31837311f6bd---------------------------------------)

Press

[Blog](https://blog.medium.com/?source=post_page-----31837311f6bd---------------------------------------)

[Privacy](https://policy.medium.com/medium-privacy-policy-f03bf92035c9?source=post_page-----31837311f6bd---------------------------------------)

[Rules](https://policy.medium.com/medium-rules-30e5502c4eb4?source=post_page-----31837311f6bd---------------------------------------)

[Terms](https://policy.medium.com/medium-terms-of-service-9db0094a1e0f?source=post_page-----31837311f6bd---------------------------------------)

[Text to speech](https://speechify.com/medium?source=post_page-----31837311f6bd---------------------------------------)