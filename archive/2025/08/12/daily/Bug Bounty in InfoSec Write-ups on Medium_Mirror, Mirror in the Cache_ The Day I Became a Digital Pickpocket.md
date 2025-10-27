---
title: Mirror, Mirror in the Cache: The Day I Became a Digital Pickpocket
url: https://infosecwriteups.com/mirror-mirror-in-the-cache-the-day-i-became-a-digital-pickpocket-ce695a86dc87?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2025-08-12
fetch_date: 2025-10-07T00:17:10.052083
---

# Mirror, Mirror in the Cache: The Day I Became a Digital Pickpocket

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2Fce695a86dc87&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fmirror-mirror-in-the-cache-the-day-i-became-a-digital-pickpocket-ce695a86dc87&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fmirror-mirror-in-the-cache-the-day-i-became-a-digital-pickpocket-ce695a86dc87&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-ce695a86dc87---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-ce695a86dc87---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

Member-only story

# 🪞 Mirror, Mirror in the Cache: The Day I Became a Digital Pickpocket

[![Iski](https://miro.medium.com/v2/resize:fill:64:64/1*PpvkjPQ1lY6aTYHT9kDX5w.png)](https://medium.com/%40iski?source=post_page---byline--ce695a86dc87---------------------------------------)

[Iski](https://medium.com/%40iski?source=post_page---byline--ce695a86dc87---------------------------------------)

3 min read

·

Aug 11, 2025

--

1

Share

Free [link](https://medium.com/%40iski/mirror-mirror-in-the-cache-the-day-i-became-a-digital-pickpocket-ce695a86dc87?sk=4975b24024319c020ea628485909b478) 🎈

Hey there!😁

Press enter or click to view image in full size

![]()

Image by AI

### Prologue: The Day I Realized My Browser Was a Snitch

They say you can tell a lot about a person by their search history. Well… my search history says *“cheap ramen near me”* followed immediately by *“sensitive data leak bounty programs”*. That’s the day I decided to go all-in on recon — my version of cardio. 🏃‍♂️💻

And like all good stories, this one starts with… boredom, caffeine, and a cloud of tabs open in Burp Suite.

[## 📂 Folder of Fortune: My Accidental Journey into Misconfigured Cloud Bucket Goldmines

### Hey there!😁

medium.com](https://medium.com/%40iski/folder-of-fortune-my-accidental-journey-into-misconfigured-cloud-bucket-goldmines-8ab7b42c287b?source=post_page-----ce695a86dc87---------------------------------------)

## Step 1: Recon Like a Stalker With a Laptop

I kicked things off with a **massive subdomain recon**.
 Tools used:

```
amass enum -passive -d target.com -o subs.txt
subfinder -d target.com -silent >> subs.txt
httpx -l subs.txt -status-code -title -tech-detect -o live_subs.txt
```

One subdomain caught my eye:
 **mirror-api.target.com** — sounds harmless… until you realize “mirror”…

--

--

1

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:96:96/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--ce695a86dc87---------------------------------------)

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:128:128/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--ce695a86dc87---------------------------------------)

Follow

[## Published in InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---post_publication_info--ce695a86dc87---------------------------------------)

[71K followers](/followers?source=post_page---post_publication_info--ce695a86dc87---------------------------------------)

·[Last published 3 hours ago](/actuator-unleashed-a-guide-to-finding-and-exploiting-spring-boot-actuator-endpoints-29252dcd9d79?source=post_page---post_publication_info--ce695a86dc87---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow

[![Iski](https://miro.medium.com/v2/resize:fill:96:96/1*PpvkjPQ1lY6aTYHT9kDX5w.png)](https://medium.com/%40iski?source=post_page---post_author_info--ce695a86dc87---------------------------------------)

[![Iski](https://miro.medium.com/v2/resize:fill:128:128/1*PpvkjPQ1lY6aTYHT9kDX5w.png)](https://medium.com/%40iski?source=post_page---post_author_info--ce695a86dc87---------------------------------------)

[## Written by Iski](https://medium.com/%40iski?source=post_page---post_author_info--ce695a86dc87---------------------------------------)

[1.8K followers](https://medium.com/%40iski/followers?source=post_page---post_author_info--ce695a86dc87---------------------------------------)

·[7 following](https://medium.com/%40iski/following?source=post_page---post_author_info--ce695a86dc87---------------------------------------)

Cybersecurity Researcher | Penetration Tester | Bug Bounty Hunter | Web security| Passionate about cyber security, security automation

## Responses (1)

See all responses

[Help](https://help.medium.com/hc/en-us?source=post_page-----ce695a86dc87---------------------------------------)

[Status](https://status.medium.com/?source=post_page-----ce695a86dc87---------------------------------------)

[About](https://medium.com/about?autoplay=1&source=post_page-----ce695a86dc87---------------------------------------)

[Careers](https://medium.com/jobs-at-medium/work-at-medium-959d1a85284e?source=post_page-----ce695a86dc87---------------------------------------)

Press

[Blog](https://blog.medium.com/?source=post_page-----ce695a86dc87---------------------------------------)

[Privacy](https://policy.medium.com/medium-privacy-policy-f03bf92035c9?source=post_page-----ce695a86dc87---------------------------------------)

[Rules](https://policy.medium.com/medium-rules-30e5502c4eb4?source=post_page-----ce695a86dc87---------------------------------------)

[Terms](https://policy.medium.com/medium-terms-of-service-9db0094a1e0f?source=post_page-----ce695a86dc87---------------------------------------)

[Text to speech](https://speechify.com/medium?source=post_page-----ce695a86dc87---------------------------------------)