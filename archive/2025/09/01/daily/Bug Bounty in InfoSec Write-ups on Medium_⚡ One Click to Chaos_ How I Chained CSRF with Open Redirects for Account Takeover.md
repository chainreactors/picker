---
title: ⚡ One Click to Chaos: How I Chained CSRF with Open Redirects for Account Takeover
url: https://infosecwriteups.com/one-click-to-chaos-how-i-chained-csrf-with-open-redirects-for-account-takeover-fd9d5d753402?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2025-09-01
fetch_date: 2025-10-02T19:29:01.215691
---

# ⚡ One Click to Chaos: How I Chained CSRF with Open Redirects for Account Takeover

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2Ffd9d5d753402&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fone-click-to-chaos-how-i-chained-csrf-with-open-redirects-for-account-takeover-fd9d5d753402&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fone-click-to-chaos-how-i-chained-csrf-with-open-redirects-for-account-takeover-fd9d5d753402&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-fd9d5d753402---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-fd9d5d753402---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

Member-only story

# ⚡ One Click to Chaos: How I Chained CSRF with Open Redirects for Account Takeover

[![Iski](https://miro.medium.com/v2/resize:fill:64:64/1*PpvkjPQ1lY6aTYHT9kDX5w.png)](https://medium.com/%40iski?source=post_page---byline--fd9d5d753402---------------------------------------)

[Iski](https://medium.com/%40iski?source=post_page---byline--fd9d5d753402---------------------------------------)

2 min read

·

Aug 28, 2025

--

1

Share

Free [link](https://medium.com/%40iski/one-click-to-chaos-how-i-chained-csrf-with-open-redirects-for-account-takeover-fd9d5d753402?sk=80f028c0a75737cb79fa1ca5596336b5) 🎈

Hey there!😁

Press enter or click to view image in full size

![]()

Image by AI

You know life is hard when your coffee machine refuses to work, your Wi-Fi drops mid-burp scan, and the only constant in life is your Recon script running on a VPS. But that day? That day the universe gave me a gift 🎁 — a shiny, vulnerable endpoint just waiting to be poked.

[## Burp, Bounce, and Break: How Web Cache Poisoning Let Me Control the App 🎈🌐

### Hey there!😁

infosecwriteups.com](/burp-bounce-and-break-how-web-cache-poisoning-let-me-control-the-app-be173528ff8a?source=post_page-----fd9d5d753402---------------------------------------)

## 🕵️ Recon Phase — Digging the Gold Mine

I kicked off with **mass recon** using `subfinder`, `amass`, and my custom chaos script to map the attack surface. While scraping through URLs with `gau` and `waybackurls`, I spotted a *weird-looking redirect param* buried deep in an old GraphQL endpoint:

```
https://target.com/graphql?next=https://evil.com
```

At first glance, it screamed **open redirect**, but I had a hunch there was more gold hidden here.

--

--

1

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:96:96/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--fd9d5d753402---------------------------------------)

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:128:128/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--fd9d5d753402---------------------------------------)

Follow

[## Published in InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---post_publication_info--fd9d5d753402---------------------------------------)

[71K followers](/followers?source=post_page---post_publication_info--fd9d5d753402---------------------------------------)

·[Last published 4 days ago](/how-to-find-p1-bugs-using-google-in-your-target-part-1-e37455324dc1?source=post_page---post_publication_info--fd9d5d753402---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow

[![Iski](https://miro.medium.com/v2/resize:fill:96:96/1*PpvkjPQ1lY6aTYHT9kDX5w.png)](https://medium.com/%40iski?source=post_page---post_author_info--fd9d5d753402---------------------------------------)

[![Iski](https://miro.medium.com/v2/resize:fill:128:128/1*PpvkjPQ1lY6aTYHT9kDX5w.png)](https://medium.com/%40iski?source=post_page---post_author_info--fd9d5d753402---------------------------------------)

[## Written by Iski](https://medium.com/%40iski?source=post_page---post_author_info--fd9d5d753402---------------------------------------)

[1.8K followers](https://medium.com/%40iski/followers?source=post_page---post_author_info--fd9d5d753402---------------------------------------)

·[7 following](https://medium.com/%40iski/following?source=post_page---post_author_info--fd9d5d753402---------------------------------------)

Cybersecurity Researcher | Penetration Tester | Bug Bounty Hunter | Web security| Passionate about cyber security, security automation

## Responses (1)

See all responses

[Help](https://help.medium.com/hc/en-us?source=post_page-----fd9d5d753402---------------------------------------)

[Status](https://status.medium.com/?source=post_page-----fd9d5d753402---------------------------------------)

[About](https://medium.com/about?autoplay=1&source=post_page-----fd9d5d753402---------------------------------------)

[Careers](https://medium.com/jobs-at-medium/work-at-medium-959d1a85284e?source=post_page-----fd9d5d753402---------------------------------------)

Press

[Blog](https://blog.medium.com/?source=post_page-----fd9d5d753402---------------------------------------)

[Privacy](https://policy.medium.com/medium-privacy-policy-f03bf92035c9?source=post_page-----fd9d5d753402---------------------------------------)

[Rules](https://policy.medium.com/medium-rules-30e5502c4eb4?source=post_page-----fd9d5d753402---------------------------------------)

[Terms](https://policy.medium.com/medium-terms-of-service-9db0094a1e0f?source=post_page-----fd9d5d753402---------------------------------------)

[Text to speech](https://speechify.com/medium?source=post_page-----fd9d5d753402---------------------------------------)