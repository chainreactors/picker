---
title: Payload in the Haystack: Using Wayback & ParamSpider to Find a Forgotten Upload Endpoint
url: https://infosecwriteups.com/payload-in-the-haystack-using-wayback-paramspider-to-find-a-forgotten-upload-endpoint-913e80351b9b?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2025-07-20
fetch_date: 2025-10-06T23:28:02.776496
---

# Payload in the Haystack: Using Wayback & ParamSpider to Find a Forgotten Upload Endpoint

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2F913e80351b9b&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fpayload-in-the-haystack-using-wayback-paramspider-to-find-a-forgotten-upload-endpoint-913e80351b9b&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fpayload-in-the-haystack-using-wayback-paramspider-to-find-a-forgotten-upload-endpoint-913e80351b9b&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-913e80351b9b---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-913e80351b9b---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

Member-only story

# 🧨 Payload in the Haystack: Using Wayback & ParamSpider to Find a Forgotten Upload Endpoint 📦

[![Iski](https://miro.medium.com/v2/resize:fill:64:64/1*PpvkjPQ1lY6aTYHT9kDX5w.png)](https://medium.com/%40iski?source=post_page---byline--913e80351b9b---------------------------------------)

[Iski](https://medium.com/%40iski?source=post_page---byline--913e80351b9b---------------------------------------)

4 min read

·

Jul 19, 2025

--

1

Share

Free [Link](https://medium.com/%40iski/payload-in-the-haystack-using-wayback-paramspider-to-find-a-forgotten-upload-endpoint-913e80351b9b?sk=93b9456232c7d61bd45a513fbd801174) 🎈

**Hey there!😁**

Press enter or click to view image in full size

![]()

Image by Gemini AI

## ☕ Life, Bugs, and ParamSpider

It was 3AM. My coffee had gone cold. My VSCode had crashed for the 4th time. And the only thing more broken than my sleep schedule was my Wi-Fi.

But hey — that’s when the real magic happens, right? Late night + recon = either full pwn or full disappointment.

This one turned out to be the former.

What started as a boring ParamSpider + Wayback combo hunt turned into a beautiful ZIP Slip exploit and a bounty that funded three months of Maggi noodles 🍜.

Let me walk you through how a forgotten `/upload` endpoint hidden deep in Wayback led me to a shell in a haystack.

## 🔍 Phase 1: Recon Rituals + Archive Gold Mining

While running the usual recon combo, I did:

```
subfinder -d target.com -o subs.txt
httpx -l subs.txt -title -tech-detect -o live.txt
gauplus -subs target.com -o gau.txt
cat live.txt | waybackurls >> all_urls.txt
paramspider -d target.com -o params.txt
```

--

--

1

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:96:96/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--913e80351b9b---------------------------------------)

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:128:128/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--913e80351b9b---------------------------------------)

Follow

[## Published in InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---post_publication_info--913e80351b9b---------------------------------------)

[71K followers](/followers?source=post_page---post_publication_info--913e80351b9b---------------------------------------)

·[Last published 3 hours ago](/actuator-unleashed-a-guide-to-finding-and-exploiting-spring-boot-actuator-endpoints-29252dcd9d79?source=post_page---post_publication_info--913e80351b9b---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow

[![Iski](https://miro.medium.com/v2/resize:fill:96:96/1*PpvkjPQ1lY6aTYHT9kDX5w.png)](https://medium.com/%40iski?source=post_page---post_author_info--913e80351b9b---------------------------------------)

[![Iski](https://miro.medium.com/v2/resize:fill:128:128/1*PpvkjPQ1lY6aTYHT9kDX5w.png)](https://medium.com/%40iski?source=post_page---post_author_info--913e80351b9b---------------------------------------)

[## Written by Iski](https://medium.com/%40iski?source=post_page---post_author_info--913e80351b9b---------------------------------------)

[1.8K followers](https://medium.com/%40iski/followers?source=post_page---post_author_info--913e80351b9b---------------------------------------)

·[7 following](https://medium.com/%40iski/following?source=post_page---post_author_info--913e80351b9b---------------------------------------)

Cybersecurity Researcher | Penetration Tester | Bug Bounty Hunter | Web security| Passionate about cyber security, security automation

## Responses (1)

See all responses

[Help](https://help.medium.com/hc/en-us?source=post_page-----913e80351b9b---------------------------------------)

[Status](https://status.medium.com/?source=post_page-----913e80351b9b---------------------------------------)

[About](https://medium.com/about?autoplay=1&source=post_page-----913e80351b9b---------------------------------------)

[Careers](https://medium.com/jobs-at-medium/work-at-medium-959d1a85284e?source=post_page-----913e80351b9b---------------------------------------)

Press

[Blog](https://blog.medium.com/?source=post_page-----913e80351b9b---------------------------------------)

[Privacy](https://policy.medium.com/medium-privacy-policy-f03bf92035c9?source=post_page-----913e80351b9b---------------------------------------)

[Rules](https://policy.medium.com/medium-rules-30e5502c4eb4?source=post_page-----913e80351b9b---------------------------------------)

[Terms](https://policy.medium.com/medium-terms-of-service-9db0094a1e0f?source=post_page-----913e80351b9b---------------------------------------)

[Text to speech](https://speechify.com/medium?source=post_page-----913e80351b9b---------------------------------------)