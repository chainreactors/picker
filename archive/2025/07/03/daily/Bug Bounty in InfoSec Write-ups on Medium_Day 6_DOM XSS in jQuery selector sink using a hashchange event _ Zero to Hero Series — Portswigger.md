---
title: Day 6:DOM XSS in jQuery selector sink using a hashchange event : Zero to Hero Series — Portswigger
url: https://infosecwriteups.com/day-6-dom-xss-in-jquery-selector-sink-using-a-hashchange-event-zero-to-hero-series-portswigger-f80367168d95?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2025-07-03
fetch_date: 2025-10-06T23:50:50.818577
---

# Day 6:DOM XSS in jQuery selector sink using a hashchange event : Zero to Hero Series — Portswigger

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2Ff80367168d95&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fday-6-dom-xss-in-jquery-selector-sink-using-a-hashchange-event-zero-to-hero-series-portswigger-f80367168d95&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fday-6-dom-xss-in-jquery-selector-sink-using-a-hashchange-event-zero-to-hero-series-portswigger-f80367168d95&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-f80367168d95---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-f80367168d95---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

# Day 6:DOM XSS in jQuery selector sink using a hashchange event : Zero to Hero Series — Portswigger

[![RayofHope](https://miro.medium.com/v2/resize:fill:64:64/1*pb6R-58-0JIs9DggdPv4MA.jpeg)](https://arayofhope7.medium.com/?source=post_page---byline--f80367168d95---------------------------------------)

[RayofHope](https://arayofhope7.medium.com/?source=post_page---byline--f80367168d95---------------------------------------)

3 min read

·

Jun 29, 2025

--

Listen

Share

Hi, my fellow hackers. This is **Rayofhope**. I have over 5 years of experience and am currently working as a consultant with a Big 4 firm.

It’s Day 22 of posting all the PortSwigger labs, not just the solutions. I’ll break down ***why*** we take each step, because once the ***‘why’ is clear, the ‘how’ becomes easy.***

**Let’s Start:**

![]()

**Before you go for this blog, make sure to read the Previous one**<https://arayofhope7.medium.com/day-5-dom-xss-in-jquery-anchor-href-attribute-sink-using-location-search-afc598397e24>

> **Video Walkthrough** — You can watch the video or read the blog, totally up to you. But if you ask me, start with the video, then read the blog to connect all the dots.

> **LAB:** This lab contains a DOM-based cross-site scripting vulnerability on the home page. It uses jQuery’s `$()` selector function to auto-scroll to a given post, whose title is passed via the `location.hash` property.
>
> To solve the lab, deliver an exploit to the victim that calls the `print()` function in their browser.

Press enter or click to view image in full size

![]()

*This is what the lab looks like.*

Press enter or click to view image in full size

![]()

*A* ***hash*** *is the part of the URL that comes* ***after the*** `#` ***symbol****.*

Press enter or click to view image in full size

![]()

*This confirms that the application is vulnerable to* ***DOM-based XSS*** *due to the unsanitized use of* `window.location.hash` *in a* `hashchange` *event listener.*

*We can see that there is an exploit server available. Let’s deliver the payload through it.*

Press enter or click to view image in full size

![]()

*In here, the* `iframe`*'s* `src` *attribute points to the vulnerable page with an empty hash value. When the* `iframe` *is loaded, an XSS payload is appended to the hash, causing the* `hashchange` *event to fire.*

Press enter or click to view image in full size

![]()

***Boom! Lab solved. And hey, if you learned something and didn’t break your brain in the process, that’s a win-win!***

Happy Hunting — Do hit a like and follow for the best content.

![]()

**My Social:**

**My Social:**

LinkedIn: <https://www.linkedin.com/in/ray-of-hope/>

YouTube Channel: [www.youtube.com/@arayofhope7](http://www.youtube.com/%40arayofhope7)

Twitter: <https://x.com/ray_of_hope7>

Instagram: <https://www.instagram.com/a_rayofhope7/>

[Web Penetration Testing](https://medium.com/tag/web-penetration-testing?source=post_page-----f80367168d95---------------------------------------)

[Ethical Hacking](https://medium.com/tag/ethical-hacking?source=post_page-----f80367168d95---------------------------------------)

[Bug Bounty](https://medium.com/tag/bug-bounty?source=post_page-----f80367168d95---------------------------------------)

[Dom Xss](https://medium.com/tag/dom-xss?source=post_page-----f80367168d95---------------------------------------)

[Cyber Security Awareness](https://medium.com/tag/cyber-security-awareness?source=post_page-----f80367168d95---------------------------------------)

--

--

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:96:96/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--f80367168d95---------------------------------------)

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:128:128/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--f80367168d95---------------------------------------)

Follow

[## Published in InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---post_publication_info--f80367168d95---------------------------------------)

[71K followers](/followers?source=post_page---post_publication_info--f80367168d95---------------------------------------)

·[Last published 3 hours ago](/actuator-unleashed-a-guide-to-finding-and-exploiting-spring-boot-actuator-endpoints-29252dcd9d79?source=post_page---post_publication_info--f80367168d95---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow

[![RayofHope](https://miro.medium.com/v2/resize:fill:96:96/1*pb6R-58-0JIs9DggdPv4MA.jpeg)](https://arayofhope7.medium.com/?source=post_page---post_author_info--f80367168d95---------------------------------------)

[![RayofHope](https://miro.medium.com/v2/resize:fill:128:128/1*pb6R-58-0JIs9DggdPv4MA.jpeg)](https://arayofhope7.medium.com/?source=post_page---post_author_info--f80367168d95---------------------------------------)

[## Written by RayofHope](https://arayofhope7.medium.com/?source=post_page---post_author_info--f80367168d95---------------------------------------)

[55 followers](https://arayofhope7.medium.com/followers?source=post_page---post_author_info--f80367168d95---------------------------------------)

·[2 following](https://medium.com/%40arayofhope7/following?source=post_page---post_author_info--f80367168d95---------------------------------------)

Cyber Security Consultant at Big 4. Bug Bounty + Youtuber + GenAI + Red Teamer + VAPT

## No responses yet

[Help](https://help.medium.com/hc/en-us?source=post_page-----f80367168d95-----------------------------...