---
title: WWW 2026｜快手提出业界首个情景感知的推理增强生成式搜索框架，从“关键词匹配”走向“语境理解”
url: https://mp.weixin.qq.com/s/IVBUbra0tICOhulJREFlAQ
source: Doonsec's feed
date: 2026-04-27
fetch_date: 2026-04-28T05:25:35.916840
---

# WWW 2026｜快手提出业界首个情景感知的推理增强生成式搜索框架，从“关键词匹配”走向“语境理解”

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1gVUsotpT1Wl1ECONNQ9AJJasSYxaicaAWsOKpzzECBu5XF2m55pxMJUyHibwCEoVg4yXr56uv3pd9ODm4OAG1kt7YibhQibFgjJ0n8sLcrgLuI/0?wx_fmt=jpeg)

# WWW 2026｜快手提出业界首个情景感知的推理增强生成式搜索框架，从“关键词匹配”走向“语境理解”

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

在电商平台中，用户每天都在与搜索框展开对话，而输入的关键词往往只是其真实需求的冰山一角，简单的查询背后往往包含着丰富的语境信息——用户的地理位置、历史搜索轨迹、最近的浏览与点击、甚至当前的时间与场景等。当一位身处西宁的35岁男性用户在深夜检索“专业装备”时，他指向的究竟是抵御极寒的户外服饰，还是追求高性价比的数码产品？传统的搜索引擎往往依赖关键词匹配或基础的向量检索，而难以穿透表象，精准洞察那些隐藏在时空、行为、画像背后的深层逻辑。

为解决这一问题，快手技术团队联合中国科学技术大学提出了业界首个上下文感知推理增强的生成式搜索框架——CRS（context-aware, reasoning-enhanced generative search），通过赋予大语言模型情境思考的推理能力，实现了从“关键词匹配”到“意图深度理解”的跨越。本工作相关成果《Towards Context-aware Reasoning-enhanced Generative Searching in E-commerce》已被人工智能顶级会议WWW 2026接收。![]()![]()

![](https://mmbiz.qpic.cn/mmbiz_png/1gVUsotpT1XTKX8zc76IJ7fdzMl9GdH0jFIeejfROibiaDibl1QVCN8xibibXDc5X0ZFHJ5T9Jb0FPs6OH55uvCRicibiatxyRjwO8zvUQgIiauYfzJU/640?wx_fmt=png&from=appmsg)

* 论文标题：Towards Context-aware Reasoning-enhanced Generative Searching in E-commerce
* 论文链接：https://arxiv.org/abs/2510.16925

**一、研究背景：被忽视的“搜索上下文”**

电商搜索系统的目标是让用户在最短时间内找到最合适的商品，然而现实搜索场景高度复杂：

* 用户意图模糊：输入“手机壳”可能意味着想找“适配某一特定手机型号的的透明壳”或“带支架的防摔壳”；
* 空间上下文：在北方寒冬搜索“保暖”，用户可能需要羽绒服；在南方搜索“保暖”，用户可能更倾向于轻薄的发热内衣。
* 行为上下文：用户刚浏览完“羽毛球拍”，紧接着搜索“YY”，其意图极大概率是指向某一特定球拍品牌。

传统匹配式方法依赖词项重叠，深度语义检索虽能捕捉语义，但仍主要基于单次查询，缺乏对时序语境和行为链条的建模能力，难以有效挖掘上下文与目标商品之间深层的逻辑关联。这导致搜索系统懂词不懂人，两者之间的鸿沟正是情境感知生成式搜索要跨越的边界。

**二、方法简介：CRS的三大核心模块**

为解决以上问题，CRS框架从表征、推理、优化三个维度进行了系统性创新：

* 统一的上下文表征与语义对齐（Context Representation & Alignment）
* 自进化推理增强范式 (Self-evolving Post-training)
* 排序感知强化学习算法（R-GRPO）

2.1 统一的上下文表征与语义对齐

##

CRS的核心创新在于让 LLM 不仅读懂搜索词，还能理解搜索场景。我们提出了一种文本化的上下文表示机制，将复杂的异构信号（用户信息、历史交互、实时点击、当前查询）统一转化为结构化文本序列（JSON），包括：

* 用户上下文：历史查询、点击与未点击商品、时间与地点等；
* 商品上下文：标题、品牌、价格、销量、类别、GMV等结构化描述。

这使得CRS不再依赖繁琐的特征工程，而是通过语言模型自身的语义理解与世界知识来解析复杂语境，实现语义与结构的对齐。

此外，团队将商品内容进一步转化为语义化ID（Semantic ID, SID），通过多层残差K-Means量化生成紧凑的编码表示。每个商品最终对应一个独特的四层语义码（如 <a\_23><b\_1><c\_124><d\_0>），并被注册为LLM的新词表，使模型能在统一的文本空间中直接生成目标商品。 这一“语言化索引”设计，让生成式搜索拥有了端到端推理的可能性——模型不再仅匹配候选，而是在理解语境后直接生成目标商品的语义标识，实现从查询到推荐的一体化生成。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1gVUsotpT1W18eSdVIUzFUuibloa8F6CPA5Butf9QO7dAAiam7vo0z3JfG0zA6cK7aR2yyGwvaUic20RHuttWrz8eDhjqqcAX36ibCKqBicHyKKo/640?wx_fmt=png&from=appmsg)

