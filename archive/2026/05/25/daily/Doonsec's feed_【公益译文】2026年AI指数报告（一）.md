---
title: 【公益译文】2026年AI指数报告（一）
url: https://mp.weixin.qq.com/s/PYEJOIVmdBO5gbuQn-qtNQ
source: Doonsec's feed
date: 2026-05-25
fetch_date: 2026-05-26T06:06:34.407658
---

# 【公益译文】2026年AI指数报告（一）

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/mAopIKtZvYtSwERZ2wH7OibAL3FlIxYvibFXlfiaw8DMwKqQBACuvmN7vl6QcWbR4GXKKk1iaTicSNTwQ0SpSHRTNWrOI3ObtTmrfoxvJlHjxcf0/0?wx_fmt=jpeg)

# 【公益译文】2026年AI指数报告（一）

绿盟科技研究通讯

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

以下文章来源于绿盟科技
，作者绿盟君

![](http://wx.qlogo.cn/mmhead/Q3auHgzwzM5hQWTd2AHZRBvI0pibt2oAA2HeHMTOqTNt5kkrQUmdaYQ/0)

**绿盟科技**
.

绿盟科技 官方微信

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/2icibGKbYdhcxhUlXcsogLPJt1BTrdQjKNmMln5LtY6Oy2LCjClU9criaIAMAMCE7TW54hRX9OCbTUGB64MyM2oAEDb5FyYYywsn3jEAsp5sQg/640?wx_fmt=gif)

**执行摘要**

随着AI的持续快速发展，问题在于围绕它构建的系统能否跟上。追踪AI影响所需的治理框架、评估方法、教育系统和数据基础设施正在努力跟上技术本身的步伐。本报告主要聚焦AI的能力范围和人类管理AI的准备程度之间的差距，追踪AI如何在推理、安全和现实世界任务执行方面进行更雄心勃勃的测试，以及为什么这些测量越来越难以依赖。

近十年来，AI指数一直致力于将可靠的全球数据带入发展速度比大多数衡量方法都快的领域。该报告为政策制定者、研究人员、高管、记者和公众提供了必要的依据，以就AI作出明智的决定。随着这项技术深入学术、医疗和立法机构等领域，重塑人们的工作、学习和治理方式，不完整数据的成本持续上升。

**1**

**研究与开发**

**概述**

2025年，AI开发所需的资源持续增长，但发布的主流模型数量却比上一年有所减少，而且前沿模型越来越集中在少数机构手中。目前，超过90%的主流AI模型都来自各大企业，而功能最强大的模型也最缺乏透明度，训练代码、数据集大小和参数数量等信息越来越不公开。自2022年以来，这些模型背后的计算能力每年增长约3.3倍，但几乎所有计算能力都流向台湾的一家芯片代工厂，这使得全球硬件供应链十分脆弱。开源开发和发布的模型持续增长，研究格局也变得更加地域分散。中国目前在模型发布数量、引用份额和专利授权方面均处于领先地位，而瑞士和新加坡等较小的国家则在人均AI研究人员数量方面领先。然而，该领域的某些方面却丝毫未变。AI人才领域的性别差距依然根深蒂固，自2010年以来，没有任何国家取得实质性进展。本章内容涵盖了AI的研发流程，从AI模型的现状，到支持计算、数据中心、能源和开源软件，再到更广泛的模型发布数量、专利和人才研究生态系统。

**1.1.主流AI模型**

本节使用EpochAI精选的主流模型数据集，探讨前沿AI模型的来源、部署方式以及构建它们所需的条件。EpochAI根据“高级”、进展、历史意义或高引用率等标准将模型评定为值得关注的模型。数据为人工整理，因此数据集并非所有AI模型的普查，也不是所有模型开发活动的完整地图，趋势应理解为领域内的模式。之后的小节将讨论这些模型背后的基础设施和投入，包括计算、数据中心、能源成本和开源软件，通过模型发布情况、专利和研究人才等方面来考察更广泛的研究生态系统。

* **按国家或地区划分**

重要的模型开发仍然集中在少数几个国家（图1.1.1-图1.1.3）。美国开发的模型数量最多，其次是中国。2025年，美国发布了50个AI模型，数量遥遥领先，中国发布了30个，韩国发布了5个。但所有主要地理区域的新模型发布数量均逐年下降。

