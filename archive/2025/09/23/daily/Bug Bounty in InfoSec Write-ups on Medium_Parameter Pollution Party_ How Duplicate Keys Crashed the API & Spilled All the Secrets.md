---
title: Parameter Pollution Party: How Duplicate Keys Crashed the API & Spilled All the Secrets
url: https://infosecwriteups.com/parameter-pollution-party-how-duplicate-keys-crashed-the-api-spilled-all-the-secrets-f2352d6620ab?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2025-09-23
fetch_date: 2025-10-02T20:31:26.128847
---

# Parameter Pollution Party: How Duplicate Keys Crashed the API & Spilled All the Secrets

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2Ff2352d6620ab&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fparameter-pollution-party-how-duplicate-keys-crashed-the-api-spilled-all-the-secrets-f2352d6620ab&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fparameter-pollution-party-how-duplicate-keys-crashed-the-api-spilled-all-the-secrets-f2352d6620ab&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-f2352d6620ab---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-f2352d6620ab---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

Member-only story

# 🎉 Parameter Pollution Party: How Duplicate Keys Crashed the API & Spilled All the Secrets

[![Iski](https://miro.medium.com/v2/resize:fill:64:64/1*PpvkjPQ1lY6aTYHT9kDX5w.png)](https://medium.com/%40iski?source=post_page---byline--f2352d6620ab---------------------------------------)

[Iski](https://medium.com/%40iski?source=post_page---byline--f2352d6620ab---------------------------------------)

4 min read

·

Sep 21, 2025

--

3

Share

Free [Link](https://medium.com/%40iski/parameter-pollution-party-how-duplicate-keys-crashed-the-api-spilled-all-the-secrets-f2352d6620ab?sk=f56539588bafd603364e215c7d603e30) 🎈

Hey there!😁

Press enter or click to view image in full size

![]()

Image by AI

From discovering duplicate parameters to bypassing authentication, accessing internal APIs, and uncovering hidden data. Join my journey of HTTP Parameter Pollution exploitation with full technical PoC. ☕

You know that feeling when you show up to a party uninvited and accidentally become the life of it? 🎊 That was me — but instead of a party, it was a multi-million dollar company’s API endpoint, and instead of funny stories, I brought duplicate URL parameters that crashed their system and spilled all their secrets. My cat watched in judgment as I celebrated finding a bug more predictable than my morning coffee routine.

[## How My Name Crashed a Welcome Party: SSI to RCE Surprise! with $$$$🎉

### Free Link🎈

infosecwriteups.com](/how-my-name-crashed-a-welcome-party-ssi-to-rce-surprise-with-f9b8a05ad138?source=post_page-----f2352d6620ab---------------------------------------)

It all started on a boring Wednesday. Coffee in hand ☕, I was testing a fancy SaaS application — let’s call them `cloudapi.com`. I'd found an interesting endpoint during recon:

```
GET /api/v1/user/profile?userId=12345
```

--

--

3

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:96:96/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--f2352d6620ab---------------------------------------)

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:128:128/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--f2352d6620ab---------------------------------------)

Follow

[## Published in InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---post_publication_info--f2352d6620ab---------------------------------------)

[71K followers](/followers?source=post_page---post_publication_info--f2352d6620ab---------------------------------------)

·[Last published 4 days ago](/how-to-find-p1-bugs-using-google-in-your-target-part-1-e37455324dc1?source=post_page---post_publication_info--f2352d6620ab---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow

[![Iski](https://miro.medium.com/v2/resize:fill:96:96/1*PpvkjPQ1lY6aTYHT9kDX5w.png)](https://medium.com/%40iski?source=post_page---post_author_info--f2352d6620ab---------------------------------------)

[![Iski](https://miro.medium.com/v2/resize:fill:128:128/1*PpvkjPQ1lY6aTYHT9kDX5w.png)](https://medium.com/%40iski?source=post_page---post_author_info--f2352d6620ab---------------------------------------)

[## Written by Iski](https://medium.com/%40iski?source=post_page---post_author_info--f2352d6620ab---------------------------------------)

[1.8K followers](https://medium.com/%40iski/followers?source=post_page---post_author_info--f2352d6620ab---------------------------------------)

·[7 following](https://medium.com/%40iski/following?source=post_page---post_author_info--f2352d6620ab---------------------------------------)

Cybersecurity Researcher | Penetration Tester | Bug Bounty Hunter | Web security| Passionate about cyber security, security automation

## Responses (3)

See all responses

[Help](https://help.medium.com/hc/en-us?source=post_page-----f2352d6620ab---------------------------------------)

[Status](https://status.medium.com/?source=post_page-----f2352d6620ab---------------------------------------)

[About](https://medium.com/about?autoplay=1&source=post_page-----f2352d6620ab---------------------------------------)

[Careers](https://medium.com/jobs-at-medium/work-at-medium-959d1a85284e?source=post_page-----f2352d6620ab---------------------------------------)

Press

[Blog](https://blog.medium.com/?source=post_page-----f2352d6620ab---------------------------------------)

[Privacy](https://policy.medium.com/medium-privacy-policy-f03bf92035c9?source=post_page-----f2352d6620ab---------------------------------------)

[Rules](https://policy.medium.com/medium-rules-30e5502c4eb4?source=post_page-----f2352d6620ab---------------------------------------)

[Terms](https://policy.medium.com/medium-terms-of-service-9db0094a1e0f?source=post_page-----f2352d6620ab---------------------------------------)

[Text to speech](https://speechify.com/medium?source=post_page-----f2352d6620ab---------------------------------------)