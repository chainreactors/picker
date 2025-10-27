---
title: From Locked to Looted: My Journey of IDOR Chains to Almost-Admin Access
url: https://infosecwriteups.com/from-locked-to-looted-my-journey-of-idor-chains-to-almost-admin-access-d15abf0046f9?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2025-09-08
fetch_date: 2025-10-02T19:48:32.964851
---

# From Locked to Looted: My Journey of IDOR Chains to Almost-Admin Access

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2Fd15abf0046f9&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Ffrom-locked-to-looted-my-journey-of-idor-chains-to-almost-admin-access-d15abf0046f9&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Ffrom-locked-to-looted-my-journey-of-idor-chains-to-almost-admin-access-d15abf0046f9&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-d15abf0046f9---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-d15abf0046f9---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

Member-only story

# 🔒 From Locked to Looted: My Journey of IDOR Chains to Almost-Admin Access

[![Iski](https://miro.medium.com/v2/resize:fill:64:64/1*PpvkjPQ1lY6aTYHT9kDX5w.png)](https://medium.com/%40iski?source=post_page---byline--d15abf0046f9---------------------------------------)

[Iski](https://medium.com/%40iski?source=post_page---byline--d15abf0046f9---------------------------------------)

3 min read

·

Sep 7, 2025

--

2

Share

Free [Link](https://medium.com/%40iski/from-locked-to-looted-my-journey-of-idor-chains-to-almost-admin-access-d15abf0046f9?sk=25844b6938a94e67519e4614671fb6b4) 🎈

Hey there!😁

Press enter or click to view image in full size

![]()

Image by AI

You know that feeling when you open your fridge at 3 AM, only to find out your roommate already looted all the pizza? 🍕 That was me — except instead of pizza, it was admin endpoints. And instead of my roommate, it was… me (oops). Welcome to my story of going from “just another recon day” to “oh wait, DID I JUST FIND THE KEYS TO THE KINGDOM?”

And trust me, this isn’t one of those stiff write‑ups where I drop dry payloads and call it a day. This is me, coffee in hand ☕, telling you how an Innocent‑Looking Endpoint™ turned into a shiny bug bounty.

[## 🧩 Puzzle to Pwnage: Decoding Hidden Endpoints for Maximum Exploitation

### Hey there!😁

medium.com](https://medium.com/%40iski/puzzle-to-pwnage-decoding-hidden-endpoints-for-maximum-exploitation-1d2841383ddc?source=post_page-----d15abf0046f9---------------------------------------)

## Recon: My Not‑So‑Boring Netflix Episode

Let’s start with mass recon. Bug hunting is pretty much Netflix binge‑watching, except instead of asking “Play next episode?”, I’m asking “Play next subdomain?”.

* Tools scanning away, subdomains falling like Tetris blocks.
* DNS bruteforcing, certificate transparency logs, the…

--

--

2

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:96:96/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--d15abf0046f9---------------------------------------)

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:128:128/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--d15abf0046f9---------------------------------------)

Follow

[## Published in InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---post_publication_info--d15abf0046f9---------------------------------------)

[71K followers](/followers?source=post_page---post_publication_info--d15abf0046f9---------------------------------------)

·[Last published 4 days ago](/how-to-find-p1-bugs-using-google-in-your-target-part-1-e37455324dc1?source=post_page---post_publication_info--d15abf0046f9---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow

[![Iski](https://miro.medium.com/v2/resize:fill:96:96/1*PpvkjPQ1lY6aTYHT9kDX5w.png)](https://medium.com/%40iski?source=post_page---post_author_info--d15abf0046f9---------------------------------------)

[![Iski](https://miro.medium.com/v2/resize:fill:128:128/1*PpvkjPQ1lY6aTYHT9kDX5w.png)](https://medium.com/%40iski?source=post_page---post_author_info--d15abf0046f9---------------------------------------)

[## Written by Iski](https://medium.com/%40iski?source=post_page---post_author_info--d15abf0046f9---------------------------------------)

[1.8K followers](https://medium.com/%40iski/followers?source=post_page---post_author_info--d15abf0046f9---------------------------------------)

·[7 following](https://medium.com/%40iski/following?source=post_page---post_author_info--d15abf0046f9---------------------------------------)

Cybersecurity Researcher | Penetration Tester | Bug Bounty Hunter | Web security| Passionate about cyber security, security automation

## Responses (2)

See all responses

[Help](https://help.medium.com/hc/en-us?source=post_page-----d15abf0046f9---------------------------------------)

[Status](https://status.medium.com/?source=post_page-----d15abf0046f9---------------------------------------)

[About](https://medium.com/about?autoplay=1&source=post_page-----d15abf0046f9---------------------------------------)

[Careers](https://medium.com/jobs-at-medium/work-at-medium-959d1a85284e?source=post_page-----d15abf0046f9---------------------------------------)

Press

[Blog](https://blog.medium.com/?source=post_page-----d15abf0046f9---------------------------------------)

[Privacy](https://policy.medium.com/medium-privacy-policy-f03bf92035c9?source=post_page-----d15abf0046f9---------------------------------------)

[Rules](https://policy.medium.com/medium-rules-30e5502c4eb4?source=post_page-----d15abf0046f9---------------------------------------)

[Terms](https://policy.medium.com/medium-terms-of-service-9db0094a1e0f?source=post_page-----d15abf0046f9---------------------------------------)

[Text to speech](https://speechify.com/medium?source=post_page-----d15abf0046f9---------------------------------------)