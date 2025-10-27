---
title: OTP Leaking Through Cookie Leads to Account Takeover
url: https://infosecwriteups.com/otp-leaking-through-cookie-leads-to-account-takeover-4fb96f255e2f?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2023-01-18
fetch_date: 2025-10-04T04:08:17.597465
---

# OTP Leaking Through Cookie Leads to Account Takeover

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2F4fb96f255e2f&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fotp-leaking-through-cookie-leads-to-account-takeover-4fb96f255e2f&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fotp-leaking-through-cookie-leads-to-account-takeover-4fb96f255e2f&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-4fb96f255e2f---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-4fb96f255e2f---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

# OTP Leaking Through Cookie Leads to Account Takeover

## OTP Bypass

[![ag3n7](https://miro.medium.com/v2/resize:fill:64:64/1*a9R_2jXpqBZkrQ_fVuqzuA.jpeg)](https://ag3n7.medium.com/?source=post_page---byline--4fb96f255e2f---------------------------------------)

[ag3n7](https://ag3n7.medium.com/?source=post_page---byline--4fb96f255e2f---------------------------------------)

3 min read

·

Dec 5, 2022

--

2

Listen

Share

Press enter or click to view image in full size

![]()

[leakage](https://smilyhomes.com/wp-content/uploads/2022/04/roof-leakage.jpeg)

Hello Hackers,

This time I am going to discuss an OTP leaking vulnerability that leads to account takeover in an e-commerce website.

Let’s Start

> What is OTP?
> A one-time password, also known as a one-time PIN, one-time authorization code or dynamic password, is a password that is valid for only one login session or transaction, on a computer system or other digital device
> (source: [wikipedia](https://en.wikipedia.org/wiki/One-time_password))

While searching for a bug bounty program on google, I got an e-commerce website. I started to check the website’s register and login page, I intercepted the requests and started searching for any sensitive data but I didn’t find anything.

After I registered an account and while trying to login, then I figured out the interesting thing on that website. I should have found the vulnerability in the register page itself.

Let’s Discuss it

After Registration, there were two options to login: with the password or with OTP

![]()

Login Page

I used Login with OTP, entered the registered number, and clicked LOGIN WITH OTP

![]()

Validate OTP

Then I checked the cookies, there is a new cookie appeared ‘otpcookies’ with the OTP value.

![]()

otp

I entered the OTP and validated it.

![]()

Successfully LoggedIn

We successfully loggedin to the account.

We can takeover any account by knowing their mobile number only. We can use the same method to register the account, and the most interesting part was there was no validation of mobile number and email id, which means we can register even with non-existing numbers and emails. These all happened on an e-commerce website :(

I reported the issue to the admin and they responded within hours, and accepted the bug. After that no response from their side and no updates till now. Let’s wait.

Thank You For Reading ….

## Follow me on :

Twitter: <https://twitter.com/ag3n7apk>

Linkedin: <https://www.linkedin.com/in/abhijith-pk-ag3n7/>

[Bug Bounty](https://medium.com/tag/bug-bounty?source=post_page-----4fb96f255e2f---------------------------------------)

[Otp Bypass](https://medium.com/tag/otp-bypass?source=post_page-----4fb96f255e2f---------------------------------------)

[Hacking](https://medium.com/tag/hacking?source=post_page-----4fb96f255e2f---------------------------------------)

[Ecommerce](https://medium.com/tag/ecommerce?source=post_page-----4fb96f255e2f---------------------------------------)

[Cookies](https://medium.com/tag/cookies?source=post_page-----4fb96f255e2f---------------------------------------)

--

--

2

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:96:96/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--4fb96f255e2f---------------------------------------)

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:128:128/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--4fb96f255e2f---------------------------------------)

Follow

[## Published in InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---post_publication_info--4fb96f255e2f---------------------------------------)

[71K followers](/followers?source=post_page---post_publication_info--4fb96f255e2f---------------------------------------)

·[Last published 5 days ago](/how-to-find-p1-bugs-using-google-in-your-target-part-1-e37455324dc1?source=post_page---post_publication_info--4fb96f255e2f---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow

[![ag3n7](https://miro.medium.com/v2/resize:fill:96:96/1*a9R_2jXpqBZkrQ_fVuqzuA.jpeg)](https://ag3n7.medium.com/?source=post_page---post_author_info--4fb96f255e2f---------------------------------------)

[![ag3n7](https://miro.medium.com/v2/resize:fill:128:128/1*a9R_2jXpqBZkrQ_fVuqzuA.jpeg)](https://ag3n7.medium.com/?source=post_page---post_author_info--4fb96f255e2f---------------------------------------)

[## Written by ag3n7](https://ag3n7.medium.com/?source=post_page---post_author_info--4fb96f255e2f---------------------------------------)

[297 followers](https://ag3n7.medium.com/followers?source=post_page---post_author_info--4fb96f255e2f---------------------------------------)

·[75 following](https://medium.com/%40ag3n7/following?source=post_page---post_author_info--4fb96f255e2f---------------------------------------)

Cyber Security Researcher <https://twitter.com/ag3n7apk>

## Responses (2)

See all responses

[Help](https://help.medium.com/hc/en-us?source=post_page-----4fb96f255e2f---------------------------------------)

[Status](https://status.medium.com/?source=post_page-----4fb96f255e2f---------------------------------------)

[About](https://medium.com/about?autoplay=1&source=post_page-----4fb96f255e2f---------------------------------------)

[Careers](https://medium.com/jobs-at-medium/work-at-medium-959d1a85284e?source=post_page-----4fb96f255e2f---------------------------------------)

Press

[Blog](https://blog.medium.com/?source=post_page-----4fb96f255e2f---------------------------------------)

[Privacy](https://policy.medium.com/medium-privacy-policy-f03bf92035c9?so...