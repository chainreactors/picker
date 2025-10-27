---
title: The Hidden XSS: A Bug Hidden in the Mist
url: https://infosecwriteups.com/the-hidden-xss-a-bug-hidden-in-the-mist-907d6cc55322?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2025-04-14
fetch_date: 2025-10-06T22:03:31.947175
---

# The Hidden XSS: A Bug Hidden in the Mist

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2F907d6cc55322&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fthe-hidden-xss-a-bug-hidden-in-the-mist-907d6cc55322&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fthe-hidden-xss-a-bug-hidden-in-the-mist-907d6cc55322&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-907d6cc55322---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-907d6cc55322---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

Member-only story

# The Hidden XSS: A Bug Hidden in the Mist

[![SIDDHANT SHUKLA](https://miro.medium.com/v2/resize:fill:64:64/1*8ZQ4ust4pThkatOZK2KniQ.jpeg)](https://ghostman01.medium.com/?source=post_page---byline--907d6cc55322---------------------------------------)

[SIDDHANT SHUKLA](https://ghostman01.medium.com/?source=post_page---byline--907d6cc55322---------------------------------------)

4 min read

·

Apr 4, 2025

--

2

Share

[Free Article Link](https://ghostman01.medium.com/907d6cc55322?sk=4937abefb609dd3115a12bb7ac034b1d) 👈

Hey fellow Bug Hunters and Security Researchers!
 As the title suggests, this is the tale of an XSS vulnerability — hidden in the mist. So, let’s dive right in.

Press enter or click to view image in full size

![meditative ghost]()

## 🔍 Starting the Hunt

In November 2024, I was testing my most loved payment app website. At that time, I was still a noob (to be honest, I still feel like one 😅). I had no idea where to begin, so I used `subfinder` to collect all the subdomains of target— a classic move.

I opened each subdomain in Firefox, one after another, and many hours later… I realized I was right back where I started. Literally **position = 0** 😂
 Frustrating as hell. All I had done was open hundreds of tabs with nothing to show for it.

## 🕳️ Digging Deeper with WaybackURLs

The next day, I decided to take a different approach. I used `waybackurls` (thanks Tomnomnom 🙌) to collect historical data for target. Within 10 minutes, I had a mountain of URLs — most of them leading to files like `.png`, `.jpg`, `.woff`, etc. Basically, useless for my purpose.

And once again, I was stuck. So many files — but **what exactly was I looking for**?

## 👻 Building GhostFilter

--

--

2

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:96:96/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--907d6cc55322---------------------------------------)

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:128:128/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--907d6cc55322---------------------------------------)

Follow

[## Published in InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---post_publication_info--907d6cc55322---------------------------------------)

[71K followers](/followers?source=post_page---post_publication_info--907d6cc55322---------------------------------------)

·[Last published 1 hour ago](/actuator-unleashed-a-guide-to-finding-and-exploiting-spring-boot-actuator-endpoints-29252dcd9d79?source=post_page---post_publication_info--907d6cc55322---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow

[![SIDDHANT SHUKLA](https://miro.medium.com/v2/resize:fill:96:96/1*8ZQ4ust4pThkatOZK2KniQ.jpeg)](https://ghostman01.medium.com/?source=post_page---post_author_info--907d6cc55322---------------------------------------)

[![SIDDHANT SHUKLA](https://miro.medium.com/v2/resize:fill:128:128/1*8ZQ4ust4pThkatOZK2KniQ.jpeg)](https://ghostman01.medium.com/?source=post_page---post_author_info--907d6cc55322---------------------------------------)

[## Written by SIDDHANT SHUKLA](https://ghostman01.medium.com/?source=post_page---post_author_info--907d6cc55322---------------------------------------)

[855 followers](https://ghostman01.medium.com/followers?source=post_page---post_author_info--907d6cc55322---------------------------------------)

·[424 following](https://medium.com/%40ghostman01/following?source=post_page---post_author_info--907d6cc55322---------------------------------------)

just a lazy hunter.

## Responses (2)

See all responses

[Help](https://help.medium.com/hc/en-us?source=post_page-----907d6cc55322---------------------------------------)

[Status](https://status.medium.com/?source=post_page-----907d6cc55322---------------------------------------)

[About](https://medium.com/about?autoplay=1&source=post_page-----907d6cc55322---------------------------------------)

[Careers](https://medium.com/jobs-at-medium/work-at-medium-959d1a85284e?source=post_page-----907d6cc55322---------------------------------------)

Press

[Blog](https://blog.medium.com/?source=post_page-----907d6cc55322---------------------------------------)

[Privacy](https://policy.medium.com/medium-privacy-policy-f03bf92035c9?source=post_page-----907d6cc55322---------------------------------------)

[Rules](https://policy.medium.com/medium-rules-30e5502c4eb4?source=post_page-----907d6cc55322---------------------------------------)

[Terms](https://policy.medium.com/medium-terms-of-service-9db0094a1e0f?source=post_page-----907d6cc55322---------------------------------------)

[Text to speech](https://speechify.com/medium?source=post_page-----907d6cc55322---------------------------------------)