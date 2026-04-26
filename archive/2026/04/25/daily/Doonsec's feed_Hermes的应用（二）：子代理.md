---
title: Hermes的应用（二）：子代理
url: https://mp.weixin.qq.com/s/RMARoT-Q_Y8Px_RE1ivzKg
source: Doonsec's feed
date: 2026-04-25
fetch_date: 2026-04-26T04:58:33.374264
---

# Hermes的应用（二）：子代理

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/2PhZXrB0gN4uicQA25Yknen9bTewXKErnaLVSOSlbWcK8icYQeElz4kPjOvBL0h4PuROzTeRyQqBsPV6L5u4GibWTaccUEeibaYM5x0zuq6TuGk/0?wx_fmt=jpeg)

# Hermes的应用（二）：子代理

原创

MicroPest
MicroPest

MicroPest

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

一、联动openclaw

本来的设想是这样的：

用户消息 → OpenClaw Gateway → Hermes Agent 处理 → 响应

搞了一段时间，才发现真没有必要，“卧龙、凤雏”得一即可。

既然现在到hermes了，还是继续啦。

二、子代理开展工作

给它部署了三项工作：

（1）“帮我研究一下市面上的主要AI Agent框架，写一份分析报告，并开发一个简单的Demo来对比它们”。

（2）“开发一个待办事项Web应用”。

（3）“对比分析最新版Llama和Qwen模型在数学推理基准上的表现，并引用近三个月的论文数据”。

它立刻进行了理解，并询问我的要求：

![](https://mmbiz.qpic.cn/mmbiz_png/2PhZXrB0gN4LTUyTPt6T5yUJicAVMUfr6n3efxEuL3yS9pibBFAibwA7M9bnvic7kbUwZhkeIXz70wu478hwkhItbWXFfsiavKnyO7rGSQq6juQQ/640?wx_fmt=png&from=appmsg)

。。。。。。

完成结果如下：

    让我确认一下：

    - 任务1: ✅ AI Agent框架分析 + Demo - 完成

    - 任务2: ✅ 待办事项Web应用 - 完成

    - 任务3: ✅ Llama vs Qwen基准对比 - 完成 (但有图表限制)

   提供一个结构化的报告，包括：

    1. 任务概述

    2. 执行方式（如何并行）

    3. 各任务结果摘要

    4. 交付物清单

    5. 问题与解决（如图表库缺失）

    6. 性能评估（时间、资源）

    7. 建议与后续

    报告日期: 2025-04-24

    执行方式: 独立Hermes进程并行

    总任务数: 3

    成功率: 100% (3/3)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2PhZXrB0gN6tuzqju2Lcib6u7DMMkA6CTKUAngIHMdouKNsaviandnxKTmRYPibtQArqa7icSdksJYKfdabhH22R9f6TmiclbEm8BRLplh0WCibNs/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2PhZXrB0gN5kerRLTOSNlxc1b3QvBQvxhLEVUVrClj3EfrstoGLARoJKHlpPQYc2vicH9Pq7mYCLQ5MCicx1cn4H6StFj87e2FkRH3GvXXkF0/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/2PhZXrB0gN4srjibbGZFMdKjRts59SibcMIM0jp8Mrec7NgBRdSRksIACeBguEias7y2aibOmtMYW8KguhKeZpv9QicXuEQsBpF5KBkqFRF30RDU/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2PhZXrB0gN4ryLyNpTibMkHgibSLvPpgyX07Kba1R4b5m8ckOlXXyOkGCJNDckA3Tb0tFHg46hCC5EA83Spon3WXh3j77bDXQYLeibM2icp20XM/640?wx_fmt=png&from=appmsg)

三、专家意见（deepseek V4评判）

看了你的以上执行报告，这三个任务的质量和团队协作方式可以这样来看：

## （一）、任务交付质量总评

