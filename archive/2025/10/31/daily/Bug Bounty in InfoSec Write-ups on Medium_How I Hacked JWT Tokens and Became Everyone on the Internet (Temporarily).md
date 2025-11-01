---
title: How I Hacked JWT Tokens and Became Everyone on the Internet (Temporarily)
url: https://infosecwriteups.com/how-i-hacked-jwt-tokens-and-became-everyone-on-the-internet-temporarily-1e05f961048d?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2025-10-31
fetch_date: 2025-11-01T03:11:14.781342
---

# How I Hacked JWT Tokens and Became Everyone on the Internet (Temporarily)

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2F1e05f961048d&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fhow-i-hacked-jwt-tokens-and-became-everyone-on-the-internet-temporarily-1e05f961048d&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fhow-i-hacked-jwt-tokens-and-became-everyone-on-the-internet-temporarily-1e05f961048d&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-1e05f961048d---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-1e05f961048d---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

Member-only story

# How I Hacked JWT Tokens and Became Everyone on the Internet (Temporarily) 😈

[![Iski](https://miro.medium.com/v2/resize:fill:64:64/1*PpvkjPQ1lY6aTYHT9kDX5w.png)](https://medium.com/%40iski?source=post_page---byline--1e05f961048d---------------------------------------)

[Iski](https://medium.com/%40iski?source=post_page---byline--1e05f961048d---------------------------------------)

6 min read

·

Oct 19, 2025

--

Share

Hey there!😁

Free [Link](https://medium.com/%40iski/how-i-hacked-jwt-tokens-and-became-everyone-on-the-internet-temporarily-1e05f961048d?sk=858472fdb5a352604ed70ed49741f426) 🎈

Press enter or click to view image in full size

![]()

Image by AI

You know that moment when you find a spare key under someone’s doormat and think “Wow, people actually do this?” Well, I found the digital equivalent last week. Except instead of a physical key, it was JSON Web Tokens, and instead of one house, it was every user’s account on the entire platform. All because someone left the key to the kingdom under a virtual doormat labeled “security.” 🗝️

It all started when I was testing “SocialFlow,” a new social media platform that was getting hype for its “military-grade security.” I had a basic user account and was ready to poke around. Little did I know I was about to become the master of keys…

[## 🌩️ DNS and Deception: How SSRF and Metadata Gave Me Cloud Access on a Silver Platter 🧠📦

### Hey there!😁

infosecwriteups.com](/%EF%B8%8F-dns-and-deception-how-ssrf-and-metadata-gave-me-cloud-access-on-a-silver-platter-e9cf97c3693f?source=post_page-----1e05f961048d---------------------------------------)

## Act 1: The Accidental Discovery — Token Troubles 🔍

After my standard recon (I should really make a keyboard shortcut for `subfinder | httpx | gau` by now), I found SocialFlow's API. I created two test accounts and started capturing traffic in Burp.

--

--

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:96:96/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--1e05f961048d---------------------------------------)

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:128:128/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--1e05f961048d---------------------------------------)

Follow

[## Published in InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---post_publication_info--1e05f961048d---------------------------------------)

[73K followers](/followers?source=post_page---post_publication_info--1e05f961048d---------------------------------------)

·[Last published 19 hours ago](/everyone-wants-to-hack-no-one-wants-to-think-a6bb8a313501?source=post_page---post_publication_info--1e05f961048d---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow

[![Iski](https://miro.medium.com/v2/resize:fill:96:96/1*PpvkjPQ1lY6aTYHT9kDX5w.png)](https://medium.com/%40iski?source=post_page---post_author_info--1e05f961048d---------------------------------------)

[![Iski](https://miro.medium.com/v2/resize:fill:128:128/1*PpvkjPQ1lY6aTYHT9kDX5w.png)](https://medium.com/%40iski?source=post_page---post_author_info--1e05f961048d---------------------------------------)

[## Written by Iski](https://medium.com/%40iski?source=post_page---post_author_info--1e05f961048d---------------------------------------)

[1.92K followers](https://medium.com/%40iski/followers?source=post_page---post_author_info--1e05f961048d---------------------------------------)

·[7 following](https://medium.com/%40iski/following?source=post_page---post_author_info--1e05f961048d---------------------------------------)

Cybersecurity Researcher | Penetration Tester | Bug Bounty Hunter | Web security| Passionate about cyber security, security automation

## No responses yet

[Help](https://help.medium.com/hc/en-us?source=post_page-----1e05f961048d---------------------------------------)

[Status](https://status.medium.com/?source=post_page-----1e05f961048d---------------------------------------)

[About](https://medium.com/about?autoplay=1&source=post_page-----1e05f961048d---------------------------------------)

[Careers](https://medium.com/jobs-at-medium/work-at-medium-959d1a85284e?source=post_page-----1e05f961048d---------------------------------------)

Press

[Blog](https://blog.medium.com/?source=post_page-----1e05f961048d---------------------------------------)

[Privacy](https://policy.medium.com/medium-privacy-policy-f03bf92035c9?source=post_page-----1e05f961048d---------------------------------------)

[Rules](https://policy.medium.com/medium-rules-30e5502c4eb4?source=post_page-----1e05f961048d---------------------------------------)

[Terms](https://policy.medium.com/medium-terms-of-service-9db0094a1e0f?source=post_page-----1e05f961048d---------------------------------------)

[Text to speech](https://speechify.com/medium?source=post_page-----1e05f961048d---------------------------------------)