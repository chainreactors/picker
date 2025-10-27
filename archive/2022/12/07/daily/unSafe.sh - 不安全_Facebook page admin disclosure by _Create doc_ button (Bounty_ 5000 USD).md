---
title: Facebook page admin disclosure by "Create doc" button (Bounty: 5000 USD)
url: https://buaq.net/go-138833.html
source: unSafe.sh - 不安全
date: 2022-12-07
fetch_date: 2025-10-04T00:38:40.827098
---

# Facebook page admin disclosure by "Create doc" button (Bounty: 5000 USD)

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

Facebook page admin disclosure by "Create doc" button (Bounty: 5000 USD)

Hi guys, it's Shubham Bhamare again. In this write-up, I'm going to tell you about my 2nd valid bug
*2022-12-6 19:43:12
Author: [infosecwriteups.com(查看原文)](/jump-138833.htm)
阅读量:14
收藏*

---

Hi guys, it's **Shubham Bhamare** again. In this write-up, I'm going to tell you about my 2nd valid bug that I found on Facebook. This issue could've accidentally revealed the identity of the Facebook page admin by the "Create doc" button. This is one of the very special findings for me because the bounty I received for this report was beyond my expectations. 😃

So without wasting time, let's start! 👉

===

**Setup and Scenario:**

1) A Facebook user Sarah is the admin of Sarah's Page.

2) Sarah's Page is linked to Sarah's Group.

3) Sarah hasn't made herself an admin of the group because she doesn't want to disclose her identity.

4) So now it's clear that Sarah's Group has only one admin i.e. Sarah's Page. Sarah is just a member of that group and always acts as a page.

===

**Reproduction steps:**

1) Using the Facebook web, acting as Sarah's Page, create a document in Sarah's Group with the "Create doc" button.

2) Before publishing that document, uncheck the option "Allow group members to edit this document". So that only the document owners or admins will be able to edit that document.

3) Now acting as Sarah's Page, edit and save that document.

4) Now if we see the version history of this document, there will be the name of Sarah.

===

**The logic behind it:**

It was easy for other group members to determine who was the admin of the page as only the document owner or admins were able to edit that document. Though there was the name of Sarah in edit history which was unintended.

===

**Fix and Bypass:**

When the team fixed this issue for the "Create doc" button which was present in the post editor, I found that there was another similar button on the "Files" page which was also vulnerable.

When the team was verifying the second fix, they internally identified 3rd vector that also could be abused.

===

**Bounty:**

5000 USD (This reward covers all three of those vulnerabilities. That's why I like Facebook bug bounty the most. 💙)

===

**Timeline:**

> Oct 13, 2018: Report sent

===

**Takeaway(s):**

1) Don't reveal your findings until you fully believe that there won't be any bypass for it. 😉 Check other endpoints/features too for similar issues.

2) Sometimes you just need logical thinking instead of any advanced tools or knowledge. Because Logic == Magic. 😊

3) Again, if you're new to Facebook bug bounty, try to find logical bugs the most.

===

Thank you for reading! Stay tuned for my next write-up and don't forget to follow me on [**Facebook**](https://facebook.com/theshubh77), [**Twitter**](https://twitter.com/theshubh77), [**Instagram**](https://instagram.com/theshubh77), and [**Medium**](https://theshubh77.medium.com). 😊

===

## From Infosec Writeups: A lot is coming up in the Infosec every day that it’s hard to keep up with. [Join our weekly newsletter](https://weekly.infosecwriteups.com/) to get all the latest Infosec trends in the form of 5 articles, 4 Threads, 3 videos, 2 GitHub Repos and tools, and 1 job alert for FREE!

文章来源: https://infosecwriteups.com/facebook-page-admin-disclosure-by-create-doc-button-bounty-5000-usd-2fd1ff615bf8?source=rss----7b722bfd1b8d--bug\_bounty
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)