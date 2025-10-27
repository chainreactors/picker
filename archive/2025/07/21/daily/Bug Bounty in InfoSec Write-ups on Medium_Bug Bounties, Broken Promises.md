---
title: Bug Bounties, Broken Promises
url: https://infosecwriteups.com/bug-bounties-broken-promises-a19557db0aaa?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2025-07-21
fetch_date: 2025-10-06T23:21:48.457414
---

# Bug Bounties, Broken Promises

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2Fa19557db0aaa&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fbug-bounties-broken-promises-a19557db0aaa&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fbug-bounties-broken-promises-a19557db0aaa&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[Mastodon](https://me.dm/%40sync_with_ivan)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-a19557db0aaa---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-a19557db0aaa---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

Member-only story

# Bug Bounties, Broken Promises

[![Andrei Ivan](https://miro.medium.com/v2/resize:fill:64:64/1*ajsLg708YNtjFmUSN4yL2g.png)](https://medium.com/%40sync-with-ivan?source=post_page---byline--a19557db0aaa---------------------------------------)

[Andrei Ivan](https://medium.com/%40sync-with-ivan?source=post_page---byline--a19557db0aaa---------------------------------------)

4 min read

·

Jul 16, 2025

--

Share

Press enter or click to view image in full size

![Bug Bounties, Broken Promises]()

Bug Bounties, Broken Promises — Real stories of “won’t-fix” tags, scope tricks, and silent patches

## Real stories of “won’t-fix” tags, scope tricks, and silent patches — plus a survival guide for new hunters

Bug bounty platforms sell a simple dream: hackers earn money, companies get safer software, and everyone wins. But dig into public disclosure threads, Reddit rants, and private Discords and you’ll find a darker subplot. Some organizations game their own programs. Dodging payouts with “won’t fix” labels, razor-thin scopes, or last-minute severity downgrades while quietly pushing patches.

Below you’ll find three common tactics, three representative case studies, and a condensed playbook that helps new hunters stay paid (and sane) in a sometimes-rigged arena.

## The Anatomy of Abuse

### ***1. “Valid but Won’t Fix”***

> **How It Works:** Company admits the bug is real but claims the risk is acceptable, so no bounty.
>
> **Why It Hurts Hunters:** Hours of research go unrewarded; no public credit.

### 2. Scope as a Shield

> **How It Works:** Programs exclude high-risk assets or domains; any bug there is auto-rejected.
>
> **Why It Hurts Hunters:** Real-world attack chains become “out of scope” fiction.

--

--

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:96:96/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--a19557db0aaa---------------------------------------)

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:128:128/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--a19557db0aaa---------------------------------------)

Follow

[## Published in InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---post_publication_info--a19557db0aaa---------------------------------------)

[71K followers](/followers?source=post_page---post_publication_info--a19557db0aaa---------------------------------------)

·[Last published 2 hours ago](/actuator-unleashed-a-guide-to-finding-and-exploiting-spring-boot-actuator-endpoints-29252dcd9d79?source=post_page---post_publication_info--a19557db0aaa---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow

[![Andrei Ivan](https://miro.medium.com/v2/resize:fill:96:96/1*ajsLg708YNtjFmUSN4yL2g.png)](https://medium.com/%40sync-with-ivan?source=post_page---post_author_info--a19557db0aaa---------------------------------------)

[![Andrei Ivan](https://miro.medium.com/v2/resize:fill:128:128/1*ajsLg708YNtjFmUSN4yL2g.png)](https://medium.com/%40sync-with-ivan?source=post_page---post_author_info--a19557db0aaa---------------------------------------)

[## Written by Andrei Ivan](https://medium.com/%40sync-with-ivan?source=post_page---post_author_info--a19557db0aaa---------------------------------------)

[101 followers](https://medium.com/%40sync-with-ivan/followers?source=post_page---post_author_info--a19557db0aaa---------------------------------------)

·[41 following](https://medium.com/%40sync-with-ivan/following?source=post_page---post_author_info--a19557db0aaa---------------------------------------)

I write hands-on guides, scripts, and deep-dives into automation, security, and the tools shaping tomorrow’s web. Passionate about making tech practical.

## No responses yet

[Help](https://help.medium.com/hc/en-us?source=post_page-----a19557db0aaa---------------------------------------)

[Status](https://status.medium.com/?source=post_page-----a19557db0aaa---------------------------------------)

[About](https://medium.com/about?autoplay=1&source=post_page-----a19557db0aaa---------------------------------------)

[Careers](https://medium.com/jobs-at-medium/work-at-medium-959d1a85284e?source=post_page-----a19557db0aaa---------------------------------------)

Press

[Blog](https://blog.medium.com/?source=post_page-----a19557db0aaa---------------------------------------)

[Privacy](https://policy.medium.com/medium-privacy-policy-f03bf92035c9?source=post_page-----a19557db0aaa---------------------------------------)

[Rules](https://policy.medium.com/medium-rules-30e5502c4eb4?source=post_page-----a19557db0aaa---------------------------------------)

[Terms](https://policy.medium.com/medium-terms-of-service-9db0094a1e0f?source=post_page-----a19557db0aaa---------------------------------------)

[Text to speech](https://speechify.com/medium?source=post_page-----a19557db0aaa---------------------------------------)