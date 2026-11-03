---
title: 个性化视频技术：历时七年的算法演进
url: https://mp.weixin.qq.com/s/8lrMtjHs3U4ZJoulNObTvQ
source: Doonsec's feed
date: 2026-11-02
fetch_date: 2026-11-03T08:46:06.150194
---

# 个性化视频技术：历时七年的算法演进

# 个性化视频技术：历时七年的算法演进

原创

抖音用户体验算法
抖音用户体验算法

字节跳动技术团队

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

**01 |****前言**

个性化视频算法是抖音体验算法团队在行业内最早创设的方向，曾于 24 年发表详述，参考：

* 首度揭示！个性化视频技术——短视频体验的秘密！

  (https://juejin.cn/post/7439556806602752051)
* Personalized Playback Technology: How Short Video Services Create Excellent User Experience(https://arxiv.org/abs/2410.17073)

数年以来，团队笃行不怠，多路并进，与当时披露的内容相比又有更多进展，在此做一详细盘点，希望可以引导、促进业界水平的提升。

回顾历史，音视频技术自互联网开端时即已成为显学，在之前三十多年的发展历程中，行业的关注重点主要在编解码标准、流媒体协议和框架开发等方向，虽然一直有零散的算法工作，意图解决实际工作流程中某一环节的问题，但抖音这条路径是通过 VLP、UIAE、Reward、CDNPilot、TACO、Demand、Vision、PRIME 等一系列算法将整条音视频链路串联起来建模，构建出完整、精细，同时又真实的个性化视频技术体系。

需要说明的是，抖音在基础视频消费之外，还承载了包括商业化、直播、电商、生活服务、短剧、游戏、搜索等数十种不同业务，需要在更高的性能资源占用约束下，追求流畅度、画质、稳定性、失败率、成本等方向的综合最优，对其中的算法技术而言，就需要其个性化算法涉及的规模和精度，与他人做法拉开跨代、量级上的差距，才能保证市场竞争优势。

与相对“传统”的音视频工作相比，个性化视频技术同时追求算法的实际价值、创新度与复杂度，因此在常规的优化武库之外，会将视野投向包括大型推荐模型、强化学习、控制论、因果推断、运筹优化、认知科学等在内所有具备潜在可能的技术，令其与音视频技术结合，交融并汇，才有希望达成“具备跨代、量级差距”的效果。

**02 |****服务端：从单点规则到系统运筹**

**2.1 视频价值预测：VLP**

**V****LP（Video Lifecycle Prediction）**是大型短视频服务需要回答的一个基础问题：每个视频（预期）到底值多少钱？这个值将决定转码资源的分配优先级、CDN 缓存策略和分发权重，甚至影响前处理流程、内容理解的推理预算。每天抖音有几千万到上亿条视频上传，传播与消费价值差异巨大，需要模型对每条视频的未来价值（vv、播放时长）做出预测，才能更精确地决定在后续链路上如何处理与干预。

抖音或其他短视频 App 的生产-消费模式，均处于一种基尼系数极高的情况，极少的视频投稿就可以覆盖多半以上的视频播放，而由于大量对视频的处理——例如转码、前处理、内容理解——十分昂贵，在满足基础服务及内容安全要求的前提下，提高大规模视频处理系统的整体效率成其为必然。

本质上，虽与 Ranking 或 CTR 问题有别，VLP 面对的仍是一种高精度的预测问题，适合用与推荐、商业化等领域相近的解法，因此有参考许多字节内外推荐团队的工作，未来的思路也会尽力与推荐、计算广告等领域的前沿工作对齐，吸纳其在建模、模型结构、特征运用、样本分析等方面的进展，并针对音视频领域调整。

**VLP v1（2021）** 让视频价值第一次在音视频链路中高精度地被计算出来，此前业务只能按粉丝数、历史播放vv做规则排序——也是业界的习惯做法，一些视频服务曾构建过预测服务但精度甚低，VLP v1 搭建了完整类推荐的召回、排序链路，引入数十个作者、视频特征，用排序模型把价值预估变为监督学习，将输出归一化到 0~1 的热度分供转码排序使用。**VLP v3（2023）**第一次使用超大规模稀疏 DNN 并支持天级更新，稀疏特征经 Embedding 拼接后送入多层前馈网络，用 LHUC 方式依据作者/类目表征生成取值  [0, 2]  的逐层缩放向量做个性化调制，以 BIAS 让关键特征直连输出层（wide & deep 思想），同时从「单一价值分」升级为多任务，一个模型同时预测未来 1d/3h 的 vv、完播、播放时长等目标，并用 GradNorm 自适应平衡各任务损失：

（往左滑动查看完整公式）

**VLP****v8（2026）** 深度实践了 LRM scaling-up 路线，进一步推动了个性化推荐、计算广告与音视频领域的技术交叉，v7 的人工特征交叉（MMCN 等）结构复杂且天花板低，self-attention 加深后 token 表征趋同（cosine相似度 0.9+，即 over-smoothing），v8 在广泛尝试对比了不同推荐技术进展的效果后，选择字节推荐团队的 TokenMixer 结构堆叠替代特征交叉主干，用 PerTokens AFFN为FFN 引入 token 级自适应门控，剪枝冗余结构后将 dense 参数扩至 1B，可验证视频价值模型同样服从scaling law（Reg-AUC 较 v7 +1.36%，MFU +167%），其核心结构与规模规律可概括为：

（往左滑动查看完整公式）

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/FGB4hYw9Fee3qGEYpgRyBicZ7ia2H9I7xo0wZvib5iatiazSU41lJytxBvwibPVUuHssUbp98ghBml3fic16PolZ8Gr8mQj0bUzXayGuG8tJc9Sn6o/640?wx_fmt=jpeg&from=appmsg)

图1：VLP v8 的 TokenMixer 主干、Adaptive-FFN 与 Mixup 结构

配合模型复杂度提升，v8 在特征侧同步做了大幅度扩展，新增了数十个 LLM 挖掘特征（视频互动水平、投稿信息、作者生态等），基于视频内容理解大模型生产的 124 个高阶语义特征（音视频画质、美学、结构、热度分析、...），接入多模态 Embedding 和投稿侧序列特征等。此外，拆分了 **CAPP**（Content and Creator Profile-Aware Popularity Prediction）模型作为 0vv 冷启动场景的补充，专门解决新视频在无历史数据时的流行度预测问题。

**2.2 档位组合决策：UIAE**

档位组合解决**「给每个视频转几个版本、每个版本什么规格」**的问题，由于视频压缩基本不可瞬时完成的特性，对同一源片提前准备多个码率/档位视频给不同用户（或同用户的不同访问时段）消费，以求取更高的用户体验，是行业惯例。

与 Content Aware Encoding 内容感知编码受到「传统」音视频算法工程师的关注不同，由我司参考 Brightcove 公司Context Aware Encoding 概念所开创的档位组合（UIAE 及其前序技术）方案视野更投向链路乃至业务的整体最优，首次令服务端与客户端的音视频链路得以形式化的方式串联到一起，将优化目标与终极目标重新塑造一致并统筹优化，是个性化视频领域的基石技术之一。个性化视频技术追求全链路精确可计算、全链路最优化，UIAE 的发展将视频处理与用户未来动态的选择进行链接，支持精确预测与在线运筹，指向全链路的理论上限。

**UIA****E（User-Item Aware Encoding）**前序使用的方案主要采用离线预计算出的固定档位组合，在不同国家和地区均曾取得良好收益，而 UIAE 的思路是，根据用户播放行为和视频编码特性，实时地动态输出可变组合，同时把决策粒度从「群体统计」推进到「用户×视频」，在转码成本约束下最大化个体期望体验：

（往左滑动查看完整公式）

参考：A User-Item Aware Encoding Framework for Short Video（https://ieeexplore.ieee.org/document/11461328）

**UIAE v1（2024）** 把前序方案的固定组合改为模型预测的可变组合，将问题建模为带约束的最优化，以各档位的播放概率 p(R) 对体验加权求期望，在码率区间、相邻档位码率差、档位数量与 CRF 等约束下选出期望 QoE 最高的一组档位，简化来看，QoE 可视为画质、卡顿、首帧三项 QoS 的组合，当视频价值上升触发「加转」时会触发重新计算：

（往左滑动查看完整公式）

**UIAE v2（2025）** v2 补回了 v1 中被简化的变量，沿「系统拆分+场景细分+自适应」的方向精细化，先按不同系统分别预估 QoS/QoE，把播放环境按不同选档策略细分统计概率，使用 Convex Hull 在 RD 曲线上筛出高性价比候选 CRF 点、枚举生成候选组合集合，再让不同编码器基于各自线上 Context 联合决策。QoE 则改进为 mVMAF（VMAF 的均值变体）、码率、卡顿时长的组合，超参数随场景与人群差异化（如 iOS 画质权重高于 Android），最终取期望体验最大的组合并辅以规则微调：

（往左滑动查看完整公式）

**UIAE v3（2026）** 沿同一决策框架扩展，新增 864p 等多个非常规候选档位，并调整多个现有档位超参，同时把转码决策与多码率下发策略联合优化——将设备能力、高峰 / 非高峰时段、大包 / 小包等下发规则纳入约束与统计场景（如低端机过滤高码率档、窄屏低清处理等），即目标函数不变，但在候选空间与可行域上大幅提升：

（往左滑动查看完整公式）

**2.3 转码资源调度：Reward**

Reward 算法回答大规模音视频链路中另一个未曾充分建模的问题：有限的转码资源如何分配给海量视频？抖音每日亿级投稿量下，转码集群容量始终有限，Reward  将问题看作资源约束下的收益最大化问题，从召回的 { 视频，档位 } 候选中选择子集提交转码，使总收益最大。

Reward 算法与 VLP、UIAE 算法一道，逐步构成了个性化视频链路中转码端的三大核心算法，将大规模音视频系统的最优化问题，进行了关联到全局收益和成本的完整建模。具体到算法本身，由于其明显的运筹属性，未来存在参考广告库存管理、物流调度、激励投放等领域的前沿技术，辅以音视频领域的先验知识，进一步提升的空间。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/FGB4hYw9FeeZQZibh9J2Px1E0WlzW6ec94IBaSibIKLXj2wYiaZibo7Q0nNibkWSZJKwXARjZnNWZd1ictLALSylyJB2pWDicbWmZhdCqH4X9NRccY/640?wx_fmt=png&from=appmsg)

