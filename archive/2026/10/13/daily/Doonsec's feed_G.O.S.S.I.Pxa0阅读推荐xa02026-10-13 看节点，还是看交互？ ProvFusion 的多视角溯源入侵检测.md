---
title: G.O.S.S.I.Pxa0阅读推荐xa02026-10-13 看节点，还是看交互？ ProvFusion 的多视角溯源入侵检测
url: https://mp.weixin.qq.com/s/Y6FZ9-bLeR2Wq7sdVpuLSg
source: Doonsec's feed
date: 2026-10-13
fetch_date: 2026-10-14T06:50:36.778419
---

# G.O.S.S.I.Pxa0阅读推荐xa02026-10-13 看节点，还是看交互？ ProvFusion 的多视角溯源入侵检测

# G.O.S.S.I.P 阅读推荐 2026-10-13 看节点，还是看交互？ ProvFusion 的多视角溯源入侵检测

Fan Yang
Fan Yang

安全研究GoSSIP

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

同一批攻击相关实体，在不同的入侵检测系统眼中，可能呈现出截然不同的异常程度。

今天要推荐的文章里，研究团队将节点检测器 MAGIC 与边检测器 Orthrus 的评分放到同一张图上，观察到一个值得关注的现象：一些恶意节点在节点视角中十分异常，在交互视角中却并不突出；另一些恶意节点恰好相反。两类检测器捕捉到了不同的攻击线索，也暴露出各自的盲区。

如何利用这种互补性，在发现更多攻击的同时控制误报？香港中文大学与中山大学的研究团队提出了 ProvFusion。相关论文 Beyond Nodes vs. Edges: A Multi-View Fusion Framework for Provenance-Based Intrusion Detection 已被 IEEE S&P 2026 接收。

![](https://mmbiz.qpic.cn/mmbiz_png/eQ0Wf6rqolXDE7EiacDIKbvXLic4krt2w7uUn6Rx24SUicRFAwtSO44LVqfn5XOj8QoicApaEykatfNbLibhibuWaPwcpva6KYIp6S7VqUjN9cqUk/640?wx_fmt=png&from=appmsg)

ProvFusion 从属性、结构和交互三个视角分别分析异常，再通过分数校准、融合与投票作出判断。在论文评测涉及的 17 次攻击活动中，系统成功发现了 16 次；在六组 DARPA TC 数据上，相比基线 Velox，平均检出的恶意节点数从 7.2 增至 24.8，平均误报节点数从 136.5 降至 6.2。

节点与边各自看到了什么

溯源图将审计日志中的进程、文件和网络连接表示为节点，将读取、写入、执行和通信等操作表示为有向边。它把零散的系统事件连接起来，为理解复杂攻击提供了上下文。

基于溯源图的细粒度检测，通常从节点或边展开。

节点检测关注实体的属性及其局部结构。异常的文件路径、命令行或连接模式，都可能成为攻击线索。但正常的软件更新、配置修改和新用户活动，也会带来此前少见的特征，进而触发误报。

边检测关注实体之间的交互是否符合正常模式。它能够发现可疑的信息流与操作关系，但攻击者同样可以通过常见的读取、执行和网络通信完成攻击，使部分恶意交互获得较低的异常分数。

![](https://mmbiz.qpic.cn/mmbiz_png/eQ0Wf6rqolVzl0T2uRrdcbSicFtkCs5UdTD1nDXj6nMHwnKTmFmiaKjcghGNONWOsqSStQcA1W8sfhOiap1g2vBQn1kHFQBlCpEvCG6WDsn93Q/640?wx_fmt=png&from=appmsg)

图 1：同一批恶意节点在 MAGIC 与 Orthrus 中的异常分数。图中的不同高分区域展示了两种检测视角的互补性。

这一观察说明，实体本身的异常与实体之间的交互异常，都能提供有价值的证据。综合这些证据，有望更完整地判断系统行为

互补的检测器，为什么还需要专门的融合设计

一个直接的思路是，将现有节点检测器和边检测器的分数组合起来。

研究团队为此加入了 MAGIC 与 Velox 的分数线性融合对照。实验发现，这种组合仍然存在较多误报，未能达到 ProvFusion 的检测效果。例如，在 THEIA-E3 上，组合方法检出了 16 个恶意节点、产生 44 个误报；ProvFusion 则检出了 91 个恶意节点、产生 2 个误报。

不同检测器提供的信息虽然互补，融合时仍需处理两个问题。

首先，不同信息可能在学习过程中相互干扰。一个正常文件出现了新的路径，其属性特征会发生变化；经过图神经网络的消息传递，这种变化还可能影响周围节点的表示，让正常的结构模式也显得异常。

其次，各个视角的分数具有不同的量纲和分布。属性距离与事件预测损失即使取值相同，代表的异常程度也可能相差很大。直接求和或平均，容易使某个视角占据过大的权重。

因此，ProvFusion 从异常信号的形成方式和异常证据的融合方式两个环节入手。

先分清异常来自哪里，再综合证据

ProvFusion 为每个实体生成三个具有明确含义的异常分数。

属性视角关注路径、命令行等语义特征。系统将这些属性编码为向量，使用 K 近邻方法衡量其与正常实体特征的距离，从而识别语义上的异常。

结构视角关注实体的连接模式与行为角色。系统保留节点类型、连接关系和事件类型，通过图掩码自编码器学习正常的结构表示，再衡量待检测节点与正常结构模式的距离。将这一过程与属性分析分开，有助于减少属性新奇性对结构判断的干扰。

因果交互视角关注溯源图中的实体交互。系统结合交互双方的语义及图上下文预测事件类型，并根据实际事件与预测结果的差异计算异常分数，进而定位参与可疑交互的实体。

三个视角分别学习和评分，使“属性少见”“结构异常”和“交互不合理”能够保留各自的含义。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/eQ0Wf6rqolW1f8lExRyTmDibicCM4xicLQPhZdicXicRhqTl8f4MYcLialHU82pv2JOfoOk5ChJViaS5RjBAoCC2ZRbnibTP3AI3LffbYcrKquVBDZw/640?wx_fmt=png&from=appmsg)

图 2：ProvFusion 的整体流程，包括溯源图构建、三个视角的异常分析，以及分数融合与投票。

随后，ProvFusion 使用良性验证数据进行百分位归一化，将原始分数转换为其在正常行为分布中的相对位置。这样，不同视角的分数便具有了可比较的含义：它们分别偏离正常行为到了什么程度。

在此基础上，系统通过七种规则检查不同的证据组合：三种分别检查单个视角，两种融合得分最高的两个视角，另外两种整合全部三个视角。多视角组合包含求和与加权融合两种形式。

每种规则依据良性验证数据设定阈值，并给出一票判断。默认情况下，至少四票认为异常时，系统触发告警。这一机制能够综合单个视角的突出信号，以及多个视角共同提供的异常证据。

每个告警还会附带三个视角的分数和七种规则的投票结果，便于分析人员追踪判断依据。

检测收益来自哪些方面

研究团队在 DARPA TC 的六组数据及 DARPA OpTC 的三个目标主机子集上进行了评测，覆盖 FreeBSD、Linux、Android 和 Windows 环境。实验比较了六种代表性检测系统，并加入简单分数融合等对照。

下面列出六组 TC 数据上的部分结果。表中数字为各组数据的节点数之和，采用论文统一的评测设置与修订后的攻击标注。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/eQ0Wf6rqolXf222kLCDZ78lEyol2K1Dp17Aomd64vr6NJsyXGbUiac8xBpmzjBna8agygyLicRvjI5Avkk3VUFOZFrj29KBzZzIpOTLo9rcwM/640?wx_fmt=png&from=appmsg)

