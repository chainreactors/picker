---
title: From 404 to $4,000: Real Bugs Found in Forgotten Endpoints
url: https://infosecwriteups.com/from-404-to-4-000-real-bugs-found-in-forgotten-endpoints-5886c06f7473?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2025-11-09
fetch_date: 2025-11-10T03:17:42.757231
---

# From 404 to $4,000: Real Bugs Found in Forgotten Endpoints

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2F5886c06f7473&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Ffrom-404-to-4-000-real-bugs-found-in-forgotten-endpoints-5886c06f7473&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Ffrom-404-to-4-000-real-bugs-found-in-forgotten-endpoints-5886c06f7473&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-5886c06f7473---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-5886c06f7473---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

Member-only story

# From 404 to $4,000: Real Bugs Found in Forgotten Endpoints

## Most hunters scroll past a 404. I didn’t and that single dead-looking endpoint turned into a $4,000 bounty.

[![Monika sharma](https://miro.medium.com/v2/da:true/resize:fill:64:64/0*Tv4b4p5mb6J3IJwD)](https://medium.com/%40commanak46?source=post_page---byline--5886c06f7473---------------------------------------)

[Monika sharma](https://medium.com/%40commanak46?source=post_page---byline--5886c06f7473---------------------------------------)

5 min read

·

18 hours ago

--

Share

Press enter or click to view image in full size

![]()

I learned early that “not found” often means “not looked at.” In large systems, endpoints die, versions split, and shadow routes persist on backends or in old mobile apps. Those forgotten endpoints are low-noise, high-impact targets. This article walks you through the mindset, the techniques and real-case archetypes that turn a casual 404 into a serious payout without being noisy or reckless.

### The forgotten-endpoint phenomenon

Forgotten endpoints aren’t glamorous. They’re leftovers from migrations, abandoned feature branches, mobile clients that never got updated or configuration files left in build artifacts. Typical origins:

* API versioning drift (/api/v1/ still running while /api/v3/ is live)
* Developer debug routes and admin stubs (/debug/, /admin\_old/)
* Old mobile app endpoints that the frontend stopped using but the backend still serves
* Misrouted CDN or caching configurations that expose archive paths

--

--

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:96:96/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--5886c06f7473---------------------------------------)

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:128:128/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--5886c06f7473---------------------------------------)

Follow

[## Published in InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---post_publication_info--5886c06f7473---------------------------------------)

[73K followers](/followers?source=post_page---post_publication_info--5886c06f7473---------------------------------------)

·[Last published 17 hours ago](/from-wooden-ducks-to-digital-flags-my-first-v1t-ctf-osint-challenge-84c38c9fbcb8?source=post_page---post_publication_info--5886c06f7473---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow

[![Monika sharma](https://miro.medium.com/v2/resize:fill:96:96/0*Tv4b4p5mb6J3IJwD)](https://medium.com/%40commanak46?source=post_page---post_author_info--5886c06f7473---------------------------------------)

[![Monika sharma](https://miro.medium.com/v2/resize:fill:128:128/0*Tv4b4p5mb6J3IJwD)](https://medium.com/%40commanak46?source=post_page---post_author_info--5886c06f7473---------------------------------------)

[## Written by Monika sharma](https://medium.com/%40commanak46?source=post_page---post_author_info--5886c06f7473---------------------------------------)

[2.1K followers](https://medium.com/%40commanak46/followers?source=post_page---post_author_info--5886c06f7473---------------------------------------)

·[7 following](https://medium.com/%40commanak46/following?source=post_page---post_author_info--5886c06f7473---------------------------------------)

## No responses yet

[Help](https://help.medium.com/hc/en-us?source=post_page-----5886c06f7473---------------------------------------)

[Status](https://status.medium.com/?source=post_page-----5886c06f7473---------------------------------------)

[About](https://medium.com/about?autoplay=1&source=post_page-----5886c06f7473---------------------------------------)

[Careers](https://medium.com/jobs-at-medium/work-at-medium-959d1a85284e?source=post_page-----5886c06f7473---------------------------------------)

Press

[Blog](https://blog.medium.com/?source=post_page-----5886c06f7473---------------------------------------)

[Privacy](https://policy.medium.com/medium-privacy-policy-f03bf92035c9?source=post_page-----5886c06f7473---------------------------------------)

[Rules](https://policy.medium.com/medium-rules-30e5502c4eb4?source=post_page-----5886c06f7473---------------------------------------)

[Terms](https://policy.medium.com/medium-terms-of-service-9db0094a1e0f?source=post_page-----5886c06f7473---------------------------------------)

[Text to speech](https://speechify.com/medium?source=post_page-----5886c06f7473---------------------------------------)