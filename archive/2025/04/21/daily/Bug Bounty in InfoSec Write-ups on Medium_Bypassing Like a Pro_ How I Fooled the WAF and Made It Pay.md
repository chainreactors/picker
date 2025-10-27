---
title: Bypassing Like a Pro: How I Fooled the WAF and Made It Pay
url: https://infosecwriteups.com/bypassing-like-a-pro-how-i-fooled-the-waf-and-made-it-pay-e433193e1d9d?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2025-04-21
fetch_date: 2025-10-06T22:04:18.705702
---

# Bypassing Like a Pro: How I Fooled the WAF and Made It Pay

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2Fe433193e1d9d&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fbypassing-like-a-pro-how-i-fooled-the-waf-and-made-it-pay-e433193e1d9d&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fbypassing-like-a-pro-how-i-fooled-the-waf-and-made-it-pay-e433193e1d9d&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-e433193e1d9d---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-e433193e1d9d---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

Member-only story

# Bypassing Like a Pro: How I Fooled the WAF and Made It Pay 💸🧢

[![Iski](https://miro.medium.com/v2/resize:fill:64:64/1*PpvkjPQ1lY6aTYHT9kDX5w.png)](https://medium.com/%40iski?source=post_page---byline--e433193e1d9d---------------------------------------)

[Iski](https://medium.com/%40iski?source=post_page---byline--e433193e1d9d---------------------------------------)

3 min read

·

Apr 18, 2025

--

2

Share

Free [Link](https://medium.com/%40iski/bypassing-like-a-pro-how-i-fooled-the-waf-and-made-it-pay-e433193e1d9d?sk=41fc2ad27b7c14e30b45791ddb9fa42d)🎈

Hi there!

Press enter or click to view image in full size

![]()

Image by Gemini AI

## Life Update (aka Why I Was Staring at My Screen at 3AM 😵‍💫):

My electricity bill was higher than my bug bounty payout. My fridge was making scarier noises than the WAF I was about to face. And the only firewall I wanted to break down was between me and a big juicy bounty. 🍔💰

So like every emotionally stable hacker, I skipped sleep, brewed some 3AM coffee (half hope, half caffeine), and whispered: *“WAF, you’re going down.”*

[## From Recon to RCE: How AI and a cup of Boost Helped Me Turn SQLi into a Command Injection Jackpot…

### Free Link🎈

infosecwriteups.com](/from-recon-to-rce-how-ai-and-a-cup-of-boost-helped-me-turn-sqli-into-a-command-injection-jackpot-1f62dc829956?source=post_page-----e433193e1d9d---------------------------------------)

## 🔍 Phase 1: Mass Recon Mode: Activated

I was hunting on a private program with pretty good scope — lots of subdomains, few known assets, and decent bounty range. I started with:

* `subfinder`, `amass`, and `dnsx` for subdomain enumeration
* `httpx` to probe live hosts
* JavaScript scraping using `getJS` and `LinkFinder`
* Grepping for API keys, secrets…

--

--

2

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:96:96/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--e433193e1d9d---------------------------------------)

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:128:128/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--e433193e1d9d---------------------------------------)

Follow

[## Published in InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---post_publication_info--e433193e1d9d---------------------------------------)

[71K followers](/followers?source=post_page---post_publication_info--e433193e1d9d---------------------------------------)

·[Last published 1 hour ago](/actuator-unleashed-a-guide-to-finding-and-exploiting-spring-boot-actuator-endpoints-29252dcd9d79?source=post_page---post_publication_info--e433193e1d9d---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow

[![Iski](https://miro.medium.com/v2/resize:fill:96:96/1*PpvkjPQ1lY6aTYHT9kDX5w.png)](https://medium.com/%40iski?source=post_page---post_author_info--e433193e1d9d---------------------------------------)

[![Iski](https://miro.medium.com/v2/resize:fill:128:128/1*PpvkjPQ1lY6aTYHT9kDX5w.png)](https://medium.com/%40iski?source=post_page---post_author_info--e433193e1d9d---------------------------------------)

[## Written by Iski](https://medium.com/%40iski?source=post_page---post_author_info--e433193e1d9d---------------------------------------)

[1.8K followers](https://medium.com/%40iski/followers?source=post_page---post_author_info--e433193e1d9d---------------------------------------)

·[7 following](https://medium.com/%40iski/following?source=post_page---post_author_info--e433193e1d9d---------------------------------------)

Cybersecurity Researcher | Penetration Tester | Bug Bounty Hunter | Web security| Passionate about cyber security, security automation

## Responses (2)

See all responses

[Help](https://help.medium.com/hc/en-us?source=post_page-----e433193e1d9d---------------------------------------)

[Status](https://status.medium.com/?source=post_page-----e433193e1d9d---------------------------------------)

[About](https://medium.com/about?autoplay=1&source=post_page-----e433193e1d9d---------------------------------------)

[Careers](https://medium.com/jobs-at-medium/work-at-medium-959d1a85284e?source=post_page-----e433193e1d9d---------------------------------------)

Press

[Blog](https://blog.medium.com/?source=post_page-----e433193e1d9d---------------------------------------)

[Privacy](https://policy.medium.com/medium-privacy-policy-f03bf92035c9?source=post_page-----e433193e1d9d---------------------------------------)

[Rules](https://policy.medium.com/medium-rules-30e5502c4eb4?source=post_page-----e433193e1d9d---------------------------------------)

[Terms](https://policy.medium.com/medium-terms-of-service-9db0094a1e0f?source=post_page-----e433193e1d9d---------------------------------------)

[Text to speech](https://speechify.com/medium?source=post_page-----e433193e1d9d---------------------------------------)