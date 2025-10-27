---
title: Token Tales: Finding Hidden API Keys in JavaScript and Turning Them Into Gold
url: https://infosecwriteups.com/token-tales-finding-hidden-api-keys-in-javascript-and-turning-them-into-gold-e4e93c51e52b?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2025-09-01
fetch_date: 2025-10-02T19:28:53.592540
---

# Token Tales: Finding Hidden API Keys in JavaScript and Turning Them Into Gold

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2Fe4e93c51e52b&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Ftoken-tales-finding-hidden-api-keys-in-javascript-and-turning-them-into-gold-e4e93c51e52b&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Ftoken-tales-finding-hidden-api-keys-in-javascript-and-turning-them-into-gold-e4e93c51e52b&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-e4e93c51e52b---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-e4e93c51e52b---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

Member-only story

# Token Tales: Finding Hidden API Keys in JavaScript and Turning Them Into Gold

[![Iski](https://miro.medium.com/v2/resize:fill:64:64/1*PpvkjPQ1lY6aTYHT9kDX5w.png)](https://medium.com/%40iski?source=post_page---byline--e4e93c51e52b---------------------------------------)

[Iski](https://medium.com/%40iski?source=post_page---byline--e4e93c51e52b---------------------------------------)

4 min read

·

Aug 29, 2025

--

1

Share

Free [link](https://medium.com/%40iski/token-tales-finding-hidden-api-keys-in-javascript-and-turning-them-into-gold-e4e93c51e52b?sk=3e1a5159548004b5b21ebf7d90ad8d25) 🎈

Hey there!😁

Press enter or click to view image in full size

![]()

Image by AI

Ever feel like your morning coffee is just a bitter prelude to the real thrill — finding exposed API keys in JavaScript? No? Just me? Alright then. But that questionable caffeine kick did help me sniff out a hidden treasure: a forgotten React build with hardcoded secrets that unlocked a high-severity jackpot. Let me walk you through my adventure.

[## When Amazon Gave Me Free Storage (But I Gave It Back)

### Free link🎈

medium.com](https://medium.com/%40iski/when-amazon-gave-me-free-storage-but-i-gave-it-back-9734c058cd05?source=post_page-----e4e93c51e52b---------------------------------------)

## 1. The Recon Ritual: Scanning JavaScript for Gold

I kicked things off with a standard recon setup:

```
subfinder -d target.com -silent > subs.txt
httpx -l subs.txt -silent -o live.txt
gau -subs target.com | grep ".js" | tee js_files.txt
```

Then I manually downloaded suspicious scripts and grepped for keywords like `api_key`, `token`, `secret`, etc.

That’s when I saw it: a minified JS file with a visible `const API_KEY = "sk_live_abc123secret";` embedded in client-side code. My heartbeat went *thump-thump*. As others…

--

--

1

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:96:96/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--e4e93c51e52b---------------------------------------)

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:128:128/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--e4e93c51e52b---------------------------------------)

Follow

[## Published in InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---post_publication_info--e4e93c51e52b---------------------------------------)

[71K followers](/followers?source=post_page---post_publication_info--e4e93c51e52b---------------------------------------)

·[Last published 4 days ago](/how-to-find-p1-bugs-using-google-in-your-target-part-1-e37455324dc1?source=post_page---post_publication_info--e4e93c51e52b---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow

[![Iski](https://miro.medium.com/v2/resize:fill:96:96/1*PpvkjPQ1lY6aTYHT9kDX5w.png)](https://medium.com/%40iski?source=post_page---post_author_info--e4e93c51e52b---------------------------------------)

[![Iski](https://miro.medium.com/v2/resize:fill:128:128/1*PpvkjPQ1lY6aTYHT9kDX5w.png)](https://medium.com/%40iski?source=post_page---post_author_info--e4e93c51e52b---------------------------------------)

[## Written by Iski](https://medium.com/%40iski?source=post_page---post_author_info--e4e93c51e52b---------------------------------------)

[1.8K followers](https://medium.com/%40iski/followers?source=post_page---post_author_info--e4e93c51e52b---------------------------------------)

·[7 following](https://medium.com/%40iski/following?source=post_page---post_author_info--e4e93c51e52b---------------------------------------)

Cybersecurity Researcher | Penetration Tester | Bug Bounty Hunter | Web security| Passionate about cyber security, security automation

## Responses (1)

See all responses

[Help](https://help.medium.com/hc/en-us?source=post_page-----e4e93c51e52b---------------------------------------)

[Status](https://status.medium.com/?source=post_page-----e4e93c51e52b---------------------------------------)

[About](https://medium.com/about?autoplay=1&source=post_page-----e4e93c51e52b---------------------------------------)

[Careers](https://medium.com/jobs-at-medium/work-at-medium-959d1a85284e?source=post_page-----e4e93c51e52b---------------------------------------)

Press

[Blog](https://blog.medium.com/?source=post_page-----e4e93c51e52b---------------------------------------)

[Privacy](https://policy.medium.com/medium-privacy-policy-f03bf92035c9?source=post_page-----e4e93c51e52b---------------------------------------)

[Rules](https://policy.medium.com/medium-rules-30e5502c4eb4?source=post_page-----e4e93c51e52b---------------------------------------)

[Terms](https://policy.medium.com/medium-terms-of-service-9db0094a1e0f?source=post_page-----e4e93c51e52b---------------------------------------)

[Text to speech](https://speechify.com/medium?source=post_page-----e4e93c51e52b---------------------------------------)