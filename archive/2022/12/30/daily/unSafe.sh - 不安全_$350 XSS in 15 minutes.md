---
title: $350 XSS in 15 minutes
url: https://buaq.net/go-143057.html
source: unSafe.sh - 不安全
date: 2022-12-30
fetch_date: 2025-10-04T02:43:01.669001
---

# $350 XSS in 15 minutes

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

$350 XSS in 15 minutes

Bug Bounty Writeup about DOM XSS via JSONP + Parameter pollutionPhoto by Pepi Stojanovski on Unsplas
*2022-12-29 20:28:13
Author: [infosecwriteups.com(查看原文)](/jump-143057.htm)
阅读量:29
收藏*

---

## Bug Bounty Writeup about DOM XSS via JSONP + Parameter pollution

Photo by [Pepi Stojanovski](https://unsplash.com/%40timbatec?utm_source=medium&utm_medium=referral) on [Unsplash](https://unsplash.com?utm_source=medium&utm_medium=referral)

Hello 👋

This is my first and last Bug Bounty Writeup this year. 😀

I am sharing with you my latest XSS finding, which I’ve found 2 weeks ago.

This was the fastest and a bit unusual flow that I normally do when I search for XSS.

So let’s dive in…

* Company asked me to retest an old XSS report.
* I’ve checked that XSS and confirmed that it was fixed properly.
* The specific endpoint had `name` a param that was vulnerable to Reflected XSS injection.

```
example.com/profile?name=<img+src=1+onerror=alert(1337)>
```

* I’ve started to search for a bypass and used the Search function in Chrome Developer tools to search this endpoint `/profile` in all JS files to check for another vulnerable param, but found another endpoint:

```
example.com/services
```

* The first idea that came to my mind was to put this URL in the google search engine and see if this endpoint was cached somewhere on the google web space with params.
* After the first try, I found a cached endpoint with params on the first page of the results, the endpoint had ID param and some other params.

```
example.com/services?id=123&page=Demo
```

* I’ve added my payload `qwe'"<X</` to the ID param and started to check if anything is reflected somewhere on the webpage’s source code.

```
example.com/services?id=123qwe'"<X</
```

* Besides that, I’ve opened the Network tab in Chrome Developer tools to check all requests that this endpoint might send somewhere.
* After the second refresh of the page, I found an interesting AJAX request that used the JSONP callback param together with the ID param from the endpoint itself. The AJAX request URL was similar to this:

```
lib.com/find?id=123qwe&jsonp=cb12
```

* The first thing that I tested was the JSONP param itself, to see if I can change it to an `alert` function with a custom parameter
* To my surprise, there was no check for JSONP value, so I easily changed it to `alert(1337);`
* Now it was time to check the ID param once again and see if it accepts other symbols, for example, `%` sign to craft an encoded payload in order to add custom parameters to AJAX URL.
* I’ve changed the endpoint URL to

```
example.com/services?id=1%26jsonp=alert(1337);%23
```

* When JS processed it, it transformed `%26` to & and `%23` to #. Everything that is behind the # (hashtag) symbol is ignored by the browser. The final AJAX call looked like this:

```
lib.com/find?id=1&jsonp=alert(1337);#&jsonp=cb12
```

* Using this AJAX URL manipulation (parameter pollution attack) I have successfully triggered an alert box with text `1337`. This confirmed the DOM XSS vulnerability existence and I have received a $350 bounty, with an additional $50 for a retest of an old report.

Thanks for reading!

P.S. I’m working on a book for beginners in Bug Bounty world. This book will include Networking, HTML & JavaScript basics, a short description of widespread vulnerabilities, and an in-depth analysis of XSS vulnerability with examples, tips, tools, and tricks. At the end of the book, I will teach you how to create and deploy your own NodeJS service for testing Blind-XSS / SSRF vulnerabilities.

P.S.S. Stay tuned for updates and don’t forget to subscribe at least somewhere so you won’t miss any info regarding the book.

Happy Holidays & Happy New Year!

## From Infosec Writeups: A lot is coming up in the Infosec every day that it’s hard to keep up with. [Join our weekly newsletter](https://weekly.infosecwriteups.com/) to get all the latest Infosec trends in the form of 5 articles, 4 Threads, 3 videos, 2 GitHub Repos and tools, and 1 job alert for FREE!

文章来源: https://infosecwriteups.com/350-xss-in-15-minutes-dcb74ad93d5f?source=rss----7b722bfd1b8d--bug\_bounty
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)