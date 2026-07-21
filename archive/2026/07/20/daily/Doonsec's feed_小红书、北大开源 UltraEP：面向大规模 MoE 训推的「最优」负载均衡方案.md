---
title: 小红书、北大开源 UltraEP：面向大规模 MoE 训推的「最优」负载均衡方案
url: https://mp.weixin.qq.com/s/rAoF65ywi5trWbI-heJieg
source: Doonsec's feed
date: 2026-07-20
fetch_date: 2026-07-21T05:01:11.689253
---

# 小红书、北大开源 UltraEP：面向大规模 MoE 训推的「最优」负载均衡方案

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/P9Hs04VFGRk4Dq4RGhWAqHnhyJG7aPeXZsoxVwo8kianPN1XeQTafpQIg4x7c25WSSTgBz5IuhiaxI5icHtPuuUhoWxU4YdHE22xtUtEe9hSia8/0?wx_fmt=jpeg)

# 小红书、北大开源 UltraEP：面向大规模 MoE 训推的「最优」负载均衡方案

小红书技术REDtech

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz_jpg/P9Hs04VFGRlsGER6MmllB6yju1icYiaGmCFKuH2oUcS3AEWhYlLNiax2YcZQYXPL04Hm1Nib3v7OpBRzWlkia8IbAZOCbRUsMecniaCvHaxMzpgdU/640?wx_fmt=jpeg&from=appmsg)

随着新一代混合专家（MoE）模型的总参数量迈向万亿规模，专家并行（EP）已经成为训练和推理的主流方案。

但一个常被忽略的问题是，即使模型在预训练时已经做了负载均衡算法调控，在真实训推中，不同 GPU 的计算负载仍然可能相差数倍。

这意味着：

* 有 GPU 提前算完却只能等待；
* token all-to-all 通信也出现瓶颈；
* 高负载 GPU 的峰值显存骤增，易触发 OOM；
* 理想（完美均衡）吞吐和真实水平相差多达一倍。

为此，小红书和北大提出**UltraEP**，首次把基于「精确」路由信息的「实时」负载均衡引入生产系统：在每个 microbatch 和每一层动态复制热点专家，让真实训推也能逼近理想性能。

UltraEP 平均达到理想性能的 **94.3%**，相比业界 SOTA 训推框架提升**1.49 倍**，并应用在了大规模预训练的实际生产中。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/P9Hs04VFGRlGBmoibopuwQiccZFLREtvU0u1es5ll9ehayd9eTHdBEhibDQnmASV8C0eYm1Els8mk4JgGOCe24rgjlQJdic9M2TOvQdABhqTmBY/640?wx_fmt=png&from=appmsg)

**论文：**

https://arxiv.org/abs/2606.04101

**技术报告：**

https://dots-infra.github.io/UltraEP/zh/

**代码：**

https://github.com/Dots-Infra/UltraEP

随着 MoE 模型参数量不断扩大，大规模专家并行在生产场景中越来越常见：专家分散在不同设备上，token 通过 all-to-all 通信在专家间交换。

