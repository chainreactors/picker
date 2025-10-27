---
title: Hacking My College panel using University Website Like a Pro
url: https://infosecwriteups.com/hacking-my-college-panel-using-university-website-like-a-pro-9dd075133dce?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2024-10-23
fetch_date: 2025-10-06T18:49:56.788822
---

# Hacking My College panel using University Website Like a Pro

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2F9dd075133dce&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fhacking-my-college-panel-using-university-website-like-a-pro-9dd075133dce&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fhacking-my-college-panel-using-university-website-like-a-pro-9dd075133dce&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-9dd075133dce---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-9dd075133dce---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

# Hacking My College Admin Panel For Fun😁

[![Raunak Gupta Aka Biscuit](https://miro.medium.com/v2/resize:fill:64:64/1*8CWlTBYd15lEaEd8vlSztw.jpeg)](https://medium.com/%40RaunakGupta1922?source=post_page---byline--9dd075133dce---------------------------------------)

[Raunak Gupta Aka Biscuit](https://medium.com/%40RaunakGupta1922?source=post_page---byline--9dd075133dce---------------------------------------)

3 min read

·

Aug 26, 2024

--

2

Listen

Share

— — — — — — — — — **Free Article link:** [**Hereeee!!!**](https://medium.com/%40RaunakGupta1922/hacking-my-college-panel-using-university-website-like-a-pro-9dd075133dce?sk=40461e20b80bcdb58aa24a2ce81a6fb3)— — — — — — — — —
Today, I’m excited to share the story of how I successfully gained access to my college panel through a vulnerability in the university’s system.

> All The Sensitive Data is blurred Due To Privacy Reason

Press enter or click to view image in full size

![]()

University Website

A few months ago, I was casually browsing my university’s website to check my second-year computer science results and I notice there two interesting panel first is **University Panel** & second is **College Panel** on my university website, After I saw it I was like why its here widely open because generally such panels are hidden.
I quickly checked University Panel on website I found nothing interesting there, After that I check college Panel and found password reset page

Then I thought why not testing this functionality 😬

Press enter or click to view image in full size

![]()

There was two input fields ***College Login ID*** & ***Password*** I tried some random words like admin, user, teacher and student which didn’t work for me then I directly jump to **Forgot Password** page.

Press enter or click to view image in full size

![]()

on **Forgot Password** page it was asking for **College Code** which was easy for me to find as **College Code** is 4 digit brute-forceable code.

Press enter or click to view image in full size

![]()

After finding correct **College Code** I enter the code on forgot password page and move to the next page which was leaking some sensitive data like User ID (Basically College Login ID) and associated Mobile Number with College. Firstly I enter some default OTP Password like 000000, 999999 and blank OTP which are some times setup by developers to avoid the hassle. It still didn’t work out for me.
Then I enter the wrong OTP and tried to Intercept the request using **BrupSuite** (Which is a Web-App pentesting Tool & works like proxy aswell)

Press enter or click to view image in full size

![]()

and here is the catch HTTP request which is carrying my wrong OTP password have some interesting parameters in it, like

> ***logid=***<contains college login id>
> ***pass=***<OTP Password being leaked here>
> ***smsmobile=***<leaked mobile number associated with college>

and from here I got all the sensitive data which is required me to set a new password for my **College Panel.**

Press enter or click to view image in full size

![]()

Press enter or click to view image in full size

![]()

After entering correct leaked OTP I set new password and got access to College panel like a pro 😎

## Now lets understand the workflow.

```
• Basic Attack Scenario.
1. Visit to University Website
2. Navigate to college panel
3. click on reset password
4. add your university code (which is easly brute-forceable 4 digit code)
5. Intercept the request and check the http request for interesting parameters.
6. Few Paramters are leaking the OTP password
7. Enter the OTP password and then set new password
8. Login with New Password.
9. Boom!! you got access to the College pannel
( which is leaking all college students emails, address, phone number, roll no, etc )
```

## Video POC

[Bugbounty Writeup](https://medium.com/tag/bugbounty-writeup?source=post_page-----9dd075133dce---------------------------------------)

[Hacking](https://medium.com/tag/hacking?source=post_page-----9dd075133dce---------------------------------------)

[Cybersecurity](https://medium.com/tag/cybersecurity?source=post_page-----9dd075133dce---------------------------------------)

[College](https://medium.com/tag/college?source=post_page-----9dd075133dce---------------------------------------)

[Bug Bounty](https://medium.com/tag/bug-bounty?source=post_page-----9dd075133dce---------------------------------------)

--

--

2

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:96:96/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--9dd075133dce---------------------------------------)

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:128:128/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--9dd075133dce---------------------------------------)

Follow

[## Published in InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---post_publication_info--9dd075133dce---------------------------------------)

[71K followers](/followers?source=post_page---post_publication_info--9dd075133dce---------------------------------------)

·[Last published 3 hours ago](/baby-dfc2547dc387?source=post_page---post_publication_info--9dd075133dce---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow

[![Raunak Gupta Aka Biscuit](https://miro.medium.com/v2/resize:fill:96:96/1*8CWlTBYd15lEaEd8vlSztw.jpeg)](https://medium.com/%40RaunakGupta1922?source=post_page---post_author_info--9dd075133dce---------------------------------------)

[![Raunak Gupta Aka Biscuit](https://miro.medium.com/v2/resize:fill:128:128/1*8CWlTBYd15lEaE...