图2：Reward 从投稿事件到价值判断的召回、粗排、打分与UIAE剪枝链路

**Reward v1（2024）**

以 Reward = Income(QoE) - Cost 为目标、TotalAvailableCost 为总资源上限，将其建模为背包问题，以动态规划求解，落地时做了剪枝，只保留码率收益一项，简化为：

（往左滑动查看完整公式）

码率收益取自码率光谱（大盘新增某档位后的平均码率变化），基础档位之外仍按视频价值分排序提交。

**Reward v2（2025）**逐项补回剪枝，码率收益改由预估模型给出（基于原视频与已转档位的预测差），免去码率光谱每加一档都需要重新统计，补回 QoE 项并以统计映射近似![](https://mmbiz.qpic.cn/mmbiz_svg/Q3auHgzwzM6h16AKqRB9N1XBcS7AGsS7YuviaNjgFn16Vib8PhWBmjO0nOJZpV0jUXYQ3b5s3I1u9zTHIdFmkCO8uJxcsbhwbZianbT64ldTEvkZ3OMeKUnIQ/640?wx_fmt=svg&from=appmsg)，目标函数扩展为：

（往左滑动查看完整公式）

指数项是编码耗时对收益的折损（价值按未来 24/3 小时计，编码过程不计收益），并将原本独立的两条编码器队列合并为混合调度，按拥堵程度动态分配普通档位与档位组合的资源比例。

**Reward v3（2025）**转向解决高价值档位的重复转码，用小时级时序价值分二次推断能否达到阈值（阈值取 0.8 时准确率超 90%），新增 0vv 价值分，同时把 UIAE 触发门槛降低下来，优化了长视频与转码耗时的 trade-off。但 v3 仍有部分瓶颈，决策范围窄、粒度粗、容量调节被动滞后（仅凭回传队列长度后验调整，恢复慢）。

**Reward v4（2026）**针对以上瓶颈升级，调度范围扩到所有线上档位（包含 UIAE 档位），而目标函数精细到视频粒度：

（往左滑动查看完整公式）

* 其中![](https://mmbiz.qpic.cn/mmbiz_svg/Q3auHgzwzM7LGVoYHRZ4icUra5KGKcYXaiaSAicra4hwu6m3cVPO07Hic3R0URK2GbpCrVvuDMB3v6y9BU45mzcCjGhlwbp4tKbUBjkLKdpXf7AsMav7yLOFiaw/640?wx_fmt=svg&from=appmsg)由 VLP 预测，![](https://mmbiz.qpic.cn/mmbiz_svg/Q3auHgzwzM7mvWQw2AQMRJ6SiamUrToGsXc1Jd3ibmShQWb8A4ZVMNxQic3T8hvfpMHg7CfibSMPSiburqrwMicZicDiceIAhe4gvsnwKUgpeOmoolibicjvltvebwpA/640?wx_fmt=svg&from=appmsg)与![](https://mmbiz.qpic.cn/mmbiz_svg/Q3auHgzwzM5UicYYEZx73EicKibdsOwjZrcSle1ro4mzoB8ibpr0KmtwROla8Z3A6896UtxHMGgb9tLtAl6Efoia3KsAczZgyzdsIgBmHHwc7GIoY0s7EXYoEZQ/640?wx_fmt=svg&from=appmsg)由多目标模型预估，![](https://mmbiz.qpic.cn/mmbiz_svg/Q3auHgzwzM7sk0EkHD8nb387bgeNkKVpDYKPc9UpetsNZZf0KUAdXR6bRFEJSeicmyxrjJ8Nxc7DR7g3Ht08ujXw6Sh1yH0BDYfFQHnIDO5ibmZyOnLs3BIw/640?wx_fmt=svg&from=appmsg)为耗时折损函数（对预期高峰 vv 却需较长转码的任务加大惩罚，因档位转出前无播放收益），𝓇 为仅作用于 UIAE 的经验权重，用于提升提交 UIAE 档位倾向的超参数。
* 容量侧用 G/G/1 排队论建模转码队列，以 Kingman 公式估计平均队列长度![](https://mmbiz.qpic.cn/mmbiz_svg/Q3auHgzwzM4zbeIqcsK6WPFCyyADxtdS3L7NibAXcZew7GjmK6pbjIIHOibibhiahsrcqgXPzfE3ibToWTciacJxF1vcelvZbLMDKeiccUSugmiaByul3u9ZfNGYmA/640?wx_fmt=svg&from=appmsg)（![](https://mmbiz.qpic.cn/mmbiz_svg/Q3auHgzwzM6jmyMibsBoEZVia7iaVLYXfnrMzuJFGtOKw72tibxywruicU77rSas1z1mwibgUibAvKiaLjibxQZlsMC8da6ZTTZ05ibjLdNwBXeKjH6Cc516HRcF5lpA/640?wx_fmt=svg&from=appmsg)、![](https://mmbiz.qpic.cn/mmbiz_svg/Q3auHgzwzM7KGRk8Ml2tCtgAfdPW8Ss7f25txTicORV3QVQGCjPNukfMYOANCAGccIpy52ALHE3GsVIyJPiaeP0aiaFOST4XopReG0iaHBgZALd8ibL2TlZghiaw/640?wx_fmt=svg&from=appmsg)为入/出队变异系数，![](https://mmbiz.qpic.cn/mmbiz_svg/Q3auHgzwzM5W0pSoibmQkFVibLDke7EARVXlZUxicyjypPZkMcKQAxmsH6UBbSBItRhzPmFCoxlGRWicrSV9IFQserteuWHbqMdYpkck3KHIMuCyRpONrC70UA/640?wx_fmt=svg&from=appmsg)为利用率，EWMA/EWMV 滚动更新均值方差），锚定目标L₀反推提交速率 ![](https://mmbiz.qpic.cn/mmbiz_svg/Q3auHgzwzM6ZGVmlgicr1yyskdmOzRJtGRdo5h9ObZmxGdYdd7dib7aEf0yibw8g2icfVDFlOx8DdBk7icGDxCg7ianIJUxJuqnBV5TO1BZjmvQUQicWicnxuCpl6Q/640?wx_fmt=svg&from=appmsg)，再按![](https://mmbiz.qpic.cn/mmbiz_svg/Q3auHgzwzM7pIp0BMlb489xxlGPvBR7r8M0PZwOa9hTDFCBHWot0PHjiaKsqKRx9oxicwVibxnDhoRdIjcnPC7OzvWIicY2ZK1bInIeeKWeHAhouETM8jhDlhA/640?wx_fmt=svg&from=appmsg)映射为每次提交上限，未来还可以视频内容与档位为 State、提交为 Action、带宽/体验为 Reward，用在线小流量 RL 学习更优策略。

**IdleTrans（2025）** 是 Reward 算法的闲时调度补充模块，把夜间等闲时的闲置算力转为增量转码资源，由于闲时允许任务堆积、提交侧不感知实时资源，故建模为**无资源约束的最优化问题**，只在「视频×档位」粒度最大化净收益：

（往左滑动查看完整公式）

其中![](https://mmbiz.qpic.cn/mmbiz_svg/Q3auHgzwzM7B8picx8lL1LTQoztmEicxRTDx00RNvQ6h3FMVibzjjvib9EtTJBuhfdE7SRZFUUgM1Hr897ibZnMibia66SyxMibXMY5pQMTbq06KZ5etZXVABes2UQ/640?wx_fmt=svg&from=appmsg)为画质/QoE业务价值，![](https://mmbiz.qpic.cn/mmbiz_s...