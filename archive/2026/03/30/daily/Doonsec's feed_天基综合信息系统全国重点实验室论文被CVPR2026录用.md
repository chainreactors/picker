---
title: 天基综合信息系统全国重点实验室论文被CVPR2026录用
url: https://mp.weixin.qq.com/s/g2m9CEIA0s_zJsayAbE-iQ
source: Doonsec's feed
date: 2026-03-30
fetch_date: 2026-03-31T04:31:04.820562
---

# 天基综合信息系统全国重点实验室论文被CVPR2026录用

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/FNlvhjUaDTPBvegk4qAqpdibcF4QN5nIVNflGHMe1V42Rz7vMJ6cQkfesSatCC5VKtG5JqLN1PJJX3TDWK1sxwUyyO32BKxCsYjhLSIKJPto/0?wx_fmt=jpeg)

# 天基综合信息系统全国重点实验室论文被CVPR2026录用

信息网络安全杂志

![]()

在小说阅读器中沉浸阅读

近日，实验室研究团队的论文“COPO: Causal-Oriented Policy Optimization for Hallucinations of MLLMs”被计算机视觉与模式识别会议（The IEEE/CVF Conference on Computer Vision and Pattern Recognition 2026，简称CVPR）接收。CVPR是中国计算机学会（CCF）推荐的A类国际学术会议，在人工智能，机器学习和数据挖掘领域享有很高的学术声誉。下面将对该论文做详细的解读，供大家交流学习。

论文题目：COPO: Causal-Oriented Policy Optimization for Hallucinations of MLLMs

论文作者：郭沛正\*，王婧瑶\*，强文文，周嘉欢，郑昌文，华刚

通讯作者：强文文

**概述**

多模态大语言模型（MLLMs）尽管展现出了令人瞩目的能力，但它们仍可能存在幻觉问题。通过实证研究，我们发现，与纯文本大语言模型相比，多模态大语言模型会不成比例地关注与任务无关的背景区域，这暗示背景与答案之间可能存在虚假关联。我们提出并分析认为，基于结果的奖励可能是导致虚假关联的重要因素，而虚假关联又可能是导致幻觉的重要因素。据此，我们提出了面向因果的策略优化（Causal-Oriented Policy Optimization, COPO）方法，以抑制这些虚假关联，进而缓解幻觉问题。该方法通过施加token级的充分性与必要性约束，来衡量每个推理token的因果贡献，从而确保输出的正确性与证据支撑性。具体而言，我们首先通过新提出的因果完备性奖励来评估每个token的因果贡献，随后将该奖励用于在 GRPO 优化框架中构建因果感知的优势函数，引导模型关注那些对准确生成而言因果上充分且必要的token。在多种基准测试上的实验结果证明了 COPO 方法的优势。

**动机与分析**

MLLMs的幻觉现象通常指模型生成的内容与输入的多模态证据不一致或缺乏支撑 。强化学习（RL），特别是组相对策略优化（GRPO），因其有效性被广泛采用为增强模型推理能力的后训练范式。然而，我们的动机实验揭示了一个有趣的现象：在相同的GRPO后训练下，无论生成的答案正确与否，MLLM在与任务无关的背景区域上的梯度显著性通常高于纯文本LLM，如图2所示。这种现象表明结果导向的奖励机制存在局限性。在GRPO训练期间，奖励仅基于最终结果的正确性。任何偶然得出正确结果的生成轨迹都会得到正向强化，即便其推理过程部分依赖于视觉输入中的背景线索。随着时间推移，这会逐渐促使模型将无关的背景线索与正确的输出结果关联起来，从而强化虚假关联。在推理阶段的Token生成通常遵循Top K等采样策略和束搜索等候选序列选择方法。由于模型同时关注前景和背景信息，背景特征有不可忽视的几率在候选生成或选择中占据主导地位。当这种情况发生时，模型就会生成偏离事实真相的流畅输出，即产生幻觉 。因此，如何设计监督信号以强化正确因果路径并抑制虚假关联，成为了方法设计的出发点。

