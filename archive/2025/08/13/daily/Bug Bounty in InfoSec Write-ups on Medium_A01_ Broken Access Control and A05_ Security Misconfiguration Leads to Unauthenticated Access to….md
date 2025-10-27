---
title: A01: Broken Access Control and A05: Security Misconfiguration Leads to Unauthenticated Access to…
url: https://infosecwriteups.com/a01-broken-access-control-and-a05-security-misconfiguration-leads-to-unauthenticated-access-to-0897e3bec491?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2025-08-13
fetch_date: 2025-10-07T00:16:34.743536
---

# A01: Broken Access Control and A05: Security Misconfiguration Leads to Unauthenticated Access to…

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2F0897e3bec491&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fa01-broken-access-control-and-a05-security-misconfiguration-leads-to-unauthenticated-access-to-0897e3bec491&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fa01-broken-access-control-and-a05-security-misconfiguration-leads-to-unauthenticated-access-to-0897e3bec491&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[Mastodon](https://me.dm/%40enigma_)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-0897e3bec491---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-0897e3bec491---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

Member-only story

# A01: Broken Access Control and A05: Security Misconfiguration Leads to Unauthenticated Access to Paid Content

[![enigma_](https://miro.medium.com/v2/resize:fill:64:64/1*Ym19t_vpdbvu02efSrcJXQ.jpeg)](https://medium.com/%40enigma_?source=post_page---byline--0897e3bec491---------------------------------------)

[enigma\_](https://medium.com/%40enigma_?source=post_page---byline--0897e3bec491---------------------------------------)

3 min read

·

Dec 6, 2024

--

2

Share

While using a service that I recently paid for, there was a slight hiccup in the service which was preventing me from using it. This service is primarily a video and audio streaming service which provides professional, recorded content on a paid subscription basis.

I decided to take a look under the hood to see if it was something on my end, or an issue on the server side. The first thing I usually do, is just inspect the source code to see if I can find anything unusual, and like similar services I’ve used in the past, I located what appeared to be the direct link to the content itself:

Press enter or click to view image in full size

![]()

Inspecting Source Code for URLs

> Another thing you can try, is to CTRL-F to “find” content and search for things like “storage”, “container”, “firebase”, “APIkey” etc.. You can also analyze the Network tab to see where data is coming from and going to.

So I decided to see if I can open this link in a separate browser, or incognito tab, and found that I could, and it listed all the contents inside of this cloud container:

![]()

Contents

--

--

2

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:96:96/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--0897e3bec491---------------------------------------)

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:128:128/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--0897e3bec491---------------------------------------)

Follow

[## Published in InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---post_publication_info--0897e3bec491---------------------------------------)

[71K followers](/followers?source=post_page---post_publication_info--0897e3bec491---------------------------------------)

·[Last published 3 hours ago](/actuator-unleashed-a-guide-to-finding-and-exploiting-spring-boot-actuator-endpoints-29252dcd9d79?source=post_page---post_publication_info--0897e3bec491---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow

[![enigma_](https://miro.medium.com/v2/resize:fill:96:96/1*Ym19t_vpdbvu02efSrcJXQ.jpeg)](https://medium.com/%40enigma_?source=post_page---post_author_info--0897e3bec491---------------------------------------)

[![enigma_](https://miro.medium.com/v2/resize:fill:128:128/1*Ym19t_vpdbvu02efSrcJXQ.jpeg)](https://medium.com/%40enigma_?source=post_page---post_author_info--0897e3bec491---------------------------------------)

[## Written by enigma\_](https://medium.com/%40enigma_?source=post_page---post_author_info--0897e3bec491---------------------------------------)

[374 followers](https://medium.com/%40enigma_/followers?source=post_page---post_author_info--0897e3bec491---------------------------------------)

·[277 following](https://medium.com/%40enigma_/following?source=post_page---post_author_info--0897e3bec491---------------------------------------)

Information Security enthusiast. Targeting OSCP Certification currently.

## Responses (2)

See all responses

[Help](https://help.medium.com/hc/en-us?source=post_page-----0897e3bec491---------------------------------------)

[Status](https://status.medium.com/?source=post_page-----0897e3bec491---------------------------------------)

[About](https://medium.com/about?autoplay=1&source=post_page-----0897e3bec491---------------------------------------)

[Careers](https://medium.com/jobs-at-medium/work-at-medium-959d1a85284e?source=post_page-----0897e3bec491---------------------------------------)

Press

[Blog](https://blog.medium.com/?source=post_page-----0897e3bec491---------------------------------------)

[Privacy](https://policy.medium.com/medium-privacy-policy-f03bf92035c9?source=post_page-----0897e3bec491---------------------------------------)

[Rules](https://policy.medium.com/medium-rules-30e5502c4eb4?source=post_page-----0897e3bec491---------------------------------------)

[Terms](https://policy.medium.com/medium-terms-of-service-9db0094a1e0f?source=post_page-----0897e3bec491---------------------------------------)

[Text to speech](https://speechify.com/medium?source=post_page-----0897e3bec491---------------------------------------)