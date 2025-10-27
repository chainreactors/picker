---
title: “$ Unearthing Digital Ghosts: How Deleted GitHub Files Can Make Your Bug Bounty Fortune”
url: https://infosecwriteups.com/unearthing-digital-ghosts-how-deleted-github-files-can-make-your-bug-bounty-fortune-e3335a74a049?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2025-07-20
fetch_date: 2025-10-06T23:28:40.596185
---

# “$ Unearthing Digital Ghosts: How Deleted GitHub Files Can Make Your Bug Bounty Fortune”

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2Fe3335a74a049&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Funearthing-digital-ghosts-how-deleted-github-files-can-make-your-bug-bounty-fortune-e3335a74a049&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Funearthing-digital-ghosts-how-deleted-github-files-can-make-your-bug-bounty-fortune-e3335a74a049&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-e3335a74a049---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-e3335a74a049---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

Member-only story

# “$ Unearthing Digital Ghosts: How Deleted GitHub Files Can Make Your Bug Bounty Fortune”

## The Illusion of “Delete”

[![Aman Sharma](https://miro.medium.com/v2/da:true/resize:fill:64:64/0*gTsmBWudIxLcZoel)](https://amannsharmaa.medium.com/?source=post_page---byline--e3335a74a049---------------------------------------)

[Aman Sharma](https://amannsharmaa.medium.com/?source=post_page---byline--e3335a74a049---------------------------------------)

4 min read

·

Jul 18, 2025

--

Share

I used to believe deleting a GitHub file erased it forever — until I stumbled upon an AWS key in a “vanished” config file during a routine bug hunt. That single discovery paid my rent for two months.

[free link | friend link](https://amannsharmaa.medium.com/unearthing-digital-ghosts-how-deleted-github-files-can-make-your-bug-bounty-fortune-e3335a74a049?sk=3cef92edff4adc6cdd89a2c4b0e344e9)

Press enter or click to view image in full size

![]()

Most developers assume `git rm` is a digital shredder. But Git’s design—meant to preserve history—turns deleted files into buried treasure. As a bug bounty hunter, I’ve found live API keys, cloud credentials, and encryption tokens lingering in "deleted" files across Fortune 500 repos. And most automated scanners? They miss these entirely.

### Why Git Never Forgets (And Why Hackers Love It)

Git’s magic is its curse:

1. Blobs: Every file becomes a compressed blob (`.git/objects`), saved indefinitely.
2. Dangling Blobs: When files are deleted, Git orphans these blobs — untethered from active commits but still retrievable.
3. Pack Files: Git bundles old blobs into pack files to save space. Your “deleted” secrets? Often snug inside.

> “Git’s history is a museum, not a graveyard. What’s ‘gone’ is usually just mislabeled.”

--

--

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:96:96/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--e3335a74a049---------------------------------------)

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:128:128/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--e3335a74a049---------------------------------------)

Follow

[## Published in InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---post_publication_info--e3335a74a049---------------------------------------)

[71K followers](/followers?source=post_page---post_publication_info--e3335a74a049---------------------------------------)

·[Last published 3 hours ago](/actuator-unleashed-a-guide-to-finding-and-exploiting-spring-boot-actuator-endpoints-29252dcd9d79?source=post_page---post_publication_info--e3335a74a049---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow

[![Aman Sharma](https://miro.medium.com/v2/resize:fill:96:96/0*gTsmBWudIxLcZoel)](https://amannsharmaa.medium.com/?source=post_page---post_author_info--e3335a74a049---------------------------------------)

[![Aman Sharma](https://miro.medium.com/v2/resize:fill:128:128/0*gTsmBWudIxLcZoel)](https://amannsharmaa.medium.com/?source=post_page---post_author_info--e3335a74a049---------------------------------------)

[## Written by Aman Sharma](https://amannsharmaa.medium.com/?source=post_page---post_author_info--e3335a74a049---------------------------------------)

[779 followers](https://amannsharmaa.medium.com/followers?source=post_page---post_author_info--e3335a74a049---------------------------------------)

·[14 following](https://medium.com/%40amannsharmaa/following?source=post_page---post_author_info--e3335a74a049---------------------------------------)

| Data Enthusiast | SQL | Python | Power BI | ML | Exploring Cybersecurity & Bug Bounty | Sharing real-world analytics, dashboards & security insights.

## No responses yet

[Help](https://help.medium.com/hc/en-us?source=post_page-----e3335a74a049---------------------------------------)

[Status](https://status.medium.com/?source=post_page-----e3335a74a049---------------------------------------)

[About](https://medium.com/about?autoplay=1&source=post_page-----e3335a74a049---------------------------------------)

[Careers](https://medium.com/jobs-at-medium/work-at-medium-959d1a85284e?source=post_page-----e3335a74a049---------------------------------------)

Press

[Blog](https://blog.medium.com/?source=post_page-----e3335a74a049---------------------------------------)

[Privacy](https://policy.medium.com/medium-privacy-policy-f03bf92035c9?source=post_page-----e3335a74a049---------------------------------------)

[Rules](https://policy.medium.com/medium-rules-30e5502c4eb4?source=post_page-----e3335a74a049---------------------------------------)

[Terms](https://policy.medium.com/medium-terms-of-service-9db0094a1e0f?source=post_page-----e3335a74a049---------------------------------------)

[Text to speech](https://speechify.com/medium?source=post_page-----e3335a74a049---------------------------------------)