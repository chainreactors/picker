---
title: 武汉大学 | JBShield: 通过激活概念分析与操控防御大语言模型免受越狱攻击
url: https://mp.weixin.qq.com/s/EZd9hJV7BarJunzyLyAaEQ
source: Doonsec's feed
date: 2026-01-08
fetch_date: 2026-01-09T03:29:32.748203
---

# 武汉大学 | JBShield: 通过激活概念分析与操控防御大语言模型免受越狱攻击

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/6Dibw6L070WET5nckc2Gb3177wG4fpPwS9bDOdibKbClxrzU0sgNwCaBD0DbgtKUhMWZtnQHVWia2g8UOFV4EE9rg/0?wx_fmt=jpeg)

# 武汉大学 | JBShield: 通过激活概念分析与操控防御大语言模型免受越狱攻击

原创

王博

安全学术圈

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/sz_mmbiz_png/6Dibw6L070WET5nckc2Gb3177wG4fpPwSvlBiaCmSnBBH4vxP7w8hIMBRdmSx0rBz5ianO81GQ1qNKARZtOMTpKlQ/640?wx_fmt=png&from=appmsg)

*论文题目：JBShield: Defending Large Language Models from Jailbreak Attacks through Activated Concept Analysis and Manipulation*
*论文作者：Shenyi Zhang, Yuchen Zhai, Keyan Guo, Hongxin Hu, Shengnan Guo, Zheng Fang,Lingchen Zhao, Chao Shen, Cong Wang, and Qian Wang*
*发表会议：\_USENIX Security\_*
*主题类型：攻击检测*
*笔记作者：王博@Web攻击检测与追踪*
*主编：黄诚@安全学术圈*

### 研究概述

以大型语言模型（LLMs）为代表的生成式人工智能功能强大，但也易受越狱攻击的威胁，导致生成有害内容，其防御机制的研究受到广泛关注。越狱攻击（即通过对原始输入添加语义扰动，绕过模型安全防护的一类攻击）不仅破坏模型安全性，还揭示了模型内部表征的脆弱性（如通过概念分析可揭示越狱机制），从这个角度来看，如何理解越狱机制并设计鲁棒的防御框架具有重要实际意义。在此背景下，本文提出了一种全面的越狱防御框架 JBSHIELD，该框架通过分析模型隐藏表征中的毒性概念和越狱概念，实现对越狱攻击的检测与缓解。所设计的框架具有通用性，可适配不同架构的LLMs（如Mistral、Vicuna、Llama等）。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/6Dibw6L070WET5nckc2Gb3177wG4fpPwSic9DiaFxmtpkpib185m9bSFqC4icJ0fnIoibl3efgEsevZVUJl6u2M6icq5w/640?wx_fmt=png&from=appmsg)

图1给出了JBSHIELD的核心框架示意图，包含越狱检测（JBSHIELD-D） 和越狱缓解（JBSHIELD-M） 两大模块，其核心思想是利用线性表征假设提取关键概念子空间，通过概念激活状态分析实现防御。JBSHIELD-D通过对比输入与校准数据的表征差异，检测毒性概念与越狱概念是否同时激活；JBSHIELD-M在检测到越狱攻击时，增强毒性概念以触发模型安全机制，同时抑制越狱概念以阻断攻击操纵。实验表明，该框架在5种LLMs上对9类越狱攻击的平均检测准确率达95%，攻击成功率从61%降至2%。

##### 本文贡献如下：

1. 揭示越狱机制：首次通过概念分析证明LLMs能识别越狱输入中的毒性语义，而越狱概念激活是模型输出从拒绝转向服从的关键原因；
2. 提出统一防御框架：设计端到端的JBSHIELD，首次实现单次前向传播的越狱检测与动态安全响应（非固定拒绝输出）；
3. 验证高效普适性：框架仅需30个校准样本，在多种LLMs与攻击中显著优于10种基线方法（检测F1分数0.94，缓解效果提升59%）。

### 贡献分析

