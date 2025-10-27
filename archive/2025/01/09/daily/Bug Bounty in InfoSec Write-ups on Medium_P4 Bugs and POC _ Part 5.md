---
title: P4 Bugs and POC | Part 5
url: https://infosecwriteups.com/p4-bugs-and-poc-part-5-556962ec83f7?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2025-01-09
fetch_date: 2025-10-06T20:08:27.102502
---

# P4 Bugs and POC | Part 5

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2F556962ec83f7&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fp4-bugs-and-poc-part-5-556962ec83f7&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fp4-bugs-and-poc-part-5-556962ec83f7&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-556962ec83f7---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-556962ec83f7---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

Member-only story

# P4 Bugs and POC | Part 5

[![Abhijeet kumawat](https://miro.medium.com/v2/resize:fill:64:64/1*lwXXZkQ5xsjHJniXHn-9Tw.jpeg)](https://medium.com/%40kumawatabhijeet2002?source=post_page---byline--556962ec83f7---------------------------------------)

[Abhijeet kumawat](https://medium.com/%40kumawatabhijeet2002?source=post_page---byline--556962ec83f7---------------------------------------)

4 min read

·

Jan 4, 2025

--

Share

## Hi everyone! 🚀

I’m **Abhijeet Kumawat**, a passionate **bug bounty hunter** and **security researcher**. I absolutely love sharing my experiences and knowledge in **bug bounty hunting** and **penetration testing** with the community.

[## Deep Recon Methodology for Bug Bounty Hunters | Part-1

### Hello, everyone! 👋

medium.com](https://medium.com/%40kumawatabhijeet2002/deep-recon-methodology-for-bug-bounty-hunters-part-1-54bdac09dcf4?source=post_page-----556962ec83f7---------------------------------------)

Today, I’m thrilled to kick off a **blog series** focused on **P4 bugs** — those sneaky low-severity vulnerabilities that often get overlooked. But here’s the catch: if you know how to find and exploit them, they can lead to some seriously impactful results! 💥

In this series, I’ll deep dive into each vulnerability, explain how it works, and walk you through a **step-by-step proof-of-concept (PoC)** demonstration. If you stick around and apply these methods on real-world targets, you’re bound to discover some valid **P4 bugs**. Let’s get started! 🕵️‍♂️

Press enter or click to view image in full size

![]()

[## Unleashing My Recon Weapon: A Custom Bash Tool for Bug Bounty🔥

### Hello, everyone! 😊

medium.com](https://medium.com/%40kumawatabhijeet2002/unleashing-my-recon-weapon-a-custom-bash-tool-for-bug-bounty-d946b5f26dd9?source=post_page-----556962ec83f7---------------------------------------)

## 1️⃣ Improper Cache-Control

--

--

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:96:96/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--556962ec83f7---------------------------------------)

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:128:128/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--556962ec83f7---------------------------------------)

Follow

[## Published in InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---post_publication_info--556962ec83f7---------------------------------------)

[71K followers](/followers?source=post_page---post_publication_info--556962ec83f7---------------------------------------)

·[Last published 5 hours ago](/baby-dfc2547dc387?source=post_page---post_publication_info--556962ec83f7---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow

[![Abhijeet kumawat](https://miro.medium.com/v2/resize:fill:96:96/1*lwXXZkQ5xsjHJniXHn-9Tw.jpeg)](https://medium.com/%40kumawatabhijeet2002?source=post_page---post_author_info--556962ec83f7---------------------------------------)

[![Abhijeet kumawat](https://miro.medium.com/v2/resize:fill:128:128/1*lwXXZkQ5xsjHJniXHn-9Tw.jpeg)](https://medium.com/%40kumawatabhijeet2002?source=post_page---post_author_info--556962ec83f7---------------------------------------)

[## Written by Abhijeet kumawat](https://medium.com/%40kumawatabhijeet2002?source=post_page---post_author_info--556962ec83f7---------------------------------------)

[2.4K followers](https://medium.com/%40kumawatabhijeet2002/followers?source=post_page---post_author_info--556962ec83f7---------------------------------------)

·[33 following](https://medium.com/%40kumawatabhijeet2002/following?source=post_page---post_author_info--556962ec83f7---------------------------------------)

Radhe Radhe ✨ || Security Researcher || Bug Hunter || Web Application Penetration Tester || Ethical Hacker ||

## No responses yet

[Help](https://help.medium.com/hc/en-us?source=post_page-----556962ec83f7---------------------------------------)

[Status](https://status.medium.com/?source=post_page-----556962ec83f7---------------------------------------)

[About](https://medium.com/about?autoplay=1&source=post_page-----556962ec83f7---------------------------------------)

[Careers](https://medium.com/jobs-at-medium/work-at-medium-959d1a85284e?source=post_page-----556962ec83f7---------------------------------------)

Press

[Blog](https://blog.medium.com/?source=post_page-----556962ec83f7---------------------------------------)

[Privacy](https://policy.medium.com/medium-privacy-policy-f03bf92035c9?source=post_page-----556962ec83f7---------------------------------------)

[Rules](https://policy.medium.com/medium-rules-30e5502c4eb4?source=post_page-----556962ec83f7---------------------------------------)

[Terms](https://policy.medium.com/medium-terms-of-service-9db0094a1e0f?source=post_page-----556962ec83f7---------------------------------------)

[Text to speech](https://speechify.com/medium?source=post_page-----556962ec83f7---------------------------------------)