![](https://mmbiz.qpic.cn/mmbiz_png/P9Hs04VFGRmkcNQBlkz9EFT0icH68e3ibu4hkMubM8LL9R6Y49EnxHHTZwAj0ws5hwU4I0aKHkPgs7f4IYGyDIMibupyRczr3ChXkPMp9PP2Zo/640?wx_fmt=png&from=appmsg)

**专家负载不均**是影响实际训推吞吐的关键变量：路由是动态的，不同专家、不同设备接收到的 token 数天然不均。

现有方案里最有代表性的是EPLB (DeepSeek, 2025)（https://github.com/deepseek-ai/EPLB），它根据上一个时间窗口的历史路由，周期性地重新摆放专家。这类“预测性”方法有个隐含前提——负载得是相对静态的。

![](https://mmbiz.qpic.cn/mmbiz_png/P9Hs04VFGRlIeRhshmpxhJFibmXePicRQJyH9JiahdibhHe7fXz3b3aLiblPvicAdDoaNEHdZXSjPPnp8VIybvsrHVshRqYjiaqFEiccmseibRBTegoA/640?wx_fmt=png&from=appmsg)

可现实恰恰相反。当下主流的细粒度 MoE（几百个“小”专家）负载高度动态，历史信息很快过时，冷热专家预测频频失准，均衡操作甚至会变成负优化。

**UltraEP 为什么能做到「最优」负载均衡**

UltraEP 走了一条看似激进、但最直接的路：基于门控后的真实负载，在每个 microbatch 中的每层实时做专家重均衡。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/P9Hs04VFGRlwWNoHLvuRSf5UCSRD8WbvXl7SgqxQkhyIXiaiaMd4GJjGBicPM3qG3jjSu0nniaGU3W768hVuc6bxexMicNEonI00UqViag4v2GicsU/640?wx_fmt=png&from=appmsg)

这消除了预测偏差，但代价也很明显：预测式方法可以提前把开销掩盖或平摊掉，而 UltraEP 的开销全暴露在**关键路径**上，还是在 microbatch 这个最细粒度上高频发生。

基于一个通信前提和一系列控制面-数据面优化，UltraEP 能把关键路径开销压到 **300µs**以内，并达到近乎最优的均衡效果。

首先，UltraEP 限定热点专家复制在高带宽 scale-up 域内进行，避免跨机专家搬运。这是实现百微秒量级专家复制的通信前提。

更关键的是，UltraEP 设计了一个高效的均衡方案在线求解算法，以及一套高度优化的专家权重/梯度通信算子，将均衡操作本身的开销降到最低。

**关键设计：让最优负载均衡走进生产**

UltraEP 的定位是生产级专家均衡库，遵循以下设计原则：

* 独立的 Python/CUDA 运行时，与 DeepEP 或训推框架解耦。
* GPU-native 的计算/通信过程，和 host 没有数据交互。
* 保持数学等价性，以及与其他常用训推配置的兼容性；
* 高效的显存管理，将额外显存开销压到最低。

在这些原则的基础上，我们归纳了 UltraEP 的关键设计：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/P9Hs04VFGRmjng9FT4eUGXa7I6Oj5Xb4LLLoyG08zFM0txtBHuLichialI7BfiaicFUiazSrcaa0TmAnRHNmgNJj2xrkLJTmjqFicLicvRyGEVAhxU/640?wx_fmt=png&from=appmsg)

UltraEP 给每个 rank 预留固定 slot 放“冗余专家”（热点专家的副本），运行时无动态显存分配。副本不需要维护优化器状态，梯度会在反向中实时归约回原专家。

