---
title: PRE-ACCOUNT TAKEOVER through Oauth misconfiguration on a mailing website
url: https://infosecwriteups.com/pre-account-takeover-through-misconfigured-oauth-on-a-mailing-website-b906a5c118e9?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2024-11-15
fetch_date: 2025-10-06T19:17:46.252461
---

# PRE-ACCOUNT TAKEOVER through Oauth misconfiguration on a mailing website

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2Fb906a5c118e9&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fpre-account-takeover-through-misconfigured-oauth-on-a-mailing-website-b906a5c118e9&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fpre-account-takeover-through-misconfigured-oauth-on-a-mailing-website-b906a5c118e9&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-b906a5c118e9---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-b906a5c118e9---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

Member-only story

# **PRE-ACCOUNT TAKEOVER through Oauth misconfiguration on a mailing website**

[![Harish](https://miro.medium.com/v2/resize:fill:64:64/1*2HOQkqdJuExdRTCM3eSFRA.jpeg)](https://harish45.medium.com/?source=post_page---byline--b906a5c118e9---------------------------------------)

[Harish](https://harish45.medium.com/?source=post_page---byline--b906a5c118e9---------------------------------------)

2 min read

·

Nov 11, 2024

--

2

Share

**About the vulnerability:**

If an application allows users to authenticate with their Gmail address using Google SSO, the system must check if the email has existing account or not. If the Oauth authorization is misconfigured, it is able to create an account with victim’s email without verifying the email. If the victim creates an account with google SSO, this leads to pre-account takeover.

**Introduction:**

The vulnerability is not yet resolved, So let’s call the website as mail.com. The mail.com has two security flaws which leads to pre-account takeover. They are,

1. If an user signup on mail.com, the website gives partial access to the account and redirects the user to the dashboard without verifying the email.
2. There is google Oauth signup option available for the users. The Oauth must check if email address has an existing account on the website. If an account is already exists, it should ask for create new password. But instead of signing up and asking to set the password, the website directly logging into the account without password.

Press enter or click to view image in full size

![]()

**Attack scenario:**

An attacker is creating an account using victim’s email and got partial access. Let’s Consider the victim likes to use the…

--

--

2

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:96:96/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--b906a5c118e9---------------------------------------)

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:128:128/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--b906a5c118e9---------------------------------------)

Follow

[## Published in InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---post_publication_info--b906a5c118e9---------------------------------------)

[71K followers](/followers?source=post_page---post_publication_info--b906a5c118e9---------------------------------------)

·[Last published 4 hours ago](/baby-dfc2547dc387?source=post_page---post_publication_info--b906a5c118e9---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow

[![Harish](https://miro.medium.com/v2/resize:fill:96:96/1*2HOQkqdJuExdRTCM3eSFRA.jpeg)](https://harish45.medium.com/?source=post_page---post_author_info--b906a5c118e9---------------------------------------)

[![Harish](https://miro.medium.com/v2/resize:fill:128:128/1*2HOQkqdJuExdRTCM3eSFRA.jpeg)](https://harish45.medium.com/?source=post_page---post_author_info--b906a5c118e9---------------------------------------)

[## Written by Harish](https://harish45.medium.com/?source=post_page---post_author_info--b906a5c118e9---------------------------------------)

[181 followers](https://harish45.medium.com/followers?source=post_page---post_author_info--b906a5c118e9---------------------------------------)

·[19 following](https://medium.com/%40harish45/following?source=post_page---post_author_info--b906a5c118e9---------------------------------------)

Bug bounty hunter, Cybersecurity researcher, Gamer, Master of Arts in English Literature

## Responses (2)

See all responses

[Help](https://help.medium.com/hc/en-us?source=post_page-----b906a5c118e9---------------------------------------)

[Status](https://status.medium.com/?source=post_page-----b906a5c118e9---------------------------------------)

[About](https://medium.com/about?autoplay=1&source=post_page-----b906a5c118e9---------------------------------------)

[Careers](https://medium.com/jobs-at-medium/work-at-medium-959d1a85284e?source=post_page-----b906a5c118e9---------------------------------------)

Press

[Blog](https://blog.medium.com/?source=post_page-----b906a5c118e9---------------------------------------)

[Privacy](https://policy.medium.com/medium-privacy-policy-f03bf92035c9?source=post_page-----b906a5c118e9---------------------------------------)

[Rules](https://policy.medium.com/medium-rules-30e5502c4eb4?source=post_page-----b906a5c118e9---------------------------------------)

[Terms](https://policy.medium.com/medium-terms-of-service-9db0094a1e0f?source=post_page-----b906a5c118e9---------------------------------------)

[Text to speech](https://speechify.com/medium?source=post_page-----b906a5c118e9---------------------------------------)