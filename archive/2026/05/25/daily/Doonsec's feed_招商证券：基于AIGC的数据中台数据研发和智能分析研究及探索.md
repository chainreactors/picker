---
title: 招商证券：基于AIGC的数据中台数据研发和智能分析研究及探索
url: https://mp.weixin.qq.com/s/m0khPm8QmAEFPGkm0FM7pw
source: Doonsec's feed
date: 2026-05-25
fetch_date: 2026-05-26T06:01:42.986653
---

# 招商证券：基于AIGC的数据中台数据研发和智能分析研究及探索

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/QYjQMklF5V0oicMW5jjHuoO8YUK6WeKDSNIPLtWialddbibMPEN5Fiag9NPMpp3pZtYMWLqM75lZiaTOT5jhyDdiaErw/0?wx_fmt=jpeg)

# 招商证券：基于AIGC的数据中台数据研发和智能分析研究及探索

点击关注→
点击关注→

智探AI应用

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

本课题通过引入AIGC技术，以数智融合的方式对数据中台的数据研发过程进行智能化变革，并探索实现以自然语言问答驱动的交互式智能BI数据分析，助力证券业金融机构在数据要素流通的大背景下，更好地挖掘数据要素价值。从而解决长期困扰整个行业的数据分析技术门槛较高、数据分析师人才储备不足和数据资产研发效率瓶颈等痛点。相关研究成果能为证券行业树立数据驱动、智能决策的创新标杆，有效促进证券业金融机构的数字化转型升级。

# 一、课题背景及意义

1.1 课题背景

随着国家对于发展新质生产力战略的推进，“数据要素×”和“AI+”等指引相继出台。招商证券也提出了数字化转型和打造AI券商的战略规划。而在战略规划实际执行过程中，却遇到了行业共性的痛点：数据工程师的开发效率和数据分析师的用数效率受制于人才储备，难以持续提升。

面对这一挑战，本课题尝试以“DATA + AI = 数智融合”的方式寻找最优解，通过引入AIGC技术，打造可复用的数智融合基础能力，并将其应用于数据资产研发和数据分析场景中，以实现开发效率和用数效率的双提升，同时通过知识库积累促进AIGC效果的准确性。

1.2 课题意义

（1）数据资产研发过程从自动化时代迈入智能化时代

支撑数据资产研发的DataOps体系历经标准化和自动化时代后，对于开发效率的提升已接近瓶颈，而智能化则是数据资产研发再次实现大幅提效的关键所在。

（2）数据分析智能化与人数交互方式变革

在传统BI数据分析模式中，人通过专业技术能力查询和分析数据；而在自然语言驱动的对话式数据分析模式中，智能体根据人的意图查询和分析数据，从而大幅降低了数据分析的技术门槛，加速数据到决策的转化过程。

（3）树立证券行业数智融合双向赋能的创新标杆

沉淀可复用的数智融合基础能力，并应用于数据开发、数据分析等场景，在实现提效的同时，又通过数据和洞察的积累促进数智基础能力提升，形成良性循环的飞轮加速效应。

# 二、课题目标及内容

2.1 课题目标

（1）数智融合基础能力

在已有的高质量数据集、元数据知识库、自然语言描述与结果对良例的基础上，通过AIGC技术，实现自然语言生成数据查询语句能力，并建立可持续运营的效果提升机制。

（2）交互式智能BI

探索通过自然语言问答驱动的交互式智能BI数据分析，提升数据分析的易用性。

（3）数据资产研发效能提升

将自然语言生成数据查询语句能力应用于数据资产研发过程，促进数据开发效率大幅提升。

（4）数据要素价值挖掘

在证券业金融机构的具体业务场景中实施智能化数据开发与数据分析，以实现在数据要素流通的背景下，更好地挖掘数据价值。

2.2 课题内容

（1）基于证券行业数据模型的数据中台Data Copilot能力平台

