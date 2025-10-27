---
title: 图片隐形工具 outguess
url: https://buaq.net/go-164984.html
source: unSafe.sh - 不安全
date: 2023-05-22
fetch_date: 2025-10-04T11:36:52.887488
---

# 图片隐形工具 outguess

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

图片隐形工具 outguess

安装可以直接 apt install outguess 或者 yum install outguess或者自行编译git clone https://g
*2023-5-21 22:35:0
Author: [blog.upx8.com(查看原文)](/jump-164984.htm)
阅读量:39
收藏*

---

## 安装

可以直接 `apt install outguess` 或者 `yum install outguess`

或者自行编译

git clone <https://github.com/crorvick/outguess>

## 使用帮助

输入 `outguess -h` 可获得 help 帮助页面

图片格式需要 jpg 格式

## 加密

outguess -k "secret key" -d input.txt pic.jpg pic\_output.jpg

其中 -k 命令是加上密码用的，`secret key` 就是密码。 -d 就是加密了，input.txt 是需要隐藏的 txt 文件，pic.jpg 是原始图片，pic\_output.jpg 是最后输出的包含隐藏内容的图片。

如果不加密码就是

outguess -d input.txt pic.jpg pic\_output.jpg

## 解密

outguess -k "secret key" -r input.jpg output.txt

-r 就是解密， input.jpg 是包含隐藏内容的、需要解密的图片文件，而 output.txt 就是隐藏内容的输出 txt 文件。

如果不加密码就是

outguess -r input.jpg output.txt

文章来源: https://blog.upx8.com/3572
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)