---
title: Not-So-Private Parts: How Public Buckets Spilled Internal Dashboards
url: https://infosecwriteups.com/not-so-private-parts-how-public-buckets-spilled-internal-dashboards-c3dd03df9951?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2025-07-06
fetch_date: 2025-10-06T23:27:06.348540
---

# Not-So-Private Parts: How Public Buckets Spilled Internal Dashboards

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2Fc3dd03df9951&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fnot-so-private-parts-how-public-buckets-spilled-internal-dashboards-c3dd03df9951&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fnot-so-private-parts-how-public-buckets-spilled-internal-dashboards-c3dd03df9951&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-c3dd03df9951---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-c3dd03df9951---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

Member-only story

# **Not-So-Private Parts: How Public Buckets Spilled Internal Dashboards 🪳🔓**

[![Iski](https://miro.medium.com/v2/resize:fill:64:64/1*PpvkjPQ1lY6aTYHT9kDX5w.png)](https://medium.com/%40iski?source=post_page---byline--c3dd03df9951---------------------------------------)

[Iski](https://medium.com/%40iski?source=post_page---byline--c3dd03df9951---------------------------------------)

3 min read

·

Jul 3, 2025

--

2

Share

Free [Link](https://medium.com/%40iski/not-so-private-parts-how-public-buckets-spilled-internal-dashboards-c3dd03df9951?sk=dfaca055982ff4114fddf5f79afe771a) 🎈

Hey there!😁

Press enter or click to view image in full size

![]()

Image by Copilot AI

**Life Tip #177:** When life gives you buckets, don’t assume they’re empty — check if they’re public and leaking secrets instead. 😅

It was one of *those* nights. My coffee was cold, my recon scripts were stuck, and I had just rage-quit another CTF challenge that felt like it was written by ancient aliens. Out of sheer boredom (or fate?), I decided to run a lazy recon pass using some forgotten one-liners. What I found next? A digital treasure chest wide open.

Let’s dive into how an exposed AWS S3 bucket led me into private dashboards, sensitive business docs, and a high-severity bounty that could probably pay for my entire Netflix subscription for the next 5 years.

[## ⚡️Oops, They Logged It! 🤭 Turning LFI into Remote Shell Like a Pro 💻⚔️🚫💸

### Free Link🎈

infosecwriteups.com](/%EF%B8%8Foops-they-logged-it-turning-lfi-into-remote-shell-like-a-pro-%EF%B8%8F-272e81c5315f?source=post_page-----c3dd03df9951---------------------------------------)

## 🔍 The Mass Recon That Started It All

I was running the usual suspects on a high-profile target:

```
assetfinder --subs-only target.com | httprobe | tee domains.txt
waybackurls target.com | tee urls.txt
```

--

--

2

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:96:96/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--c3dd03df9951---------------------------------------)

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:128:128/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--c3dd03df9951---------------------------------------)

Follow

[## Published in InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---post_publication_info--c3dd03df9951---------------------------------------)

[71K followers](/followers?source=post_page---post_publication_info--c3dd03df9951---------------------------------------)

·[Last published 3 hours ago](/actuator-unleashed-a-guide-to-finding-and-exploiting-spring-boot-actuator-endpoints-29252dcd9d79?source=post_page---post_publication_info--c3dd03df9951---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow

[![Iski](https://miro.medium.com/v2/resize:fill:96:96/1*PpvkjPQ1lY6aTYHT9kDX5w.png)](https://medium.com/%40iski?source=post_page---post_author_info--c3dd03df9951---------------------------------------)

[![Iski](https://miro.medium.com/v2/resize:fill:128:128/1*PpvkjPQ1lY6aTYHT9kDX5w.png)](https://medium.com/%40iski?source=post_page---post_author_info--c3dd03df9951---------------------------------------)

[## Written by Iski](https://medium.com/%40iski?source=post_page---post_author_info--c3dd03df9951---------------------------------------)

[1.8K followers](https://medium.com/%40iski/followers?source=post_page---post_author_info--c3dd03df9951---------------------------------------)

·[7 following](https://medium.com/%40iski/following?source=post_page---post_author_info--c3dd03df9951---------------------------------------)

Cybersecurity Researcher | Penetration Tester | Bug Bounty Hunter | Web security| Passionate about cyber security, security automation

## Responses (2)

See all responses

[Help](https://help.medium.com/hc/en-us?source=post_page-----c3dd03df9951---------------------------------------)

[Status](https://status.medium.com/?source=post_page-----c3dd03df9951---------------------------------------)

[About](https://medium.com/about?autoplay=1&source=post_page-----c3dd03df9951---------------------------------------)

[Careers](https://medium.com/jobs-at-medium/work-at-medium-959d1a85284e?source=post_page-----c3dd03df9951---------------------------------------)

Press

[Blog](https://blog.medium.com/?source=post_page-----c3dd03df9951---------------------------------------)

[Privacy](https://policy.medium.com/medium-privacy-policy-f03bf92035c9?source=post_page-----c3dd03df9951---------------------------------------)

[Rules](https://policy.medium.com/medium-rules-30e5502c4eb4?source=post_page-----c3dd03df9951---------------------------------------)

[Terms](https://policy.medium.com/medium-terms-of-service-9db0094a1e0f?source=post_page-----c3dd03df9951---------------------------------------)

[Text to speech](https://speechify.com/medium?source=post_page-----c3dd03df9951---------------------------------------)