---
title: [WRITE-UP] Irremovable comments on the FB Lite app | A story of a simple FB Lite bug that I found…
url: https://buaq.net/go-138835.html
source: unSafe.sh - 不安全
date: 2022-12-07
fetch_date: 2025-10-04T00:38:42.974003
---

# [WRITE-UP] Irremovable comments on the FB Lite app | A story of a simple FB Lite bug that I found…

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

[WRITE-UP] Irremovable comments on the FB Lite app | A story of a simple FB Lite bug that I found…

Hi guys, I’m Shubham Bhamare again. In this write-up, I’m going to tell you how I found a simple FB
*2022-12-6 19:39:48
Author: [infosecwriteups.com(查看原文)](/jump-138835.htm)
阅读量:11
收藏*

---

Hi guys, I’m **Shubham Bhamare** again. In this write-up, I’m going to tell you how I found a simple FB Lite bug that restricted FB Lite app users from deleting comments under certain circumstances. This was an easy finding because it was found just by observation. (Just like my [previous finding of 5000 USD](https://medium.com/%40theshubh77/write-up-missing-rate-limiting-how-i-was-able-to-add-any-unowned-phone-number-to-my-fb-account-fe4d7e67cf10), where I was able to add any unowned phone number to my Facebook account.)

So without wasting time, let’s start! 👉

===

**Description:**

FYI, let me clarify that when I reported this issue, Facebook (now Meta) used to consider those bugs too where users were unable to perform certain actions through the FB Lite app but were able to perform through other platforms like Facebook Web, Facebook for Android/iOS, etc. This is because users with low bandwidth and storage were unable to use the other platforms mentioned above.

I don’t know if Facebook still accepts these types of bugs as I’m not hunting for bugs nowadays. Please confirm in the comments section if you have recently got a bounty for the same bug.

===

**The story:**

**Chapter 1:** I still remember when I reported this issue, it was the 1st day of August and a rainy afternoon. I was lying on the bed after lunch and scrolling through my old Facebook posts using the FB Lite app. Suddenly, I came across an old post of mine on which I had commented twice with the same word. So I tried to delete that comment but the app threw an error saying “We can’t process this request at the moment. Please try a bit later!”

I tried to delete my other comments but they too didn’t get deleted. After that, I tried to delete other people’s comments on my old posts but it threw the same error. I thought it was because I haven't updated the FB Lite app so I quickly updated it and tried to delete those comments again. But still, I wasn’t able to delete them.

It was a eureka moment for me as it was something unintended. I quickly recorded a video PoC demonstrating this bug and reported it to Facebook.

**Chapter 2:** On the same day, Facebook replied and requested additional information such as Post ID, FB Lite version, Device information, etc. as they were unable to reproduce this issue.

So I created a test post to send its ID to the team and commented on it and tried to delete that comment. But this time comment got deleted successfully. I felt sad assuming that my reported bug is nothing but a false positive. Now I tried to delete old comments and this time it threw the same error.

It was weird. I tested it further and found that only old comments that were made in the year 2013 or prior were affected by this issue. Added this additional information to the report and after some follow-ups, the team was able to reproduce this issue.

===

**Timeline:**

> Aug 01, 2019: Report sent
>
> Aug 01, 2019: Additional information requested by Facebook
>
> Aug 02, 2019 — Aug 16, 2019: Follow-ups
>
> Aug 23, 2019: Triaged
>
> Oct 25, 2019: 500 USD bounty awarded

> Feb 07, 2020: Fixed completely

===

**Takeaway(s):**

1. While browsing something (even though you’re not in the mood of hunting bugs), always observe whether something’s working as intended or not.
2. If you are new to the Facebook bug bounty, then these types of FB Lite bugs are low-hanging fruit for you. Just observe, apply your logic and grab them.
3. Some bugs may be time and account specific

===

Thank you for reading! Stay tuned for my next write-up, and don’t forget to follow me on [**Facebook**](https://facebook.com/theshubh77), [**Twitter**](https://twitter.com/theshubh77), [**LinkedIn,**](https://linkedin.com/in/theshubh77)and[**Instagram**](https://instagram.com/theshubh77)**. 😊**

===

## From Infosec Writeups: A lot is coming up in the Infosec every day that it’s hard to keep up with. [Join our weekly newsletter](https://weekly.infosecwriteups.com/) to get all the latest Infosec trends in the form of 5 articles, 4 Threads, 3 videos, 2 GitHub Repos and tools, and 1 job alert for FREE!

文章来源: https://infosecwriteups.com/write-up-irremovable-comments-on-fb-lite-app-a-story-of-a-simple-fb-lite-bug-that-i-found-just-125aaa826dd8?source=rss----7b722bfd1b8d--bug\_bounty
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)