---
title: Recon Isn’t Just Technical — It’s Psychological
url: https://infosecwriteups.com/recon-isnt-just-technical-it-s-psychological-0bc51a58487b?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2026-05-23
fetch_date: 2026-05-24T06:00:48.834487
---

# Recon Isn’t Just Technical — It’s Psychological

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://play.google.com/store/apps/details?id=com.medium.reader&referrer=utm_source%3DmobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Frecon-isnt-just-technical-it-s-psychological-0bc51a58487b&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

Get app

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Frecon-isnt-just-technical-it-s-psychological-0bc51a58487b&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![Unknown user](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-0bc51a58487b---------------------------------------)

·

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-0bc51a58487b---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Member-only story

# Recon Isn’t Just Technical — It’s Psychological 🧠🌑

[![Iski](https://miro.medium.com/v2/resize:fill:64:64/1*PpvkjPQ1lY6aTYHT9kDX5w.png)](https://medium.com/%40iski?source=post_page---byline--0bc51a58487b---------------------------------------)

[Iski](https://medium.com/%40iski?source=post_page---byline--0bc51a58487b---------------------------------------)

7 min read

·

3 days ago

--

[Listen](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2Fplans%3Fdimension%3Dpost_audio_button%26postId%3D0bc51a58487b&operation=register&redirect=https%3A%2F%2Finfosecwriteups.com%2Frecon-isnt-just-technical-it-s-psychological-0bc51a58487b&source=---header_actions--0bc51a58487b---------------------post_audio_button------------------)

Share

Hey there!😁

Free [Link](https://medium.com/%40iski/recon-isnt-just-technical-it-s-psychological-0bc51a58487b?sk=712135b7183f6e76ef9139d56c5c7bb3) 🎈

Press enter or click to view image in full size

![]()

Image by AI

## How I Profiled an Attacker’s Mindset, Poisoned a Cache Layer, and Walked Into Sensitive Internal Data 💀

> Some people stalk Instagram profiles at 2 AM.I stalk forgotten subdomains and misconfigured CDNs.Some people read relationship red flags.I read response headers like they’re breakup texts from DevOps. *😭*

There’s something weirdly personal about recon.

Not because of the targets.
 Not because of the vulnerabilities.

But because after years of hunting bugs, you slowly realize this:

> *Recon isn’t about technology anymore.
>  It’s about understanding how humans think when they build systems.*

And humans?
 Humans are predictable.

Lazy cache rules.
 Forgotten admin panels.
 Temporary testing environments that become “permanent.”
 Developers naming internal APIs `final-v2-new-last-fixed-real-final`.

Yeah. Recon becomes psychology after a while. 🧠

--

--

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:96:96/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--0bc51a58487b---------------------------------------)

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:128:128/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--0bc51a58487b---------------------------------------)

[## Published in InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---post_publication_info--0bc51a58487b---------------------------------------)

[86K followers](/followers?source=post_page---post_publication_info--0bc51a58487b---------------------------------------)

·[Last published 21 hours ago](/auth-mastery-part-1-credential-types-curl-handles-7b10a5b810d2?source=post_page---post_publication_info--0bc51a58487b---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

[![Iski](https://miro.medium.com/v2/resize:fill:96:96/1*PpvkjPQ1lY6aTYHT9kDX5w.png)](https://medium.com/%40iski?source=post_page---post_author_info--0bc51a58487b---------------------------------------)

[![Iski](https://miro.medium.com/v2/resize:fill:128:128/1*PpvkjPQ1lY6aTYHT9kDX5w.png)](https://medium.com/%40iski?source=post_page---post_author_info--0bc51a58487b---------------------------------------)

[## Written by Iski](https://medium.com/%40iski?source=post_page---post_author_info--0bc51a58487b---------------------------------------)

[2.2K followers](https://medium.com/%40iski/followers?source=post_page---post_author_info--0bc51a58487b---------------------------------------)

·[7 following](https://medium.com/%40iski/following?source=post_page---post_author_info--0bc51a58487b---------------------------------------)

Cybersecurity Researcher | Penetration Tester | Bug Bounty Hunter | Web security| Passionate about cyber security, security automation

[Help](https://help.medium.com/hc/en-us?source=post_page-----0bc51a58487b---------------------------------------)

[Status](https://status.medium.com/?source=post_page-----0bc51a58487b---------------------------------------)

[About](https://medium.com/about?autoplay=1&source=post_page-----0bc51a58487b---------------------------------------)

[Careers](https://medium.com/jobs-at-medium/work-at-medium-959d1a85284e?source=post_page-----0bc51a58487b---------------------------------------)

Press

[Blog](https://blog.medium.com/?source=post_page-----0bc51a58487b---------------------------------------)

[Privacy](https://policy.medium.com/medium-privacy-policy-f03bf92035c9?source=post_page-----0bc51a58487b---------------------------------------)

[Rules](https://policy.medium.com/medium-rules-30e5502c4eb4?source=post_page-----0bc51a58487b---------------------------------------)

[Terms](https://policy.medium.com/medium-terms-of-service-9db0094a1e0f?source=post_page-----0bc51a58487b---------------------------------------)

[Text to speech](https://speechify.com/medium?source=post_page-----0bc51a58487b---------------------------------------)