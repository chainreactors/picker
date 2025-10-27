---
title: Behind the Scenes: How Pre-Prod Leaks Led Me to Prod Secrets
url: https://infosecwriteups.com/behind-the-scenes-how-pre-prod-leaks-led-me-to-prod-secrets-6cea22dcc64e?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2025-07-06
fetch_date: 2025-10-06T23:26:33.732463
---

# Behind the Scenes: How Pre-Prod Leaks Led Me to Prod Secrets

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2F6cea22dcc64e&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fbehind-the-scenes-how-pre-prod-leaks-led-me-to-prod-secrets-6cea22dcc64e&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fbehind-the-scenes-how-pre-prod-leaks-led-me-to-prod-secrets-6cea22dcc64e&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-6cea22dcc64e---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-6cea22dcc64e---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

Member-only story

# **Behind the Scenes: How Pre-Prod Leaks Led Me to Prod Secrets 🎮🔍**

[![Iski](https://miro.medium.com/v2/resize:fill:64:64/1*PpvkjPQ1lY6aTYHT9kDX5w.png)](https://medium.com/%40iski?source=post_page---byline--6cea22dcc64e---------------------------------------)

[Iski](https://medium.com/%40iski?source=post_page---byline--6cea22dcc64e---------------------------------------)

4 min read

·

Jul 4, 2025

--

Share

Free [Link](https://medium.com/%40iski/behind-the-scenes-how-pre-prod-leaks-led-me-to-prod-secrets-6cea22dcc64e?sk=e4ceb2ebf5250c981f35094e0101a33f) 🎈

Hey there!😁

Press enter or click to view image in full size

![]()

Image by Gemini AI

**When Dev Said “This Is Just Pre-Prod,” But the Secrets Were Real 🤯**

One fine night, while most people were cuddling their pillows or their partners, I was cuddling my terminal and hugging Burp Suite like it owed me money. I had just nuked my ramen and decided, instead of eating, to feast on bugs — and guess what? This time, dinner was served from pre-prod.

This is the story of how a sleepy staging server spilled production secrets like a kid who couldn’t keep a birthday surprise 🤔🎉

[## How I Turned a 403 Forbidden Into a Goldmine 🚀

### Free Link🎈

infosecwriteups.com](/how-i-turned-a-403-forbidden-into-a-goldmine-738cdf1407aa?source=post_page-----6cea22dcc64e---------------------------------------)

## 🛠️ Recon Begins: The Hunt for Forgotten Realms

I kicked off mass recon using the usual tools:

```
subfinder -d target.com | httpx -mc 200 > live.txt
```

Then, some focused Google dorking:

```
site:target.com inurl:staging
site:target.com intitle:"pre-prod"
```

--

--

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:96:96/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--6cea22dcc64e---------------------------------------)

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:128:128/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--6cea22dcc64e---------------------------------------)

Follow

[## Published in InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---post_publication_info--6cea22dcc64e---------------------------------------)

[71K followers](/followers?source=post_page---post_publication_info--6cea22dcc64e---------------------------------------)

·[Last published 3 hours ago](/actuator-unleashed-a-guide-to-finding-and-exploiting-spring-boot-actuator-endpoints-29252dcd9d79?source=post_page---post_publication_info--6cea22dcc64e---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow

[![Iski](https://miro.medium.com/v2/resize:fill:96:96/1*PpvkjPQ1lY6aTYHT9kDX5w.png)](https://medium.com/%40iski?source=post_page---post_author_info--6cea22dcc64e---------------------------------------)

[![Iski](https://miro.medium.com/v2/resize:fill:128:128/1*PpvkjPQ1lY6aTYHT9kDX5w.png)](https://medium.com/%40iski?source=post_page---post_author_info--6cea22dcc64e---------------------------------------)

[## Written by Iski](https://medium.com/%40iski?source=post_page---post_author_info--6cea22dcc64e---------------------------------------)

[1.8K followers](https://medium.com/%40iski/followers?source=post_page---post_author_info--6cea22dcc64e---------------------------------------)

·[7 following](https://medium.com/%40iski/following?source=post_page---post_author_info--6cea22dcc64e---------------------------------------)

Cybersecurity Researcher | Penetration Tester | Bug Bounty Hunter | Web security| Passionate about cyber security, security automation

## No responses yet

[Help](https://help.medium.com/hc/en-us?source=post_page-----6cea22dcc64e---------------------------------------)

[Status](https://status.medium.com/?source=post_page-----6cea22dcc64e---------------------------------------)

[About](https://medium.com/about?autoplay=1&source=post_page-----6cea22dcc64e---------------------------------------)

[Careers](https://medium.com/jobs-at-medium/work-at-medium-959d1a85284e?source=post_page-----6cea22dcc64e---------------------------------------)

Press

[Blog](https://blog.medium.com/?source=post_page-----6cea22dcc64e---------------------------------------)

[Privacy](https://policy.medium.com/medium-privacy-policy-f03bf92035c9?source=post_page-----6cea22dcc64e---------------------------------------)

[Rules](https://policy.medium.com/medium-rules-30e5502c4eb4?source=post_page-----6cea22dcc64e---------------------------------------)

[Terms](https://policy.medium.com/medium-terms-of-service-9db0094a1e0f?source=post_page-----6cea22dcc64e---------------------------------------)

[Text to speech](https://speechify.com/medium?source=post_page-----6cea22dcc64e---------------------------------------)