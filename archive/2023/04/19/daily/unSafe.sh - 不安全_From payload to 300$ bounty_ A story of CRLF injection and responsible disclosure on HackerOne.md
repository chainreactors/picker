---
title: From payload to 300$ bounty: A story of CRLF injection and responsible disclosure on HackerOne
url: https://buaq.net/go-159306.html
source: unSafe.sh - 不安全
date: 2023-04-19
fetch_date: 2025-10-04T11:32:50.398735
---

# From payload to 300$ bounty: A story of CRLF injection and responsible disclosure on HackerOne

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

From payload to 300$ bounty: A story of CRLF injection and responsible disclosure on HackerOne

As a bug bounty hunter, I’m always on the lookout for security vulnerabilities that I can report to
*2023-4-18 23:31:17
Author: [infosecwriteups.com(查看原文)](/jump-159306.htm)
阅读量:36
收藏*

---

As a bug bounty hunter, I’m always on the lookout for security vulnerabilities that I can report to companies and earn rewards. Recently, I discovered a CRLF injection vulnerability on a popular website through the HackerOne platform, and in this blog post, I’m going to share how I found it and the impact it had.

First, let me explain what CRLF injection is. CRLF stands for “Carriage Return Line Feed”, which are special characters used to represent the end of a line in various protocols, including HTTP. An attacker can inject CRLF characters into an HTTP header, which can lead to various attacks, such as HTTP response splitting, cross-site scripting, and cookie manipulation.

During my bug bounty testing, I used my [crlfi](https://github.com/karthi-the-hacker/crlfi) tool, I created this tool for the purpose of detect the CRLF injection Bug. You can install it on your machine by running the following command: “npm install crlfi -g”. It is supported on Windows, Mac, and Linux operating systems. To learn more about how to use it, please visit my Github repository “<https://github.com/karthi-the-hacker/crlfi>”.

After a few minutes of scanning, I was able to obtain a vulnerable output with the payload.

I noticed that the location header value was not properly sanitized, and I was able to inject CRLF characters into it using a simple payload like “%0d%0a” Example [http://example.com/](http://example.com/random)%0D%0ATest-Header:karthithehacker .

This allowed me to manipulate the server’s response and inject arbitrary content into it, such as fake headers or even JavaScript code.

To demonstrate the impact of the vulnerability, I created a proof of concept that injected a fake “Set-Cookie” header into the server’s response, which could be used to steal session cookies and perform session hijacking attacks. I reported the vulnerability to the company through the HackerOne platform, and they confirmed it and rewarded me with a bounty.

> Technical Content : <https://karthithehacker.com/blogs/crlf-in-h1-poc.html>

The lesson here is that even seemingly harmless headers can be vulnerable to CRLF injection, and it’s important to properly sanitize user input before using it in HTTP headers. As a bug bounty hunter, it’s also important to keep an eye out for these types of vulnerabilities, as they can have a significant impact on the security of a web application.

> *Tips:- Downgrade the HTTPS to HTTP and inject CRLF payloads*

POC Video :

In conclusion, CRLF injection is a powerful technique that attackers can use to manipulate HTTP headers and perform various attacks. By understanding how it works and how to prevent it, we can help make the web a safer place for everyone.

Connect with me:

Twitter: <https://twitter.com/karthithehacker>

Instagram: <https://www.instagram.com/karthithehacker/>

LinkedIn: <https://www.linkedin.com/in/karthikeyan--v/>

Website: <https://www.karthithehacker.com/>

Github : <https://github.com/karthi-the-hacker/>

npmjs: <https://www.npmjs.com/~karthithehacker>

Youtube: <https://www.youtube.com/karthithehacker>

> **Thank you**

[Karthikeyan.V](https://medium.com/u/a14784d94f2c?source=post_page-----eeff74aff422--------------------------------)

文章来源: https://infosecwriteups.com/from-payload-to-300-bounty-a-story-of-crlf-injection-and-responsible-disclosure-on-hackerone-eeff74aff422?source=rss----7b722bfd1b8d--bug\_bounty
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)