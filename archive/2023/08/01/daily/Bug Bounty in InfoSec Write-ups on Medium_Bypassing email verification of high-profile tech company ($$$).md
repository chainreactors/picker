---
title: Bypassing email verification of high-profile tech company ($$$)
url: https://infosecwriteups.com/bypassing-email-verification-of-high-profile-tech-company-e592cc4a89ce?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2023-08-01
fetch_date: 2025-10-06T17:00:14.618344
---

# Bypassing email verification of high-profile tech company ($$$)

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2Fe592cc4a89ce&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fbypassing-email-verification-of-high-profile-tech-company-e592cc4a89ce&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fbypassing-email-verification-of-high-profile-tech-company-e592cc4a89ce&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-e592cc4a89ce---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-e592cc4a89ce---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

# Bypassing email verification of high-profile tech company ($$$)

[![can1337](https://miro.medium.com/v2/resize:fill:64:64/1*HgWum8hST4CDGwBkdXjy-A.jpeg)](https://canmustdie.medium.com/?source=post_page---byline--e592cc4a89ce---------------------------------------)

[can1337](https://canmustdie.medium.com/?source=post_page---byline--e592cc4a89ce---------------------------------------)

3 min read

·

Jul 29, 2023

--

6

Listen

Share

Hi guys, after almost a year, I thought I should create a new write-up. Today, I’m gonna show you the email verification bypass vulnerability that I found at high-profile tech & software company. So I’ll call that company as “redacted” and let’s get started!

Basically, when you sign up with the redacted company, you have 48 hours to verify your email.

Press enter or click to view image in full size

![]()

(I want you to know that I have censored some tabs with company logo and product name for all images.)

As you can see in this picture, it is a demo intended for limited access by new users. During this time, you can use the application, but after 48 hours have passed, you cannot log in without verifying your email.

Press enter or click to view image in full size

![]()

And when you want to log in after 48 hours, you will see the tab below and you will need to verify your email. Yes, I waited 2 days for this.

When we click the “click to resend” button to continue using the account, we receive an email for email verification. Lemme show you that mail.

Press enter or click to view image in full size

![]()

At this point, I noticed that the token value sent in the mail for verification purposes is the same as the token value in the URL field in the second image.

Take a look at this match, we can also view this token from the Burp Suite interface.

Press enter or click to view image in full size

![]()

![]()

![]()

You can easily see the match in all three images (first and second images for the verification area). This means that even if a user registered with an email that doesn’t have, he/she can use that email unlimitedly.

As a result, users can copy this token value and convert it to the URL format sent for email verification.

Press enter or click to view image in full size

![]()

Demo Steps:
1- Create a new account with admin@redacted.com mail at redacted.com
2- After 48 hours, you need to verify your account. Login to the site and you will see that email verification tab.
3- Copy the token value in URL section of verfication tab and paste here: www.redacted.com/Login/UserEmailConfirm?Token=\*HERE\*

The team accepted and fixed this report as email verification bypass and pre-auth account takeover and rewarded me $$$ bounty.

That’s all for now. Thanks for reading this far and I hope you liked it!

<https://twitter.com/canmustdie>
<https://0xcan1337.github.io/>

[Bug Bounty](https://medium.com/tag/bug-bounty?source=post_page-----e592cc4a89ce---------------------------------------)

[Infosec](https://medium.com/tag/infosec?source=post_page-----e592cc4a89ce---------------------------------------)

[Cybersecurity](https://medium.com/tag/cybersecurity?source=post_page-----e592cc4a89ce---------------------------------------)

--

--

6

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:96:96/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--e592cc4a89ce---------------------------------------)

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:128:128/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--e592cc4a89ce---------------------------------------)

Follow

[## Published in InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---post_publication_info--e592cc4a89ce---------------------------------------)

[71K followers](/followers?source=post_page---post_publication_info--e592cc4a89ce---------------------------------------)

·[Last published 1 hour ago](/baby-dfc2547dc387?source=post_page---post_publication_info--e592cc4a89ce---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow

[![can1337](https://miro.medium.com/v2/resize:fill:96:96/1*HgWum8hST4CDGwBkdXjy-A.jpeg)](https://canmustdie.medium.com/?source=post_page---post_author_info--e592cc4a89ce---------------------------------------)

[![can1337](https://miro.medium.com/v2/resize:fill:128:128/1*HgWum8hST4CDGwBkdXjy-A.jpeg)](https://canmustdie.medium.com/?source=post_page---post_author_info--e592cc4a89ce---------------------------------------)

[## Written by can1337](https://canmustdie.medium.com/?source=post_page---post_author_info--e592cc4a89ce---------------------------------------)

[1.2K followers](https://canmustdie.medium.com/followers?source=post_page---post_author_info--e592cc4a89ce---------------------------------------)

·[85 following](https://medium.com/%40canmustdie/following?source=post_page---post_author_info--e592cc4a89ce---------------------------------------)

application security researcher / part-time bug hunter / [twitter.com/canmustdie](http://twitter.com/canmustdie)

## Responses (6)

See all responses

[Help](https://help.medium.com/hc/en-us?source=post_page-----e592cc4a89ce---------------------------------------)

[Status](https://status.medium.com/?source=post_page-----e592cc4a89ce---------------------------------------)

[About](https://medium.com/about?autoplay=1&source=post_page-----e592cc4a89ce---------------------------------------)

[Careers](https://medium.com/jobs-at-medium/work-at-medium-959d1a85284e?source=post_page-----e592cc4a89ce---------------------------------------)

Press

[Blog](https://blo...