| 任务 | 完整性 | 可用性 | 文档 | 专业深度 | 总评 |
| --- | --- | --- | --- | --- | --- |
| T1 – AI Agent 框架分析 + Demo | ✅ 覆盖全面 | ✅ Demo 可直接运行 | ✅ 阅读与运行指南完整 | ✅ 13 维度对比 + 选型矩阵 | ⭐⭐⭐⭐⭐ |
| T2 – 待办事项 Web 应用 | ✅ 前后端功能完备 | ✅ Docker 一键部署，生产就绪 | ✅ README、API 文档、架构说明 | ✅ 全栈实现，代码规范 | ⭐⭐⭐⭐⭐ |
| T3 – Llama vs Qwen 基准对比 | ✅ 数据准确、覆盖面广 | ✅ 分析报告可用 | ✅ 数据文件完整、可复现 | ✅ 关键洞察到位，但缺少专业图表 | ⭐⭐⭐⭐ |

**结论：整体完成度非常高。**

* T1、T2 质量几乎无可挑剔，交付物可直接用于研究或部署。
* T3 的分析深度和洞察力很强，唯一短板是**图表可视化**受限于当时的运行环境（缺少 matplotlib/pandas），用了 Unicode 条形图替代，但数据表和分析本身依然扎实。如果需要，后续花几分钟补上专业图表就能达到 5 星水准。

---

## （二）、三个代理之间的“协作”情况分析

严格来说，**这次并没有发生真正的代理间协作**，而是一种“由主控进程（你）发起的独立并行”。

### 1. 实际执行方式

```
主进程（你）├─ 子进程 A → T1（AI Agent框架分析）├─ 子进程 B → T2（待办事项Web应用）└─ 子进程 C → T3（基准对比）
```

三个 `hermes chat -q` 通过独立 terminal 后台启动，各自的会话、内存、工具、文件系统完全隔离。

### 2. 代理间互动等级：0

* ✖ **无任务依赖传递**：T1 的结果没有实时输入给 T2 或 T3。
* ✖ **无中间通信**：进程间没有消息队列、共享内存或结果交换。
* ✖ **无动态任务再分配**：如果一个子代理先完成，不会去帮助另一个。

因此，这次实现的是**并行独立执行**，而不是多代理协作。报告中也注明了“进程间通信需手动协调（未使用）”。

### 3. 这种模式的优势与局限

**优势**

* 隔离性极强：一个任务失败完全不影响其他任务，报告里也验证了这一点。
* 无阻塞：真正同时推进，总耗时约等于最慢任务的耗时，效率提升 2.6 倍。
* 实现简单：不需要复杂的 ACP（Agent Communication Protocol）配置，直接用 shell 启动即可。

**局限**

* 无法处理需要**代理间相互依赖**的复合任务（例如：T2 需要实时读取 T1 的报告数据，或者 T3 需要 T1 采集的网页数据作为输入）。
* 没有“团队合作”的沟通痕迹，更像三个完全独立的专家各干各的，最后你把结果汇总。

---

## （三）、总结与建议

* **质量**：非常高，属于高价值交付。
* **协作**：名义上是“三个代理”，但实际是**并行独立执行**，没有协作。这种模式适合**无依赖的独立任务**，如果要实现真正的多代理协作（比如动态分拆子目标、互相审阅、流水线式知识传递），需要启用 Hermes 的 `delegate_task` + ACP，或自己设计进程间通信管道。

简单来说：**产出优秀，但“团队”其实并没有在一起工作，更像三个独立专家同时开工。** 如果后续任务需要深度协同（例如一个代理做研究、另一个把研究结果写成代码、第三个负责测试），就值得启用内置的子代理委派和通信机制了。

总结：专家点评的很到位，这三个任务是各代理独立并行完成，三者之间没有产生交互协作，这可能跟我们的题目不需要协作有关，但产出优秀，质量很高。后面我们会再来一些相关内容的测试。

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/2hnvgPYNzpI857XC5Kft3W5TyR4cickrqaIUibKveibjF4531l9HGGu8dISFz0Yr6OUkCHfulChWC2acVmh4b39dg/0?wx_fmt=png)

MicroPest

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/2hnvgPYNzpI857XC5Kft3W5TyR4cickrqaIUibKveibjF4531l9HGGu8dISFz0Yr6OUkCHfulChWC2acVmh4b39dg/0?wx_fmt=png)

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