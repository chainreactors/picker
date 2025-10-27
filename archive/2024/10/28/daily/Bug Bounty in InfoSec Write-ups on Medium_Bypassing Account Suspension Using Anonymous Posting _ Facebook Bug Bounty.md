---
title: Bypassing Account Suspension Using Anonymous Posting | Facebook Bug Bounty
url: https://infosecwriteups.com/bypassing-account-suspension-using-anonymous-posting-facebook-bug-bounty-b204433c98d1?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2024-10-28
fetch_date: 2025-10-06T18:48:15.008876
---

# Bypassing Account Suspension Using Anonymous Posting | Facebook Bug Bounty

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2Fb204433c98d1&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fbypassing-account-suspension-using-anonymous-posting-facebook-bug-bounty-b204433c98d1&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fbypassing-account-suspension-using-anonymous-posting-facebook-bug-bounty-b204433c98d1&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-b204433c98d1---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-b204433c98d1---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

# Bypassing Account Suspension Using Anonymous Posting | Facebook Bug Bounty

[![Ph.Hitachi](https://miro.medium.com/v2/da:true/resize:fill:64:64/0*WZn-64UUVRL95-ov)](https://ph-hitachi.medium.com/?source=post_page---byline--b204433c98d1---------------------------------------)

[Ph.Hitachi](https://ph-hitachi.medium.com/?source=post_page---byline--b204433c98d1---------------------------------------)

Jul 17, 2024

--

Listen

Share

Hi guys,

so i want to share my recent bug bounty at facebook this year.

![]()

The user that has been suspended on the group can still post & comments via anonymous posting, this happen because anonymous posting generate an anonymous id aside from the real user id of suspended accounts.

## PoC:

![]()

**Timeline**:
- June 29, 2024 —**Initial Report**
- July 1, 2024 — **Triaged**
- July 3, 2024 — **Bounty awarded**
- July 17, 2024 — **Fixed**

Contact:
Email: ph-hitachi@wearehackerone.com
Twitter: <https://x.com/PhHitachi>
LinkedIn: [www.linkedin.com/in/phhitachi](http://www.linkedin.com/in/phhitachi)

[Bug Bounty](https://medium.com/tag/bug-bounty?source=post_page-----b204433c98d1---------------------------------------)

[Facebook Bug Bounty](https://medium.com/tag/facebook-bug-bounty?source=post_page-----b204433c98d1---------------------------------------)

[Bypass Restriction](https://medium.com/tag/bypass-restriction?source=post_page-----b204433c98d1---------------------------------------)

--

--

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:96:96/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--b204433c98d1---------------------------------------)

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:128:128/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--b204433c98d1---------------------------------------)

Follow

[## Published in InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---post_publication_info--b204433c98d1---------------------------------------)

[71K followers](/followers?source=post_page---post_publication_info--b204433c98d1---------------------------------------)

·[Last published 3 hours ago](/baby-dfc2547dc387?source=post_page---post_publication_info--b204433c98d1---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow

[![Ph.Hitachi](https://miro.medium.com/v2/resize:fill:96:96/0*WZn-64UUVRL95-ov)](https://ph-hitachi.medium.com/?source=post_page---post_author_info--b204433c98d1---------------------------------------)

[![Ph.Hitachi](https://miro.medium.com/v2/resize:fill:128:128/0*WZn-64UUVRL95-ov)](https://ph-hitachi.medium.com/?source=post_page---post_author_info--b204433c98d1---------------------------------------)

[## Written by Ph.Hitachi](https://ph-hitachi.medium.com/?source=post_page---post_author_info--b204433c98d1---------------------------------------)

[733 followers](https://ph-hitachi.medium.com/followers?source=post_page---post_author_info--b204433c98d1---------------------------------------)

·[4 following](https://medium.com/%40ph-hitachi/following?source=post_page---post_author_info--b204433c98d1---------------------------------------)

Read A Quality & Amazing Bugs and Unique Security Issues Related Follow me <https://x.com/PhHitachi>

## No responses yet

[Help](https://help.medium.com/hc/en-us?source=post_page-----b204433c98d1---------------------------------------)

[Status](https://status.medium.com/?source=post_page-----b204433c98d1---------------------------------------)

[About](https://medium.com/about?autoplay=1&source=post_page-----b204433c98d1---------------------------------------)

[Careers](https://medium.com/jobs-at-medium/work-at-medium-959d1a85284e?source=post_page-----b204433c98d1---------------------------------------)

Press

[Blog](https://blog.medium.com/?source=post_page-----b204433c98d1---------------------------------------)

[Privacy](https://policy.medium.com/medium-privacy-policy-f03bf92035c9?source=post_page-----b204433c98d1---------------------------------------)

[Rules](https://policy.medium.com/medium-rules-30e5502c4eb4?source=post_page-----b204433c98d1---------------------------------------)

[Terms](https://policy.medium.com/medium-terms-of-service-9db0094a1e0f?source=post_page-----b204433c98d1---------------------------------------)

[Text to speech](https://speechify.com/medium?source=post_page-----b204433c98d1---------------------------------------)