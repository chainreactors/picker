---
title: HOW I FOUND MY FIRST XSS BUG
url: https://infosecwriteups.com/how-i-found-my-first-xss-bug-553225548d29?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2024-12-07
fetch_date: 2025-10-06T19:38:09.230902
---

# HOW I FOUND MY FIRST XSS BUG

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2F553225548d29&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fhow-i-found-my-first-xss-bug-553225548d29&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fhow-i-found-my-first-xss-bug-553225548d29&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-553225548d29---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-553225548d29---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

# HOW I FOUND MY FIRST XSS BUG

[![ZEROSEC](https://miro.medium.com/v2/resize:fill:64:64/1*kcRAs3KDKoSWu6KDXpx1Dw.jpeg)](https://medium.com/%40Zeroo_sec?source=post_page---byline--553225548d29---------------------------------------)

[ZEROSEC](https://medium.com/%40Zeroo_sec?source=post_page---byline--553225548d29---------------------------------------)

2 min read

·

Nov 25, 2024

--

2

Listen

Share

## Introduction:

Let’s start with how I found my first love… oh wait, Zero, snap out of it — you’re daydreaming again! Right, back to reality. Sorry, I meant to say, how I found my first XSS! Fellow hackers, buckle up because this is a story packed with curiosity, chaos, and that unforgettable adrenaline rush when a simple pop-up alert feels like winning a boss fight. If you’re just starting your hacking journey, don’t sweat it — XSS is a beginner-friendly challenge, and I’m here to walk you through how I tackled mine. Let’s dive in!

## How I Found It

It all started with a classic **Google Dork**:

> **site:radicated.com**

After scrolling through a few pages, I thought, *let’s refine this a bit*. So, I switched it up:

> **site:radicated.\***

Still not quite there, I decided to get clever and filter out unnecessary subdomains:

> site:radicated.\* -www -blog

This nifty trick removes the **www** and **blog** subdomain pages, making the search results much cleaner. That’s when I stumbled upon a **webpage with a comment functionality**.

Press enter or click to view image in full size

![]()

Immediately, the thought of XSS popped into my head like a lightbulb in a cartoon.

![]()

I grabbed a simple payload and threw it into the comment box:

> “><img src=x onerror=alert(‘xss’)>

To my surprise, the XSS was **stored**, and it worked! I couldn’t believe my luck. I was just testing, thinking the input would be sanitized. But nope — no sanitization. *Boom*, it worked like a charm.

![]()

For a brief moment, I felt like the king of the world. But then, reality hit me, and I remembered all the cautionary tales of irresponsible hacking. My soaring confidence quickly came back down to earth. I decided to do the right thing — I wrote up a detailed report and submitted it to the company.

![]()

## Connect With Me:

If you enjoyed this write-up and want to stay connected, feel free to follow me on [**LinkedIn**](https://www.linkedin.com/in/ranjan-yadav-82b28b249/) and [**X (formerly Twitter)**](https://x.com/ig_ftw). Let’s grow and learn together — happy hacking! 🎯

[Bug Bounty](https://medium.com/tag/bug-bounty?source=post_page-----553225548d29---------------------------------------)

[Bug Bounty Tips](https://medium.com/tag/bug-bounty-tips?source=post_page-----553225548d29---------------------------------------)

[Hacking](https://medium.com/tag/hacking?source=post_page-----553225548d29---------------------------------------)

[Ethical Hacking](https://medium.com/tag/ethical-hacking?source=post_page-----553225548d29---------------------------------------)

--

--

2

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:96:96/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--553225548d29---------------------------------------)

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:128:128/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--553225548d29---------------------------------------)

Follow

[## Published in InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---post_publication_info--553225548d29---------------------------------------)

[71K followers](/followers?source=post_page---post_publication_info--553225548d29---------------------------------------)

·[Last published 4 hours ago](/baby-dfc2547dc387?source=post_page---post_publication_info--553225548d29---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow

[![ZEROSEC](https://miro.medium.com/v2/resize:fill:96:96/1*kcRAs3KDKoSWu6KDXpx1Dw.jpeg)](https://medium.com/%40Zeroo_sec?source=post_page---post_author_info--553225548d29---------------------------------------)

[![ZEROSEC](https://miro.medium.com/v2/resize:fill:128:128/1*kcRAs3KDKoSWu6KDXpx1Dw.jpeg)](https://medium.com/%40Zeroo_sec?source=post_page---post_author_info--553225548d29---------------------------------------)

[## Written by ZEROSEC](https://medium.com/%40Zeroo_sec?source=post_page---post_author_info--553225548d29---------------------------------------)

[137 followers](https://medium.com/%40Zeroo_sec/followers?source=post_page---post_author_info--553225548d29---------------------------------------)

·[111 following](https://medium.com/%40Zeroo_sec/following?source=post_page---post_author_info--553225548d29---------------------------------------)

Hey there! I’m Ranjan Yadav, but in the hacking world, I go by Zero\_Sec. Bug bounty hunting and security research are my passion

## Responses (2)

See all responses

[Help](https://help.medium.com/hc/en-us?source=post_page-----553225548d29---------------------------------------)

[Status](https://status.medium.com/?source=post_page-----553225548d29---------------------------------------)

[About](https://medium.com/about?autoplay=1&source=post_page-----553225548d29---------------------------------------)

[Careers](https://medium.com/jobs-at-medium/work-at-medium-959d1a85284e?source=post_page-----553225548d29---------------------------------------)

Press

[Blog](https://blog.medium.com/?source=post_page-----553225548d29---------------------------------------)

[Privacy](https://policy.medium.com/medium-privacy-policy-f03bf92035c9?source=post_page-----553225548d29---------------------------------------)

[Rules](https://polic...