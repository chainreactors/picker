---
title: Reflected XSS using Double Encoding
url: https://buaq.net/go-138829.html
source: unSafe.sh - 不安全
date: 2022-12-07
fetch_date: 2025-10-04T00:38:37.229879
---

# Reflected XSS using Double Encoding

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

Reflected XSS using Double Encoding

Bypassing XSS filters using Double EncodingHello Hackers,Recently I started my bug hunting journey a
*2022-12-6 19:46:56
Author: [infosecwriteups.com(查看原文)](/jump-138829.htm)
阅读量:32
收藏*

---

## Bypassing XSS filters using Double Encoding

Hello Hackers,

Recently I started my bug hunting journey and got an XSS by Bypassing Cloudflare WAF (you can read about it [here](https://medium.com/%40ag3n7/how-i-bypassed-cloudflare-waf-to-get-my-first-bug-f02dab3a2d10)). Now I am back with another XSS by [Double Encoding](https://owasp.org/www-community/Double_Encoding).

> This attack technique consists of encoding user request parameters twice in hexadecimal format to bypass security controls or cause unexpected behavior from the application. It’s possible because the webserver accepts and processes client requests in many encoded forms.

Going directly into it…

If there is a will, there is a way. Like that if there is an input field, there is a ***chance*** of cross-site scripting. Currently, I am using very basic methods while trying to find bugs and improve myself by learning more methods and bugs. While going through some of the targets and testing input fields (like search boxes), I got an interesting input field, I just entered the usual input

Search Bar

and checked the source code.

source code

Then I added a single quote but it filtered the input and replaced it with *hello1&amp;* in some places and with ‘&’ in our target fields.

I tried URL encoding there, Then also got the same output which means it decodes the input.

So I used [Double Encoding](https://owasp.org/www-community/Double_Encoding).

It works.

Then our basic payload ‘><script>alert(1)</script> with double encoding tried.

> %2527%253E%253Cscript%253Ealert%25281%2529%253C%252Fscript%253E

But it created an error

I searched for attributes of input tag to exploit using it.
[onfocus](https://www.w3schools.com/jsref/event_onfocus.asp) : The onfocus event occurs when an element gets focus.

‘ onfocus=’alert(1)’

> %2527%2520onfocus%253D%2527alert%25281%2529%2527%2520

I clicked on the search bar, and the popup alert appeared.

But I thought of modifying it a little bit with autofocus which makes the text field automatically get focused upon page load and creates the popup alert while visiting the page itself.

‘ onfocus=’alert(1)’ autofocus=’

> %2527%2520onfocus%253D%2527alert%25281%2529%2527%2520autofocus%253D%2527

Yeah. It worked …

OpenBugBounty

You can also use payloads like

‘ onmouseover=’alert(1)’

> %2527%2520onmouseover%253D%2527alert%25281%2529%2527%2520

Thank You For Reading ….

Twitter: <https://twitter.com/ag3n7apk>

Linkedin: <https://www.linkedin.com/in/abhijith-pk-ag3n7/>

## From Infosec Writeups: A lot is coming up in the Infosec every day that it’s hard to keep up with. [Join our weekly newsletter](https://weekly.infosecwriteups.com/) to get all the latest Infosec trends in the form of 5 articles, 4 Threads, 3 videos, 2 GitHub Repos and tools, and 1 job alert for FREE!

文章来源: https://infosecwriteups.com/got-another-xss-using-double-encoding-e6493a9f7368?source=rss----7b722bfd1b8d--bug\_bounty
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)