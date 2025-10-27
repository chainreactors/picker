---
title: ️ DNS and Deception: How SSRF and Metadata Gave Me Cloud Access on a Silver Platter
url: https://infosecwriteups.com/%EF%B8%8F-dns-and-deception-how-ssrf-and-metadata-gave-me-cloud-access-on-a-silver-platter-e9cf97c3693f?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2025-07-30
fetch_date: 2025-10-06T23:28:30.509004
---

# ️ DNS and Deception: How SSRF and Metadata Gave Me Cloud Access on a Silver Platter

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2Fe9cf97c3693f&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2F%25EF%25B8%258F-dns-and-deception-how-ssrf-and-metadata-gave-me-cloud-access-on-a-silver-platter-e9cf97c3693f&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2F%25EF%25B8%258F-dns-and-deception-how-ssrf-and-metadata-gave-me-cloud-access-on-a-silver-platter-e9cf97c3693f&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-e9cf97c3693f---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-e9cf97c3693f---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

Member-only story

# 🌩️ DNS and Deception: How SSRF and Metadata Gave Me Cloud Access on a Silver Platter 🧠📦

[![Iski](https://miro.medium.com/v2/resize:fill:64:64/1*PpvkjPQ1lY6aTYHT9kDX5w.png)](https://medium.com/%40iski?source=post_page---byline--e9cf97c3693f---------------------------------------)

[Iski](https://medium.com/%40iski?source=post_page---byline--e9cf97c3693f---------------------------------------)

4 min read

·

Jul 24, 2025

--

2

Share

Free [Link](https://medium.com/%40iski/%EF%B8%8F-dns-and-deception-how-ssrf-and-metadata-gave-me-cloud-access-on-a-silver-platter-e9cf97c3693f?sk=c166d6c26e4f6781ebf53e1e221f3c67) 🎈

**Hey there!😁**

Press enter or click to view image in full size

![]()

Image by AI

## 🚶‍♂️💼 Life, Bugs, and Breakfast

There I was, sitting with my 3-day-old coffee, debugging a recon script that looked more tired than me.

Just when I was questioning my entire bug bounty career (and my life choices), a DNS endpoint whispered:
 **“psst… wanna see something spicy?”**

[## When Life Throws Errors, I Throw Commands: My Command Injection Bug🤓

### Hey there..! 👋

infosecwriteups.com](/when-life-throws-errors-i-throw-commands-my-command-injection-bug-18969d979da4?source=post_page-----e9cf97c3693f---------------------------------------)

I leaned in. DNS never lies. And so began a rabbit hole that led to cloud credentials, `169.254.169.254`, and *one hell of a payout*. 🤑

## 🔍 Part 1: The Recon That Whispered Secrets

During one of my wild mass recon sprees (read: letting `httpx`, `waybackurls`, and `gau` scream into the void), I stumbled across a juicy subdomain:

```
export-pdf.internal.mytarget.com
```

🔥 Suspicious? Yes.
 🔐 Auth required? Nope.
 ⚠️ Rate limit? Not even close.

--

--

2

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:96:96/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--e9cf97c3693f---------------------------------------)

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:128:128/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--e9cf97c3693f---------------------------------------)

Follow

[## Published in InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---post_publication_info--e9cf97c3693f---------------------------------------)

[71K followers](/followers?source=post_page---post_publication_info--e9cf97c3693f---------------------------------------)

·[Last published 3 hours ago](/actuator-unleashed-a-guide-to-finding-and-exploiting-spring-boot-actuator-endpoints-29252dcd9d79?source=post_page---post_publication_info--e9cf97c3693f---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow

[![Iski](https://miro.medium.com/v2/resize:fill:96:96/1*PpvkjPQ1lY6aTYHT9kDX5w.png)](https://medium.com/%40iski?source=post_page---post_author_info--e9cf97c3693f---------------------------------------)

[![Iski](https://miro.medium.com/v2/resize:fill:128:128/1*PpvkjPQ1lY6aTYHT9kDX5w.png)](https://medium.com/%40iski?source=post_page---post_author_info--e9cf97c3693f---------------------------------------)

[## Written by Iski](https://medium.com/%40iski?source=post_page---post_author_info--e9cf97c3693f---------------------------------------)

[1.8K followers](https://medium.com/%40iski/followers?source=post_page---post_author_info--e9cf97c3693f---------------------------------------)

·[7 following](https://medium.com/%40iski/following?source=post_page---post_author_info--e9cf97c3693f---------------------------------------)

Cybersecurity Researcher | Penetration Tester | Bug Bounty Hunter | Web security| Passionate about cyber security, security automation

## Responses (2)

See all responses

[Help](https://help.medium.com/hc/en-us?source=post_page-----e9cf97c3693f---------------------------------------)

[Status](https://status.medium.com/?source=post_page-----e9cf97c3693f---------------------------------------)

[About](https://medium.com/about?autoplay=1&source=post_page-----e9cf97c3693f---------------------------------------)

[Careers](https://medium.com/jobs-at-medium/work-at-medium-959d1a85284e?source=post_page-----e9cf97c3693f---------------------------------------)

Press

[Blog](https://blog.medium.com/?source=post_page-----e9cf97c3693f---------------------------------------)

[Privacy](https://policy.medium.com/medium-privacy-policy-f03bf92035c9?source=post_page-----e9cf97c3693f---------------------------------------)

[Rules](https://policy.medium.com/medium-rules-30e5502c4eb4?source=post_page-----e9cf97c3693f---------------------------------------)

[Terms](https://policy.medium.com/medium-terms-of-service-9db0094a1e0f?source=post_page-----e9cf97c3693f---------------------------------------)

[Text to speech](https://speechify.com/medium?source=post_page-----e9cf97c3693f---------------------------------------)