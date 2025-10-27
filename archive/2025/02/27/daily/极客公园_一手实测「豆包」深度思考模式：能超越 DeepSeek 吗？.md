---
title: 一手实测「豆包」深度思考模式：能超越 DeepSeek 吗？
url: https://mp.weixin.qq.com/s?__biz=MTMwNDMwODQ0MQ==&mid=2653074477&idx=1&sn=3b1bec0b061ad7a07162b4a2b2cd3af0&chksm=7e57c99b4920408d47648d081ffe33689be8b9b6ce125e50e469410211410450d9b276ad1abb&scene=58&subscene=0#rd
source: 极客公园
date: 2025-02-27
fetch_date: 2025-10-06T20:36:39.893867
---

# 一手实测「豆包」深度思考模式：能超越 DeepSeek 吗？

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/8cu01Kavc5YgsE4tcuHny9pxoJfNzcbNneMqsze5GZicRP1RlzxrHRChrLiaTKyYDIsh3jDJ7VakjfSXcya5znmw/0?wx_fmt=jpeg)

# 一手实测「豆包」深度思考模式：能超越 DeepSeek 吗？

原创

连冉

极客公园

![](https://mmbiz.qpic.cn/mmbiz_jpg/8cu01Kavc5YgsE4tcuHny9pxoJfNzcbNQp9icMsS9oCcs5XL4822w4OQsmb4HguquONFytGOr8HPmASB9xCq8Nw/640?wx_fmt=jpeg&from=appmsg)

「元宝」给了「豆包」压力？

**作者｜连冉****编辑｜**郑玄****

字节跳动旗下 AI 助手豆包正在小范围测试深度思考模型，据豆包相关负责人对极客公园表示，当前测试的是自家深度思考模型的不同实验版本。

另外有报道称，豆包正在测试的深度思考模型是基于豆包 1.5 基座模型研发。

其实此前在 1 月中旬，在豆包大模型团队发布豆包 1.5Pro 时，就已宣布了深度推理模型 Doubao-1.5-pro-AS1-Preview 的存在，并称「在完全不使用其他模型数据的条件下，通过 RL 算法的突破和工程优化，充分发挥 Test Time Scaling 的算力优势，完成了 RL Scaling，研发了 Doubao 深度思考模式。」

极客公园实测发现，与豆包对话时后者生成的答案确实有开始显示推理过程的思维链，不过并不稳定出现。目前在豆包对话页面也尚未出现「深度思考」功能的入口。

从 2 月 22 日开始，豆包就被腾讯旗下的 AI 应用「腾讯元宝」压了一个身位，位居中国区苹果应用商店免费 APP 下载排行榜第三位（第一名还是 deepseek)，在腾讯、百度多个应用接入 deepseek 后，字节豆包会如何处之就成为大家关注的焦点，如今答案正在显现。

***01***

******豆包也上「深度思考」了？******

最早具备深度思考能力的模型是 OpenAI 于 2023 年 12 月推出的 o1 系统，但其采用闭源策略而且仅限付费用户使用（每月 200 美元）。而 DeepSeek 则通过开源策略、成本降低以及交互创新，成为首个将深度思考能力大规模普及的 AI 公司——DeepSeek 于 2024 年 11 月 20 日发布 R1-Lite-Preview，成为国内首个对标 o1 的推理模型，并在 2025 年 1 月 20 日开源了 R1 模型。

R1 模型的创新点在于：透明化思维链；展示完整的推理过程，包括自我质疑、假设验证等拟人化思考路径；低成本与开源；R1 模型的推理成本仅为 OpenAI o1 的 1/27，且代码完全开放。

DeepSeek 的深度思考模式是一种通过显性化 AI 模型的推理过程来增强用户理解的功能，思维链（Chain of Thought, CoT）是支撑这一模式的核心技术。

简单来说，深度思考模式可以让用户直观看到模型的思考过程，这中间涉及思维链的展示，也就是 COT（Chain of Thought）——思维链是模拟出来的，通过训练让模型输出中间步骤，比如自我质疑和反思，虽然只是文字序列，但看起来像人类的思考过程。

