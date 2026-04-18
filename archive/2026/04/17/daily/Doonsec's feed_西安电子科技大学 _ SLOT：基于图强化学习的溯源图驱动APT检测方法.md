---
title: 西安电子科技大学 | SLOT：基于图强化学习的溯源图驱动APT检测方法
url: https://mp.weixin.qq.com/s/SmxPnJjdubjx1oFnxZy2gw
source: Doonsec's feed
date: 2026-04-17
fetch_date: 2026-04-18T04:26:56.460561
---

# 西安电子科技大学 | SLOT：基于图强化学习的溯源图驱动APT检测方法

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/8dQ2T4EPrnzjcX4EbjQmVlaOic0LxfPvzsQ6jlBRhjg9JFwpULicDNvav8CUl6Z7KYZ2fyujo93dwcblOXgvs84EPZOic6gj2ECmnAdPwxJaho/0?wx_fmt=jpeg)

# 西安电子科技大学 | SLOT：基于图强化学习的溯源图驱动APT检测方法

原创

龙函城
龙函城

安全学术圈

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz_png/8dQ2T4EPrnyxA8GLO3wgUKJyRnLvG1pzlUhe7rofxqYqB7rTWOtoOlxGjRs9WOPzXadVDYT5g9FHbogq68Kb6DJ6Enj6prhTF8no8g0SBW4/640?wx_fmt=png&from=appmsg)

> *原文标题：SLOT: Provenance-Driven APT Detection through Graph Reinforcement Learning*
> *原文作者：Wei Qiao, Yebo Feng, Teng Li, Zhuo Ma, Yulong Shen, Jianfeng Ma, Yang Liu*
> *发表会议：CCS'25*
> *笔记作者：龙函城*
> *主编：黄诚@安全学术圈*

## 研究概述

高级持续性威胁（APT）通常具有潜伏周期长、攻击阶段多、行为隐蔽且伴随伪装等特点，因此传统检测方法很难同时兼顾检测精度、误报控制与分析可解释性。论文指出，现有基于溯源图的APT检测方法主要包括统计型、规范型和学习型三类：统计型方法容易将低频但正常的行为误判为攻击；规范型方法依赖专家知识和规则维护，其适应性不足；而学习型方法虽然能够借助图神经网络建模系统行为，但在攻击者将正常行为嵌入攻击链进行伪装时，仍容易受到邻接节点干扰，导致恶意节点表示失真。

针对上述问题，本文提出Slot，一种基于图强化学习的溯源图驱动APT检测方法。其核心思路是：首先从系统审计日志中构建溯源图，将进程、文件、网络流等实体及其交互关系表示为图结构，并提取进程名、命令行参数、文件路径、IP 地址、端口等语义信息作为节点初始特征；随后通过潜在行为挖掘机制，在原始系统调用关系之外进一步发现多跳路径中的隐藏关系，以增强对行为因果链、上下文依赖和间接攻击痕迹的刻画能力；在此基础上，引入图强化学习，根据节点的语义与拓扑相似性自适应筛选邻接节点，尽可能过滤伪装性较强的干扰节点，从而提升图表示学习的准确性与鲁棒性。

