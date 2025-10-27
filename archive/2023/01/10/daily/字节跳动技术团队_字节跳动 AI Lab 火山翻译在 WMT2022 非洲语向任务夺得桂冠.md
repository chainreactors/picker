---
title: 字节跳动 AI Lab 火山翻译在 WMT2022 非洲语向任务夺得桂冠
url: https://mp.weixin.qq.com/s?__biz=MzI1MzYzMjE0MQ==&mid=2247501077&idx=1&sn=3974cb7e69129c6b0b3d0a8379832e22&chksm=e9d30ef7dea487e1db64140d4f9e7781c90e6617a78273914335624c7652900b31a8f3447164&scene=58&subscene=0#rd
source: 字节跳动技术团队
date: 2023-01-10
fetch_date: 2025-10-04T03:27:34.100882
---

# 字节跳动 AI Lab 火山翻译在 WMT2022 非洲语向任务夺得桂冠

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/5EcwYhllQOhDBN1L3eTrM5YEFT5WNBnEIvGkPPmvwG6whA09ictrTjDqTzzjdGy7e9XL5TbFdEldib2P4sL3HxdA/0?wx_fmt=jpeg)

# 字节跳动 AI Lab 火山翻译在 WMT2022 非洲语向任务夺得桂冠

原创

钱线 & 王明轩

字节跳动技术团队

**动手点关注**

