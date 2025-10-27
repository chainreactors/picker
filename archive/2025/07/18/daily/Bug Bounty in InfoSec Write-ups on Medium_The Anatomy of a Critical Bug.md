---
title: The Anatomy of a Critical Bug
url: https://infosecwriteups.com/the-anatomy-of-a-critical-bug-388329a1c55a?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2025-07-18
fetch_date: 2025-10-06T23:28:35.256741
---

# The Anatomy of a Critical Bug

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2F388329a1c55a&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fthe-anatomy-of-a-critical-bug-388329a1c55a&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fthe-anatomy-of-a-critical-bug-388329a1c55a&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-388329a1c55a---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-388329a1c55a---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

Member-only story

# The Anatomy of a Critical Bug

[![SIDDHANT SHUKLA](https://miro.medium.com/v2/resize:fill:64:64/1*8ZQ4ust4pThkatOZK2KniQ.jpeg)](https://ghostman01.medium.com/?source=post_page---byline--388329a1c55a---------------------------------------)

[SIDDHANT SHUKLA](https://ghostman01.medium.com/?source=post_page---byline--388329a1c55a---------------------------------------)

4 min read

·

Jul 16, 2025

--

3

Share

> A blank page. Quiet recon. A bug they never saw coming.

![]()

Johan Liebert

### [Read For Freee..ee..👈](https://ghostman01.medium.com/388329a1c55a?sk=474f5bcf0878235d8a3dc0cc75d9f276)

## 🐞Yo!!

Hey fellow Bug Hunter or Security Researcher,
 As promised in my previous write-up *Accessing Admin Directory*, I’m back with another one — this time, a **Critical Severity bug** that builds directly on the last discovery.

[## Accessing Admin Directory

### Bug hunting through sleep, subdomains, and surprises

infosecwriteups.com](/accessing-admin-directory-eec04145a0fc?source=post_page-----388329a1c55a---------------------------------------)

Let’s dive into the continuation of this hunt.

## 🔭 Expanding the Horizon

After finding the accessible `/admin` directory, a thought struck me — could there be other environment-based subdomains like:

```
dev.target.com
prod.target.com
staging.target.com
dev0.target.com
dev1.target.com
```

So, I started manually checking possible variants.

## 🛠️ Enumeration Begins

I ran a basic Subfinder command:

```
subfinder -d target.com --all --recursive | anew subs.txt
```

--

--

3

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:96:96/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--388329a1c55a---------------------------------------)

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:128:128/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--388329a1c55a---------------------------------------)

Follow

[## Published in InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---post_publication_info--388329a1c55a---------------------------------------)

[71K followers](/followers?source=post_page---post_publication_info--388329a1c55a---------------------------------------)

·[Last published 3 hours ago](/actuator-unleashed-a-guide-to-finding-and-exploiting-spring-boot-actuator-endpoints-29252dcd9d79?source=post_page---post_publication_info--388329a1c55a---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow

[![SIDDHANT SHUKLA](https://miro.medium.com/v2/resize:fill:96:96/1*8ZQ4ust4pThkatOZK2KniQ.jpeg)](https://ghostman01.medium.com/?source=post_page---post_author_info--388329a1c55a---------------------------------------)

[![SIDDHANT SHUKLA](https://miro.medium.com/v2/resize:fill:128:128/1*8ZQ4ust4pThkatOZK2KniQ.jpeg)](https://ghostman01.medium.com/?source=post_page---post_author_info--388329a1c55a---------------------------------------)

[## Written by SIDDHANT SHUKLA](https://ghostman01.medium.com/?source=post_page---post_author_info--388329a1c55a---------------------------------------)

[855 followers](https://ghostman01.medium.com/followers?source=post_page---post_author_info--388329a1c55a---------------------------------------)

·[424 following](https://medium.com/%40ghostman01/following?source=post_page---post_author_info--388329a1c55a---------------------------------------)

just a lazy hunter.

## Responses (3)

See all responses

[Help](https://help.medium.com/hc/en-us?source=post_page-----388329a1c55a---------------------------------------)

[Status](https://status.medium.com/?source=post_page-----388329a1c55a---------------------------------------)

[About](https://medium.com/about?autoplay=1&source=post_page-----388329a1c55a---------------------------------------)

[Careers](https://medium.com/jobs-at-medium/work-at-medium-959d1a85284e?source=post_page-----388329a1c55a---------------------------------------)

Press

[Blog](https://blog.medium.com/?source=post_page-----388329a1c55a---------------------------------------)

[Privacy](https://policy.medium.com/medium-privacy-policy-f03bf92035c9?source=post_page-----388329a1c55a---------------------------------------)

[Rules](https://policy.medium.com/medium-rules-30e5502c4eb4?source=post_page-----388329a1c55a---------------------------------------)

[Terms](https://policy.medium.com/medium-terms-of-service-9db0094a1e0f?source=post_page-----388329a1c55a---------------------------------------)

[Text to speech](https://speechify.com/medium?source=post_page-----388329a1c55a---------------------------------------)