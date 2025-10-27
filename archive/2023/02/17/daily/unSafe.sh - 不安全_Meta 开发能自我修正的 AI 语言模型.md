---
title: Meta 开发能自我修正的 AI 语言模型
url: https://buaq.net/go-149703.html
source: unSafe.sh - 不安全
date: 2023-02-17
fetch_date: 2025-10-04T06:50:30.762814
---

# Meta 开发能自我修正的 AI 语言模型

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

Meta 开发能自我修正的 AI 语言模型

OpenAI 的 ChatGPT 让无数人惊叹，然而它在简单任务如算术和事实核查上仍然存在明显缺陷。Meta 的研究人员最近透露了一种新的语言模型 Toolformer，能在不牺牲核心语言
*2023-2-16 20:15:12
Author: [www.solidot.org(查看原文)](/jump-149703.htm)
阅读量:15
收藏*

---

OpenAI 的 ChatGPT 让无数人惊叹，然而它在简单任务如算术和事实核查上仍然存在明显缺陷。Meta 的研究人员最近透露了一种新的语言模型 Toolformer，能在不牺牲核心语言建模能力的情况下利用外部工具如搜索引擎、计算器和日历来自我修正。Toolformer 的关键在于它能以无缝和自动化的方式使用 API。在训练中，研究人员给了一组人类编写的示例演示 API 如何使用，然后让它使用 API 调用给一个大语言建模数据集做注解。Toolformer 以自我监督的方式完成了任务，意味着它可以在不需要明确的人类指导下学习。模型学会了预测每个基于文本的 API 调用，可以在需要时插入调用，它还能基于上下文自行决定使用哪个工具，以及如何使用。如 Toolformer 能使用计算器来解决大语言模型（LLM）在算术上的局限性。Toolformer 基于预训练的 GPT-J 模型，该模型有 67 亿个参数。测试显示它的表现优于有 1750 亿个参数的 GPT-3 模型。

https://arxiv.org/abs/2302.04761

文章来源: https://www.solidot.org/story?sid=74154
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)