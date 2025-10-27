---
title: How I Earned $650 Using Just Recon: A Bug Hunter’s Success Story
url: https://infosecwriteups.com/how-i-earned-650-using-just-recon-a-bug-hunters-success-story-4d78788e46a5?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2024-11-24
fetch_date: 2025-10-06T19:15:02.127380
---

# How I Earned $650 Using Just Recon: A Bug Hunter’s Success Story

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2F4d78788e46a5&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fhow-i-earned-650-using-just-recon-a-bug-hunters-success-story-4d78788e46a5&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fhow-i-earned-650-using-just-recon-a-bug-hunters-success-story-4d78788e46a5&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[Mastodon](https://me.dm/%40myselfakash20)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-4d78788e46a5---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-4d78788e46a5---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

Member-only story

# How I Earned $650 Using Just Recon: A Bug Hunter’s Success Story

[![Akash Ghosh](https://miro.medium.com/v2/resize:fill:64:64/1*xbttpz6vUW1KE6Wd1M2OEg.png)](https://myselfakash20.medium.com/?source=post_page---byline--4d78788e46a5---------------------------------------)

[Akash Ghosh](https://myselfakash20.medium.com/?source=post_page---byline--4d78788e46a5---------------------------------------)

5 min read

·

Nov 20, 2024

--

2

Share

Press enter or click to view image in full size

![]()

Every hacker dreams of the perfect find — a critical vulnerability hiding in plain sight, waiting to be discovered. For me, that moment came during a routine recon session, when I uncovered a severe **Sensitive Information Leakage** on one of the biggest e-commerce platforms. With nothing more than meticulous recon techniques, I revealed sensitive customer transaction data, exposed access keys, and even credit card-related information stored openly in a GitHub repository. That find earned me **$650** — and a spot in their hall of fame.

But let’s make one thing clear: this wasn’t luck, and it wasn’t a fluke. As any seasoned hacker will tell you, **recon is where the magic happens**. It’s where data you weren’t supposed to see gets unearthed. It’s where bugs most people miss rise to the surface. And it’s where the difference between an average report and a high-impact vulnerability lies.

This is the story of how I used the art of recon to turn scattered digital breadcrumbs into a critical report and a rewarding bounty. Whether you’re a seasoned bug bounty hunter or just getting started, this write-up will show you why recon is the ultimate weapon in a hacker’s arsenal — and how you can master it to uncover your own success stories.

> Why Recon is the Key to Bug Hunting Success

--

--

2

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:96:96/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--4d78788e46a5---------------------------------------)

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:128:128/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--4d78788e46a5---------------------------------------)

Follow

[## Published in InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---post_publication_info--4d78788e46a5---------------------------------------)

[71K followers](/followers?source=post_page---post_publication_info--4d78788e46a5---------------------------------------)

·[Last published 4 hours ago](/baby-dfc2547dc387?source=post_page---post_publication_info--4d78788e46a5---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow

[![Akash Ghosh](https://miro.medium.com/v2/resize:fill:96:96/1*xbttpz6vUW1KE6Wd1M2OEg.png)](https://myselfakash20.medium.com/?source=post_page---post_author_info--4d78788e46a5---------------------------------------)

[![Akash Ghosh](https://miro.medium.com/v2/resize:fill:128:128/1*xbttpz6vUW1KE6Wd1M2OEg.png)](https://myselfakash20.medium.com/?source=post_page---post_author_info--4d78788e46a5---------------------------------------)

[## Written by Akash Ghosh](https://myselfakash20.medium.com/?source=post_page---post_author_info--4d78788e46a5---------------------------------------)

[658 followers](https://myselfakash20.medium.com/followers?source=post_page---post_author_info--4d78788e46a5---------------------------------------)

·[2 following](https://medium.com/%40myselfakash20/following?source=post_page---post_author_info--4d78788e46a5---------------------------------------)

Akash Ghosh|Ethical Hacker | Cybersecurity Expert | Web & Mobile Security Expert

## Responses (2)

See all responses

[Help](https://help.medium.com/hc/en-us?source=post_page-----4d78788e46a5---------------------------------------)

[Status](https://status.medium.com/?source=post_page-----4d78788e46a5---------------------------------------)

[About](https://medium.com/about?autoplay=1&source=post_page-----4d78788e46a5---------------------------------------)

[Careers](https://medium.com/jobs-at-medium/work-at-medium-959d1a85284e?source=post_page-----4d78788e46a5---------------------------------------)

Press

[Blog](https://blog.medium.com/?source=post_page-----4d78788e46a5---------------------------------------)

[Privacy](https://policy.medium.com/medium-privacy-policy-f03bf92035c9?source=post_page-----4d78788e46a5---------------------------------------)

[Rules](https://policy.medium.com/medium-rules-30e5502c4eb4?source=post_page-----4d78788e46a5---------------------------------------)

[Terms](https://policy.medium.com/medium-terms-of-service-9db0094a1e0f?source=post_page-----4d78788e46a5---------------------------------------)

[Text to speech](https://speechify.com/medium?source=post_page-----4d78788e46a5---------------------------------------)