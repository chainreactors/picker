---
title: The $8,000 Shortcut: Hijacking Microsoft Edge via NTFS Directory Junctions
url: https://infosecwriteups.com/the-8-000-shortcut-hijacking-microsoft-edge-via-ntfs-directory-junctions-087e5fdf8c9d?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2026-09-02
fetch_date: 2026-09-03T06:38:54.857975
---

# The $8,000 Shortcut: Hijacking Microsoft Edge via NTFS Directory Junctions

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://play.google.com/store/apps/details?id=com.medium.reader&referrer=utm_source%3DmobileNavBar&source=---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fthe-8-000-shortcut-hijacking-microsoft-edge-via-ntfs-directory-junctions-087e5fdf8c9d&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=---top_nav_layout_nav-----------------------------------------)

Get app

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fthe-8-000-shortcut-hijacking-microsoft-edge-via-ntfs-directory-junctions-087e5fdf8c9d&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![Unknown user](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-087e5fdf8c9d---------------------------------------)

·

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-087e5fdf8c9d---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Member-only story

[Cybersecurity](https://medium.com/tag/cybersecurity?source=post_page---header_tags--087e5fdf8c9d---------------------------------------)

[Bug Bounty](https://medium.com/tag/bug-bounty?source=post_page---header_tags--087e5fdf8c9d---------------------------------------)

[Infosec](https://medium.com/tag/infosec?source=post_page---header_tags--087e5fdf8c9d---------------------------------------)

[Ethical Hacking](https://medium.com/tag/ethical-hacking?source=post_page---header_tags--087e5fdf8c9d---------------------------------------)

[Microsoft](https://medium.com/tag/microsoft?source=post_page---header_tags--087e5fdf8c9d---------------------------------------)

# 🎯 The $8,000 Shortcut: Hijacking Microsoft Edge via NTFS Directory Junctions

[![Sachin Patil](https://miro.medium.com/v2/resize:fill:64:64/1*lBfsaAFp3OMldQI_lnwrPg.png)](https://medium.com/%40sachinpatilsp?source=post_page---byline--087e5fdf8c9d---------------------------------------)

[Sachin Patil](https://medium.com/%40sachinpatilsp?source=post_page---byline--087e5fdf8c9d---------------------------------------)

4 min read

·

1 day ago

--

[Listen](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2Fplans%3Fdimension%3Dpost_audio_button%26postId%3D087e5fdf8c9d&operation=register&redirect=https%3A%2F%2Finfosecwriteups.com%2Fthe-8-000-shortcut-hijacking-microsoft-edge-via-ntfs-directory-junctions-087e5fdf8c9d&source=---header_actions--087e5fdf8c9d---------------------post_audio_button------------------)

Share

***How a classic Windows filesystem feature turned the Edge browser into a ‘Confused Deputy’.***

Press enter or click to view image in full size

![]()

Over my years defending enterprise architectures, I’ve realized one fundamental truth about cybersecurity: **The most beautiful vulnerabilities don’t always come from broken code. They come from broken assumptions.**

Recently, I was awarded an **$8,000 bounty** and recognized in the **MSRC Hall of Fame (May 2026)** for an Elevation of Privilege (EoP) vulnerability in Microsoft Edge.

I didn’t use a zero-day memory corruption or a complex sandbox escape. Instead, I used a feature that Windows has supported for decades: the humble NTFS Directory Junction. Here is the story of how I tricked Microsoft Edge into doing my dirty work.

## 🔍 The Hunter’s Mindset: Why Look Here?

My recent security research heavily involved directory poisoning and symlink manipulations. That deep dive rewired my brain to constantly question how highly privileged applications interact with local file paths.

I started observing Microsoft Edge’s background routines. Like all modern browsers, Edge runs scheduled cleanup and file-handling tasks. Some of these routines run with elevated privileges to manage system-level…

--

--

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:96:96/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--087e5fdf8c9d---------------------------------------)

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:128:128/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--087e5fdf8c9d---------------------------------------)

[## Published in InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---post_publication_info--087e5fdf8c9d---------------------------------------)

[88K followers](/followers?source=post_page---post_publication_info--087e5fdf8c9d---------------------------------------)

·[Last published 1 day ago](/the-8-000-shortcut-hijacking-microsoft-edge-via-ntfs-directory-junctions-087e5fdf8c9d?source=post_page---post_publication_info--087e5fdf8c9d---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

[![Sachin Patil](https://miro.medium.com/v2/resize:fill:96:96/1*lBfsaAFp3OMldQI_lnwrPg.png)](https://medium.com/%40sachinpatilsp?source=post_page---post_author_info--087e5fdf8c9d---------------------------------------)

[![Sachin Patil](https://miro.medium.com/v2/resize:fill:128:128/1*lBfsaAFp3OMldQI_lnwrPg.png)](https://medium.com/%40sachinpatilsp?source=post_page---post_author_info--087e5fdf8c9d---------------------------------------)

[## Written by Sachin Patil](https://medium.com/%40sachinpatilsp?source=post_page---post_author_info--087e5fdf8c9d---------------------------------------)

[43 followers](https://medium.com/%40sachinpatilsp/followers?source=post_page---post_author_info--087e5fdf8c9d---------------------------------------)

·[447 following](https://medium.com/%40sachinpatilsp/following?source=post_page---post_author_info--087e5fdf8c9d---------------------------------------)

Vulnerability researcher. CVEs in AWS, Axios & npm. Microsoft MSRC Hall of Fame. I write about privilege escalation, patch bypasses & AI-assisted triage.

[Help](https://help.medium.com/hc/en-us?source=post_page-----087e5fdf8c9d---------------------------------------)

[Status](https://status.medium.com/?source=post_page-----087e5fdf8c9d---------------------------------------)

[About](https://medium.com/about?autoplay=1&source=post_page-----087e5fdf8c9d---------------------------------------)

[Careers](https://medium.com/jobs-at-medium/work-at-medium-959d1a85284e?source=post_page-----087e5fdf8c9d---------------------------------------)

Press

[Blog](https://blog.medium.com/?source=post_page-----087e5fdf8c9d---------------------------------------)

[Store](https://medium.com/store)

[Privacy](https://policy.medium.com/medium-privacy-policy-f03bf92035c9?source=post_page-----087e5fdf8c9d---------------------------------------)

[Rules](https://policy.medium.com/medium-rules-30e5502c4eb4?source=post_page-----087e5fdf8c9d---------------------------------------)

[Terms](https://policy.me...