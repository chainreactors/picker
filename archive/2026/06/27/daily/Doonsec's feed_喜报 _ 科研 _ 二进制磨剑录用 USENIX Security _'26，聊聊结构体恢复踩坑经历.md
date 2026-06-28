---
title: 喜报 | 科研 | 二进制磨剑录用 USENIX Security \'26，聊聊结构体恢复踩坑经历
url: https://mp.weixin.qq.com/s/upTYkK-kaqbgtxYaGHX8FA
source: Doonsec's feed
date: 2026-06-27
fetch_date: 2026-06-28T06:10:29.924202
---

# 喜报 | 科研 | 二进制磨剑录用 USENIX Security \'26，聊聊结构体恢复踩坑经历

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/zxuXxbLaCLAuUhNakZMgficOxWmHFtFxO2OqvaGZw6eia9ZevBJgOiabTrK3A2hFL8OMcbaSgggLicWfDH9bmQM3xyj2qa8hPpsibQRnjDWjUHjY/0?wx_fmt=jpeg)

# 喜报 | 科研 | 二进制磨剑录用 USENIX Security '26，聊聊结构体恢复踩坑经历

原创

Yuxin Chen
Yuxin Chen

二进制磨剑

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

> USENIX Security Symposium 是国际网络与系统安全领域公认顶会，系统安全领域四大顶会之一，与 S&P、CCS、NDSS 并列，也是中国计算机学会（CCF）推荐的A类会议，长期深耕系统安全、软硬件安全、二进制程序分析、漏洞挖掘防御等前沿方向。USENIX Security 2026 将于2026年8月12日至14日在美国马里兰州巴尔的摩（Baltimore）举行。

有幸被 USENIX Security ’26 接收，

> RecStruct: Recovering Nested Struct Types from Stripped Binaries via Stack-Driven Unification

---

## 问题

![](https://mmbiz.qpic.cn/mmbiz_png/zxuXxbLaCLDqgO6tR8vPdiccd7VRcAI8UDzhuSIbnbwupkzWnCu5PpbuicaxmsoTau0cmcYOr37AyicUpz9JHicsn7S7gB2UXxF2nWyfhxQjQGg/640?wx_fmt=png&from=appmsg)

在二进制程序剥离符号（stripped）的编译流程中，源码层面清晰的嵌套结构体语义会完全丢失，仅保留底层内存偏移访问逻辑。

如这张示例图所示：源码里直观的多层结构体链式访问`a->b->c->c3`、`a->b->b2`，编译剥离符号后，在反编译结果中退化为多层指针偏移运算`*(*(*(a1 + 8) + 8LL) + 8LL)`、`*(*(a1 + 8) + 4LL)`。

此时逆向人员会面临一系列核心难题：

* • 无法还原结构体 A 自身的内存字段排布；
* • 无法厘清 A 所引用的多级嵌套结构体的层级与布局关系；
* • 结构体布局信息的缺失，会直接阻碍漏洞挖掘、程序功能分析等下游逆向工作的推进。

## 摘要

Recovering composite data types from stripped binaries is critical for reverse engineering and vulnerability analysis. Existing approaches either rely on heavyweight decompilers with limited type reasoning, or employ expensive constraint solvers that fail to scale. While some methods can handle nested structures, they struggle with large real-world binaries due to prohibitive computational costs. We present RecStruct, a fast type recovery framework that reconstructs nested structures without dependence on any decompiler. RecStruct lifts binaries directly, performs flow-insensitive symbolic execution to reduce memory aliases, and introduces Stack-Driven Unification—a novel union-find algorithm that maintains an offset stack during traversal to merge types only when their nesting depths align. This enables precise recovery of recursive structures. We implement an end-to-end pipeline and evaluate it on 418 binaries comprising 744,770 functions, including benchmarks from prior work and large-scale programs such as QEMU and OpenSSL. Experimental results demonstrate competitive accuracy compared to existing tools, with substantial improvements in efficiency and scalability, enabling analysis of binaries that were previously intractable.

---

从剥离符号的二进制程序中还原复合数据类型，是逆向工程、漏洞分析的核心基础。现有两类主流方案存在明显短板：一类依赖重量级反编译器，类型推理能力存在局限；另一类采用高开销约束求解器，很难适配大规模程序。部分方案虽支持基础嵌套结构，但面对真实大型二进制时，会因计算成本过高无法落地。

为此我们设计 RecStruct：一套不依赖反编译器、可高效重建嵌套结构体的类型恢复框架。框架直接对二进制做中间表示提升，借助流不敏感符号执行削减内存别名干扰；核心创新为**栈驱动合一（Stack-Driven Unification）**，该并查集算法在遍历过程维护偏移栈，仅在嵌套层级匹配时合并类型，以此精准还原递归结构体。

我们搭建完整端到端处理流水线，在包含 418 份二进制、总计 744770 个函数的数据集完成验证，数据集涵盖领域经典基准与 QEMU、OpenSSL 等大型工程。实验证明 RecStruct 精度对标现有主流工具，同时运行效率、可扩展性实现大幅提升，能够处理过往方案无法分析的大型二进制文件。

---

## 核心方法

结构体恢复的难点不在于识别单一基址偏移访问，而是不同函数仅能观测同一个结构体的局部片段；叠加多层指针后，内外层结构体、递归结构的依赖关系极易混淆。RecStruct 的核心目标，就是把分散在各函数中的局部内存访问证据，融合为全局统一、完整的结构体定义。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/zxuXxbLaCLC94MJk1ibZKqFfVOHQbw0cqM3VzH8A2mIsd8eycsEzeRR4wcjbbALiaficmfqiaGc5OroBQVVlBMFiau7cD2eHGGCP7hNpC65iaraz4/640?wx_fmt=png&from=appmsg)

会议召开后，我们将公布论文完整数据集、代码与文章。

预览时标签不可点

![]()

微信扫一扫
关注该公众号

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/FMiaMMfBpPgDs6JsyVq6ZxicHiaHutt2aBviba6ic3ews9EyFib8lE4N0h43Zu70DibLKSGfY8HGhicGo0a8446JrN0cDA/0?wx_fmt=png)

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