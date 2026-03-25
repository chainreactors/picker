---
title: WSDM 2026｜快手大促CVR预测技术斩获最佳长文提名奖！
url: https://mp.weixin.qq.com/s/nO59NE0gKSxVmJ5-L0Et7g
source: Doonsec's feed
date: 2026-03-24
fetch_date: 2026-03-25T04:14:56.595180
---

# WSDM 2026｜快手大促CVR预测技术斩获最佳长文提名奖！

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1gVUsotpT1Wr71251pgoC8AddV1mkQdlW6jiaHETpSLJiaG1P3k1SbKA8B6soWLpYnwpia0wLEeLDopLTVL3bsfCnSaFkba8KlAhqgXgZUb5R4/0?wx_fmt=jpeg)

# WSDM 2026｜快手大促CVR预测技术斩获最佳长文提名奖！

原创

快手技术
快手技术

快手技术

![]()

在小说阅读器中沉浸阅读

![图片](https://mmbiz.qpic.cn/sz_mmbiz_gif/ZxDY5TMPs0EqL7dlyXD8OFyXn6yNGvQ8uEibL6TkOHqFvaK0bR9GEhZicTHuDtaTficMGS88ecXKIVPnFJCTMz7aQ/640?wx_fmt=gif&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=0)

近日，国际数据挖掘顶级学术会议WSDM 2026（ACM International Conference on Web Search and Data Mining）在美国爱达荷州博伊西举行。由快手商业化算法团队联合复旦大学、天津大学共同完成的研究论文《TemporalExpertNet: Cross-Temporal Knowledge Reuse for Promotion-Aware CVR Prediction》，荣获大会Best Full Research Paper Runner-Up（最佳长文提名奖）。

该工作聚焦大促场景下转化率预估这一核心问题，提出了面向工业级广告系统的跨时序知识复用框架，并已在快手大规模短视频广告平台完成线上验证与全量应用，在学术创新与业务落地两个层面均展现出重要价值。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1gVUsotpT1UvJUaKFqiccoGvIlDrI4MBibYtJBuqChFLfY2qcNpP0vMZFo0RGrtaAicAo2nK2htkbrKewIvJ30Sbony8Rdl99kfvUVnTHr2PJ4/640?wx_fmt=png&from=appmsg)

* 论文标题：TemporalExpertNet: Cross-Temporal Knowledge Reuse for Promotion-Aware CVR Prediction
* 论文链接：https://dl.acm.org/doi/10.1145/3773966.3777956

本届WSDM大会评审竞争激烈，主会议共收到全球投稿613篇，最终录用100篇，录用率仅16.3%。在此基础上，大会仅评选出1篇Best Full Research Paper和1篇Best Full Research Paper Runner-Up。作为国际公认的Web搜索与数据挖掘领域顶级学术会议之一，WSDM长期聚焦信息检索、数据挖掘、推荐系统、在线广告等前沿方向，具有广泛国际影响力。

**1、研究背景：**

**大促流量激增下，CVR预估为何更难？**

在短视频广告与推荐场景中，CVR（Conversion Rate，转化率）预测是商业化系统中的关键环节，直接影响广告投放效率、用户体验与平台收益。但在618、双11、黑五等大型促销节点，系统往往面临一个极具挑战的问题——数据分布在短时间内发生剧烈且不均匀的变化，这种变化并非所有流量一起变化，而是具有明显的异质性，具体如下：

* 广告主侧：不同广告主对大促的响应程度并不一致。部分广告主会显著提升预算，并动态调整出价与投放策略，而部分广告主的整体投放节奏变化相对有限。
* 用户侧：用户对促销活动的敏感度同样存在明显差异。部分用户会因价格刺激、活动氛围等因素表现出更强的转化意愿，而另一部分用户的行为模式则与日常阶段接近。

数据分布并非整体同步变化，而是分群体发生偏移，这一特征使得大促期间的数据分布呈现出更强的非平稳性。也正因如此，基于平稳假设或依赖常规历史分布训练得到的CVR模型，会在大促期间出现明显的预测偏差、校准失真与泛化退化。

