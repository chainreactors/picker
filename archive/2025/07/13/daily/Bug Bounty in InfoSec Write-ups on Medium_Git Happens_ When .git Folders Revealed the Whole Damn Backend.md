---
title: Git Happens: When .git Folders Revealed the Whole Damn Backend
url: https://infosecwriteups.com/git-happens-when-git-folders-revealed-the-whole-damn-backend-b181b77c4c76?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2025-07-13
fetch_date: 2025-10-06T23:27:16.207457
---

# Git Happens: When .git Folders Revealed the Whole Damn Backend

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2Fb181b77c4c76&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fgit-happens-when-git-folders-revealed-the-whole-damn-backend-b181b77c4c76&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fgit-happens-when-git-folders-revealed-the-whole-damn-backend-b181b77c4c76&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-b181b77c4c76---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-b181b77c4c76---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

Member-only story

# Git Happens: When .git Folders Revealed the Whole Damn Backend 🧠📂

[![Iski](https://miro.medium.com/v2/resize:fill:64:64/1*PpvkjPQ1lY6aTYHT9kDX5w.png)](https://medium.com/%40iski?source=post_page---byline--b181b77c4c76---------------------------------------)

[Iski](https://medium.com/%40iski?source=post_page---byline--b181b77c4c76---------------------------------------)

3 min read

·

Jul 11, 2025

--

2

Share

Free [Link](https://medium.com/%40iski/git-happens-when-git-folders-revealed-the-whole-damn-backend-b181b77c4c76?sk=2166674232e94e88d8833c6fe95f5d5f) 🎈

Hey there!😁

Press enter or click to view image in full size

![]()

Image by Gemini AI

## 🥱 Life Lesson: Never underestimate a “hidden” folder

You know that moment when you’re binge-eating Maggi at 3 AM, half asleep, and decide *“just one last recon scan”*? Yeah. That one “last scan” turned into *the* recon run of my life — and my bounty wallet agreed 💰💥.

While people were flexing Burp Collaborator payloads and exotic CVEs, I was out here snooping `.git/` like it owed me rent. And guess what? It did. Rent, source code, admin credentials, the *whole* backend — gift-wrapped and labeled “pls exploit me.”

[## Rate Limit? I Barely Know Her: How I Brute-Forced OTPs Like a Gentleman 🚦🚨

### Free Link 🎈

infosecwriteups.com](/rate-limit-i-barely-know-her-how-i-brute-forced-otps-like-a-gentleman-6f1235c559cc?source=post_page-----b181b77c4c76---------------------------------------)

## ☠️ Recon Phase: Git it Started

## 🔍 Tools used:

* `gau + waybackurls + gf`
* `dirsearch`
* `git-dumper`
* `wget + gittools`
* `httpx` + `nuclei` custom template

--

--

2

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:96:96/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--b181b77c4c76---------------------------------------)

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:128:128/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--b181b77c4c76---------------------------------------)

Follow

[## Published in InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---post_publication_info--b181b77c4c76---------------------------------------)

[71K followers](/followers?source=post_page---post_publication_info--b181b77c4c76---------------------------------------)

·[Last published 3 hours ago](/actuator-unleashed-a-guide-to-finding-and-exploiting-spring-boot-actuator-endpoints-29252dcd9d79?source=post_page---post_publication_info--b181b77c4c76---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow

[![Iski](https://miro.medium.com/v2/resize:fill:96:96/1*PpvkjPQ1lY6aTYHT9kDX5w.png)](https://medium.com/%40iski?source=post_page---post_author_info--b181b77c4c76---------------------------------------)

[![Iski](https://miro.medium.com/v2/resize:fill:128:128/1*PpvkjPQ1lY6aTYHT9kDX5w.png)](https://medium.com/%40iski?source=post_page---post_author_info--b181b77c4c76---------------------------------------)

[## Written by Iski](https://medium.com/%40iski?source=post_page---post_author_info--b181b77c4c76---------------------------------------)

[1.8K followers](https://medium.com/%40iski/followers?source=post_page---post_author_info--b181b77c4c76---------------------------------------)

·[7 following](https://medium.com/%40iski/following?source=post_page---post_author_info--b181b77c4c76---------------------------------------)

Cybersecurity Researcher | Penetration Tester | Bug Bounty Hunter | Web security| Passionate about cyber security, security automation

## Responses (2)

See all responses

[Help](https://help.medium.com/hc/en-us?source=post_page-----b181b77c4c76---------------------------------------)

[Status](https://status.medium.com/?source=post_page-----b181b77c4c76---------------------------------------)

[About](https://medium.com/about?autoplay=1&source=post_page-----b181b77c4c76---------------------------------------)

[Careers](https://medium.com/jobs-at-medium/work-at-medium-959d1a85284e?source=post_page-----b181b77c4c76---------------------------------------)

Press

[Blog](https://blog.medium.com/?source=post_page-----b181b77c4c76---------------------------------------)

[Privacy](https://policy.medium.com/medium-privacy-policy-f03bf92035c9?source=post_page-----b181b77c4c76---------------------------------------)

[Rules](https://policy.medium.com/medium-rules-30e5502c4eb4?source=post_page-----b181b77c4c76---------------------------------------)

[Terms](https://policy.medium.com/medium-terms-of-service-9db0094a1e0f?source=post_page-----b181b77c4c76---------------------------------------)

[Text to speech](https://speechify.com/medium?source=post_page-----b181b77c4c76---------------------------------------)