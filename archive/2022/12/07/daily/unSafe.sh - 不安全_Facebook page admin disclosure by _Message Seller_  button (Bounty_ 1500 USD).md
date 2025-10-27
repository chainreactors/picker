---
title: Facebook page admin disclosure by "Message Seller"  button (Bounty: 1500 USD)
url: https://buaq.net/go-138832.html
source: unSafe.sh - 不安全
date: 2022-12-07
fetch_date: 2025-10-04T00:38:40.160776
---

# Facebook page admin disclosure by "Message Seller"  button (Bounty: 1500 USD)

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

Facebook page admin disclosure by "Message Seller" button (Bounty: 1500 USD)

Hi guys, I’m Shubham Bhamare from Maharashtra, India. As I promised in my previous write-up, here’s
*2022-12-6 19:43:26
Author: [infosecwriteups.com(查看原文)](/jump-138832.htm)
阅读量:10
收藏*

---

Hi guys, I’m **Shubham Bhamare** from Maharashtra, India. As I promised in my previous write-up, here’s my first Facebook bug bounty write-up. Finally! 😂

I know it’s too late to publish this write-up as this bug was found and rewarded in 2018. I’m extremely sorry for that. Anyways, I’m going to publish all my other findings too in the coming days.

So without wasting time, let's start! 👉

===

**Description:**

This issue could've accidentally revealed the identity of the Facebook page admin under certain circumstances.

On Facebook, page admin’s roles are secret. Disclosing the identity of the page admin may cause a significant privacy issue. In this case, it was possible to disclose the identity of the page admin under certain circumstances.

===

**Setup:**

2 Facebook users i.e. Shubham and John

1 Facebook page i.e. Shubham's Page

1 Facebook group i.e Shubham's Page Group

Platform: [Facebook Web](https://www.facebook.com)

===

**Scenario:**

As mentioned above, there are 2 Facebook users i.e. Shubham and John.

Shubham is the admin of Shubham's Page.

Shubham's Page is linked to Shubham's Page group which is a group for Shopping. Post approval for this group is turned on.

John is a member of said group.

Shubham hasn't made himself an admin of a group because he doesn't want to disclose his identity.

So now that group has only one admin i.e. Shubham's Page.

Shubham is just a member of that group and always acts as a page.

===

**Reproduction steps:**

1) From John's account, create a selling post in the group.

2) Post will be sent to admin for approval.

3) Now from Shubham’s account (acting as a page), click on the "Message Seller" button at the bottom of the above unapproved post and send a message.

4) Message will be sent from Shubham's personal profile instead of the page, which is unintended.

===

**The logic behind it:**

It’s easy for John to determine who’s the admin of the page as there’s only one group admin (Shubham’s Page) who can see that unapproved post.

===

**Fix:**

The team fixed this issue by removing the "Message Seller" button when acting as a page.

===

**Bypass:**

I found that fix was incomplete as this issue was still working on old unapproved posts.

===

**Bounty:**

1500 USD

===

**Timeline:**

> Sep 09, 2018: Report sent

===

**Takeaway(s):**

1) If you're new to Facebook bug bounty, try to find logical bugs the most.

2) Always try to find a bypass.

===

Thank you for reading! My next write-up will be about my second bug in Facebook (Bounty: 5000 USD). So stay tuned and don’t forget to follow me on [**Facebook**](https://facebook.com/theshubh77), [**Twitter**](https://twitter.com/theshubh77), [**Instagram**](https://instagram.com/theshubh77), and [**Medium**](https://theshubh77.medium.com). 😊

===

## From Infosec Writeups: A lot is coming up in the Infosec every day that it’s hard to keep up with. [Join our weekly newsletter](https://weekly.infosecwriteups.com/) to get all the latest Infosec trends in the form of 5 articles, 4 Threads, 3 videos, 2 GitHub Repos and tools, and 1 job alert for FREE!

文章来源: https://infosecwriteups.com/facebook-page-admin-disclosure-by-message-seller-button-bounty-1500-usd-caaa2eac4121?source=rss----7b722bfd1b8d--bug\_bounty
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)