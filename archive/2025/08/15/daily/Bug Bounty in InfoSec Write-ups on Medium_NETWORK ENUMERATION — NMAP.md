---
title: NETWORK ENUMERATION — NMAP
url: https://infosecwriteups.com/network-enumeration-nmap-6018ef8a7556?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2025-08-15
fetch_date: 2025-10-07T00:47:40.822371
---

# NETWORK ENUMERATION — NMAP

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2F6018ef8a7556&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fnetwork-enumeration-nmap-6018ef8a7556&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fnetwork-enumeration-nmap-6018ef8a7556&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-6018ef8a7556---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-6018ef8a7556---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

Member-only story

# NETWORK ENUMERATION — NMAP

[![PARADOX](https://miro.medium.com/v2/resize:fill:64:64/1*J3k1FJDWCemetGOK0Qqveg.jpeg)](https://medium.com/%40P4RAD0X?source=post_page---byline--6018ef8a7556---------------------------------------)

[PARADOX](https://medium.com/%40P4RAD0X?source=post_page---byline--6018ef8a7556---------------------------------------)

10 min read

·

Aug 11, 2025

--

2

Share

Hey there! 👋 I’m currently working through the [CPTS](https://academy.hackthebox.com/preview/certifications/htb-certified-penetration-testing-specialist) module from [Hack The Box Academy](https://academy.hackthebox.com/) and thought why not share my notes along the way?
Whether you’re grinding for CPTS or just here to pick up something new, this post’s got you covered.

Today’s topic: **Nmap**. The go-to tool for scanning networks, finding open ports, and uncovering potential vulnerabilities. Whether you’re into hacking or just curious about networks, this tool is a must-know.

[**Free Link**](https://medium.com/%40P4RAD0X/network-enumeration-nmap-6018ef8a7556?sk=7861a0b19308f987ed1d87580b1be1a8)

**Covered topics in this post —** what is enumeration, what is Nmap, enumeration hosts and types of enumeration, what is firewall and IDP/IPS, bypassing some security measure, Cheat Sheet, etc.

If you don’t feel like going through the full details, you can skip straight to the last section, Cheat Sheet 😊

## Enumeration

Enumeration is the most important part of hacking. It’s not about just getting access to a system, it’s about finding all the possible ways in. The tools are cool, but it’s how we use the info they give us that really matters. By digging into services, understanding how they work, and finding misconfigurations (usually from poor security habits), we start to see opportunities. The more info we collect, the easier it is to figure out how to break in.

**Enumeration is the key.** Simple as that! :)

## Introduction to NMAP

--

--

2

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:96:96/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--6018ef8a7556---------------------------------------)

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:128:128/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--6018ef8a7556---------------------------------------)

Follow

[## Published in InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---post_publication_info--6018ef8a7556---------------------------------------)

[71K followers](/followers?source=post_page---post_publication_info--6018ef8a7556---------------------------------------)

·[Last published 4 hours ago](/actuator-unleashed-a-guide-to-finding-and-exploiting-spring-boot-actuator-endpoints-29252dcd9d79?source=post_page---post_publication_info--6018ef8a7556---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow

[![PARADOX](https://miro.medium.com/v2/resize:fill:96:96/1*J3k1FJDWCemetGOK0Qqveg.jpeg)](https://medium.com/%40P4RAD0X?source=post_page---post_author_info--6018ef8a7556---------------------------------------)

[![PARADOX](https://miro.medium.com/v2/resize:fill:128:128/1*J3k1FJDWCemetGOK0Qqveg.jpeg)](https://medium.com/%40P4RAD0X?source=post_page---post_author_info--6018ef8a7556---------------------------------------)

[## Written by PARADOX](https://medium.com/%40P4RAD0X?source=post_page---post_author_info--6018ef8a7556---------------------------------------)

[78 followers](https://medium.com/%40P4RAD0X/followers?source=post_page---post_author_info--6018ef8a7556---------------------------------------)

·[11 following](https://medium.com/%40P4RAD0X/following?source=post_page---post_author_info--6018ef8a7556---------------------------------------)

Just another Pentester. Leveling up with every hack, every challenge, and every lesson. In this game, the grind never stops... :)

## Responses (2)

See all responses

[Help](https://help.medium.com/hc/en-us?source=post_page-----6018ef8a7556---------------------------------------)

[Status](https://status.medium.com/?source=post_page-----6018ef8a7556---------------------------------------)

[About](https://medium.com/about?autoplay=1&source=post_page-----6018ef8a7556---------------------------------------)

[Careers](https://medium.com/jobs-at-medium/work-at-medium-959d1a85284e?source=post_page-----6018ef8a7556---------------------------------------)

Press

[Blog](https://blog.medium.com/?source=post_page-----6018ef8a7556---------------------------------------)

[Privacy](https://policy.medium.com/medium-privacy-policy-f03bf92035c9?source=post_page-----6018ef8a7556---------------------------------------)

[Rules](https://policy.medium.com/medium-rules-30e5502c4eb4?source=post_page-----6018ef8a7556---------------------------------------)

[Terms](https://policy.medium.com/medium-terms-of-service-9db0094a1e0f?source=post_page-----6018ef8a7556---------------------------------------)

[Text to speech](https://speechify.com/medium?source=post_page-----6018ef8a7556---------------------------------------)