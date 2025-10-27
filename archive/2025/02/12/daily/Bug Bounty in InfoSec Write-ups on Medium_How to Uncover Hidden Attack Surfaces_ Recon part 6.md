---
title: How to Uncover Hidden Attack Surfaces? Recon part 6
url: https://infosecwriteups.com/how-to-uncover-hidden-attack-surfaces-recon-part-6-61e43976ed22?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2025-02-12
fetch_date: 2025-10-06T20:34:47.790483
---

# How to Uncover Hidden Attack Surfaces? Recon part 6

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2F61e43976ed22&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fhow-to-uncover-hidden-attack-surfaces-recon-part-6-61e43976ed22&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fhow-to-uncover-hidden-attack-surfaces-recon-part-6-61e43976ed22&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-61e43976ed22---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-61e43976ed22---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

Member-only story

# How to Uncover Hidden Attack Surfaces? Recon part 6

[![It4chis3c](https://miro.medium.com/v2/resize:fill:64:64/1*ekYPXyjIXBk7Zvd1Tb0oBw.jpeg)](https://it4chis3c.medium.com/?source=post_page---byline--61e43976ed22---------------------------------------)

[It4chis3c](https://it4chis3c.medium.com/?source=post_page---byline--61e43976ed22---------------------------------------)

5 min read

·

Feb 9, 2025

--

Share

Probing | IP Resolution | Port Scanning

[Friend Link | Free Link](https://it4chis3c.medium.com/how-to-uncover-hidden-attack-surfaces-recon-part-6-61e43976ed22)

Hi geeks, ***it4chis3c*** ([Twitter](https://x.com/it4chis3c)) came-up with another bounty earning write-up in the Bug Bounty Hunting Series:

![It4chis3c](https://miro.medium.com/v2/resize:fill:40:40/1*ekYPXyjIXBk7Zvd1Tb0oBw.jpeg)

[It4chis3c](https://it4chis3c.medium.com/?source=post_page-----61e43976ed22---------------------------------------)

## Bug Bounty Hunting Series

[View list](https://it4chis3c.medium.com/list/bug-bounty-hunting-series-fb1cd38823f1?source=post_page-----61e43976ed22---------------------------------------)

43 stories

![](https://miro.medium.com/v2/resize:fill:388:388/1*5-rzwuDYy6rm9GggmhkRtw.png)

![](https://miro.medium.com/v2/resize:fill:388:388/1*3W5rcFkvh_LYTEoEzjEs6Q.png)

![](https://miro.medium.com/v2/resize:fill:388:388/1*JH5F-vhNDF3wXYiMLIbN_w.png)

Press enter or click to view image in full size

![]()

Credit: DALL-E

Up until now, in my previous write-ups I have demonstrated steps & actions to collect subdomains related to target. Save all the collected subdomains via different tools in a single file. For example, “**subdomains.txt**”.

In this writeup i will cover **How you can Uncover & Increase your Attack Surface”**. If you are a beginner, then I’d recommend you to read these 3 write-ups to have a better idea about what I am talking in this writeup.

[## How to Find More Subdomains for Bug Bounties? Dive into Recon part 3

### Hi geeks, it4chis3c (Twitter) came-up with another bounty earning write-up in the Bug Bounty Hunting Series:

systemweakness.com](https://systemweakness.com/how-to-find-more-subdomains-for-bug-bounties-dive-into-recon-part-3-c9825eac2d68?source=post_page-----61e43976ed22---------------------------------------)

--

--

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:96:96/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--61e43976ed22---------------------------------------)

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:128:128/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--61e43976ed22---------------------------------------)

Follow

[## Published in InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---post_publication_info--61e43976ed22---------------------------------------)

[71K followers](/followers?source=post_page---post_publication_info--61e43976ed22---------------------------------------)

·[Last published just now](/actuator-unleashed-a-guide-to-finding-and-exploiting-spring-boot-actuator-endpoints-29252dcd9d79?source=post_page---post_publication_info--61e43976ed22---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow

[![It4chis3c](https://miro.medium.com/v2/resize:fill:96:96/1*ekYPXyjIXBk7Zvd1Tb0oBw.jpeg)](https://it4chis3c.medium.com/?source=post_page---post_author_info--61e43976ed22---------------------------------------)

[![It4chis3c](https://miro.medium.com/v2/resize:fill:128:128/1*ekYPXyjIXBk7Zvd1Tb0oBw.jpeg)](https://it4chis3c.medium.com/?source=post_page---post_author_info--61e43976ed22---------------------------------------)

[## Written by It4chis3c](https://it4chis3c.medium.com/?source=post_page---post_author_info--61e43976ed22---------------------------------------)

[2.5K followers](https://it4chis3c.medium.com/followers?source=post_page---post_author_info--61e43976ed22---------------------------------------)

·[27 following](https://medium.com/%40it4chis3c/following?source=post_page---post_author_info--61e43976ed22---------------------------------------)

Security Researcher | Bug Bounties | Tips & Tricks

## No responses yet

[Help](https://help.medium.com/hc/en-us?source=post_page-----61e43976ed22---------------------------------------)

[Status](https://status.medium.com/?source=post_page-----61e43976ed22---------------------------------------)

[About](https://medium.com/about?autoplay=1&source=post_page-----61e43976ed22---------------------------------------)

[Careers](https://medium.com/jobs-at-medium/work-at-medium-959d1a85284e?source=post_page-----61e43976ed22---------------------------------------)

Press

[Blog](https://blog.medium.com/?source=post_page-----61e43976ed22---------------------------------------)

[Privacy](https://policy.medium.com/medium-privacy-policy-f03bf92035c9?source=post_page-----61e43976ed22---------------------------------------)

[Rules](https://policy.medium.com/medium-rules-30e5502c4eb4?source=post_page-----61e43976ed22---------------------------------------)

[Terms](https://policy.medium.com/medium-terms-of-service-9db0094a1e0f?source=post_page-----61e43976ed22---------------------------------------)

[Text to speech](https://speechify.com/medium?source=post_page-----61e43976ed22---------------------------------------)