![](https://mmbiz.qpic.cn/mmbiz_png/P9Hs04VFGRnnQYZnOBoHuvqm7I2tNtmuv9o3Alicxj3ziapRJzKrAKsHThic34XObYkCFJK1ZqQficn1YOtTe0D6uKvKmKapynKv7R9fePqKch0/640?wx_fmt=png&from=appmsg)

更关键的是权重/梯度 buffer 采用**跨层复用**：以 Qwen3-235B 为例，单个冗余 slot 的额外显存开销能从 9.9 GB 降到 108 MB。

![](https://mmbiz.qpic.cn/mmbiz_png/P9Hs04VFGRmrMqflvicUib2ia4XCC6Arj4l6cW0PVQ191ZK8nlyCWic93kP9iaY24ZEhSjtiaq9QkAyt3Apu2cJSnpYKFWyhcXJt2XXGh5pb4Fhtk/640?wx_fmt=png&from=appmsg)

实时负载均衡最大的挑战，在于新增的计算和通信是否会拖慢训练或推理过程。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/P9Hs04VFGRntdse8VvHKEKvoUj6xXVCC2ibHIJWz3lj6IkHd8RU5GC5EJTBJxkJ1xddbIOqB2uIWBMI14fB9YgUjoPo1wiblIhicd71ccs2bMs/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/P9Hs04VFGRlczjiaVbuZGKToQSK2Bj9oqMicXvTBcXKezRfWTpiaX8vheEf5UPEWQnPibTQESA5jn1C9CbDhedgLHxuaMZngkehwwwMUEncBGwA/640?wx_fmt=png&from=appmsg)

前向传播中，UltraEP 需要在门控完成后获取全局负载，才能进行**复制方案求解**（replication planning）和**专家权重分发**（weight distribution）。**重路由**（reroute）负责在同一个固有专家的多个副本间分流 token。相比于前两个操作，重路由更轻，且基本都可以被权重分发掩盖。

在控制面的均衡方案求解中，此前方法把“专家放置”和“token 重路由”看作解耦的两阶段，容易互相拖累。

UltraEP 直接求解每个专家实例最终会接到多少负载（quota），把两阶段耦合起来：每一步探索既能实例化新副本，也能更新负载分布。借助 warp-level 并行，EP64 下求解时间仍保持在 100µs 以内。

在数据面上，专家权重分发和梯度归约都是高度动态、稀疏的通信，经典集合通信库和 in-switch 卸载都吃不下这种非规则模式。更棘手的是，少数热专家副本极多，其所在 rank 的对外多播会成为新瓶颈。

为了打满 scale-up 物理带宽，UltraEP 基于持久化算子（persistent kernel）实现，将专家权重或梯度切分成若干 tile，利用内存语义和 TMA 进行异步的卡间数据搬运。

![](https://mmbiz.qpic.cn/mmbiz_png/P9Hs04VFGRmjYEl01Dibb50QwuCyicL68pHyv7YEqjpMjLrTx6QuJIvLzbHQjFhJsWKHWwDXnLzQ5yg1gRyCL1LicibgQSesMicZnkgcHcYVZwx4/640?wx_fmt=png&from=appmsg)

为了消除通信热点，UltraEP 设计了**分片流式中继**（chunk streaming relay）的通信策略，按实时流量构建两阶段中继树，让低流量 rank 帮忙分摊、转发热点流量，并通过 chunk 级流式转发避免全局 barrier 和通信 bubble。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/P9Hs04VFGRkKHOnxZc2Q4Kiajca8Qez2pblibgHrgdEFnf7VtyZ4QbBVx1mnEQWY4DXrPib3GyknR74rPqNQTIxEGS6MW8gPqyJYPK3iaWXvdoM/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/P9Hs04VFGRmEiaVDSElvsnPdAcibKIeW4bXmEEhs2ywgQQEAo2Un8sm8ZWLFnVPgU8j8JRTQ3YTdIDYmiaI6NzGhwHMPZCNXrGnHn6y5aCq8TU/640?wx_fmt=png&from=appmsg)

反向传播时，专家重分发和**梯度归约**（gradient reduction）可以和其他反向计算 overlap。UltraEP 精细控制它们的 SM 占用和共享内存 footprint，避免拖慢反向计算，并用保序累加保证梯度归约的确定性。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/P9Hs04VFGRlMgr74UMjcfnCzvrKPRmVejqEMib08bYV2FtvobbeMg61YSfOialjgxZu17U3KfcicylU9tKpEU95QJy00ib1wJvP7ysHTKPu8Vaw/640?wx_fmt=png&from=appmsg)

除了均衡算法，UltraEP 还提供了一套可视化 profiler，对均衡前后的负载情况进行层次化分析：既能一览全局分布，也能看清每个 microbatch 中具体的冷热 rank 和专家负载，从而全面评估均衡效果和剩余瓶颈。

