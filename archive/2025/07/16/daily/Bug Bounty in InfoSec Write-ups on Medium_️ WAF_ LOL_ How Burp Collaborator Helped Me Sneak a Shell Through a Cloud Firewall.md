---
title: ️ WAF? LOL: How Burp Collaborator Helped Me Sneak a Shell Through a Cloud Firewall
url: https://infosecwriteups.com/%EF%B8%8F-waf-lol-how-burp-collaborator-helped-me-sneak-a-shell-through-a-cloud-firewall-14d662e47999?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2025-07-16
fetch_date: 2025-10-06T23:50:53.861295
---

# ️ WAF? LOL: How Burp Collaborator Helped Me Sneak a Shell Through a Cloud Firewall

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2F14d662e47999&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2F%25EF%25B8%258F-waf-lol-how-burp-collaborator-helped-me-sneak-a-shell-through-a-cloud-firewall-14d662e47999&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2F%25EF%25B8%258F-waf-lol-how-burp-collaborator-helped-me-sneak-a-shell-through-a-cloud-firewall-14d662e47999&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-14d662e47999---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-14d662e47999---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

Member-only story

# 🛡️🐚 WAF? LOL: How Burp Collaborator Helped Me Sneak a Shell Through a Cloud Firewall

[![Iski](https://miro.medium.com/v2/resize:fill:64:64/1*PpvkjPQ1lY6aTYHT9kDX5w.png)](https://medium.com/%40iski?source=post_page---byline--14d662e47999---------------------------------------)

[Iski](https://medium.com/%40iski?source=post_page---byline--14d662e47999---------------------------------------)

4 min read

·

Jul 15, 2025

--

Share

Free [Link](https://medium.com/%40iski/%EF%B8%8F-waf-lol-how-burp-collaborator-helped-me-sneak-a-shell-through-a-cloud-firewall-14d662e47999?sk=d9654ee4a713eed9215eb8f04e9a6fdb) 🎈

Hey there!😁

Press enter or click to view image in full size

![]()

Gemini AI

> *“They said WAF would protect them. I said… Watch And Fail.”*

**Life was peaceful — until it wasn’t.** My chai turned cold, my Wi-Fi played hide and seek, and my bug bounty dashboard had all zeros. Clearly, the universe was begging me to hack something. So I whispered to my terminal:

`mass_recon --please-give-me-bugs`

…and boom — a wild endpoint appeared. Not just any endpoint, but one that led me straight into a fight with a WAF. 😈

Let’s walk through how I chained cloud recon, header tricks, and some cheeky Burp Collaborator magic to sneak a shell through a shiny cloud firewall and escalate it into a sensitive data leak worth every sleepless night. 💤💰

[## 🚪 Login? Who Needs That? Bypassing OAuth Like a Lazy Hacker on Sunday ☀️🔑

### Free Link🎈

infosecwriteups.com](/login-who-needs-that-bypassing-oauth-like-a-lazy-hacker-on-sunday-%EF%B8%8F-76802cc8025d?source=post_page-----14d662e47999---------------------------------------)

## 🛰️ Phase 1: Reconnaissance — Not Your Average Subdomain Discovery

It all started with a usual recon run:

--

--

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:96:96/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--14d662e47999---------------------------------------)

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:128:128/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--14d662e47999---------------------------------------)

Follow

[## Published in InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---post_publication_info--14d662e47999---------------------------------------)

[71K followers](/followers?source=post_page---post_publication_info--14d662e47999---------------------------------------)

·[Last published 3 hours ago](/actuator-unleashed-a-guide-to-finding-and-exploiting-spring-boot-actuator-endpoints-29252dcd9d79?source=post_page---post_publication_info--14d662e47999---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow

[![Iski](https://miro.medium.com/v2/resize:fill:96:96/1*PpvkjPQ1lY6aTYHT9kDX5w.png)](https://medium.com/%40iski?source=post_page---post_author_info--14d662e47999---------------------------------------)

[![Iski](https://miro.medium.com/v2/resize:fill:128:128/1*PpvkjPQ1lY6aTYHT9kDX5w.png)](https://medium.com/%40iski?source=post_page---post_author_info--14d662e47999---------------------------------------)

[## Written by Iski](https://medium.com/%40iski?source=post_page---post_author_info--14d662e47999---------------------------------------)

[1.8K followers](https://medium.com/%40iski/followers?source=post_page---post_author_info--14d662e47999---------------------------------------)

·[7 following](https://medium.com/%40iski/following?source=post_page---post_author_info--14d662e47999---------------------------------------)

Cybersecurity Researcher | Penetration Tester | Bug Bounty Hunter | Web security| Passionate about cyber security, security automation

## No responses yet

[Help](https://help.medium.com/hc/en-us?source=post_page-----14d662e47999---------------------------------------)

[Status](https://status.medium.com/?source=post_page-----14d662e47999---------------------------------------)

[About](https://medium.com/about?autoplay=1&source=post_page-----14d662e47999---------------------------------------)

[Careers](https://medium.com/jobs-at-medium/work-at-medium-959d1a85284e?source=post_page-----14d662e47999---------------------------------------)

Press

[Blog](https://blog.medium.com/?source=post_page-----14d662e47999---------------------------------------)

[Privacy](https://policy.medium.com/medium-privacy-policy-f03bf92035c9?source=post_page-----14d662e47999---------------------------------------)

[Rules](https://policy.medium.com/medium-rules-30e5502c4eb4?source=post_page-----14d662e47999---------------------------------------)

[Terms](https://policy.medium.com/medium-terms-of-service-9db0094a1e0f?source=post_page-----14d662e47999---------------------------------------)

[Text to speech](https://speechify.com/medium?source=post_page-----14d662e47999---------------------------------------)