---
title: CyberStrikeAI：批量任务不止排队——定时与一句话创建
url: https://mp.weixin.qq.com/s/dNytjXVmk9hjw9-5KDYtiA
source: Doonsec's feed
date: 2026-04-13
fetch_date: 2026-04-14T04:39:02.374593
---

# CyberStrikeAI：批量任务不止排队——定时与一句话创建

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/ufQ2xnAD33vTrHRAecLc7oqA4CjVRHgTicllZor26sT5Z8UjkAaFGeFsBmhDiaSt7sK2u1qlnHvUXKbTYKAUeMR7pcA13NPZhVa4zcicrx1icibw/0?wx_fmt=jpeg)

# CyberStrikeAI：批量任务不止排队——定时与一句话创建

原创

学安全也就图一乐
学安全也就图一乐

低调学安全

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

> 本文介绍 CyberStrikeAI 在原有**批量任务队列**之上的能力：**Cron 定时 / 循环调度**，以及通过**对话**用自然语言「创建并开启」任务的方式。文中示例仅供说明产品能力；**所有探测与测试须在合法授权范围内进行**。

---

## 摘要

此前 CyberStrikeAI 已支持**批量任务队列**：多条指令按顺序执行，适合渗透步骤脚本化、批量验证、固定剧本复跑。新版本在「队列」之上补齐 **Cron 定时与循环调度**，并进一步把能力接到 **对话里**——用自然语言描述「多久跑一次、跑什么」，即可走通创建与启动，降低 Cron 与队列配置的门槛。

**对话创建**示例（在聊天中直接发送）：

* 「给我创建并开启一个任务，每分钟 ping 一下 baidu.com」
* 「给我创建并开启一个任务，每天上午九点 ping 一下 baidu.com」

理想情况下，智能体会理解周期与动作，完成队列创建、必要时配置 Cron，并**启动执行**（具体依赖当前环境是否为对话智能体暴露 `batch_task_create`、`batch_task_start` 等 MCP/工具能力）。

![](https://mmbiz.qpic.cn/mmbiz_png/ufQ2xnAD33vick6ibTqWibKiaSKWYBezQ6KBeWT2nMw8uaWiaRy1WWvl82mibtgkLDUiacFLReBQhRaudbuZD1S3IWtCbcMEibBqGBsicf4qlUYoicEro/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/ufQ2xnAD33uXgOEKWjoXPLtic6eFRZqpuIWqaF9gBBJiarxFLvf7tm6AT53j7IQnEB8HQbGQ1ymz9yPf1iaiaVFqiceOcFRS962rnwQw5vZyLVfY/640?wx_fmt=png&from=appmsg)

当然也支持手工创建：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ufQ2xnAD33u8KAib4ClFsibmQt7aAib79gS7To939WoHz9YiaOC4H1kiaPCy5cxSUMlOwUkdVs87ZrySy7iby1CvmABibcCibychHBaODLatFibLbAuE/640?wx_fmt=png&from=appmsg)

---

## 一、为什么要在「队列」之外再做定时？

**批量任务队列**解决的是：**同一批事情，按顺序自动往下执行**，每条指令背后往往是一次独立对话、一次工具编排，状态可追溯。这在授权测试里很常见：先信息收集、再定点扫描、再汇总结论——不必每次手动复制粘贴。

但真实工作里还有一大类需求是 **「按时间重复」**：

* 每分钟 / 每小时做一次轻量存活探测；
* 每天固定时间跑一轮巡检；
* 阶段性项目里，希望在**不常驻人工**的情况下，仍保持可预期的执行节奏。

若只有「手工点一次跑一轮」，人要么守着控制台，要么反复登录触发，**成本在「时间维度」上放大了**。因此，在保留原有「队列顺序执行」的前提下，增加 **定时（Cron）与调度策略**，是工具从「能跑一批」到「能按日历跑」的自然一步。

---

## 二、定时任务在这里「是什么」？

