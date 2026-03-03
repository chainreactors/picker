---
title: 电子科技大学|智能模型研究室在人工智能顶级会议WWW26发表2篇论文
url: https://mp.weixin.qq.com/s/qtC2ud6uRB9fhod3Fw0HSA
source: Doonsec's feed
date: 2026-03-02
fetch_date: 2026-03-03T04:07:52.176694
---

# 电子科技大学|智能模型研究室在人工智能顶级会议WWW26发表2篇论文

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/FNlvhjUaDTN4HhyCKtEKuQdEvAc38HzibZ1ibBIDib8W2SYiceiarHpMWxbd5VOBCwss3tMEgBt5LHfichy2RibVPiaEaEmhAk5t1o08CnVXtKnxo1U/0?wx_fmt=jpeg)

# 电子科技大学|智能模型研究室在人工智能顶级会议WWW26发表2篇论文

信息网络安全杂志

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/sz_mmbiz_png/hjvWmePM2bpTk3qBXoibvUObMSwFWk4BIicodXZ4FbSpDo3YUeVh59GYut29iaFjrd6d4lSC5icKmC6JRlQ6Jl7mYQ/640?wx_fmt=png&from=appmsg)

2026年1月，国际万维网大会 The Web Conference (WWW 2026) 公布录用结果，本届大会收到了3370份有效投稿，其中676篇(20.1%)被会议接受。我院智能模型研究室2篇关于大语言模型在复杂图理解推理与安全风险的论文被会议接收。

**01**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/hjvWmePM2bpTk3qBXoibvUObMSwFWk4BI9uCicctbvuvCacnpcDDibNownvj72AbZ3RuqiamnRlmPVrD6ichRqxRZUw/640?wx_fmt=png&from=appmsg)

第一篇论文的录用信息为：**GraphCogent: Mitigating LLMs’ Working Memory Constraints via Multi-Agent Collaboration in Complex Graph Understanding.**

研究院2024级博士研究生王荣正为论文第一作者，导师为秦科教授，协助指导老师为梁爽副研究员，电子科技大学为第一单位。

以下是论文的主要内容：

图结构数据广泛存在于Web、交通、社交与引文网络等真实场景中，但现有大语言模型在处理“规模更大、查询更复杂”的真实图推理任务时，常因工作记忆（Working Memory）受限而导致推理路径错误或执行不稳定。

针对上述挑战，论文提出GraphCogent协作式智能体框架，借鉴人类工作记忆模型，将复杂图推理拆解为“感知（Sense）—缓冲（Buffer）—执行（Execute）”三类专业智能体：由Sensory Module通过子图采样将多样的图文本表示规范化；由Buffer Module融合并索引跨格式图数据（如NumPy、PyG、NetworkX等）；由Execution Module将工具调用与工具创建结合，以更高效、更可靠的方式完成图算法推理与任务执行。

为系统评测真实图推理能力，论文构建Graph4real基准，覆盖Web、交通、社交、引文四类真实图数据，包含21类图推理任务，并按结构查询、算法推理与预测建模三大类型组织；相较既有基线模型，其图规模可扩展至约10倍，可应对真实应用复杂性带来的挑战。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/hjvWmePM2bpTk3qBXoibvUObMSwFWk4BIV9s0pMhSSWBkP9B4F6K77uJicdiaf7ibicfcJprq1tGu4D5DSoGwwYJiaSA/640?wx_fmt=png&from=appmsg)

图1：GraphCogent整体框架示意图（Sensory–Buffer–Execution）

实验结果表明：基于Llama3.1-8B的GraphCogent在Graph4real上取得显著提升，相比超大规模模型DeepSeek-R1（671B）实现约50%的性能提升；相较于代表性的多智能体基线方法，准确率提升约20%，并在工具集内任务与工具集外任务上分别降低约80%与30%的Token消耗，体现了在效果与成本上的双重优势。

**02**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/hjvWmePM2bpTk3qBXoibvUObMSwFWk4BI9uCicctbvuvCacnpcDDibNownvj72AbZ3RuqiamnRlmPVrD6ichRqxRZUw/640?wx_fmt=png&from=appmsg)

第二篇论文的录用信息为：**KEPo: Knowledge Evolution Poison on Graph-based Retrieval-Augmented Generation**

学校2023级博士研究生陈麒至为论文第一作者，导师为秦科教授，协助指导老师为梁爽副研究员，电子科技大学为第一单位。

以下是论文的主要内容：

检索增强生成（Retrieval-Augmented Generation, RAG）通过检索外部知识库为大模型生成提供证据支撑，但也面临因“外部知识源可被注入恶意内容”带来的新型攻击。近年来，GraphRAG进一步将知识组织为实体-关系图谱并按社区/子图进行检索与汇总，以更好支撑复杂知识关联与多跳推理。然而，现有面向传统RAG的投毒方法多基于文本句段的相关性操纵，在GraphRAG的知识抽取、图构建与社区汇总机制下往往难以有效提升恶意内容的检索排名，从而难以持续误导生成模型输出目标答案。

