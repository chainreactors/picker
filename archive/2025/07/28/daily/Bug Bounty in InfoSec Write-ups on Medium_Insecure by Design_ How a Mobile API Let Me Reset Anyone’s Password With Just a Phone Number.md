---
title: Insecure by Design: How a Mobile API Let Me Reset Anyone’s Password With Just a Phone Number
url: https://infosecwriteups.com/insecure-by-design-how-a-mobile-api-let-me-reset-anyones-password-with-just-a-phone-number-ba588ec384e5?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2025-07-28
fetch_date: 2025-10-06T23:17:34.132698
---

# Insecure by Design: How a Mobile API Let Me Reset Anyone’s Password With Just a Phone Number

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2Fba588ec384e5&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Finsecure-by-design-how-a-mobile-api-let-me-reset-anyones-password-with-just-a-phone-number-ba588ec384e5&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Finsecure-by-design-how-a-mobile-api-let-me-reset-anyones-password-with-just-a-phone-number-ba588ec384e5&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-ba588ec384e5---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-ba588ec384e5---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

Member-only story

# 📱 Insecure by Design: How a Mobile API Let Me Reset Anyone’s Password With Just a Phone Number 🔓

[![Iski](https://miro.medium.com/v2/resize:fill:64:64/1*PpvkjPQ1lY6aTYHT9kDX5w.png)](https://medium.com/%40iski?source=post_page---byline--ba588ec384e5---------------------------------------)

[Iski](https://medium.com/%40iski?source=post_page---byline--ba588ec384e5---------------------------------------)

4 min read

·

Jul 26, 2025

--

3

Share

Free [Link](https://medium.com/%40iski/insecure-by-design-how-a-mobile-api-let-me-reset-anyones-password-with-just-a-phone-number-ba588ec384e5?sk=e3d7745d285ad12f439971e6b33ca875) 🎈

Hey there!😁

Press enter or click to view image in full size

![]()

Image by AI

> *⚠️* Disclaimer: *This blog is for* ***educational purposes*** *only. All vulnerabilities mentioned here have been responsibly disclosed to the organization involved. Don’t be a script kiddie. Be a responsible researcher. 🙏*

## 🧠 Reality Check: Passwords Can Be as Fragile as My Sleep Schedule 😴

It was 3:12 AM.

I was lying there, like most security researchers, contemplating if *the fourth cup of coffee was a mistake* or a stepping stone to glory. My eyes were burning, fingers jittery, and tabs — oh boy — **128 tabs open** in Burp Suite like a DJ’s deck.

Some people count sheep to fall asleep.
 **I count open ports.** 🐏🛜

And somewhere between `api/v2/user/profile` and my 7th screenshot of a 403 Forbidden, I struck gold. Or rather... I struck a **leaky faucet of logic flaw** in an API endpoint that screamed:

> ***“I was made on a Friday evening, deploy-ready, zero test cases.”***

--

--

3

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:96:96/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--ba588ec384e5---------------------------------------)

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:128:128/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--ba588ec384e5---------------------------------------)

Follow

[## Published in InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---post_publication_info--ba588ec384e5---------------------------------------)

[71K followers](/followers?source=post_page---post_publication_info--ba588ec384e5---------------------------------------)

·[Last published 2 hours ago](/actuator-unleashed-a-guide-to-finding-and-exploiting-spring-boot-actuator-endpoints-29252dcd9d79?source=post_page---post_publication_info--ba588ec384e5---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow

[![Iski](https://miro.medium.com/v2/resize:fill:96:96/1*PpvkjPQ1lY6aTYHT9kDX5w.png)](https://medium.com/%40iski?source=post_page---post_author_info--ba588ec384e5---------------------------------------)

[![Iski](https://miro.medium.com/v2/resize:fill:128:128/1*PpvkjPQ1lY6aTYHT9kDX5w.png)](https://medium.com/%40iski?source=post_page---post_author_info--ba588ec384e5---------------------------------------)

[## Written by Iski](https://medium.com/%40iski?source=post_page---post_author_info--ba588ec384e5---------------------------------------)

[1.8K followers](https://medium.com/%40iski/followers?source=post_page---post_author_info--ba588ec384e5---------------------------------------)

·[7 following](https://medium.com/%40iski/following?source=post_page---post_author_info--ba588ec384e5---------------------------------------)

Cybersecurity Researcher | Penetration Tester | Bug Bounty Hunter | Web security| Passionate about cyber security, security automation

## Responses (3)

See all responses

[Help](https://help.medium.com/hc/en-us?source=post_page-----ba588ec384e5---------------------------------------)

[Status](https://status.medium.com/?source=post_page-----ba588ec384e5---------------------------------------)

[About](https://medium.com/about?autoplay=1&source=post_page-----ba588ec384e5---------------------------------------)

[Careers](https://medium.com/jobs-at-medium/work-at-medium-959d1a85284e?source=post_page-----ba588ec384e5---------------------------------------)

Press

[Blog](https://blog.medium.com/?source=post_page-----ba588ec384e5---------------------------------------)

[Privacy](https://policy.medium.com/medium-privacy-policy-f03bf92035c9?source=post_page-----ba588ec384e5---------------------------------------)

[Rules](https://policy.medium.com/medium-rules-30e5502c4eb4?source=post_page-----ba588ec384e5---------------------------------------)

[Terms](https://policy.medium.com/medium-terms-of-service-9db0094a1e0f?source=post_page-----ba588ec384e5---------------------------------------)

[Text to speech](https://speechify.com/medium?source=post_page-----ba588ec384e5---------------------------------------)