可以把它理解成：**还是同一个批量任务队列，只是多了一块「时间表」**。

| 模式 | 说明 |
| --- | --- |
| **手工** | 与早期体验一致，适合一次性剧本；需要跑时在界面或通过 API/MCP **启动执行**。 |
| **Cron** | 为队列绑定标准 **Cron 表达式**（分、时、日、月、周），系统计算 **下次执行时间**；一轮子任务全部跑完后，进入「等待下一轮调度」的状态，而不是简单当成「彻底结束」——与「每天九点再来一遍」的心智一致。 |

同时，产品侧提供 **「是否允许 Cron 自动调度」** 一类开关：

* **关**：保留表达式，**不**自动按点触发，避免误跑；
* **开**：到点自动进入下一轮（以当前版本行为为准）。

这样，**定时**不是飘在系统外的另一个模块，而是 **队列生命周期里对「何时触发下一轮」的显式建模**，便于在任务管理里统一查看状态、下次执行时间、调度错误等。

---

## 三、「对话创建」：把配置成本交给自然语言

很多安全/运维同学对 Cron 不陌生，但在**高频、碎片化**的需求里，「打开表单、填表达式、填子任务、再去找启动按钮」仍然打断思路。CyberStrikeAI 作为 **AI 原生** 平台，更顺的一条路径是：**把意图说给对话里的智能体，由它完成结构化配置与调用**。

典型流程可归纳为：

1. **理解意图**：「每分钟」「每天上午九点」→ 生成或校对 **Cron 表达式**；「ping xxx」→ 落成队列中的 **子任务指令**（实际执行取决于环境与工具策略）。
2. **创建队列**：写入调度模式、表达式、子任务列表等。
3. **立即执行**：若用户明确「创建**并开启**」，智能体应在创建后 **再发起启动**，让**第一轮**跑起来；仅「创建」则可停在 `pending`，由人审阅后再开跑。
4. **定时延续**：Cron 开关打开时，第一轮结束后按表达式等待下一轮；若业务上只需跑一次，更适合手工队列或只启动一轮。

**稍深一层**：对话创建的本质是 **自然语言 → 结构化参数 → 与 UI/API/MCP 共用的同一套队列语义**。任务管理页负责「看见与纠偏」，对话负责「快速发起」，MCP 负责「被 Cursor 等客户端编排」——**入口变多，数据模型不变**，审计与复盘仍可在统一队列视图里完成。

---

## 四、适用场景与边界

**更适合：**

* **授权环境**内的周期性健康检查、资产探活、重复性低危巡检；
* 与 **角色 / Skills** 绑定的固定套路，希望按日历复用；
* 需要 **可追溯**：每条子任务对应会话与执行记录。

**需要克制或人工复核：**

* **高影响、高频率**的扫描或利用类动作：即使用自然语言创建，也应在角色工具集、网络边界、流程上收紧；
* **自然语言与 Cron 是否真等价**（时区、语义歧义）：重要任务务必在任务管理里核对 **「下次执行时间」**；
* **「创建」与「启动」分离**是常见安全设计；「一句话创建并开启」把两步合并，适合可信环境与已隔离靶场。

---

## 五、小结

1. **队列还在**：顺序执行、可审计。
2. **定时是队列的一种运行方式**，不是另一套孤岛功能。
3. **对话创建**省掉表单与文档摩擦；**授权、角色工具与界面核对**仍是底线。

---

*项目仓库链接:https://github.com/Ed1s0nZ/CyberStrikeAI*

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/KzNYA6icKe6ny3nDMkDelsYYnPJzRX2erWFEia2S7Bqqc7CjicEpJYQtId7a2jXKCial6Mw8ck8IFQEqmZnldrG2EQ/0?wx_fmt=png)

低调学安全

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/KzNYA6icKe6ny3nDMkDelsYYnPJzRX2erWFEia2S7Bqqc7CjicEpJYQtId7a2jXKCial6Mw8ck8IFQEqmZnldrG2EQ/0?wx_fmt=png)

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