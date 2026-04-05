---
title: AI Agent 架构中的四个核心概念
url: https://mp.weixin.qq.com/s/547v4eGeWOAmw-6rJ5bmng
source: Doonsec's feed
date: 2026-04-04
fetch_date: 2026-04-05T04:33:43.630967
---

# AI Agent 架构中的四个核心概念

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/Hh1PYgqfZnvTrJmywQ9ickibROBSgMIa3flNgXleyZ5Yy43jnrMibrbMVDzBq6kVGurwqgVl0rAiaZffBLSc1jy8bj6dmKsjROfcGo73Tb7dtdU/0?wx_fmt=jpeg)

# AI Agent 架构中的四个核心概念

原创

刁
刁

KeepHack1ng

![]()

在小说阅读器中沉浸阅读

随着 AI 从单轮对话系统演进为多步骤、自主执行的 Agent 系统，其核心问题不再是“如何写 Prompt”，而是“如何构建一个稳定的信息系统”。在这一过程中，Sub-agent、Context Engineering、上下文隔离、记忆系统成为基础能力。

本文从工程视角，对这四个概念进行系统性梳理。

![](https://mmecoa.qpic.cn/mmecoa_gif/t229OYlZTuibdWiczD6mQsbW8yOLXjVq91cjJvX7N5EgJ3OHtZY1FsYmWIwk2ARsKT5y8fxeku9mYYy9UhoOickZH8NKnAk1rlUlof6N27eBaU/640?from=appmsg)

01

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/CR1RM74K0cLWUbubqqy39LJG1IYEWlfRIy6GFK3D3OQ7b85q450eNyRDhEyWFRthbficia3sHxNBfOEz9Uhb7AC5o8UtWrAp3RbHTE1JcLvyc/640?from=appmsg)

AI Agent 的本质