从业务视角来看，这一问题更为关键。虽然大促周期在全年中占比有限，但往往对应着极高的流量峰值与收入贡献，因此，如何在这些关键节点提升CVR预测的稳定性与准确性，始终是广告系统中的核心挑战之一。

**2、核心问题：**

**历史大促知识能否服务当前预测？**

既然618、双11等大促具有周期性，那么历史大促中所积累的知识，是否可以直接迁移到当前大促中使用？答案并不简单。

首先，历史大促中沉淀了大量高价值知识，例如：特定用户群体在促销周期中的行为模式、广告主预算变化对转化的影响机制，以及某些促销场景下更容易触发转化的上下文规律。然而，当前流量与历史流量不完全一致。尽管都是大促场景，但不同年份、不同阶段、不同平台环境下，流量结构和行为模式均存在显著差异。如果直接复用历史模型，可能因为分布不匹配而导致知识失效。

因此，值得关注的不是“能不能用历史模型”，而是如何把历史大促中的有效知识，以可控、结构化的方式迁移到当前任务中。

现有研究大多围绕相对稳定场景下的转化预测展开，通常依赖当前数据进行直接拟合，默认训练分布与应用场景基本一致。然而，在大促场景中，用户兴趣、商品供给与转化机制都会随时间发生显著变化，因而存在更强的时序漂移与分布偏移。针对这一问题，已有部分方法开始尝试引入历史促销信息进行适配，但其核心仍主要停留在数据层面的复用，即利用历史大促数据缓解当前场景的数据不足或分布变化，对历史促销过程中沉淀下来的可迁移知识缺乏显式建模。

与这类工作不同，本论文更关注知识层面的复用。其核心是从历史大促中提炼具备泛化能力的促销模式与行为规律，并将其迁移至当前大促任务中。同时，进一步针对跨时序表征不一致、历史知识难以直接复用等关键问题进行建模，使历史知识能够以更高效、可控的方式服务于当前场景。

**3、方法设计：**

TEN如何让历史大促知识服务当前预测？

围绕上述关键问题，本论文提出了面向工业级广告系统的跨时序知识复用框架TemporalExpertNet（TEN）。TEN的目标是让系统具备更强的能力：在当前流量基础上，有选择地调用历史大促知识，并将其转化为对当前预测有价值的信号。其关键思路是让模型具备识别、对齐、调用历史促销知识的能力。整体来看，TEN主要包括四个核心设计。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1gVUsotpT1XOsZx8AFRG7VNv7ooHNztRC2uE9L1YwjBr0yhn7qJp8cMayLfdSHneONT7SL3M4tjlEB7EtkicCh3YRqT8PAz8Lib3ZSGmV0ic98/640?wx_fmt=png&from=appmsg)

**1. 结构解耦：**

**把日常能力和促销能力拆开建模**

当前流量中的日常行为模式与历史大促中沉淀下来的促销知识，在本质上承担着不同作用，不应被混在同一套表示中统一建模，这构成了TEN的出发点。

基于这一认识，TEN将模型拆分为两部分：

* 日常编码器：用于刻画当前最新流量下的基础行为模式，捕捉用户、广告和上下文在日常分布中的表征；
* 促销专家：用于承载历史大促场景中学到的转化模式知识，尤其是那些只在促销期间才更明显出现的行为规律。

这样的结构设计使模型既能保持对当前流量的敏感性，又能有选择地复用历史大促知识，从而避免在每次大促到来时都重新学习。

**2. BridgeNet：**

**让历史大促知识与当前数据接合**

把历史促销专家保留下来，不代表这些知识能直接被当前样本使用。一个关键挑战在于历史促销专家所适配的输入分布，与当前日常流量生成的表示空间不一致。历史模型中的知识虽然有价值，但它形成于过去时点和过去分布之上。如果直接拿来作用于当前流量，很可能因为表征错位而难以发挥效果。

