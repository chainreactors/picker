---
title: 无需数据的秘密揭露：图神经网络能否通过数据无关的模型窃取攻击被利用
url: https://mp.weixin.qq.com/s/dJ4udgITnCH_o5b8NacaoQ
source: Doonsec's feed
date: 2026-02-12
fetch_date: 2026-02-13T04:14:16.552181
---

# 无需数据的秘密揭露：图神经网络能否通过数据无关的模型窃取攻击被利用

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/6Dibw6L070WHxkpnsKqs368C4jRYttVtYmJcOXiccLEX3EhtbnP5LegafgKzoJGicibQlYibM9icGFVAC3Puq0yBnc7A/0?wx_fmt=jpeg)

# 无需数据的秘密揭露：图神经网络能否通过数据无关的模型窃取攻击被利用

原创

周辰昕
周辰昕

安全学术圈

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/sz_mmbiz_png/6Dibw6L070WHxkpnsKqs368C4jRYttVtY4ibCbmNx8vRObavOUP9udaqcYd3N3ZMe6whm2ib6y3BXwyCF50XtX5SA/640?wx_fmt=png&from=appmsg)

> *论文题目：Unveiling the Secrets without Data: Can Graph Neural Networks Be Exploited through Data-Free Model Extraction Attacks?*
> *论文作者：Yuanxin Zhuang, Chuan Shi, Mengmei Zhang, Jinghui Chen, Lingjuan Lyu, Pan Zhou, Lichao Sun*
> *发表会议：33rd USENIX Security Symposium*
> *主题类型：攻击检测*
> *笔记作者：周辰昕@Web攻击检测与追踪*
> *主编：黄诚@安全学术圈*

# 研究概述

论文聚焦于图神经网络（GNN）的安全性问题，特别是数据无关的模型提取攻击。论文指出，尽管GNN在诸多领域表现突出，但其对知识产权威胁的脆弱性却不容忽视。以往的模型提取攻击多依赖于对受害模型训练数据的特定信息访问，如节点属性和图结构等，然而在实际场景中，这些信息往往难以获取。

为此，文章提出了首个针对GNN的数据无关模型提取攻击框架——STEALGNN。该框架具备三大优势：一是完全数据无关，无需真实节点特征或图结构即可实现攻击；二是攻击范围广，适用于节点分类和链接预测等任务；三是能在硬标签攻击场景下运作，此时攻击者对目标GNN一无所知，仅能通过查询获取预测标签。论文通过在四个基准图数据集上的实验，验证了STEALGNN对代表性GNN模型攻击的有效性。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/6Dibw6L070WHxkpnsKqs368C4jRYttVtYd7zA4fb94icRqo3TPNrp8VpZKIocfA1mPXjZBTqB9lS0feAdqcgZXxA/640?wx_fmt=png&from=appmsg)

图1 三种攻击类型生成器更新策略示意图

图1展示了 STEALGNN 框架中生成器更新的三种不同策略，旨在通过不同的梯度更新方法来优化生成器，以便更有效地提取GNN模型的知识。具体来说，图1包括三个子图：(a)、(b) 和 (c)，分别对应 Type I、Type II 和 Type III 攻击。其中蓝色箭头表示数据流的方向，MG表示图生成器，负责生成合成图；MV表示受害模型，攻击者无法直接访问其参数；MS表示替代模型，攻击者训练该模型以模仿受害模型的行为；L是损失函数，用于衡量替代模型和受害模型输出之间的差异。

* Type I攻击中，生成器的梯度更新通过替代模型和对受害模型的梯度估计来实现。生成器产生的图同时输入到受害模型和替代模型中。通过比较两者的输出，计算损失函数。然后，使用零阶梯度估计方法来近似受害模型的梯度，并结合替代模型的梯度来更新生成器的参数。这种方法能够利用受害模型的丰富知识来优化生成器，从而生成更有效的查询图。
* Type II 攻击中，生成器的梯度更新仅通过替代模型来实现。生成器产生的图输入到替代模型中，通过比较替代模型的输出与受害模型的输出（硬标签），计算损失函数。然后，仅使用替代模型的梯度来更新生成器的参数。这种方法简化了梯度更新过程，适合在查询次数受限的情况下使用。
* Type III 攻击中，生成器的梯度更新通过两个替代模型来实现。生成器产生的图输入到两个替代模型和受害模型中。通过比较两个替代模型的输出与受害模型的输出，计算损失函数。然后，利用两个替代模型的梯度差异来更新生成器的参数。这种方法能够捕捉到更复杂的知识，因为它利用了两个替代模型之间的差异来优化生成器。

# **贡献分析**

* 贡献点1：论文针对现有GNN模型提取攻击中对原始训练数据依赖的问题，提出了首个数据无关的模型提取攻击框架STEALGNN，实现了无需真实数据即可从GNN模型中提取知识的攻击方法，为GNN模型的安全性研究开辟了新的方向；
* 贡献点2：论文针对现有攻击方法在硬标签攻击场景下的局限性，提出了适用于硬标签场景的攻击策略，实现了在攻击者对目标模型一无所知时的知识提取，显著提升了攻击的实用性和威胁性；
* 贡献点3：论文针对GNN在节点分类和链接预测任务中的应用，提出了统一的攻击框架STEALGNN，实现了对这两种任务的有效攻击，验证了该框架在不同任务场景下的广泛适用性。

