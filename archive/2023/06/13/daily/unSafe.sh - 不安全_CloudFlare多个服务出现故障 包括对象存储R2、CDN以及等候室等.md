---
title: CloudFlare多个服务出现故障 包括对象存储R2、CDN以及等候室等
url: https://buaq.net/go-168433.html
source: unSafe.sh - 不安全
date: 2023-06-13
fetch_date: 2025-10-04T11:44:16.299250
---

# CloudFlare多个服务出现故障 包括对象存储R2、CDN以及等候室等

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

![](https://8aqnet.cdn.bcebos.com/43806c36db33546f3992f30429498c0e.jpg)

CloudFlare多个服务出现故障 包括对象存储R2、CDN以及等候室等

据 CloudFlare 状态页发布的消息，自今天晚上 7 点半开始 (以下均为中国时间) 起，CloudFlare 多个产品出现可用性下降问题，受影响的产品包括 CloudFlare
*2023-6-12 23:53:16
Author: [www.landiannews.com(查看原文)](/jump-168433.htm)
阅读量:17
收藏*

---

据 CloudFlare 状态页发布的消息，自今天晚上 7 点半开始 (以下均为中国时间) 起，CloudFlare 多个产品出现可用性下降问题，受影响的产品包括 CloudFlare R2、Waiting Room、Durable Objects、Queues、 Stream Live、CDN 文件刷新问题。

[![CloudFlare多个服务出现故障 包括对象存储R2、CDN以及等候室等](https://img.lancdn.com/landian/2022/03/92942.png)](https://img.lancdn.com/landian/2022/03/92942.png)

其中使用 CloudFlare R2、Waiting Room、Stream Live、Queues 的客户在向 Durable Objects 发出请求时会出现 HTTP 500 错误或提示网络连接丢失。

在尝试刷新 CDN 缓存时，如果刷新的是单个文件，则也会出现 HTTP 500 或提示网络连接丢失，如果尝试清除所有缓存的内容则可以正常进行。

截止至本文发布时这些问题仍未解决，CloudFlare 称团队已经找出问题原因，正在努力缓解问题，更多更新信息即将发布。

状态页：<https://www.cloudflarestatus.com/>

注：根据蓝点网测试，目前使用 CloudFlare CDN 的网站不受影响，因此用户的访问也不受影响。

版权声明：感谢您的阅读，除非文中已注明来源网站名称或链接，否则均为蓝点网原创内容。转载时请务必注明：来源于蓝点网、标注作者及[本文完整链接](https://www.landiannews.com/archives/99127.html)，谢谢理解。

文章来源: https://www.landiannews.com/archives/99127.html
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)