为了解决这个问题，论文设计了BridgeNet。它通过表示对齐机制，将当前日常流量下得到的特征，映射到更适合历史促销专家理解和利用的语义空间中，缓解跨时序表征不匹配带来的知识调用障碍。

由此，TEN超越了对历史知识的简单保留，而能够让历史知识真正服务当前预测。

**3. TEG：**

**精准建模不同样本需求**

大促带来的分布变化不是全局统一的，而是具有明显的样本异质性。

对于一部分样本而言，用户或广告主在活动期间的行为模式变化显著，此时历史促销知识拥有较高参考价值；而对于行为仍与日常阶段接近的另一部分样本而言，如果强行引入促销知识，反而可能带来干扰。

因此，TEN不是让所有样本统一走促销分支，而是进一步提出了TemporalExpertGate（TEG）。TEG会根据样本特征进行动态路由与专家融合，判断当前预测更应依赖日常能力，还是更应激活历史促销专家，从而实现细粒度、自适应的预测调整。

基于此，TEN能够更精细地建模不同样本对促销知识的实际需求。

**4. 两阶段训练：**

**先解决“能不能迁”，再解决“该怎么用”**

除了结构设计之外，TEN的另一个关键点在于其两阶段训练策略。BridgeNet和TEG所承担的目标并不相同：前者关注“如何让当前样本能够对接历史知识”，后者则关注“在样本层面如何合理调度不同知识源”。如果从一开始就将这些目标同时联合优化，训练过程中容易出现信号干扰，影响模型收敛与最终效果。

为此，TEN将训练过程拆分为两个阶段：

第一阶段，重点学习跨时序表示对齐，先解决历史知识能否顺利迁移到当前样本的问题，该阶段选择历史大促数据进行微调；

第二阶段，再进一步学习门控融合机制，让模型在完成基本对齐后，能够针对不同样本自适应决定如何组合日常能力与促销能力，该阶段选择最新数据进行微调。

这种“先对齐、再融合”的训练方式，本质上是将“知识迁移”和“知识调度”拆开优化，既降低了训练难度，也提升了整体稳定性和最终效果。

**4、效果验证：**

**离在线均取得显著收益**

TEG在离线对比基线方法取得显著收益，消融实验证明不同模块设计的有效性。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1gVUsotpT1Vib7Xd1PGrvBF1d8dXpv0kLNeXB8jLOZKdichmibr81bPNicThha4YfnfmtL2n2LXtjWjfaLuE6pIy9M4cibQdeHKZ7XsJmOW5qn8I/640?wx_fmt=png&from=appmsg)

离线实验效果图

在线上实验中，TEN已在快手大规模短视频广告平台完成部署验证。结果显示，在618预热期，相较于生产基线，TEN在如下两个方向实现了提升：

* CVR提升 7.52%
* RPM提升 4.27%

与此同时，模型的工程开销保持在较低水平：

* 模型体积仅增加0.23%
* 推理时延仅增加1.8%

在取得稳定收益后，TEN进一步全量上线至618当日全部流量，带来了显著的业务增益。TEN在几乎不显著增加系统负担的前提下，有效提升了大促场景下的预测质量，体现出较强的工程可落地性和实际业务价值。

**5、结语**

TemporalExpertNet (TEN) 的提出，旨在解决时变环境下的建模挑战。其核心价值在于提出了一种新的迭代思路：从单纯的“模型替换”转向“知识累积”。该方法通过结构化的知识解耦、对齐与调度机制，使系统能够保留历史大促中的有效信息，避免每次面对新场景时都重新学习。TEN不仅提升了商业化系统在关键节点的稳定性与收益，还增强了模型在长时间跨度下的经验复用能力和适应性。

**关于我们**

