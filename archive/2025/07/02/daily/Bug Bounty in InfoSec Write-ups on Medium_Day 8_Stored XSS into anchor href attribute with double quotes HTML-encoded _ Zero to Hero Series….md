---
title: Day 8:Stored XSS into anchor href attribute with double quotes HTML-encoded : Zero to Hero Series…
url: https://infosecwriteups.com/day-8-stored-xss-into-anchor-href-attribute-with-double-quotes-html-encoded-zero-to-hero-series-f4bcab7d9b8f?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2025-07-02
fetch_date: 2025-10-06T23:50:30.672520
---

# Day 8:Stored XSS into anchor href attribute with double quotes HTML-encoded : Zero to Hero Series…

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2Ff4bcab7d9b8f&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fday-8-stored-xss-into-anchor-href-attribute-with-double-quotes-html-encoded-zero-to-hero-series-f4bcab7d9b8f&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fday-8-stored-xss-into-anchor-href-attribute-with-double-quotes-html-encoded-zero-to-hero-series-f4bcab7d9b8f&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-f4bcab7d9b8f---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-f4bcab7d9b8f---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

# Day 8:Stored XSS into anchor `href` attribute with double quotes HTML-encoded : Zero to Hero Series — Portswigger

[![RayofHope](https://miro.medium.com/v2/resize:fill:64:64/1*pb6R-58-0JIs9DggdPv4MA.jpeg)](https://arayofhope7.medium.com/?source=post_page---byline--f4bcab7d9b8f---------------------------------------)

[RayofHope](https://arayofhope7.medium.com/?source=post_page---byline--f4bcab7d9b8f---------------------------------------)

3 min read

·

Jun 29, 2025

--

Listen

Share

Hi, my fellow hackers. This is **Rayofhope**. I have over 5 years of experience and am currently working as a consultant with a Big 4 firm.

It’s Day 24 of posting all the PortSwigger labs, not just the solutions. I’ll break down ***why*** we take each step, because once the ***‘why’ is clear, the ‘how’ becomes easy.***

**Let’s Start:**

![]()

> ***Video Walkthrough*** *— You can watch the video or read the blog, totally up to you. But if you ask me, start with the video, then read the blog to connect all the dots.*

> **Lab:** This lab contains a stored cross-site scripting vulnerability in the comment functionality. To solve this lab, submit a comment that calls the `alert` function when the comment author name is clicked.

Press enter or click to view image in full size

![]()

*This is what the lab looks like, and we can see that there are no input fields here. However, we have an option to view the post.*

Press enter or click to view image in full size

![]()

*We have an input field to leave a comment. Let’s fill it out with normal details and observe how it responds.*

Press enter or click to view image in full size

![]()

Let’s Submit.

Press enter or click to view image in full size

![]()

Comments have been submitted

Press enter or click to view image in full size

![]()

*The comment has been posted, and we can see a hyperlink in it. Let’s click on ‘RayofHope’ and see where it redirects.*

Press enter or click to view image in full size

![]()

*It redirected to nobody.com. Let’s look at the code to analyze why this happened.*

Press enter or click to view image in full size

![]()

*The application is* ***automatically wrapping the username or comment*** *(*`"RayofHope"`*) in an* `<a>` *tag, and assigning it a* ***default*** `href` ***of*** `https://nobody.com`*, likely as a* ***placeholder*** *or default profile link for anonymous users or non-registered commenters.*

Let’s try injecting javascript:alert(1)

Press enter or click to view image in full size

![]()

*The script has been submitted and the lab is now solved. Let’s go back to the blog to check if any popup appears.*

Press enter or click to view image in full size

![]()

*As expected, clicking on the comment successfully triggered the XSS payload, resulting in a pop-up. Let’s now analyze the code to understand why it was executed.*

In this case, the `href` attribute of the anchor tag is set to a `javascript:` URI scheme. When the user clicks on the link labeled `'ray'`, the browser interprets and executes the embedded JavaScript (`alert(1)`), confirming an XSS vulnerability.

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

[Bug Bounty](https://medium.com/tag/bug-bounty?source=post_page-----f4bcab7d9b8f---------------------------------------)

[Ethical Hacking](https://medium.com/tag/ethical-hacking?source=post_page-----f4bcab7d9b8f---------------------------------------)

[Web Penetration Testing](https://medium.com/tag/web-penetration-testing?source=post_page-----f4bcab7d9b8f---------------------------------------)

[Stored Xss](https://medium.com/tag/stored-xss?source=post_page-----f4bcab7d9b8f---------------------------------------)

[Cyber Security Awareness](https://medium.com/tag/cyber-security-awareness?source=post_page-----f4bcab7d9b8f---------------------------------------)

--

--

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:96:96/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--f4bcab7d9b8f---------------------------------------)

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:128:128/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--f4bcab7d9b8f---------------------------------------)

Follow

[## Published in InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---post_publication_info--f4bcab7d9b8f---------------------------------------)

[71K followers](/followers?source=post_page---post_publication_info--f4bcab7d9b8f---------------------------------------)

·[Last published 3 hours ago](/actuator-unleashed-a-guide-to-finding-and-exploiting-spring-boot-actuator-endpoints-29252dcd9d79?source=post_page---post_publication_info--f4bcab7d9b8f---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow

[![RayofHope](https://miro.medium.com/v2/resize:fill:96:96/1*pb6R-58-0JIs9DggdPv4MA.jpeg)](https://arayofhope7.medium.com/?source=post_page---post_author_info--f4bcab7d9b8f---------------------------------------)

[![RayofHope](https://miro.medium.com/v2/resize:fill:128:128/1*pb6R-58-0JIs9DggdPv4MA.jpeg)](https://arayofhope...