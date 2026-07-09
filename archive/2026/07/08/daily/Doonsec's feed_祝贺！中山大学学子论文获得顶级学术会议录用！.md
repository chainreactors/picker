---
title: 祝贺！中山大学学子论文获得顶级学术会议录用！
url: https://mp.weixin.qq.com/s/6HQjjWk8q3pYVeK8y9LkGQ
source: Doonsec's feed
date: 2026-07-08
fetch_date: 2026-07-09T05:56:53.447897
---

# 祝贺！中山大学学子论文获得顶级学术会议录用！

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/FNlvhjUaDTNicJNOfcXcFLZum0EzdC7Xv7CGabq1tpicfQKpRZWHvfz1NQYicsz5SqS481fR41ngHzaLygYydkQBiabibyDPqiabBQCGs9AJ9zRF0/0?wx_fmt=jpeg)

# 祝贺！中山大学学子论文获得顶级学术会议录用！

信息网络安全杂志

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

近日，机器学习与人工智能领域国际顶级学术会议ICML 2026论文接收结果公布，**我校网络空间安全学院师生共有24篇论文获得录用**。其中，学院**2022级本科生彭梓杰**在沈力副教授指导下完成的论文成功被会议接收。

![](https://mmbiz.qpic.cn/mmbiz_png/vJMPdJ0dUUibv9KqdJyj52ibAhAm7vxLKzKPhZhRZj99micEnRiahzuOrq8pRxgBwHRVRQzjb3mQfxtyhBLHS3ZA5qLFabu9ZbggCZQPZXr6t7E/640?wx_fmt=png)

国际机器学习大会ICML（International Conference on Machine Learning）创办于1980年，与NeurIPS、ICLR并称为**机器学习领域国际三大顶级学术会议**，同时也是中国计算机学会**（CCF）推荐的****A类会议**。ICML 2026接收率为26.6%。

**网安学子论文速览**

**1**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MVPvEL7Qg0Giav3ZasiaicZ0ianQ9KraPL8OK9wjia8CSgMTt9eLQcbGBcKdLFDtziaM2ganLGpXY6tGOB4GG16uwuibQ/640?wx_fmt=png)

**Continual Personalization of Diffusion Models via Submodular Concept Neuron Selection**

作者：**彭梓杰（2022级本科生）**、杨恩能（博士后）、程亦飞（博士后）、袁红亮、马飞、操晓春（教授）、沈力（副教授）

（上下滑动文字查看，下同）

本文针对定制扩散模型（CDMs）在持续个性化任务中存在的灾难性遗忘、语义冗余、参数更新效率低等问题，提出一种基于子模集概念神经元选择的轻量化持续学习方法 SCNS。现有扩散模型个性化方法多假设概念静态，依赖模型融合或顺序微调，易出现属性纠缠、概念干扰，且传统神经元选择依赖启发式规则，忽略语义冗余与参数冲突。SCNS 将持续个性化建模为约束子模集优化问题，融合基于设施选址的语义覆盖目标、Fisher 加权风险保护项与代价感知贪心选择规则，在边际收益递减特性下筛选最小且足够的概念专属神经元子集，仅微调交叉注意力层的极少量参数（平均每个概念仅更新 0.41% 参数），无需模型后融合即可实现稳定性与可塑性的平衡。实验在 8-10 个连续概念流上验证，SCNS 在图像对齐、身份保真度与抗遗忘性能上均达到 SOTA，且存储与计算开销极低、对概念学习顺序鲁棒，跨架构泛化性强，为隐私友好、高效的生成式 AI 持续个性化提供了理论与工程可行的新方案。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/vJMPdJ0dUU8qYPTca4bA1w38snDnhSLWgiaKJSEZUOzXSW4nSZlaNYoukNAGj4icDEpPibQ4JaAZZR3pAjXvkfZ9fqIcKl2akIcicMib9jWqnqFA/640?wx_fmt=png)

**2**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MVPvEL7Qg0Giav3ZasiaicZ0ianQ9KraPL8OK9wjia8CSgMTt9eLQcbGBcKdLFDtziaM2ganLGpXY6tGOB4GG16uwuibQ/640?wx_fmt=png)

**HTAC: Hierarchical Task-Aware Composition for Continual Offline Reinforcement Learning**

作者：**周启扬（2025级博士生）**、许锐航（博士后）、王鹏（博士后）、芦文杰、操晓春（教授）、谭乃强、沈力（副教授）

持续离线强化学习（CORL）旨在从静态数据集中构建具备长期自主学习能力的智能体。然而，任务间在环境动态、奖励函数和行为策略上的异质性，要求智能体在迁移过程中既能选择性复用共享知识，又能隔离任务特异性特征。现有方法采用的扁平化知识共享机制难以捕捉这种区分，限制了跨任务泛化能力。为此，我们提出层次化任务感知组合方法（HTAC），通过双层任务编码与软组合机制实现可塑性与稳定性的平衡。HTAC包含四个核心模块：（1）层次化语义任务表示，将任务解耦为域级与任务级嵌入；（2）双层专家网络，按需创建域专家与任务专家以实现参数高效的知识隔离；（3）自适应知识组合模块，通过注意力机制整合历史专家输出以实现知识复用；（4）任务适配器，保护历史路由权重以防止遗忘。在离线持续世界基准上的实验表明，HTAC优于现有基线方法，展现出更优的知识复用与迁移能力。

