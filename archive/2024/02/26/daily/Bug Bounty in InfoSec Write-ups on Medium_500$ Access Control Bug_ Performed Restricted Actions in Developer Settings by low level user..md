---
title: 500$ Access Control Bug: Performed Restricted Actions in Developer Settings by low level user.
url: https://infosecwriteups.com/500-access-control-bug-performed-restricted-actions-in-developer-settings-by-low-level-user-b4ecaa6d1aa1?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2024-02-26
fetch_date: 2025-10-04T12:05:50.988862
---

# 500$ Access Control Bug: Performed Restricted Actions in Developer Settings by low level user.

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2Fb4ecaa6d1aa1&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2F500-access-control-bug-performed-restricted-actions-in-developer-settings-by-low-level-user-b4ecaa6d1aa1&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2F500-access-control-bug-performed-restricted-actions-in-developer-settings-by-low-level-user-b4ecaa6d1aa1&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[Mastodon](https://me.dm/%40a13h1)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-b4ecaa6d1aa1---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-b4ecaa6d1aa1---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

Member-only story

# 500$ Access Control Bug: Performed Restricted Actions in Developer Settings by low level user.

[![Abhi Sharma](https://miro.medium.com/v2/resize:fill:64:64/1*sBSRPckiQ7rHLIsqREevhw.png)](https://medium.com/%40a13h1?source=post_page---byline--b4ecaa6d1aa1---------------------------------------)

[Abhi Sharma](https://medium.com/%40a13h1?source=post_page---byline--b4ecaa6d1aa1---------------------------------------)

3 min read

·

Jan 6, 2024

--

3

Share

Recently,i found an interesting bug during my testing that enables a supporter to carry out restricted actions within the developer settings, specifically tweaking notifications without proper authorization in an Private Program. This issue sheds light on a loophole where a low-level actor or a restricted supporter can attempt to manipulate the application’s logic.

Press enter or click to view image in full size

![]()

> **Understanding Target**

ExamNote(Virtual Name of BBP) is a comprehensive platform designed to prioritize customer needs by offering an all-in-one solution for modern card issuer processing and program management. It empowers businesses to efficiently build and launch new revenue streams, providing a seamless experience for both businesses and their customers.In this context, the identified bug allowing unauthorized actions in the developer settings poses a potential risk.

> **The Bug**

The bug I discovered in ExamNote a flaw that enables a supporter or low-level actor to perform restricted actions in the developer settings. Specifically, it allows the user to change notifications without the necessary permissions.

This issue becomes significant because a user with lower privileges, like a supporter, can attempt to manipulate the…

--

--

3

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:96:96/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--b4ecaa6d1aa1---------------------------------------)

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:128:128/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--b4ecaa6d1aa1---------------------------------------)

Follow

[## Published in InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---post_publication_info--b4ecaa6d1aa1---------------------------------------)

[71K followers](/followers?source=post_page---post_publication_info--b4ecaa6d1aa1---------------------------------------)

·[Last published 5 days ago](/how-to-find-p1-bugs-using-google-in-your-target-part-1-e37455324dc1?source=post_page---post_publication_info--b4ecaa6d1aa1---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow

[![Abhi Sharma](https://miro.medium.com/v2/resize:fill:96:96/1*sBSRPckiQ7rHLIsqREevhw.png)](https://medium.com/%40a13h1?source=post_page---post_author_info--b4ecaa6d1aa1---------------------------------------)

[![Abhi Sharma](https://miro.medium.com/v2/resize:fill:128:128/1*sBSRPckiQ7rHLIsqREevhw.png)](https://medium.com/%40a13h1?source=post_page---post_author_info--b4ecaa6d1aa1---------------------------------------)

[## Written by Abhi Sharma](https://medium.com/%40a13h1?source=post_page---post_author_info--b4ecaa6d1aa1---------------------------------------)

[1.92K followers](https://medium.com/%40a13h1/followers?source=post_page---post_author_info--b4ecaa6d1aa1---------------------------------------)

·[0 following](https://medium.com/%40a13h1/following?source=post_page---post_author_info--b4ecaa6d1aa1---------------------------------------)

Cybersecurity Consultant | Pentester | Bug Bounty Hunter | ContentWriter 🔗 Connect with me on <https://twitter.com/a13h1_> and <https://www.linkedin.com/in/a13h1/>

## Responses (3)

See all responses

[Help](https://help.medium.com/hc/en-us?source=post_page-----b4ecaa6d1aa1---------------------------------------)

[Status](https://status.medium.com/?source=post_page-----b4ecaa6d1aa1---------------------------------------)

[About](https://medium.com/about?autoplay=1&source=post_page-----b4ecaa6d1aa1---------------------------------------)

[Careers](https://medium.com/jobs-at-medium/work-at-medium-959d1a85284e?source=post_page-----b4ecaa6d1aa1---------------------------------------)

Press

[Blog](https://blog.medium.com/?source=post_page-----b4ecaa6d1aa1---------------------------------------)

[Privacy](https://policy.medium.com/medium-privacy-policy-f03bf92035c9?source=post_page-----b4ecaa6d1aa1---------------------------------------)

[Rules](https://policy.medium.com/medium-rules-30e5502c4eb4?source=post_page-----b4ecaa6d1aa1---------------------------------------)

[Terms](https://policy.medium.com/medium-terms-of-service-9db0094a1e0f?source=post_page-----b4ecaa6d1aa1---------------------------------------)

[Text to speech](https://speechify.com/medium?source=post_page-----b4ecaa6d1aa1---------------------------------------)