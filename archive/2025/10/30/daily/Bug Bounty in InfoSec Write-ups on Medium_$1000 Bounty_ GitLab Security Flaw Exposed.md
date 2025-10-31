---
title: $1000 Bounty: GitLab Security Flaw Exposed
url: https://infosecwriteups.com/1000-bounty-gitlab-security-flaw-exposed-dd309788abb4?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2025-10-30
fetch_date: 2025-10-31T03:12:47.976102
---

# $1000 Bounty: GitLab Security Flaw Exposed

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2Fdd309788abb4&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2F1000-bounty-gitlab-security-flaw-exposed-dd309788abb4&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2F1000-bounty-gitlab-security-flaw-exposed-dd309788abb4&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-dd309788abb4---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-dd309788abb4---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

Member-only story

# $1000 Bounty: GitLab Security Flaw Exposed

## How a $1000 Bounty Hunt Revealed a GraphQL Type Check Nightmare Allowing Maintainers to Nuke Repositories

[![Monika sharma](https://miro.medium.com/v2/da:true/resize:fill:64:64/0*Tv4b4p5mb6J3IJwD)](https://medium.com/%40commanak46?source=post_page---byline--dd309788abb4---------------------------------------)

[Monika sharma](https://medium.com/%40commanak46?source=post_page---byline--dd309788abb4---------------------------------------)

5 min read

·

18 hours ago

--

Share

Press enter or click to view image in full size

![]()

Hey folks, welcome back to another deep dive into the wild world of bug bounties! Today, we’re unpacking a slick vulnerability report that snagged a cool $1000 bounty on HackerOne. This report ([858671](https://hackerone.com/reports/858671)) shines a spotlight on a sneaky GraphQL flaw in GitLab that let project maintainers users who shouldn’t be able to wipe out entire repositories like they were deleting spam emails.

I’ll break it down step by step: the what, the why, the how-to-reproduce, and the fallout. (Pro tip: GitLab fixed this beast, but understanding it could save your next API from a similar facepalm.)

### The Setup: GitLab’s Permission Puzzle

GitLab is a powerhouse for code collab think GitHub but with more enterprise flair. In a typical project, roles are locked down tight:

* Developer: Can code, review, but no deleting projects.
* Maintainer: Can manage merges, issues, and snippets, but crucially, cannot delete or archive the repository. That’s owner/admin territory.

Enter GraphQL: GitLab’s shiny API for querying and mutating data efficiently. It’s…

--

--

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:96:96/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--dd309788abb4---------------------------------------)

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:128:128/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--dd309788abb4---------------------------------------)

Follow

[## Published in InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---post_publication_info--dd309788abb4---------------------------------------)

[73K followers](/followers?source=post_page---post_publication_info--dd309788abb4---------------------------------------)

·[Last published 18 hours ago](/how-i-hacked-iit-delhi-885a7f810292?source=post_page---post_publication_info--dd309788abb4---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow

[![Monika sharma](https://miro.medium.com/v2/resize:fill:96:96/0*Tv4b4p5mb6J3IJwD)](https://medium.com/%40commanak46?source=post_page---post_author_info--dd309788abb4---------------------------------------)

[![Monika sharma](https://miro.medium.com/v2/resize:fill:128:128/0*Tv4b4p5mb6J3IJwD)](https://medium.com/%40commanak46?source=post_page---post_author_info--dd309788abb4---------------------------------------)

[## Written by Monika sharma](https://medium.com/%40commanak46?source=post_page---post_author_info--dd309788abb4---------------------------------------)

[2K followers](https://medium.com/%40commanak46/followers?source=post_page---post_author_info--dd309788abb4---------------------------------------)

·[7 following](https://medium.com/%40commanak46/following?source=post_page---post_author_info--dd309788abb4---------------------------------------)

## No responses yet

[Help](https://help.medium.com/hc/en-us?source=post_page-----dd309788abb4---------------------------------------)

[Status](https://status.medium.com/?source=post_page-----dd309788abb4---------------------------------------)

[About](https://medium.com/about?autoplay=1&source=post_page-----dd309788abb4---------------------------------------)

[Careers](https://medium.com/jobs-at-medium/work-at-medium-959d1a85284e?source=post_page-----dd309788abb4---------------------------------------)

Press

[Blog](https://blog.medium.com/?source=post_page-----dd309788abb4---------------------------------------)

[Privacy](https://policy.medium.com/medium-privacy-policy-f03bf92035c9?source=post_page-----dd309788abb4---------------------------------------)

[Rules](https://policy.medium.com/medium-rules-30e5502c4eb4?source=post_page-----dd309788abb4---------------------------------------)

[Terms](https://policy.medium.com/medium-terms-of-service-9db0094a1e0f?source=post_page-----dd309788abb4---------------------------------------)

[Text to speech](https://speechify.com/medium?source=post_page-----dd309788abb4---------------------------------------)