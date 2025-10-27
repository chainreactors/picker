---
title: cloudflare-chatgpt
url: https://buaq.net/go-139726.html
source: unSafe.sh - 不安全
date: 2022-12-13
fetch_date: 2025-10-04T01:17:11.156575
---

# cloudflare-chatgpt

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

![](https://8aqnet.cdn.bcebos.com/292dcf8d95d87b75a6b30be023a7a36a.jpg)

cloudflare-chatgpt

run chatgpt in cloudflare worker, then you can call it anywhereHow to use cloudflare
*2022-12-12 21:38:19
Author: [github.com(查看原文)](/jump-139726.htm)
阅读量:67
收藏*

---

run chatgpt in cloudflare worker, then you can call it anywhere

### How to use cloudflare

cloudflare worker : <https://workers.cloudflare.com/>

You can have 100000 requests/day for free

### how to get cookies

Go to <https://chat.openai.com/chat> and log in or sign up.
Open dev tools.
Open Application > Cookies.

[![image](https://user-images.githubusercontent.com/29261120/206084836-4f86f741-c560-4d0d-92c7-6cd8960c831a.png)](https://user-images.githubusercontent.com/29261120/206084836-4f86f741-c560-4d0d-92c7-6cd8960c831a.png)

### How to request data

#### id && message\_id ：Generated using uuid, it is recommended to use v4

url: xxxxxx
Method : POST

#### body :

{
"id" : "d8cc4969-23c8-4d2c-b5a9-7b85331d678c",
"message" : "hello",
"message\_id" :"7e50d02c-4c79-407a-b8a9-56127d197c86"
}

文章来源: https://github.com/y35uishere/cloudflare-chatgpt
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)