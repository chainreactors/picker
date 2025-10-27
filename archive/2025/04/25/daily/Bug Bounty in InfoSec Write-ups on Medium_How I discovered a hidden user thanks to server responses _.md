---
title: How I discovered a hidden user thanks to server responses ?
url: https://infosecwriteups.com/how-i-discovered-a-hidden-user-thanks-to-server-responses-b65e198f4e73?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2025-04-25
fetch_date: 2025-10-06T22:04:42.973917
---

# How I discovered a hidden user thanks to server responses ?

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2Fb65e198f4e73&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fhow-i-discovered-a-hidden-user-thanks-to-server-responses-b65e198f4e73&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fhow-i-discovered-a-hidden-user-thanks-to-server-responses-b65e198f4e73&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[Mastodon](https://me.dm/%40phoenixcatalan)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-b65e198f4e73---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-b65e198f4e73---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

Member-only story

# 🔍 How I discovered a hidden user thanks to server responses ?

[![phoenixcatalan](https://miro.medium.com/v2/resize:fill:64:64/1*vyxgJnHAeNgHofU2nyukJA.jpeg)](https://medium.com/%40phoenixcatalan?source=post_page---byline--b65e198f4e73---------------------------------------)

[phoenixcatalan](https://medium.com/%40phoenixcatalan?source=post_page---byline--b65e198f4e73---------------------------------------)

5 min read

·

Apr 16, 2025

--

Share

My first real step into web hacking and it wasn’t what i thought it would be.

Press enter or click to view image in full size

![]()

Username Enumeration : when answers say too much “optional for automation

### 🚀 Introduction

This lab of *Portswigger* on username enumeration blew my mind and i understood why authentication is conceptually among the **simplest security mechanisms** employed in web applications. No need for complex scripting or twisted injection. **Just a little observation**. It’s not just that I’ve “**solved a lab**”. It’s because this lab has enabled me to build up a real **thinking workflow** that i can reuse in other contexts, whether in CTF, bug bounty or pentesting. Thanks to him, I’ve come to understand the importance of carefully observing server responses, companing behavior according to different inputs, and making the right assumption at the right time.

🧠 In this article, I’m going to show you:

* How i approach this lab (step by step)
* My understanding of enumeration logic
* And most importantly of all, the **thinking workflow** i’ve drawn from it, which you can apply elsewhere.

### 🎯 Lab objective

The purpose of the lab is simple :

➡️ enumerate a valid username, brute-force this user’s password, then access their account page.

--

--

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:96:96/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--b65e198f4e73---------------------------------------)

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:128:128/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--b65e198f4e73---------------------------------------)

Follow

[## Published in InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---post_publication_info--b65e198f4e73---------------------------------------)

[71K followers](/followers?source=post_page---post_publication_info--b65e198f4e73---------------------------------------)

·[Last published 1 hour ago](/actuator-unleashed-a-guide-to-finding-and-exploiting-spring-boot-actuator-endpoints-29252dcd9d79?source=post_page---post_publication_info--b65e198f4e73---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow

[![phoenixcatalan](https://miro.medium.com/v2/resize:fill:96:96/1*vyxgJnHAeNgHofU2nyukJA.jpeg)](https://medium.com/%40phoenixcatalan?source=post_page---post_author_info--b65e198f4e73---------------------------------------)

[![phoenixcatalan](https://miro.medium.com/v2/resize:fill:128:128/1*vyxgJnHAeNgHofU2nyukJA.jpeg)](https://medium.com/%40phoenixcatalan?source=post_page---post_author_info--b65e198f4e73---------------------------------------)

[## Written by phoenixcatalan](https://medium.com/%40phoenixcatalan?source=post_page---post_author_info--b65e198f4e73---------------------------------------)

[106 followers](https://medium.com/%40phoenixcatalan/followers?source=post_page---post_author_info--b65e198f4e73---------------------------------------)

·[5 following](https://medium.com/%40phoenixcatalan/following?source=post_page---post_author_info--b65e198f4e73---------------------------------------)

🎯 Developer with a passion for Angular & cybersecurity Guardian of web applications thanks to cybersecurity 🛡️.

## No responses yet

[Help](https://help.medium.com/hc/en-us?source=post_page-----b65e198f4e73---------------------------------------)

[Status](https://status.medium.com/?source=post_page-----b65e198f4e73---------------------------------------)

[About](https://medium.com/about?autoplay=1&source=post_page-----b65e198f4e73---------------------------------------)

[Careers](https://medium.com/jobs-at-medium/work-at-medium-959d1a85284e?source=post_page-----b65e198f4e73---------------------------------------)

Press

[Blog](https://blog.medium.com/?source=post_page-----b65e198f4e73---------------------------------------)

[Privacy](https://policy.medium.com/medium-privacy-policy-f03bf92035c9?source=post_page-----b65e198f4e73---------------------------------------)

[Rules](https://policy.medium.com/medium-rules-30e5502c4eb4?source=post_page-----b65e198f4e73---------------------------------------)

[Terms](https://policy.medium.com/medium-terms-of-service-9db0094a1e0f?source=post_page-----b65e198f4e73---------------------------------------)

[Text to speech](https://speechify.com/medium?source=post_page-----b65e198f4e73---------------------------------------)