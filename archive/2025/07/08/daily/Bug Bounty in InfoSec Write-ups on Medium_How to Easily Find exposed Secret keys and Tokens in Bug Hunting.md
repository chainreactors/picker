---
title: How to Easily Find exposed Secret keys and Tokens in Bug Hunting
url: https://infosecwriteups.com/how-to-easily-find-exposed-secret-keys-and-tokens-in-bug-hunting-afed1ea9e883?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2025-07-08
fetch_date: 2025-10-06T23:23:55.249040
---

# How to Easily Find exposed Secret keys and Tokens in Bug Hunting

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2Fafed1ea9e883&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fhow-to-easily-find-exposed-secret-keys-and-tokens-in-bug-hunting-afed1ea9e883&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fhow-to-easily-find-exposed-secret-keys-and-tokens-in-bug-hunting-afed1ea9e883&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-afed1ea9e883---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-afed1ea9e883---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

Member-only story

# **How to Easily Find exposed Secret keys and Tokens in Bug Hunting**

[![RivuDon](https://miro.medium.com/v2/resize:fill:64:64/1*GgVWlQkhYQwCNeI5neIaVA.png)](https://rivudon.medium.com/?source=post_page---byline--afed1ea9e883---------------------------------------)

[RivuDon](https://rivudon.medium.com/?source=post_page---byline--afed1ea9e883---------------------------------------)

4 min read

·

Jul 7, 2025

--

5

Share

Earn rewards with this simple method.

Press enter or click to view image in full size

![]()

📩 Read for Free [**CLICK HERE.**](https://rivudon.medium.com/afed1ea9e883?sk=2521270b92696f51af863f47407d619c)

> Hi, I’m **Rivek Raj Tamang (RivuDon)**, a Security Researcher, Bug Hunter, and an Ethical Hacker currently pursuing a Master’s in Cybersecurity. I have secured many companies, received bounties, and numerous Hall of Fames mentions and Letter of Appreciation / Recognition.
>
> Feel free to connect with me! You can find out more about me on my [**LinkedIn**,](https://www.linkedin.com/in/rivektamang/) I am active there.

**Hi readers**, this write-up is a quick guide one on how I found and find **Exposed secret keys and tokens** easily. How you can too.

So, without further ado, let’s get straight to it!

## What are they?

**Exposed secret keys and tokens** are sensitive credentials made publicly accessible by mistake. Attackers can use them to access systems or data without permission, leading to potential breaches or misuse of services.

*Examples include**API Keys, tokens, Hardcoded Credentials, secret links etc. that are not meant to be for public exposure.*

## Method

**Where are they hidden?**

**The answer: Source codes** and **JS Files**

--

--

5

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:96:96/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--afed1ea9e883---------------------------------------)

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:128:128/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--afed1ea9e883---------------------------------------)

Follow

[## Published in InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---post_publication_info--afed1ea9e883---------------------------------------)

[71K followers](/followers?source=post_page---post_publication_info--afed1ea9e883---------------------------------------)

·[Last published 2 hours ago](/actuator-unleashed-a-guide-to-finding-and-exploiting-spring-boot-actuator-endpoints-29252dcd9d79?source=post_page---post_publication_info--afed1ea9e883---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow

[![RivuDon](https://miro.medium.com/v2/resize:fill:96:96/1*GgVWlQkhYQwCNeI5neIaVA.png)](https://rivudon.medium.com/?source=post_page---post_author_info--afed1ea9e883---------------------------------------)

[![RivuDon](https://miro.medium.com/v2/resize:fill:128:128/1*GgVWlQkhYQwCNeI5neIaVA.png)](https://rivudon.medium.com/?source=post_page---post_author_info--afed1ea9e883---------------------------------------)

[## Written by RivuDon](https://rivudon.medium.com/?source=post_page---post_author_info--afed1ea9e883---------------------------------------)

[630 followers](https://rivudon.medium.com/followers?source=post_page---post_author_info--afed1ea9e883---------------------------------------)

·[110 following](https://medium.com/%40rivudon/following?source=post_page---post_author_info--afed1ea9e883---------------------------------------)

Security Researcher | Bug Hunter | Hacker | Tech | Lifestyle LinkedIn: @RivekRajTamang

## Responses (5)

See all responses

[Help](https://help.medium.com/hc/en-us?source=post_page-----afed1ea9e883---------------------------------------)

[Status](https://status.medium.com/?source=post_page-----afed1ea9e883---------------------------------------)

[About](https://medium.com/about?autoplay=1&source=post_page-----afed1ea9e883---------------------------------------)

[Careers](https://medium.com/jobs-at-medium/work-at-medium-959d1a85284e?source=post_page-----afed1ea9e883---------------------------------------)

Press

[Blog](https://blog.medium.com/?source=post_page-----afed1ea9e883---------------------------------------)

[Privacy](https://policy.medium.com/medium-privacy-policy-f03bf92035c9?source=post_page-----afed1ea9e883---------------------------------------)

[Rules](https://policy.medium.com/medium-rules-30e5502c4eb4?source=post_page-----afed1ea9e883---------------------------------------)

[Terms](https://policy.medium.com/medium-terms-of-service-9db0094a1e0f?source=post_page-----afed1ea9e883---------------------------------------)

[Text to speech](https://speechify.com/medium?source=post_page-----afed1ea9e883---------------------------------------)