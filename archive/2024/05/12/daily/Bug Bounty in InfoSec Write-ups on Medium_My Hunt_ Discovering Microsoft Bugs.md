---
title: My Hunt: Discovering Microsoft Bugs
url: https://infosecwriteups.com/my-hunt-discovering-microsoft-bugs-f6a9c790bec0?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2024-05-12
fetch_date: 2025-10-06T17:16:15.883115
---

# My Hunt: Discovering Microsoft Bugs

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2Ff6a9c790bec0&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fmy-hunt-discovering-microsoft-bugs-f6a9c790bec0&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fmy-hunt-discovering-microsoft-bugs-f6a9c790bec0&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-f6a9c790bec0---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-f6a9c790bec0---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

Member-only story

# My Hunt: Discovering Microsoft Bugs

[![c0d3x27](https://miro.medium.com/v2/resize:fill:64:64/1*Kj6QOt5K6dTAPyZ9xrbcbA.png)](https://c0d3x27.medium.com/?source=post_page---byline--f6a9c790bec0---------------------------------------)

[c0d3x27](https://c0d3x27.medium.com/?source=post_page---byline--f6a9c790bec0---------------------------------------)

5 min read

·

May 11, 2024

--

2

Share

Navigating the Terrain of Microsoft’s Software: Insights from a Bug Hunter

Press enter or click to view image in full size

![]()

Photo by [Clint Patterson](https://unsplash.com/%40cbpsc1?utm_source=medium&utm_medium=referral) on [Unsplash](https://unsplash.com/?utm_source=medium&utm_medium=referral)

If you’ve been following along, you’ll know that I used to be a bug hunter. However, as exploiting vulnerabilities evolved into a means of exploiting those trying to learn about cybersecurity, I transitioned to the private sector. Make no mistake, whenever I come across an opportunity to report on something juicy or that could earn me some cash for the time invested, I’ll take it. That’s how I recently discovered four bugs.

This was the case with Microsoft. As mentioned earlier, I now do Bug Bounty work but for a monthly paycheck. I have to be honest, it’s disheartening when you uncover issues like **RCE, SQLI, IDORs, PE, SSRF, BOLA,** and more that in a Bug Bounty program could fetch you months’ or years worth of paychecks, but what can you do? For better or for worse, at least it’s consistent even if is not much.

During one of these private engagements, I was granted access to a ***Microsoft SharePoint*** environment. While testing their product, I stumbled upon a **Stored XSS** vulnerability.

### Stored XSS

Press enter or click to view image in full size

![]()

Stored xss

--

--

2

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:96:96/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--f6a9c790bec0---------------------------------------)

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:128:128/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--f6a9c790bec0---------------------------------------)

Follow

[## Published in InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---post_publication_info--f6a9c790bec0---------------------------------------)

[71K followers](/followers?source=post_page---post_publication_info--f6a9c790bec0---------------------------------------)

·[Last published 2 hours ago](/baby-dfc2547dc387?source=post_page---post_publication_info--f6a9c790bec0---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow

[![c0d3x27](https://miro.medium.com/v2/resize:fill:96:96/1*Kj6QOt5K6dTAPyZ9xrbcbA.png)](https://c0d3x27.medium.com/?source=post_page---post_author_info--f6a9c790bec0---------------------------------------)

[![c0d3x27](https://miro.medium.com/v2/resize:fill:128:128/1*Kj6QOt5K6dTAPyZ9xrbcbA.png)](https://c0d3x27.medium.com/?source=post_page---post_author_info--f6a9c790bec0---------------------------------------)

[## Written by c0d3x27](https://c0d3x27.medium.com/?source=post_page---post_author_info--f6a9c790bec0---------------------------------------)

[1.8K followers](https://c0d3x27.medium.com/followers?source=post_page---post_author_info--f6a9c790bec0---------------------------------------)

·[15 following](https://medium.com/%40c0d3x27/following?source=post_page---post_author_info--f6a9c790bec0---------------------------------------)

OSCP || OSWE || eMAPT || CompTIA CYSA+, Sec+, A+, ITF+, CSAP | | 0-day Researcher | | Security Consultant

## Responses (2)

See all responses

[Help](https://help.medium.com/hc/en-us?source=post_page-----f6a9c790bec0---------------------------------------)

[Status](https://status.medium.com/?source=post_page-----f6a9c790bec0---------------------------------------)

[About](https://medium.com/about?autoplay=1&source=post_page-----f6a9c790bec0---------------------------------------)

[Careers](https://medium.com/jobs-at-medium/work-at-medium-959d1a85284e?source=post_page-----f6a9c790bec0---------------------------------------)

Press

[Blog](https://blog.medium.com/?source=post_page-----f6a9c790bec0---------------------------------------)

[Privacy](https://policy.medium.com/medium-privacy-policy-f03bf92035c9?source=post_page-----f6a9c790bec0---------------------------------------)

[Rules](https://policy.medium.com/medium-rules-30e5502c4eb4?source=post_page-----f6a9c790bec0---------------------------------------)

[Terms](https://policy.medium.com/medium-terms-of-service-9db0094a1e0f?source=post_page-----f6a9c790bec0---------------------------------------)

[Text to speech](https://speechify.com/medium?source=post_page-----f6a9c790bec0---------------------------------------)