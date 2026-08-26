---
title: 用 AgentKit，5 分钟搭建云端安全隔离的 DeepSeek Harness
url: https://mp.weixin.qq.com/s/1qKTbU8guMKRACzeKG-oNg
source: Doonsec's feed
date: 2026-08-25
fetch_date: 2026-08-26T03:01:33.523812
---

# 用 AgentKit，5 分钟搭建云端安全隔离的 DeepSeek Harness

# 用 AgentKit，5 分钟搭建云端安全隔离的 DeepSeek Harness

AgentKit
AgentKit

字节跳动技术团队

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

近期，DeepSeek Harness 热度持续走高。尤其在 Coding Agent 场景中，它能够围绕代码库，快速完成代码理解、文件编辑、命令执行等多步开发任务，并提供 Web 界面和基础沙箱，帮助开发者高效搭建和体验 AI 编程智能体。

但当 Harness 从个人开发工具走向团队研发和企业生产，本地运行模式的局限也随之显现：

* **长任务难以稳定运行：**任务依赖个人电脑，休眠、关机或断网都可能导致执行中断。对于耗时数小时甚至更久的代码生成、构建和测试任务，本地环境很难提供稳定、持续的运行保障。
* **安全治理能力不足：**高权限 AK/SK、代码和运行数据分散在本地环境，既存在凭据泄露和越权风险，也缺少统一的身份认证、权限控制和操作审计。
* **部署与管理成本高：**从 Python、依赖包到模型配置，都需要在本地完成安装和调试，依赖冲突还可能污染开发环境；进入团队后，不同开发者的环境、配置和版本也难以统一，进一步增加维护和协作成本。

因此，要真正进入企业生产，还需要解决如何让 Agent 更安全、更稳定、更低成本地规模化“跑下去”。

**一句话定位：**面向想在**团队里试用 DeepSeek Harness、又怕搞坏本地环境、还不想先花大钱的研发团队**，AgentKit Sandbox 是一个云端隔离的智能体运行环境—— 5 分钟就能创建一个可跑  DeepSeek Harness沙箱，**随用随建、用完即弃，不碰本地任何配置、按量计费极低且与火山方舟 Coding Plan  / Agent Plan 无缝打通。**

**AgentKit Sandbox：让 Harness 在云端安全隔离、7×24 小时持续运行**

AgentKit 是火山引擎推出的企业级 AI Agent 基础设施平台，提供 Agent 开发、运行与治理的端到端能力，通过安全隔离的 Sandbox、统一身份与权限、运行治理及企业系统集成，让 Agent 在安全、可控、可观测的环境中持续运行，并真正融入企业业务流程。

其中，Sandbox 是承载 Agent 实际执行任务的核心运行环境。代码执行、命令调用、浏览器操作等任务都可以在独立的云端沙箱中完成，不再依赖个人电脑。

针对本地运行的局限，AgentKit Sandbox 提供：

* **安全隔离：**基于 microVM 构建独立执行环境，将代码、命令和浏览器操作限制在受控空间内
* **云端持续运行：**任务不依赖个人电脑，本地关机或断网也不会影响云端执行
* **按需创建与回收：**Sandbox 可按任务创建，并支持自动或手动回收，降低长期资源占用
* **会话状态管理：**任务过程中可复用上下文和文件状态，会话结束后及时释放环境
* **统一身份鉴权：**与身份权限体系打通，减少敏感凭据硬编码和本地散落带来的安全风险

除此之外，这种云端运行方式并不意味着更高的资源成本。以 2 vCPU / 4 GB 规格为例，Sandbox 每小时成本约 0.9 元，并支持按秒计费。即使一个 5 人团队每天每人使用 2 小时，持续一个月，计算资源成本也仅需 200 元左右。

**快速体验：基于AgentKit，5分钟安装云端DeepSeek Harness**

前置条件：

* 请确认已完成火山引擎**账号注册**和**实名认证**，并确保账户未欠费。
* 已**开通火山方舟模型服务**。

**操作步骤**

**步骤 1**

登录AgentKit控制台，并根据引导开通产品

控制台地址：

https://console.volcengine.com/AgentKit

