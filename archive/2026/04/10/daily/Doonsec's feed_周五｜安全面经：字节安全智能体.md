---
title: 周五｜安全面经：字节安全智能体
url: https://mp.weixin.qq.com/s/U61AjV62EXDbNBpw-wdrzA
source: Doonsec's feed
date: 2026-04-10
fetch_date: 2026-04-11T04:15:19.116501
---

# 周五｜安全面经：字节安全智能体

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/z0u4bSRUopOKs7WmmiaT4h8DS7KBCLQjZdncz3LA2ZjCOjzvuDib0XT7n5HHEFMS3MnEsZ3GZmianKsPnmxK25ibg28pUGWeDmTzRPZCYfKNbks/0?wx_fmt=jpeg)

# 周五｜安全面经：字节安全智能体

原创

heyong
heyong

AI安全圈

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

网友@花生的字节安全智能体一面复盘

- 流程：
- 个人项目介绍
- 问答环节：
- 基础内容:
- 不同 agent 架构差别比较：
- 根据我的知识背景，问了 agent flow, react 和 multi-agent 三者的差别
- LLM 如何预测下一个词
- 现有 agent 实践上：
- 不同 agent 使用体感差别在哪里，有哪些优势和不足
- 回答准确点：model routing 上
- file system 是什么？它起到什么作用？使用它相比其他传统的 agent 好在哪里？
- skills 相比于传统 agent 好处在哪里？工具 skills 和产品 skills 如何理解，差别在哪里？
- openclaw 有没有用过，它为什么会火爆？技术 or 架构上做对了什么？
- 知不知道最近的 harness engineering？
- 由于任务表述并不清晰，不同 agent 对于同一任务的表现并不完全一致，如何处理这个问题？
- 对未来工程架构上的理解：
- 对于 agent 未来 to C 和 to B 在技术和架构上觉得未来可能会有什么发展
- 其他：
- 最近看了些什么新的内容可以分享？
- 反问：
- 工具skills 和产品 skills 如何理解，差别在哪里？为什么需要这么做？
- 上述极大依赖于 model routing (or 主 agent 能力) ，目前工程上是否真的做的足够好？

- 初步复盘：
- 知识储备上：
- 对于 agent 实践的背后原理并不熟悉，而仅仅体现在应用；同时，对于应用本身的经验和体悟并不深入，为什么它们做好 or 做不好某个任务并没有深入思考总结
- 对于前沿新技术并没及时 update 到
- 语言表达上：
- 回答有些杂糅：
- 原因：没有优先初步梳理回答的方向，并且根据方向组织自己的回复，而是仅仅凭借直觉回答
- 结果：
- 分要点回答时，不同 要点 之间关系杂糅（甚至可能是同一个要点），意识到时回复有些卡壳➕心虚
- 不熟悉的问题，回答比较含糊
- 认知上：
- 工程实践 ”不仅要考虑效果，还需要考虑规模化”，未来可以从这两个视角来出发分析问题

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/0R80na6wzXdZWBKECSwo8H5S6LNZvXaLNemfgTALpBNqL3VpUlA3mQtwfrEoIh2LHb1zJuv8A5z0Jo60tH7pgw/0?wx_fmt=png)

AI安全圈

向上滑动看下一个

知道了

![]()
微信扫一扫
使用小程序

取消
允许

取消
允许

取消
允许

×
分析

![跳转二维码]()

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/0R80na6wzXdZWBKECSwo8H5S6LNZvXaLNemfgTALpBNqL3VpUlA3mQtwfrEoIh2LHb1zJuv8A5z0Jo60tH7pgw/0?wx_fmt=png)

微信扫一扫可打开此内容，
使用完整服务

：
，
，
，
，
，
，
，
，
，
，
，
，
。

视频
小程序
赞
，轻点两下取消赞
在看
，轻点两下取消在看
分享
留言
收藏
听过