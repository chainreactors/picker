---
title: ICLR 2026｜快手GoalRank：颠覆两阶段范式，生成式排序迈入Scaling Law时代！
url: https://mp.weixin.qq.com/s/j-CQbAnqP-LvnsDByJjXQg
source: Doonsec's feed
date: 2026-05-15
fetch_date: 2026-05-16T05:13:45.372251
---

# ICLR 2026｜快手GoalRank：颠覆两阶段范式，生成式排序迈入Scaling Law时代！

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1gVUsotpT1W7132ajEusm2fccrZr56ibIuazx9oeLAtIm6rnHqVlGibow9vbDafrrtkjqKN6SGhoqODaHwMno0Jzb1mxriaOhDx1iakJMSiaXBvg/0?wx_fmt=jpeg)

# ICLR 2026｜快手GoalRank：颠覆两阶段范式，生成式排序迈入Scaling Law时代！

原创

快手技术
快手技术

快手技术

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![图片](https://mmbiz.qpic.cn/sz_mmbiz_gif/ZxDY5TMPs0EqL7dlyXD8OFyXn6yNGvQ8uEibL6TkOHqFvaK0bR9GEhZicTHuDtaTficMGS88ecXKIVPnFJCTMz7aQ/640?wx_fmt=gif&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=0)

推荐系统中的排序模块需要解决复杂的物品展示序列的组合优化问题，现有主流方案集中在Generator-only（仅列表生成器）和Generator-Evaluator（列表生成器+评估器）两种范式上，且G-E范式目前在实践中被证明优于G-only范式。

本文从理论出发，论证了两种范式的区别，并发现「G-only 性能的理论上限比G-E的理论上限更高」这一反直觉结论。通过进一步推导，作者得到了GoalRank优化方案，通过reward model引导generator进行学习，并通过组优化方案对抗奖励模型偏差，弥补了传统G-only范式在优化上的缺陷。通过离线实验和快手的线上重排场景验证，GoalRank实现了离线排序指标和线上各指标的全面提升。

本工作相关成果《GoalRank: Group-Relative Optimization for A Large Ranking Model》已被人工智能顶级会议ICLR 2026接收。

![](https://mmbiz.qpic.cn/mmbiz_png/1gVUsotpT1XXacFJNN2Fz85o8eqpk3xr9FnzTrBFdB1Xu6APU2T7pGl52GAygLibnrUMukpojAqgcqnZ64gaVRSaRKqVJH2HpQJJJNRqHDq4/640?wx_fmt=png&from=appmsg)

* 论文链接：https://arxiv.org/pdf/2509.22046

* 代码仓库：https://github.com/Kaike-Zhang/GoalRank

**一、背景和动机**

在推荐系统中，排序（Ranking）阶段决定了最终展示给用户的物品item序列，对用户体验和平台核心收益起着决定性作用。

该阶段从建模上可以定义为一个从一个item候选集（大小为 N）生成一个曝光list（大小为 L，L<N）的组合优化任务，工业界主流的排序方案已历经多次范式迭代：

* 一阶段list生成（Generator-only）范式：从早期的learning-to-rank方案到候选集重打分方案（如 PRM[1]），这类方案建模了候选集中item之间的相互关系，但是并未建模透出list内item之间的相互关系。
* “生成器-评估器（Generator-Evaluator, G-E）”的两阶段范式：先由生成器产生候选列表，再由评估器打分择优。近年来，为了进一步突破性能瓶颈，许多研究通过引入多生成器（Multi-Generator, MG-E[2]）来扩充候选列表池。然而，在排列组合爆炸的搜索空间中，仅仅盲目增加候选数量或生成器数量，性能提升很快就会触及天花板（如图1）。

![](https://mmbiz.qpic.cn/mmbiz_png/1gVUsotpT1UEEGsgFjsibXmaDkaRicdI32eick5CiawSgwUyGs2ggfW3m3QafVXWwlgtUgMvEH43xsAgJMcU8yicum1YiakKl4h5tTPzYSmhAicD9U/640?wx_fmt=png&from=appmsg)

图1：不同ranking范式

##

## 一个反思

##

随着近期端到端生成式召回模型的发展，一个范式层面的问题自然浮现：我们是否还需要复杂的两阶段设计？一个强大的、端到端的“单阶段（Generator-only）”大模型，能否直接输出高质量的排序列表？该如何优化？

## 主要贡献

##

* 理论支撑：证明了单阶段生成器模型的表达能力上限优于多生成器+评估器框架；
* 优化方案：提出了全新的GoalRank框架，从上述理论证明出发给出了清晰的优化方案的数学推导；
* 模型验证：亿级工业场景的落地实践。

**二、打破直觉的理论证明，G-only表达能力更优**

## 2.1 范式能力上限的理论支撑

##

过去，人们普遍认为单阶段生成（G-only）的策略难以捕捉曝光列表内的item依赖关系。但GoalRank从理论层面给出了严密的反直觉证明：单阶段list生成器大模型（G-only）的表达能力上限实际上优于多生成器-评估器（MG-E）框架。

具体的，论文中定义了目标策略  与策略空间  之间的近似距离（KL 散度）：

定理1（Theorem 1）严格证明了：对于由  个小生成器和评估器组合而成的多生成器混合策略空间  ，总存在一个参数规模更大的G-only模型空间    ，其对最优排序策略的逼近误差严格更小。

（具体证明见论文附录）

这一理论推导表明，相较于横向堆叠多个小模型（MG-E），直接扩大单一生成器模型的容量（G-only）能够触达更高的性能上限，但现有的G-only方法由于无法直接建模曝光列表或其他优化方案上的局限性，并非在向这一性能上限进行优化。

## 2.2 组相对优化（Group-Relative Optimization）的推导

![](https://mmbiz.qpic.cn/mmbiz_png/1gVUsotpT1XIEUR2r1Bo0vux2Jevo2uKZnCzqB7ZTsNZavz4YFibA3LmsIwnHfZib4TSVQ4tqoRPEGjb8KZ6K2L6X7DwA1WrpBibjSdpQ1DCRk/640?wx_fmt=png&from=appmsg)

图2：GoalRank训练框架

既然单阶段模型具有更优的理论上限，该如何有效训练它？在真实业务中，我们往往无法获得完美的、无偏的理想反馈（Ideal Reward   ）。GoalRank提出了一种“组相对优化”框架，以下是其核心推导过程：

i. 明确优化目标

假设有一个无偏的理想奖励  ，为了避免模型过度贪婪并鼓励探索，引入熵正则化，最优Oracle策略  服从玻尔兹曼分布：

优化模型其实等价于最小化模型策略    与    之间的KL散度。

ii. 消除奖励模型偏差

现实中，只能用真实反馈数据训练一个有偏的奖励模型  。为了对消掉偏差  ，GoalRank巧妙地为用户构建了一个候选列表组  。当组内奖励差值足够大时，利用组内相对均值  和标准差  ，可以构建出一个鲁棒的参考策略（Reference Policy） ：

iii. 最终的训练目标

通过将大模型的策略  与上述参考策略对齐，可以得到一个完全可计算的、极具实践价值的交叉熵损失函数：

**三、实验结果**

为了验证GoalRank的能力，研究团队在ML-1M、Amazon-Book以及包含上亿次交互的真实工业级短视频数据集上进行了全方位评测。

### 3.1 离线评测

###

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1gVUsotpT1XLu2PyCubiav0q6SM1ojIicCyB8VibKQEicmec9VD4Wu7gGLuVia8WRX4UAEian4HkPC0bv0dck14Rl9kqHAG74Unv5mguB5npg7heE/640?wx_fmt=png&from=appmsg)

无论是对比经典的DNN，还是当前最先进的两阶段模型PIER [3] 、NAR4Rec [4] ，亦或是堆叠了上百个生成器的MG-E架构，GoalRank在 Hit Ratio@6、NDCG@6、MAP@6等所有核心指标上均实现了大幅提升。在大型工业数据集上，Hit Ratio@6提升了25.39%，MAP@6提升了29.63%！

![](https://mmbiz.qpic.cn/mmbiz_png/1gVUsotpT1XSRlsAkvRt7WW3a23BLDicrbhyhVfswx31CUCcjebYCMSQ2jByj5BzNabmfUndexDHFvFagmYwV5VxDibcA0CNH6g0YLJlVMG8U/640?wx_fmt=png&from=appmsg)

此外，当GoalRank的模型参数从1M扩展至0.1B时，性能呈现出持续且陡峭的上升趋势，而传统基准模型在扩大规模后很快陷入停滞。

### 3.2 在线评测

###

GoalRank在快手短视频推荐平台上进行了长达两周的大规模在线A/B测试。

![](https://mmbiz.qpic.cn/mmbiz_png/1gVUsotpT1XpGVs0gib6xYFqVjaibsXG2uSNiaq2woXFwKMRXA0Bo26CFBaq7NxOjmmg6zfeWjJNZxVxFUr8icSAzRdxXhtWX8c9MJ3NibWqUpUE/640?wx_fmt=png&from=appmsg)

与平台线上原有的复杂MG-E [2] 架构相比，GoalRank在App停留时长、观看时长、有效播放量、点赞和评论率等所有核心指标上，均实现了 全面且显著的正向提升 。目前，采用GoalRank混合架构的系统已经成功在全量生产环境中上线部署，直接服务数亿用户！

**四、总结与展望**

GoalRank打破了推荐系统排序阶段长期依赖“生成-评估”两阶段架构的思维定势。它不仅从严密的数学理论上证明了“单阶段大模型”的绝对优势，更通过组相对优化方法提供了一条切实可行的训练路径，为下一代推荐系统的演进指明了一道充满想象力的新航道。与此同时，新的挑战也随之出现，包括但不限于：多任务适配和动态策略调整、跨越单点召回和list排序的端到端列表生成、reward model联合优化。

**参考资料**

[1] Pei, Changhua, et al. "Personalized re-ranking for recommendation." Proceedings of the 13th ACM conference on recommender systems. 2019.

[2] Yang, Hailan, et al. "Comprehensive list generation for multi-generator reranking." Proceedings of the 48th International ACM SIGIR Conference on Research and Development in Information Retrieval. 2025.

[3] Shi, Xiaowen, et al. "Pier: Permutation-level interest-based end-to-end re-ranking framework in e-commerce." Proceedings of the 29th ACM SIGKDD Conference on Knowledge Discovery and Data Mining. 2023

[4] Ren, Yuxin, et al. "Non-autoregressive generative models for reranking recommendation." Proceedings of the 30th ACM SIGKDD Conference on Knowledge Discovery and Data Mining. 2024.

**团队介绍**

消费策略算法部是负责快手短视频推荐的核心算法团队，致力于用强化学习、因果推断、增益模型、跨域学习、元学习、图模型、运筹优化、博弈机制、端上智能等前沿技术持续优化用户的内容消费体验，提升用户对平台粘性和大盘DAU，不断改进冷启动和大盘流量分配机制，促进社区生态的长期繁荣与多种营收指标共同提升。

团队负责场景覆盖快手单列、双列、关注、同城等核心页面。技术成果在KDD/SIGIR/WWW/NeurIPS/ICLR/WSDM/CIKM等顶会上发表，并获得CIKM Best Paper和SIGIR Best Paper Award Honorable Mention。

成员多来自国内外顶尖高校硕博毕业，很多有国内外头部大厂核心团队经历，不乏头顶快Star/阿里星/天才少年/ACM金牌等光环者，同时团队积累了业内领先的人才和充足的算力，期待加入一起探索AI时代的新推荐系统。

**岗位介绍**

* 职位名称

* 推荐算法工程师-【用户推荐与社交互动】
* 推荐算法工程师-【内容生态算法】
* 推荐算法工程师-【创新孵化&评论生态】
* 推荐算法工程师-【极速版单列推荐】
* 推荐算法工程师-【主站关注页】
* 推荐算法工程师-【主APP】
* 推荐算法工程师-【投稿与UGC社区】
* 推荐算法工程师-【多业务混排】
* 推荐算法工程师-【留用实习】

* 职位描述

* 探索大模型与推荐算法结合的下一代推荐系统技术，充分利用大模型的领域知识和学习范式为推荐系统注入新的能量，包括但不限于文本/ID生成式推荐、模型Scaling Law、用户超长序列端到端建模等；

* 探索视频、文本和语音等多模态信号的高效处理方式以及与推荐系统对齐的能力，让推荐系统看懂、听懂和理解世界；
* 混合专家、蒸馏剪枝等兼顾模型性能和效果的技术探索；
* 紧跟行业及大模型技术发展，结合业界前沿技术和业务需求，打造大模型应用的最佳实践。

* 任职要求

* 有较强的工程实现能力，熟悉C/C++、Python、 Java等至少一门主流编程语言；
* 对搜广推算法、LLM(ChatGPT等)/多模态模型(LLaVa、BLIP2、instructBLIP等)模型或者量化/蒸馏/剪枝有深入研究经验；
* 熟悉常用机器学习和数据挖掘算法，优秀的分析和解决问题的能力，同时具有较好的团队协作能力。

* 加分项：

* 密切关注业界最新进展，在国际顶会上发表过LLM/MLLM/推荐等相关论文；
* 有搜广推业务上大规模机器学习优化落地经验；
* 在ACM-ICPC/NOI/IOI编程竞赛或Kaggle等机器学习相关竞赛拿过奖项者优先。

* 投递方式：

扫描下方二维码投递，或投递简历至邮箱：chenyuxi09@kuaishou.com

![](https://mmbiz.qpic.cn/mmbiz_jpg/1gVUsotpT1U03nHLhNuM1Mn1SdjghJQpqIavBw3w1bM2lGNNBpEEGnicvsZGg3yBRZAvib31E04mt2a4ZZ2DYrqtU0mRuEyL7mhEaMc8mcTWs/640?wx_fmt=jpeg&from=appmsg)

【相关阅读】

[![](https://mmbiz.qpic.cn/sz_mmbiz_png/1gVUsotpT1UYzlvAxADvoibv6SOcUWYqpoDdCWHyKeW0mS4LyTgShcLssnsKMVcbk74p7Hc3pX2r6UnzdBfFqKpqv5cHVxw2HRTNHUxXGvjg/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=Mzg2NzU4MDM0MQ==&mid=2247500258&idx=1&sn=b825edfc31618dcd3fd1f53f48ed1332&scene=21#wechat_redirect)

点击【阅读原文】，了解GoalRank详情！

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/ZxDY5TMPs0GnTFDtpq8oAf91ZQDzvLt6LCp56JQCbFT2cT8uZquFdeJOKbmM4fucIPqtAPvMT0X4DpfpuZibic3Q/0?wx_fmt=png)

快手技术

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/ZxDY5TMPs0GnTFDtpq8oAf91ZQDzvLt6LCp56JQCbFT2cT8uZquFdeJOKbmM4fucIPqtAPvMT0X4DpfpuZibic3Q/0?wx_fmt=png)

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