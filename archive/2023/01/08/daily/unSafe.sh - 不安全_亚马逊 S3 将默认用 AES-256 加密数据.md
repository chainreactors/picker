---
title: 亚马逊 S3 将默认用 AES-256 加密数据
url: https://buaq.net/go-144596.html
source: unSafe.sh - 不安全
date: 2023-01-08
fetch_date: 2025-10-04T03:18:41.771574
---

# 亚马逊 S3 将默认用 AES-256 加密数据

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

亚马逊 S3 将默认用 AES-256 加密数据

亚马逊 Simple Storage Service (S3)将默认在服务器端用 AES-256 自动加密新数据。AWS 的服务器端加密已经存在了十多年，但现在为了加强安全将默认启用。管理
*2023-1-7 22:14:56
Author: [www.solidot.org(查看原文)](/jump-144596.htm)
阅读量:29
收藏*

---

亚马逊 Simple Storage Service (S3)将默认在服务器端用 AES-256 自动加密新数据。AWS 的服务器端加密已经存在了十多年，但现在为了加强安全将默认启用。管理员无需采取任何行动，亚马逊表示加密不会对性能产生任何影响。默认的加密算法是 AES-256，管理员可以选择 SSE-C 或 SSE-KMS 等替代方法。其中 SSE-C 将由存储桶的所有者控制密钥，SSE-KMS 将由亚马逊管理密钥。存储桶的所有者还可以为每个 KMS 密钥设置不同的权限以便于细化控制。

https://aws.amazon.com/blogs/aws/amazon-s3-encrypts-new-objects-by-default/

文章来源: https://www.solidot.org/story?sid=73832
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)