---
title: Strange 2FA Misconfiguration
url: https://infosecwriteups.com/strange-2fa-misconfiguration-ff1d375c447e?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2023-01-14
fetch_date: 2025-10-04T03:52:08.956288
---

# Strange 2FA Misconfiguration

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2Fff1d375c447e&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fstrange-2fa-misconfiguration-ff1d375c447e&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fstrange-2fa-misconfiguration-ff1d375c447e&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-ff1d375c447e---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-ff1d375c447e---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

# **Strange 2FA Misconfiguration**

[![Bharat Singh](https://miro.medium.com/v2/da:true/resize:fill:64:64/1*SLUmV3MPNVcuzAnQFICGyg.gif)](https://bharat-singh.medium.com/?source=post_page---byline--ff1d375c447e---------------------------------------)

[Bharat Singh](https://bharat-singh.medium.com/?source=post_page---byline--ff1d375c447e---------------------------------------)

3 min read

·

Jan 13, 2023

--

Listen

Share

Hey guys I am back again with another interesting bug bounty writeup. In this write-up, I am going to tell you about my recent finding on a VDP. Due to the company’s policy, I can’t reveal the name of the program.
It was a strange 2FA misconfiguration, so without any delay let’s move on to our main story.

Press enter or click to view image in full size

![]()

### Story of the Bug:

I was looking for a newly released VDP (Vulnerability Disclosure Program) through Google Dorking with help of my dork list.

> **NOTE: You guys can get access to that list through my GitHub, link attached below.**
>
> <https://github.com/BH4R4T-SINGH/Bug_Bounty-Google_Dorks/blob/main/Bug%20Bounty%20Google%20Dorks.txt>

I found a good target with many functionalities including 2FA which was perfect to hunt on. After analysing the working of the whole web app manually I started to hunt for bugs. Usually, I begin with password reset and email verification type bugs, but this time I decided to go for 2FA(Two-factor authentication).

To setup 2FA there were two options:

![]()

>Either you can setup using another app. (Google Authenticator, Authy, or Microsoft Authenticator)

>Or you can set up using your Phone number via SMS.

I went for the SMS option, and after that, I entered my Phone Number and received an OTP to set up the 2FA. After entering the OTP I clicked on verify button and intercepted that request.

The request has 3 parameters in the body: Phone Number, Country Code, and Verification type. I tried to change the phone number to another phone number to see how the application will respond.

![]()

It was showing me a 200 OK response also in the 2FA option it was showing my Second phone number (changed phone number).

On the front end, my phone number was changed without any verification but not sure whether it was updated on the backend or not. So I logged out from my account and try to log in again, and to my surprise, I received the 2FA code on my Second Phone number. Also, there was no rate limit on 2FA code request so an attacker can do sms bombing to the victim’s phone number.

**ENDING**

That’s it for this writeup guys, hope u have enjoyed the writeup. Feel free to connect with me, my DM’s are always open for any recommendation or help. See ya all with a new writeup.

**>>>>>>>>>>>>>>>>>>>>>>>>>>>**[**TWITTER**](https://twitter.com/zingzangoo)**<<<<<<<<<<<<<<<<<<<<<<<<<<<**

**>>>>>>>>>>>>>>>>>>>>>>>>>>>**[**LINKEDIN**](https://www.linkedin.com/in/bharat-s1ngh/)**<<<<<<<<<<<<<<<<<<<<<<<<<<**

[Bug Bounty](https://medium.com/tag/bug-bounty?source=post_page-----ff1d375c447e---------------------------------------)

[Hacking](https://medium.com/tag/hacking?source=post_page-----ff1d375c447e---------------------------------------)

[Bug Bounty Tips](https://medium.com/tag/bug-bounty-tips?source=post_page-----ff1d375c447e---------------------------------------)

[Hackerone](https://medium.com/tag/hackerone?source=post_page-----ff1d375c447e---------------------------------------)

--

--

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:96:96/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--ff1d375c447e---------------------------------------)

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:128:128/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--ff1d375c447e---------------------------------------)

Follow

[## Published in InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---post_publication_info--ff1d375c447e---------------------------------------)

[71K followers](/followers?source=post_page---post_publication_info--ff1d375c447e---------------------------------------)

·[Last published 5 days ago](/how-to-find-p1-bugs-using-google-in-your-target-part-1-e37455324dc1?source=post_page---post_publication_info--ff1d375c447e---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow

[![Bharat Singh](https://miro.medium.com/v2/resize:fill:96:96/1*SLUmV3MPNVcuzAnQFICGyg.gif)](https://bharat-singh.medium.com/?source=post_page---post_author_info--ff1d375c447e---------------------------------------)

[![Bharat Singh](https://miro.medium.com/v2/resize:fill:128:128/1*SLUmV3MPNVcuzAnQFICGyg.gif)](https://bharat-singh.medium.com/?source=post_page---post_author_info--ff1d375c447e---------------------------------------)

[## Written by Bharat Singh](https://bharat-singh.medium.com/?source=post_page---post_author_info--ff1d375c447e---------------------------------------)

[356 followers](https://bharat-singh.medium.com/followers?source=post_page---post_author_info--ff1d375c447e---------------------------------------)

·[83 following](https://medium.com/%40bharat-singh/following?source=post_page---post_author_info--ff1d375c447e---------------------------------------)

Cybersecurity enthusiast who plays CTFs and do Bug Bounty for fun. >>>><https://www.linkedin.com/in/bharat-s1ngh/><<<<

## No responses yet

[Help](https://help.medium.com/hc/en-us?source=post_page-----ff1d375c447e---------------------------------------)

[Status](https://status.medium.com/?source=post_page-----ff1d375c447e---------------------------------------)

[About](https://medium.com/about?autoplay=1&source=post_page-----ff1d...