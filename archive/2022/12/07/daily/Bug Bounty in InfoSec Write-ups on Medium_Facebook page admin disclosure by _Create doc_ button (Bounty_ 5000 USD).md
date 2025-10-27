---
title: Facebook page admin disclosure by "Create doc" button (Bounty: 5000 USD)
url: https://infosecwriteups.com/facebook-page-admin-disclosure-by-create-doc-button-bounty-5000-usd-2fd1ff615bf8?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2022-12-07
fetch_date: 2025-10-04T00:40:45.593098
---

# Facebook page admin disclosure by "Create doc" button (Bounty: 5000 USD)

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2F2fd1ff615bf8&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Ffacebook-page-admin-disclosure-by-create-doc-button-bounty-5000-usd-2fd1ff615bf8&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Ffacebook-page-admin-disclosure-by-create-doc-button-bounty-5000-usd-2fd1ff615bf8&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-2fd1ff615bf8---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-2fd1ff615bf8---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

# Facebook page admin disclosure by "Create doc" button (Bounty: 5000 USD)

## This issue could have accidentally revealed the identity of the Facebook page admin by the “Create doc” button

[![Shubham Bhamare](https://miro.medium.com/v2/resize:fill:64:64/1*YJZ3Ns7NJ_u8GA9ad3G3-A.png)](https://theshubh77.medium.com/?source=post_page---byline--2fd1ff615bf8---------------------------------------)

[Shubham Bhamare](https://theshubh77.medium.com/?source=post_page---byline--2fd1ff615bf8---------------------------------------)

4 min read

·

Dec 28, 2020

--

5

Listen

Share

Press enter or click to view image in full size

![]()

Hi guys, it's **Shubham Bhamare** again. In this write-up, I'm going to tell you about my 2nd valid bug that I found on Facebook. This issue could have accidentally revealed the identity of the Facebook page admin by the "Create doc" button. This is one of the very special findings for me because the bounty I received for this report was beyond my expectations. 😃

So without wasting time, let's start! 👉

===

**Setup and Scenario:**

1) A Facebook user Sarah is the admin of Sarah's Page.

2) Sarah's Page is linked to Sarah's Group.

3) Sarah hasn't made herself an admin of the group because she doesn't want to disclose her identity.

4) So now it's clear that Sarah's Group has only one admin i.e. Sarah's Page. Sarah is just a member of that group and always acts as a page.

Press enter or click to view image in full size

![]()

===

**Reproduction steps:**

1) Using the Facebook web, acting as Sarah's Page, create a document in Sarah's Group with the "Create doc" button.

Press enter or click to view image in full size

![]()

2) Before publishing that document, uncheck the option "Allow group members to edit this document". So that only the document owners or admins will be able to edit that document.

Press enter or click to view image in full size

![]()

3) Now acting as Sarah's Page, edit and save that document.

![]()

4) Now if we see the version history of this document, there will be the name of Sarah.

Press enter or click to view image in full size

![]()

===

**The logic behind it:**

It was easy for other group members to determine who was the admin of the page as only the document owner or admins were able to edit that document. Though there was the name of Sarah in edit history which was unintended.

===

**Fix and Bypass:**

When the team fixed this issue for the "Create doc" button which was present in the post editor, I found that there was another similar button on the "Files" page which was also vulnerable.

When the team was verifying the second fix, they internally identified 3rd vector that also could be abused.

===

**Bounty:**

5000 USD (This reward covers all three of those vulnerabilities. That's why I like Facebook bug bounty the most. 💙)

Press enter or click to view image in full size

![]()

===

**Timeline:**

> Oct 13, 2018: Report sent
> Oct 17, 2018: Pre-triaged
> Oct 17, 2018: Triaged
> Oct 17, 2018: Sent additional information about another vulnerable "Create doc" button
> Feb 09, 2019: Fixed completely
> Feb 09, 2019: 5000 USD bounty awarded

===

**Takeaway(s):**

1) Don't reveal your findings until you fully believe that there won't be any bypass for it. 😉 Check other endpoints/features too for similar issues.

2) Sometimes you just need logical thinking instead of any advanced tools or knowledge. Because Logic == Magic. 😊

3) Again, if you're new to Facebook bug bounty, try to find logical bugs the most.

===

Thank you for reading! Stay tuned for my next write-up and don't forget to follow me on [**Facebook**](http://facebook.com/theshubh77), [**Twitter**](http://twitter.com/theshubh77), [**Instagram**](http://instagram.com/theshubh77), and [**Medium**](http://theshubh77.medium.com). 😊

===

### From Infosec Writeups: A lot is coming up in the Infosec every day that it’s hard to keep up with. [Join our weekly newsletter](https://weekly.infosecwriteups.com/) to get all the latest Infosec trends in the form of 5 articles, 4 Threads, 3 videos, 2 GitHub Repos and tools, and 1 job alert for FREE!

[Bug Bounty](https://medium.com/tag/bug-bounty?source=post_page-----2fd1ff615bf8---------------------------------------)

[Facebook Bug](https://medium.com/tag/facebook-bug?source=post_page-----2fd1ff615bf8---------------------------------------)

[Facebook Bug Bounty](https://medium.com/tag/facebook-bug-bounty?source=post_page-----2fd1ff615bf8---------------------------------------)

[Cybersecurity](https://medium.com/tag/cybersecurity?source=post_page-----2fd1ff615bf8---------------------------------------)

[Ethical Hacking](https://medium.com/tag/ethical-hacking?source=post_page-----2fd1ff615bf8---------------------------------------)

--

--

5

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:96:96/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--2fd1ff615bf8---------------------------------------)

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:128:128/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--2fd1ff615bf8---------------------------------------)

Follow

[## Published in InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---post_publication_info--2fd1ff615bf8---------------------------------------)

[71K followers](/followers?source=post_page---post_publication_info--2fd1ff615bf8---------------------------------------)

·[Last published 5 days ago](/how-to-find-p1-bugs-using-google-in-your-target-part-1-e37455324dc1?source=post_page---post_publication_info--2fd1ff615bf8---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly n...