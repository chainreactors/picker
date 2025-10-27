---
title: Signed, Sealed, Delivered: How I Replayed Signed URLs to Steal Everything ✍️
url: https://infosecwriteups.com/signed-sealed-delivered-how-i-replayed-signed-urls-to-steal-everything-%EF%B8%8F-df28cbe93b34?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2025-06-20
fetch_date: 2025-10-06T22:52:00.926053
---

# Signed, Sealed, Delivered: How I Replayed Signed URLs to Steal Everything ✍️

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2Fdf28cbe93b34&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fsigned-sealed-delivered-how-i-replayed-signed-urls-to-steal-everything-%25EF%25B8%258F-df28cbe93b34&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fsigned-sealed-delivered-how-i-replayed-signed-urls-to-steal-everything-%25EF%25B8%258F-df28cbe93b34&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-df28cbe93b34---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-df28cbe93b34---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

Member-only story

# 📦 Signed, Sealed, Delivered: How I Replayed Signed URLs to Steal Everything ✍️💣

[![Iski](https://miro.medium.com/v2/resize:fill:64:64/1*PpvkjPQ1lY6aTYHT9kDX5w.png)](https://medium.com/%40iski?source=post_page---byline--df28cbe93b34---------------------------------------)

[Iski](https://medium.com/%40iski?source=post_page---byline--df28cbe93b34---------------------------------------)

4 min read

·

Jun 18, 2025

--

Share

Free [Link](https://medium.com/%40iski/signed-sealed-delivered-how-i-replayed-signed-urls-to-steal-everything-%EF%B8%8F-df28cbe93b34?sk=735c4879687b6ee950e64a96c8eb6a7e) 🎈

Hey there!😁

Press enter or click to view image in full size

![]()

Image by Gemini AI

You know it’s a rough week when:

* Your food delivery app delivers to your neighbor again.
* You miss your bus by 2 seconds.
* And to top it off, your crush leaves you on “seen”.

So what did I do? Poured a cup of iced black coffee, opened my Burp Suite, and let my loneliness guide me to the land of recon. 🤓☕

And guess what? The cloud may have forgotten me, but it sure didn’t forget to expose secrets…

[## ⚔️ Unsafe Eval = Unlimited Control: How a JS Sink Let Me Run Anything 💻💥

### Hey there!😁

infosecwriteups.com](/%EF%B8%8F-unsafe-eval-unlimited-control-how-a-js-sink-let-me-run-anything-60794929a295?source=post_page-----df28cbe93b34---------------------------------------)

## 🌩️ Step 1: Recon — The Cloud Has No Privacy

It all started with my recon routine — the digital equivalent of checking everyone’s trash for treasure:

```
subfinder -d target.com -o subs.txt
httpx -l subs.txt -status-code -tech-detect -title -o live.txt
gau --subs target.com > gau.txt
katana -list live.txt -js-crawl -o js_endpoints.txt
```

--

--

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:96:96/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--df28cbe93b34---------------------------------------)

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:128:128/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--df28cbe93b34---------------------------------------)

Follow

[## Published in InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---post_publication_info--df28cbe93b34---------------------------------------)

[71K followers](/followers?source=post_page---post_publication_info--df28cbe93b34---------------------------------------)

·[Last published 2 hours ago](/actuator-unleashed-a-guide-to-finding-and-exploiting-spring-boot-actuator-endpoints-29252dcd9d79?source=post_page---post_publication_info--df28cbe93b34---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow

[![Iski](https://miro.medium.com/v2/resize:fill:96:96/1*PpvkjPQ1lY6aTYHT9kDX5w.png)](https://medium.com/%40iski?source=post_page---post_author_info--df28cbe93b34---------------------------------------)

[![Iski](https://miro.medium.com/v2/resize:fill:128:128/1*PpvkjPQ1lY6aTYHT9kDX5w.png)](https://medium.com/%40iski?source=post_page---post_author_info--df28cbe93b34---------------------------------------)

[## Written by Iski](https://medium.com/%40iski?source=post_page---post_author_info--df28cbe93b34---------------------------------------)

[1.8K followers](https://medium.com/%40iski/followers?source=post_page---post_author_info--df28cbe93b34---------------------------------------)

·[7 following](https://medium.com/%40iski/following?source=post_page---post_author_info--df28cbe93b34---------------------------------------)

Cybersecurity Researcher | Penetration Tester | Bug Bounty Hunter | Web security| Passionate about cyber security, security automation

## No responses yet

[Help](https://help.medium.com/hc/en-us?source=post_page-----df28cbe93b34---------------------------------------)

[Status](https://status.medium.com/?source=post_page-----df28cbe93b34---------------------------------------)

[About](https://medium.com/about?autoplay=1&source=post_page-----df28cbe93b34---------------------------------------)

[Careers](https://medium.com/jobs-at-medium/work-at-medium-959d1a85284e?source=post_page-----df28cbe93b34---------------------------------------)

Press

[Blog](https://blog.medium.com/?source=post_page-----df28cbe93b34---------------------------------------)

[Privacy](https://policy.medium.com/medium-privacy-policy-f03bf92035c9?source=post_page-----df28cbe93b34---------------------------------------)

[Rules](https://policy.medium.com/medium-rules-30e5502c4eb4?source=post_page-----df28cbe93b34---------------------------------------)

[Terms](https://policy.medium.com/medium-terms-of-service-9db0094a1e0f?source=post_page-----df28cbe93b34---------------------------------------)

[Text to speech](https://speechify.com/medium?source=post_page-----df28cbe93b34---------------------------------------)