**3**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MVPvEL7Qg0Giav3ZasiaicZ0ianQ9KraPL8OK9wjia8CSgMTt9eLQcbGBcKdLFDtziaM2ganLGpXY6tGOB4GG16uwuibQ/640?wx_fmt=png)

**VIRUS: Injecting Persistent Cognitive Pathogens into Stateful Zero-Shot Object Navigation Agents**

作者：**林旭升（2025级博士生）**、郑浩（博士后）、加小俊、李秋岑（博士后）、单天奇（2025级硕士生）、许杰、任文琦（教授）

文章研究了零样本目标导航智能体在长期任务规划中的潜在安全风险。随着机器人和智能体逐渐具备持续记忆、环境理解和自主决策能力，其内部状态一旦受到错误感知信息影响，可能会在后续行动中持续放大，带来导航失效与安全隐患。论文提出 VIRUS 框架，系统分析了状态化零样本目标导航智能体在视觉与语言双重触发条件下的脆弱性，并通过实验验证了该问题在不同导航架构、视觉语言模型和复杂室内环境中的普遍存在。研究结果表明，仅依靠模型规模提升或常规安全对齐，难以充分保障具身智能系统的长期可靠性。该工作为未来构建更安全、更可信的机器人导航系统提供了重要参考。

**4**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MVPvEL7Qg0Giav3ZasiaicZ0ianQ9KraPL8OK9wjia8CSgMTt9eLQcbGBcKdLFDtziaM2ganLGpXY6tGOB4GG16uwuibQ/640?wx_fmt=png)

**Efficient Bilevel Optimization for CKA-Guided MoE Upcycling**

作者：**余致远（2026级准博士生）**、杨恩能（博士后）、蒋昊、朱国杰、何飞宏（2024级博士生）、王鹏（博士后）、沈力（副教授）

上循环（Upcycling）是一种通过复制预训练的前馈或专家混合网络（MoE）来初始化MoE以扩展模型容量的策略，因其在缓解灾难性遗忘方面的有效性，已成为持续学习中的流行方法。然而，现有范式依赖无差别扩展，以极端的低效为代价优先追求准确率，在引入参数冗余的同时，未能利用对于以架构经济性对抗遗忘至关重要的结构异质性。

为解决这一问题，我们利用中心化核对齐（CKA）和损失景观平坦度来研究训练动态中遗忘的决定因素，分析扩展前后MoE层的行为，揭示了深层表征的不稳定性以及专家对新任务的异质性敏感度，从而证明了选择性上循环消除冗余的潜力。因此，我们提出了一个动态双层优化框架来指导自适应上循环，其外层循环采用Gumbel-Softmax可微掩码执行神经架构搜索（NAS）以实现自适应增长，而内层循环则通过任务目标和CKA正则化回放来优化权重更新。

在TRACE基准测试上的实验表明，我们提出的方法在平均准确率方面表现更优，同时减少了80%的遗忘，并有效消除了标准上循环会引入的60%冗余参数扩展。

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/MVPvEL7Qg0GnB0HoAz6et8CCnxyj1ZuTbibLicgffRjlcMdVIdN51jg8QUEWdeDSfJYJ6p3qeJQdGMo4rpVa2jPA/640?wx_fmt=gif)

24篇顶会论文的背后，是网安师生逐梦学术前沿的铿锵足迹，更是学院科研育人、薪火相传的生动体现。学院将始终锚定立德树人根本任务，全面提高人才自主培养质量，持续赋能拔尖创新人才培育，提升基础研究原始创新能力，为国家网络空间安全事业培养更多拥有卓越创新思维、勇担时代使命的栋梁之材。

来源：中大学工微信公众号

![图片](https://mmbiz.qpic.cn/mmbiz_png/icL7Q0hLWsN8yDJWicSECDq8dgel7DctAMAnNheJf2kkfQOiaFMdZaWNIDt9IxOkEhI5TJar4wnyAiba9twTOxeKZg/640?wx_fmt=png&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=1)

**信息网络安全**

《信息网络安全》创刊于2001年，是由公安部主管，公安部第三研究所、中国计算机学会主办，面向国内外公开发行的国内首批信息安全类期刊之一，于2015年成为中国科技核心期刊，2017年成为中国科学引文数据库来源期刊，2018年成为中文核心期刊，2022年入选CCF计算领域高质量科技期刊分级目录。

![图片](https://mmbiz.qpic.cn/mmbiz_jpg/icL7Q0hLWsN9e1fkuM1ibgD3PcZiaqJrZia7KQWDwichD8lvo4RqfPcNkuyqje45IOXD0HocBDntaDdK4tibWoTIs5Ww/640?wx_fmt=jpeg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=2)

中文核心期刊

中国科技核心期刊

中国科学引文数据库来源期刊

CCF计算领域高质量科技期刊

![图片](https://mmbiz.qpic.cn/mmbiz_png/v4vz52CcB12BRNZGqdRDIBsUQ6WickDoUNkuVicKXooNbRSzdGDGuJtxJodlbpr1B07yAReAz5V5jj47Yaq7ujRw/640?wx_fmt=png&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=3)

我们在不断努力和完善中，期待您的关注和支持！

预览时标签不可点

![]()

微信扫一扫
关注该公众号

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