![](https://mmbiz.qpic.cn/mmbiz_png/258NgbMqbciaMYPiaJG5Mib74JhsWe9dOZt04nd1BjT5hf1EenWGT2rpX5HVHUgDFibrRia1ibyEDxyQnjEOOznicWumBJPF4jUAmCOviaaPwo1p7nc/640?from=appmsg)

AI Agent 是一种能够在复杂环境中进行感知、决策和执行的系统，通常具备规划、记忆和行动能力 。

与传统模型不同，Agent 的行为不是单次生成，而是由连续的上下文驱动。因此：

>核心问题从“生成能力”转向“上下文管理能力”。

![](https://mmecoa.qpic.cn/mmecoa_gif/t229OYlZTuibdWiczD6mQsbW8yOLXjVq91cjJvX7N5EgJ3OHtZY1FsYmWIwk2ARsKT5y8fxeku9mYYy9UhoOickZH8NKnAk1rlUlof6N27eBaU/640?from=appmsg)

02

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/CR1RM74K0cLWUbubqqy39LJG1IYEWlfRIy6GFK3D3OQ7b85q450eNyRDhEyWFRthbficia3sHxNBfOEz9Uhb7AC5o8UtWrAp3RbHTE1JcLvyc/640?from=appmsg)

Sub-agent：任务拆分与执行单元

![](https://mmbiz.qpic.cn/mmbiz_png/258NgbMqbciaMYPiaJG5Mib74JhsWe9dOZt04nd1BjT5hf1EenWGT2rpX5HVHUgDFibrRia1ibyEDxyQnjEOOznicWumBJPF4jUAmCOviaaPwo1p7nc/640?from=appmsg)

Sub-agent 是多 Agent 架构中的基本执行单元。

在复杂任务中，系统通常采用层级结构：

* 主 Agent 负责规划与调度

* 子 Agent 负责具体任务执行

这种结构本质上是一种任务分解机制。智能体可以被组织为多个子代理，每个子代理负责低层功能，共同完成复杂目标 。

其核心作用包括：

* 降低单个 Agent 的复杂度

* 避免上下文过载

* 支持并行执行

实践中，一个完整系统往往由多个专职子 Agent组成，例如检索、分析、生成、执行等不同角色。

![](https://mmecoa.qpic.cn/mmecoa_gif/t229OYlZTuibdWiczD6mQsbW8yOLXjVq91cjJvX7N5EgJ3OHtZY1FsYmWIwk2ARsKT5y8fxeku9mYYy9UhoOickZH8NKnAk1rlUlof6N27eBaU/640?from=appmsg)

03

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/CR1RM74K0cLWUbubqqy39LJG1IYEWlfRIy6GFK3D3OQ7b85q450eNyRDhEyWFRthbficia3sHxNBfOEz9Uhb7AC5o8UtWrAp3RbHTE1JcLvyc/640?from=appmsg)

Context Engineering：上下文工程

![](https://mmbiz.qpic.cn/mmbiz_png/258NgbMqbciaMYPiaJG5Mib74JhsWe9dOZt04nd1BjT5hf1EenWGT2rpX5HVHUgDFibrRia1ibyEDxyQnjEOOznicWumBJPF4jUAmCOviaaPwo1p7nc/640?from=appmsg)

Context Engineering 是 Agent 系统的核心设计能力。

定义：为模型在每一步提供“恰当的信息集合”，而不是简单构造 Prompt 。

其范围包括：

* 系统提示词

* 历史对话

* 外部检索数据

* 工具调用结果

* 记忆系统输出

本质是对“模型输入环境”的整体设计。

研究表明，Agent 的性能高度依赖上下文质量，而不是上下文规模。过多无关信息会显著降低效果 。

工程上通常包含四类操作：

1. 选择信息
2. 组织结构
3. 压缩内容
4. 控制输入边界

其目标是：

![](https://mmbiz.qpic.cn/mmbiz_png/yLf5YKBxcTpp7gvJdBnPabAca0r11IDmvmAtHBgDJcJOXJ64P7UbdbYDEh8jVjrdVYP0MGUoQfpFUuNyZnNmOicyWwwmXXVDf2BINd5ek19g/640?from=appmsg)

在有限上下文窗口中，最大化有效信息密度。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/4fQhRs8GnLS117JOAqp0hicGtcbjeNSZsjC8Wl2p1Ng9xMuv7wOQfcTThuO0op04J4et8NNVRTSiaNsM0YEn3DQ5GyYN7Ug1IltSjCsfCxsxs/640?from=appmsg)

![](https://mmecoa.qpic.cn/mmecoa_gif/t229OYlZTuibdWiczD6mQsbW8yOLXjVq91cjJvX7N5EgJ3OHtZY1FsYmWIwk2ARsKT5y8fxeku9mYYy9UhoOickZH8NKnAk1rlUlof6N27eBaU/640?from=appmsg)

04

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/CR1RM74K0cLWUbubqqy39LJG1IYEWlfRIy6GFK3D3OQ7b85q450eNyRDhEyWFRthbficia3sHxNBfOEz9Uhb7AC5o8UtWrAp3RbHTE1JcLvyc/640?from=appmsg)

上下文隔离：安全与稳定性的核心机制

![](https://mmbiz.qpic.cn/mmbiz_png/258NgbMqbciaMYPiaJG5Mib74JhsWe9dOZt04nd1BjT5hf1EenWGT2rpX5HVHUgDFibrRia1ibyEDxyQnjEOOznicWumBJPF4jUAmCOviaaPwo1p7nc/640?from=appmsg)

上下文隔离是指：

![](https://mmbiz.qpic.cn/mmbiz_png/yLf5YKBxcTpp7gvJdBnPabAca0r11IDmvmAtHBgDJcJOXJ64P7UbdbYDEh8jVjrdVYP0MGUoQfpFUuNyZnNmOicyWwwmXXVDf2BINd5ek19g/640?from=appmsg)

不同任务、不同 Agent 之间的上下文必须严格分离。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/4fQhRs8GnLS117JOAqp0hicGtcbjeNSZsjC8Wl2p1Ng9xMuv7wOQfcTThuO0op04J4et8NNVRTSiaNsM0YEn3DQ5GyYN7Ug1IltSjCsfCxsxs/640?from=appmsg)

这一机制来源于实际安全问题。研究指出，Agent 在执行过程中如果直接共享上下文，会导致以下风险：

* Prompt 注入在系统中持续传播

* 外部数据污染决策过程

* 敏感信息跨任务泄露

标准工程实践包括：

* 子 Agent 在独立上下文中运行

* 主 Agent 不直接接收子 Agent 的原始过程数据

* 只允许结构化结果跨上下文传递

这一机制类似操作系统中的进程隔离，其本质是：

![](https://mmbiz.qpic.cn/mmbiz_png/yLf5YKBxcTpp7gvJdBnPabAca0r11IDmvmAtHBgDJcJOXJ64P7UbdbYDEh8jVjrdVYP0MGUoQfpFUuNyZnNmOicyWwwmXXVDf2BINd5ek19g/640?from=appmsg)

限制信息传播路径，而不是限制能力本身。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/4fQhRs8GnLS117JOAqp0hicGtcbjeNSZsjC8Wl2p1Ng9xMuv7wOQfcTThuO0op04J4et8NNVRTSiaNsM0YEn3DQ5GyYN7Ug1IltSjCsfCxsxs/640?from=appmsg)

![](https://mmecoa.qpic.cn/mmecoa_gif/t229OYlZTuibdWiczD6mQsbW8yOLXjVq91cjJvX7N5EgJ3OHtZY1FsYmWIwk2ARsKT5y8fxeku9mYYy9UhoOickZH8NKnAk1rlUlof6N27eBaU/640?from=appmsg)

05

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/CR1RM74K0cLWUbubqqy39LJG1IYEWlfRIy6GFK3D3OQ7b85q450eNyRDhEyWFRthbficia3sHxNBfOEz9Uhb7AC5o8UtWrAp3RbHTE1JcLvyc/640?from=appmsg)

记忆系统：跨时间的信息能力

![](https://mmbiz.qpic.cn/mmbiz_png/258NgbMqbciaMYPiaJG5Mib74JhsWe9dOZt04nd1BjT5hf1EenWGT2rpX5HVHUgDFibrRia1ibyEDxyQnjEOOznicWumBJPF4jUAmCOviaaPwo1p7nc/640?from=appmsg)

记忆系统用于解决 Agent 的长期一致性问题。

通常分为两类：

短期记忆

* 当前任务上下文

* 对话历史

长期记忆

* 用户信息

* 历史行为

* 外部知识库

记忆使 Agent 能够在多轮交互中保持连续性，是系统稳定运行的基础组件 。

但记忆也引入新的问题：

* 上下文膨胀

* 信息噪声累积

* 记忆污染

因此，现代系统普遍采用“按需检索”机制，而不是直接将所有记忆注入上下文。

![](https://mmecoa.qpic.cn/mmecoa_gif/t229OYlZTuibdWiczD6mQsbW8yOLXjVq91cjJvX7N5EgJ3OHtZY1FsYmWIwk2ARsKT5y8fxeku9mYYy9UhoOickZH8NKnAk1rlUlof6N27eBaU/640?from=appmsg)

06

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/CR1RM74K0cLWUbubqqy39LJG1IYEWlfRIy6GFK3D3OQ7b85q450eNyRDhEyWFRthbficia3sHxNBfOEz9Uhb7AC5o8UtWrAp3RbHTE1JcLvyc/640?from=appmsg)

四者之间的关系

![](https://mmbiz.qpic.cn/mmbiz_png/258NgbMqbciaMYPiaJG5Mib74JhsWe9dOZt04nd1BjT5hf1EenWGT2rpX5HVHUgDFibrRia1ibyEDxyQnjEOOznicWumBJPF4jUAmCOviaaPwo1p7nc/640?from=appmsg)

这四个概念并非独立，而是构成一个完整的 Agent 运行体系：

* 记忆系统提供可用信息

* Context Engineering 负责筛选与组织

* 上下文隔离控制信息边界

* Sub-agent 在受控上下文中执行任务

可以理解为：

* 记忆是数据来源

* 上下文工程是信息调度

* 上下文隔离是安全机制

* 子 Agent 是执行单元

![](https://mmecoa.qpic.cn/mmecoa_gif/t229OYlZTuibdWiczD6mQsbW8yOLXjVq91cjJvX7N5EgJ3OHtZY1FsYmWIwk2ARsKT5y8fxeku9mYYy9UhoOickZH8NKnAk1rlUlof6N27eBaU/640?from=appmsg)

07

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/CR1RM74K0cLWUbubqqy39LJG1IYEWlfRIy6GFK3D3OQ7b85q450eNyRDhEyWFRthbficia3sHxNBfOEz9Uhb7AC5o8UtWrAp3RbHTE1JcLvyc/640?from=appmsg)

核心结论

![](https://mmbiz.qpic.cn/mmbiz_png/258NgbMqbciaMYPiaJG5Mib74JhsWe9dOZt04nd1BjT5hf1EenWGT2rpX5HVHUgDFibrRia1ibyEDxyQnjEOOznicWumBJPF4jUAmCOviaaPwo1p7nc/640?from=appmsg)

AI Agent 的本质不是更强的模型，而是更复杂的信息系统。

系统能力取决于：

1. 是否能提供正确的信息
2. 是否能控制信息流动
3. 是否能限制错误传播

在多 Agent 架构中，问题的关键不在于推理能力，而在于上下文管理能力。

>谁控制上下文，谁就控制 Agent 的行为。

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/JCAnUicSia7ic0BMxHx2tqGXtibPwvTUNZeq3gs8YgniaOG30TgicqiauktfUgibahESB1HS530df9wMwkpZL9Jw3FZlCg/0?wx_fmt=png)

KeepHack1ng

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/JCAnUicSia7ic0BMxHx2tqGXtibPwvTUNZeq3gs8YgniaOG30TgicqiauktfUgibahESB1HS530df9wMwkpZL9Jw3FZlCg/0?wx_fmt=png)

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