---
title: Secrets in Session: How a Forgotten Cookie Let Me Walk Into Admin Panel Like I Owned the Place…
url: https://infosecwriteups.com/secrets-in-session-how-a-forgotten-cookie-let-me-walk-into-admin-panel-like-i-owned-the-place-6aeb97f7f9de?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2025-07-22
fetch_date: 2025-10-06T23:27:05.955739
---

# Secrets in Session: How a Forgotten Cookie Let Me Walk Into Admin Panel Like I Owned the Place…

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2F6aeb97f7f9de&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fsecrets-in-session-how-a-forgotten-cookie-let-me-walk-into-admin-panel-like-i-owned-the-place-6aeb97f7f9de&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fsecrets-in-session-how-a-forgotten-cookie-let-me-walk-into-admin-panel-like-i-owned-the-place-6aeb97f7f9de&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-6aeb97f7f9de---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-6aeb97f7f9de---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

Member-only story

# 🍪 Secrets in Session: How a Forgotten Cookie Let Me Walk Into Admin Panel Like I Owned the Place 🔑

[![Iski](https://miro.medium.com/v2/resize:fill:64:64/1*PpvkjPQ1lY6aTYHT9kDX5w.png)](https://medium.com/%40iski?source=post_page---byline--6aeb97f7f9de---------------------------------------)

[Iski](https://medium.com/%40iski?source=post_page---byline--6aeb97f7f9de---------------------------------------)

3 min read

·

Jul 20, 2025

--

1

Share

Free [Link](https://medium.com/%40iski/secrets-in-session-how-a-forgotten-cookie-let-me-walk-into-admin-panel-like-i-owned-the-place-6aeb97f7f9de?sk=a1c9941cf495c2770da320958ab4feae) 🎈

**Hey there!😁**

Press enter or click to view image in full size

![]()

Image by GEmini AI

> *Life Tip #235: If logging out of your ex’s life was as easy as logging out of some web apps… we’d all be healed by now. 💔🍪*

I was on my third cup of coffee (read: coping mechanism ☕) at 2:47 AM, half-watching a 2008 CTF talk and half-scrolling through recon output from a random fintech target. Just as I was about to give up for the night, I noticed something weird. A logout endpoint that was… lying to me. And when a logout button lies, you better believe there’s treasure hidden behind it.

This is the tale of how I stumbled upon a forgotten cookie that was still holding onto the past — and how that cookie gave me full admin access.

[## Who Needs Admin When You Have GraphQL? Abusing Queries for Fun and Data 🌝📊

### Hey there!😁

infosecwriteups.com](/who-needs-admin-when-you-have-graphql-abusing-queries-for-fun-and-data-03456b01da34?source=post_page-----6aeb97f7f9de---------------------------------------)

## 🔍 Recon Rituals & Cookie Crumbs

I began with basic mass recon — nothing fancy:

```
subfinder -d target.com | tee subs.txt
httpx -l subs.txt -status-code -title -tech-detect > alive.txt
gau…
```

--

--

1

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:96:96/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--6aeb97f7f9de---------------------------------------)

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:128:128/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--6aeb97f7f9de---------------------------------------)

Follow

[## Published in InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---post_publication_info--6aeb97f7f9de---------------------------------------)

[71K followers](/followers?source=post_page---post_publication_info--6aeb97f7f9de---------------------------------------)

·[Last published 3 hours ago](/actuator-unleashed-a-guide-to-finding-and-exploiting-spring-boot-actuator-endpoints-29252dcd9d79?source=post_page---post_publication_info--6aeb97f7f9de---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow

[![Iski](https://miro.medium.com/v2/resize:fill:96:96/1*PpvkjPQ1lY6aTYHT9kDX5w.png)](https://medium.com/%40iski?source=post_page---post_author_info--6aeb97f7f9de---------------------------------------)

[![Iski](https://miro.medium.com/v2/resize:fill:128:128/1*PpvkjPQ1lY6aTYHT9kDX5w.png)](https://medium.com/%40iski?source=post_page---post_author_info--6aeb97f7f9de---------------------------------------)

[## Written by Iski](https://medium.com/%40iski?source=post_page---post_author_info--6aeb97f7f9de---------------------------------------)

[1.8K followers](https://medium.com/%40iski/followers?source=post_page---post_author_info--6aeb97f7f9de---------------------------------------)

·[7 following](https://medium.com/%40iski/following?source=post_page---post_author_info--6aeb97f7f9de---------------------------------------)

Cybersecurity Researcher | Penetration Tester | Bug Bounty Hunter | Web security| Passionate about cyber security, security automation

## Responses (1)

See all responses

[Help](https://help.medium.com/hc/en-us?source=post_page-----6aeb97f7f9de---------------------------------------)

[Status](https://status.medium.com/?source=post_page-----6aeb97f7f9de---------------------------------------)

[About](https://medium.com/about?autoplay=1&source=post_page-----6aeb97f7f9de---------------------------------------)

[Careers](https://medium.com/jobs-at-medium/work-at-medium-959d1a85284e?source=post_page-----6aeb97f7f9de---------------------------------------)

Press

[Blog](https://blog.medium.com/?source=post_page-----6aeb97f7f9de---------------------------------------)

[Privacy](https://policy.medium.com/medium-privacy-policy-f03bf92035c9?source=post_page-----6aeb97f7f9de---------------------------------------)

[Rules](https://policy.medium.com/medium-rules-30e5502c4eb4?source=post_page-----6aeb97f7f9de---------------------------------------)

[Terms](https://policy.medium.com/medium-terms-of-service-9db0094a1e0f?source=post_page-----6aeb97f7f9de---------------------------------------)

[Text to speech](https://speechify.com/medium?source=post_page-----6aeb97f7f9de---------------------------------------)