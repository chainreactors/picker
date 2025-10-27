---
title: Tumblr Post+ Creator and Got Paid $100
url: https://infosecwriteups.com/tumblr-post-creator-and-got-paid-100-e3659f776cb5?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2025-07-20
fetch_date: 2025-10-06T23:28:18.812829
---

# Tumblr Post+ Creator and Got Paid $100

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2Fe3659f776cb5&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Ftumblr-post-creator-and-got-paid-100-e3659f776cb5&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Ftumblr-post-creator-and-got-paid-100-e3659f776cb5&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-e3659f776cb5---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-e3659f776cb5---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

Member-only story

# **Tumblr Post+ Creator and Got Paid $100**

## A low-impact but unexpected behavior in Tumblr’s Post+ system allowed subscriptions to creators who had already opted out — here’s how I found it, how it worked, and why it still mattered.

[![Monika sharma](https://miro.medium.com/v2/da:true/resize:fill:64:64/0*Tv4b4p5mb6J3IJwD)](https://medium.com/%40commanak46?source=post_page---byline--e3659f776cb5---------------------------------------)

[Monika sharma](https://medium.com/%40commanak46?source=post_page---byline--e3659f776cb5---------------------------------------)

4 min read

·

Jul 19, 2025

--

Share

Press enter or click to view image in full size

![]()

> **Introduction**

Tumblr’s Post+ was designed to let creators monetize exclusive content. But what happens when a user can still subscribe to a creator who has already opted out?

While this behavior might seem harmless at first glance, digging deeper reveals unexpected application logic — leading to inconsistencies in access control, payment flow, and potentially creator visibility.

In this write-up, I’ll walk you through a quirky but fascinating bug that allowed me to subscribe to an inactive Post+ creator, earning a $100 bounty for responsibly reporting the issue to Automattic.

> **Understanding Tumblr’s Post+ and the Bug Context**

Tumblr’s Post+ feature relies on a WooCommerce-powered payment flow that links a creator’s Post+ status to a unique `blogMembershipsId`. When a creator opts in, a `checkout` URL is generated using that ID. If they opt out, the expectation is that the creator’s Post+ content and checkout capabilities are disabled.

--

--

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:96:96/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--e3659f776cb5---------------------------------------)

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:128:128/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--e3659f776cb5---------------------------------------)

Follow

[## Published in InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---post_publication_info--e3659f776cb5---------------------------------------)

[71K followers](/followers?source=post_page---post_publication_info--e3659f776cb5---------------------------------------)

·[Last published 3 hours ago](/actuator-unleashed-a-guide-to-finding-and-exploiting-spring-boot-actuator-endpoints-29252dcd9d79?source=post_page---post_publication_info--e3659f776cb5---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow

[![Monika sharma](https://miro.medium.com/v2/resize:fill:96:96/0*Tv4b4p5mb6J3IJwD)](https://medium.com/%40commanak46?source=post_page---post_author_info--e3659f776cb5---------------------------------------)

[![Monika sharma](https://miro.medium.com/v2/resize:fill:128:128/0*Tv4b4p5mb6J3IJwD)](https://medium.com/%40commanak46?source=post_page---post_author_info--e3659f776cb5---------------------------------------)

[## Written by Monika sharma](https://medium.com/%40commanak46?source=post_page---post_author_info--e3659f776cb5---------------------------------------)

[2K followers](https://medium.com/%40commanak46/followers?source=post_page---post_author_info--e3659f776cb5---------------------------------------)

·[7 following](https://medium.com/%40commanak46/following?source=post_page---post_author_info--e3659f776cb5---------------------------------------)

## No responses yet

[Help](https://help.medium.com/hc/en-us?source=post_page-----e3659f776cb5---------------------------------------)

[Status](https://status.medium.com/?source=post_page-----e3659f776cb5---------------------------------------)

[About](https://medium.com/about?autoplay=1&source=post_page-----e3659f776cb5---------------------------------------)

[Careers](https://medium.com/jobs-at-medium/work-at-medium-959d1a85284e?source=post_page-----e3659f776cb5---------------------------------------)

Press

[Blog](https://blog.medium.com/?source=post_page-----e3659f776cb5---------------------------------------)

[Privacy](https://policy.medium.com/medium-privacy-policy-f03bf92035c9?source=post_page-----e3659f776cb5---------------------------------------)

[Rules](https://policy.medium.com/medium-rules-30e5502c4eb4?source=post_page-----e3659f776cb5---------------------------------------)

[Terms](https://policy.medium.com/medium-terms-of-service-9db0094a1e0f?source=post_page-----e3659f776cb5---------------------------------------)

[Text to speech](https://speechify.com/medium?source=post_page-----e3659f776cb5---------------------------------------)