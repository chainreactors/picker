---
title: Day4 Recon: Hunting Hidden Attack Surfaces , using Nmap, Masscan & Dirsearch for Service &…
url: https://infosecwriteups.com/day4-recon-hunting-hidden-attack-surfaces-using-nmap-masscan-dirsearch-for-service-c623de2fcdf6?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2025-08-11
fetch_date: 2025-10-07T00:17:08.193246
---

# Day4 Recon: Hunting Hidden Attack Surfaces , using Nmap, Masscan & Dirsearch for Service &…

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2Fc623de2fcdf6&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fday4-recon-hunting-hidden-attack-surfaces-using-nmap-masscan-dirsearch-for-service-c623de2fcdf6&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fday4-recon-hunting-hidden-attack-surfaces-using-nmap-masscan-dirsearch-for-service-c623de2fcdf6&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-c623de2fcdf6---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-c623de2fcdf6---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

Member-only story

# Day4 Recon: **Hunting Hidden Attack Surfaces , using Nmap, Masscan & Dirsearch for Service & Directory Enumeration**

[![Ayush Kumar](https://miro.medium.com/v2/resize:fill:64:64/1*02Ex2WoqjL8muk2ApxE_mA.jpeg)](https://3xabyt3.medium.com/?source=post_page---byline--c623de2fcdf6---------------------------------------)

[Ayush Kumar](https://3xabyt3.medium.com/?source=post_page---byline--c623de2fcdf6---------------------------------------)

3 min read

·

Aug 9, 2025

--

Share

If you’re skipping over service and directory enumeration, you’re likely missing out on critical vulnerabilities. Here’s how to uncover them with real tools and simple steps.

Press enter or click to view image in full size

![]()

When it comes to ethical hacking or bug bounty hunting, a lot of people focus on the obvious — domains, subdomains, maybe a little port scanning. But what about what’s *not* visible at first glance?

Not a member: [**Read Here**](https://3xabyt3.medium.com/day4-recon-hunting-hidden-attack-surfaces-using-nmap-masscan-dirsearch-for-service-c623de2fcdf6?sk=fceb79160f8b826eb3e587ccd9eae216)

That’s where **service and directory enumeration** comes in. It’s how you uncover the stuff most people miss: unprotected admin panels, forgotten services, misconfigured APIs, and more.

In this post, we’ll walk through three powerful tools — **Nmap**, **Masscan**, and **Dirsearch** — and show how you can use them in real-life scenarios to uncover hidden attack surfaces.

Let’s keep it simple, actionable, and hands-on.

## Why Enumeration Even Matters

Think of enumeration as digital exploration. You’re not attacking anything — you’re discovering what’s there.

* **Service enumeration** tells you what’s running (like SSH, HTTP, MySQL).
* **Directory enumeration** digs into web…

--

--

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:96:96/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--c623de2fcdf6---------------------------------------)

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:128:128/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--c623de2fcdf6---------------------------------------)

Follow

[## Published in InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---post_publication_info--c623de2fcdf6---------------------------------------)

[71K followers](/followers?source=post_page---post_publication_info--c623de2fcdf6---------------------------------------)

·[Last published 3 hours ago](/actuator-unleashed-a-guide-to-finding-and-exploiting-spring-boot-actuator-endpoints-29252dcd9d79?source=post_page---post_publication_info--c623de2fcdf6---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow

[![Ayush Kumar](https://miro.medium.com/v2/resize:fill:96:96/1*02Ex2WoqjL8muk2ApxE_mA.jpeg)](https://3xabyt3.medium.com/?source=post_page---post_author_info--c623de2fcdf6---------------------------------------)

[![Ayush Kumar](https://miro.medium.com/v2/resize:fill:128:128/1*02Ex2WoqjL8muk2ApxE_mA.jpeg)](https://3xabyt3.medium.com/?source=post_page---post_author_info--c623de2fcdf6---------------------------------------)

[## Written by Ayush Kumar](https://3xabyt3.medium.com/?source=post_page---post_author_info--c623de2fcdf6---------------------------------------)

[681 followers](https://3xabyt3.medium.com/followers?source=post_page---post_author_info--c623de2fcdf6---------------------------------------)

·[16 following](https://medium.com/%403xabyt3/following?source=post_page---post_author_info--c623de2fcdf6---------------------------------------)

Hello eveyone , this is Ayush from India. I write about DevOps, Cloud, Cyber Security, Programming

## No responses yet

[Help](https://help.medium.com/hc/en-us?source=post_page-----c623de2fcdf6---------------------------------------)

[Status](https://status.medium.com/?source=post_page-----c623de2fcdf6---------------------------------------)

[About](https://medium.com/about?autoplay=1&source=post_page-----c623de2fcdf6---------------------------------------)

[Careers](https://medium.com/jobs-at-medium/work-at-medium-959d1a85284e?source=post_page-----c623de2fcdf6---------------------------------------)

Press

[Blog](https://blog.medium.com/?source=post_page-----c623de2fcdf6---------------------------------------)

[Privacy](https://policy.medium.com/medium-privacy-policy-f03bf92035c9?source=post_page-----c623de2fcdf6---------------------------------------)

[Rules](https://policy.medium.com/medium-rules-30e5502c4eb4?source=post_page-----c623de2fcdf6---------------------------------------)

[Terms](https://policy.medium.com/medium-terms-of-service-9db0094a1e0f?source=post_page-----c623de2fcdf6---------------------------------------)

[Text to speech](https://speechify.com/medium?source=post_page-----c623de2fcdf6---------------------------------------)