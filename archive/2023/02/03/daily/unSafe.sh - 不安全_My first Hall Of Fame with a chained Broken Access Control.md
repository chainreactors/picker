---
title: My first Hall Of Fame with a chained Broken Access Control
url: https://buaq.net/go-147719.html
source: unSafe.sh - 不安全
date: 2023-02-03
fetch_date: 2025-10-04T05:33:53.675771
---

# My first Hall Of Fame with a chained Broken Access Control

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

My first Hall Of Fame with a chained Broken Access Control

This blog is about how I got my first HOF after chaining multiple bugs.Let’s get started.In simple w
*2023-2-2 22:25:6
Author: [infosecwriteups.com(查看原文)](/jump-147719.htm)
阅读量:31
收藏*

---

This blog is about how I got my first HOF after chaining multiple bugs.

Let’s get started.

> In simple words, BAC means you are able to perform certain actions or fetch certain files which you are not authorized to.

Let’s name the program ***redacted.com***. After some enumeration I found a support page i.e. ***redacted.com/support*** which has a login feature. I created an account i.e. **Attacker1** and started exploring with it.

Later I found that you can create ticket in the help desk section. I simply files a test complaint and created a ticket and checked the Burp History I was a parameter named opener ID. Then I got two ideas, Rate Limit and IDOR.

Request Captured in Burp while submitting the ticket

## Bug 1: Rate Limit

For this, capture the request in Burp while submitting the ticket > send the request to intruder > add the position > start the attack. As expected, there was not Rate Limit and I was able to create as many tickets I want.

## Bug 2: IDOR

Since I already the ID parameter in request, I created another account i.e. **Attacker2** without wasting any time.

I created a ticket with the Attacker1’s account > Captured the request > changed the ID number with Attacker2’s ID > send the request to intruder > add the position > start the attack.

And as expected, It worked. I was able to create as many tickets as I want in other users help desk portal.

By Doing so, an attacker can create many unwanted tickets which can be a hectic for the support team to close the tickets as well as the user’s too and can also spam the user’s email.

## HOF

Thanks for reading this writeup. This is my first blog related to Bug Bounty, so Feedback is appreciated. And if you have any doubt, you can reach me at:

| [LinkedIn](http://linkedin.com/in/namx05) | [Twitter](https://twitter.com/namx05) |

文章来源: https://infosecwriteups.com/my-first-hall-of-fame-with-a-chained-broken-access-control-76f9e2e0e467?source=rss----7b722bfd1b8d--bug\_bounty
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)