本课题以招商证券的云原生数据中台和天启大模型平台为基础，结合了元数据知识库与良例问答对这两种NL2SQL实现思路，落地了一套全自主研发的自然语言生成数据查询语句能力。

经查阅文献资料和了解主流开源、商业NL2SQL组件特性，基于元数据知识库的技术路线对于存量数据资产的元数据质量有很高的要求，在数据表、字段命名高度准确的情况下，还需辅以一定数量的特征标签，才能确保模型的高准确率；而基于良例问答对的技术路线则要求持续输入并维护问答对，对于陌生问题的泛化学习能力存在显著短板。总结来看，前者需要大量的初始人工投入，而后者需要持续稳定的人工投入。本课题将两种思路有机结合，优先使用良例问答对匹配机制，再通过元数据知识库作为补充，形成以下处理流程。

![图片](https://mmbiz.qpic.cn/mmbiz_png/T3GKbZ1T6h2XslQOhTGicRf4qp9eZSzJpprT2icKRiaXFGLibaLUyXDIKdLw78G2WMrMKy4dH0vkOje83tEMAZj3XQ/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=0)图1 处理流程示意图

招商证券Data Copilot的实现思路既利用了数据中台已有的证券业数据模型和高质量数据集对应的元数据知识库，又从线上数据加工作业代码和即席数据查询脚本中提取良例问答对，实现了高效冷启动。同时，配合人工改写与专家审核机制，能持续更新和扩充良例问答对，达到模型效果稳步提升的目的。

（2）对话式智能BI分析平台

以自然语言生成数据查询语句能力为基础，配合自然语言生成数据可视化展现，即可实现对话式智能BI分析，即ChatBI。相对于传统BI模式，对话式智能BI彻底改变了人数交互模式，使数据分析的技术门槛大幅降低，也给受限于数据分析师人才不足而无法有效发挥数据要素价值的金融机构带来了希望。

![图片](https://mmbiz.qpic.cn/mmbiz_png/T3GKbZ1T6h2XslQOhTGicRf4qp9eZSzJpdGQ4CYfDDzCLgvVFcMGhtZbjwRicK5BkaNXFu04VksKQMXGVF2MwXiaA/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=1)

![图片](https://mmbiz.qpic.cn/mmbiz_png/T3GKbZ1T6h2XslQOhTGicRf4qp9eZSzJpcopMc94MzLRjxef8p1XxTl1NicDOOCB2eM3Rq3QCoAFbiaO6h5ZL6dlg/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=2)

招商证券基于公司天启大模型平台基础能力，构建BI智能问答提示词工程与向量库；依托招证北斗BI平台底座，搭建了对话式智能分析平台，并在试点业务场景中实现了PC端和移动端的智能问数功能。

![图片](https://mmbiz.qpic.cn/mmbiz_png/T3GKbZ1T6h2XslQOhTGicRf4qp9eZSzJpJuMdaUkI7umAThwSLrBOKNmAE4sWWEMXlXDapcGOQhgwhhbpzAEnicg/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=3)图3 对话式智能BI分析平台

 （3）数据中台一站式开发套件集成智能数据开发能力

招商证券自主研发了数据中台开发套件“招证数坊”。实现数据中台数据加工全链路从数据采集、表设计、数据加工作业、数据质量校验作业、数据分发以及各类数据作业调度和运维监控配置的自动化、工具化开发。并将Data Copilot能力集成到数据加工作业开发场景中，实现数据开发提效。

另一方面，使用招证数坊完成开发并遵循DataOps流程自动化部署后，相关元数据信息自动更新元数据知识库，并通过作业中的语句注释和实际语句代码的对应关系积累良例问答对，使Data Copilot能力所依赖的语料信息可以持续、高效完成迭代更新，形成良性循环的正反馈，助力生成语句准确性的持续提升。

![图片](https://mmbiz.qpic.cn/mmbiz_png/T3GKbZ1T6h2XslQOhTGicRf4qp9eZSzJpLaCyMnVGHS244w4YcibqpibjOUxWaUr39p0IRB6ZMyYbAsUvFfa50K0w/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=4)图4 招证数坊

# 三、课题成果与创新

3.1 课题成果

（1）数据中台Data Copilot能力平台

该平台提供自然语言生成数据查询语句能力，上线以来已开放给数据中台所有数据开发人员使用，月活用户约200人，截至2024年末累计生成SQL语句10900+次。在试点开发场景中的采纳率约为63%。与主流开源框架vanna对比，Data Copilot在小样本提示（few-shot prompting）下准确率更高。因其配备了可持续运营的元数据知识库更新和良例问答对积累机制，在泛化能力方面也有优异表现。

![图片](https://mmbiz.qpic.cn/mmbiz_png/T3GKbZ1T6h2XslQOhTGicRf4qp9eZSzJpttia5Xd0omI3AcOWe0ZibqoBQ1mOLhDKp73NDGy4Uptj2HKCCgaBAWsA/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=5)图5 SQL语句生成准确率对比

（2）招证北斗智能问数场景试点

招证北斗作为招商证券的公司级BI门户，集成对话式智能分析能力后，在财富管理业务领域的经营分析、绩效考核两个业务场景中率先进行了应用试点。通过PC端和移动端的智能问数功能，截至2024年末，累计赋能79个营业部的89名客户服务管理人员，提供智能问答服务6247次，准确率达90%以上。

![图片](https://mmbiz.qpic.cn/mmbiz_png/T3GKbZ1T6h2XslQOhTGicRf4qp9eZSzJpeEY88B1ozZp5R3Dd6ic21y1uNZCYpjDH0yj93IARvibrlGKyox9sbaXA/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=6)

![图片](https://mmbiz.qpic.cn/mmbiz_png/T3GKbZ1T6h2XslQOhTGicRf4qp9eZSzJpEbuo1NrYeOhdW0Eu61dF2NicS1On3WFJqZXYHqehKB6qzYGxtFx9u8A/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=7)图6 招证北斗智能BI平台

（3）招证数坊智能数据开发提效

招证数坊集成智能数据开发功能以来，截至2024年末已服务于数据中台9个数据集市迁移上云项目，整体研发效率提升约30%。并且大幅提升了研发交付的规范性和口径一致性，减少因数据质量问题造成的重复开发工作，实现了质效双升。此外，通过积累600+良例问答对，实现智能数据开发从试点项目逐渐推广到其它项目时，生成准确率保持稳定。

![图片](https://mmbiz.qpic.cn/mmbiz_png/T3GKbZ1T6h2XslQOhTGicRf4qp9eZSzJpicxasU4QMr3cLa0icCWPf7Jw8iazPicibUuYgicYzD2cTkqsd8WMNXp0K0uQ/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=8)图7 招证数坊智能数据开发提效

3.2 创新点

（1）在Data Copilot能力平台实现NL2SQL过程中采用了元数据知识库与良例问答对相结合的思路，并搭配可持续运营的元数据知识库自动更新机制和良例问答对积累机制。

（2）将Data Copilot基础能力应用于对话式智能BI实际业务场景，转变数据分析过程中的人数交互模式，大幅降低数据分析的技术门槛，释放数据要素价值。

（3）将Data Copilot基础能力应用于数据中台数据开发场景，与公司级DataOps流程相结合，在促进开发提效的同时，实现自动化更新元数据知识库并积累良例问答对，形成AIGC效果稳步提升的良性循环。

转自：证券期货业金融科技中心

课题研究机构：招商证券

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/QYjQMklF5V2IQLEJ7RFWIfFseSEhs72C7xTlY5mHpqTpnRx2t6OW5ibdgkVAVkrKt2vDr3bTLR484LFPg77apbA/0?wx_fmt=png)

智探AI应用

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/QYjQMklF5V2IQLEJ7RFWIfFseSEhs72C7xTlY5mHpqTpnRx2t6OW5ibdgkVAVkrKt2vDr3bTLR484LFPg77apbA/0?wx_fmt=png)

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