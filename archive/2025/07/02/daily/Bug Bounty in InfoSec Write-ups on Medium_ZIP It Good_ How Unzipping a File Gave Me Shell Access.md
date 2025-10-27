---
title: ZIP It Good: How Unzipping a File Gave Me Shell Access
url: https://infosecwriteups.com/zip-it-good-how-unzipping-a-file-gave-me-shell-access-15c740bf5226?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2025-07-02
fetch_date: 2025-10-06T23:50:23.404859
---

# ZIP It Good: How Unzipping a File Gave Me Shell Access

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2F15c740bf5226&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fzip-it-good-how-unzipping-a-file-gave-me-shell-access-15c740bf5226&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fzip-it-good-how-unzipping-a-file-gave-me-shell-access-15c740bf5226&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-15c740bf5226---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-15c740bf5226---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

Member-only story

# **ZIP It Good: How Unzipping a File Gave Me Shell Access 🎒💥**

[![Iski](https://miro.medium.com/v2/resize:fill:64:64/1*PpvkjPQ1lY6aTYHT9kDX5w.png)](https://medium.com/%40iski?source=post_page---byline--15c740bf5226---------------------------------------)

[Iski](https://medium.com/%40iski?source=post_page---byline--15c740bf5226---------------------------------------)

3 min read

·

Jun 30, 2025

--

1

Share

Free [Link](https://medium.com/%40iski/zip-it-good-how-unzipping-a-file-gave-me-shell-access-15c740bf5226?sk=84f0487af20e08da6f67683785af877d) 🎈

Hey there!😁

Press enter or click to view image in full size

![]()

Image by Gemini AI

**Life Lesson #86:** If life gives you a ZIP file, don’t just extract it — *exploit it.*

I was halfway through a bowl of noodles that were just too spicy and life decisions that were just too questionable when I stumbled upon a target accepting ZIP file uploads. My brain whispered, “Bro, remember the good ol’ Zip Slip days?”

And oh boy, I zipped, slipped, and shell-ed my way into their server like I was born to unzip chaos.

[## How I Turned a 403 Forbidden Into a Goldmine 🚀

### Free Link🎈

infosecwriteups.com](/how-i-turned-a-403-forbidden-into-a-goldmine-738cdf1407aa?source=post_page-----15c740bf5226---------------------------------------)

## 🔎 Reconnaissance: The Digital Dumpster Dive

Like always, I was neck-deep in recon with:

```
subfinder -d victim.com | httpx -mc 200 > live.txt
waybackurls victim.com | grep -i 'upload'
```

I came across an endpoint like:

```
https://app.victim.com/tools/uploadPlugin
```

Looked boring. Felt suspicious. Accepted ZIP files. Jackpot? Maybe.

--

--

1

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:96:96/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--15c740bf5226---------------------------------------)

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:128:128/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--15c740bf5226---------------------------------------)

Follow

[## Published in InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---post_publication_info--15c740bf5226---------------------------------------)

[71K followers](/followers?source=post_page---post_publication_info--15c740bf5226---------------------------------------)

·[Last published 3 hours ago](/actuator-unleashed-a-guide-to-finding-and-exploiting-spring-boot-actuator-endpoints-29252dcd9d79?source=post_page---post_publication_info--15c740bf5226---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow

[![Iski](https://miro.medium.com/v2/resize:fill:96:96/1*PpvkjPQ1lY6aTYHT9kDX5w.png)](https://medium.com/%40iski?source=post_page---post_author_info--15c740bf5226---------------------------------------)

[![Iski](https://miro.medium.com/v2/resize:fill:128:128/1*PpvkjPQ1lY6aTYHT9kDX5w.png)](https://medium.com/%40iski?source=post_page---post_author_info--15c740bf5226---------------------------------------)

[## Written by Iski](https://medium.com/%40iski?source=post_page---post_author_info--15c740bf5226---------------------------------------)

[1.8K followers](https://medium.com/%40iski/followers?source=post_page---post_author_info--15c740bf5226---------------------------------------)

·[7 following](https://medium.com/%40iski/following?source=post_page---post_author_info--15c740bf5226---------------------------------------)

Cybersecurity Researcher | Penetration Tester | Bug Bounty Hunter | Web security| Passionate about cyber security, security automation

## Responses (1)

See all responses

[Help](https://help.medium.com/hc/en-us?source=post_page-----15c740bf5226---------------------------------------)

[Status](https://status.medium.com/?source=post_page-----15c740bf5226---------------------------------------)

[About](https://medium.com/about?autoplay=1&source=post_page-----15c740bf5226---------------------------------------)

[Careers](https://medium.com/jobs-at-medium/work-at-medium-959d1a85284e?source=post_page-----15c740bf5226---------------------------------------)

Press

[Blog](https://blog.medium.com/?source=post_page-----15c740bf5226---------------------------------------)

[Privacy](https://policy.medium.com/medium-privacy-policy-f03bf92035c9?source=post_page-----15c740bf5226---------------------------------------)

[Rules](https://policy.medium.com/medium-rules-30e5502c4eb4?source=post_page-----15c740bf5226---------------------------------------)

[Terms](https://policy.medium.com/medium-terms-of-service-9db0094a1e0f?source=post_page-----15c740bf5226---------------------------------------)

[Text to speech](https://speechify.com/medium?source=post_page-----15c740bf5226---------------------------------------)