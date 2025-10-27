---
title: 甲骨文云(Oracle Cloud)增加硬盘空间 | 引导卷大小
url: https://buaq.net/go-148041.html
source: unSafe.sh - 不安全
date: 2023-02-06
fetch_date: 2025-10-04T05:47:01.031406
---

# 甲骨文云(Oracle Cloud)增加硬盘空间 | 引导卷大小

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

甲骨文云(Oracle Cloud)增加硬盘空间 | 引导卷大小

教程：https://www.youtube.com/watch?v=7FBYKdW5gos这个视频将展示，如何在Oracle Cloud(甲骨文云）的
*2023-2-5 23:43:35
Author: [blog.upx8.com(查看原文)](/jump-148041.htm)
阅读量:31
收藏*

---

教程：<https://www.youtube.com/watch?v=7FBYKdW5gos>

这个视频将展示，如何在Oracle Cloud(甲骨文云）的免费实例VPS上增加驱动器空间。默认大小约为 50GB，您可以在首次设置实例时增加此大小。 您也可以稍后增加它，这有点复杂，但是通过以下操作可以实现。

命令：

sudo su -

在甲骨文云修改Boot Volume以后，得到类似于以下的命令行：

growpart /dev/sda 1

resize2fs /dev/sda1

df -h

文章来源: https://blog.upx8.com/3209
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)