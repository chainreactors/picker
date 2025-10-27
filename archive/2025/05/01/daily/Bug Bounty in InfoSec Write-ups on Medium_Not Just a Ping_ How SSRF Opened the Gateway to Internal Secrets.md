---
title: Not Just a Ping: How SSRF Opened the Gateway to Internal Secrets
url: https://infosecwriteups.com/not-just-a-ping-how-ssrf-opened-the-gateway-to-internal-secrets-d18eeccd4745?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2025-05-01
fetch_date: 2025-10-06T22:25:15.258687
---

# Not Just a Ping: How SSRF Opened the Gateway to Internal Secrets

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2Fd18eeccd4745&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fnot-just-a-ping-how-ssrf-opened-the-gateway-to-internal-secrets-d18eeccd4745&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fnot-just-a-ping-how-ssrf-opened-the-gateway-to-internal-secrets-d18eeccd4745&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-d18eeccd4745---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-d18eeccd4745---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

Member-only story

# 🚰 Not Just a Ping: How SSRF Opened the Gateway to Internal Secrets 🔓🧠

[![Iski](https://miro.medium.com/v2/resize:fill:64:64/1*PpvkjPQ1lY6aTYHT9kDX5w.png)](https://medium.com/%40iski?source=post_page---byline--d18eeccd4745---------------------------------------)

[Iski](https://medium.com/%40iski?source=post_page---byline--d18eeccd4745---------------------------------------)

4 min read

·

Apr 29, 2025

--

4

Share

Free [Link](https://medium.com/%40iski/not-just-a-ping-how-ssrf-opened-the-gateway-to-internal-secrets-d18eeccd4745?sk=237909756b1a90b0397fb7d1c7f9d4e6)🎈

Hey there!😁

Press enter or click to view image in full size

![]()

Image by Copilot

You know that feeling when you poke something *just a little*, and the whole thing falls apart like a Jenga tower?
 That’s what this SSRF bug felt like. One small ping… **BOOM — internal secrets, cloud keys, and money raining down.** 💸😂

If curiosity killed the cat, **thank god I’m a hacker, not a cat.** 🐱‍💻

Grab your coffee ☕ — here’s the full story of how I *accidentally* became an internal server’s best friend. 🧑‍🤝‍🧑

## 🔍 Phase 1: Recon Recon Recon — The Dating App for Bug Hunters ❤️

I was doing what all serious bounty hunters do:
**Mass recon** while binge-watching Netflix in the background. 🎬

Here’s how I started:

[## From Recon to RCE: How AI and a cup of Boost Helped Me Turn SQLi into a Command Injection Jackpot…

### Free Link🎈

infosecwriteups.com](/from-recon-to-rce-how-ai-and-a-cup-of-boost-helped-me-turn-sqli-into-a-command-injection-jackpot-1f62dc829956?source=post_page-----d18eeccd4745---------------------------------------)

```
subfinder -d target.com -silent > subs.txt
httpx -l subs.txt -mc 200,302 -title -tech-detect -vhost > live.txt
nuclei -l live.txt -t ssrf -severity high,critical
```

--

--

4

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:96:96/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--d18eeccd4745---------------------------------------)

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:128:128/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--d18eeccd4745---------------------------------------)

Follow

[## Published in InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---post_publication_info--d18eeccd4745---------------------------------------)

[71K followers](/followers?source=post_page---post_publication_info--d18eeccd4745---------------------------------------)

·[Last published 2 hours ago](/actuator-unleashed-a-guide-to-finding-and-exploiting-spring-boot-actuator-endpoints-29252dcd9d79?source=post_page---post_publication_info--d18eeccd4745---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow

[![Iski](https://miro.medium.com/v2/resize:fill:96:96/1*PpvkjPQ1lY6aTYHT9kDX5w.png)](https://medium.com/%40iski?source=post_page---post_author_info--d18eeccd4745---------------------------------------)

[![Iski](https://miro.medium.com/v2/resize:fill:128:128/1*PpvkjPQ1lY6aTYHT9kDX5w.png)](https://medium.com/%40iski?source=post_page---post_author_info--d18eeccd4745---------------------------------------)

[## Written by Iski](https://medium.com/%40iski?source=post_page---post_author_info--d18eeccd4745---------------------------------------)

[1.8K followers](https://medium.com/%40iski/followers?source=post_page---post_author_info--d18eeccd4745---------------------------------------)

·[7 following](https://medium.com/%40iski/following?source=post_page---post_author_info--d18eeccd4745---------------------------------------)

Cybersecurity Researcher | Penetration Tester | Bug Bounty Hunter | Web security| Passionate about cyber security, security automation

## Responses (4)

See all responses

[Help](https://help.medium.com/hc/en-us?source=post_page-----d18eeccd4745---------------------------------------)

[Status](https://status.medium.com/?source=post_page-----d18eeccd4745---------------------------------------)

[About](https://medium.com/about?autoplay=1&source=post_page-----d18eeccd4745---------------------------------------)

[Careers](https://medium.com/jobs-at-medium/work-at-medium-959d1a85284e?source=post_page-----d18eeccd4745---------------------------------------)

Press

[Blog](https://blog.medium.com/?source=post_page-----d18eeccd4745---------------------------------------)

[Privacy](https://policy.medium.com/medium-privacy-policy-f03bf92035c9?source=post_page-----d18eeccd4745---------------------------------------)

[Rules](https://policy.medium.com/medium-rules-30e5502c4eb4?source=post_page-----d18eeccd4745---------------------------------------)

[Terms](https://policy.medium.com/medium-terms-of-service-9db0094a1e0f?source=post_page-----d18eeccd4745---------------------------------------)

[Text to speech](https://speechify.com/medium?source=post_page-----d18eeccd4745---------------------------------------)