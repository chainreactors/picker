---
title: My Latest XSS Finding, Explained To Beginners | Bug Bounty
url: https://buaq.net/go-137952.html
source: unSafe.sh - 不安全
date: 2022-12-01
fetch_date: 2025-10-04T00:09:43.913905
---

# My Latest XSS Finding, Explained To Beginners | Bug Bounty

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

My Latest XSS Finding, Explained To Beginners | Bug Bounty

It’s been a while since i posted a writeup so i thought it would be wise to make one for beginners.S
*2022-11-30 23:11:56
Author: [infosecwriteups.com(查看原文)](/jump-137952.htm)
阅读量:41
收藏*

---

It’s been a while since i posted a writeup so i thought it would be wise to make one for beginners.

So to begin i want to answer some questions, what is **Cross-site** **Scripting(XSS)?**

imperva.com

**Cross-site Scripting(XSS)** is a really well-known vulnerability that occurs because applications take user inputs in an unsecured way. There is other types of XSS vulnerabilities too but today i am going to talk about **Reflected** **Cross-site Scripting.**

Lots of wannabe bug bounty hunters thinks that xss just copying and pasting *<img src=x onerror=alert(1)>* everywhere and expecting to see a pop up on the screen. What xss really about is actually the context. So let’s say the XSS context is into an HTML tag attribute value, you might be able to terminate the attribute value, close the tag and create a second tag which will store your payload. Unfortunately in most cases, angle brackets will be blocked or encoded.

**But** if you know about XSS contexts, you may still be able to terminate the attribute value and create a new attribute that will store your payload. I.E

```
" autofocus onfocus=alert(document.domain) x="
```

To close up, i am going to talk about **my finding.**

I found an error page on webarchive, there was a parameter called result in the url but site wasn’t showing anything. So i thought it’d be wise to look at the source code of the site and to my luck the parameter was reflecting inside of a script tag. If you were to just paste*“><img src=x onerror=alert(1)>* into the parameter, you wouldn’t see any pop up. You need to close the script tag first and create a new tag that will store your payload. The final payload i used as a PoC in my report was

```
</script>"><img src=x onerror=alert(1)>
```

**Reported On: 11/10/2022**

**Triaged On: 11/11/2022**

**$$$ Bounty Paid On: 11/15/2022**

Triaged in 1 day and i got paid $$$ bounty in a week. It was one of the fastest paid report.

## From Infosec Writeups: A lot is coming up in the Infosec every day that it’s hard to keep up with. [Join our weekly newsletter](https://weekly.infosecwriteups.com/) to get all the latest Infosec trends in the form of 5 articles, 4 Threads, 3 videos, 2 GitHub Repos and tools, and 1 job alert for FREE!

文章来源: https://infosecwriteups.com/my-latest-xss-finding-explained-to-beginners-bug-bounty-8674fa3626e7?source=rss----7b722bfd1b8d--bug\_bounty
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)