![](https://mmbiz.qpic.cn/sz_mmbiz_png/FGB4hYw9FefkpfV42a7VngzV90UKajEa1GFw6EQuh6kVicicPZCdCttulRTwQrNb0jl50w3Vt8UOe75pwGBK2wZDBMJvw0icwkEOMMvNn9RricA/640?wx_fmt=png&from=appmsg)

**步骤 2**

进入「沙箱模板」，点击「创建沙箱模板」

![](https://mmbiz.qpic.cn/sz_mmbiz_png/FGB4hYw9FefHhrv219890xLcJribFLVQS9fg1cBfhwTvl8tGWRiczFaJfc318HVcSum5BY879x8Oz1eqO9UCqTO5FREPgDkYibw2Gbb0eKLnAQ/640?wx_fmt=png&from=appmsg)

**步骤 3**

重点填写以下信息，其他保持默认即可，点击提交

* 基本信息-类型：选择 Code Sandbox
* 模型与技能配置：

+ 如果你已订购Coding Plan / Agent Pla，可选择该选项
+ 如果仅仅开通了方舟模型服务，则选择模型广场

![](https://mmbiz.qpic.cn/mmbiz_png/FGB4hYw9FedrDEPShMu3EjNJJuklfEsbxbPQgCR8icxqrV2JVn2JXMWF60wbaC24v3vib0Z5GQZML7XHX2EqGu8L4YU2tKIXAOy0a3XPXwBic4/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/FGB4hYw9Fefx3DjrXrJa6Wlic6vjQPJZ6XZrVicpZSqGHIpSiawnWrasXYjNibA7Bgxa3DbfQ3I0iaQmu4t6w3wVStI7QvxTV8v9qYTJb4JlPw1M/640?wx_fmt=png&from=appmsg)

**步骤 4**

等待沙箱创建，约1分钟左右，直到状态显示「运行中」

![](https://mmbiz.qpic.cn/mmbiz_png/FGB4hYw9FefZCyRIqTm3s37zm3NFWtK4icfGicZWbhWHBANYZoYPLtCWcjzlB6XerXqcVtFRI0iaWibRj6vIicM7nezfTdI3iatcwo9BQibfEFFL6A/640?wx_fmt=png&from=appmsg)

**步骤 5**

点击已创建沙箱名称，进入「实例管理」，创建一个实例，执行时长设置为 10800 秒

![](https://mmbiz.qpic.cn/mmbiz_png/FGB4hYw9Fefic8gVXfd1pEIo7RvvVUZNubuHWQXcVeywasqnAwqdQZIe7Fut3zBEKffPOTK8PPcCMviaWp5ZicPq7lcdFk1EnP4pQu1OETpGb4/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/FGB4hYw9FedqzQOsHtCRUicibTmmSCic9Wickjn0fJIC8sthOTNia0UjJxFz6jSAL2iboCtACw6HAunia8qClosD9Du7zctJKZcbuvxWJibxebQFhnU/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/FGB4hYw9FeeNnoVAAJJYoejUNsDEyB8ALRlvKEexERRPQAyiaYQDkhBcemCJYIB1x7PPsrUj7UbBdD8d8N9fPekjYrPqzJnvVdk4XkJKSans/640?wx_fmt=png&from=appmsg)

**步骤 6**

复制 公网访问地址到浏览器

![](https://mmbiz.qpic.cn/sz_mmbiz_png/FGB4hYw9FefQQG1WuqCcribqPRU1n5RAGBl6jDbskEXektRg00LvHe8Hk14y1AqlYaUECia3axcpSX3w8KZdTxKcofrrDhLecaNEgaibKGPHMM/640?wx_fmt=png&from=appmsg)

**步骤 7**

完成 DeepSeek Harness 云端部署

![](https://mmbiz.qpic.cn/mmbiz_png/FGB4hYw9FeeObmEXjChdwEys2aJLmwz4PibNPQ0w8jNBZ2LUq0lelK0XRn6wLs8XXzJ6BStIrl6eic96yTaLqAyxOkEJvkXs6g1lEBIlbibr30/640?wx_fmt=png&from=appmsg)

**步骤 8**

用DeepSeek Harness执行一个任务：

在执行任务之前，如果你想将产物持久化保存，可以先挂载火山引擎TOS（对象存储）

* 开通火山引擎TOS，并创建桶

![](https://mmbiz.qpic.cn/mmbiz_png/FGB4hYw9FeeZQW3xzvgEvA7WmGCBVziav5AdibeibFJAiauEpLospuGgwiamPS5nvStAxX1w5adia7MlHI55Tvp5VZZLnnbpKW0j60zrdDUBUCjDc/640?wx_fmt=png&from=appmsg)

* 回到AgentKit控制台-沙箱模板-实例管理-配置信息-存储，Bucket选择你在TOS创建的桶，即可完成挂载

![](https://mmbiz.qpic.cn/sz_mmbiz_png/FGB4hYw9FefjYHCMhh98giaztkAHldA8VzalcYQgJDG7M6941Zgy6nHfd93ZAGvqA22YDVicCc7jfX0JCzSyWSQPjPcYB7xHJgLwPTIc3jWqY/640?wx_fmt=png&from=appmsg)

**步骤 9**

用DeepSeek Harness执行一个任务：

输入任务要求：

执行任务：帮我模拟一份某电商公司 6 个月的销售数据（含月份、销售额、订单量、退货率、区域），用 Python 做数据分析，并生成一份 HTML 可视化报告：包含关键指标卡片、销售额趋势折线图、区域占比饼图，以及一段自动总结的分析结论。最终产物帮我上传到TOS中。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/FGB4hYw9FeefWJpWnsVyTqP02SHm5x9QfREf4ko9jeTnJAxDybCUZ5EI9oH8BFj8FAg2icEJznyN8GtaxzhRoYs2icwd78arzyuBiaWicl5RJa4/640?wx_fmt=png&from=appmsg)

**步骤 10**

用DeepSeek Harness执行一个任务：

回到火山引擎TOS中下载产物，打开即可看到最终效果

![](https://mmbiz.qpic.cn/mmbiz_png/FGB4hYw9FefSxIedfSo2eB3zK20SGjvU3g9L8nyUiaG5L0mWh9MWzfbIOjfrSMdWJz1c3uHhgI0yYcUqHH3NA9lnuZibv84Iy4kSBndvsxA3Q/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/FGB4hYw9Fef0fVYkJeiaQxpct96xS5DHCx3AEKyYV2uWQYwhLd4liaIv5FRY9CuWXypUqeMgFPDdar3vY8UdsRPn6eWehibu4PAazTwmicnUHDc/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/FGB4hYw9Fedvl6fK50Pd4u7V5esYrcYeaIBeicojubOq8qcNXftJibWCXlYIc1tlqO5k3mgZkEFOvIM9eD5MDKa04wzL5w4fGpDvcdQVJfBicI/640?wx_fmt=png&from=appmsg)

**深入使用：从「快速验证」走向「企业生产」**

当 Agent 开始真正进入团队和业务流程，你可能会进一步面临这些需求：

* **统一管理多个 Coding Agent：**不同项目、不同开发者的 Agent 集中管理，避免环境、配置和版本各自维护
* **支撑长时间开发任务：**让代码生成、构建、测试、调试等任务在云端持续运行，不受本地关机、断网影响
* **保障代码与凭据安全：**统一管理代码仓库、API Key 和系统权限，并对 Agent 的操作全程留痕、可审计
* **融入真实研发流程：**连接代码仓库、CI/CD、Issue 等研发工具，让 Agent 从“写一段代码”走向完整的软件工程流程

这时，就需要进一步使用 AgentKit 完整的企业级能力。AgentKit 提供覆盖身份、工具、运行时与治理的端到端能力，让 Coding Agent 在安全、可观测、可靠的环境中持续完成开发任务，真正实现从“个人 Coding Demo”到“企业级 AI 开发生产力”的升级。

想进一步了解 AgentKit 的完整能力与使用方式，可点击文末**「阅读原文」**，进入 AgentKit 官网了解详情。

预览时标签不可点

阅读原文

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/5EcwYhllQOhkoWTP1gVm0Lqs480XOARyoSYjPEsRVCSF35cbWIp6cliaYic8KUfNfiaSjVnruzTQUTCA0lmv9vUmw/0?wx_fmt=png)

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