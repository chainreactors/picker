---
title: How BAC(Broken Access Control) got me a Pre Account Takeover
url: https://infosecwriteups.com/how-bac-broken-access-control-got-me-a-pre-account-takeover-2481931b7b3a?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2023-07-06
fetch_date: 2025-10-04T11:53:05.162848
---

# How BAC(Broken Access Control) got me a Pre Account Takeover

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2F2481931b7b3a&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fhow-bac-broken-access-control-got-me-a-pre-account-takeover-2481931b7b3a&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fhow-bac-broken-access-control-got-me-a-pre-account-takeover-2481931b7b3a&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-2481931b7b3a---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-2481931b7b3a---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

# **How BAC(Broken Access Control) got me a Pre Account Takeover**

[![Bharat Singh](https://miro.medium.com/v2/da:true/resize:fill:64:64/1*SLUmV3MPNVcuzAnQFICGyg.gif)](https://bharat-singh.medium.com/?source=post_page---byline--2481931b7b3a---------------------------------------)

[Bharat Singh](https://bharat-singh.medium.com/?source=post_page---byline--2481931b7b3a---------------------------------------)

3 min read

·

Jun 27, 2023

--

2

Listen

Share

Press enter or click to view image in full size

![]()

## Introduction:

Hey Hackers!!!

This is a writeup about one of my recent findings on a VDP. I found a Broken Access Control bug which was eventually leading to Pre-Account Takeover. Lets head on to our main story…

## Story of the Bug:

It was a typical, boring and unexciting Saturday, I was looking for something to kill the time. So, I decided to do some bug hunting. With the help of this [Bug Bounty Google Dork list](https://github.com/BH4R4T-SINGH/Bug_Bounty-Google_Dorks) I found a program to test my skills.

When I signed up on the web application, I discovered some interesting features like creating groups and inviting users. As a bug hunter, it felt like stumbling upon a treasure chest of possibilities, I started manually hunting for Vulnerabilities in Password Reset and 2FA Functionality but I got nothing there. So I went for User Manager option to test without wasting any more time.

Next, using a test account called **“attacker@778899gmail.com”** I invited myself to the platform. Then, I explored the User Manager option to see what information I could find.

There we got some basic info about the invited user like name, login, email… Here the **login** field is responsible for **password change**, But I was **not allowed to change the login and email field of the invited user.**

Press enter or click to view image in full size

![]()

Not allowed to change Login and Email

I intercepted the request and attempted to modify the **login parameter,** hoping it would give me **Account Takeover** to the invited user’s account. Unfortunately, my plan didn’t work out as expected. However, I didn’t give up just yet.

So I went to change the **Email address to “victim778899@gmail.com”** by intercepting the request and to my surprize it actually changed the email address of the invited user on the front-end as well as on back-end.

Press enter or click to view image in full size

![]()

Change the email parameter in request body

Press enter or click to view image in full size

![]()

Email Successfully changed

I know this is a Low Severity bug, but this is an intresting find for me, So I couldn’t resist sharing this writeup with all of you.

**Impact:**

This vulnerability can lead to Per Account Takeover of any unregistered user and an attacker can misuse the identity of the victim.

**Timeline:**

25-March-2023 >> Bug Reported

20-June-2023 >> They patched the vulnerability & marked it as **low severity.**

Press enter or click to view image in full size

![]()

Their Response

If you guys like this writeup and learned something valuable then do hit the clap **👏 X 50 times.**

Feel free to connect with me on [Linkedin](https://www.linkedin.com/in/bharat-s1ngh/) and [Twitter](https://twitter.com/zingzangoo).

[Bug Bounty](https://medium.com/tag/bug-bounty?source=post_page-----2481931b7b3a---------------------------------------)

[Infosec](https://medium.com/tag/infosec?source=post_page-----2481931b7b3a---------------------------------------)

[Cybersecurity](https://medium.com/tag/cybersecurity?source=post_page-----2481931b7b3a---------------------------------------)

[Bug Bounty Tips](https://medium.com/tag/bug-bounty-tips?source=post_page-----2481931b7b3a---------------------------------------)

[Hacking](https://medium.com/tag/hacking?source=post_page-----2481931b7b3a---------------------------------------)

--

--

2

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:96:96/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--2481931b7b3a---------------------------------------)

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:128:128/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--2481931b7b3a---------------------------------------)

Follow

[## Published in InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---post_publication_info--2481931b7b3a---------------------------------------)

[71K followers](/followers?source=post_page---post_publication_info--2481931b7b3a---------------------------------------)

·[Last published 5 days ago](/how-to-find-p1-bugs-using-google-in-your-target-part-1-e37455324dc1?source=post_page---post_publication_info--2481931b7b3a---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow

[![Bharat Singh](https://miro.medium.com/v2/resize:fill:96:96/1*SLUmV3MPNVcuzAnQFICGyg.gif)](https://bharat-singh.medium.com/?source=post_page---post_author_info--2481931b7b3a---------------------------------------)

[![Bharat Singh](https://miro.medium.com/v2/resize:fill:128:128/1*SLUmV3MPNVcuzAnQFICGyg.gif)](https://bharat-singh.medium.com/?source=post_page---post_author_info--2481931b7b3a---------------------------------------)

[## Written by Bharat Singh](https://bharat-singh.medium.com/?source=post_page---post_author_info--2481931b7b3a---------------------------------------)

[356 followers](https://bharat-singh.medium.com/followers?source=post_page---post_author_info--2481931b7b3a---------------------------------------)

·[83 following](https://medium.com/%40bharat-singh/following?source=post_page-...