# 代码分析

代码链接：https://github.com/T-Breezy444/Data-Free-GNN-attack

1. 代码使用类库分析，是否全为开源类库的集成？

项目依赖类库有：torch、numpy、matplotlib、seaborn、scikit-learn、tqdm等，均为开源类库。

2. 代码实现难度及工作量评估

代码实现难度较高，涉及GNN模型设计、生成对抗网络和对抗攻击策略。需处理梯度计算、模型状态切换，针对不同数据集调整模型参数并验证攻击效果，工作量较大。

3. 代码关键实现的功能（模块）

* 受害者模型定义不同数据集的GNN模型；
* 替代模型通过模仿受害者模型的输出辅助攻击；
* 生成器生成合成图数据（特征与邻接矩阵），用于替代真实数据驱动攻击流程；
* 攻击模块实现论文所定义的三种攻击；
* 评估模块整合数据集加载、受害者模型训练、攻击执行及结果评估。

# 论文点评

1. 论文提出了首个针对图神经网络（GNN）的数据无关模型提取攻击框架STEALGNN，这一创新性贡献突破了现有攻击方法对原始训练数据的依赖，实现了无需真实数据即可提取GNN模型知识的攻击方法。论文的实验设计较为全面，涵盖了四个基准图数据集，并在多个GNN模型（如GCN、GAT和GraphSAGE）上进行了验证。实验结果表明，STEALGNN在多个数据集上均能取得较高的攻击成功率，且在某些情况下，替代模型的性能甚至超过了原始模型。这表明STEALGNN生成的合成图能够有效地捕捉和转移GNN模型的知识。
2. 论文对STEALGNN的攻击机制和优化策略进行了较为深入的理论分析，为理解和实现该攻击提供了基础。论文提出了创新的图生成器，能够在无需真实数据的情况下生成合成图。这种生成器的设计结合了特征生成和结构生成两个方面，确保生成图的多样性和复杂性。论文还通过损失函数引导生成器产生更复杂的图，从而提升替代模型的学习效果。这种协同优化策略不仅提高了攻击的成功率，还展示了生成器和替代模型之间的有效交互。
3. 尽管论文在创新性和实验验证方面表现出色，但仍有一些可以改进的地方。未来的工作可以进一步拓展实验，例如在更大规模和更复杂的图数据集上进行测试，以验证STEALGNN在实际应用中的表现。此外，与更多最新相关工作的对比可以进一步增强实验结果的说服力。论文可以进一步探讨STEALGNN在具体实际场景（如金融风控、社交网络分析等）中的应用，以及如何在实际系统中防御此类攻击。对于STEALGNN的理论性质（如收敛性、泛化能力等）分析可以进一步完善，以更好地指导实践应用。论文代码在实现细节上可以更加透明，例如提供更详细的超参数设置和调试经验，优化代码的模块化设计，以便其他研究人员更容易复现实验结果和在此基础上进行扩展研究。

# 论文文献

1. Zhuang Y, Shi C, Zhang M, et al. Unveiling the Secrets without Data: Can Graph Neural Networks Be Exploited through Data-Free Model Extraction Attacks?[C]// Proceedings of the 33rd USENIX Security Symposium. Philadelphia, PA, USA: USENIX Association, 2024: 5251-5266.

> [安全学术圈招募队友-ing](http://mp.weixin.qq.com/s?__biz=MzU5MTM5MTQ2MA==&mid=2247484475&idx=1&sn=2c91c6a161d1c5bc3b424de3bccaaee0&chksm=fe2efbb0c95972a67513c3340c98e20c752ca06d8575838c1af65fc2d6ddebd7f486aa75f6c3&scene=21#wechat_redirect)
> 有兴趣加入学术圈的请联系 **secdr#qq.com**

---

**专题最新征文**

* [期刊征文 | 暗网抑制前沿进展](https://mp.weixin.qq.com/s?__biz=MzU5MTM5MTQ2MA==&mid=2247491610&idx=1&sn=8b6c9caf92435cbd9b76b77686619972&scene=21#wechat_redirect) (中文核心)
* [期刊征文 | 网络攻击分析与研判](https://mp.weixin.qq.com/s?__biz=MzU5MTM5MTQ2MA==&mid=2247491661&idx=1&sn=ab0a97741cdf854757ef3024b03f1d44&scene=21#wechat_redirect) (CCF T2)
* [期刊征文 | 域名安全评估与风险预警](https://mp.weixin.qq.com/s?__biz=MzU5MTM5MTQ2MA==&mid=2247491703&idx=1&sn=7f351031fc81e1b63d5215ddb8dc91b5&scene=21#wechat_redirect) (CCF T2)

---

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/6Dibw6L070WFvZRQiafv3iccicic1dIYUEQ1ZzLh1a10l7tfw7zkWkRbY9kEPBwX2NiadOrwFl9a48as9qiayp3eOgDUQ/0?wx_fmt=png)

安全学术圈

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/6Dibw6L070WFvZRQiafv3iccicic1dIYUEQ1ZzLh1a10l7tfw7zkWkRbY9kEPBwX2NiadOrwFl9a48as9qiayp3eOgDUQ/0?wx_fmt=png)

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