![](https://mmbiz.qpic.cn/mmbiz_svg/ZqDaDiccbgkjkXh51mrAMoT3ZCACkYnlug8cUETdh9Day9fNPrUxPnf16aImK9XpkTCvMufrR9HiaPqbFKCRMxoMlZmAlwZCog/640?wx_fmt=svg&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=4)

商业化算法部是快手核心算法部门，负责快手国内及海外多场景的变现算法研发，致力于建设领先的广告变现算法，通过算法驱动商业营销增长，不断优化用户和客户体验，引领行业创新型解决方案，推动行业变革。团队成员多来自国内外顶尖高校，以及头部大厂核心团队。团队推荐相关技术获得了24年钱伟长科技进步一等奖。出价上基于RL和生成模型在NeurIPS 2024 广告出价比赛获得双赛道第一名。近年团队技术成果在KDD/WWW/ICLR/NeurIPS/CVPR/ICCV/AAAI等顶会上发表论文100+，其中不乏获得CIKM Best Paper、SIGIR Best Paper提名奖和WSDM Best Paper提名奖。

**热招岗位**

![](https://mmbiz.qpic.cn/mmbiz_svg/ZqDaDiccbgkjkXh51mrAMoT3ZCACkYnlug8cUETdh9Day9fNPrUxPnf16aImK9XpkTCvMufrR9HiaPqbFKCRMxoMlZmAlwZCog/640?wx_fmt=svg&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=4)

* 职位名称

  广告算法实习生 -【商业化算法部】
* 任职要求：

+ 2027届优秀毕业生，计算机、数学、统计学等相关专业本科以上学历，博士、硕士优先；
+ 熟悉Linux，精通C / C++、Java、Python等至少一门编程语言，优秀的编码能力，扎实的数据结构和算法功底；
+ 熟悉机器学习、数据挖掘、计算广告学相关基础知识，对常用算法有使用经验，并能根据实际场景进行优化，熟悉大规模数据挖掘处理、分布式计算；
+ 善于阅读文献，快速学习，具备优秀的分析和解决问题能力，良好的沟通协作能力。

* 加分项：

+ 有互联网广告算法、搜索 / 推荐系统、机器学习、计算机视觉、计算广告学及博弈论相关领域研究，及一线互联网公司实习经验者优先；
+ 在NIPS、ICML、ICLR、IJCAI / AAAI、SIGKDD、CVPR / ICCV、ACL等相关国际顶级会议或期刊上有文章发表者优先；
+ 有Kaggle、KDD Cup等推荐算法、数据挖掘比赛获奖者优先；
+ 有ACM / Topcoder Algorithm或类似算法竞赛经历者优先。

* 投递方式：

  扫描下方二维码投递，或投递简历至邮箱：liyuzhe@kuaishou.com

![](https://mmbiz.qpic.cn/mmbiz_png/1gVUsotpT1Xriaob6gECbQ6VS7YOwjwGDY0rQgWkXvYEM4VicCY9pkJzzJZfqK9CxibA9nGqEwQf9TuibvtOWyxAZxibRmHrXLQXotuzLibXMmf6E/640?wx_fmt=png&from=appmsg)

【相关阅读】

[![](https://mmbiz.qpic.cn/mmbiz_png/1gVUsotpT1XwRp6SRsg3ic8639vlZAbKSEuTFrFhTIcVKyt8An5ULLjvweRic1l2zWVn4lsKjeibeSbZXm8L0bvEWWChrw78yyYewUqGCnLibcQ/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=Mzg2NzU4MDM0MQ==&mid=2247499463&idx=1&sn=02732e8827304631d3802694be059808&scene=21#wechat_redirect)[![](https://mmbiz.qpic.cn/sz_mmbiz_png/1gVUsotpT1Ub9IZLrls7ELGswytGVuDXKNUVkRwnXXj1rsUNcqpic0fWuNIFOV5DKsr0WTfhHgMC2fhnwpkVBRGmnaonPTXjt8GpEFxCWVnw/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=Mzg2NzU4MDM0MQ==&mid=2247498727&idx=1&sn=4396d59680637e3dbe7e2776cded5860&scene=21#wechat_redirect)

点击【阅读原文】，加入我们！

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