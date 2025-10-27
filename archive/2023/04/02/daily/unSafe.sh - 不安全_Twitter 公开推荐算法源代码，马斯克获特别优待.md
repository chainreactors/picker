---
title: Twitter 公开推荐算法源代码，马斯克获特别优待
url: https://buaq.net/go-156467.html
source: unSafe.sh - 不安全
date: 2023-04-02
fetch_date: 2025-10-04T11:26:31.916647
---

# Twitter 公开推荐算法源代码，马斯克获特别优待

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

Twitter 公开推荐算法源代码，马斯克获特别优待

Twitter 公开了推荐算法源代码，源代码托管在 GitHub 上，采用 GNU Affero General Public License v3.0 许可证。推荐算法的一个主要目的是筛
*2023-4-1 15:55:6
Author: [www.solidot.org(查看原文)](/jump-156467.htm)
阅读量:27
收藏*

---

Twitter 公开了推荐算法源代码，源代码托管在 GitHub 上，采用 GNU Affero General Public License v3.0 许可证。推荐算法的一个主要目的是筛选出流行推文，利用机器学习模型进行排名，应用过滤器过滤掉 NSFW 推文和已屏蔽用户推文等，最后展示到用户的时间线。Twitter 的算法引发了用户的强烈兴趣，用户很快发现 Twitter CEO 马斯克（Elon Musk）得到了特别对待。上个月马斯克的推文曾一度展示给几乎所有 Twitter 用户。相关算法代码特别提到了 author\_is\_elon、author\_is\_power\_user、author\_is\_democrat、author\_is\_republican...代码注解声称这些用户 ID 只是用于数据收集的目的。对于这一发现，马斯克本人在 Twitter 上表示将会移除，声称他也是才知道。

https://github.com/twitter/the-algorithm/blob/7f90d0ca342b928b479b512ec51ac2c3821f5922/home-mixer/server/src/main/scala/com/twitter/home\_mixer/functional\_component/decorator/HomeTweetTypePredicates.scala#L225

文章来源: https://www.solidot.org/story?sid=74553
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)