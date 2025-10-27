---
title: Bug Hunting 101: How to Find XSS in Unusual Places ️
url: https://infosecwriteups.com/bug-hunting-101-how-to-find-xss-in-unusual-places-%EF%B8%8F-08a132dac4c3?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2025-08-07
fetch_date: 2025-10-07T00:47:50.544840
---

# Bug Hunting 101: How to Find XSS in Unusual Places ️

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2F08a132dac4c3&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fbug-hunting-101-how-to-find-xss-in-unusual-places-%25EF%25B8%258F-08a132dac4c3&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fbug-hunting-101-how-to-find-xss-in-unusual-places-%25EF%25B8%258F-08a132dac4c3&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-08a132dac4c3---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-08a132dac4c3---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

Member-only story

# Bug Hunting 101: How to Find XSS in Unusual Places 🕵️

[![Vipul Sonule](https://miro.medium.com/v2/resize:fill:64:64/1*3BWnARhHAdOwHCGvC440qA.png)](https://medium.com/%40vipulsonule71?source=post_page---byline--08a132dac4c3---------------------------------------)

[Vipul Sonule](https://medium.com/%40vipulsonule71?source=post_page---byline--08a132dac4c3---------------------------------------)

4 min read

·

Aug 6, 2025

--

Share

> **👉** [**Free Link**](https://thehackerslog.substack.com/p/bug-hunting-101-how-to-find-xss-in)

Press enter or click to view image in full size

![]()

Welcome, fellow hacker! 🚀 If you’ve ever chased bounties or simply explored the world of web security, you’ve likely crossed paths with Cross-Site Scripting (XSS). But what if I told you that most researchers miss the **juiciest XSS bugs** because they’re stuck looking in all the *obvious* places?

In this post, we’re going off the beaten path. Let’s explore **unusual locations** where XSS vulnerabilities hide — and learn the tools, techniques, and mindset needed to uncover them. 🧠

## 🎯 What is XSS, Really?

Before we dive deep, let’s quickly recap:

**Cross-Site Scripting (XSS)** is a vulnerability that allows an attacker to inject malicious JavaScript into a web application. When another user loads the affected page, the script executes in their browser.

Types:

* **Stored XSS**: Script is permanently stored on the server (e.g., in a database).
* **Reflected XSS**: Script is reflected off the server (e.g., in an error message or search result).
* **DOM-based XSS**: The script is injected into the page via client-side JavaScript.

But you knew that, right? 😉 Let’s level up.

## 🔍 Where Everyone Looks…

--

--

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:96:96/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--08a132dac4c3---------------------------------------)

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:128:128/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--08a132dac4c3---------------------------------------)

Follow

[## Published in InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---post_publication_info--08a132dac4c3---------------------------------------)

[71K followers](/followers?source=post_page---post_publication_info--08a132dac4c3---------------------------------------)

·[Last published 4 hours ago](/actuator-unleashed-a-guide-to-finding-and-exploiting-spring-boot-actuator-endpoints-29252dcd9d79?source=post_page---post_publication_info--08a132dac4c3---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow

[![Vipul Sonule](https://miro.medium.com/v2/resize:fill:96:96/1*3BWnARhHAdOwHCGvC440qA.png)](https://medium.com/%40vipulsonule71?source=post_page---post_author_info--08a132dac4c3---------------------------------------)

[![Vipul Sonule](https://miro.medium.com/v2/resize:fill:128:128/1*3BWnARhHAdOwHCGvC440qA.png)](https://medium.com/%40vipulsonule71?source=post_page---post_author_info--08a132dac4c3---------------------------------------)

[## Written by Vipul Sonule](https://medium.com/%40vipulsonule71?source=post_page---post_author_info--08a132dac4c3---------------------------------------)

[2.1K followers](https://medium.com/%40vipulsonule71/followers?source=post_page---post_author_info--08a132dac4c3---------------------------------------)

·[497 following](https://medium.com/%40vipulsonule71/following?source=post_page---post_author_info--08a132dac4c3---------------------------------------)

I’m a cybersecurity enthusiast and bug bounty hunter who loves programming, exploring AI, and sharing tips on hacking, coding, and tech.

## No responses yet

[Help](https://help.medium.com/hc/en-us?source=post_page-----08a132dac4c3---------------------------------------)

[Status](https://status.medium.com/?source=post_page-----08a132dac4c3---------------------------------------)

[About](https://medium.com/about?autoplay=1&source=post_page-----08a132dac4c3---------------------------------------)

[Careers](https://medium.com/jobs-at-medium/work-at-medium-959d1a85284e?source=post_page-----08a132dac4c3---------------------------------------)

Press

[Blog](https://blog.medium.com/?source=post_page-----08a132dac4c3---------------------------------------)

[Privacy](https://policy.medium.com/medium-privacy-policy-f03bf92035c9?source=post_page-----08a132dac4c3---------------------------------------)

[Rules](https://policy.medium.com/medium-rules-30e5502c4eb4?source=post_page-----08a132dac4c3---------------------------------------)

[Terms](https://policy.medium.com/medium-terms-of-service-9db0094a1e0f?source=post_page-----08a132dac4c3---------------------------------------)

[Text to speech](https://speechify.com/medium?source=post_page-----08a132dac4c3---------------------------------------)