---
title: The Cookie Bomb: My First $10K in Bug Bounties
url: https://infosecwriteups.com/the-cookie-bomb-my-first-10k-in-bug-bounties-f86cb22c37fa?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2025-09-02
fetch_date: 2025-10-02T19:30:45.652362
---

# The Cookie Bomb: My First $10K in Bug Bounties

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2Ff86cb22c37fa&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fthe-cookie-bomb-my-first-10k-in-bug-bounties-f86cb22c37fa&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fthe-cookie-bomb-my-first-10k-in-bug-bounties-f86cb22c37fa&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-f86cb22c37fa---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-f86cb22c37fa---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

# The Cookie Bomb: My First $10K in Bug Bounties

[![Arshad Kazmi](https://miro.medium.com/v2/resize:fill:64:64/0*gAjmVBOIzADzdg_U.)](https://medium.com/%40arshadkazmi42?source=post_page---byline--f86cb22c37fa---------------------------------------)

[Arshad Kazmi](https://medium.com/%40arshadkazmi42?source=post_page---byline--f86cb22c37fa---------------------------------------)

3 min read

·

Aug 31, 2025

--

8

Listen

Share

When I started bug bounty hunting in 2019–2020, I came across a vulnerability that was simple to exploit yet surprisingly widespread. I began calling it the **Cookie Bomb** — and it earned me over **$10,000 in my first year.**

## Where It All Started

While reading public HackerOne reports, I saw a bug where a query parameter value was directly written into a cookie. Since cookies are sent back to the server with every request, an attacker could inject an **oversized string** into a cookie, and the victim’s browser would keep sending it in every request.

This led to a **self-DoS** situation:

* The victim’s browser stored the malicious cookie.
* Every request to the backend included that cookie.
* The server hit header size limits → requests failed.
* The victim’s session was essentially bricked until they cleared cookies.

That idea stuck in my mind: *could this be happening on other sites too?*

## Hunting for Query Parameters That Set Cookies

I started experimenting with query parameters that are commonly used for tracking and analytics, like:

* gclid (Google Ads)
* utm\_source, utm\_medium, utm\_campaign (Google Analytics)
* fbclid (Facebook)
* dclid

I used **Wappalyzer** to quickly identify whether a target was using Google or Facebook tracking. Then, I crafted requests with **random 4000-character strings** (around the max size for cookies).

> [https://target.com/?gclid=AAAA...[4000](https://target.com/?gclid=AAAA...%5B4000) chars]…AAAA

On reload, I checked if the string was stored as a cookie.

* Sometimes **one parameter was enough** to trigger the DoS.
* Other times, I had to combine **multiple parameters** (gclid + utm\_campaign, etc.) to push total cookie size over the limit.
* In a few cases, I had to repeat the attack across multiple subdomains in order to set several malicious cookies. Only after combining them did the total cookie size exceed the backend’s header size limit and trigger the DoS.

## The Cookie Bomb Effect

When successful, here’s what happened:

1. Victim clicks the malicious link.
2. Tracking parameter(s) get stored as cookies.
3. Cookies exceed header size limit.
4. All further requests fail with errors like **400 Bad Request** or **414 URI Too Large.**
5. Victim can no longer use the application until they **clear their cookies.**

## A Few rewarded reports

Press enter or click to view image in full size![]()

Press enter or click to view image in full size![]()

Press enter or click to view image in full size![]()

Press enter or click to view image in full size![]()

Press enter or click to view image in full size![]()

Press enter or click to view image in full size![]()

Press enter or click to view image in full size![]()

Press enter or click to view image in full size![]()

Press enter or click to view image in full size![]()

Press enter or click to view image in full size![]()

Press enter or click to view image in full size![]()

Rewards reports on Hackerone and Bugcrowd

[Hackerone](https://medium.com/tag/hackerone?source=post_page-----f86cb22c37fa---------------------------------------)

[Bugcrowd](https://medium.com/tag/bugcrowd?source=post_page-----f86cb22c37fa---------------------------------------)

[Cookies](https://medium.com/tag/cookies?source=post_page-----f86cb22c37fa---------------------------------------)

[Bug Bounty](https://medium.com/tag/bug-bounty?source=post_page-----f86cb22c37fa---------------------------------------)

[Analytics](https://medium.com/tag/analytics?source=post_page-----f86cb22c37fa---------------------------------------)

--

--

8

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:96:96/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--f86cb22c37fa---------------------------------------)

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:128:128/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--f86cb22c37fa---------------------------------------)

Follow

[## Published in InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---post_publication_info--f86cb22c37fa---------------------------------------)

[71K followers](/followers?source=post_page---post_publication_info--f86cb22c37fa---------------------------------------)

·[Last published 4 days ago](/how-to-find-p1-bugs-using-google-in-your-target-part-1-e37455324dc1?source=post_page---post_publication_info--f86cb22c37fa---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow

[![Arshad Kazmi](https://miro.medium.com/v2/resize:fill:96:96/0*gAjmVBOIzADzdg_U.)](https://medium.com/%40arshadkazmi42?source=post_page---post_author_info--f86cb22c37fa---------------------------------------)

[![Arshad Kazmi](https://miro.medium.com/v2/resize:fill:128:128/0*gAjmVBOIzADzdg_U.)](https://medium.com/%40arshadkazmi42?source=post_page---post_author_info--f86cb22c37fa---------------------------------------)

[## Written by Arshad Kazmi](https://medium.com/%40arshadkazmi42?source=post_page---post_author_info--f86cb22c37fa---------------------------------------)

[497 followers](https://medium.com/%40arshadkazmi42/followers?source=post_page---post_author_info--f86cb22c37fa---------------------------------------)

·...