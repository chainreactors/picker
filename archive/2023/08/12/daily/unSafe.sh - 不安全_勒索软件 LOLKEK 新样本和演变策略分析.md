---
title: 勒索软件 LOLKEK 新样本和演变策略分析
url: https://buaq.net/go-174266.html
source: unSafe.sh - 不安全
date: 2023-08-12
fetch_date: 2025-10-04T12:00:29.783789
---

# 勒索软件 LOLKEK 新样本和演变策略分析

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

勒索软件 LOLKEK 新样本和演变策略分析

在快速变化的网络威胁世界中，了解最新变化和模式至关重要。这对于勒索软件来说尤其如此，它以快速变化和复杂的策略而闻名。今年8月，我们在SentinelOne的MDR团队偶然发现了一些异常情
*2023-8-11 17:5:3
Author: [hackernews.cc(查看原文)](/jump-174266.htm)
阅读量:15
收藏*

---

在快速变化的网络威胁世界中，了解最新变化和模式至关重要。这对于勒索软件来说尤其如此，它以快速变化和复杂的策略而闻名。今年8月，我们在SentinelOne的[MDR](https://www.sentinelone.com/global-services/vigilance-respond/ "MDR")团队偶然发现了一些异常情况：新的LOLKEK实例，也被称为GlobeImposter，表明这个长期存在的勒索软件家族正在进行新的改变。

LOLKEK，也被称为 [GlobeImposter](https://www.sentinelone.com/anthology/globeimposter/)，于2016年首次亮相。在快节奏的勒索软件世界里，事件瞬息万变，而[Maze ransomware](https://www.sentinelone.com/anthology/maze/)于 2019年才再次被看见。GlobeImposter标签很巧妙地描述了这种新的勒索软件是如何模仿Globe的。

LOLKEK可以被认为是一种“现成的”勒索软件，其经常会进行迭代更新。尤其是在目标选择和勒索要求方面要求相对较低，如在最近的攻击中，勒索金额通常低于2000美元。相比之下，像Cl0p、LockBit和Royal这样的重量级勒索软件要求的赎金数额令人瞠目结舌。

LOLKEK的主要目标是中小型企业(smb)和个人用户。尽管如此，有时这种勒索软件也会在更复杂、更有计划的金融攻击中发挥作用。以2017年为例，臭名昭著的[TA505](https://www.sentinelone.com/labs/breaking-ta505s-crypter-with-an-smt-solver/)(也被称为G0092，GOLD TAHOE)集团开始雇用GlobeImposter进行系列行为。

这扩大了他们的网络，提高他们的运作能力，也展示了LOLKEK在更广泛的勒索软件领域的适应性和作用。

本文将带您探索最近的LOLKEK有效载荷，重点介绍关键特性、策略更改以及对IOC指标的观察。我们还将强调一个持续存在的OPSEC错误，该错误不断泄露勒索软件运营商的游戏。

**更多内容请至Seebug Paper****阅读全文****：<https://paper.seebug.org/3005>/**

**消息来源：[sentinelone](https://www.sentinelone.com/blog/lolkek-unmasked-an-in-depth-analysis-of-new-samples-and-evolving-tactics/)****，封面来自网络，译者：知道创宇404实验室翻译组。**

**本文由**[**HackerNews.cc**](https://hackernews.cc/)**翻译整理。**

**转载请注明“转自 HackerNews.cc ” 并附上原文链接。**

文章来源: https://hackernews.cc/archives/45097
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)