最终，通过上下文-SID预测以及物品-SID映射等自监督的预训练任务，模型实现了LLM通用知识与电商特定业务语义的深度融合，为后续的推理打下了坚实基础。

##

## 2.2 自进化推理增强范式

如何让模型具备真正的电商情境感知推理能力？

在电商场景中，我们并没有像数学或问答那样的标准推理链条可供监督。为此，CRS提出了一个极具创造性的解决方案——自进化后训练（Self-evolving Post-training）。

这一过程可理解为一种“自我进化循环”：

* 初始化阶段：模型先在少量高质量语境推理数据上进行监督微调，学习基础的推理格式与思考逻辑；
* 探索阶段（RL）：模型在数据集上自由探索，对错误预测样本重点优化，实现推理策略的自我修正；
* 利用阶段（SFT）：将RL模型生成的正确推理轨迹作为样本重新进行微调，锁定并泛化优秀的推理能力；
* 循环往复：通过“探索—利用”交替，模型不断强化其语境推理能力。

这一机制有效解决了缺乏高质量标注的问题，使模型能在真实交互数据中“自我成长”。

![](https://mmbiz.qpic.cn/mmbiz_png/1gVUsotpT1UrcfehWqqboWoT9xNMPibquTFGjYOZrhObia4BtCJTNTpT3f5r2sMekv3vprbC0hry0Q3h5dp7mKuxmK0VMmzYnWsTSV2KMtqJc/640?wx_fmt=png&from=appmsg)

##

## 2.3 排序感知强化学习算法

##

传统的强化学习算法在应用于搜索任务时，往往只关注Top-1结果的准确性，忽略了搜索系统本质上是一个排序（Ranking）问题，导致以下两个核心问题：

* 优化目标错位：仅关注top-1结果，忽视整个排序列表的质量；
* 奖励估计偏差：错误轨迹也可能获得相同奖励，导致学习信号混乱。

针对这些问题，CRS基于经典的GRPO算法设计了R-GRPO，从机制层面引入了排名感知与去偏估计：

* 多级奖励设计：同时评估推理格式、结果有效性、语义匹配与排序质量；
* 分层累积分数计算：通过加权排名函数将完整排序表纳入优化目标。

![](https://mmbiz.qpic.cn/mmbiz_jpg/1gVUsotpT1V7AGfSNibowv7ZYuvNEWwbbH23jkSktEnj6F4pL4DrIOhmDa6PfyMvyBqToicaPFqeHGcicpMokFeynkv2HITPxicTQspjb1v5YY0/640?wx_fmt=jpeg&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/1gVUsotpT1XbsWAZtPNqjILQ3CAzMzFkaxo65ofLDgTuRhC2PszJFAicXKlsC5fMaMoRFnsYxF30Jibcf7XjGJibv3IFnJibic6Cu7A4At6Q2Kvk/640?wx_fmt=png&from=appmsg)

实验表明，R-GRPO在每一轮训练中均显著优于原始GRPO，在HR@10与NDCG@10上平均提升约1–2%，为大规模搜索推荐中的RL优化提供了可复用范式。此外，由于算法只修改了rollout过程以及相应的奖励估计方案，其可以很容易地扩展到最近的RL算法的各种变体。

总而言之，CRS框架的三个核心模块相辅相成。统一的上下文表征与语义对齐为大语言模型理解复杂的电商语境提供了结构化的通用语义基础；自进化推理增强范式创造性地解决了电商场景下缺乏显式推理轨迹标注的瓶颈，使模型能够在不断探索中“自我进化” ；而R-GRPO算法则通过引入排名感知机制，精准纠正了传统强化学习在搜索推荐中优化目标错位和奖励估计偏差的固有问题 。这三者的深度结合，让模型不再是机械的检索器，而是真正具备了端到端语境推理与推荐能力的“智能导购” 。

**三、实验结果：语境推理的力量**

为了全面验证CRS框架在真实电商搜索场景下的有效性，我们基于快手平台的大规模真实搜索日志进行了深度的实验评估。这些实验不仅横向对比了传统的匹配式检索模型与前沿的生成式基线，还针对细粒度垂类检索、长尾冷启动等复杂的现实挑战进行了多维度的剖析。

## 3.1 离线效果

##

团队基于快手电商平台的大规模真实搜索日志构建了All-100K, All-50K, Fashion-27K三个离线数据集，并在此之上进行了广泛实验。结果显示，CRS在HR@10和NDCG@10等关键指标上显著优于BM25、BGE等检索模型，以及DSI、LTRGR等主流生成式基线：

![](https://mmbiz.qpic.cn/mmbiz_png/1gVUsotpT1VVyn9G36KX1C6MORJxt6PLWgmXQrAjjyiaFHnZfueUWLyCNm3oly7w4DSEhmKF74zFqlxy7Nq7WsGL09SEosrr54EEBBy8s91M/640?wx_fmt=png&from=appmsg)

在具体的离线表现上，相较于当前表现最优的基线模型，CRS在All-100K和All-50K这两个大规模综合数据集上取得了3%至11%的显著提升。更具突破性的是，在商品同质化严重、对细粒度意图识别要求极高的Fashion-27K（服饰类）数据集中，CRS实现了高达约47%的相对性能飞跃。这充分证明了显式的语境推理机制在挖掘模糊查询背后的真实意图时，具有传统单点匹配无法比拟的创新优势。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1gVUsotpT1UScEtsmXhAkEviam8eJplgRwibDHXvwibovLicfdfI1T7uj5sKYmOZLxBnBbdfoj4jaCASWibhgdkcaLZWQ0KVmhPNOHFJrEVKl7Xw/640?wx_fmt=png&from=appmsg)

此外，在工业界极为看重的可利用性和扩展性方面，CRS同样表现优异。研究证实，随着底层基座模型参数量从0.6B扩展至1.7B甚至4B，CRS在各项评估指标上的表现呈现出持续且稳定的增长。这种优异的规模扩展性，意味着该框架可以根据业务场景的实际算力限制进行灵活定制与部署，为不同体量的电商平台提供了极高的工程实用价值 。

## 3.2 冷启动分析

##

此外，在用户历史行为不足的冷启动场景中，CRS依旧展现出强大的泛化性，性能提升达8.55%，表明其上下文语境式推理机制能够帮助模型推断用户潜在兴趣。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1gVUsotpT1VCYtPGMMJXIWmoqHuSAbm9caL2kDgzLHcq6icGySpeXsAibs9QHibbpMoweMXydIcU0ZpufQgnTRpqEbPiaeziczU3fykG8CmX4u6c/640?wx_fmt=png&from=appmsg)

综合各项实验数据可以看出，赋予搜索系统“思考”和“推理”的能力，为其性能上限带来了质的飞跃。无论是在常规的大范围商品检索、极具挑战的细粒度垂类推荐，还是用户行为数据稀缺的冷启动场景，CRS框架都展现出了压倒性的性能优势和强大的泛化能力。这不仅验证了“文本化上下文理解+强化学习推理优化”这一技术路径的科学性，也为其在更广泛的工业级搜索、推荐和广告业务中的大规模落地验证了可行性。

**四、意义与展望**

CRS的提出不仅是一次算法创新，也在重新界定搜索这一传统任务的方式。它使搜索系统逐步具备更接近认知层面的能力，能够在处理信息时结合用户语境进行理解，并进一步对潜在意图进行推理，同时通过持续反馈实现自我优化和演进。

在这一变化过程中，电商搜索的核心逻辑也在发生转移，逐渐从以相关性检索为主，转向以意图理解为中心；系统的工作方式也从以词级匹配为基础，发展为更接近对话式的理解与响应。

未来，团队将进一步探索大语言模型在排序阶段的强化学习优化、实时更新等方向，持续推动端到端生成式系统在推荐、广告等多业务场景中的广泛应用。

**五、关于我们**

快手社区科学线的电商策略算法部是快手核心推荐算法团队之一，负责快手整个电商包括to B和to C两大块业务的算法优化工作，包括电商直播间、电商短视频、买家首页、货架猜你喜欢等推荐业务场景，覆盖快手主站精选页，极速版发现页，以及关注页等核心用户场景。

我们致力于用技术优化提升电商业务的推荐效果，为快手老铁们打造极致的电商购物体验。团队技术氛围浓厚，研究兴趣广泛，在RecSyS，CIKM，KDD等顶级会议上有多篇论文发表，在大规模深度学习，在线学习，迁移学习，对比学习，强化学习等领域都有所涉及。

* 团队优势

  团队一直坚持学术与业务并向发展的方式，目前在CVPR、WWW、AAAI、EMNLP、SIGIR等会议发表论文多篇 (其中一篇Shared Task Best Paper, 一篇Outstanding Paper)，并在国内知名赛事与榜单荣获过多项Top2成绩；内部提供充分的交流讨论，现有正式员工与实习同学均来自国内/全球顶尖学校；在这里你会有专业的Mentor实时指导技术创新与业务落地。我们团队的 OneSug、OneSearch、OneSearchV2等相关工作受到业界广泛关注。

**六、热招岗位**

* ### 职位名称

### 1、电商直播推荐算法工程师

### 2、电商短视频推荐算法专家

### 3、电商推荐算法工程师-【B端算法】

### 4、电商推荐算法-【流量策略方向】

### 5、电商增长&激励算法工程师/专家

### 6、电商资深推荐算法工程师

### 7、电商搜索算法工程师

### 8、推荐算法实习生-【电商】

* ### 岗位职责

1、参与亿级用户规模的电商搜索/推荐优化，提升电商搜索/推荐场景的GMV、购买用户数、点击率、转化率等核心指标，提升用户电商搜索购物体验，促进生态良性发展；

2、参与机器学习与深度学习算法的核心研发工作，对搜索/推荐全链路进行建模优化，包括但不限于召回、相关性、粗排、精排、机制等，深度进行序列建模、迁移学习、强化学习、对比学习、多模态大模型等的算法和系统研发；

3、针对海量用户行为数据，提供基于分布式计算的算法解决方案，大幅提升算法计算规模和性能；

4、参与搜索推荐机制的顶层设计，结合业务战略，优化电商流量结构和GMV结构，促进电商生态的健康发展。

* ### 任职要求

1、硕士及以上学历，计算机、数学或统计学相关专业，出色的分析问题、解决问题的能力，有强烈的技术热情，有皮实乐观、不畏挫折的心态；

2、熟悉Linux环境、C++和Python语言，良好的逻辑思维能力，优秀的编码能力，扎实的数据结构和算法功底；

3、具有机器学习、数据挖掘、搜索系统、推荐系统或者自然语言理解等相关领域知识；有工业界相关业务与技术方向的实践经验者，或在ACM或数据挖掘/机器学习类竞赛中取得优异名次者优先；

4、具备良好的文献阅读能力和快速学习能力，优秀的分析和解决问题的能力，良好的沟通协作能力；

5、在SIGIR、SIGKDD、ICML、NIPS、WWW、AAAI KM、ACL、RECSYS、CVPR、ICCV、ECCV、ICLR等顶级计算机学术会议或期刊上发表过论文者优先。

* ### 投递方式

扫描下方二维码投递，或投递简历至邮箱：qiuyuyang05@kuaishou.com

![](https://mmbiz.qpic.cn/mmbiz_png/1gVUsotpT1UjZcOjTGnjmwHH4CpgFM6VlI9NSBGm514wM5lMicmibIq6prQia73L7XQJVI1LCorD9s2VMWjmr0AwJlHHBiaicCtC9iarqk4NYed4c/640?wx_fmt=png&from=appmsg)

【相关阅读】

[![](https://mmbiz.qpic.cn/mmbiz_png/1gVUsotpT1Wm7wHYP4DibjmqCs8BVNgcGnxBibq7ribL2H0WcP9M6WLHfqNxdQHbVCLk6TRwiaJhaLhBEmQMnBVoPF9J1VZFiamKP9mbUqgOqd3c/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=Mzg2NzU4MDM0MQ==&mid=2247499952&idx=1&sn=bae3a26ec690cb4c593f0f58a8889311&scene=21#wechat_redirect)

点击【阅读原文】，加入我们！

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/ZxDY5TMPs0GnTFDtpq8oAf91ZQDzvLt6LCp56JQCbFT2cT8uZquFdeJOKbmM4fucIPqtAPvMT0X4DpfpuZibic3Q/0?wx_fmt=...