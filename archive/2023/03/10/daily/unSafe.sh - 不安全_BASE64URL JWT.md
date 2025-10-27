---
title: BASE64URL JWT
url: https://buaq.net/go-152773.html
source: unSafe.sh - 不安全
date: 2023-03-10
fetch_date: 2025-10-04T09:05:26.645857
---

# BASE64URL JWT

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

BASE64URL JWT

BASE64URL是一种在BASE64的基础上编码形成新的加密方式，为了编码能在网络中安全顺畅传输，需要对BASE64进行的编码，特别是互联网中。BASE64U
*2023-3-9 22:10:47
Author: [www.yanglong.pro(查看原文)](/jump-152773.htm)
阅读量:24
收藏*

---

BASE64URL是一种在BASE64的基础上编码形成新的加密方式，为了编码能在网络中安全顺畅传输，需要对BASE64进行的编码，特别是互联网中。

BASE64URL编码的流程：

      1、明文使用BASE64进行加密

      2、在BASE64的基础上进行一下的编码：

               1)去除尾部的”=”

               2)把”+”替换成”-“

               3)把”/”替换成”\_”

BASE64URL解码的流程：

      1、把BASE64URL的编码做如下解码：

               1)把”-“替换成”+”

               2)把”\_”替换成”/”

               3)(计算BASE64URL编码长度)%4

                           a)结果为0，不做处理

                           b)结果为2，字符串添加”==”

                           c)结果为3，字符串添加”=”

      2、使用BASE64解码密文，得到原始的明文

---

文章来源: https://www.yanglong.pro/base64url-jwt/
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)