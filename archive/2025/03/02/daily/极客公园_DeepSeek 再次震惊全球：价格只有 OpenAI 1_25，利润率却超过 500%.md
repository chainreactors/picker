---
title: DeepSeek 再次震惊全球：价格只有 OpenAI 1/25，利润率却超过 500%
url: https://mp.weixin.qq.com/s?__biz=MTMwNDMwODQ0MQ==&mid=2653074804&idx=1&sn=a75fc037dcb5ad97464fc7fedac9a6b5&chksm=7e57c8c2492041d41331064bab74282ee1677e240bed2e41c6534576905bb9de3fc4cc0365df&scene=58&subscene=0#rd
source: 极客公园
date: 2025-03-02
fetch_date: 2025-10-06T21:57:33.310275
---

# DeepSeek 再次震惊全球：价格只有 OpenAI 1/25，利润率却超过 500%

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/8cu01Kavc5ZtJknJlWs679Xevox34ssiaw1gCtk4icuLlh9neSd5icS00jTiaEoQV7vj2icCVeC2H5XlsiaMJssRNs9g/0?wx_fmt=jpeg)

# DeepSeek 再次震惊全球：价格只有 OpenAI 1/25，利润率却超过 500%

宛辰

极客公园

![](https://mmbiz.qpic.cn/mmbiz_jpg/8cu01Kavc5ZtJknJlWs679Xevox34ssiaEia7GRrdGb4ZSVcckWVwezImGmcy9aLicGK7HdwIF3PSVEohO9jvg9icg/640?wx_fmt=jpeg&from=appmsg)

DeepSeek 开源周真正的意义，藏在今天的彩蛋里。

**作者｜宛辰****编辑｜**郑玄****

过去一周，DeepSeek 连续开放了 5 个 Infra 项目的源代码，正当大家以为这场开源盛宴已经结束。

刚刚，DeepSeek 的彩蛋来了！开源周 Day6，DeepSeek 官方团队在 Github 和知乎给出了 DeepSeek-V3 / R1 推理系统的技术解读。

先说结论：通过优化吞吐和延迟，**DeepSeek「理论上一天的总收入为 $562,027，成本利润率 545%。」**

敏锐的网友——如 MenloVentures 投资人 Deedy 翻译了这意味着什么：「理论 ARR 2 亿美金、利润率超过 500%，这样的商业效率理应是一家值 100 亿美金的公司。」

![](https://mmbiz.qpic.cn/mmbiz_png/8cu01Kavc5ZtJknJlWs679Xevox34ssiaQvxR5AMsjzX6NBS2BUTEmC2YYtBZibMvkHuaUTfib7ybXSCAh9O9jGsQ/640?wx_fmt=png&from=appmsg)

从 2024 年 5 月发布 DeepSeekV2 以来，DeepSeek 模型服务就以「价格屠夫」示众，总是比行业其他模型便宜 1/10 左右，质疑 DeepSeek 亏本打价格战的声音也一直有。

通过这 5 天开放源代码以及今天的推理系统概述，这一疑虑也被打消，可以预见，模型推理价格越来越负担得起，且服务提供方也有得赚。这一事件的影响也可以通过 X 平台网友展现出刷屏的惊喜得以一窥，「成本利润率 545%，等于说你是在告诉我，我被 Open AI 抢劫了？开源周 Day7 的彩蛋是 AGI？」

**但更大的信号指向生态伙伴，部署 DeepSeek 有得赚。**

一位 AI 领域的投资人向极客公园阐述，「官方技术解读表明，云平台和上下游通过部署 DeepSeek 的服务，理论上收益和利润率可以达到很高」。无论是对于提供在线推理、还是私有化部署等服务的供应商，都是利好。

在这波 DeepSeek 热中受益的云平台硅基流动创始人袁进辉也在第一时间发表了自己的感受，「DeepSeek 官方披露大规模部署成本和收益，又一次颠覆了很多人认知。」

但需要时间适配 DeepSeek V3/R1 模型架构，他表示「现在很多供应商还做不到这个水平，主要是 V3/R1 架构和其它主流模型差别太大了，由大量小 Expert 组成，导致瞄准其它主流模型结构开发的系统都不再有效，必须按照 DeepSeek 报告描述的方法才能达到最好的效率，而开发这样的系统难度很高，需要时间」。

他进一步指出现在**复现这样的推理服务的难度以及 DeepSeek 可能的战略思考，**「幸好这周 DeepSeek 五连发已经把主要模块开源出来了，降低了社区复现的难度。这些成果充分体现了 DeepSeek 团队第一性原理的思考方式和强悍的意志，他们应该是首先是基于某些原因（？）想到了用这样的模型结构，然后发现这样的结构无论是训练还是推理，要做好都有非常大的工程挑战，不过这些问题在他们工程团队来说并不是搞不定的，关键是花那么大力气做完是否有大的收益呢，在最终结果出来前，谁也说不准，他们还是赌了，结果是赌对了。也可能是反过来的，基于系统的出发点设计了这样一个全新的模型结构。」

在 DeepSeek 官方报告中也提示了 DeepSeek-V3 / R1 推理系统的优化目标是：更大的吞吐，更低的延迟。配合技术解读，DeepSeek 开源周放出的 5 个代码库带来的影响力才刚刚开始。

**附：《DeepSeek-V3 / R1 推理系统概览全文**

DeepSeek-V3 / R1 推理系统的优化目标是：更大的吞吐，更低的延迟。

为了实现这两个目标，我们的方案是使用大规模跨节点专家并行（Expert Parallelism / EP）。首先 EP 使得 batch size 大大增加，从而提高 GPU 矩阵乘法的效率，提高吞吐。其次 EP 使得专家分散在不同的 GPU 上，每个 GPU 只需要计算很少的专家（因此更少的访存需求），从而降低延迟。

但 EP 同时也增加了系统的复杂性。复杂性主要体现在两个方面：

1. EP 引入跨节点的传输。为了优化吞吐，需要设计合适的计算流程使得传输和计算可以同步进行。
2. EP 涉及多个节点，因此天然需要 Data Parallelism（DP），不同的 DP 之间需要进行负载均衡。

因此，本文的主要内容是如何使用 EP 增大 batch size，如何隐藏传输的耗时，如何进行负载均衡。

***01***

**大规模跨节点专家并行**

**（Expert Parallelism / EP）**

由于 DeepSeek-V3 / R1 的专家数量众多，并且每层 256 个专家中仅激活其中 8 个。模型的高度稀疏性决定了我们必须采用很大的 overall batch size，才能给每个专家提供足够的 expert batch size，从而实现更大的吞吐、更低的延时。需要大规模跨节点专家并行（Expert Parallelism / EP）。

我们采用多机多卡间的专家并行策略来达到以下目的：

* Prefill：路由专家 EP32、MLA 和共享专家 DP32，一个部署单元是 4 节点，32 个冗余路由专家，每张卡 9 个路由专家和 1 个共享专家
* Decode：路由专家 EP144、MLA 和共享专家 DP144，一个部署单元是 18 节点，32 个冗余路由专家，每张卡 2 个路由专家和 1 个共享专家

***02***

**计算通信重叠**

多机多卡的专家并行会引入比较大的通信开销，所以我们使用了双 batch 重叠来掩盖通信开销，提高整体吞吐。

对于 prefill 阶段，两个 batch 的计算和通信交错进行，一个 batch 在进行计算的时候可以去掩盖另一个 batch 的通信开销；

![](https://mmbiz.qpic.cn/mmbiz_jpg/8cu01Kavc5ZtJknJlWs679Xevox34ssiah3Eq3zSDC9hSJGchb7y0icQ1212cv578wdXzzbSqiasntsLIVcEE0SdQ/640?wx_fmt=jpeg&from=appmsg)Prefill 阶段的双 batch 重叠

对于 decode 阶段，不同阶段的执行时间有所差别，所以我们把 attention 部分拆成了两个 stage，共计 5 个 stage 的流水线来实现计算和通信的重叠。

![](https://mmbiz.qpic.cn/mmbiz_jpg/8cu01Kavc5ZtJknJlWs679Xevox34ssiaib3XwoicSbGrwGVuIKsYGlvquS8nogGx2CjI42ewWra9vrlGqLqbZz1A/640?wx_fmt=jpeg&from=appmsg)Decode 阶段的双 batch 重叠

关于更多双 batch 重叠的细节，可以参考我们的 profiling 数据的 GitHub 仓库：https://github.com/deepseek-ai/profile-data。

***03***

**尽可能地负载均衡**

由于采用了很大规模的并行（包括数据并行和专家并行），如果某个 GPU 的计算或通信负载过重，将成为性能瓶颈，拖慢整个系统；同时其他 GPU 因为等待而空转，造成整体利用率下降。因此我们需要尽可能地为每个 GPU 分配均衡的计算负载、通信负载。

1. Prefill Load Balancer

1. 核心问题：不同数据并行（DP）实例上的请求个数、长度不同，导致 core-attention 计算量、dispatch 发送量也不同
2. 优化目标：各 GPU 的计算量尽量相同（core-attention 计算负载均衡）、输入的 token 数量也尽量相同（dispatch 发送量负载均衡），避免部分 GPU 处理时间过长

2. Decode Load Balancer

1. 核心问题：不同数据并行（DP）实例上的请求数量、长度不同，导致 core-attention 计算量（与 KVCache 占用量相关）、dispatch 发送量不同
2. 优化目标：各 GPU 的 KVCache 占用量尽量相同（core-attention 计算负载均衡）、请求数量尽量相同（dispatch 发送量负载均衡）

3. Expert-Parallel Load Balancer

1. 核心问题：对于给定 MoE 模型，存在一些天然的高负载专家（expert），导致不同 GPU 的专家计算负载不均衡
2. 优化目标：每个 GPU 上的专家计算量均衡（即最小化所有 GPU 的 dispatch 接收量的最大值）

***04***

**参考架构图**

![](https://mmbiz.qpic.cn/mmbiz_jpg/8cu01Kavc5ZtJknJlWs679Xevox34ssiaEosUFEDdd3SmG7SEEqHz9YZL8ckXbWJgJNzxbIUqDnaZA2UH7tWAHQ/640?wx_fmt=jpeg&from=appmsg)

***05***

**线上系统的实际统计数据**

DeepSeek V3 和 R1 的所有服务均使用 H800 GPU，使用和训练一致的精度，即矩阵计算和 dispatch 传输采用和训练一致的 FP8 格式，core-attention 计算和 combine 传输采用和训练一致的 BF16，最大程度保证了服务效果。

另外，由于白天的服务负荷高，晚上的服务负荷低，因此我们实现了一套机制，在白天负荷高的时候，用所有节点部署推理服务。晚上负荷低的时候，减少推理节点，以用来做研究和训练。在最近的 24 小时里（北京时间 2025/02/27 12:00 至 2025/02/28 12:00），DeepSeek V3 和 R1 推理服务占用节点总和，峰值占用为 278 个节点，平均占用 226.75 个节点（每个节点为 8 个 H800 GPU）。假定 GPU 租赁成本为 2 美金/小时，总成本为 $87,072/天。

![](https://mmbiz.qpic.cn/mmbiz_jpg/8cu01Kavc5ZtJknJlWs679Xevox34ssiaz1Mp1TBLBAKhym9TiboFsC5OXA2jjKWrP33ffObiaelv1QIpm0j3sgzA/640?wx_fmt=jpeg&from=appmsg)

在 24 小时统计时段内，DeepSeek V3 和 R1：

* 输入 token 总数为 608B，其中 342B tokens（56.3%）命中 KVCache 硬盘缓存。
* 输出 token 总数为 168B。平均输出速率为 20~22 tps，平均每输出一个 token 的 KVCache 长度是 4989。
* 平均每台 H800 的吞吐量为：对于 prefill 任务，输入吞吐约 73.7k tokens/s（含缓存命中）；对于 decode 任务，输出吞吐约 14.8k tokens/s。

以上统计包括了网页、APP 和 API 的所有负载。如果所有 tokens 全部按照 DeepSeek R1 的定价 ([1]) 计算，理论上一天的总收入为 $562,027，成本利润率 545%。

> 当然我们实际上没有这么多收入，因为 V3 的定价更低，同时收费服务只占了一部分，另外夜间还会有折扣。

![](https://mmbiz.qpic.cn/mmbiz_jpg/8cu01Kavc5ZtJknJlWs679Xevox34ssiaic8lbialxdCYlfaXxQP6HambichusuAmbqrdalVHlAeMWTfrOTJDXa3Zw/640?wx_fmt=jpeg&from=appmsg)

**参考**

1. ^DeepSeek R1 的定价：$0.14 / 百万输入 tokens (缓存命中)，$0.55 / 百万输入 tokens (缓存未命中)，$2.19 / 百万输出 tokens。

\*头图来源：视觉中国

本文为极客公园原创文章，转载请联系极客君微信 geekparkGO

**极客一问**

**你觉得 DeepSeek**

**未来会成为云平台吗****？**

![](https://mmbiz.qpic.cn/mmbiz_png/8cu01Kavc5YTxYGib55rtMHhP1YJ44FLtVGp8Keyg6D2X3AUhgNicT1ibKKh0fE1eiaGqkSXnTlW0ib96ib3HDAIrnVA/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_png/8cu01Kavc5bXib8IGpjbghqj305kKeYibwx0gmZO3iaFibnGncpOnsDNKDciaIH6xNBnpPpk7o5de1RKLzgq70eibBTw/640?wx_fmt=png)

**![](https://mmbiz.qpic.cn/mmbiz_png/8cu01Kavc5an0KBXb9IbCwiajJefiaywlMX2G9daxebRIz0bpONcZbhCkA7mNIG39fwRUOEzpoBIPvAXIuA82B9Q/640?wx_fmt=png)

**热点视频****

苏姿丰：职业生涯我足够幸运，老板给我机会让我成长。

点赞关注极客公园视频号，

观看更多精彩视频

**![](https://mmbiz.qpic.cn/mmbiz_png/8cu01Kavc5an0KBXb9IbCwiajJefiaywlMX2G9daxebRIz0bpONcZbhCkA7mNIG39fwRUOEzpoBIPvAXIuA82B9Q/640?wx_fmt=png)

**更多阅读****

[![](https://mmbiz.qpic.cn/mmbiz_png/8cu01Kavc5brwsvZG3ZkJUx8wibjUltsC0gtlUyzrHz0jibYmBdJqLl3Pic5oOYrj5VVG6GEJGvKQWRMY0luuagrg/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MTMwNDMwODQ0MQ==&mid=2653074667&idx=1&sn=fac18e918cbba8e1b25f79a5e72ff796&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/mmbiz_png/8cu01Kavc5brwsvZG3ZkJUx8wibjUltsCU1hmfZUb6ibkaWvOqEamliazicoNCTv390iczmD0BT2bLmbd7AO8khPZDQ/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MTMwNDMwODQ0MQ==&mid=2653074631&idx=1&sn=f9824515835e9d0c91314215b9913137&scene=21#wechat_redirect)

![](https://mmbiz.qpic.cn/mmbiz_gif/8cu01Kavc5ZENt3gIiatQKstoLiatpXoWBUwkB6tO2b9y2Hoj5HpcnXc5zRJEX6MhbyXJ3q0gjTrrBIUF7boJGDA/640?wx_fmt=gif)

![](https://mmbiz.qpic.cn/mmbiz_gif/8cu01Kavc5YR1a8dIHV2UrCdNIhialnevdQkialrf9oMibXZhuHeD0nPUHuFlYzYB4WYzwnTbhSyAvj9ibZb7ibewPw/640?wx_fmt=gif)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/8cu01Kavc5aZd3zlj8Yykibdibgmjs5Xm2KAOicKZoIGib0c12wVnDwaH10PY2076aqwaK6aCJHd4RibkpVrON2Oh0Q/0?wx_fmt=png)

极客公园

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/8cu01Kavc5aZd3zlj8Yykibdibgmjs5Xm2KAOicKZoIGib0c12wVnDwaH10PY2076aqwaK6aCJHd4RibkpVrON2Oh0Q/0?wx_fmt=png)

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