在深度思考模式下，用户不仅能看到 AI 的最终答案，还能观察到模型解决问题的完整逻辑链条，包括自我质疑、假设验证、错误修正等步骤。比如，在解决数学题时，模型会展示其从问题拆解、多方法验证到最终结论的全过程。

结合实时联网功能后，模型可抓取最新信息并进行逻辑整合。25 日，Anthropic 发布了 Claude 3.7 Sonnet 混合推理模型，阿里云 Qwen 推理模型「QwQ-Max 预览版」也亮相了，我让豆包评价了一下这两款推理模型：

![](https://mmbiz.qpic.cn/mmbiz_png/8cu01Kavc5YgsE4tcuHny9pxoJfNzcbNPkrjKa0jmZgSKD2g2RlyNt7sgmvj5GoWRQXrzLg3LiaIic9ucWYYyNgQ/640?wx_fmt=png&from=appmsg)

可以看到豆包搜到 9 篇资料并进行了「深入思考」｜图片来源：极客公园

![](https://mmbiz.qpic.cn/mmbiz_png/8cu01Kavc5YgsE4tcuHny9pxoJfNzcbNclLPK41YhKSJOawkwxBVDtTOUMQVR8INIU1nM9RMz08uxUHCpaAPsA/640?wx_fmt=png&from=appmsg)

豆包展示了思考过程｜图片来源：极客公园

![](https://mmbiz.qpic.cn/mmbiz_png/8cu01Kavc5YgsE4tcuHny9pxoJfNzcbNvrbyq8MRkd0wr6sMD7MXAoyAk95I40xRwl1GGdUtgSAOC97SiaKqfHg/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/8cu01Kavc5YgsE4tcuHny9pxoJfNzcbNLFibPibibLr0XJgG8D41fb7j1fM1eOG4TLmvx36ribjTlp76R6PmDxYFfQ/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/8cu01Kavc5YgsE4tcuHny9pxoJfNzcbNUw8YlpiaibbibyNPiavYXG0bmp5e4fqWqxoTnialNMkNda9w0TgqXzuM2wA/640?wx_fmt=png&from=appmsg)

思考完毕的豆包输出了对这两款模型的评价｜图片来源：极客公园

思考过程的展示，让用户能够清晰地看到模型的推理步骤，而不仅仅是最终结果，这样一来，用户能够感受到模型的决策是有依据的，对模型输出的结果也会更有信任感。

***02***

******豆包 vs deepseek，各有千秋******

因为还在测试中，目前在豆包对话页面暂未显示「深度思考」功能的入口，输入消息时也没有像其他接入 deepseek 的产品一样有选择框可以选择是否开启「深度思考」功能，只是被灰度到的用户在问一些问题时会触发该功能。

我拿几个问题同时问了一下豆包和 deepseek，看下两者在「深度思考」上会有哪些不同表现。

**经典的数学问题：「9.11 和 9.9 谁大」**

先看下豆包的思考过程：

先说一下，在测试中，我发现豆包的「深度思考」模式出现得并不稳定，在第一次输入「9.11 和 9.9 谁大」后，它只是简单地回应了我一下：

![](https://mmbiz.qpic.cn/mmbiz_png/8cu01Kavc5YgsE4tcuHny9pxoJfNzcbNAPrtayMN6OtTk97gUR9XrcbeJZFicW1fDPRIH0NTAWq7j4JmnZlCe9g/640?wx_fmt=png&from=appmsg)

图片来源：极客公园

但在我又输入了一遍「9.11 和 9.9 谁大」想试试会不会触发「深度思考」模式时，还真出现了：

![](https://mmbiz.qpic.cn/mmbiz_png/8cu01Kavc5YgsE4tcuHny9pxoJfNzcbNUfaExSVpwziaACAo4BjzVK9FwYE4ZEPLzmeibvxCdbN4UFGl5bLO0Xow/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/8cu01Kavc5YgsE4tcuHny9pxoJfNzcbNChunFLrBdntP450bKDMetvX0VYCrVx4RibRiaQFrM4XWgMISI1BMyLBQ/640?wx_fmt=png&from=appmsg)

豆包详细地考虑了为什么我会第二次问它这个问题……｜图片来源：极客公园

可以看到，虽然豆包意识到刚刚已经回答过我，但它还是贴心地考虑了多种也许我没理解前面答案的可能性，然后再给出判断方法最后输出结果。

再看一下 deepseek 的思考过程：

![](https://mmbiz.qpic.cn/mmbiz_png/8cu01Kavc5YgsE4tcuHny9pxoJfNzcbNsrQRNAdCINepZEiaa2QT1e4hcLicEJAIBth0HkjQ7wWp59iaScvmO8d3g/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/8cu01Kavc5YgsE4tcuHny9pxoJfNzcbNY4KuLZubwNj1hia1zQz45R6KW8hib9sLBaptAh7t31wvVyuquUXpSDNA/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/8cu01Kavc5YgsE4tcuHny9pxoJfNzcbN8NJGyuMAQpjAPuQlKIWgnV77muVqU8TcbURWg8Le5UqaSvhYFOLKtg/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/8cu01Kavc5YgsE4tcuHny9pxoJfNzcbNKdjjrwR6Gg46AgVx5fiaNQ2mRuNibC3gpTlA9mvfGNzkSiaUlFJmwUPJw/640?wx_fmt=png&from=appmsg)

可以看出，虽然这是一个「看起来很简单」的问题，deepseek 的思考过程同样很详细，要比豆包的思考过程更全面。

在这个简单数学题上，豆包和 deepseek 都遵循了小数比较的基本规则，并采用多种方法验证；不同点在于豆包注重教学引导和考虑到用户可能的误解，而 DeepSeek 则更现自我质疑和反复验证，思考过程更复杂。

**哲学问题：意识的本质是什么？AI 会获得自我意识吗？**

先来看豆包的回答：

![](https://mmbiz.qpic.cn/mmbiz_png/8cu01Kavc5YgsE4tcuHny9pxoJfNzcbNbgia4HgCJ4ETfCbuBHR2gNRxaD5pzUKjxy8Y1NPEnqvGiaVWkO5zUgGA/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/8cu01Kavc5YgsE4tcuHny9pxoJfNzcbNIbtqQ5p8qjiaxu90Ynjsn3c3tVWicZBL4bYiccqPiahKDZe18gbXcpjibjg/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/8cu01Kavc5YgsE4tcuHny9pxoJfNzcbNiazV4wPfSNib0HHByh98Z4pbkA3MElO2fT7sm6uqMibq5sFVbcjCZqBoA/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/8cu01Kavc5YgsE4tcuHny9pxoJfNzcbN8wGZk1x2WvRvKtKSks7KiaXFhm63tmpMWLYzgTB7Y2WIYYHvEibj8dUg/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/8cu01Kavc5YgsE4tcuHny9pxoJfNzcbNChoGuC5IP8lKA4RcUXqkINV2eZ5f0FBTkRqzU0NYwEgoA6mmSjM87g/640?wx_fmt=png&from=appmsg)

再来看看 deepseek 的回答：

![](https://mmbiz.qpic.cn/mmbiz_png/8cu01Kavc5YgsE4tcuHny9pxoJfNzcbNwII7JTgibXNibM7CNLgicyQbtSTSULBE5RAicia9EP4vIY9HEp8591PfDjg/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/8cu01Kavc5YgsE4tcuHny9pxoJfNzcbNdIPZIia5ZQicvbFzbwCovzhIAHheOjicSVZlvCNfciaPiaJVnwic49pT9neg/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/8cu01Kavc5YgsE4tcuHny9pxoJfNzcbNhkBicVakia8gD5ibibwKHpzVzjVpQbzer4h5M3sP7YBoQK3NGM8HQzOJcw/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/8cu01Kavc5YgsE4tcuHny9pxoJfNzcbNLjcaZdRWqvj6ia0iaAQOMuR84AXSVLs2lAZl8qsYon5Zj9cvba3ic7oFA/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/8cu01Kavc5YgsE4tcuHny9pxoJfNzcbNI86sQTcQmbyOECxcicDTLibqeu84iaicnuy6wXLEiaibibWPnS1kibx2dBRZLw/640?wx_fmt=png&from=appmsg)

可以看出，DeepSeek 的回答分为科学理论、AI 意识路径、伦理框架和解决路径四个部分，引用了神经科学、量子理论等，还提到了法律案例和具体数据；而豆包的回答更偏向哲学理论分类，列举了物理主义、二元论等，并讨论了支持与反对 AI 权利的观点，不过没有深入技术细节。

两者都承认意识本质尚无共识，也都提到了哲学和科学理论、伦理问题，不同则在于深度和技术细节，DeepSeek 更技术导向，涉及神经形态计算、量子封印技术等，而豆包更侧重哲学流派和现有伦理指南。

通过本次实测，我们看到了豆包在深度思考模式上的初步表现，虽然目前处于测试阶段，且功能的稳定性和入口尚未完全开放，但其对推理过程的初步展示已为用户带来了更直观的理解路径。

\*头图来源：视觉中国

本文为极客公园原创文章，转载请联系极客君微信 geekparkGO

**极客一问**

**你认为豆包能超过 Deepseek 吗****？**

![](https://mmbiz.qpic.cn/mmbiz_png/8cu01Kavc5YTxYGib55rtMHhP1YJ44FLtVGp8Keyg6D2X3AUhgNicT1ibKKh0fE1eiaGqkSXnTlW0ib96ib3HDAIrnVA/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_png/8cu01Kavc5bXib8IGpjbghqj305kKeYibwJbLCR7ekIluWOwQhQdiaR8gj7ibC2JvhYKWq6fBeoqoNLSZTcuOMibFBQ/640?wx_fmt=png)

**![](https://mmbiz.qpic.cn/mmbiz_png/8cu01Kavc5an0KBXb9IbCwiajJefiaywlMX2G9daxebRIz0bpONcZbhCkA7mNIG39fwRUOEzpoBIPvAXIuA82B9Q/640?wx_fmt=png)

**热点视频****

马斯克：在特斯拉高管没有特权，流水线员工也能晋升高管。

点赞关注极客公园视频号，

观看更多精彩视频

**![](https://mmbiz.qpic.cn/mmbiz_png/8cu01Kavc5an0KBXb9IbCwiajJefiaywlMX2G9daxebRIz0bpONcZbhCkA7mNIG39fwRUOEzpoBIPvAXIuA82B9Q/640?wx_fmt=png)

**更多阅读****

[![](https://mmbiz.qpic.cn/mmbiz_png/8cu01Kavc5bt4pHibfwUSHvsTiavuNylgOAv7DZEf7XNhH13gYCV2bBcn5qvIESrk6jLLhcF1CODngFtPHmhECbg/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MTMwNDMwODQ0MQ==&mid=2653074301&idx=1&sn=d2aea29d33ebdadafde3347033dfc7d9&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/mmbiz_png/8cu01Kavc5bqq02BeTpFvgIH39r6UTHg8hCsEvqkuFWe8eqqYlNzr5hLTicSicIG5nL4BU056xpicd3WgxnjEXRdA/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MTMwNDMwODQ0MQ==&mid=2653074278&idx=1&sn=f855825f92ba2c9f049418b0255a9623&scene=21#wechat_redirect)

![](https://mmbiz.qpic.cn/mmbiz_gif/8cu01Kavc5ZENt3gIiatQKstoLiatpXoWBUwkB6tO2b9y2Hoj5HpcnXc5zRJEX6MhbyXJ3q0gjTrrBIUF7boJGDA/640?wx_fmt=gif)

![](https://mmbiz.qpic.cn/mmbiz_gif/8cu01Kavc5YR1a8dIHV2UrCdNIhialnevdQkialrf9oMibXZhuHeD0nPUHuFlYzYB4WYzwnTbhSyAvj9ibZb7ibewPw/640?wx_fmt=gif)‍

‍

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/8cu...