这些结果表明，在这组评测中，ProvFusion 同时改善了恶意实体检出数量和误报控制。简单融合虽整合了两类检测器的输出，仍未充分发挥它们的互补优势。

在攻击活动层面，ProvFusion 发现了 TC 中的 13/14 次攻击，以及三个 OpTC 主机上的全部三次攻击，合计 16/17 次。这里的“发现”指至少检出一个直接参与该攻击的恶意节点。

消融实验进一步说明了分数校准的作用：在六组 TC 数据上，将百分位归一化替换为 Min-Max 归一化后，攻击覆盖从 13/14 降至 8/14，误报节点总数从 37 增至 2378。不同视角之间如何对齐，对最终结果具有显著影响。

多视角分析也保持了有竞争力的运行效率。例如，在论文的 CADETS-E5 实验中，ProvFusion 的整体训练耗时较 Velox 增加约 2.6%，推理耗时则更短。

从几个关键节点追踪攻击行为

检测结果还需要为后续调查提供线索。

在 CLEARSCOPE-E3 的一个案例中，ProvFusion 检出了六个攻击相关节点。围绕这些节点扩展一跳邻居后，可以得到一个紧凑的子图，呈现 Firefox 相关进程、文件访问以及与外部网络端点之间的通信关系。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/eQ0Wf6rqolWu1rOQk4MgMiareX766qVviaxbQXIuZhGmztpedUEYQgjExtjqc3INKK4IzR7ELszUqpZfRtibUrK4QPzOAdP2GTvlaaRoBdCohQ/640?wx_fmt=png&from=appmsg)

图 3：围绕检测出的攻击相关节点扩展得到的子图，红色节点为系统正确检出的恶意实体。

子图中重复出现了三次文件访问与网络传输模式，与攻击记录中因连接不稳定而进行的三次数据外传尝试相吻合。结合节点的异常分数和投票结果，分析人员能够从具体告警出发，检查相关进程与交互，逐步理解攻击过程。

ProvFusion 的研究展示了将实体属性、结构角色和交互模式共同用于入侵检测的价值。当前框架主要面向单主机静态溯源图，后续可以进一步引入事件时序、扩展跨主机分析，并增强对不完整日志的适应能力。

研究团队已公开代码、模型检查点及相关复现实验资源，欢迎开展复现、比较和进一步研究。

论文pdf：https://ieeexplore.ieee.org/abstract/document/11573614

代码与复现资源

代码与复现说明：https://github.com/Joney-Yf/ProvFusion

数据与模型资源：https://huggingface.co/datasets/Joney233/ProvFusion

预览时标签不可点

不喜欢

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/uicdfzKrO21EibxMcqx9KdafugxDicBiaW3cb1gyTuWooDCJjH1ibu8aibOiapYLq8BJMwNbIeUK1t0japdvmdqTfCxhg/0?wx_fmt=png)

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