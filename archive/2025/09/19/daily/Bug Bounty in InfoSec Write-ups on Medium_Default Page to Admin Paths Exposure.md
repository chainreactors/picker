---
title: Default Page to Admin Paths Exposure
url: https://infosecwriteups.com/default-page-to-admin-paths-exposure-1d5709b3725b?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2025-09-19
fetch_date: 2025-10-02T20:21:39.912583
---

# Default Page to Admin Paths Exposure

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2F1d5709b3725b&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fdefault-page-to-admin-paths-exposure-1d5709b3725b&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fdefault-page-to-admin-paths-exposure-1d5709b3725b&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-1d5709b3725b---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-1d5709b3725b---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

Member-only story

# Default Page to Admin Paths Exposure

## Uncovering Hidden API

[![SIDDHANT SHUKLA](https://miro.medium.com/v2/resize:fill:64:64/1*8ZQ4ust4pThkatOZK2KniQ.jpeg)](https://ghostman01.medium.com/?source=post_page---byline--1d5709b3725b---------------------------------------)

[SIDDHANT SHUKLA](https://ghostman01.medium.com/?source=post_page---byline--1d5709b3725b---------------------------------------)

3 min read

·

Sep 14, 2025

--

3

Share

### [Read for Freee..ee.e](https://ghostman01.medium.com/1d5709b3725b?sk=955728857b108205c302090e0f0a3625)

![]()

gojo eyes

### 🐺Hunters,

I hope my write-ups are simple and helpful for you. So you can gain some knowledge using my bug findings and apply yourself in your bug hunting journey.

### Introduction

In August 2024, after first valid Bug and a Bounty I started hunting on a new program. I was new and I don’t have any idea what to do, most of the time I was looking for subdomains using subfinder and this was the first time I started hunting for subdomains using ffuf tool.

### Subdomains

I started with basic subdomain enumeration using subfinder tool:

```
subfinder -d target.com --all --recursive | anew subs.txt
```

In couple of minutes, I got a lot of subdomains and they are overwhelming to me because **I don’t know what to do with them ?**

So, I left all subdomains and started with **fuzzing**.

If you ask me, What I want to achieve? **I don’t know either because at that time I was just finding Subdomains.**

### More Subdomains

I started again for hunting subdoamins with **ffuf** tool:

```
ffuf -u…
```

--

--

3

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:96:96/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--1d5709b3725b---------------------------------------)

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:128:128/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--1d5709b3725b---------------------------------------)

Follow

[## Published in InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---post_publication_info--1d5709b3725b---------------------------------------)

[71K followers](/followers?source=post_page---post_publication_info--1d5709b3725b---------------------------------------)

·[Last published 4 days ago](/how-to-find-p1-bugs-using-google-in-your-target-part-1-e37455324dc1?source=post_page---post_publication_info--1d5709b3725b---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow

[![SIDDHANT SHUKLA](https://miro.medium.com/v2/resize:fill:96:96/1*8ZQ4ust4pThkatOZK2KniQ.jpeg)](https://ghostman01.medium.com/?source=post_page---post_author_info--1d5709b3725b---------------------------------------)

[![SIDDHANT SHUKLA](https://miro.medium.com/v2/resize:fill:128:128/1*8ZQ4ust4pThkatOZK2KniQ.jpeg)](https://ghostman01.medium.com/?source=post_page---post_author_info--1d5709b3725b---------------------------------------)

[## Written by SIDDHANT SHUKLA](https://ghostman01.medium.com/?source=post_page---post_author_info--1d5709b3725b---------------------------------------)

[825 followers](https://ghostman01.medium.com/followers?source=post_page---post_author_info--1d5709b3725b---------------------------------------)

·[423 following](https://medium.com/%40ghostman01/following?source=post_page---post_author_info--1d5709b3725b---------------------------------------)

just a lazy hunter.

## Responses (3)

See all responses

[Help](https://help.medium.com/hc/en-us?source=post_page-----1d5709b3725b---------------------------------------)

[Status](https://status.medium.com/?source=post_page-----1d5709b3725b---------------------------------------)

[About](https://medium.com/about?autoplay=1&source=post_page-----1d5709b3725b---------------------------------------)

[Careers](https://medium.com/jobs-at-medium/work-at-medium-959d1a85284e?source=post_page-----1d5709b3725b---------------------------------------)

Press

[Blog](https://blog.medium.com/?source=post_page-----1d5709b3725b---------------------------------------)

[Privacy](https://policy.medium.com/medium-privacy-policy-f03bf92035c9?source=post_page-----1d5709b3725b---------------------------------------)

[Rules](https://policy.medium.com/medium-rules-30e5502c4eb4?source=post_page-----1d5709b3725b---------------------------------------)

[Terms](https://policy.medium.com/medium-terms-of-service-9db0094a1e0f?source=post_page-----1d5709b3725b---------------------------------------)

[Text to speech](https://speechify.com/medium?source=post_page-----1d5709b3725b---------------------------------------)