![](https://mmbiz.qpic.cn/mmbiz_png/8dQ2T4EPrnzN3Q3HvN1f6icLB711kia5DBSd1mHc2f4qn9PPKNEdibueGcO4P5icxZ9QWTX5ickXLV6pwtnk2IygsZaC4GcyVb6wSv2VexQAtIjg/640?wx_fmt=png&from=appmsg)

图1 Slot方法整体架构

如图1所示，Slot的整体流程主要包括五个阶段：图构建、潜在行为挖掘、基于图强化学习的嵌入表示、威胁检测以及攻击链重构。其中，在表示学习阶段，Slot先融合节点属性特征与拓扑特征计算相似性，再通过Bernoulli multi-armed bandit形式的强化学习机制动态调整不同关系下的邻域筛选阈值，引导GNN在多关系图上完成更稳健的聚合。检测阶段则结合MLP与Isolation Forest，一方面识别已学习到的良性与恶意模式，另一方面补充发现未知异常行为；最后，系统进一步结合ATT&CK中的TTP编码与标签传播方法，对离散异常节点进行聚合和重构，生成更紧凑、更易于人工分析的攻击链结果。

与一般基于溯源图的检测方法相比，Slot的特点在于它并未将图神经网络直接用于异常分类，而是进一步把邻接节点是否可信作为表示学习中的关键问题来处理。为此，论文设计了相似性感知机制，并利用强化学习动态优化不同关系下的邻居保留比例，使模型在聚合上下文信息时尽量保留真正相关的邻接节点及其关系信息，削弱伪装正常行为对恶意节点表征的干扰。同时，Slot只使用少量恶意样本作为监督信号，结合半监督学习完成训练，并在输出层进一步重构攻击链，使系统结果不再停留于单个异常节点，而能够形成更具阶段性和可解释性的攻击路径。

实验结果表明，Slot在StreamSpot、Unicorn Wget和DARPA E3等多个公开数据集上都取得了较好的检测效果，整体检测准确率约为99%，并在对抗伪装场景下表现出优于现有方法的鲁棒性。论文还指出，借助图强化学习机制，Slot能够更有效地抵御攻击者通过修改图邻域结构来模仿良性行为的对抗策略，同时在案例分析中展示出较好的攻击路径重构能力。Slot不仅提升了APT检测精度，也增强了结果的可解释性。

## 贡献分析

* **贡献点1** ：提出APT检测方法Slot

  论文提出了Slot，一种基于图强化学习的溯源图驱动APT检测方法。该方法能够在大规模审计日志中有效识别恶意活动，并在检测过程中进一步完成攻击链重构，从而为后续有针对性的防御策略制定提供支持。
* **贡献点2** ：提出高级图挖掘技术，用于发现图中的多层隐藏关系

  论文提出了一种高级图挖掘机制，能够有效挖掘图中的多层隐藏关系，包括因果关系、上下文关系以及间接关联关系等。这使得模型不仅能够关注局部直接连接，还能够从更深层次上理解APT攻击过程中跨节点和跨路径的行为依赖。
* **贡献点3** ：设计有限标签条件下的半监督学习机制

  Slot通过高效的标签相似性计算，在仅有少量标签的条件下实现半监督学习。这种设计能够在标签受限的情况下显著提升检测性能与模型鲁棒性。对于真实APT检测场景而言，该机制具有较强现实意义，因为高质量恶意标签通常难以大规模获取。
* **贡献点4** ：将强化学习引入溯源图分析，提升系统对抗鲁棒性

  论文将强化学习引入溯源图表示学习过程，在融合节点语义特征与拓扑特征的基础上，通过强化学习自适应调整邻接节点选择与关系聚合策略，从而减轻伪装正常行为对恶意节点表示的干扰。
* **贡献点5** ：通过真实数据集实验验证了方法的有效性与实用价值

  论文在多个真实APT数据集上对Slot进行了全面评估。实验结果表明，Slot在APT检测准确性、对抗攻击鲁棒性以及攻击链分析支持能力方面均表现突出，验证了其在APT检测与防御支撑中的实际应用潜力。

## 实验结果分析

论文围绕半监督检测能力、与现有方法的整体比较、系统开销、模块有效性、对抗鲁棒性以及告警验证效果等方面进行了系统实验。实验数据包括批日志层面的 StreamSpot、Unicorn Wget，以及实体级的 DARPA E3（TRACE、CADETS、THEIA）数据集，既覆盖了相对简单的场景，也包含了具有较强伪装性和更复杂攻击链结构的APT场景。

表1 Slot方法与当前主流先进方法的对比结果

![](https://mmbiz.qpic.cn/sz_mmbiz_png/8dQ2T4EPrnx4RgxpmUwJFibmRTQSSAhbn18XuEJ7FWaxeuzjNT4ICsLAY9AUA9Viaqq7ibicSYd9CsruGC20GfHqic7MMz7OyiavOTrOvnPjszOfo/640?wx_fmt=png&from=appmsg)

从整体检测效果来看，Slot 在多个数据集上都取得了较优结果。表1显示，在StreamSpot、Unicorn Wget和DARPA E3三组数据上，Slot的Accuracy、Recall和F1-Score整体优于Log2vec、Threatrace、FLASH、MAGIC等方法，同时保持较低的误报率。在较简单的StreamSpot数据集上，多种方法都能取得较好效果，但Slot依然接近最优；而在伪装性更强的Unicorn Wget和DARPA E3数据集上，Slot的优势更加明显，这说明其对复杂APT行为和伪装上下文具有更强的区分能力。

表 2 批日志级与事件级训练数据集中恶意结构占比对检测性能的影响

![](https://mmbiz.qpic.cn/sz_mmbiz_png/8dQ2T4EPrnwqyebibeA3eH0UliaaQcibeAxCicdtelppbJBFQT0g8C2xt4ibp3DiakgrXk7EZ5D1XGZDoEPAdRFnJ2rzC2M5OhuNYrXjJibNib4QQnE/640?wx_fmt=png&from=appmsg)

在半监督场景下，Slot 同样表现出较好的有效性。论文仅使用少量恶意结构作为监督信号，通过标签相似性计算和过采样完成训练。表2所示，当训练集中的恶意结构比例从5%提升到10%时，模型性能显著提升，但即使监督信号较少，Slot依然能够获得较高的检测准确率。这说明该方法在标签有限的真实安全场景中具有较好的实用性。

表 3 在 300K 节点训练图上 Slot 各阶段的时间开销及占比

![](https://mmbiz.qpic.cn/mmbiz_png/8dQ2T4EPrnxdOicYhJdpsReSPfh08N2PVyUMic5ribkDq4SX3WPicgSarlP2yEicQudbuVDd3c3S9x1I2VtIHuJQiaSxLnBD6p3iciaFf75k1gPP7x4/640?wx_fmt=png&from=appmsg)

从运行代价来看，Slot 的主要额外开销来自强化学习过程。表3所示，在300K节点训练图上，图构建耗时46.12秒，强化学习耗时331.94秒，GNN部分耗时64.69秒，其中强化学习占总开销的74.97%。这说明Slot的性能提升并非无代价获得，而是主要通过邻域筛选与鲁棒表示学习换来的。不过，这种开销是可以接受的，因为它带来了更强的对抗鲁棒性和更高的检测质量。

![](https://mmbiz.qpic.cn/mmbiz_png/8dQ2T4EPrnwto9LXYgBvsC1iaziaHeOBu8GGow1l4nh4F8ickrFHw2aFfcj6eIachd6Hy4qcEglUc2nyicJzQ8lr0IOFcZFG3ibzYyrdOd2ZnwwM/640?wx_fmt=png&from=appmsg)

图 2 对抗攻击鲁棒性结果

论文构造了mimicry attack，通过在攻击图中不断插入良性结构来干扰检测模型。从图2可以看出，随着插入的良性事件数量增加，FLASH的检测得分明显下降，并逐渐接近异常判定阈值；相比之下，Slot的得分始终保持在较高水平，波动也相对更小。该结果表明，Slot通过相似性感知和强化学习筛选邻接节点，能够更有效地削弱伪装良性行为对恶意节点表示的干扰，因此在对抗场景下具有更强鲁棒性。

![](https://mmbiz.qpic.cn/mmbiz_png/8dQ2T4EPrnxc4y9OsBo6nqC3z8yYkMMIpTiboup9jRTQ5USHjcoU9MX2hxyElp1UMZIxArqMgJ7zTwZEjFRkCc0H2ib5R8YQca6YzHWzsDeaM/640?wx_fmt=png&from=appmsg)

图 3 告警数量与攻击链误报控制效果

图3所示，论文还评估了Slot在人工分析支持上的价值。在DARPA E3的TRACE、CADETS和THEIA数据集上，原始alert-node数量显著高于最终生成的attack-chain数量，而攻击链内部的precision仍保持在较高水平。这说明Slot在攻击链重构后，能够有效压缩分析人员需要人工检查的对象规模，同时较好地控制误报。其不仅能够检测异常，还能够把离散告警组织成更紧凑、更可解释的攻击路径，从而提升告警验证效率。

## 论文点评

总体来看，这篇论文的价值在于，它抓住了APT检测中的一个关键现实问题：在基于溯源图的分析中，攻击者往往会通过嵌入正常行为来伪装攻击路径，从而干扰模型判断。相比传统方法容易受到上下文噪声影响、在复杂场景下鲁棒性不足的问题，Slot进一步将图强化学习引入溯源图分析，使检测过程不仅关注异常识别，也关注邻接关系是否可信，因此整体思路较为清晰，也更贴近真实APT分析场景。

从方法设计上看，论文最突出的亮点有两个。第一是提出了潜在行为挖掘与相似性感知相结合的思路，用于发现图中的深层关系并削弱伪装邻接节点带来的干扰；第二是将攻击链重构纳入整体框架，不仅判断节点是否异常，还进一步组织出更具阶段性和上下文关联的攻击路径。这样一来，系统输出的不再只是零散异常节点，而是更具解释性和分析价值的攻击结果，这一点比单纯的图异常检测更有实际意义。

不过，这篇论文也存在一定局限。其方法整体链路较长，涉及图构建、隐藏关系挖掘、强化学习筛选、分类检测和攻击链重构等多个环节，因此实现与部署成本相对较高；同时，虽然论文在对抗伪装场景下表现出较好鲁棒性，但对于更强的开放环境攻击和未知行为，仍可能面临误报问题。

## 论文文献

Qiao, Wei, et al. "Slot: Provenance-Driven APT detection through graph reinforcement learning." Proceedings of the 2025 ACM SIGSAC Conference on Computer and Communications Security. 2025.

> [安全学术圈招募队友-ing](http://mp.weixin.qq.com/s?__biz=MzU5MTM5MTQ2MA==&mid=2247484475&idx=1&sn=2c91c6a161d1c5bc3b424de3bccaaee0&chksm=fe2efbb0c95972a67513c3340c98e20c752ca06d8575838c1af65fc2d6ddebd7f486aa75f6c3&scene=21#wechat_redirect)
> 有兴趣加入学术圈的请联系 **secdr#qq.com**

---

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/6Dibw6L070WFvZRQiafv3iccicic1dIYUEQ1ZzLh1a10l7tfw7zkWkRbY9kEPBwX2NiadOrwFl9a48as9qiayp3eOgDUQ/0?wx_fmt=png)

安全学术圈

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/6Dibw6L070WFvZRQiafv3iccicic1dIYUEQ1ZzLh1a10l7tfw7zkWkRbY9kEPBwX2NiadOrwFl9a48as9qiayp3eOgDUQ/0?wx_fmt=png)

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