![](https://mmbiz.qpic.cn/mmbiz_png/2icibGKbYdhcyrYYvKeSyjbKhAAickJIcicSyY8aXKWOcEdIkkuRiaelNDKuzicb1WUoha0v4DvdH4mAKMw6jte5Dk1w3W7ic1wlWuXUbPI2BKJtnM/640?wx_fmt=png&from=appmsg)

图1.1.1

![](https://mmbiz.qpic.cn/mmbiz_png/2icibGKbYdhcyIjNHicxHF2ZrJsU0icXUQYAc110kqiaAr4vZfP3rqjc82PiaYpQ8Z8l6SKEbxIofA2LGlMlR6absOpiakCNfKibyaF7G4o48CacxZQ/640?wx_fmt=png)

图1.1.2

![](https://mmbiz.qpic.cn/mmbiz_png/2icibGKbYdhcwhwiaKhxEa0CGPCmdqCmM2yu3xOV3U3qrLJiaRTOFoNQpuVOxgg9sicsgpxj6kM9CsZibrBicNuNXlI8jHdyrKQ517qDeeseprvjOc/640?wx_fmt=png)

图1.1.3

* **按企业和组织划分**

主流AI模型的开发仍然主要集中在各大企业（图1.1.4和图1.1.5）。过去十年，企业贡献的份额稳步增长，目前已遥遥领先，达到91.6%。2025年，EpochAI识别出高校发布的主流AI模型，而来自企业的则有87个。少数机构占据了大部分的发布份额（图1.1.6和图1.1.7）。2025年，贡献最大的企业是OpenAI（19个）、谷歌（12个）和阿里巴巴（11个）。自2014年以来，谷歌发布的高级模型数量最多，其次是Meta和OpenAI。此外，在过去十年中，贡献最大的各国高校包括清华大学（26个）、斯坦福大学（26个）和卡内基梅隆大学（25个）。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2icibGKbYdhcwH5pDrriaKicS3I9k2vZyApfYcrcX2yibAialGOrc8SP9NtQx93rJrIEgh8hiaOBvrbDfyHDLEzmJx8joCSlNYPSNqs095ab396UAY/640?wx_fmt=png)

图1.1.4

![](https://mmbiz.qpic.cn/mmbiz_png/2icibGKbYdhcwmiceupEvPbkHrCT4ASfV1dl83IBwjyIFPZBwRl4DiaOwaWc30rsUSXwqk6saWGfBzvx0OibUgyyYb7E3lEdbQ9eUln8MPx3L6Qw/640?wx_fmt=png)

图1.1.5

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2icibGKbYdhcx6vQ972jyFC7ZQkuEouSAbn24icdU0lROTWlsVe3xCeicGaRUibMH5tZbzy9AsE1UjXdQDnW5fwBLiazw55g0ibBibtMm4rbya1cCKc/640?wx_fmt=png)

图1.1.6

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2icibGKbYdhcy47RZ1bnq5moZIxEJ9iagQ3okSq21S1hDuHmVaFAv6ia0dibbllalQAuLNjXPxNoQgVYG4IJXjTkPOia7AxSvh4QwGCzYdXdAD824/640?wx_fmt=png)

图1.1.7

* **模型发布**

主流AI模型的发布模式持续向受控访问方向转变（图1.1.8）。2025年，API访问是最常见的发布类型，95个模型中有45个以API访问方式发布。2020年以来，仅提供API访问方式的模型数量持续增长。第二常见的发布类型是“开放权重（无限制）”，这意味着这些模型可以完全用于使用、修改和重新分发。其他模型以多种访问类型混合发布，包括“托管访问（无API）” 、“开放权重（限制使用）”和“开放权重（非商业用途）”。“未知”指的是访问类型不明确或未公开的模型，“未发布”模型仍然是专有的，仅供其开发者或特定合作伙伴访问。

训练代码的可访问性甚至比模型代码整体的可访问性更低（图1.1.9）。2025年，95个主流模型中有80个在发布时未公开相应的训练代码，而只有4个将其代码开源。2020年，公开训练代码和未公开训练代码的模型数量大致相同，但到2023年，大多数模型都未公开，且差距持续扩大。这种日益增长的不透明性限制了外部研究人员复现结果、审核开发过程和验证安全声明的能力。

![](https://mmbiz.qpic.cn/mmbiz_png/2icibGKbYdhcxxbic5XYwt0iakrum3NCSKMXBB5lgCoSBcQiaicvEB5VLAL3caugfG2hdlWtyFYPPWKT5kR6nc1VKHKbUjGRF3SUzO15cgSmbpkqc/640?wx_fmt=png)

图1.1.8

![](https://mmbiz.qpic.cn/mmbiz_png/2icibGKbYdhcz3oLkYRXA3l2ryiahNvcUCSGTKsHjnvicy1DuCAic7lVjE96XFIoyWrQ9iaVNfU6cl11LLgstKLr8ex6iaCbW6hAEDdqibUV8KknCdQ/640?wx_fmt=png)

图1.1.9

* **参数和计算趋势**

到2022年，受模型架构日益复杂、数据可用性增强、硬件改进等因素的推动，已验证的有效性更大的主流模型的参数数量显著增加（图1.1.10–1.1.12）。此后，报告的参数数量增长趋于平缓，但由于缺少某些数据点，这可能低估了实际增长情况。近年来发布的一些资源消耗最大的模型，包括来自OpenAI、Anthropic和谷歌的模型，均未公开披露参数数量、训练数据集大小或训练时长。同样，训练数据集大小和训练时长均有所增加，领先的模型在超过100天的时间内，使用数万亿个令牌进行训练。由于主要前沿实验室披露的信息有限，近几年的相关数据并不完整。

![](https://mmbiz.qpic.cn/mmbiz_png/2icibGKbYdhczicR0rN9Y3k1ff689opJiar6kOyLG5K2yOGsIFXCqBYUcWfFbQGDmu8aZUvZgK63KeV0YJsdTiaOo4wjPXpeibqxgV6Oz00NHznMI/640?wx_fmt=png)

图1.1.10

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2icibGKbYdhczSpUNTia6zScDiaoDJUFeRITtAcSWpCL3SVKrctmUeDibh2Q5jTEWB0BAEB5eYuYBTVUsZTUB1hWax8I2GYiaBZHTfPycmVE1icayU/640?wx_fmt=png)

图1.1.11

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2icibGKbYdhczhLzhlsMUw3f7yj78qHbLJp6cM5ldtddr5qgMSoWOAxYhzWsMdtwsPgXNZd643IOC2IOSX91b6mf30giavz4wF9ZCg1yArsKHA/640?wx_fmt=png)

图1.1.12

即使计算量未直接报告，也可以进行估算，因此，主流模型的训练计算量趋势在同一时期内呈现明显的增长趋势（图1.1.13和图1.1.14）。主流模型的计算需求已增长了几个数量级，其中行业领域的计算量最高。在模型发布数量最高的两个国家中，美国模型的计算量高于中国模型。然而，近年来，由于美国模型未直接报告其训练计算量，因此无法完全证实这一比较结果。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2icibGKbYdhcznrFH79tpEqqN1d8icia5glQEh4ZI1jmw6mkKwib8eHg6ia7rtsg7zO2rIbSJJnaicoTMKGAOH853bkPaic4KLyWoP75TQmjCXSUsCc/640?wx_fmt=png)

图1.1.13

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2icibGKbYdhczqRqJrnH6HMgSIB7T0QqqibD36fxrvgP4OmnTmODW0aBkFMWiaPtzCropePwqNzDhv9Fx8nh76Ea8ZBfMibicTNya5gBqVYcHfC1w/640?wx_fmt=png)

