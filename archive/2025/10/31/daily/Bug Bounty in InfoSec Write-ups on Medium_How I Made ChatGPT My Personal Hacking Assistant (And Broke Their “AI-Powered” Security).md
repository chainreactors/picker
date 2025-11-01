---
title: How I Made ChatGPT My Personal Hacking Assistant (And Broke Their “AI-Powered” Security)
url: https://infosecwriteups.com/how-i-made-chatgpt-my-personal-hacking-assistant-and-broke-their-ai-powered-security-ee37d4a725c2?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2025-10-31
fetch_date: 2025-11-01T03:11:13.797368
---

# How I Made ChatGPT My Personal Hacking Assistant (And Broke Their “AI-Powered” Security)

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2Fee37d4a725c2&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fhow-i-made-chatgpt-my-personal-hacking-assistant-and-broke-their-ai-powered-security-ee37d4a725c2&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fhow-i-made-chatgpt-my-personal-hacking-assistant-and-broke-their-ai-powered-security-ee37d4a725c2&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-ee37d4a725c2---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-ee37d4a725c2---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

Member-only story

# How I Made ChatGPT My Personal Hacking Assistant (And Broke Their “AI-Powered” Security) 🤖💥

[![Iski](https://miro.medium.com/v2/resize:fill:64:64/1*PpvkjPQ1lY6aTYHT9kDX5w.png)](https://medium.com/%40iski?source=post_page---byline--ee37d4a725c2---------------------------------------)

[Iski](https://medium.com/%40iski?source=post_page---byline--ee37d4a725c2---------------------------------------)

8 min read

·

1 day ago

--

Share

Free [Link](https://medium.com/%40iski/how-i-made-chatgpt-my-personal-hacking-assistant-and-broke-their-ai-powered-security-ee37d4a725c2?sk=c7552c9b0a649dff69f30473c7c7acd8) 🎈

Hey there!😁

Press enter or click to view image in full size

![]()

Image by AI

You know that feeling when you’re arguing with a customer service chatbot and you realize you’re basically shouting at a brick wall that occasionally says “I understand your frustration”? Yeah, that was me last month. Except instead of trying to get a refund, I was trying to convince an AI-powered firewall that my SQL injection payloads were actually friendly database compliments. And it worked. I used AI to bypass AI security, and for a brief moment, I felt what it must be like to be on the right side of the robot uprising. 🦾

I was testing “NeuroShield,” a company that claimed their AI-powered WAF could “stop 99.9% of attacks using deep learning algorithms.” Their marketing materials featured more buzzwords than a tech conference after three espressos. Challenge accepted.

[## 🌀 Infinite Loops, Infinite Loot: Exploiting an Overlooked API Rate Limit for Full Account Takeover

### Hey there!😁

medium.com](https://medium.com/%40iski/infinite-loops-infinite-loot-exploiting-an-overlooked-api-rate-limit-for-full-account-takeover-b14070e1cd5e?source=post_page-----ee37d4a725c2---------------------------------------)

## Act 1: The Brick Wall — Meeting My AI Adversary 🧱

--

--

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:96:96/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--ee37d4a725c2---------------------------------------)

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:128:128/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--ee37d4a725c2---------------------------------------)

Follow

[## Published in InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---post_publication_info--ee37d4a725c2---------------------------------------)

[73K followers](/followers?source=post_page---post_publication_info--ee37d4a725c2---------------------------------------)

·[Last published 19 hours ago](/everyone-wants-to-hack-no-one-wants-to-think-a6bb8a313501?source=post_page---post_publication_info--ee37d4a725c2---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow

[![Iski](https://miro.medium.com/v2/resize:fill:96:96/1*PpvkjPQ1lY6aTYHT9kDX5w.png)](https://medium.com/%40iski?source=post_page---post_author_info--ee37d4a725c2---------------------------------------)

[![Iski](https://miro.medium.com/v2/resize:fill:128:128/1*PpvkjPQ1lY6aTYHT9kDX5w.png)](https://medium.com/%40iski?source=post_page---post_author_info--ee37d4a725c2---------------------------------------)

[## Written by Iski](https://medium.com/%40iski?source=post_page---post_author_info--ee37d4a725c2---------------------------------------)

[1.92K followers](https://medium.com/%40iski/followers?source=post_page---post_author_info--ee37d4a725c2---------------------------------------)

·[7 following](https://medium.com/%40iski/following?source=post_page---post_author_info--ee37d4a725c2---------------------------------------)

Cybersecurity Researcher | Penetration Tester | Bug Bounty Hunter | Web security| Passionate about cyber security, security automation

## No responses yet

[Help](https://help.medium.com/hc/en-us?source=post_page-----ee37d4a725c2---------------------------------------)

[Status](https://status.medium.com/?source=post_page-----ee37d4a725c2---------------------------------------)

[About](https://medium.com/about?autoplay=1&source=post_page-----ee37d4a725c2---------------------------------------)

[Careers](https://medium.com/jobs-at-medium/work-at-medium-959d1a85284e?source=post_page-----ee37d4a725c2---------------------------------------)

Press

[Blog](https://blog.medium.com/?source=post_page-----ee37d4a725c2---------------------------------------)

[Privacy](https://policy.medium.com/medium-privacy-policy-f03bf92035c9?source=post_page-----ee37d4a725c2---------------------------------------)

[Rules](https://policy.medium.com/medium-rules-30e5502c4eb4?source=post_page-----ee37d4a725c2---------------------------------------)

[Terms](https://policy.medium.com/medium-terms-of-service-9db0094a1e0f?source=post_page-----ee37d4a725c2---------------------------------------)

[Text to speech](https://speechify.com/medium?source=post_page-----ee37d4a725c2---------------------------------------)