---
title: Blog Title: Not Your File: How Misconfigured MIME Types Let Me Upload Evil Scripts
url: https://infosecwriteups.com/blog-title-not-your-file-how-misconfigured-mime-types-let-me-upload-evil-scripts-889efb18a7ce?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2025-05-16
fetch_date: 2025-10-06T22:25:30.655454
---

# Blog Title: Not Your File: How Misconfigured MIME Types Let Me Upload Evil Scripts

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2F889efb18a7ce&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fblog-title-not-your-file-how-misconfigured-mime-types-let-me-upload-evil-scripts-889efb18a7ce&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fblog-title-not-your-file-how-misconfigured-mime-types-let-me-upload-evil-scripts-889efb18a7ce&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-889efb18a7ce---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-889efb18a7ce---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

Member-only story

# 📝 **Blog Title:** Not Your File: How Misconfigured MIME Types Let Me Upload Evil Scripts 📁😈

[![Iski](https://miro.medium.com/v2/resize:fill:64:64/1*PpvkjPQ1lY6aTYHT9kDX5w.png)](https://medium.com/%40iski?source=post_page---byline--889efb18a7ce---------------------------------------)

[Iski](https://medium.com/%40iski?source=post_page---byline--889efb18a7ce---------------------------------------)

3 min read

·

May 15, 2025

--

Share

Free [Link](https://medium.com/%40iski/blog-title-not-your-file-how-misconfigured-mime-types-let-me-upload-evil-scripts-889efb18a7ce?sk=4b3e39dad81004ef3da3c9188db47da9) 🎈

Hey there!😁

Press enter or click to view image in full size

![]()

Image by Gemini AI

> ***Life’s Rule #1:*** *Never trust someone who says, “Just upload your resume here.” Because I did. And ended up getting RCE.*
>
> ***Rule #2:*** *If your file upload accepts* `.svg`*, it’s probably open to the gates of hell.*
>
> ***Rule #3:*** *Always double-check your MIME types, unless you enjoy turning profile pictures into payloads.*

## 🧭 The Recon Phase: From Innocent Endpoints to Upload Armageddon

While sipping chai and passively scrolling through JS files like it’s my toxic ex’s Instagram, I stumbled upon an interesting endpoint:

```
POST /user/upload/avatar
```

It looked boring. Typical profile image upload, accepting JPEGs, PNGs, blah blah. But here’s the kicker — it **didn’t validate MIME types server-side**. Not even a peep of sanitization.

So I thought: *“Can I fake it ’til I make it?”*

Answer: Yes. Yes, I can. And I did. 😈

--

--

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:96:96/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--889efb18a7ce---------------------------------------)

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:128:128/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--889efb18a7ce---------------------------------------)

Follow

[## Published in InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---post_publication_info--889efb18a7ce---------------------------------------)

[71K followers](/followers?source=post_page---post_publication_info--889efb18a7ce---------------------------------------)

·[Last published 2 hours ago](/actuator-unleashed-a-guide-to-finding-and-exploiting-spring-boot-actuator-endpoints-29252dcd9d79?source=post_page---post_publication_info--889efb18a7ce---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow

[![Iski](https://miro.medium.com/v2/resize:fill:96:96/1*PpvkjPQ1lY6aTYHT9kDX5w.png)](https://medium.com/%40iski?source=post_page---post_author_info--889efb18a7ce---------------------------------------)

[![Iski](https://miro.medium.com/v2/resize:fill:128:128/1*PpvkjPQ1lY6aTYHT9kDX5w.png)](https://medium.com/%40iski?source=post_page---post_author_info--889efb18a7ce---------------------------------------)

[## Written by Iski](https://medium.com/%40iski?source=post_page---post_author_info--889efb18a7ce---------------------------------------)

[1.8K followers](https://medium.com/%40iski/followers?source=post_page---post_author_info--889efb18a7ce---------------------------------------)

·[7 following](https://medium.com/%40iski/following?source=post_page---post_author_info--889efb18a7ce---------------------------------------)

Cybersecurity Researcher | Penetration Tester | Bug Bounty Hunter | Web security| Passionate about cyber security, security automation

## No responses yet

[Help](https://help.medium.com/hc/en-us?source=post_page-----889efb18a7ce---------------------------------------)

[Status](https://status.medium.com/?source=post_page-----889efb18a7ce---------------------------------------)

[About](https://medium.com/about?autoplay=1&source=post_page-----889efb18a7ce---------------------------------------)

[Careers](https://medium.com/jobs-at-medium/work-at-medium-959d1a85284e?source=post_page-----889efb18a7ce---------------------------------------)

Press

[Blog](https://blog.medium.com/?source=post_page-----889efb18a7ce---------------------------------------)

[Privacy](https://policy.medium.com/medium-privacy-policy-f03bf92035c9?source=post_page-----889efb18a7ce---------------------------------------)

[Rules](https://policy.medium.com/medium-rules-30e5502c4eb4?source=post_page-----889efb18a7ce---------------------------------------)

[Terms](https://policy.medium.com/medium-terms-of-service-9db0094a1e0f?source=post_page-----889efb18a7ce---------------------------------------)

[Text to speech](https://speechify.com/medium?source=post_page-----889efb18a7ce---------------------------------------)