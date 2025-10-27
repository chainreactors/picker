---
title: Irremovable Facebook group album photos and entire album under certain circumstances (Bounty: 1000…
url: https://buaq.net/go-138834.html
source: unSafe.sh - 不安全
date: 2022-12-07
fetch_date: 2025-10-04T00:38:42.036397
---

# Irremovable Facebook group album photos and entire album under certain circumstances (Bounty: 1000…

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

Irremovable Facebook group album photos and entire album under certain circumstances (Bounty: 1000…

Hi guys, it's Shubham Bhamare again. In this write-up, I'm going to tell you about one of my very si
*2022-12-6 19:42:39
Author: [infosecwriteups.com(查看原文)](/jump-138834.htm)
阅读量:17
收藏*

---

Hi guys, it's **Shubham Bhamare** again. In this write-up, I'm going to tell you about one of my very simple Facebook bug which was found accidentally as I wasn't in the mood of testing at that time and was just browsing our business group on Facebook.

Due to this issue, Facebook group admin was unable to delete group album photos as well as entire album under certain circumstances.

So without wasting time, let's start! 👉

===

**Setup and Scenario:**

1) A Facebook group where only a page (ABC) is an admin.

2) An attacker (XYZ) is a Facebook user who's the member of above group.

Platform: [Facebook Web](https://www.facebook.com)

===

**Reproduction steps:**

1) From ABC's perspective, create an album in a group.

Creating an album in a group

Album created by ABC

2) From XYZ's perspective, add some photos to above album.

Adding photos to the album

Photo uploaded by group member (XYZ)

3) Now when ABC will try to delete that photos added by XYZ, there won't have any option to delete them. Even though ABC used other platforms like Android/iOS/Lite app, mobile site to delete that photos, it won't be possible.

There's no option to delete a photo uploaded by group member

> **ABC will only be able to delete his/her own photos. Being an admin of the group, he should be able to delete photos added by other group members. But there wasn't have any option at that time when I reported this issue.**

===

**Fix and Bypass:**

Team fixed this issue by adding edit button on photos added by other group members. But when I was verifying the fix, I found that if group admin tried to delete entire album (if it includes photos of other members), he/she won't be able to delete it as it was showing an error message.

Delete Album button

Showing an error message while deleting entire album

Impact behind this 2nd issue was, if malicious member added thousand of inappropriate photos to album, then group admin won't be able to delete that entire album. He/she'll have to delete every photo one by one.

Also we can imagine what will happen if multiple group members added thousand of inappropriate photos to that album. 😁

===

**Bounty:**

1000 USD (500 USD for initial report and 500 USD for bypassing the fix or for finding 2nd issue)

1000 USD bounty awarded by Facebook

===

**Timeline:**

> Apr 21, 2019: Report sent

===

**Takeaway(s):**

1) While browsing something (even though you're not in the mood of hunting), always observe whether something's working as intended or not.

2) Don't reveal your findings until you fully believe that there won't be any bypass for it. 😉 Check another endpoints/features too for similar issues.

3) Sometimes you just need logical thinking instead of any advanced tools or knowledge. Because Logic == Magic. 😊

4) If you're new to Facebook bug bounty, try to find logical bugs the most.

===

Thank you for reading! Stay tuned for my next write-up, and don’t forget to follow me on [**Facebook**](https://facebook.com/theshubh77), [**Twitter**](https://twitter.com/theshubh77), [**LinkedIn,**](https://linkedin.com/in/theshubh77)and[**Instagram**](https://instagram.com/theshubh77)**. 😊**

===

## From Infosec Writeups: A lot is coming up in the Infosec every day that it’s hard to keep up with. [Join our weekly newsletter](https://weekly.infosecwriteups.com/) to get all the latest Infosec trends in the form of 5 articles, 4 Threads, 3 videos, 2 GitHub Repos and tools, and 1 job alert for FREE!

文章来源: https://infosecwriteups.com/irremovable-facebook-group-album-photos-and-entire-album-under-certain-circumstances-bounty-1000-b1b2a870b8e0?source=rss----7b722bfd1b8d--bug\_bounty
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)