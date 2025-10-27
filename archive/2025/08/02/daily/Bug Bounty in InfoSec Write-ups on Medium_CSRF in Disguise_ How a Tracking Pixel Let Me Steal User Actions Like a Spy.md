---
title: CSRF in Disguise: How a Tracking Pixel Let Me Steal User Actions Like a Spy
url: https://infosecwriteups.com/csrf-in-disguise-how-a-tracking-pixel-let-me-steal-user-actions-like-a-spy-28c084002d1e?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2025-08-02
fetch_date: 2025-10-07T00:47:49.444082
---

# CSRF in Disguise: How a Tracking Pixel Let Me Steal User Actions Like a Spy

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2F28c084002d1e&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fcsrf-in-disguise-how-a-tracking-pixel-let-me-steal-user-actions-like-a-spy-28c084002d1e&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fcsrf-in-disguise-how-a-tracking-pixel-let-me-steal-user-actions-like-a-spy-28c084002d1e&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-28c084002d1e---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-28c084002d1e---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

Member-only story

# 📡 CSRF in Disguise: How a Tracking Pixel Let Me Steal User Actions Like a Spy 🚁🎯

[![Iski](https://miro.medium.com/v2/resize:fill:64:64/1*PpvkjPQ1lY6aTYHT9kDX5w.png)](https://medium.com/%40iski?source=post_page---byline--28c084002d1e---------------------------------------)

[Iski](https://medium.com/%40iski?source=post_page---byline--28c084002d1e---------------------------------------)

3 min read

·

Jul 31, 2025

--

2

Share

Free [Link](https://medium.com/%40iski/csrf-in-disguise-how-a-tracking-pixel-let-me-steal-user-actions-like-a-spy-28c084002d1e?sk=e3b6f6c968b9f7a7a425fb784097d48e) 🎈

**Hey there!😁**

Press enter or click to view image in full size

![]()

Image by Gemini AI

### 😂 Life is pixelated…

Ever feel like you’re being watched by that one invisible guy in every movie? Yeah, that was me this week, except instead of invisibility powers, I had a 1x1 pixel image and a CSRF misconfig. Welcome to another episode of *“Hack the Planet with Minimal Effort and Maximum Drama.”*

Now, let’s be honest — adulting is hard. But nothing is harder than trying to explain to your mom that you’re not hacking Facebook, you’re responsibly disclosing bugs. She still thinks I work at “Google support.”

Anyway…

[## How I Found a Payment Tampering Bug and Almost Paid Zero Dollars!

### Free Link🎈

infosecwriteups.com](/how-i-found-a-payment-tampering-bug-and-almost-paid-zero-dollars-0933297f77f0?source=post_page-----28c084002d1e---------------------------------------)

## 🌐 Reconnaissance: The Pixel Hunt Begins

Like every bug bounty hunter worth their hoodie, I started with **massive recon**. Using tools like `gau`, `waybackurls`, and `katana`, I started pulling endpoints from every subdomain like I was vacuuming the internet.

```
# Grab endpoints
gau target.com >…
```

--

--

2

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:96:96/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--28c084002d1e---------------------------------------)

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:128:128/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--28c084002d1e---------------------------------------)

Follow

[## Published in InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---post_publication_info--28c084002d1e---------------------------------------)

[71K followers](/followers?source=post_page---post_publication_info--28c084002d1e---------------------------------------)

·[Last published 4 hours ago](/actuator-unleashed-a-guide-to-finding-and-exploiting-spring-boot-actuator-endpoints-29252dcd9d79?source=post_page---post_publication_info--28c084002d1e---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow

[![Iski](https://miro.medium.com/v2/resize:fill:96:96/1*PpvkjPQ1lY6aTYHT9kDX5w.png)](https://medium.com/%40iski?source=post_page---post_author_info--28c084002d1e---------------------------------------)

[![Iski](https://miro.medium.com/v2/resize:fill:128:128/1*PpvkjPQ1lY6aTYHT9kDX5w.png)](https://medium.com/%40iski?source=post_page---post_author_info--28c084002d1e---------------------------------------)

[## Written by Iski](https://medium.com/%40iski?source=post_page---post_author_info--28c084002d1e---------------------------------------)

[1.8K followers](https://medium.com/%40iski/followers?source=post_page---post_author_info--28c084002d1e---------------------------------------)

·[7 following](https://medium.com/%40iski/following?source=post_page---post_author_info--28c084002d1e---------------------------------------)

Cybersecurity Researcher | Penetration Tester | Bug Bounty Hunter | Web security| Passionate about cyber security, security automation

## Responses (2)

See all responses

[Help](https://help.medium.com/hc/en-us?source=post_page-----28c084002d1e---------------------------------------)

[Status](https://status.medium.com/?source=post_page-----28c084002d1e---------------------------------------)

[About](https://medium.com/about?autoplay=1&source=post_page-----28c084002d1e---------------------------------------)

[Careers](https://medium.com/jobs-at-medium/work-at-medium-959d1a85284e?source=post_page-----28c084002d1e---------------------------------------)

Press

[Blog](https://blog.medium.com/?source=post_page-----28c084002d1e---------------------------------------)

[Privacy](https://policy.medium.com/medium-privacy-policy-f03bf92035c9?source=post_page-----28c084002d1e---------------------------------------)

[Rules](https://policy.medium.com/medium-rules-30e5502c4eb4?source=post_page-----28c084002d1e---------------------------------------)

[Terms](https://policy.medium.com/medium-terms-of-service-9db0094a1e0f?source=post_page-----28c084002d1e---------------------------------------)

[Text to speech](https://speechify.com/medium?source=post_page-----28c084002d1e---------------------------------------)