---
title: From Recon to RCE: How AI and a cup of Boost Helped Me Turn SQLi into a Command Injection Jackpot…
url: https://infosecwriteups.com/from-recon-to-rce-how-ai-and-a-cup-of-boost-helped-me-turn-sqli-into-a-command-injection-jackpot-1f62dc829956?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2025-04-10
fetch_date: 2025-10-06T22:04:37.711162
---

# From Recon to RCE: How AI and a cup of Boost Helped Me Turn SQLi into a Command Injection Jackpot…

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2F1f62dc829956&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Ffrom-recon-to-rce-how-ai-and-a-cup-of-boost-helped-me-turn-sqli-into-a-command-injection-jackpot-1f62dc829956&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Ffrom-recon-to-rce-how-ai-and-a-cup-of-boost-helped-me-turn-sqli-into-a-command-injection-jackpot-1f62dc829956&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-1f62dc829956---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-1f62dc829956---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

Member-only story

# From Recon to RCE: How AI and a cup of Boost Helped Me Turn SQLi into a Command Injection Jackpot 💵💰🚀

[![Iski](https://miro.medium.com/v2/resize:fill:64:64/1*PpvkjPQ1lY6aTYHT9kDX5w.png)](https://medium.com/%40iski?source=post_page---byline--1f62dc829956---------------------------------------)

[Iski](https://medium.com/%40iski?source=post_page---byline--1f62dc829956---------------------------------------)

4 min read

·

Apr 8, 2025

--

5

Share

Free [Link](https://medium.com/%40iski/from-recon-to-rce-how-ai-and-a-cup-of-boost-helped-me-turn-sqli-into-a-command-injection-jackpot-1f62dc829956?sk=1a0ad79134f06c2ed851d65ff4e65f2e)🎈

Hey there!🙌

Press enter or click to view image in full size

![]()

image by copilot

It was just another lazy day. **I was battling depression, dodging family WhatsApp groups asking when I’d get married, and wondering if my life had any plot other than debugging my own existence. 😩**

I told myself, ‘Just 5 minutes of bug hunting to distract myself.’ Five hours later, my terminal looked like it had found the meaning of life — or at least a vulnerable endpoint that would soon make mine better. 😅

Little did I know, this recon session was about to turn my loneliness into a critical RCE report.

Yes. With a little help from AI. And a lot of caffeine says (**BOOST IS THE SECRET OF MY ENERGY).**

[## How Recon → SQLi Made €€€€ Bounty

### Hi there…!

infosecwriteups.com](/how-recon-sqli-made-bounty-425fc0fa2e92?source=post_page-----1f62dc829956---------------------------------------)

## Phase 1: Recon Like a Beast 🦖

Here’s how it all started. My recon stack:

```
assetfinder target.com -subs-only | tee -a asset.txt
crtsh -d target.com | tee -a crtsh.txt
findomain -t target.com -o…
```

--

--

5

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:96:96/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--1f62dc829956---------------------------------------)

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:128:128/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--1f62dc829956---------------------------------------)

Follow

[## Published in InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---post_publication_info--1f62dc829956---------------------------------------)

[71K followers](/followers?source=post_page---post_publication_info--1f62dc829956---------------------------------------)

·[Last published 1 hour ago](/actuator-unleashed-a-guide-to-finding-and-exploiting-spring-boot-actuator-endpoints-29252dcd9d79?source=post_page---post_publication_info--1f62dc829956---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow

[![Iski](https://miro.medium.com/v2/resize:fill:96:96/1*PpvkjPQ1lY6aTYHT9kDX5w.png)](https://medium.com/%40iski?source=post_page---post_author_info--1f62dc829956---------------------------------------)

[![Iski](https://miro.medium.com/v2/resize:fill:128:128/1*PpvkjPQ1lY6aTYHT9kDX5w.png)](https://medium.com/%40iski?source=post_page---post_author_info--1f62dc829956---------------------------------------)

[## Written by Iski](https://medium.com/%40iski?source=post_page---post_author_info--1f62dc829956---------------------------------------)

[1.8K followers](https://medium.com/%40iski/followers?source=post_page---post_author_info--1f62dc829956---------------------------------------)

·[7 following](https://medium.com/%40iski/following?source=post_page---post_author_info--1f62dc829956---------------------------------------)

Cybersecurity Researcher | Penetration Tester | Bug Bounty Hunter | Web security| Passionate about cyber security, security automation

## Responses (5)

See all responses

[Help](https://help.medium.com/hc/en-us?source=post_page-----1f62dc829956---------------------------------------)

[Status](https://status.medium.com/?source=post_page-----1f62dc829956---------------------------------------)

[About](https://medium.com/about?autoplay=1&source=post_page-----1f62dc829956---------------------------------------)

[Careers](https://medium.com/jobs-at-medium/work-at-medium-959d1a85284e?source=post_page-----1f62dc829956---------------------------------------)

Press

[Blog](https://blog.medium.com/?source=post_page-----1f62dc829956---------------------------------------)

[Privacy](https://policy.medium.com/medium-privacy-policy-f03bf92035c9?source=post_page-----1f62dc829956---------------------------------------)

[Rules](https://policy.medium.com/medium-rules-30e5502c4eb4?source=post_page-----1f62dc829956---------------------------------------)

[Terms](https://policy.medium.com/medium-terms-of-service-9db0094a1e0f?source=post_page-----1f62dc829956---------------------------------------)

[Text to speech](https://speechify.com/medium?source=post_page-----1f62dc829956---------------------------------------)