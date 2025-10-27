---
title: [WRITE-UP] ATO bug in a target who wasn’t running any bug bounty program (Bounty: 40K INR)
url: https://buaq.net/go-138831.html
source: unSafe.sh - 不安全
date: 2022-12-07
fetch_date: 2025-10-04T00:38:39.547772
---

# [WRITE-UP] ATO bug in a target who wasn’t running any bug bounty program (Bounty: 40K INR)

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

[WRITE-UP] ATO bug in a target who wasn’t running any bug bounty program (Bounty: 40K INR)

Hi guys, I’m Shubham Bhamare from Maharashtra, India. It’s my first bug bounty write-up about my fir
*2022-12-6 19:44:26
Author: [infosecwriteups.com(查看原文)](/jump-138831.htm)
阅读量:20
收藏*

---

Hi guys, I’m **Shubham Bhamare** from Maharashtra, India. It’s my first bug bounty write-up about my first valid bug which could have allowed a malicious user to take over any account on that target site.

So let's start! 👉

===

**Target:**

As I can’t disclose the name of the company, let’s call it “Target”. While using their website, I found that there should be something unintended.

But unfortunately, they weren’t running any bug bounty program. But due to the severity of this bug and the huge number of their users, I decided to contact them via email and ask them whether they’re running any bug bounty program or not. TBH, I just wanted to bring this issue to their attention, didn’t expect any reward from them. Just wanted to get this bug fixed as I also was a user of their service(s).

So on the next day, they replied that they're not running any bug bounty program currently but can give a bounty based on the severity of a bug.

So with their consent, I proceed further.

===

**Setup:**

2 accounts of that target i.e. Attacker and Victim.

===

**Reproduction steps/scenario:**

1) Target has a login option. Users can login with both by entering a password or OTP.

2) Assume that both attacker and victim have created their accounts on that target.

3) Now from the attacker's perspective, try to login to the victim's account with OTP by entering the victim's phone or username.

4) A 6-digit code will be sent to the victim.

5) After 60 seconds, click the 'Resend' button and capture the request.

6) Modify the *"phone"* parameter with the attacker's phone (where the attacker can receive messages).

7) Forward the request.

8) Now attacker will receive the OTP and after entering it, he'll successfully log in to the victim's account.

My reaction that time 😂

> **Here, target wasn't authenticating phone number while re-sending OTPs.**

===

**Bypass:**

When the team fixed this issue, I found another similar vector that also could be abused.

It was asking OTP if the user requested to delete the account. So this endpoint was also vulnerable.

===

**Bounty:**

40K INR for both bugs.

===

**Takeaway(s):**

1) Although the company doesn't have their bug bounty program and you believe that there's something unintended in their infrastructure that should be fixed, contact them for their consent to test it further. Because securing something from bad guys is always a good practice.

2) Don't hunt on that programs/features where everyone's hunting already. Find your own programs/hidden features/techniques.

3) Always try to find a bypass.

===

Thank you for reading! Also, I’m going to publish all my **Facebook bug bounty** **write-ups** very soon. So don’t forget to follow me on [**Facebook**](https://facebook.com/theshubh77), [**Twitter**](https://twitter.com/theshubh77), [**Instagram**](https://instagram.com/theshubh77), and [**Medium**](https://medium.com/%40theshubh77). 😊

===

## From Infosec Writeups: A lot is coming up in the Infosec every day that it’s hard to keep up with. [Join our weekly newsletter](https://weekly.infosecwriteups.com/) to get all the latest Infosec trends in the form of 5 articles, 4 Threads, 3 videos, 2 GitHub Repos and tools, and 1 job alert for FREE!

文章来源: https://infosecwriteups.com/my-first-bug-bounty-write-up-about-my-first-valid-finding-a-very-simple-ato-bug-in-a-target-who-1b8259f531d6?source=rss----7b722bfd1b8d--bug\_bounty
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)