图1.1.14

* **模型是否会耗尽数据**

2025年，AI指数强调了数据瓶颈以及与训练数据相关的扩展方法的可持续性问题。领先的AI开发企业公开声称，用于训练大型模型的高质量人类文本和网络数据池已经枯竭，这种情况通常被称为“数据峰值”。这持续引发了整个行业对扩展规律可持续性的担忧，这些规律历来依赖于不断扩大的数据集。EpochAI的一组预测报告指出，在某些情况下，预计数据可能在2026年至2032年之间耗尽。

* **预训练中的合成数据**

如果由AI模型生成的合成数据可用于提升后续模型的性能，那么现实中的数据的可用性限制可能影响较小。此前的AI指数并未发现确凿依据表明合成数据能在预训练阶段提升模型性能。2024年报告引用的研究表明，用合成数据替换真实训练数据时，模型性能可能会急剧下降。2025年报告指出，研究发现，训练数据中如果包含真实数据，则可以避免模型性能下降，但简单地添加更多数据并不一定能提高性能。人们对这一问题的共识基本没有改变。

目前尚无可靠依据表明合成数据能够完全弥补预训练环境中真实数据的匮乏。然而，近期研究表明，合成数据在更有限的场景下可能具有价值。结合真实数据和合成数据的混合训练方法可以显著提升训练效果。加速训练规模有时会扩大五到十倍，但最终模型的性能却并未超过真实数据。使用纯合成数据进行训练，对于较小的模型或勉强已定义任务，例如，分类、代码生成或相关工作低资源语言，但这些成果并未推广到大型通用语言模型。在仅使用合成训练的情况下，达到的性能与真实数据相当，但通常涉及的模型规模要小得多，无法与当前最先进的模型直接比较。例如，完全基于合成数据训练的SYNTHLLM系列模型的能力较强，但在主要基准测试中仍然落后于高级模型（图1.1.15）。