针对上述挑战，论文提出知识演化投毒（Knowledge Evolution Poison, KEPo）方法：在单目标场景下，KEPo围绕目标问答生成包含投毒知识的“毒性事件”，并基于原始事实构造带时间顺序的知识演化路径，通过伪造可信背景与按时间线组织的攻击语料，将投毒知识自然“融合”进既有图社区；在多目标场景下，KEPo进一步跨多个投毒子社区抽取关键节点并建立虚构关系，实现多语料互相强化与投毒范围扩张，从而系统性提升投毒知识的检索排名与攻击效果。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/hjvWmePM2bpTk3qBXoibvUObMSwFWk4BISjoReSRFe7M8evVB3ppbDyHzxiazJHtxMgmibSWjRYKIcpqT742J3RPw/640?wx_fmt=png&from=appmsg)

图2：KEPo攻击流程示意图（论文Figure 3）

实验方面，论文在GraphRAG-Bench（Graph-Story与Graph-Medical）以及多跳问答数据集MuSiQue上开展系统评测，采用ASR（Attack Success Rate）与CASR（Conditional ASR）衡量攻击成功率，并在GraphRAG、LightRAG（全局/局部检索）与HippoRAG 2等代表性GraphRAG框架以及naive RAG上，与PoisonedRAG、CorruptRAG、GRAG-Poison等基线方法进行对比。结果表明，KEPo在单目标与多目标场景下均取得更高的攻击成功率，并在检索框架退化为naive RAG时仍保持显著优势。进一步分析显示：投毒文本长度增加可快速提升ASR，但在约100词后收益逐渐趋于饱和；多目标场景下，跨语料连接数量增加可提升ASR，但在连接过多时可能因语义相关性下降而出现边际收益降低。

此外，论文评估了查询改写、指令忽略与提示检测等常见防御策略，发现其对KEPo攻击的抑制效果有限，凸显了GraphRAG安全防护仍需面向“知识演化伪造”这一新型攻击范式开展更有针对性的检测与鲁棒检索研究。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/hjvWmePM2bpTk3qBXoibvUObMSwFWk4BIicodXZ4FbSpDo3YUeVh59GYut29iaFjrd6d4lSC5icKmC6JRlQ6Jl7mYQ/640?wx_fmt=png&from=appmsg)

**相关链接：**

国际万维网大会（The Web Conference，简称 WWW，现亦称 ACM Web Conference）是Web领域最具影响力的国际学术会议之一，由国际万维网大会委员会（International World Wide Web Conference Committee，IW3C2）组织举办，长期推动Web相关研究与发展。 该会议系列始于1994年，首届WWW1在瑞士日内瓦CERN举办并由Robert Cailliau组织；IW3C2亦于1994年由Joseph Hardin与Robert Cailliau发起成立，持续负责该会议系列的组织与治理。在学术评价体系中，WWW被中国计算机学会（CCF）推荐为A类国际学术会议（交叉/综合/新兴领域）。

来源：电子科技大学

往期精彩回顾

[从竞赛“练兵场”到人才“孵化器”: 湖南大学、复旦大学、四川大学、西安邮电大学引领塑造网络安全新生力](https://mp.weixin.qq.com/s?__biz=Mzg3NjU0Nzg1Nw==&mid=2247514301&idx=1&sn=ebd506c4481ec750d918db24d60650be&scene=21#wechat_redirect)

[守护语音安全: 华中科技大学CPSS团队如何打造Anti-Deepfake系统斩获创意作品赛冠军？](https://mp.weixin.qq.com/s?__biz=Mzg3NjU0Nzg1Nw==&mid=2247511846&idx=1&sn=a6d9787957489c5fc1b89d936f922aa8&scene=21#wechat_redirect)

![图片](https://mmbiz.qpic.cn/mmbiz_png/icL7Q0hLWsN8yDJWicSECDq8dgel7DctAMAnNheJf2kkfQOiaFMdZaWNIDt9IxOkEhI5TJar4wnyAiba9twTOxeKZg/640?wx_fmt=png)

**信息网络安全**

《信息网络安全》创刊于2001年，是由公安部主管，公安部第三研究所、中国计算机学会主办，面向国内外公开发行的国内首批信息安全类期刊之一，于2015年成为中国科技核心期刊，2017年成为中国科学引文数据库来源期刊，2018年成为中文核心期刊，2022年入选CCF计算领域高质量科技期刊分级目录。

![](https://mmbiz.qpic.cn/mmbiz_jpg/icL7Q0hLWsN9e1fkuM1ibgD3PcZiaqJrZia7KQWDwichD8lvo4RqfPcNkuyqje45IOXD0HocBDntaDdK4tibWoTIs5Ww/640?wx_fmt=jpeg)

中文核心期刊

中国科技核心期刊

中国科学引文数据库来源期刊

CCF计算领域高质量科技期刊

![图片](https://mmbiz.qpic.cn/mmbiz_png/v4vz52CcB12BRNZGqdRDIBsUQ6WickDoUNkuVicKXooNbRSzdGDGuJtxJodlbpr1B07yAReAz5V5jj47Yaq7ujRw/640?wx_fmt=png)

我们在不断努力和完善中，期待您的关注和支持！

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/icL7Q0hLWsNibBlGIDAuhv04Ap5j7X2I4Se7j2nvibDibXXmaA8WJqgXZ2Lh8sShG6jas26z3WlRcANNqZnr3nMTnQ/0?wx_fmt=png)

信息网络安全杂志

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/icL7Q0hLWsNibBlGIDAuhv04Ap5j7X2I4Se7j2nvibDibXXmaA8WJqgXZ2Lh8sShG6jas26z3WlRcANNqZnr3nMTnQ/0?wx_fmt=png)

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