---
title: 论文录用 | NASP实验室2篇论文被SIGCOMM 2026录用
url: https://mp.weixin.qq.com/s/_2pTCuCuk0R4q5kjDStDJg
source: Doonsec's feed
date: 2026-05-12
fetch_date: 2026-05-13T05:43:54.586272
---

# 论文录用 | NASP实验室2篇论文被SIGCOMM 2026录用

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/5mMLC1RrpviaGc8TdwFW7HWMMfBiczPDpKjTxN6icpPQjS8bY98weDb8qG7Z4Yw1KyqIHfKpjXfxndFuSnHCDwTCQ14HjPq8xICww7qia0s6BMs/0?wx_fmt=jpeg)

# 论文录用 | NASP实验室2篇论文被SIGCOMM 2026录用

NASPLab
NASPLab

NASP网络实验室

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

**NASP实验室2篇论文获得SIGCOMM 2026录用，另有1篇进入此会议one-shot revision环节。**

[1] Yanyu Ren, Xianshang Lin, Chenxu Wang, Li Chen, Shuai Wang, Kaihui Gao, Dan Li, Yunfeng Bai, Chen Tian, Xinlei Zhang, Yungang Li, Tao Lin, Ennan Zhai. "Networked Agent Memory and Causality Representation: Experiences towards Interpretable Cloud-Scale Root-Causing", ACM SIGCOMM 2026, Denver, Colorado, USA.

本论文针对大规模网络根因诊断中，大模型智能体上下文易饱和及缺乏可验证解释性等问题 ，创新提出了一种基于多智能体的根因分析框架XIHE 。XIHE首先设计了知识引导的多智能体推理框架，将复杂的诊断任务拆解给多个分布式智能体结合知识库并行执行 ，从而适应未知的多变故障模式 。为了在规避单点内存饱和的同时构建全局上下文，XIHE进一步设计了网络化智能体记忆（Networked Agent Memory）和网络化因果表示（Networked Causality Representation）机制 ，前者使得智能体能通过拓扑通信原语共享局部诊断洞察 ，后者则将分布式的推理结果合成为透明可验证的全局因果图 。实际部署与实验表明，XIHE在阿里云网络中协助处理了三千余起事件，不仅实现了94.6%的整体高准确率，还将运维人员的根因分析时间缩短了25.8% 。

论文第一作者为清华大学博士生任彦羽，完成单位包括清华大学、阿里云、中关村实验室和南京大学。

[2] Hongtao Xie, Jianmin Liu, Ce Yang, Yu He, Li Chen, Dan Li, Mineng Fu, Xi Chen, Siyu Chen, “Open the Floodgates in a Digital Twin: Experiences of Building Spillway for 100M+-User Signaling Storms in Cellular Core Network”, ACM SIGCOMM 2026, Denver, Colorado, USA.

中国移动运营着世界最大的5G独立组网蜂窝网络。论文针对4/5G蜂窝核心网中大规模终端同步重连引发的信令风暴问题，创新提出了一种基于数字孪生的信令风暴全局防御系统 Spillway，实现了过载缓解参数的自动化配置。现有的静态、局部过载控制机制难以应对异构网元间复杂的串行依赖，极易引发级联与亚稳态故障；为此，Spillway引入了一种分层防御架构，通过实施“利他式”限流策略，促使上游网元主动减载，从而保护下游瓶颈网元。为高效评估海量配置策略，本文进一步设计了领域特定的数字孪生系统CN-DES。该系统采用新颖的向量化内核，将具有相同协议状态的用户进行聚合建模，成功将仿真复杂度与用户规模解耦，在千万级用户场景下实现了 60 倍的仿真加速。同时，系统结合异方差进化贝叶斯优化算法，能够在复杂、非凸的高维参数空间中高效寻优。现网数据表明，Spillway已在中国移动（覆盖260万个基站，服务约 6.22 亿用户）的核心网中实现了长达五年的规模化部署。在应对各类真实网络突发故障时，经Spillway优化的配置有效保障了全网元始终运行于安全边界内，显著降低了用户的业务回退率。

论文第一作者为清华大学博士生谢洪涛，完成单位包括清华大学、中关村实验室、中国移动通信有限公司。

**ACM SIGCOMM是计算机网络领域入选计算机科学顶级学术会议列表CSRankings（https://csrankings.org）的两大国际学术会议之一（另一会议为USENIX NSDI）。**

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/5mMLC1RrpviaticKzRYbib4GNVqkV1Upmz1oA9xx37eFB165uoZe53PZe2vk4QhHibBNjqFRjPcaOwEcs2n0nQictxoicdAYhlic9l0zawicasyXgkc/640?wx_fmt=jpeg)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/wgW61zX4SsNgCqFgcZIW9RkKmCYkLttpkzdxEfDEFX0esiavjA7SCUwCLibRAnd5wYppIiaN0q7jGghmBqUFTL4Kw/0?wx_fmt=png)

NASP网络实验室

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/wgW61zX4SsNgCqFgcZIW9RkKmCYkLttpkzdxEfDEFX0esiavjA7SCUwCLibRAnd5wYppIiaN0q7jGghmBqUFTL4Kw/0?wx_fmt=png)

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