---
title: AI SOC产品思考：如何用有限算力撬动最大效率
url: https://mp.weixin.qq.com/s/wCa_Xf0bd-U3iZXxcaypOg
source: Doonsec's feed
date: 2026-01-24
fetch_date: 2026-01-25T03:54:54.634269
---

# AI SOC产品思考：如何用有限算力撬动最大效率

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/rAhhJ9X0j5Te3HWQWNZZmSANaKfeWvbQ1FBl80NOz2tnIjm9yD2ChVV95l2YYzSqTSNibyxjhe0gp2r7ODBDnqw/0?wx_fmt=jpeg)

# AI SOC产品思考：如何用有限算力撬动最大效率

原创

LSJ
LSJ

安全开发

![]()

在小说阅读器中沉浸阅读

# **引言：当"AI理想"撞上"算力现实"**

最近在AI SOC安全运营分析类产品设计中遇到两个看似矛盾的问题：

![](https://mmbiz.qpic.cn/mmbiz_png/rAhhJ9X0j5Te3HWQWNZZmSANaKfeWvbQqt5vw39GATNOadZmhnJrfGGL7I2mDjaC0vbEjAs8z5iceWCMiaqonruw/640?wx_fmt=png&from=appmsg)

然而现实情况是，多数客户没有"足够多"的算力，只有"够用"的有限算力。因此，将AI视为"万能工具"，把一切安全分析任务通通丢给AI处理似乎是一种理想化。

于是不得不思考，如何用有限算力撬动人效，实现安全运营效率的最大化提升？

AI SOC的真正价值："让1份GPU算力，产生10份分析师人效的价值！"

![](https://mmbiz.qpic.cn/mmbiz_png/rAhhJ9X0j5Te3HWQWNZZmSANaKfeWvbQKCjz8j5uIUcdUfq1avTM9jkrcE6Ldoj7rwNnWaFA7lGrdmeY7C8jVQ/640?wx_fmt=png&from=appmsg)

# **一、设计理念：从"堆AI"到"用对AI"转变**

面对算力资源有限的现实挑战，AI SOC设计必须建立严格的算力分配漏斗，明确能力优先级：

* 第一优先级：保证"精准分析"
* 第二优先级：实现"智能调度"

## **1. 从"全量分析"到"精准投入"**

1）是否应该对全量安全告警进行AI分析？

在算力有限的情况下，AI不应盲目追求全量日志分析，而应优先分析高价值告警。例如，优先分析HTTP告警，确认是真实攻击后再考虑进行攻击链路还原和攻击事件还原。

![](https://mmbiz.qpic.cn/mmbiz_png/rAhhJ9X0j5Te3HWQWNZZmSANaKfeWvbQejLicP8I6SykWnfZKAL24cC51XJGgMX0BSSzn4dN8DiaXQYCECLouydw/640?wx_fmt=png&from=appmsg)

2）使用AI降噪还是规则降噪？

在实时流中，用复杂AI模型对每一条日志进行"是否噪音"的判断是算力的巨大浪费。应采用高效规则和阈值进行第一层降噪，这能在CPU上以极低成本滤除大量粗颗粒噪音。

![](https://mmbiz.qpic.cn/mmbiz_png/rAhhJ9X0j5Te3HWQWNZZmSANaKfeWvbQR9ib8Rvt433zBnpny1UhZYlmZY2rMXcZNp0g4MRLIoVYic4JEywJPHzg/640?wx_fmt=png&from=appmsg)

## **2. 攻击链路还原：从"完美还原"到"最大概率重建"**

      攻击链路还原的目标并非追求毫无遗漏的“完美考古”！而是定位为**“在有限证据约束下，还原出置信度最高的攻击叙事链”**。

![](https://mmbiz.qpic.cn/mmbiz_png/rAhhJ9X0j5Te3HWQWNZZmSANaKfeWvbQZK9G7xPbVfjLKDgEbSdTExpcysNKeBdkKUl03ROEJ2vtZeQKJGaeVA/640?wx_fmt=png&from=appmsg)

        系统通过逻辑推理构建最可能的攻击故事线，直接指导下一步的排查方向，实现“有限算力”中的“高效决策”。

![](https://mmbiz.qpic.cn/mmbiz_png/rAhhJ9X0j5Te3HWQWNZZmSANaKfeWvbQQC6qdJCKMtRWIMBibiahFJibiaBibyrX48Yj1OkdVf7w4k47gicTdDyFWPxg/640?wx_fmt=png&from=appmsg)

#### 1）触发机制：交互式主动触发

采用**按需分析**模式，由安全分析师在控制台主动点击已聚合的安全事件，发起“攻击链路还原”请求。系统仅在收到明确指令后执行还原动作，确保计算资源的精准投入。

#### 2）数据检索：基于多维信息的精准上下文构建

摒弃资源消耗巨大的“全量日志关联”，转向高效的“关键实体关联”策略，通过以下步骤构建最小化证据集：

* **多源数据聚合：从聚合事件中自动关联云、网、端等不同维度的安全设备日志。**
* **拓扑标签分层：设备配置时预置网络区域标签（如边界、内网），便于大模型依据网络拓扑进行分阶段、动态调查。**
* **智能采样限流：针对不同类安全设备设置不同的日志检索阈值，基于源目的IP、告警类型等关键因子设定选取规则，严格控制输入大模型的上下文窗口大小。**

#### 3）异步分析：Agent驱动的非阻塞推理

采用**异步任务架构**，将构建好的证据包提交至任务队列。由智能体自主领取任务，并调用大模型进行深度推理分析。该机制彻底隔离了计算密集型任务与实时交互流程，保障前台业务的响应速度与系统稳定性。

#### 4）结果交付：可视化呈现与知识持久化

* **即时反馈：在秒级到分钟级的延迟内，向分析师输出可视化的攻击图谱及详细的**

**推理过程**。

* **结论复用：自动将分析结论结构化存储为该事件的“攻击链分析”字段。在后续查询中，若无新增日志，系统将直接命中缓存结果，避免重复计算与资源浪费。**

## **3. 实时分析的智能调度**

      安全告警日志的实时分析应摒弃机械的“先进先出”（FIFO）静态队列模式，转而采用**基于风险态势的动态优先级调度机制**。系统通过规则引擎实时评估每条日志的紧迫性与威胁等级，确保高危攻击优先获取算力资源。

![](https://mmbiz.qpic.cn/mmbiz_png/rAhhJ9X0j5Te3HWQWNZZmSANaKfeWvbQnuPibkCfzYA5aiaSibHS56ZMMDCNEcIFQtcAuQvjzpFjGYJPFt6g3fqow/640?wx_fmt=png&from=appmsg)

#### 1）多维优先级规则集设计：（示例）

* 规则一（**陌生高危**）：IF 源IP为首次出现（24h内无历史记录） **AND** 告警等级 ≥ High THEN 优先级 = 高
* 规则二（**高频持续**）：IF 源IP在过去1小时内的告警触发频率 > 设定阈值 THEN 优先级 = 极高
* 规则三（情报命中）：IF 源IP/目标哈希命中本地威胁情报库或外部信誉黑名单THEN 优先级 = 极高
* 规则四（核心资产）：IF 目标资产标签 ∈ [核心数据库, 域控服务器, 重要的管理系统] THEN 优先级 = 高

#### 2）资源感知调度执行

* **动态评分：规则引擎融合上述特征，为每一条入站日志输出一个实时的**

**动态优先级分数**。

* **智能体决策：调度智能体作为资源分配器，综合权衡日志的优先级分数**

与当前**GPU资源池的实时负载状态**。

+ **高优先级 + 资源空闲：立即抢占算力，直达推理队列。**
+ **高优先级 + 资源繁忙：进入快速通道，等待现有任务完成后立即处理。**
+ **低优先级 + 资源繁忙：进入缓冲队列，进行错峰分析或降级处理。**

二、双线并行：构建高效安全运营体系

主线一：聚焦有效攻击源，实现“快准”自动化

## **AI模型专注于处理能够明确识别攻击内容的日志来源和高置信度的攻击行为，核心目标是“快”和“准”。这正是“用对AI”理念中“精准投入”的体现，即并非所有攻击源都需要消耗宝贵的AI算力。**

![](https://mmbiz.qpic.cn/mmbiz_png/rAhhJ9X0j5Te3HWQWNZZmSANaKfeWvbQA1icoFDlIAzKibXibRZfgfq1s5wHTOEdCsCVDJr5cdj2FCkbxTGPicD19Q/640?wx_fmt=png&from=appmsg)

##

## **主线二：聚焦规则降噪，关注重点事件**

## **经过**人工设定规则降噪后聚合成一条条新的安全事件。AI模型**对聚合后的安全事件进行深度语义分析与上下文关联，**通过多维度特征提取与异常检测算法，挖掘出隐藏在常规流量中的高级持续性威胁，****对高危事件进行智能优先级排序，实现从“海量告警”到“精准情报”的升华。****

![](https://mmbiz.qpic.cn/mmbiz_png/rAhhJ9X0j5Te3HWQWNZZmSANaKfeWvbQcpwTKTI5TlNZmyxvPyRJbebWlrtmx2e65RIHAzdRH2icYwWGBBLrt5g/640?wx_fmt=png&from=appmsg)

|  |  |  |
| --- | --- | --- |
| **维度** | **主线一：聚焦攻击源（自动化阻断）** | **主线二：聚焦降噪事件（风险发现）** |
| **处理对象** | 高置信度，可明确识别攻击内容的告警日志 | 规则降噪过滤重新聚合的重点事件 |
| **分析核心** | **关联分析** | **深度挖掘** |
| **运营目标** | **自动化处置** | **潜在风险挖掘、重点事件关注** |

# **三、安全分析流程**

**1）整体流程设计**

* ### **顶层预处理：日志清洗与标准化**

* ### **双路径并行处理：攻击溯源与事件聚合**

#### **左侧路径：攻击源IP聚合与真实攻击判定**

#### **右侧路径：安全事件聚合与智能调查**

![](https://mmbiz.qpic.cn/mmbiz_png/rAhhJ9X0j5Te3HWQWNZZmSANaKfeWvbQ8A7kQ6W4AmNEcOc80zKRrlEGoiaTtc9O5uQR7ib4eBQqrGRT3fbvQCOA/640?wx_fmt=png&from=appmsg)

### **2）核心逻辑与价值**

* **动态优先级调度：通过“危险系数”“阈值判断”实现攻击源的优先级标记，确保高威胁事件优先分析。**
* **AI+规则融合：结合预定义规则（如威胁情报匹配）和AI模型（如异常检测），提升攻击判定的准确性。**
* **模块化智能体：通过“云/流量/主机”等专用智能体，实现多源日志的协同分析，避免单点分析局限。**
* **闭环溯源：从日志清洗到攻击链路还原，形成“检测-分析-溯源”的完整闭环，辅助安全人员快速响应。**

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/rAhhJ9X0j5QBwtZk247jjQ5uLzPlpWAVYr8DOakrNfVruso9ldngicm5wH0iahzmlOIcibgyqzfgpWtYcs5jDjRCQ/0?wx_fmt=png)

安全开发

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/rAhhJ9X0j5QBwtZk247jjQ5uLzPlpWAVYr8DOakrNfVruso9ldngicm5wH0iahzmlOIcibgyqzfgpWtYcs5jDjRCQ/0?wx_fmt=png)

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