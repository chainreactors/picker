---
title: 从告警积压到持续调查，AI Agent正在重写SOC工作流
url: https://mp.weixin.qq.com/s/MOUSekPpkWt_7lmIK4tjmw
source: Doonsec's feed
date: 2026-08-28
fetch_date: 2026-08-29T08:29:28.763307
---

# 从告警积压到持续调查，AI Agent正在重写SOC工作流

# 从告警积压到持续调查，AI Agent正在重写SOC工作流

FreeBuf

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

![FreeBuf](https://mmbiz.qpic.cn/mmbiz_gif/icBE3OpK1IX1tefepWNegtic1THIRuo0zXWcDPh2UGibjkricko3DvuUEPvh0n645TqZO9fJD5uEzKmiaatp7XrmAJxtsbQfwIfDz3AJAKlqndIU/640?wx_fmt=gif)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/icBE3OpK1IX29CFBYhGGLxKT5FFdkN1aSzu2PVv2lxZ2zQe4WeoLiayOKtRrqfCgbXBGR2JZRZGaVzjnzuAvn9pl8Pa3UN7JsypfEVj8oFiaE8/640?wx_fmt=png&from=appmsg)

我们熟知的SOC，自始至终都建立在一个注定会让大部分告警队列永远等不到分析师审核的模式之上。时间从来都不够用。在传统SOC中，典型的处理流程遵循一个众所周知的模式：告警到达，检测引擎为其赋予严重性评分；然后，该事件只能等待人工来判断是否需要升级为正式调查。

考虑到安全技术栈中网络遥测数据的庞大数量，将人作为调查层必然导致队列的出现。漫长的告警队列还迫使安全团队在尚未弄清信号含义之前，就必须决定优先分析哪些信号。

威胁狩猎一直通过另一种思路来回答安全问题：先提出关于攻击者行为的假设，再检索可用证据，最后证实或推翻该假设。这种方式虽然行之有效，但终究会撞上同一堵墙——人的能力上限。

Agentic安全运营改变了这一范式。

如今正在建设中的SOC以Agentic AI为基础，能够更快地完成调查——只需几秒或几分钟，而非数小时。但速度的提升并非唯一的变化。调查的执行顺序同样得到了升级。由于Agent能够快速分析海量遥测数据，它们可以彻底倒转告警队列模型：先调查，再依据证据决定是否升级。

Part01

倒转如何实现

由AI Agent推动的假设驱动调查，是一种正在兴起的改进检测效果并缩小攻击面的方法。当运行成本足够低廉、可以持续不断执行时，以假设（而非队列）为驱动力的SOC便具备了可扩展性，人的角色也会从执行调查转变为评判调查结果。

告警一旦出现，Agent就可以立即展开调查：验证检测结果、检查底层网络活动、对被影响的实体进行画像、考察历史行为、关联相关活动，并从数据中收集补充证据。

调查不再需要争夺分析师的注意力。Agent可以异步工作，并行推进多项调查，并返回有证据支撑的结论。

Agentic分流工作流利用结构化的调查手册（playbook）深入检查网络遥测数据，并给出有数据支持的判定。这种工作流不仅加快了分流速度，还意味着更多信号可以在不消耗人力资源的情况下得到调查。在案件到达分析师手中之前，Agent就利用更广泛的网络数据消除了人工调查这一步骤。

Part02

机器规模的威胁狩猎

更有意思的，是告警出现“之前”以及“之外”所发生的事情。

威胁狩猎不必从“检测到了什么”开始，而可以从“攻击者在做什么”开始。

设想以下这些假设。攻击者可能正在：

* 使用非常规协议进行命令与控制（C2）
* 通过远程管理服务进行横向移动
* 暂存数据准备外泄
* 与没有合法通信理由的系统进行通信
* 使用专门设计用于规避现有检测阈值的攻击技术

每一条假设都对应着可观察的行为。网络流量提供的证据既可以支持假设，也可以推翻假设，并确定某个已检测到的信号是否具有真实意义。

AI驱动的假设狩猎并不会取代检测，而是利用网络证据来验证和扩展可验证的检测结果。网络遥测数据成为调查的基础。

这就是当Agent能够并行运行大量调查时，威胁狩猎所呈现的形态。

Part03

Agent可以在确定性产生之前展开调查

Agentic调查的真正优势在于，Agent在开始行动之前并不需要确定性。

它可以追踪一个微弱的信号，检验一个假设，并在证据不再支持该假设时果断停止。其业务优势在于：它能够调整假设并循环往复，速度远超任何人类分析师。

Agent可以自主地追问：

* 什么东西看起来不寻常？
* 哪些关联关系值得进一步检查？
* 哪些证据支持该假设？
* 哪些证据与之相矛盾？
* 还需要哪些额外证据来降低不确定性？
* 证据何时才足以引起人工关注？

由此产生的结果，是在网络活动、检测与已确认威胁之间增加了一个调查层。大多数调查无需人工介入即可结束；真正需要升级的案件在到达人类手中时，已经附带了完整的证据和上下文。

Part04

为人类的时间设定更高门槛

AI SOC的模型与以人为主的SOC有着显著区别。不再是：告警 → 队列 → 分析师 → 调查 → 处置

Agentic告警验证模型变成了：告警 → 队列 → 机器调查 → 证据 → 人工判断

传统的威胁狩猎模型则是：遥测 → 信号 → 分析师 → 假设 → 调查 → 处置

现在，基于假设的Agentic模型变成了：遥测 → 信号 → 假设 → 机器调查 → 证据 → 人工判断

在这些新模型中，最终结果是调查覆盖面的扩大，而分析师人力无需成比例增加：

* 单次调查成本更低：Agent负责证据收集与分析
* 威胁覆盖更广：SOC可以调查更多潜在攻击路径
* 风险降低更快：真正有意义的威胁能够更早浮出水面
* 分析师时间价值更高：人类专注于决策、响应和复杂案件
* 遥测数据价值更大：安全数据真正转化为可操作的证据

Part05

用持续调查取代队列

在AI SOC中，调查不再必须从队列开始，而可以从信号开始。Agent将利用遥测数据来验证告警、检验假设，并随着可疑活动的展开持续追踪。

只有当Agent带着有网络证据支撑的案件返回时，才需要人类介入。在这样的未来中，SOC将持续运行异步调查，这些调查以证据为驱动，不再受限于告警队列的瓶颈或人类分析师有限的时间视角。

参考来源：

Imagine the SOC Without a Queue: From Alert Backlog to AI Hypothesis Engine

https://thehackernews.com/2026/08/imagine-soc-without-queue-from-alert.html

###

### **推荐阅读**

[![](https://mmbiz.qpic.cn/sz_mmbiz_png/icBE3OpK1IX0grlwwcpsEQ5CIH725a7xAnwDLGFctXFohPibiaOVyzdqwaibKgD4x4enG6jhdgJQHziaqTMy1WR0Hibx4MceSVKd6C7HGGlA9zLibg/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MjM5NjA0NjgyMA==&mid=2651344398&idx=1&sn=56c4e0d580e04a250d0e8c6cffd592b8&scene=21#wechat_redirect)

###

### **电报讨论**

![](https://mmbiz.qpic.cn/mmbiz_png/icBE3OpK1IX3eRDUpH3UJicSe4tdw7nZYu9aa5PQ9KgkaP84oZz0bVYdBiaDt97VfDBLulDp3sWLgvzI4m0mc89MZ7feP2yfFAmcRWOlicWubZ4/640?wx_fmt=png&from=appmsg)

![扫码加入AI安全交流群](https://mmbiz.qpic.cn/mmbiz_png/icBE3OpK1IX0Py7ibxdLKXia1pMziaic5vIE9XPXG9OGaeJDa07iaG10eicuzhW59nwpF5msHiaYZvfMqCNkx2aFDiaMzm3oAf4rTaHXU5UAI1mUYgts/640?wx_fmt=png)

![下载FreeBuf知识大陆APP](https://mmbiz.qpic.cn/mmbiz_png/icBE3OpK1IX0TIGzII2Hcmtzu7AJeZFicnqd1mXojVoawje2uLxYqwJbVgzJpmSXzVhrpOsLurRZ2lVa4vfgLBqg7uJKbrKg5F18VzZxVPicZU/640?wx_fmt=png)

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/qq5rfBadR3ibLOEAnkkKa2dHtqcjZ55KLsqibib6n4UDNUhLIuMRdAJ9ibfZkSK5LViaGJLEQN7p9OGo7mNnVv3EmkQ/0?wx_fmt=png)

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