![](https://mmbiz.qpic.cn/mmbiz_png/P9Hs04VFGRm2r5cVnfYV6VAoAw7ARrme27mhSiabfiaKYOz0WWQUodtg98zE7ur2msEdggPtm0gxKMcM1DZtnVubpXicibSC2Lt4rA7ryesxVcw/640?wx_fmt=png&from=appmsg)

在 Qwen3-235B、GLM4.5/4.7、DeepSeek-V3 等模型上，我们分别基于 Megatron-LM（训练）和 SGLang（推理 prefill）做了评估，训练统一用 EP64 的专家并行，推理则根据模型专家数采用 EP64 或 EP40。

![](https://mmbiz.qpic.cn/mmbiz_png/P9Hs04VFGRnGRcAX7fd9EDvc6LSq6gfNwrE1huZq07RF88fibOHByR1KWeYHSTG0OoCpTS1g9rqOzNx0Dk1HHUpH02oWP0kOIlKqcgKtw6B4/640?wx_fmt=png&from=appmsg)

训练实验结果，包括吞吐（TFLOPS/GPU）和总体均衡度。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/P9Hs04VFGRleDzhBTp47JVmgskLDogpcbbH3pxjvibkJKZVP1vibKicGTEW5BJDfz0OItUmbzYZgOl1C2L5O8RoHnwNwVfngYyvBg8Piad7GU9c/640?wx_fmt=png&from=appmsg)

推理实验结果，包括 TTFT 随每秒请求数（RPS）的变化，以及总体均衡度。

主要结果：

* 训练：平均达到理想吞吐的**94.6%**，相比 Megatron-LM **提升****42%**；
* 推理 prefill：达到理想吞吐的**90%–97%**，相比 SGLang **提升****1.56 倍**；
* EPLB、LPLB 因历史滞后、复制预算受限，效果始终落后于 UltraEP。

值得一提的是，UltraEP 把 rank 间不均衡从 1.30–4.01 稳定压到 **1.01–1.04**。它与理想上限之间剩下的差距，主要来自实际路由下各专家负载的固有非一致性和少量控制开销，而**不是**残余不均衡或关键路径开销。

![](https://mmbiz.qpic.cn/mmbiz_png/P9Hs04VFGRk7VFuDCxbxGZLtQZ5gYeY3tFVxpIicV7IF1gl3DQL2MvC4yiayMnMtCiaLU3PSWHwYwhMFBhJJMy13L5fguBhJb5Mic2PFiccE5sWI/640?wx_fmt=png&from=appmsg)

UltraEP 已经在正式生产中部署。在一个 288B 参数 MoE 模型的完整预训练中，UltraEP 保持了不低于理想性能 92% 的水平，显著提升并稳定了长周期训练吞吐。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/P9Hs04VFGRkhyn3dHOmm7NOFx1CeHwbZDOINn541ib2jEIgeeeD1bT1LfPZYdXn7lO7NmDrb1kiajOYDBiapI6o0Ricu24ZPwtdGMAibPicnjS0To/640?wx_fmt=png&from=appmsg)

UltraEP 的核心判断是：随着通信带宽提升，实时、精确的系统侧负载均衡会成为专家并行的基础能力。算法侧均衡负责训练稳定性和专家特化（specialization），系统侧均衡则负责把每个 microbatch 中已经发生的负载偏斜重新摊平；二者目标不同，但可以自然叠加。

下一步很自然的扩展是 RL 场景。由于面向特定领域数据，且没有预训练中的算法侧均衡调控，专家负载往往表现出ReLibra（https://arxiv.org/abs/2605.08639）观察到的，类似推理 prefill 中的强动态性。因此，UltraEP 有机会成为 MoE RL 基础设施中统一的负载调节层。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/P9Hs04VFGRm2NIq1WpyKmg93FZuhBCpQvMCcPibe37Z4ArxPsuTo1PibHBvpveWPfKXD7JMLJtwqMfxP0qtMJ2VfnDs4qElULgu81xtF9uQJo/640?wx_fmt=png&from=appmsg)

**魏新明**

小红书 dots infra 组实习生，北京大学计算机学院在读博士生，主要从事软硬件协同设计、MoE 训推优化等工作。

**涂涂（戴拓）**

小红书 dots infra 组工程师，博士毕业于北京大学，主要从事大模型预训练框架开发与优化、软硬件协同优化等工作。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/P9Hs04VFGRlh9BFhp3EBiazeV4kjk9PFSr8AvHvo5RYyWM9dlPRDIuNJVSKoKVQmKp5zOfh5PFbsUsI3PSlibyyfgT0FkicEPO71V7gvR8l16E/640?wx_fmt=png&from=appmsg)

**我们是负责支撑dots系列大模型的工程团队 —— dots infra。**团队业务**覆盖大模型infra的核心场景**，包括文本/多模理解大模型的预训练、多模生成模型的预训练、通用/应用等方向后训练、dots 系列模型的推理服务、data infra、模型codesign等多个方向。这里有**硬核且纯粹的工程师团队**，成员拥有顶级技术背景（多篇系统顶会、OI 选手/ICPC world final），日常讨论技术氛围浓厚；还有**行业内最顶级的施展空间**，包括世界级算力规模、全栈自研技术栈、千万级 DAU 战场、Deep Co-design 机会。

![](https://mmbiz.qpic.cn/mmbiz_png/P9Hs04VFGRlyO8icibIVy...