**![](https://mmbiz.qpic.cn/mmbiz_gif/JaFvPvvA2J063TNzibibGfI89U9UaWNPqYGUFNRVJ1TkA4Bv0Ew946EkhX4dNibLx6ZK9E4ibdtqH01ZGs9a4gvo4w/640?wx_fmt=gif)**

**干货不迷路**

# 1. 非洲语言的现状

非洲是**世界上面积第二大**的大洲，也是**世界上第二个人口大洲**，其大陆上存在 **2146**种语言——约占世界语言总数的三分之一。广袤的面积、繁多的种族，还有宗教传播和殖民统治的影响，使其成为世界上语言最复杂的一个大陆。然而，随着英语、法语等语言在非洲的普及，这些承载着多样文化的两千多种语言正在逐渐无声消亡。

在过去的几年里，低资源语种的机器翻译质量得到了很大提升，这得益于多语言机器翻译的跨语种知识共享、语料挖掘还有大语言模型的应用。然而还是有很多语言，特别是上述的非洲语言，进展并不顺利。去年的多语言机器翻译任务上，以爱尔兰语和威尔士语为代表的印欧语系获得了平均 19.3 BLEU 的大幅提升，而以富拉尼语和伊博语为代表的非洲语种的平均提升只有 3.5 BLEU。究其原因，一是相比于其他语言，非洲语言鲜被重视；二是非洲语言种类繁多，大多数语言使用人数不到百万，其中有些甚至只以口语形式流传，这两者导致缺乏足够的非洲语言语料数据，非洲语种的机器翻译效果也难以提升。

# 2. 字节跳动火山翻译的解决方案

字节跳动的火山翻译团队从几年前就开始深耕多语言机器翻译技术，旨在通过跨语言技术提升小语种的翻译能力，克服非洲语言等小语种语料数据缺乏的问题，并通过扩大单个模型的语种数提升服务稀有语种翻译请求的 GPU 利用率。在近两年的顶级自然语言处理的学术会议 ACL、EMNLP 上火山翻译发表多篇论文，包括嫁接预训练语言模型的使用，通过对齐技术扩充语料数量的方法 mRASP，以及集成对比学习的 mCOLT 方法，利用子网络划分来避免小语种对大语种的干扰技术，以及为每个语种保留部分独有参数从而达到互不干扰，快速训练的 adapter 结构。

火山翻译整体系统的提升来源于越来越大的大模型使用，通过集成预训练、数据增强等其他技术达到单一模型全面提升所有语种翻译质量的目的。团队并没有采用往届 WMT 评测中频繁使用的集成学习、重排序、领域微调等技巧。一方面这些技巧增加了翻译模型的复杂度，提高了不同设备上的部署成本，另一方面增加了额外的计算量，会导致服务延时加剧。比如重排序需要低效的 nBEST 解码，以及额外的模块进行特征抽取排序。而集成学习则通过数据切分，以及不同的模型参数来训练多个模型，增加了训练成本。

过去两年，火山翻译在 170+ 的语种上进行了大量的实验，并和谷歌、DeepL 等 SOTA 的翻译系统比较，以确保翻译质量达到业界先进水平。这次参加 WMT 也是为了验证火山翻译在非洲语种上的能力。

# 3. 技术细节及实验结果

今年的第七届机器翻译 workshop 中的多语言翻译任务聚焦 24 个非洲小语种与英语法语之间共 100 个语向的互译。采用严格的测试流程：参赛方无法获取评测数据，也不能通过提交系统得到评测数据上的成绩。参赛方只能提交最多两个可运行的程序给组织方，由组织方在评测数据上跑出成绩。此外由于 sacreBLEU 的缺陷，这次评测使用 sentencepiece BLEU，而不是 sacreBLEU 作为其排名的参考。其中共有 8 个单位参赛，提交系统 14 个。火山翻译团队自研的系统获得了全场最好成绩：平均 spBLEU 21.9，较第二名的 17.6 高出 4.3 个点 (+24.4%)。在 100 个语向上，获得了 96 个语向的第一。

虽然火山翻译采用开放式系统，可以使用额外数据，其他系统采用受约束系统，只能使用主办方规定的数据，但参考以往的评测成绩，这一区别仍旧不能完全弥补 BLEU 上的差距。

此外，火山翻译系统超越了同是开放系统的 NLLB 模型。NLLB (No Langauge Behind) 是 Meta 公司最近发布的一个拥有 54B 参数的大型多语言翻译模型，其论文声称其在小语种上的平均成绩已经超过谷歌。而在 WMT22 的 100 个语向上，火山翻译的平均 spBLEU 是 23.54，超过 NLLB 0.7 个点。这说明火山翻译已经达到了业界的先进水平。下图显示了在不同语向的分组上火山翻译与 NLLB 的对比。可以看出火山翻译在以非洲语言为目标的语向上高出 NLLB，而在以英语法语为目标的语向上，略逊于 NLLB。

![](https://mmbiz.qpic.cn/mmbiz_png/5EcwYhllQOhDBN1L3eTrM5YEFT5WNBnECoiahU2SkqJVLhZZz0zF940wJ8eAuichGEUOEhnPIiaThicLnaqBQTibkOg/640?wx_fmt=png)

在训练策略和模型选择上和 NLLB 以及历届的评测系统不同，火山翻译追求简洁的模型和通用的训练流程，放弃了更加复杂的优化技巧，比如集成学习，重排序等等，也没有使用 NLLB 中的课程学习 (curriculum learning) , 专家模型 (Mix of Experts) ，tagged back translation 等精细的调优手段。这么做一方面简化了模型的从训练到上线的流程，不需要额外的开发来支持特殊的模型结构。另一方面也使得实验结果易于复现，模型的通用性更强。火山翻译系统只经过评测规定的短短四个月的调试，相信再经过一段时间的精调，扩大模型容量，火山翻译将有更好的表现。

火山翻译取得如此的成绩离不开长时间的基础积累，包括全网数据搜集系统、硬件加速库 LightSeq、以及支持大规模数据读写的训练框架 ParaGen。原因可以归为三个字：多、大、快。即数据多，模型大，速度快。我们的系统采集了超过开源数据 30 倍的训练数据，从根本上解决小语种的数据稀缺问题。我们的模型采用 128 层 Transformer，2.1B 参数，是参赛模型中最深的。最后采用 LightSeq 进行大规模 back translation，即使是 128 层这样的大模型，也达到了每秒近 12 句的速度，保证了一个月内翻译完 1.4B 的单语语料句子。

数据采集方面，火山翻译对 commoncrawl 数据进行平行句对的挖掘。分为单页面和双页面两部分。通过分句、语种检测，判断页面内是否存在平行的句对，或者通过 url 特征判断两个页面是否平行。用最先进的 Laser3 句子编码工具将句子转成向量，并通过 FAISS 的最近邻检索找出配对的句对。总计挖掘出 150M 句对，是官方数据量的 3 倍。此外我们人工对特定的网站进行了单语、双语数据的挖掘，比如圣经、JW 网站、VOA news 等等。

模型选择方面，火山翻译平衡了训练速度和模型容量。太大的模型会导致一张显卡装不下，如果需要跨卡通信，则会导致训练速度下降。而过小的模型则容量不够，导致欠拟合。平衡这两点，我们采用了 64 层编码，64 层解码，共 128 层的 Transformer 模型。

速度方面，火山翻译使用 Lightseq 对训练加速，训练速度超过 pytorch + apex 的 40%。而在 back translation 时，也用 lightseq 解码，速度大概是 torch 实现的 25 倍。通过 50 张 V100 的卡 1 个月的翻译，完成了 1.4B 单语句子的翻译，这些数据在实验中提升系统 3.2 个 BLEU（16.3%），成为火山翻译立足顶尖水平的关键。

综上，火山翻译集成了多项业界先进技术于一体，开辟出了一条通过规模化大幅提升翻译系统的思路。在未来的实践中，将结合精细化的模型微调，进一步提高翻译质量，解决推理延时、显存占用等部署问题，更好地服务于现实应用中。

![](https://mmbiz.qpic.cn/mmbiz_png/7QRTvkK2qC6RyGcCclHibMw08rYZOOtkfZud4IA4b3ORre5LScE0yBXTg19E6cQ4XbOP7iaWfVREuT3Dgxc4p3hw/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_gif/7QRTvkK2qC7IHABFmuMlWQkSSzOMicicfBLfsdIjkOnDvssu6Znx4TTPsH8yZZNZ17hSbD95ww43fs5OFEppRTWg/640?wx_fmt=gif)

[● SpriteJS：图形库造轮子的那些事儿](http://mp.weixin.qq.com/s?__biz=MzI1MzYzMjE0MQ==&mid=2247501068&idx=1&sn=4839629ea06fa805b24196105f3e14c7&chksm=e9d30eeedea487f8fbae2564d764b525fef669df5613e46294d6a6a28e1edd7a341dec728c61&scene=21#wechat_redirect)

[● 从100w核到450w核：字节跳动超大规模云原生离线训练实践](http://mp.weixin.qq.com/s?__biz=MzI1MzYzMjE0MQ==&mid=2247500979&idx=1&sn=880f9dd458a96709269756e1f64a4a40&chksm=e9d30f51dea48647408de90732a9abd1cc7a173e568b36d9b9a24b16d0ccde4c91112f96b504&scene=21#wechat_redirect)

[●](https://mp.weixin.qq.com/s?__biz=MzI1MzYzMjE0MQ==&mid=2247499750&idx=1&sn=c7fc5b6c7b0bcbec73a6f318014d2a58&chksm=e9d33404dea4bd128356318818a80f416a31bc9cf09aa74c6dc99e074a96a9b7f8c0b9a4f256&token=785874804&lang=zh_CN&scene=21#wechat_redirect)[【活动推荐】Flutter 深度用户，字节跳动如何落地实践？](http://mp.weixin.qq.com/s?__biz=MzI1MzYzMjE0MQ==&mid=2247500979&idx=2&sn=0f9e0cbac39fd5942e4d9a5f0084cff4&chksm=e9d30f51dea48647496a4f79e7a285e5c66104beafc9e71d3fc68ae2d1ae6718e540cc47ee7d&scene=21#wechat_redirect)

[●](https://mp.weixin.qq.com/s?__biz=MzI1MzYzMjE0MQ==&mid=2247499750&idx=1&sn=c7fc5b6c7b0bcbec73a6f318014d2a58&chksm=e9d33404dea4bd128356318818a80f416a31bc9cf09aa74c6dc99e074a96a9b7f8c0b9a4f256&token=785874804&lang=zh_CN&scene=21#wechat_redirect)[火山引擎 DataLeap 的 Data Catalog 系统公有云实践](http://mp.weixin.qq.com/s?__biz=MzI1MzYzMjE0MQ==&mid=2247500746&idx=1&sn=49798c1d670fb596acead96995d3f122&chksm=e9d30828dea4813ec70e9756bcf9c76b1e9f41c015f4469a0d93350289ad4cdd74d10eaa2cfe&scene=21#wechat_redirect)

预览时标签不可点

修改于

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/5EcwYhllQOhkoWTP1gVm0Lqs480XOARyoSYjPEsRVCSF35cbWIp6cliaYic8KUfNfiaSjVnruzTQUTCA0lmv9vUmw/0?wx_fmt=png)

字节跳动技术团队

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/5EcwYhllQOhkoWTP1gVm0Lqs480XOARyoSYjPEsRVCSF35cbWIp6cliaYic8KUfNfiaSjVnruzTQUTCA0lmv9vUmw/0?wx_fmt=png)

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