![](https://mmbiz.qpic.cn/mmbiz_png/2icibGKbYdhcxlEqAyytQAhYsWAhkww5CP7KSThicKsY8MPTjnbyzxforpCO1bhHxlficfDsVGlz5IMEVj3icvS2ZicWoOppEddFtFpvN1B4BEOicU/640?wx_fmt=png)

图1.1.15

* **以数据为中心的方法**

关于数据可用性的讨论常常忽略了近期AI研究中的重要转变，性能的提升越来越依赖于提高现有数据集的质量，而非获取更多数据集。研究人员不再盲目地扩展数据，而是投入更多精力对训练输入进行修剪、筛选和优化。数据中心方法强调通过清理标签、去重样本和构建更高质量数据集等方法来提升性能。越来越多的研究表明，使用低质量或受污染的数据训练模型会显著降低模型性能。同样，最近的依据表明，数据剪枝（即选择最具信息量的训练输入）通常优于不加选择地使用所有可用数据进行训练的方法。

近期大规模模型开发实践证明了这种方法的有效性。Olmo 3系列模型的研究人员优先考虑大规模去重、质量感知的数据选择以及阶段特定的训练方案，而不是盲目地扩展数据。这些干预措施，结合用于评估和改进候选数据组合的迭代反馈循环，使得他们的模型即使在训练所用的标记数量远少于其他高级模型的情况下，其性能也具有竞争力（图1.1.17和图1.1.16）。例如，Olmo 3.1的Think 32B模型包含大约320亿个参数，相比少了近90倍。Grok 4模型的数据集规模为3万亿美元，但在2025年美国数学邀请赛（AIME）等多个基准测试中，其性能与现有模型相当。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2icibGKbYdhcx4iarUP0t1e4McgSOSwvVj5CGqzwVZwOePMG7Jjh5voTmLico2NvicE3MPdBic7u4WJvpmMicK0Ymlwz7VQkAAtibLOicVXCspuibO50Y/640?wx_fmt=png)

图1.1.16

* **训练后的合成数据**

近期研究表明，合成数据可以有效地提高训练后设置中的模型性能，包括微调、对齐、指令调整和强化学习，2025年发布的大量研究支持了这一发现。研究表明，在少样本生成设置中，训练后的合成数据是有效的，主要体现在以下方面：增强长上下文学习能力、优化强化学习工作流程和加强更广泛的推理能力。

* **合成内容的普及程度**

2022年11月ChatGPT发布以来，很多人预测，网络很快就会被各种AI生成内容淹没。Graphite的研究报告指出，2025年以来，超过50%的新发布的内容由AI生成（图1.1.17）。还有研究表明，2026年，这一比例会持续升高。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2icibGKbYdhcytRJHYk0kj3icmiaicDjZvAwL9lVAS87z3U6BPaPjO0ELfQmpbvjwDypoZFwNBb9yUwNHsRn0zd63nuCJsa5KbdgibOI1GrvabL90/640?wx_fmt=png)

图1.1.17

人们越来越关注合成数据是否适合用于AI模型的训练，这一趋势引发了人们对当前扩展路径长期可靠性的质疑。为此，许多依赖高质量训练数据的公司越来越多地转向专有数据源。2025年5月，《纽约时报》与亚马逊达成许可协议，允许将其内容用于训练。2025年年中，Meta成为参与新闻机构进行类似磋商，同时，百时美施贵宝等健康和生命科学公司也参与其中。这些情况表明，随着公开可用的训练数据量不断增加，训练前沿AI模型的公司正在调整其数据采集策略。

**1.2.计算和基础设施**

AI模型的开发需要大量的基础设施投资。随着训练过程规模和复杂性的增加，底层硬件的速度和效率也得到了提升。反过来，这些进步也决定了研究人员和实验室能够构建的模型类型。如果没有硬件能力的相应提升，训练计算能力的增长是不可能实现的。本节将通过EpochAI的数据跟踪硬件性能、采用情况和总计算能力随时间的变化。

* **性能和效率**

2008年至2025年间，机器学习硬件的峰值计算性能呈指数级增长（图1.2.1）。这种提升在低精度类型中尤为明显，精度指的是用于表示数值的位数。FP16和Tensor-FP16/BF16等低精度格式目前展现出最高的性能水平，已成为许多训练和推理场景的标准配置。

...