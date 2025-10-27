---
title: Admin Panel Access via Default Credentials
url: https://infosecwriteups.com/admin-panel-access-via-default-credentials-215b92b030bb?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2024-12-24
fetch_date: 2025-10-06T19:37:18.801122
---

# Admin Panel Access via Default Credentials

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2F215b92b030bb&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fadmin-panel-access-via-default-credentials-215b92b030bb&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fadmin-panel-access-via-default-credentials-215b92b030bb&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-215b92b030bb---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-215b92b030bb---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

# Admin Panel Access via Default Credentials 🤩

[![cryptoshant🇮🇳](https://miro.medium.com/v2/resize:fill:64:64/1*WB_W42RWlz5rAUWNCTByiw.png)](https://medium.com/%40dsmodi484?source=post_page---byline--215b92b030bb---------------------------------------)

[cryptoshant🇮🇳](https://medium.com/%40dsmodi484?source=post_page---byline--215b92b030bb---------------------------------------)

3 min read

·

Dec 18, 2024

--

2

Listen

Share

Hello Hackers, In this write-up I am going to tell how quickly and easily I can access to admin panel using default credentials.

Press enter or click to view image in full size

![]()

Credit: DALL-E 3

After choosing a target which is VDP but the big company in India. Now when I look at the scope I see one domain which looks like **xyz.redacted.com** so why I choose this domain? I don’t know I just open this domain in new tab and it redirect me to login page and the url looks like **xyz.redacted.com/login**

There is no way to create an account only thing is you can access the website after entering the credentials like Email or Username and Password. Now I simply try some fuzzing to find-out any hidden paths or something or 403 errors so I will try to bypass them.

> **If you want to bypass 403 & 401 methods here I made a write-up which contains all the methods and some automation tools you can use all are in this writeup:**

[## Methods to bypass 403 & 401

### Hello Hackers, today in this write-up I am going to give you all things you need to know to bypass 403 & 401 error…

infosecwriteups.com](/methods-to-bypass-403-401-38df4cec069e?source=post_page-----215b92b030bb---------------------------------------)

Let’s come to point, I didn’t find any interesting things so I think let’s enter some default credentials to access the admin panel. And guess what this works 😛

I enter **admin:admin** in username and password filed and it give me direct access to the admin panel 🥳

After gaining access to admin panel I want to dig more what things this panel disclosing and what I found it disclosed all the employees details and I as an attacker can perform all the **CRUD ( create, read, update, delete)** operations to the employees.

Another juicy thing I found was all the logs of the users, all the vendors information including their email, phone no, address, vendor company names, all vendor CEO information and lots of things. Even I can change the admin password.

After that I quickly make a report to the company and wait for their response but sadly this report was closed as **DUPLICATE** but they give me **HOF 🥳** and I am still happy to find my another **P1 bug** and this is a part of bug bounty so be consistent and stay motivated.

Thanks for reading! Give clap and 👋

Another articles may you found helpful:

[## 💥 My First Critical Bug: Exposing 3.5 Lakh+ PII! 🛡️

### Hello Hackers, Today in this write-up I am going to tell you how accidently I discovered my very first critical bug…

infosecwriteups.com](/my-first-critical-bug-exposing-3-5-lakh-pii-%EF%B8%8F-fbad616ddbea?source=post_page-----215b92b030bb---------------------------------------)

[## 🎉 My First Bounty of ₹₹₹ 🎉

### Hello Hackers! 👋 I’m Dishant, and today I’m thrilled to share the story of how I earned my first bounty with a simple…

osintteam.blog](https://osintteam.blog/my-first-bounty-of-37c2d40cbdd9?source=post_page-----215b92b030bb---------------------------------------)

[## 🚀 ISRO: YouTube Broken Link Hijack 🐞

### Hello Hackers, Today in this write-up I am going to discuss very quick and easy bug broken link hijacking and how I got…

osintteam.blog](https://osintteam.blog/isro-youtube-broken-link-hijack-304a92001b47?source=post_page-----215b92b030bb---------------------------------------)

[Bug Bounty](https://medium.com/tag/bug-bounty?source=post_page-----215b92b030bb---------------------------------------)

[Hacking](https://medium.com/tag/hacking?source=post_page-----215b92b030bb---------------------------------------)

[Hall Of Fame](https://medium.com/tag/hall-of-fame?source=post_page-----215b92b030bb---------------------------------------)

[Bug Bounty Tips](https://medium.com/tag/bug-bounty-tips?source=post_page-----215b92b030bb---------------------------------------)

[Pentesting](https://medium.com/tag/pentesting?source=post_page-----215b92b030bb---------------------------------------)

--

--

2

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:96:96/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--215b92b030bb---------------------------------------)

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:128:128/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--215b92b030bb---------------------------------------)

Follow

[## Published in InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---post_publication_info--215b92b030bb---------------------------------------)

[71K followers](/followers?source=post_page---post_publication_info--215b92b030bb---------------------------------------)

·[Last published 4 hours ago](/baby-dfc2547dc387?source=post_page---post_publication_info--215b92b030bb---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow

[![cryptoshant🇮🇳](https://miro.medium.com/v2/resize:fill:96:96/1*WB_W42RWlz5rAUWNCTByiw.png)](https://medium.com/%40dsmodi484?source=post_page---post_author_info--215b92b030bb---------------------------------------)

[![cryptoshant🇮🇳](https://miro.medium.com/v2/resize:fill:128:128/1*WB_W42RWlz5rAUWNCTByiw.png)](https://medium.com/%40dsmodi484?source=post_page---post_author_info--215b92b030bb-------------------------...