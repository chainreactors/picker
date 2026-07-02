---
title: Auth Bypass is it?
url: https://infosecwriteups.com/auth-bypass-is-it-bb19f10cbbba?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2026-07-01
fetch_date: 2026-07-02T05:56:49.381555
---

# Auth Bypass is it?

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://play.google.com/store/apps/details?id=com.medium.reader&referrer=utm_source%3DmobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fauth-bypass-is-it-bb19f10cbbba&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

Get app

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fauth-bypass-is-it-bb19f10cbbba&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![Unknown user](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-bb19f10cbbba---------------------------------------)

·

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-bb19f10cbbba---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Member-only story

# Auth Bypass is it?

[![Devansh Patel](https://miro.medium.com/v2/resize:fill:64:64/1*UbOj48VcY7qPnQSGWQhuaA.jpeg)](https://medium.com/%40devanshpatel930?source=post_page---byline--bb19f10cbbba---------------------------------------)

[Devansh Patel](https://medium.com/%40devanshpatel930?source=post_page---byline--bb19f10cbbba---------------------------------------)

4 min read

·

19 hours ago

--

[Listen](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2Fplans%3Fdimension%3Dpost_audio_button%26postId%3Dbb19f10cbbba&operation=register&redirect=https%3A%2F%2Finfosecwriteups.com%2Fauth-bypass-is-it-bb19f10cbbba&source=---header_actions--bb19f10cbbba---------------------post_audio_button------------------)

Share

> *Target, domains, API keys, bearer tokens, SSO IDs, and organisation names are redacted. This writeup is for educational purposes and describes testing performed in an authorised UAT bug bounty scope.*

Press enter or click to view image in full size

![]()

## Summary

After finding a client-side encrypted API flow, I looked for other places where the application trusted encrypted data from the browser.

One interesting flow was an MSPACE-style auto-login/deeplink feature. The frontend accepted a `data` URL parameter, decrypted it with a client-side key/IV, parsed it as JSON, and sent the values to a backend endpoint:

```
POST /<REDACTED_PATH>/api/leads/control-transfer
```

The critical finding was that the backend returned a successful MSPACE token-validation message even when the inner MSPACE token was a random fake string.

## The Two Token Layers

This bug involved two different token concepts:

```
1. Outer API bearer token
   Sent in the Authorisation header.
   Required to call the backend API.

2. Inner MSPACE deeplink token
   Sent inside the encrypted JSON request body.
   Supposed to prove the MSPACE deeplink/control-transfer is legitimate.
```

The outer API bearer token was valid. The vulnerability was that the inner MSPACE token was fake, but the backend still…

--

--

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:96:96/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--bb19f10cbbba---------------------------------------)

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:128:128/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--bb19f10cbbba---------------------------------------)

[## Published in InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---post_publication_info--bb19f10cbbba---------------------------------------)

[87K followers](/followers?source=post_page---post_publication_info--bb19f10cbbba---------------------------------------)

·[Last published 19 hours ago](/how-i-found-an-email-verification-bypass-on-an-ai-freelance-platform-6ad76663b658?source=post_page---post_publication_info--bb19f10cbbba---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

[![Devansh Patel](https://miro.medium.com/v2/resize:fill:96:96/1*UbOj48VcY7qPnQSGWQhuaA.jpeg)](https://medium.com/%40devanshpatel930?source=post_page---post_author_info--bb19f10cbbba---------------------------------------)

[![Devansh Patel](https://miro.medium.com/v2/resize:fill:128:128/1*UbOj48VcY7qPnQSGWQhuaA.jpeg)](https://medium.com/%40devanshpatel930?source=post_page---post_author_info--bb19f10cbbba---------------------------------------)

[## Written by Devansh Patel](https://medium.com/%40devanshpatel930?source=post_page---post_author_info--bb19f10cbbba---------------------------------------)

[287 followers](https://medium.com/%40devanshpatel930/followers?source=post_page---post_author_info--bb19f10cbbba---------------------------------------)

·[9 following](https://medium.com/%40devanshpatel930/following?source=post_page---post_author_info--bb19f10cbbba---------------------------------------)

Hacking legally so companies don’t get hacked illegally. Cybersecurity analyst | Bug bounty hunter | Breaking things so others can call it ‘secure’

[Help](https://help.medium.com/hc/en-us?source=post_page-----bb19f10cbbba---------------------------------------)

[Status](https://status.medium.com/?source=post_page-----bb19f10cbbba---------------------------------------)

[About](https://medium.com/about?autoplay=1&source=post_page-----bb19f10cbbba---------------------------------------)

[Careers](https://medium.com/jobs-at-medium/work-at-medium-959d1a85284e?source=post_page-----bb19f10cbbba---------------------------------------)

Press

[Blog](https://blog.medium.com/?source=post_page-----bb19f10cbbba---------------------------------------)

[Store](https://medium.com/store)

[Privacy](https://policy.medium.com/medium-privacy-policy-f03bf92035c9?source=post_page-----bb19f10cbbba---------------------------------------)

[Rules](https://policy.medium.com/medium-rules-30e5502c4eb4?source=post_page-----bb19f10cbbba---------------------------------------)

[Terms](https://policy.medium.com/medium-terms-of-service-9db0094a1e0f?source=post_page-----bb19f10cbbba---------------------------------------)

[Text to speech](https://speechify.com/medium?source=post_page-----bb19f10cbbba---------------------------------------)