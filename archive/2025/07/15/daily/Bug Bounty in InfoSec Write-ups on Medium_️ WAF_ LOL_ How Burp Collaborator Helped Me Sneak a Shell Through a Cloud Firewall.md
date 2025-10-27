---
title: ️ WAF? LOL: How Burp Collaborator Helped Me Sneak a Shell Through a Cloud Firewall
url: https://infosecwriteups.com/%EF%B8%8F-waf-lol-how-burp-collaborator-helped-me-sneak-a-shell-through-a-cloud-firewall-c537bbf53c05?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2025-07-15
fetch_date: 2025-10-06T23:24:59.656601
---

# ️ WAF? LOL: How Burp Collaborator Helped Me Sneak a Shell Through a Cloud Firewall

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2Fc537bbf53c05&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2F%25EF%25B8%258F-waf-lol-how-burp-collaborator-helped-me-sneak-a-shell-through-a-cloud-firewall-c537bbf53c05&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2F%25EF%25B8%258F-waf-lol-how-burp-collaborator-helped-me-sneak-a-shell-through-a-cloud-firewall-c537bbf53c05&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-c537bbf53c05---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-c537bbf53c05---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

Member-only story

# 🛡️🐚 WAF? LOL: How Burp Collaborator Helped Me Sneak a Shell Through a Cloud Firewall

[![Iski](https://miro.medium.com/v2/resize:fill:64:64/1*PpvkjPQ1lY6aTYHT9kDX5w.png)](https://medium.com/%40iski?source=post_page---byline--c537bbf53c05---------------------------------------)

[Iski](https://medium.com/%40iski?source=post_page---byline--c537bbf53c05---------------------------------------)

4 min read

·

Jul 13, 2025

--

1

Share

Free [Link](https://medium.com/%40iski/%EF%B8%8F-waf-lol-how-burp-collaborator-helped-me-sneak-a-shell-through-a-cloud-firewall-c537bbf53c05?sk=78a43597fabcce7876b809a696483919) 🎈

Hey there!😁

Press enter or click to view image in full size

![]()

Gemini AI

## 🤔 Life Tip #487: If you’re not allowed in through the door… just spoof the delivery guy.

As a bug bounty hunter, I’ve learned two universal truths:

1. Coffee is a protocol.
2. WAFs (Web Application Firewalls) love to pretend they’re smarter than they are.

This is the story of how I gently waved at a WAF, spoofed my way past it, and used **Burp Collaborator** to exfiltrate internal data like a magician pulling secrets from a firewalled hat. 🎩✨

[## 💥 HTTP Parameter Pollution: The Dirty Little Secret That Gave Me Full Backend Access 🧼🛠️

### Free Link🎈

infosecwriteups.com](/http-parameter-pollution-the-dirty-little-secret-that-gave-me-full-backend-access-%EF%B8%8F-f7777c569648?source=post_page-----c537bbf53c05---------------------------------------)

## 🕵️‍♂️ Setting the Scene: The Recon That Started It All

Like every bounty hunter’s morning, mine started with **massive recon** and absolutely no expectation of sleep.

While scanning a **subdomain behind a popular CDN (Cloudflare)**, I noticed something peculiar: a file upload endpoint that…

--

--

1

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:96:96/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--c537bbf53c05---------------------------------------)

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:128:128/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--c537bbf53c05---------------------------------------)

Follow

[## Published in InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---post_publication_info--c537bbf53c05---------------------------------------)

[71K followers](/followers?source=post_page---post_publication_info--c537bbf53c05---------------------------------------)

·[Last published 3 hours ago](/actuator-unleashed-a-guide-to-finding-and-exploiting-spring-boot-actuator-endpoints-29252dcd9d79?source=post_page---post_publication_info--c537bbf53c05---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow

[![Iski](https://miro.medium.com/v2/resize:fill:96:96/1*PpvkjPQ1lY6aTYHT9kDX5w.png)](https://medium.com/%40iski?source=post_page---post_author_info--c537bbf53c05---------------------------------------)

[![Iski](https://miro.medium.com/v2/resize:fill:128:128/1*PpvkjPQ1lY6aTYHT9kDX5w.png)](https://medium.com/%40iski?source=post_page---post_author_info--c537bbf53c05---------------------------------------)

[## Written by Iski](https://medium.com/%40iski?source=post_page---post_author_info--c537bbf53c05---------------------------------------)

[1.8K followers](https://medium.com/%40iski/followers?source=post_page---post_author_info--c537bbf53c05---------------------------------------)

·[7 following](https://medium.com/%40iski/following?source=post_page---post_author_info--c537bbf53c05---------------------------------------)

Cybersecurity Researcher | Penetration Tester | Bug Bounty Hunter | Web security| Passionate about cyber security, security automation

## Responses (1)

See all responses

[Help](https://help.medium.com/hc/en-us?source=post_page-----c537bbf53c05---------------------------------------)

[Status](https://status.medium.com/?source=post_page-----c537bbf53c05---------------------------------------)

[About](https://medium.com/about?autoplay=1&source=post_page-----c537bbf53c05---------------------------------------)

[Careers](https://medium.com/jobs-at-medium/work-at-medium-959d1a85284e?source=post_page-----c537bbf53c05---------------------------------------)

Press

[Blog](https://blog.medium.com/?source=post_page-----c537bbf53c05---------------------------------------)

[Privacy](https://policy.medium.com/medium-privacy-policy-f03bf92035c9?source=post_page-----c537bbf53c05---------------------------------------)

[Rules](https://policy.medium.com/medium-rules-30e5502c4eb4?source=post_page-----c537bbf53c05---------------------------------------)

[Terms](https://policy.medium.com/medium-terms-of-service-9db0094a1e0f?source=post_page-----c537bbf53c05---------------------------------------)

[Text to speech](https://speechify.com/medium?source=post_page-----c537bbf53c05---------------------------------------)