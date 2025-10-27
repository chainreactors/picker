---
title: AI表格生成（自动处理表格）
url: https://buaq.net/go-155553.html
source: unSafe.sh - 不安全
date: 2023-03-28
fetch_date: 2025-10-04T10:49:34.155486
---

# AI表格生成（自动处理表格）

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

![](https://8aqnet.cdn.bcebos.com/4292e732edda051366dabdb718ae682c.jpg)

AI表格生成（自动处理表格）

ChatExcel的原理一言以蔽之，就是直接把“大白话指令”转换成类似于VBA这样的程序语言，然后再执行程序。底层基于Transformer架构，基本技
*2023-3-27 22:51:45
Author: [blog.upx8.com(查看原文)](/jump-155553.htm)
阅读量:37
收藏*

---

ChatExcel的原理一言以蔽之，就是直接把“大白话指令”转换成类似于VBA这样的程序语言，然后再执行程序。

底层基于Transformer架构，基本技术路线就是无监督训练+具体场景微调。

但NLP模型搞数学，一直都很容易出错，强大如ChatGPT都很难避免。

为此，团队在训练模型的过程中，将重点放在了**符号逻辑**上，期间还有意引入了一些逻辑符号的新知识。

由此我们也看到，它在计算上出错的概率并不高。

除了**数学能力**出众之外，ChatExcel最大的一个特点就是**持续交互**。

![](https://i.postimg.cc/xT94kX2c/image.png)

这是因为ChatExcel每次的生成结果，都是基于用户提出的新需求+上一轮生成的表格。对模型的理解力及运算其实提出了更高的要求。

为什么要实现这一功能？

团队介绍说，如Dall·E、ChatBCG等AI工具，完成任务的方式都是单次不持续的。但在人们的实际使用过程中，想法是一步步推进的。

ChatExcel团队表示的确有商业化的考虑，但会是To B层面的。

在线地址：

文章来源: https://blog.upx8.com/3370
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)