---
title: $500 Bounty: Subdomain Takeover on live.firefox.com via Unclaimed Fastly CNAME
url: https://infosecwriteups.com/500-bounty-subdomain-takeover-on-live-firefox-com-via-unclaimed-fastly-cname-c7d1971e1a32?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2025-07-06
fetch_date: 2025-10-06T23:26:44.583252
---

# $500 Bounty: Subdomain Takeover on live.firefox.com via Unclaimed Fastly CNAME

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2Fc7d1971e1a32&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2F500-bounty-subdomain-takeover-on-live-firefox-com-via-unclaimed-fastly-cname-c7d1971e1a32&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2F500-bounty-subdomain-takeover-on-live-firefox-com-via-unclaimed-fastly-cname-c7d1971e1a32&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-c7d1971e1a32---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-c7d1971e1a32---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

Member-only story

# $500 Bounty: Subdomain Takeover on `live.firefox.com` via Unclaimed Fastly CNAME

## **How an Unregistered CDN Entry Could’ve Been Weaponized for Malware Campaigns and Cookie-Based Attacks**

[![Monika sharma](https://miro.medium.com/v2/da:true/resize:fill:64:64/0*Tv4b4p5mb6J3IJwD)](https://medium.com/%40commanak46?source=post_page---byline--c7d1971e1a32---------------------------------------)

[Monika sharma](https://medium.com/%40commanak46?source=post_page---byline--c7d1971e1a32---------------------------------------)

3 min read

·

Jul 5, 2025

--

2

Share

Press enter or click to view image in full size

![]()

When a domain as recognizable as `firefox.com` has a dangling subdomain, it’s not just a technical misstep—it’s an open door for phishing, malware delivery, and trust abuse.

Security researcher martinvw earned a $500 bounty from Mozilla by identifying and successfully proving a subdomain takeover vulnerability on `live.firefox.com`. The root cause? A CNAME pointing to Fastly without a corresponding service registration, allowing the researcher to claim the subdomain and serve arbitrary content under Firefox’s domain umbrella.

This write-up details the vulnerability, exploitation process, and the potential real-world impact of such an oversight.

## What is a Subdomain Takeover?

A **subdomain takeover** occurs when:

* A subdomain (e.g., `live.firefox.com`) points via CNAME to a service (like Fastly),
* But that service is not claimed or configured by the original domain owner,
* Allowing attackers to claim the endpoint and control what content is served.

--

--

2

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:96:96/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--c7d1971e1a32---------------------------------------)

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:128:128/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--c7d1971e1a32---------------------------------------)

Follow

[## Published in InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---post_publication_info--c7d1971e1a32---------------------------------------)

[71K followers](/followers?source=post_page---post_publication_info--c7d1971e1a32---------------------------------------)

·[Last published 3 hours ago](/actuator-unleashed-a-guide-to-finding-and-exploiting-spring-boot-actuator-endpoints-29252dcd9d79?source=post_page---post_publication_info--c7d1971e1a32---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow

[![Monika sharma](https://miro.medium.com/v2/resize:fill:96:96/0*Tv4b4p5mb6J3IJwD)](https://medium.com/%40commanak46?source=post_page---post_author_info--c7d1971e1a32---------------------------------------)

[![Monika sharma](https://miro.medium.com/v2/resize:fill:128:128/0*Tv4b4p5mb6J3IJwD)](https://medium.com/%40commanak46?source=post_page---post_author_info--c7d1971e1a32---------------------------------------)

[## Written by Monika sharma](https://medium.com/%40commanak46?source=post_page---post_author_info--c7d1971e1a32---------------------------------------)

[2K followers](https://medium.com/%40commanak46/followers?source=post_page---post_author_info--c7d1971e1a32---------------------------------------)

·[7 following](https://medium.com/%40commanak46/following?source=post_page---post_author_info--c7d1971e1a32---------------------------------------)

## Responses (2)

See all responses

[Help](https://help.medium.com/hc/en-us?source=post_page-----c7d1971e1a32---------------------------------------)

[Status](https://status.medium.com/?source=post_page-----c7d1971e1a32---------------------------------------)

[About](https://medium.com/about?autoplay=1&source=post_page-----c7d1971e1a32---------------------------------------)

[Careers](https://medium.com/jobs-at-medium/work-at-medium-959d1a85284e?source=post_page-----c7d1971e1a32---------------------------------------)

Press

[Blog](https://blog.medium.com/?source=post_page-----c7d1971e1a32---------------------------------------)

[Privacy](https://policy.medium.com/medium-privacy-policy-f03bf92035c9?source=post_page-----c7d1971e1a32---------------------------------------)

[Rules](https://policy.medium.com/medium-rules-30e5502c4eb4?source=post_page-----c7d1971e1a32---------------------------------------)

[Terms](https://policy.medium.com/medium-terms-of-service-9db0094a1e0f?source=post_page-----c7d1971e1a32---------------------------------------)

[Text to speech](https://speechify.com/medium?source=post_page-----c7d1971e1a32---------------------------------------)