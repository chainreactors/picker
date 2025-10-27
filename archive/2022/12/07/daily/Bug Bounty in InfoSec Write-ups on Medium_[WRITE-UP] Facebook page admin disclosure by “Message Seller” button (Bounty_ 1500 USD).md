---
title: [WRITE-UP] Facebook page admin disclosure by “Message Seller” button (Bounty: 1500 USD)
url: https://infosecwriteups.com/facebook-page-admin-disclosure-by-message-seller-button-bounty-1500-usd-caaa2eac4121?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2022-12-07
fetch_date: 2025-10-04T00:40:42.710188
---

# [WRITE-UP] Facebook page admin disclosure by “Message Seller” button (Bounty: 1500 USD)

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2Fcaaa2eac4121&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Ffacebook-page-admin-disclosure-by-message-seller-button-bounty-1500-usd-caaa2eac4121&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Ffacebook-page-admin-disclosure-by-message-seller-button-bounty-1500-usd-caaa2eac4121&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-caaa2eac4121---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-caaa2eac4121---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

# Facebook page admin disclosure by "Message Seller" button (Bounty: 1500 USD)

## This issue could have accidentally revealed the identity of the Facebook page admin under certain circumstances

[![Shubham Bhamare](https://miro.medium.com/v2/resize:fill:64:64/1*YJZ3Ns7NJ_u8GA9ad3G3-A.png)](https://theshubh77.medium.com/?source=post_page---byline--caaa2eac4121---------------------------------------)

[Shubham Bhamare](https://theshubh77.medium.com/?source=post_page---byline--caaa2eac4121---------------------------------------)

3 min read

·

Dec 25, 2020

--

2

Listen

Share

![]()

Hi guys, I’m **Shubham Bhamare** from Maharashtra, India. As I promised in my [previous write-up](https://medium.com/theshubh77/my-first-bug-bounty-write-up-about-my-first-valid-finding-a-very-simple-ato-bug-in-a-target-who-1b8259f531d6), here’s my first Facebook bug bounty write-up. Finally! 😂

I know it’s too late to publish this write-up as this bug was found and rewarded in 2018. I’m extremely sorry for that. Anyways, I’m going to publish all my other findings too in the coming days.

So without wasting time, let's start! 👉

===

**Description:**

This issue could have accidentally revealed the identity of the Facebook page admin under certain circumstances.

On Facebook, page admin’s roles are secret. Disclosing the identity of the page admin may cause a significant privacy issue. In this case, it was possible to disclose the identity of the page admin under certain circumstances.

===

**Setup:**

2 Facebook users i.e. Shubham and John

1 Facebook page i.e. Shubham's Page

1 Facebook group i.e Shubham's Page Group

Platform: [Facebook Web](https://www.facebook.com)

===

**Scenario:**

As mentioned above, there are 2 Facebook users i.e. Shubham and John.

Shubham is the admin of Shubham's Page.

Shubham's Page is linked to Shubham's Page group which is a group for Shopping. Post approval for this group is turned on.

John is a member of said group.

Shubham hasn't made himself an admin of a group because he doesn't want to disclose his identity.

So now that group has only one admin i.e. Shubham's Page.

Shubham is just a member of that group and always acts as a page.

===

**Reproduction steps:**

1) From John's account, create a selling post in the group.

Press enter or click to view image in full size

![]()

2) Post will be sent to admin for approval.

3) Now from Shubham’s account (acting as a page), click on the "Message Seller" button at the bottom of the above unapproved post and send a message.

Press enter or click to view image in full size

![]()

4) Message will be sent from Shubham's personal profile instead of the page, which is unintended.

![]()

===

**The logic behind it:**

It’s easy for John to determine who’s the admin of the page as there’s only one group admin (Shubham’s Page) who can see that unapproved post.

===

**Fix:**

The team fixed this issue by removing the "Message Seller" button when acting as a page.

===

**Bypass:**

I found that fix was incomplete as this issue was still working on old unapproved posts.

===

**Bounty:**

1500 USD

Press enter or click to view image in full size

![]()

===

**Timeline:**

> Sep 09, 2018: Report sent
> Sep 11, 2018: Pre-triaged
> Sep 12, 2018: Triaged
> Oct 13, 2018: Fixed
> Oct 13, 2018: Fix bypassed
> Oct 23, 2018: Fixed completely
> Nov 03, 2018: 1500 USD bounty awarded

===

**Takeaway(s):**

1) If you're new to Facebook bug bounty, try to find logical bugs the most.

2) Always try to find a bypass.

===

Thank you for reading! My next write-up will be about my [**second bug in Facebook (Bounty: 5000 USD)**](https://medium.com/bugbountywriteup/facebook-page-admin-disclosure-by-create-doc-button-bounty-5000-usd-2fd1ff615bf8). So stay tuned and don’t forget to follow me on [**Medium**](http://theshubh77.medium.com). 😊

===

### From Infosec Writeups: A lot is coming up in the Infosec every day that it’s hard to keep up with. [Join our weekly newsletter](https://weekly.infosecwriteups.com/) to get all the latest Infosec trends in the form of 5 articles, 4 Threads, 3 videos, 2 GitHub Repos and tools, and 1 job alert for FREE!

[Bug Bounty](https://medium.com/tag/bug-bounty?source=post_page-----caaa2eac4121---------------------------------------)

[Facebook Bug](https://medium.com/tag/facebook-bug?source=post_page-----caaa2eac4121---------------------------------------)

[Facebook Bug Bounty](https://medium.com/tag/facebook-bug-bounty?source=post_page-----caaa2eac4121---------------------------------------)

[Cybersecurity](https://medium.com/tag/cybersecurity?source=post_page-----caaa2eac4121---------------------------------------)

[Ethical Hacking](https://medium.com/tag/ethical-hacking?source=post_page-----caaa2eac4121---------------------------------------)

--

--

2

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:96:96/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--caaa2eac4121---------------------------------------)

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:128:128/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--caaa2eac4121---------------------------------------)

Follow

[## Published in InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---post_publication_info--caaa2eac4121---------------------------------------)

[71K followers](/followers?source=post_page---post_publication_info--caaa2eac4121---------------------------------------)

·[Last published 5 days ago](/how-to-find-p1-bugs-using-google-in-your-target-part-1-e37455324dc1?source=post_page---post_publication_info--caaa2eac4121---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life e...