* 贡献点1：论文针对越狱攻击机制不明确问题，提出了基于线性表征假设的激活概念分析法，实现了首次揭示LLMs通过毒性概念识别恶意语义、通过越狱概念触发行为篡改的核心攻击机理；
* 贡献点2：论文针对现有防御方案检测与缓解割裂问题，提出了端到端框架JBSHIELD（含JBSHIELD-D检测器与JBSHIELD-M缓解器），实现了单次前向传播完成越狱识别（检测F1=0.94）及动态安全响应；
* 贡献点3：论文针对防御方法泛化性差与数据依赖强问题，提出了校准数据驱动的概念子空间锚定技术，实现了仅需30个样本即在5类LLMs上平均降低ASR 59%（61%→2%）的轻量化部署。

# 代码分析

代码链接：https://github.com/NISPLab/JBShield

1. 本文代码完全基于开源类库集成，以transformers、pytorch、pandas、scikit-learn、nltk等均为主流开源库为核心依赖库。其所有LLM均通过官方开源渠道下载。
2. 代码实现难度及工作量评估；代码实现难度较高，需逆向工程LLM隐藏层激活，定位jailbreak相关概念，涉及激活空间操纵、概念解耦等前沿技术。工作量大，需要做到全流程覆盖：需要做到数据预处理、概念提取、双模块开发多模型评测框架。
3. 代码核心模块包括概念提取模块、检测模块、缓解模块、数据管理模块和模型加载器。其中，概念提取模块从LLM隐藏层提取与jailbreak相关的可解释概念，进行激活空间分析、关键神经元定位。检测模块实时检测jailbreak攻击基于激活概念分析计算风险分数。缓解模块动态防御攻击通过修改高风险激活向量降低攻击成功率。

# 论文点评

* **线性表征假设有一定局限性：** 论文完全依赖线性表征假设，但LLM的高维表征可能存在复杂非线性交互。实验仅通过SVD分解一阶线性差异，未验证概念子空间的独立性。可以考虑引入非线性分解方法提取概念。通过对比学习优化概念子空间，确保其判别性。
* **概念定义模糊：** 毒性概念与越狱概念的定义依赖人工选择的对比样本（有害/良性/越狱提示），但未量化概念语义边界。不同攻击的越狱概念token差异大，缺乏统一语义解释。可以考虑结合概念激活向量等可解释性工具，建立概念与人类可理解特征的映射。设计跨攻击的共享概念词典。
* **实验设计与评估存在不足：** 校准数据集仅含850个样本，且依赖AdvBench和Alpaca等公开集，覆盖场景有限（如缺少多语言、多模态攻击）。可以考虑构建更大规模、多样化的越狱提示库。采用增量学习动态更新概念子空间，适应新型攻击。实验未考虑多轮越狱攻击（如对话上下文诱导），而当前方法仅针对单次输入检测。可以考虑设计黑盒适配方案。扩展至对话状态跟踪，引入时序概念分析。
* **计算效率与部署成本存在问题：** 每输入需两次SVD分解和层间表征操作，表18显示平均推理耗时增加0.05秒。关键层选择需预计算校准数据，对低资源设备不友好。用近似SVD可以加速矩阵分解。将概念子空间压缩为低秩矩阵，减少存储开销。概念操作依赖固定缩放因子δ，但表8显示：移除毒性概念增强时ASR升至12%，说明参数敏感性。自适应攻击可使GCG攻击ASR升至14%，表明了当前线性操作的脆弱性。设计自适应δ机制：根据概念激活强度动态调整。同时引入对抗训练：在概念空间中生成对抗样本优化鲁棒性。
* **探索概念纠缠理论：** 量化毒性/越狱概念与其他语义的耦合关系。结合人工神经网络：类比LLM概念激活与人脑语义处理机制。扩展防御框架理论，多模态防御，适配图文/音视频混合越狱攻击。采取跨模型协同，构建概念共享网络（如小型模型为大型模型提供概念锚点）

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