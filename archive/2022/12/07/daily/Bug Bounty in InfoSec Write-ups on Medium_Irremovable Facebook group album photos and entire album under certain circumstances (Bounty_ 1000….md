---
title: Irremovable Facebook group album photos and entire album under certain circumstances (Bounty: 1000…
url: https://infosecwriteups.com/irremovable-facebook-group-album-photos-and-entire-album-under-certain-circumstances-bounty-1000-b1b2a870b8e0?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2022-12-07
fetch_date: 2025-10-04T00:40:48.506641
---

# Irremovable Facebook group album photos and entire album under certain circumstances (Bounty: 1000…

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2Fb1b2a870b8e0&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Firremovable-facebook-group-album-photos-and-entire-album-under-certain-circumstances-bounty-1000-b1b2a870b8e0&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Firremovable-facebook-group-album-photos-and-entire-album-under-certain-circumstances-bounty-1000-b1b2a870b8e0&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-b1b2a870b8e0---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-b1b2a870b8e0---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

# [WRITE-UP] Irremovable Facebook group album photos and entire album under certain circumstances (Bounty: 1000 USD)

[![Shubham Bhamare](https://miro.medium.com/v2/resize:fill:64:64/1*YJZ3Ns7NJ_u8GA9ad3G3-A.png)](https://theshubh77.medium.com/?source=post_page---byline--b1b2a870b8e0---------------------------------------)

[Shubham Bhamare](https://theshubh77.medium.com/?source=post_page---byline--b1b2a870b8e0---------------------------------------)

4 min read

·

Jan 14, 2021

--

Listen

Share

![]()

Hi guys, it's **Shubham Bhamare** again. In this write-up, I'm going to tell you about one of my very simple Facebook bug which was found accidentally as I wasn't in the mood of testing at that time and was just browsing our business group on Facebook.

Due to this issue, Facebook group admin was unable to delete group album photos as well as entire album under certain circumstances.

So without wasting time, let's start! 👉

===

**Setup and Scenario:**

1) A Facebook group where only a page (ABC) is an admin.

2) An attacker (XYZ) is a Facebook user who's the member of above group.

Platform: [Facebook Web](https://www.facebook.com)

===

**Reproduction steps:**

1) From ABC's perspective, create an album in a group.

![]()

Creating an album in a group

![]()

Album created by ABC

2) From XYZ's perspective, add some photos to above album.

Press enter or click to view image in full size

![]()

Adding photos to the album

Press enter or click to view image in full size

![]()

Photo uploaded by group member (XYZ)

3) Now when ABC will try to delete that photos added by XYZ, there won't have any option to delete them. Even though ABC used other platforms like Android/iOS/Lite app, mobile site to delete that photos, it won't be possible.

Press enter or click to view image in full size

![]()

There's no option to delete a photo uploaded by group member

> **ABC will only be able to delete his/her own photos. Being an admin of the group, he should be able to delete photos added by other group members. But there wasn't have any option at that time when I reported this issue.**

===

**Fix and Bypass:**

Team fixed this issue by adding edit button on photos added by other group members. But when I was verifying the fix, I found that if group admin tried to delete entire album (if it includes photos of other members), he/she won't be able to delete it as it was showing an error message.

Press enter or click to view image in full size

![]()

Delete Album button

![]()

Showing an error message while deleting entire album

Impact behind this 2nd issue was, if malicious member added thousand of inappropriate photos to album, then group admin won't be able to delete that entire album. He/she'll have to delete every photo one by one.

Also we can imagine what will happen if multiple group members added thousand of inappropriate photos to that album. 😁

===

**Bounty:**

1000 USD (500 USD for initial report and 500 USD for bypassing the fix or for finding 2nd issue)

Press enter or click to view image in full size

![]()

1000 USD bounty awarded by Facebook

===

**Timeline:**

> Apr 21, 2019: Report sent
> Apr 24, 2019: Pre-triaged
> Apr 27, 2019: Triaged
> May 15, 2019: Fixed
> May 16, 2019: Fix bypassed/2nd issue found
> May 17, 2019: Fixed completely
> May 17, 2019: 1000 USD bounty awarded

===

**Takeaway(s):**

1) While browsing something (even though you're not in the mood of hunting), always observe whether something's working as intended or not.

2) Don't reveal your findings until you fully believe that there won't be any bypass for it. 😉 Check another endpoints/features too for similar issues.

3) Sometimes you just need logical thinking instead of any advanced tools or knowledge. Because Logic == Magic. 😊

4) If you're new to Facebook bug bounty, try to find logical bugs the most.

===

Thank you for reading! Stay tuned for my next write-up, and don’t forget to follow me on [**Facebook**](http://facebook.com/theshubh77), [**Twitter**](http://twitter.com/theshubh77), [**LinkedIn,**](https://linkedin.com/in/theshubh77)and[**Instagram**](http://instagram.com/theshubh77)**. 😊**

===

### From Infosec Writeups: A lot is coming up in the Infosec every day that it’s hard to keep up with. [Join our weekly newsletter](https://weekly.infosecwriteups.com/) to get all the latest Infosec trends in the form of 5 articles, 4 Threads, 3 videos, 2 GitHub Repos and tools, and 1 job alert for FREE!

[Bug Bounty](https://medium.com/tag/bug-bounty?source=post_page-----b1b2a870b8e0---------------------------------------)

[Facebook Bug](https://medium.com/tag/facebook-bug?source=post_page-----b1b2a870b8e0---------------------------------------)

[Facebook Bug Bounty](https://medium.com/tag/facebook-bug-bounty?source=post_page-----b1b2a870b8e0---------------------------------------)

[Cybersecurity](https://medium.com/tag/cybersecurity?source=post_page-----b1b2a870b8e0---------------------------------------)

[Ethical Hacking](https://medium.com/tag/ethical-hacking?source=post_page-----b1b2a870b8e0---------------------------------------)

--

--

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:96:96/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--b1b2a870b8e0---------------------------------------)

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:128:128/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--b1b2a870b8e0---------------------------------------)

Follow

[## Published in InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---post_publication_info--b1b2a870b8e0---------------------------------------)

[71K followers](/followers?source=post_page---post_publication_info--b1b2a870b8e0---------------------------------------)

·[L...