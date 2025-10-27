---
title: From Broken Access Control to First Bounty
url: https://infosecwriteups.com/from-broken-access-control-to-first-bounty-01712b1dab53?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2024-12-26
fetch_date: 2025-10-06T19:37:34.942868
---

# From Broken Access Control to First Bounty

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2F01712b1dab53&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Ffrom-broken-access-control-to-first-bounty-01712b1dab53&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Ffrom-broken-access-control-to-first-bounty-01712b1dab53&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-01712b1dab53---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-01712b1dab53---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

Press enter or click to view image in full size

![]()

# From Broken Access Control to First Resolved Bug

## In the Name of Allah, the Most Beneficent, the Most Merciful. All the praises and thanks be to Allah, the Lord of the ‘Alamin (mankind, jinns and all that exists).

[![callgh0st](https://miro.medium.com/v2/resize:fill:64:64/1*S943nhX0uzpVeh6N-49duw.jpeg)](https://callgh0st.medium.com/?source=post_page---byline--01712b1dab53---------------------------------------)

[callgh0st](https://callgh0st.medium.com/?source=post_page---byline--01712b1dab53---------------------------------------)

3 min read

·

Dec 24, 2024

--

5

Listen

Share

**Alhamdulillah (All Praise Be to Allah).** I hope you’re all doing well. It’s been a while since I posted a write-up. I’ve been so occupied and, honestly, a bit lazy.

In’sha Allah (God willing), in the next couple of months, I’ll be sharing some of the reports I submitted to bug bounty platforms and self-hosted programs. These reports will include cases where I received duplicates, no response, or “not applicable” statuses and, of course, the ones that were resolved.

Let’s get started!

After a few months of receiving P5s and informatives on HackerOne and BugCrowd, a friend introduced me to a self-hosted program. For privacy reasons, I’ll refer to it as **humanity.com** (this is not the program’s actual name).

We decided to collaborate on this program. It’s a service that allows users to track, create, and manage paperless forms and surveys under their own dedicated accounts. The forms can be accessed and utilized from a desktop, Apple, or Android device. Additionally, users can add others to a group or establish a relationship (friend).

I came across a bug allows a user to continue interacting with a shared resource (a form) even after being removed from a group by the user(Admin) who created the group and the form.

## Steps to Reproduce:

**Account Setup:**

> Create three accounts: Gaza, `test1`, and `test2`.
>
> Log in as `Gaza` and add `test1` and `test2` as friends.
>
> Create a group that includes `test1` and `test2`.
>
> Share a form within the group.

**Interaction:**

> Log in as `test1` then open burpsuite to capture your requests and begin adding pictures to the form shared by `Gaza`.

**Simulate Removal:**

> Log in as `Gaza` and remove `test1` from the friend list.
>
> Confirm that `test1` no longer has access to the group or the form shared within it.

**Exploit the Bug:**

> As `test1`, check Burp Suite to for the request made when adding pictures to the form.
>
> Resend the captured request via Burp Suite after being removed from the group.
>
> Observe that the request is successfully processed, and the picture is added to the form despite no longer being part of the group.

### Expected Behavior:

Once a user (test1) is removed from a group, they should no longer be able to interact with any resources (forms, etc.) shared within that group. The system should invalidate any previously captured requests once a user is removed.

### Actual Behavior:

Test1 can still interact with the form by resending previously captured requests even after being removed from the group. Additionally, upon being re-added as a friend, test1 is automatically added back to the old group, potentially leading to unauthorized access to new resources shared in the group.

**Alhamdulillah (All Praise Be to Allah),** the report was accepted and resolved.
The severity was categorized as Low-Medium.

Press enter or click to view image in full size

![]()

I hope you’ve learned a few things from this write-up. Thank you for reading all the way to the end! If you found it helpful, kindly show your support by clapping for this write-up.

> *For any suggestions or Correction, Kindly reach out to me:*
>
> *Twitter —* [*callgh0st*](https://twitter.com/callgh0st)

> Many people of conscience are seeking ways to support Palestinians in Gaza as the genocide continues. Let the world also hear your voice against Israel’s actions. Help the Palestinian people in any way you can, whether through donations, prayers, or other forms of support.

[Bug Bounty](https://medium.com/tag/bug-bounty?source=post_page-----01712b1dab53---------------------------------------)

[Access Control](https://medium.com/tag/access-control?source=post_page-----01712b1dab53---------------------------------------)

[Gaza](https://medium.com/tag/gaza?source=post_page-----01712b1dab53---------------------------------------)

[Palestine](https://medium.com/tag/palestine?source=post_page-----01712b1dab53---------------------------------------)

[Hacking](https://medium.com/tag/hacking?source=post_page-----01712b1dab53---------------------------------------)

--

--

5

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:96:96/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--01712b1dab53---------------------------------------)

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:128:128/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--01712b1dab53---------------------------------------)

Follow

[## Published in InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---post_publication_info--01712b1dab53---------------------------------------)

[71K followers](/followers?source=post_page---post_publication_info--01712b1dab53---------------------------------------)

·[Last published 4 hours ago](/baby-dfc2547dc387?source=post_page---post_publication_info--01712b1dab53---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow

[![callgh0st](https://miro.medium.com/v2/resize:fill:96:96/...