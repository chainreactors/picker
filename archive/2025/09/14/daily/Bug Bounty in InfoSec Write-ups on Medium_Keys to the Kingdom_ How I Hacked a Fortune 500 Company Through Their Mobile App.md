---
title: Keys to the Kingdom: How I Hacked a Fortune 500 Company Through Their Mobile App
url: https://infosecwriteups.com/keys-to-the-kingdom-how-i-hacked-a-fortune-500-company-through-their-mobile-app-e26debedd3f3?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2025-09-14
fetch_date: 2025-10-02T20:08:53.560628
---

# Keys to the Kingdom: How I Hacked a Fortune 500 Company Through Their Mobile App

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2Fe26debedd3f3&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fkeys-to-the-kingdom-how-i-hacked-a-fortune-500-company-through-their-mobile-app-e26debedd3f3&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fkeys-to-the-kingdom-how-i-hacked-a-fortune-500-company-through-their-mobile-app-e26debedd3f3&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-e26debedd3f3---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-e26debedd3f3---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

Member-only story

# 🔑 Keys to the Kingdom: How I Hacked a Fortune 500 Company Through Their Mobile App

[![Iski](https://miro.medium.com/v2/resize:fill:64:64/1*PpvkjPQ1lY6aTYHT9kDX5w.png)](https://medium.com/%40iski?source=post_page---byline--e26debedd3f3---------------------------------------)

[Iski](https://medium.com/%40iski?source=post_page---byline--e26debedd3f3---------------------------------------)

5 min read

·

Sep 13, 2025

--

3

Share

Free [Link](https://medium.com/%40iski/keys-to-the-kingdom-how-i-hacked-a-fortune-500-company-through-their-mobile-app-e26debedd3f3?sk=9f57f7c73831dd9a2299cfbd984a844f) 🎈

Hey there!😁

Press enter or click to view image in full size

![]()

Image by AI

From downloading an Android app to extracting AWS keys, API secrets, and full database access. Join my journey of reverse engineering, decompiling, and exploiting hardcoded secrets for a critical bounty. Full PoC included. ☕

You know that feeling when you lose your actual keys and find them months later in the pocket of an old jacket? 🧥 That was me — but instead of keys, I found hardcoded AWS credentials, and instead of a jacket, it was a multi-million dollar company’s mobile app. My roommate thought I was crazy celebrating in the living room at 3 AM. Little did he know, I’d just found the digital keys to their entire kingdom.

It all started when I decided to shift my focus from web apps to mobile. I downloaded the Android APK for a major retail company — let’s call them “MegaShop” — from a mirror site (always get permission first! ⚠️).

[## 🔒 From Locked to Looted: My Journey of IDOR Chains to Almost-Admin Access

### Free Link 🎈

infosecwriteups.com](/from-locked-to-looted-my-journey-of-idor-chains-to-almost-admin-access-d15abf0046f9?source=post_page-----e26debedd3f3---------------------------------------)

## 🎯 Phase 1: Cracking Open the APK

--

--

3

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:96:96/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--e26debedd3f3---------------------------------------)

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:128:128/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--e26debedd3f3---------------------------------------)

Follow

[## Published in InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---post_publication_info--e26debedd3f3---------------------------------------)

[71K followers](/followers?source=post_page---post_publication_info--e26debedd3f3---------------------------------------)

·[Last published 4 days ago](/how-to-find-p1-bugs-using-google-in-your-target-part-1-e37455324dc1?source=post_page---post_publication_info--e26debedd3f3---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow

[![Iski](https://miro.medium.com/v2/resize:fill:96:96/1*PpvkjPQ1lY6aTYHT9kDX5w.png)](https://medium.com/%40iski?source=post_page---post_author_info--e26debedd3f3---------------------------------------)

[![Iski](https://miro.medium.com/v2/resize:fill:128:128/1*PpvkjPQ1lY6aTYHT9kDX5w.png)](https://medium.com/%40iski?source=post_page---post_author_info--e26debedd3f3---------------------------------------)

[## Written by Iski](https://medium.com/%40iski?source=post_page---post_author_info--e26debedd3f3---------------------------------------)

[1.8K followers](https://medium.com/%40iski/followers?source=post_page---post_author_info--e26debedd3f3---------------------------------------)

·[7 following](https://medium.com/%40iski/following?source=post_page---post_author_info--e26debedd3f3---------------------------------------)

Cybersecurity Researcher | Penetration Tester | Bug Bounty Hunter | Web security| Passionate about cyber security, security automation

## Responses (3)

See all responses

[Help](https://help.medium.com/hc/en-us?source=post_page-----e26debedd3f3---------------------------------------)

[Status](https://status.medium.com/?source=post_page-----e26debedd3f3---------------------------------------)

[About](https://medium.com/about?autoplay=1&source=post_page-----e26debedd3f3---------------------------------------)

[Careers](https://medium.com/jobs-at-medium/work-at-medium-959d1a85284e?source=post_page-----e26debedd3f3---------------------------------------)

Press

[Blog](https://blog.medium.com/?source=post_page-----e26debedd3f3---------------------------------------)

[Privacy](https://policy.medium.com/medium-privacy-policy-f03bf92035c9?source=post_page-----e26debedd3f3---------------------------------------)

[Rules](https://policy.medium.com/medium-rules-30e5502c4eb4?source=post_page-----e26debedd3f3---------------------------------------)

[Terms](https://policy.medium.com/medium-terms-of-service-9db0094a1e0f?source=post_page-----e26debedd3f3---------------------------------------)

[Text to speech](https://speechify.com/medium?source=post_page-----e26debedd3f3---------------------------------------)