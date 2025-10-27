---
title: From Recon to Root ⚡: A Beginner’s Journey Into CTF Hacking
url: https://infosecwriteups.com/from-recon-to-root-a-beginners-journey-into-ctf-hacking-575374698b02?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2025-09-20
fetch_date: 2025-10-02T20:25:47.833060
---

# From Recon to Root ⚡: A Beginner’s Journey Into CTF Hacking

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2F575374698b02&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Ffrom-recon-to-root-a-beginners-journey-into-ctf-hacking-575374698b02&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Ffrom-recon-to-root-a-beginners-journey-into-ctf-hacking-575374698b02&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-575374698b02---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-575374698b02---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

Member-only story

# From Recon to Root ⚡: A Beginner’s Journey Into CTF Hacking

[![Vipul Sonule](https://miro.medium.com/v2/resize:fill:64:64/1*3BWnARhHAdOwHCGvC440qA.png)](https://medium.com/%40vipulsonule71?source=post_page---byline--575374698b02---------------------------------------)

[Vipul Sonule](https://medium.com/%40vipulsonule71?source=post_page---byline--575374698b02---------------------------------------)

8 min read

·

Sep 19, 2025

--

Share

Press enter or click to view image in full size

![]()

[***👉 Free Link***](https://thehackerslog.substack.com/p/from-recon-to-root-a-beginners-journey)

There’s a magical moment in every security learner’s life when scanning a box, finding a weak service, and typing `sudo` for the first time clicks into place. It feels like climbing a mountain and standing on the top — the air tastes different. That’s what Capture The Flag (CTF) hacking does to people: it turns curiosity into craft, curiosity into muscle memory, and sticky notes into a toolkit you carry forever.

This guide is your companion on a beginner-friendly, human-first walkthrough from **recon** to **root**. It’s written in a conversational style, packed with practical steps, real-world mental models, links, resources, and earning paths (yes — hackers can earn legitimately). Think of it as the long-form guide you’d want on your screen at 2 AM while you crack your first box. ⚡

## Table of Contents

1. The CTF Mindset (Why CTFs?) 🧠
2. Types of CTFs: Jeopardy vs. Attack-Defense 🧩
3. The Essential Toolkit (What you’ll use) 🛠️
4. Recon: Start with Listening and Observation 👂
5. Enumeration: The Art of Asking the Right Questions 🔎
6. Exploitation Basics: Web, Binary, Crypto, Forensics, Pwn 💥
7. Privilege Escalation…

--

--

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:96:96/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--575374698b02---------------------------------------)

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:128:128/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--575374698b02---------------------------------------)

Follow

[## Published in InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---post_publication_info--575374698b02---------------------------------------)

[71K followers](/followers?source=post_page---post_publication_info--575374698b02---------------------------------------)

·[Last published 4 days ago](/how-to-find-p1-bugs-using-google-in-your-target-part-1-e37455324dc1?source=post_page---post_publication_info--575374698b02---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow

[![Vipul Sonule](https://miro.medium.com/v2/resize:fill:96:96/1*3BWnARhHAdOwHCGvC440qA.png)](https://medium.com/%40vipulsonule71?source=post_page---post_author_info--575374698b02---------------------------------------)

[![Vipul Sonule](https://miro.medium.com/v2/resize:fill:128:128/1*3BWnARhHAdOwHCGvC440qA.png)](https://medium.com/%40vipulsonule71?source=post_page---post_author_info--575374698b02---------------------------------------)

[## Written by Vipul Sonule](https://medium.com/%40vipulsonule71?source=post_page---post_author_info--575374698b02---------------------------------------)

[2.1K followers](https://medium.com/%40vipulsonule71/followers?source=post_page---post_author_info--575374698b02---------------------------------------)

·[497 following](https://medium.com/%40vipulsonule71/following?source=post_page---post_author_info--575374698b02---------------------------------------)

I’m a cybersecurity enthusiast and bug bounty hunter who loves programming, exploring AI, and sharing tips on hacking, coding, and tech.

## No responses yet

[Help](https://help.medium.com/hc/en-us?source=post_page-----575374698b02---------------------------------------)

[Status](https://status.medium.com/?source=post_page-----575374698b02---------------------------------------)

[About](https://medium.com/about?autoplay=1&source=post_page-----575374698b02---------------------------------------)

[Careers](https://medium.com/jobs-at-medium/work-at-medium-959d1a85284e?source=post_page-----575374698b02---------------------------------------)

Press

[Blog](https://blog.medium.com/?source=post_page-----575374698b02---------------------------------------)

[Privacy](https://policy.medium.com/medium-privacy-policy-f03bf92035c9?source=post_page-----575374698b02---------------------------------------)

[Rules](https://policy.medium.com/medium-rules-30e5502c4eb4?source=post_page-----575374698b02---------------------------------------)

[Terms](https://policy.medium.com/medium-terms-of-service-9db0094a1e0f?source=post_page-----575374698b02---------------------------------------)

[Text to speech](https://speechify.com/medium?source=post_page-----575374698b02---------------------------------------)