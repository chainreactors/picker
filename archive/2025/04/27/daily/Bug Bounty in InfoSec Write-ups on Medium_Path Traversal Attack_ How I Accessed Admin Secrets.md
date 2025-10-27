---
title: Path Traversal Attack: How I Accessed Admin Secrets
url: https://infosecwriteups.com/path-traversal-attack-how-i-accessed-admin-secrets-fa5de1865031?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2025-04-27
fetch_date: 2025-10-06T22:03:46.771966
---

# Path Traversal Attack: How I Accessed Admin Secrets

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2Ffa5de1865031&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fpath-traversal-attack-how-i-accessed-admin-secrets-fa5de1865031&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fpath-traversal-attack-how-i-accessed-admin-secrets-fa5de1865031&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-fa5de1865031---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-fa5de1865031---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

Member-only story

# Path Traversal Attack: How I Accessed Admin Secrets 📂

[![Vipul Sonule](https://miro.medium.com/v2/resize:fill:64:64/1*3BWnARhHAdOwHCGvC440qA.png)](https://medium.com/%40vipulsonule71?source=post_page---byline--fa5de1865031---------------------------------------)

[Vipul Sonule](https://medium.com/%40vipulsonule71?source=post_page---byline--fa5de1865031---------------------------------------)

3 min read

·

Apr 26, 2025

--

1

Share

## Path Traversal Attack: How I Accessed Admin Secrets 📂

Press enter or click to view image in full size

![]()

## Introduction 🧠

Web apps are supposed to protect their files, right?
 But what if I told you that just a *small trick* could let you *sneak in* and peek at hidden admin files, secrets, and sensitive stuff? 😈

Today, I’ll share how I **found a Path Traversal bug**, **accessed admin secrets**, and how you can **protect your apps** from these sneaky attacks too.
 Let’s dive into this real hacking story! 🕵️‍♂️

## What is Path Traversal? 🚶‍♂️

**Path Traversal** (also called *Directory Traversal*) is when a hacker changes the file path to access files outside the folder they are supposed to be in.

In short — they trick the server into giving files like:

* `/etc/passwd` 📄 (Linux user database)
* `C:\Windows\System32\config\SAM` 📄 (Windows password file)
* Hidden admin configs and backups 🔒

👉 **Example payloads**:

```
../../../../etc/passwd
..\..\..\..\windows\win.ini
```

Such small tricks — but *super powerful*! 💣

--

--

1

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:96:96/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--fa5de1865031---------------------------------------)

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:128:128/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--fa5de1865031---------------------------------------)

Follow

[## Published in InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---post_publication_info--fa5de1865031---------------------------------------)

[71K followers](/followers?source=post_page---post_publication_info--fa5de1865031---------------------------------------)

·[Last published 1 hour ago](/actuator-unleashed-a-guide-to-finding-and-exploiting-spring-boot-actuator-endpoints-29252dcd9d79?source=post_page---post_publication_info--fa5de1865031---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow

[![Vipul Sonule](https://miro.medium.com/v2/resize:fill:96:96/1*3BWnARhHAdOwHCGvC440qA.png)](https://medium.com/%40vipulsonule71?source=post_page---post_author_info--fa5de1865031---------------------------------------)

[![Vipul Sonule](https://miro.medium.com/v2/resize:fill:128:128/1*3BWnARhHAdOwHCGvC440qA.png)](https://medium.com/%40vipulsonule71?source=post_page---post_author_info--fa5de1865031---------------------------------------)

[## Written by Vipul Sonule](https://medium.com/%40vipulsonule71?source=post_page---post_author_info--fa5de1865031---------------------------------------)

[2.1K followers](https://medium.com/%40vipulsonule71/followers?source=post_page---post_author_info--fa5de1865031---------------------------------------)

·[497 following](https://medium.com/%40vipulsonule71/following?source=post_page---post_author_info--fa5de1865031---------------------------------------)

I’m a cybersecurity enthusiast and bug bounty hunter who loves programming, exploring AI, and sharing tips on hacking, coding, and tech.

## Responses (1)

See all responses

[Help](https://help.medium.com/hc/en-us?source=post_page-----fa5de1865031---------------------------------------)

[Status](https://status.medium.com/?source=post_page-----fa5de1865031---------------------------------------)

[About](https://medium.com/about?autoplay=1&source=post_page-----fa5de1865031---------------------------------------)

[Careers](https://medium.com/jobs-at-medium/work-at-medium-959d1a85284e?source=post_page-----fa5de1865031---------------------------------------)

Press

[Blog](https://blog.medium.com/?source=post_page-----fa5de1865031---------------------------------------)

[Privacy](https://policy.medium.com/medium-privacy-policy-f03bf92035c9?source=post_page-----fa5de1865031---------------------------------------)

[Rules](https://policy.medium.com/medium-rules-30e5502c4eb4?source=post_page-----fa5de1865031---------------------------------------)

[Terms](https://policy.medium.com/medium-terms-of-service-9db0094a1e0f?source=post_page-----fa5de1865031---------------------------------------)

[Text to speech](https://speechify.com/medium?source=post_page-----fa5de1865031---------------------------------------)