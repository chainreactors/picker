---
title: Day 7: Reflected XSS into attribute with angle brackets HTML-encoded: Zero to Hero Series —…
url: https://infosecwriteups.com/day-7-reflected-xss-into-attribute-with-angle-brackets-html-encoded-zero-to-hero-series-8b0c775fc7b5?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2025-07-03
fetch_date: 2025-10-06T23:50:46.996814
---

# Day 7: Reflected XSS into attribute with angle brackets HTML-encoded: Zero to Hero Series —…

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2F8b0c775fc7b5&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fday-7-reflected-xss-into-attribute-with-angle-brackets-html-encoded-zero-to-hero-series-8b0c775fc7b5&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fday-7-reflected-xss-into-attribute-with-angle-brackets-html-encoded-zero-to-hero-series-8b0c775fc7b5&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-8b0c775fc7b5---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-8b0c775fc7b5---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

# Day 7: Reflected XSS into attribute with angle brackets HTML-encoded: Zero to Hero Series — Portswigger

[![RayofHope](https://miro.medium.com/v2/resize:fill:64:64/1*pb6R-58-0JIs9DggdPv4MA.jpeg)](https://arayofhope7.medium.com/?source=post_page---byline--8b0c775fc7b5---------------------------------------)

[RayofHope](https://arayofhope7.medium.com/?source=post_page---byline--8b0c775fc7b5---------------------------------------)

2 min read

·

Jul 2, 2025

--

Listen

Share

Hi, my fellow hackers. This is **Rayofhope**. I have over 5 years of experience and am currently working as a consultant with a Big 4 firm.

It’s Day 23 of posting all the PortSwigger labs, not just the solutions. I’ll break down ***why*** we take each step, because once the ***‘why’ is clear, the ‘how’ becomes easy.***

**Let’s Start:**

![]()

> **Video Walkthrough** — You can watch the video or read the blog, totally up to you. But if you ask me, start with the video, then read the blog to connect all the dots.

*This is what the lab looks like: we have a search function field.*

Press enter or click to view image in full size

![]()

Let's search for rayofhope

Press enter or click to view image in full size

![]()

*The value of* `search` *is taken directly from user input (*`?search=...`*) and inserted into the* `value="..."` *field without escaping.*

Let's try to use a script.

Press enter or click to view image in full size

![]()

Here, the payload (“) breaks out of an existing attribute and injects a new attribute (`onmouseover`).

***Boom! Lab solved. And hey, if you learned something and didn’t break your brain in the process, that’s a win-win!***

Happy Hunting — Do hit a like and follow for the best content.

![]()

**My Social:**

LinkedIn: <https://www.linkedin.com/in/ray-of-hope/>

YouTube Channel: [www.youtube.com/@arayofhope7](http://www.youtube.com/%40arayofhope7)

Twitter: <https://x.com/ray_of_hope7>

Instagram: <https://www.instagram.com/a_rayofhope7/>

[Bug Bounty](https://medium.com/tag/bug-bounty?source=post_page-----8b0c775fc7b5---------------------------------------)

[Ethical Hacking](https://medium.com/tag/ethical-hacking?source=post_page-----8b0c775fc7b5---------------------------------------)

[Web Penetration Testing](https://medium.com/tag/web-penetration-testing?source=post_page-----8b0c775fc7b5---------------------------------------)

[Cyber Security Awareness](https://medium.com/tag/cyber-security-awareness?source=post_page-----8b0c775fc7b5---------------------------------------)

[Reflected Xss](https://medium.com/tag/reflected-xss?source=post_page-----8b0c775fc7b5---------------------------------------)

--

--

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:96:96/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--8b0c775fc7b5---------------------------------------)

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:128:128/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--8b0c775fc7b5---------------------------------------)

Follow

[## Published in InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---post_publication_info--8b0c775fc7b5---------------------------------------)

[71K followers](/followers?source=post_page---post_publication_info--8b0c775fc7b5---------------------------------------)

·[Last published 3 hours ago](/actuator-unleashed-a-guide-to-finding-and-exploiting-spring-boot-actuator-endpoints-29252dcd9d79?source=post_page---post_publication_info--8b0c775fc7b5---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow

[![RayofHope](https://miro.medium.com/v2/resize:fill:96:96/1*pb6R-58-0JIs9DggdPv4MA.jpeg)](https://arayofhope7.medium.com/?source=post_page---post_author_info--8b0c775fc7b5---------------------------------------)

[![RayofHope](https://miro.medium.com/v2/resize:fill:128:128/1*pb6R-58-0JIs9DggdPv4MA.jpeg)](https://arayofhope7.medium.com/?source=post_page---post_author_info--8b0c775fc7b5---------------------------------------)

[## Written by RayofHope](https://arayofhope7.medium.com/?source=post_page---post_author_info--8b0c775fc7b5---------------------------------------)

[55 followers](https://arayofhope7.medium.com/followers?source=post_page---post_author_info--8b0c775fc7b5---------------------------------------)

·[2 following](https://medium.com/%40arayofhope7/following?source=post_page---post_author_info--8b0c775fc7b5---------------------------------------)

Cyber Security Consultant at Big 4. Bug Bounty + Youtuber + GenAI + Red Teamer + VAPT

## No responses yet

[Help](https://help.medium.com/hc/en-us?source=post_page-----8b0c775fc7b5---------------------------------------)

[Status](https://status.medium.com/?source=post_page-----8b0c775fc7b5---------------------------------------)

[About](https://medium.com/about?autoplay=1&source=post_page-----8b0c775fc7b5---------------------------------------)

[Careers](https://medium.com/jobs-at-medium/work-at-medium-959d1a85284e?source=post_page-----8b0c775fc7b5---------------------------------------)

Press

[Blog](https://blog.medium.com/?source=post_page-----8b0c775fc7b5---------------------------------------)

[Privacy](https://policy.medium.com/medium-privacy-policy-f03bf92035c9?source=post_page-----8b0c775fc7b5---------------------------------------)

[Rules](https://policy.medium.com/medium-rules-30e5502c4eb4?source=post_page-----8b0c775fc7b5---------------------------------------)

[Terms](https://policy.medium.com/medium-terms-of-service-9db0094a1e0f?source=post_page-----...