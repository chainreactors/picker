---
title: How BAC(Broken Access Control) got me a Pre Account Takeover
url: https://buaq.net/go-171302.html
source: unSafe.sh - 不安全
date: 2023-07-06
fetch_date: 2025-10-04T11:51:19.600863
---

# How BAC(Broken Access Control) got me a Pre Account Takeover

* [unSafe.sh - 不安全](https://unsafe.sh)
* [我的收藏](/user/collects)
* [今日热榜](/?hot=true)
* [公众号文章](/?gzh=true)
* [导航](/nav/index)
* [Github CVE](/cve)
* [Github Tools](/tools)
* [编码/解码](/encode)
* [文件传输](/share/index)
* [Twitter Bot](https://twitter.com/buaqbot)
* [Telegram Bot](https://t.me/aqinfo)
* [Search](/search/search)

[Rss](/rss.xml)

[ ]
黑夜模式

![]()

How BAC(Broken Access Control) got me a Pre Account Takeover

Hey Hackers!!!This is a writeup about one of my recent findings on a VDP. I found a Broken Access Co
*2023-7-5 23:40:1
Author: [infosecwriteups.com(查看原文)](/jump-171302.htm)
阅读量:24
收藏*

---

[![Bharat Singh](https://miro.medium.com/v2/da:true/resize:fill:88:88/1*SLUmV3MPNVcuzAnQFICGyg.gif)](https://bharat-singh.medium.com/?source=post_page-----2481931b7b3a--------------------------------)[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:48:48/1*A6LVtmXcJ3QJy_sdCyFx1Q.png)](https://infosecwriteups.com/?source=post_page-----2481931b7b3a--------------------------------)

Hey Hackers!!!

This is a writeup about one of my recent findings on a VDP. I found a Broken Access Control bug which was eventually leading to Pre-Account Takeover. Lets head on to our main story…

It was a typical, boring and unexciting Saturday, I was looking for something to kill the time. So, I decided to do some bug hunting. With the help of this [Bug Bounty Google Dork list](https://github.com/BH4R4T-SINGH/Bug_Bounty-Google_Dorks) I found a program to test my skills.

When I signed up on the web application, I discovered some interesting features like creating groups and inviting users. As a bug hunter, it felt like stumbling upon a treasure chest of possibilities, I started manually hunting for Vulnerabilities in Password Reset and 2FA Functionality but I got nothing there. So I went for User Manager option to test without wasting any more time.

Next, using a test account called **“[[email protected]](/cdn-cgi/l/email-protection)”** I invited myself to the platform. Then, I explored the User Manager option to see what information I could find.

There we got some basic info about the invited user like name, login, email… Here the **login** field is responsible for **password change**, But I was **not allowed to change the login and email field of the invited user.**

Not allowed to change Login and Email

I intercepted the request and attempted to modify the **login parameter,** hoping it would give me **Account Takeover** to the invited user’s account. Unfortunately, my plan didn’t work out as expected. However, I didn’t give up just yet.

So I went to change the **Email address to “[[email protected]](/cdn-cgi/l/email-protection)”** by intercepting the request and to my surprize it actually changed the email address of the invited user on the front-end as well as on back-end.

Change the email parameter in request body

Email Successfully changed

I know this is a Low Severity bug, but this is an intresting find for me, So I couldn’t resist sharing this writeup with all of you.

**Impact:**

This vulnerability can lead to Per Account Takeover of any unregistered user and an attacker can misuse the identity of the victim.

**Timeline:**

25-March-2023 >> Bug Reported

20-June-2023 >> They patched the vulnerability & marked it as **low severity.**

If you guys like this writeup and learned something valuable then do hit the clap **👏 X 50 times.**

Feel free to connect with me on [Linkedin](https://www.linkedin.com/in/bharat-s1ngh/) and [Twitter](https://twitter.com/zingzangoo).

文章来源: https://infosecwriteups.com/how-bac-broken-access-control-got-me-a-pre-account-takeover-2481931b7b3a?source=rss----7b722bfd1b8d--bug\_bounty
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)