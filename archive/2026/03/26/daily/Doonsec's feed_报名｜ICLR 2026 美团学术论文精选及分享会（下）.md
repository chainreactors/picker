---
title: 报名｜ICLR 2026 美团学术论文精选及分享会（下）
url: https://mp.weixin.qq.com/s/WDc3-A6MzvA6jT13XSG_4A
source: Doonsec's feed
date: 2026-03-26
fetch_date: 2026-03-27T04:29:16.817076
---

# 报名｜ICLR 2026 美团学术论文精选及分享会（下）

![cover_image](http://mmecoa.qpic.cn/sz_mmecoa_jpg/V95GN2mm0DzEgqXvbe5B7ltD8CYnb6Es4Vq4iaExuX6uzScPor8ew8kEYibyMnSTsgMJq6lYIkjhFHWM9b10TcEIbxsE0N1vG2umg2A0Hhx7I/0?wx_fmt=jpeg)

# 报名｜ICLR 2026 美团学术论文精选及分享会（下）

美团技术团队

![]()

在小说阅读器中沉浸阅读

![](https://mmecoa.qpic.cn/mmecoa_gif/V95GN2mm0DxF02oh3f8zbibSWYMLCzPmVictXGk8g5HrmictaJaWtoUycOw3e8vzDmrwl1koykr9XAxhyhj4HSRibGYB51eicRKMficichkOS5bjcg/640?wx_fmt=gif&from=appmsg)

点亮👆“☆”星标，不错过推送内容~

ICLR（International Conference on Learning Representations）是机器学习和人工智能领域最具影响力的年度学术会议之一，与 NeurIPS、ICML 并列为AI领域的三大顶级会议，特别聚焦于表示学习与深度学习的理论、算法和应用研究。

🎯 活动预告：我们刚刚直播了 ICLR 2026 论文分享会 ASX 专场的6篇论文解读，论文下载地址、直播沉淀的PPT和视频见下方。

4 月 9 日（周四）下午，我们将继续分享 ICLR 5篇论文（Main Conference）相关知识点和技术思考，[报名请点击这里](https://hdxu.cn/1GaY1)，文末还有详细信息。

![](https://mmecoa.qpic.cn/sz_mmecoa_png/V95GN2mm0DyKEfgicdibr8tKB77AGbJPlHYRfC8TMCrXlnRVLRLOvMcTiakQuhbOOQ52hrURMlFV7Fd5IGGcHBtMUAOVhtqSqAAXu6KYmPLlhE/640?wx_fmt=png&from=appmsg)

上期论文下载：[ICLR 2026 美团论文精选及分享会（上）——搜推 ASX 专场](https://mp.weixin.qq.com/s?__biz=MjM5NjQ5MTI5OA==&mid=2651782334&idx=2&sn=7953ce827cdd35a33f51669ad44467d0&scene=21#wechat_redirect)

上期直播沉淀：美团技术沙龙论文分享会：ICLR 2026 美团搜推 ASX 专场

## **01**

AMemGym: Interactive Memory Benchmarking for Assistants in Long-Horizon Conversations

AMemGym: 长程对话中的交互式记忆评测

论文类型：ICLR Main Conference

**论文下载**：[PDF](https://openreview.net/pdf?id=sfrVLzsmlf)

![](https://mmecoa.qpic.cn/sz_mmecoa_png/V95GN2mm0Dw2GXFicJbplPYbAQMUdQXFASiaSzBmU3ZibnAAHm1pX0icHlCSywEOLz1XEb1zsKpLIa0tNv07BHCPtNTWFByc2kqpV6Nk8T3yicjc/640?wx_fmt=png&from=appmsg)

论文简介：记忆是Agent实现泛化与适应动态环境的基础，也是通往AGI最具潜力的路径之一。然而，记忆的优化与评测均面临长程依赖建模的挑战：长程依赖数据的长尾稀缺性导致优化与评测的高成本。传统记忆评测方法为节约成本通常复用静态长文本问答（Long-context QA）数据，考察Agent对固定外部长输入的理解能力。这种评测方式偏离了真实多轮交互中记忆的动态特性，我们称之为离策略评测（off-policy evaluation）。在多轮长对话场景中，同策略评测（on-policy evaluation）则需要额外建模记忆读写对Agent输出、外部输入以及下一轮记忆读写的循环递归影响，对应更高的评测复杂度与成本。AMemGym通过结合用户模拟器与关联结构化数据，保证可靠性的同时有效控制了评测成本。

我们的对比研究表明，基于静态数据的离策略评测结果难以提供真实有效的对比与优化信号，尤其在复杂Agent系统中，存在显著的重用偏差（reuse bias）。此外，AMemGym 通过对记忆生命周期进行分解，提供了更细粒度的诊断与归因信号。同时，它可作为针对记忆机制的持续学习模拟环境，为验证长对话场景下的个性化能力自提升（self-improvement）算法提供了可靠的测试平台。

02

PosterCraft: Rethinking High-Quality Aesthetic Poster Generation in a Unified Framework

PosterCraft：统一框架下高质量美感海报生成的重构与探索

论文类型：ICLR Main Conference

**论文下载**：[PDF](https://openreview.net/pdf?id=GhqnOEXQh3)

![](https://mmecoa.qpic.cn/sz_mmecoa_png/V95GN2mm0DwfiaMmGIuQ14BtZlHWfXZxZnFicguMJvKNKicAI09mwc75dG1zyaEJ8BG93KlyL8gWD22ISbRFWlntFL3OYbJSoOiaZb9LwOdUly8/640?wx_fmt=png&from=appmsg)

论文简介：PosterCraft聚焦“高审美海报生成”这一更具挑战的设计任务：不仅需要高精度文字渲染，还要在抽象背景、版式布局与整体风格一致性之间实现统一。

为摆脱以往依赖模块化管线与固定版式规划的上限，作者提出统一生成框架，通过级联训练流程逐步释放基础模型能力：先用大规模Text-Render-2M进行文本渲染优化，再在HQ-Poster-100K上进行区域感知的高质量海报微调以平衡文本/非文本区域风格，随后基于偏好数据Poster-Preference-100K进行审美-文本强化学习，最后引入Poster-Reflect-120K与联合视觉-语言反馈实现迭代精修与更强一致性。

实验表明，该方法在文字准确性、布局连贯性与整体视觉吸引力上显著优于开源基线，并接近主流闭源系统的质量水平。该项目也开源至MeiGen-AI仓库：[PosterCraft](https://github.com/MeiGen-AI/PosterCraft)。

03

VitaBench: Benchmarking LLM Agents with Versatile Interactive Tasks in Real-world Applications

VitaBench：基于真实生活场景的交互式大模型智能体评测基准

论文类型：ICLR Main Conference

**论文下载**：[PDF](https://arxiv.org/abs/2509.26490)

![](https://mmecoa.qpic.cn/mmecoa_png/V95GN2mm0Dy57y37thd54PbbKShBLfWjRT2Rico8ibEso6vLTRNaP5bVC0Kh2qItLXPpFbKVibzVgHx5cEBwsTIbgYvv5BHbkjOTVE4o6WkILk/640?wx_fmt=png&from=appmsg)

论文简介：现有智能体评测基准与真实生活场景之间存在显著鸿沟：工具生态过于简单、信息密度不足、交互动态性缺失。我们提出 VitaBench，以外卖点餐、餐厅就餐、旅游出行三大高频生活场景为载体，首次将智能体任务复杂度系统拆解为推理、工具、交互三大维度进行量化建模。

VitaBench 构建了包含 66 个真实工具的交互式评测环境与有向依赖图，避免了传统基准依赖冗长 Policy 文档的局限，让模型通过工具描述自主推理领域逻辑。基准共包含 400 项任务（300 项单场景 + 100 项跨场景），每个任务配备差异化用户画像与行为属性，并通过基于 LLM 的用户模拟器动态驱动交互。针对长轨迹评估，我们提出基于 Rubric 的滑动窗口评估器，将任务目标拆解为原子化评估准则，实现细粒度的行为覆盖与可解释评估。

对 20 余款主流模型的评测结果显示：即便是最强的 o3（high）模型，跨场景任务成功率也仅为 30%。错误分析表明，推理错误占主导，揭示了当前智能体在多维信息整合、策略调度与自我反思方面的根本性短板。

04

Look Back to Reason Forward: Revisitable Memory for Long-Context LLM Agents

面向长上下文大模型智能体的可回访记忆

论文类型：ICLR Main Conference

**论文下载**：[PDF](https://arxiv.org/abs/2509.23040)

![](https://mmecoa.qpic.cn/mmecoa_png/V95GN2mm0DzupxOF7ehCKOkwNTNM31qFYicfXxG6VhSvNxZpiafibkVuh6dQxHdE1chqpNvroz2jvzLJJGoGFjibiaHcp10XTHayA7Vk2JicYrKxk/640?wx_fmt=png&from=appmsg)

论文简介：在长文本问答任务中，查询的关键证据往往散落于百万级的 Token 之中，这给大语言模型带来了严峻的挑战。现有研究通常为大语言模型引入记忆缓存机制，通过线性扫描文档来动态更新记忆，这类方法亦被称为“边读边记”（memorize while reading）法。尽管该方法具有出色的扩展效率，却面临着潜在证据被过早剔除、记忆覆盖导致信息丢失，以及强化学习信号稀疏等诸多弊端。

为攻克上述难题，我们提出了 ReMemR1 方法。该模型将记忆检索机制巧妙融入记忆更新过程，赋予智能体选择性调取历史记忆的能力，从而实现非线性推理。为进一步提升训练效果，我们设计了一种多层级奖励机制，将最终答案奖励与密集的步骤级信号相结合，以此引导模型对记忆的有效利用。上述创新齐头并进，有效缓解了信息衰减问题，提升了监督效能，并为复杂的多跳推理提供了有力支持。

大量实验表明，ReMemR1 在长文本问答任务上显著优于现有最佳（SOTA）基线模型，且带来的额外计算开销微乎其微，充分证实了其能够以极小的边际成本换取稳健的长文本推理能力。我们的代码已开源至GitHub：[ReMemR1](https://github.com/syr-cn/ReMemR1)。

05

Unveiling Super Experts in Mixture-of-Experts Large Language Models

揭示混合专家大语言模型中的超级专家

论文类型：ICLR Main Conference

**论文下载**：[PDF](https://openreview.net/forum?id=JYwGNKfPPp)

![](https://mmecoa.qpic.cn/mmecoa_png/V95GN2mm0DwBticNuP64VsIXtOXdMjxLOhJ4wAibHXfZBeTqric8qiaG9CSe94bvF5sB0MPmictAgKIziarv0nTy8xOicOf5yueGzn430k0joKbsF0/640?wx_fmt=png&from=appmsg)

论文简介：本研究首次发现并系统地研究了在混合专家大语言模型前向推理中发挥关键作用的一类特殊专家。这类专家在开源混合专家大语言模型中普遍存在，尽管其数量极其有限，但对其进行剪枝会导致模型性能显著下降（例如，在 6,144 个专家中仅剪掉 3 个，就会导致 Qwen3-30B-A3B 生成重复且无信息量的输出）。我们将这些专家称为“超级专家”（Super Experts，SE）。我们的全面分析对 SE 提供了逐步深入的理解：

* SE的特征是在 down\_proj 输出中出现罕见但极端的激活异常，这会在解码器层之间的隐藏状态中引发大规模激活。此外，SE 的分布具有模型特异性，与数据无关，并且不受训练后处理过程的影响。
* 通过对 SE 进行剪枝，我们评估了其在多种任务中的重要性，揭示了其对模型整体性能的显著影响，尤其是在数学推理任务中。
* 我们进一步研究了为何压缩 SE会产生如此显著的影响。结果表明，在 混合专家大语言模型 中，SE 是 Transformer 中系统性异常机制的主要来源，而对其进行压缩会深刻扰乱该机制，最终导致注意力汇（Attention Sinks）的崩溃。

---

活动预告

识别图上二维码或 [点击这里](https://hdxu.cn/1GaY1) 报名

![](https://mmecoa.qpic.cn/mmecoa_png/V95GN2mm0DyUR2wHOfhNNiahEChVVun0fibzegzzr22RyyFN5ghGiaEjzkUC054iaG1planxEQhlbe2dSJhLic3QibkwHBDuyaaQibtOZeibicZDEyzg/640?wx_fmt=png&from=appmsg)

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/hEx03cFgUsVGibnsaEib3aNlqF0tOrA2RGEmNSbia2nnohE4Tpf95UyTiaSjDVbHRfY8WNBeTuLLTaVdSckkNyEx1Q/0?wx_fmt=png)

美团技术团队

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/hEx03cFgUsVGibnsaEib3aNlqF0tOrA2RGEmNSbia2nnohE4Tpf95UyTiaSjDVbHRfY8WNBeTuLLTaVdSckkNyEx1Q/0?wx_fmt=png)

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