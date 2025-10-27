---
title: How I Hacked India’s Most Popular Matrimony Website and Earned a ₹10,000 Amazon Gift Card
url: https://infosecwriteups.com/how-i-hacked-indias-most-popular-matrimony-website-and-earned-a-10-000-amazon-gift-card-4dad7b6eff5d?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2025-02-25
fetch_date: 2025-10-06T20:34:42.029206
---

# How I Hacked India’s Most Popular Matrimony Website and Earned a ₹10,000 Amazon Gift Card

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2F4dad7b6eff5d&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fhow-i-hacked-indias-most-popular-matrimony-website-and-earned-a-10-000-amazon-gift-card-4dad7b6eff5d&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fhow-i-hacked-indias-most-popular-matrimony-website-and-earned-a-10-000-amazon-gift-card-4dad7b6eff5d&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-4dad7b6eff5d---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-4dad7b6eff5d---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

Member-only story

# How I Hacked India’s Most Popular Matrimony Website and Earned a ₹10,000 Amazon Gift Card

[![Vivek PS](https://miro.medium.com/v2/resize:fill:64:64/1*gswVWtLbFDKYFuLKsi063g.png)](https://medium.com/%40vivekps143?source=post_page---byline--4dad7b6eff5d---------------------------------------)

[Vivek PS](https://medium.com/%40vivekps143?source=post_page---byline--4dad7b6eff5d---------------------------------------)

5 min read

·

Feb 23, 2025

--

1

Share

> **My article is open to everyone; non-member readers can click** [**this link**](https://medium.com/%40vivekps143/how-i-hacked-indias-most-popular-matrimony-website-and-earned-a-10-000-amazon-gift-card-4dad7b6eff5d?sk=1110d51c3ae92aa1ce595d763e66a6af) **to read the full text.**

## **Introduction**

I don’t know why, but after getting married, I started receiving more and more invitations from beautiful girls on a popular matrimony website. Browsing through their profiles and photos was quite entertaining — just make sure your wife isn’t nearby while doing this!

Since mine was an arranged marriage, I didn’t delete my profile immediately. I thought, *Why not keep it for a few more months? If anything goes wrong, I can continue using the same account without paying again.* At least I’d save some money — even if I couldn’t save the marriage. A practical backup plan.

One night, after dinner, I was casually checking my email on my laptop when I noticed a new interest from a girl on the site. I turned back — safety first. No sign of my wife. “Let’s go, handsome,” I told myself and clicked the link.

Just then, I noticed a shadow growing larger near the room door. No, it wasn’t a ghost — it was my wife.

Press enter or click to view image in full size

![]()

“What are you doing, dear?” she asked, staring at my screen.

--

--

1

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:96:96/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--4dad7b6eff5d---------------------------------------)

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:128:128/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--4dad7b6eff5d---------------------------------------)

Follow

[## Published in InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---post_publication_info--4dad7b6eff5d---------------------------------------)

[71K followers](/followers?source=post_page---post_publication_info--4dad7b6eff5d---------------------------------------)

·[Last published just now](/actuator-unleashed-a-guide-to-finding-and-exploiting-spring-boot-actuator-endpoints-29252dcd9d79?source=post_page---post_publication_info--4dad7b6eff5d---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow

[![Vivek PS](https://miro.medium.com/v2/resize:fill:96:96/1*gswVWtLbFDKYFuLKsi063g.png)](https://medium.com/%40vivekps143?source=post_page---post_author_info--4dad7b6eff5d---------------------------------------)

[![Vivek PS](https://miro.medium.com/v2/resize:fill:128:128/1*gswVWtLbFDKYFuLKsi063g.png)](https://medium.com/%40vivekps143?source=post_page---post_author_info--4dad7b6eff5d---------------------------------------)

[## Written by Vivek PS](https://medium.com/%40vivekps143?source=post_page---post_author_info--4dad7b6eff5d---------------------------------------)

[420 followers](https://medium.com/%40vivekps143/followers?source=post_page---post_author_info--4dad7b6eff5d---------------------------------------)

·[69 following](https://medium.com/%40vivekps143/following?source=post_page---post_author_info--4dad7b6eff5d---------------------------------------)

I’m a programmer, web security researcher and chess player, focused on innovation, learning, and creating impactful solutions for growth.

## Responses (1)

See all responses

[Help](https://help.medium.com/hc/en-us?source=post_page-----4dad7b6eff5d---------------------------------------)

[Status](https://status.medium.com/?source=post_page-----4dad7b6eff5d---------------------------------------)

[About](https://medium.com/about?autoplay=1&source=post_page-----4dad7b6eff5d---------------------------------------)

[Careers](https://medium.com/jobs-at-medium/work-at-medium-959d1a85284e?source=post_page-----4dad7b6eff5d---------------------------------------)

Press

[Blog](https://blog.medium.com/?source=post_page-----4dad7b6eff5d---------------------------------------)

[Privacy](https://policy.medium.com/medium-privacy-policy-f03bf92035c9?source=post_page-----4dad7b6eff5d---------------------------------------)

[Rules](https://policy.medium.com/medium-rules-30e5502c4eb4?source=post_page-----4dad7b6eff5d---------------------------------------)

[Terms](https://policy.medium.com/medium-terms-of-service-9db0094a1e0f?source=post_page-----4dad7b6eff5d---------------------------------------)

[Text to speech](https://speechify.com/medium?source=post_page-----4dad7b6eff5d---------------------------------------)