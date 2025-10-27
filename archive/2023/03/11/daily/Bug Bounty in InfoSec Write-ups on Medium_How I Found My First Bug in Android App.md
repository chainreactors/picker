---
title: How I Found My First Bug in Android App
url: https://infosecwriteups.com/how-i-found-my-first-bug-in-android-41153093ba57?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2023-03-11
fetch_date: 2025-10-04T09:13:42.747978
---

# How I Found My First Bug in Android App

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2F41153093ba57&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fhow-i-found-my-first-bug-in-android-41153093ba57&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fhow-i-found-my-first-bug-in-android-41153093ba57&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-41153093ba57---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-41153093ba57---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

# How I Found My First Bug in Android App

## Bypass the Password and Biometrics Functionalities

[![Barath Stalin](https://miro.medium.com/v2/da:true/resize:fill:64:64/0*QSoMFmFJzk2KtF7d)](https://medium.com/%40severustalin?source=post_page---byline--41153093ba57---------------------------------------)

[Barath Stalin](https://medium.com/%40severustalin?source=post_page---byline--41153093ba57---------------------------------------)

2 min read

·

Jan 26, 2023

--

2

Listen

Share

Press enter or click to view image in full size

![]()

Photo by [Lukenn Sabellano](https://unsplash.com/%40luferlex?utm_source=medium&utm_medium=referral) on [Unsplash](https://unsplash.com/?utm_source=medium&utm_medium=referral)

***A simple story about me***

*Learned about web application testing online during the COVID-19 period. Did testing on multiple web apps but if I reported any bugs it may informational and duplicates. Then I was curious about android app development so I learned about developing apps. Then I could able to find security issues in android apps. It is like low-hanging fruit — bugs*

**Analyzing**

I used an app for 2FA to get TOTP. Little curious about the applock function so I decompiled the app using JADX-GUI(a tool to decompile the apk) and saw the Androidmanifest.xml file to get the details of the app. [com.demo.app.HandleRedirectionActivity] is exported=true(means any app can call this activity ) so read the code of the activity it doesn’t have anything to read it is just redirection\_handler activity. Jumped into app\_lock [com.demo.app.PinLock while analyzing the code I get to know it doesn’t validate the activity call.

**Exploiting**

Then I call the redirection activity directly using ADB. Haa!! app lock activity doesn’t authenticate the redirection\_handler activity.

*$ adb shell am start -n* *com.demo.app/.HandleRedirectionActivity*

**Creating POC**

Most of the VDP programs don’t allow to use of the ADB. So I Created an Android Application in Android Studio.

> *intent intent = new Intent();*
>
> *intent.setClassName(“com.demo.app”, “com.demo.app.HandleRedirectionActivity”);*
>
> *startActivity(intent);*

Just Create an app to call the redirection\_handler activity, when you open the attacker app it bypassed the biometric entry into the TOTP activity

***LinkedIn profile:*** [*Barath Stalin*](https://www.linkedin.com/in/barathstalin/)

[Android](https://medium.com/tag/android?source=post_page-----41153093ba57---------------------------------------)

[Bug Bounty](https://medium.com/tag/bug-bounty?source=post_page-----41153093ba57---------------------------------------)

[Information Security](https://medium.com/tag/information-security?source=post_page-----41153093ba57---------------------------------------)

[Cybersecurity](https://medium.com/tag/cybersecurity?source=post_page-----41153093ba57---------------------------------------)

[Pentesting](https://medium.com/tag/pentesting?source=post_page-----41153093ba57---------------------------------------)

--

--

2

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:96:96/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--41153093ba57---------------------------------------)

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:128:128/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--41153093ba57---------------------------------------)

Follow

[## Published in InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---post_publication_info--41153093ba57---------------------------------------)

[71K followers](/followers?source=post_page---post_publication_info--41153093ba57---------------------------------------)

·[Last published 5 days ago](/how-to-find-p1-bugs-using-google-in-your-target-part-1-e37455324dc1?source=post_page---post_publication_info--41153093ba57---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow

[![Barath Stalin](https://miro.medium.com/v2/resize:fill:96:96/0*QSoMFmFJzk2KtF7d)](https://medium.com/%40severustalin?source=post_page---post_author_info--41153093ba57---------------------------------------)

[![Barath Stalin](https://miro.medium.com/v2/resize:fill:128:128/0*QSoMFmFJzk2KtF7d)](https://medium.com/%40severustalin?source=post_page---post_author_info--41153093ba57---------------------------------------)

[## Written by Barath Stalin](https://medium.com/%40severustalin?source=post_page---post_author_info--41153093ba57---------------------------------------)

[61 followers](https://medium.com/%40severustalin/followers?source=post_page---post_author_info--41153093ba57---------------------------------------)

·[3 following](https://medium.com/%40severustalin/following?source=post_page---post_author_info--41153093ba57---------------------------------------)

Security Researcher | Pentester | CTF Player | Blogger

## Responses (2)

See all responses

[Help](https://help.medium.com/hc/en-us?source=post_page-----41153093ba57---------------------------------------)

[Status](https://status.medium.com/?source=post_page-----41153093ba57---------------------------------------)

[About](https://medium.com/about?autoplay=1&source=post_page-----41153093ba57---------------------------------------)

[Careers](https://medium.com/jobs-at-medium/work-at-medium-959d1a85284e?source=post_page-----41153093ba57---------------------------------------)

Press

[Blog](https://blog.medium.com/?source=post_page-----41153093ba57---------------------------------------)

[Privacy](https://policy.medium.com/medium-privacy-policy-f03bf92035c9?source=post_page-----41153093ba57---------------------------------------)

[Rules...