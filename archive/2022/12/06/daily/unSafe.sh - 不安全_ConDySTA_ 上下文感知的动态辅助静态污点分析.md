---
title: ConDySTA: 上下文感知的动态辅助静态污点分析
url: https://buaq.net/go-138700.html
source: unSafe.sh - 不安全
date: 2022-12-06
fetch_date: 2025-10-04T00:32:35.091203
---

# ConDySTA: 上下文感知的动态辅助静态污点分析

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

![](https://8aqnet.cdn.bcebos.com/e505625f0a12791b7ba423eef84ceb9e.jpg)

ConDySTA: 上下文感知的动态辅助静态污点分析

原文标题：ConDySTA: Context-Aware Dynamic Supplement to Static Taint Analysis原文作者：Zhang X, Wang X, Slavin
*2022-12-5 23:22:22
Author: [mp.weixin.qq.com(查看原文)](/jump-138700.htm)
阅读量:19
收藏*

---

![](https://mmbiz.qpic.cn/mmbiz_png/6Dibw6L070WFxb2EWWK8Fjz8olK6TTB3bjBjiabwoiacicib08WCLJqibNDMT3ba8YJwSwVolWbjoFQu7icX4m7wE6LwQ/640?wx_fmt=jpeg)

> 原文标题：ConDySTA: Context-Aware Dynamic Supplement to Static Taint Analysis

## Introduction

污点分析技术是一种跟踪并分析污点信息在程序中流动的技术，是分析代码漏洞，检测攻击方式的重要手段。污点分析技术可分为动态污点分析与静态污点分析两大类。

* 静态分析在不修改且不运行代码的前提下，对所有可能的路径进行污点传播，从而检测所有可能的污点信息流。静态分析理论上是soundness的，因此也容易产生误报。在真实世界的复杂场景下，静态分析也可能会出现漏报的情况。
* 动态分析侧重检测程序在实际运行的过程中污点数据的传播情况，因此会遗漏运行过程中未触发的路径，且资源开销较大。

由于动态特性代码（反射，动态加载/代码生成，外部代码执行等）只有在运行时才能获得具体信息，传统的静态污点分析无法精确地分析出其中可能存在的安全问题，也就导致了漏报率的上升。而现有的静态污点分析工具通常会忽略这些动态语言特性，不考虑流向数据库或文件的污点流。面临上述问题，作者采用了动态辅助静态的方式进行污点分析，但是简单对动态分析结果进行整合又会导致上下文不敏感，进而导致误报率提高。因此作者提出了ConDySTA，通过将动态分析的结果插入到静态分析对应上下文的变量中。

## Approach Overview

作者首先展示了一个在缺少动态分析情况下所导致的漏报。假定在方法 *foo()* 中 *blocker()* 接受的参数 *in* 值可以可以通过方法 *foo2()* 中的 *blocker2()* 获取，一种简单的情况是与服务器进行交互。显然在这种情况下，静态污点分析技术无法对污点变量的传递进行追踪。作者将这种情况产生新污点变量的污点源称为 *intermediate source*。![](https://mmbiz.qpic.cn/mmbiz_png/6Dibw6L070WFXRzOjL7XEqfPc296PSXCj4ruDPrSLkOGdDyl4n9icjcl7M2EoyXrIFaTuzJlicAGpeD75NTyQ7WfA/640?wx_fmt=png)

在动态分析的辅助下，通过追踪 *blocker()* 和 *blocker2()* 的数据流，此次分析会将 *intermediate source* 处生成的新变量标记为污点变量，因此也能成功识别 *line 13* 处的污点汇聚点。但是由于该情况并没有考虑动态分析的调用上下文（ *line 14-15* ），在 *intermediate source* 会产生一个新的污点流，从而导致了误报。作者在此基础上进行改进，通过考虑动态调用上下文，与动态分析上下文不匹配的静态污点传播路径将被自动排除。

![](https://mmbiz.qpic.cn/mmbiz_png/6Dibw6L070WFXRzOjL7XEqfPc296PSXCjwINGpwmib0GzE5qbQ71RPB2rcAOfGkxT3HaznUMX036fmnib7jXJ8CcA/640?wx_fmt=png)

ConDySTA采用了FlowDroid（基于IFDS）作为其静态污点分析部分，动态部分采用了 value-based 动态污点分析技术。虽然 value-based 动态污点分析技术无法处理控制依赖以及加密数据，但是其在黑盒的处理场景下仍具备优势。

![](https://mmbiz.qpic.cn/mmbiz_png/6Dibw6L070WFXRzOjL7XEqfPc296PSXCjc9blJetZibwqRSyAldUkv4gSYgJR5mUjEFG8n4Cpn9niaB5v3uckicic9w/640?wx_fmt=png)

value-based 动态污点分析技术需要污点源的值，作者采用了安卓设备的用户信息作为其污点值。![](https://mmbiz.qpic.cn/mmbiz_png/6Dibw6L070WFXRzOjL7XEqfPc296PSXCj0vW3e2FlpsR0zQQUzLiae86xg8duciaziaK8PWxMibW9oLPBjickIqCloHg/640?wx_fmt=png)

作者通过软件测试生成的系统日志记录字符串类型的返回值以及函数调用栈，并将返回值与上表进行对比，收集了返回类型为 *java.lang.String* 的方法作为 *intermediate source* 。

## Evaluation

作者使用REPRODROID（a large and up-to-date benchmark which combines multiple earlier benchmarks，whose dataset primarily consists of small apps with labeled taint flows）和从Google Play选取的下载量前100的APP。在REPRODROID的基准测试中，在其他六种最新的分析工具产生了28个漏报上，ConDySTA降至12。对于real-world的APP污点分析，ConDySTA在FLOWDROID检测出的281条污点流的基础上检测出额外的39条污点流。

![](https://mmbiz.qpic.cn/mmbiz_png/6Dibw6L070WFXRzOjL7XEqfPc296PSXCjSqs5uQVBUJXm9ut6O0EvkfXIpkPol3Rnibm4BQRBibByfHfNQaYED7Hw/640?wx_fmt=png)![](https://mmbiz.qpic.cn/mmbiz_png/6Dibw6L070WFXRzOjL7XEqfPc296PSXCjb2KR4XW1FaPebPbmWvyAibia4I01aRibzk7kL8WArxOPQfpZKiaA6ZEDpw/640?wx_fmt=png)

> [安全学术圈招募队友-ing](https://mp.weixin.qq.com/s?__biz=MzU5MTM5MTQ2MA==&mid=2247484475&idx=1&sn=2c91c6a161d1c5bc3b424de3bccaaee0&chksm=fe2efbb0c95972a67513c3340c98e20c752ca06d8575838c1af65fc2d6ddebd7f486aa75f6c3&scene=21#wechat_redirect)
> 有兴趣加入学术圈的请联系 **secdr#qq.com**

文章来源: https://mp.weixin.qq.com/s?\_\_biz=MzU5MTM5MTQ2MA==&mid=2247488299&idx=1&sn=79401150cf2601ab1e5215013585f16e&chksm=fe2eeca0c95965b6dc4c5a5436a822e6b01efa2da5d414370e42c7bdb6db3c2ed09071c5012f#rd
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)