![图片](https://mmecoa.qpic.cn/sz_mmecoa_png/eDliapVbWcC5IwVaKK7NrOyUALDoicUibNbSD8str6MEjMCrL0bSdMHchYdhM1YRMPjHYDBhZ98jMVYPZ2Y0H3kw5wgfol8prWGkpXicZAG6VtA/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=10005&wx_lazy=1#imgIndex=0)

**图1 动机实验结果**

**方法**

为了解决因虚假关联引发的幻觉问题，我们从因果理论出发，构建了MLLMs的结构因果模型（SCM），并提出了COPO框架。该框架的核心在于要求生成的推理Token同时满足因果的“充分性”和“必要性”，鼓励模型关注携带不可或缺的预测信息的因果因素，并抑制背景等非因果因素的干扰。为了量化每个Token的贡献，COPO首先计算“因果充分性得分”和“因果必要性得分”。因果充分性通过对比包含与不包含该Token时奖励的提升程度来衡量；因果必要性则通过将该Token掩码后奖励的下降程度来评估。随后，我们将这两个得分加权融合成因果完整性奖励，为满足因果充分性与必要性的Token分配更高奖励。在优化阶段，COPO将该因果奖励整合到GRPO的推理Token优势函数中。通过联合优化目标，COPO在保留GRPO优势的同时，利用Token级别的因果监督明确增强策略学习。这引导模型在学习过程中优先考虑提供因果证据的推理Token，抑制虚假关联，从而有效缓解幻觉 。

![图片](https://mmecoa.qpic.cn/sz_mmecoa_png/eDliapVbWcC4U3SgYTcFMNMaxBcs0O4QzK6w8rIo1a6NLu0zIk65cqFIxibIiaT4P67LEZlvSicdD9rUdqGgTLUFWwibTH5rvbQYoHK3kRX53Z8g/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=10005&wx_lazy=1#imgIndex=1)

**图2  因果导向的策略优化（COPO）框架概述**

**实验**

我们在多个主流多模态大模型和标准幻觉评估基准上系统测试了COPO框架，并与现有多项基线方法进行了对比。实验结果表明：COPO能够通过抑制模型生成过程中的虚假关联，有效降低幻觉错误率，并提升输出事实的一致性。此外，消融实验与计算开销表明，COPO的充分性与必要性约束模块不仅有效，还在性能表现与计算开销之间展现出了良好的平衡与应用价值。

![图片](https://mmecoa.qpic.cn/sz_mmecoa_png/eDliapVbWcC4vNJibribOhj5KjPsBO1GqVMJlyJ86uUKI38I4uHzW43GjHKSRnUojYh3x4zSEXw7lXyMhibltpWk1Emnibk9AYQGYg4qASzTrRFI/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=10005&wx_lazy=1#imgIndex=2)

**表1 幻觉评估任务结果**

来源：天基综合信息系统全国重点实验室微信公众号

![图片](https://mmbiz.qpic.cn/mmbiz_png/icL7Q0hLWsN8yDJWicSECDq8dgel7DctAMAnNheJf2kkfQOiaFMdZaWNIDt9IxOkEhI5TJar4wnyAiba9twTOxeKZg/640?wx_fmt=other&wxfrom=5&wx_lazy=1&randomid=qnylxjok&tp=webp#imgIndex=2)

**信息网络安全**

《信息网络安全》创刊于2001年，是由公安部主管，公安部第三研究所、中国计算机学会主办，面向国内外公开发行的国内首批信息安全类期刊之一，于2015年成为中国科技核心期刊，2017年成为中国科学引文数据库来源期刊，2018年成为中文核心期刊，2022年入选CCF计算领域高质量科技期刊分级目录。

![图片](https://mmbiz.qpic.cn/mmbiz_jpg/icL7Q0hLWsN9e1fkuM1ibgD3PcZiaqJrZia7KQWDwichD8lvo4RqfPcNkuyqje45IOXD0HocBDntaDdK4tibWoTIs5Ww/640?wx_fmt=other&wxfrom=5&wx_lazy=1&randomid=fbknkhlb&tp=webp#imgIndex=3)

中文核心期刊

中国科技核心期刊

中国科学引文数据库来源期刊

CCF计算领域高质量科技期刊

![图片](https://mmbiz.qpic.cn/mmbiz_png/v4vz52CcB12BRNZGqdRDIBsUQ6WickDoUNkuVicKXooNbRSzdGDGuJtxJodlbpr1B07yAReAz5V5jj47Yaq7ujRw/640?wx_fmt=other&wxfrom=5&wx_lazy=1&randomid=23elspay&tp=webp#imgIndex=4)

我们在不断努力和完善中，期待您的关注和支持！

预览时标签不可点

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