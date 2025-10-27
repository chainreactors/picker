---
title: Recon Basics for Beginners: A Simple Guide
url: https://infosecwriteups.com/recon-basics-for-beginners-a-simple-guide-e76885cdd333?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2025-07-02
fetch_date: 2025-10-06T23:50:02.720679
---

# Recon Basics for Beginners: A Simple Guide

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2Fe76885cdd333&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Frecon-basics-for-beginners-a-simple-guide-e76885cdd333&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Frecon-basics-for-beginners-a-simple-guide-e76885cdd333&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[Mastodon](https://me.dm/%40satyampathania)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-e76885cdd333---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-e76885cdd333---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

Press enter or click to view image in full size

![]()

Member-only story

# Recon Basics for Beginners: A Simple Guide

[![Satyam Pathania](https://miro.medium.com/v2/resize:fill:64:64/1*JPS1IZD4U8su1FV_T-n-gA.png)](https://medium.com/%40SatyamPathania?source=post_page---byline--e76885cdd333---------------------------------------)

[Satyam Pathania](https://medium.com/%40SatyamPathania?source=post_page---byline--e76885cdd333---------------------------------------)

3 min read

·

Jul 1, 2025

--

1

Share

I am not an active bug bounty hunter but when i was in the field the most basic approach how i get started was this .

If you’re just starting out in ethical hacking or bug bounty hunting, the first thing you should learn is **Reconnaissance**, or simply **Recon**. Think of recon as the “stalking” phase — but legal and with computers. You gather as much info as you can before trying to break anything.

This guide will explain recon in super basic terms. No fancy words, no hacker lingo. Just beginner-friendly steps with a pinch of humor

## What is Recon?

Recon is like researching your target. Just like before going on a date, you check their Instagram, LinkedIn, and maybe their dog’s name — here, you do the same but with websites.

*There are two types of recon:*

* **Passive Recon**: You act like a ninja. No interaction with the target. (No one knows you’re spying.)
* **Active Recon**: You start poking the target gently. Like knocking on someone’s door just to see who’s home.

## Step 1: Find All Subdomains (Subdomain Enumeration)

Websites don’t live alone. They have roommates — called subdomains. Like:

* login.example.com

--

--

1

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:96:96/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--e76885cdd333---------------------------------------)

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:128:128/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--e76885cdd333---------------------------------------)

Follow

[## Published in InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---post_publication_info--e76885cdd333---------------------------------------)

[71K followers](/followers?source=post_page---post_publication_info--e76885cdd333---------------------------------------)

·[Last published 3 hours ago](/actuator-unleashed-a-guide-to-finding-and-exploiting-spring-boot-actuator-endpoints-29252dcd9d79?source=post_page---post_publication_info--e76885cdd333---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow

[![Satyam Pathania](https://miro.medium.com/v2/resize:fill:96:96/1*JPS1IZD4U8su1FV_T-n-gA.png)](https://medium.com/%40SatyamPathania?source=post_page---post_author_info--e76885cdd333---------------------------------------)

[![Satyam Pathania](https://miro.medium.com/v2/resize:fill:128:128/1*JPS1IZD4U8su1FV_T-n-gA.png)](https://medium.com/%40SatyamPathania?source=post_page---post_author_info--e76885cdd333---------------------------------------)

[## Written by Satyam Pathania](https://medium.com/%40SatyamPathania?source=post_page---post_author_info--e76885cdd333---------------------------------------)

[3.9K followers](https://medium.com/%40SatyamPathania/followers?source=post_page---post_author_info--e76885cdd333---------------------------------------)

·[56 following](https://medium.com/%40SatyamPathania/following?source=post_page---post_author_info--e76885cdd333---------------------------------------)

Hello, I'm Satyam Pathania, a cybersecurity writer. I simplify digital security to empower readers. Join me to explore tech, code, and books!

## Responses (1)

See all responses

[Help](https://help.medium.com/hc/en-us?source=post_page-----e76885cdd333---------------------------------------)

[Status](https://status.medium.com/?source=post_page-----e76885cdd333---------------------------------------)

[About](https://medium.com/about?autoplay=1&source=post_page-----e76885cdd333---------------------------------------)

[Careers](https://medium.com/jobs-at-medium/work-at-medium-959d1a85284e?source=post_page-----e76885cdd333---------------------------------------)

Press

[Blog](https://blog.medium.com/?source=post_page-----e76885cdd333---------------------------------------)

[Privacy](https://policy.medium.com/medium-privacy-policy-f03bf92035c9?source=post_page-----e76885cdd333---------------------------------------)

[Rules](https://policy.medium.com/medium-rules-30e5502c4eb4?source=post_page-----e76885cdd333---------------------------------------)

[Terms](https://policy.medium.com/medium-terms-of-service-9db0094a1e0f?source=post_page-----e76885cdd333---------------------------------------)

[Text to speech](https://speechify.com/medium?source=post_page-----e76885cdd333---------------------------------------)