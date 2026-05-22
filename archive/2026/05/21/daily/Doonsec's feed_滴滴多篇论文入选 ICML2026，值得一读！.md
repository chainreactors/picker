---
title: 滴滴多篇论文入选 ICML2026，值得一读！
url: https://mp.weixin.qq.com/s/cBQnS-ThQgLLc12flLW8ug
source: Doonsec's feed
date: 2026-05-21
fetch_date: 2026-05-22T05:59:29.195892
---

# 滴滴多篇论文入选 ICML2026，值得一读！

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1kYDdPrxHSpfHzU761xz4LlZb8eLoKQYSKrWIMmUYE272EY6cuYQ8qkHVaEgE7PEMs6eRvN177PPiaNdtgeLr4JK6bPiaExliayQzBhS18F0p8/0?wx_fmt=jpeg)

# 滴滴多篇论文入选 ICML2026，值得一读！

滴滴技术

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

**近日，机器学习与人工智能领域国际顶会 ICML 2026 录用结果正式揭晓，滴滴共有五篇高质量学术成果被大会收录。本次中稿论文分别来自滴滴L Lab团队、滴滴网约车交易市场技术团队，与中山大学、香港科技大学（广州）、北京大学、上海财经大学等高校联合研发完成。未来，滴滴将继续深耕业务场景，让前沿探索与产业需求相互激发，与学界携手推动更多技术成果落地。**

国际机器学习大会（International Conference on Machine Learning，简称 ICML）是机器学习领域最具影响力的顶级学术会议之一，同时也是中国计算机学会（CCF）推荐的 A 类国际学术会议。第 43 届 ICML 会议将于 2026 年 7 月 6 日-11 日在韩国首尔举行。本届 ICML 会议共收到 23918 份提交论文，其中 6352 篇论文被录用，526 篇被选为 Spotlight Paper。

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/1kYDdPrxHSoZneGvMHE67AKHMzVcv3EsFUbCfzkSjYnWPqkKu3rNDtp9gTUg6dgicrCfz8iapibkQrhicVFwy3rjvSDwKCzhQGzGlyeStqdcgR4/640?wx_fmt=gif&from=appmsg)

**中稿论文如下**

（\*排名不分先后）：

**论文一：**

UltraHorizon: Benchmarking LLM-Agent Capabilities in Ultra Long-Horizon Scenarios

**作者：** Haotian Luo, Huaisong Zhang, Xuelin Zhang, Haoyu Wang, Zeyu Qin, WenJie Lu, Guozheng Ma, Haiying He, Yingsha Xie, Qiyang Zhou, Zixuan Hu, Hongze Mi, Yibo Wang, Naiqiang Tan, Hong Chen, Yi R. Fung, Chun Yuan, Li Shen

**研究团队：**滴滴 L-Lab × 中山大学

**研究方向：**大模型智能体评估基准 / 长周期（Long-Horizon）任务推理、规划与工具使用

**论文下载链接：https://arxiv.org/pdf/2509.21766**

**论文介绍：**现有的自主智能体评估未能涵盖现实世界中那些需要持续推理、记忆管理和工具调用的长周期且部分可观察的复杂任务。为了填补这一空白，我们提出了一个全新的跨环境探索基准测试，其特点是具有极长的智能体交互轨迹、极高的Token消耗量和频繁的工具调用。

广泛的实验表明，当前最先进的智能体在这些任务中表现远不如人类，且无法通过简单的扩大规模来提升，其失败的主要原因在于上下文锁定（in-context locking）和基础能力的缺失。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1kYDdPrxHSq94es5JTHZgJtTHNxpa5Y2Z0NBvZqa9JP3DWm3o6J36JibA3p6vuRMlNfse3L9KoVNuU1cKH2x8mHWqODcNLI6IB9xCphoP1x4/640?wx_fmt=png&from=appmsg)

**论文二：**Darwinian Memory: A Training-Free Self-Regulating Memory System for GUI Agent Evolution

**作者：**Hongze Mi, Yibo Feng, WenJie Lu, Song Cao, Jinyuan Li, Yanming Li, Xuelin Zhang, Haotian Luo, Songyang Peng, He Cui, Tengfei Tian, Jun Fang, Hua Chai, Naiqiang Tan

**研究团队：**滴滴 L-Lab

**研究方向：**多模态大模型（MLLM）智能体 / GUI 自动化 / 自进化记忆系统

**论文下载链接：https://arxiv.org/pdf/2601.22528**

**论文介绍：**为了克服多模态大语言模型（MLLM）在复杂GUI自动化中的记忆与上下文限制，我们提出了达尔文记忆系统（DMS），该自进化架构利用效用驱动的“自然选择”机制来动态分解任务并淘汰次优策略。

通过将记忆构建为一个不断进化的生态系统，DMS在无需任何额外训练的情况下，显著提升了MLLM智能体的任务成功率、执行稳定性与效率。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1kYDdPrxHSrgC5pFZ99DKQ6G2UwLFK4OX8fZoA1MQdDA49wf5hjcKUUH3d3gZVTDAo13UAibXxRAl5JAymmbvqWwGibVnKyJ6Q4Ussb9oP1J8/640?wx_fmt=png&from=appmsg)

**论文三：**HTAC: Hierarchical Task-Aware Composition for Continual Offline Reinforcement Learning

**作者：**Qiyang Zhou，Ruihang Xu，Peng Wang，Wenjie Lu，Xiaochun Cao，Naiqiang Tan，Li Shen

**研究团队：**滴滴 L-Lab × 中山大学

**研究方向：**持续离线强化学习（Continual Offline RL） / 跨任务知识迁移与隔离 / 层次化任务表示

**论文介绍：**为了克服持续离线强化学习（CORL）在任务异质性下的知识复用与隔离难题，我们提出了层次化任务感知组合方法（HTAC），该方法通过双层任务编码与软组合机制，将任务解耦为域级与任务级嵌入，并借助按需创建的专家网络与注意力式知识整合实现参数高效的知识隔离与复用。在离线持续世界基准上，HTAC兼顾了可塑性与稳定性，显著提升了智能体的跨任务泛化与知识迁移能力。

![](https://mmbiz.qpic.cn/mmbiz_png/1kYDdPrxHSrpHGQO2DBFdqhgAt49siaxx5c5AG5wMsMY3uwbH8HX10ia5mqicfBK1c1zzEIK6aOkJHtWx9hMH2XkIQloibKcTkENVa8QZ2jfL7Q/640?wx_fmt=png&from=appmsg)

**论文四：**Agent-Omit: Adaptive Context Omission for Efficient LLM Agents

**作者：**Yansong Ning, Jun Fang, Naiqiang Tan, Hao Liu

**研究团队：**滴滴 L-Lab  × 香港科技大学（广州）

**研究方向：**大语言模型智能体

**论文下载链接：https://arxiv.org/pdf/2602.04284v2**

**论文介绍：本文提出Agent-Omit框架，用于提升大语言模型智能体在多轮交互中的执行效率。现有方法通常对思考过程与环境观察进行统一压缩，未考虑不同交互轮次的效用差异。**

**本文通过定量分析证实，智能体在交互中间轮次产生的思考与观察信息存在大量冗余，可在不降低任务效果的前提下安全省略。Agent-Omit 采用两阶段训练：先基于冷启动数据微调，让模型掌握省略行为规范；再通过省略感知的智能体强化学习，结合双采样机制与专属奖励，实现自适应省略冗余内容。**

**理论分析表明，该省略策略的偏差受 KL 散度上界约束。在五大智能体基准测试中，Agent-Omit-8B 性能比肩前沿大模型，且显著降低 token 开销，实现效果与效率的最优平衡。**

**![](https://mmbiz.qpic.cn/mmbiz_png/1kYDdPrxHSpclmmibUbzhoZJjuK1EuSRFOXwGyvhsCpc53R9NznmJNd0vZ32mm9u6Gs6OVwTTBu2tPNhR2IXDDTU5MccN3X9cy9A3ibcAFPv8/640?wx_fmt=png&from=appmsg)**

**论文五：**Feasible Fusion: Constrained Joint Estimation under Structural Non-Overlap（结构性重叠缺失下带约束的联合估计范式）

**作者：**Yuxi Du, Zhiheng Zhang, Haoxuan Li, Cong Fang, Jixing Xu, Zhen Peng, Jiecheng Guo

**研究团队：**滴滴网约车交易市场技术 × 北京大学、上海财经大学

**研究方向：**因果推断

**论文下载链接：https://arxiv.org/pdf/2602.22612**

**论文介绍：现代大规模营销场景中因果推断正面临日益严峻的挑战，这些挑战包括高维协变量（high-dimensional covariates）、多值处理（multi-valued）、大规模观察性数据，以及由于成本约束而数量有限的随机对照试验样本。**

**本文对由处理机制诱发的结构性非重叠进行了形式化刻画，并证明：在这一情形下，常用的加权融合方法在理论上无法满足随机化识别约束。为应对这一问题，本文提出了一种受约束的联合估计框架：在最小化观察数据风险的同时，通过正交的实验矩条件来保证因果有效性。进一步地，我们表明，结构性非重叠会在原始协变量空间中对矩约束的施加构成一种可行性障碍。在方法上，本文推导出一种带惩罚项的原始—对偶算法，用于联合学习表征与预测器，并将误差分解为重叠恢复误差、矩违背误差以及统计误差三部分。**

大量合成实验表明，该方法在不同程度的非重叠情形下均表现出稳健性能。与此同时，在一个滴滴大规模网约车应用场景中的实验进一步显示，本文方法相较于现有基线方法取得了显著提升，其效果可与使用显著更多 RCT 数据训练得到的模型相仿。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1kYDdPrxHSqg12rbZFGeGtQw7f58qXT0D1QKggOlIbmkMYuVSJJjZHYAXbYnxzoQDRqacOe1hckhmytZB5YIg6riayicrXzhA1VWY6Ss4icvTQ/640?wx_fmt=png&from=appmsg)

- End -

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/1wBZCGiaYqBHxH4cCwCOochEJ8ekFkaFCpZPtJBXXibYk1vt31HhZ7McAeVAryqYqUickFl10bkD5Q7922uSgGEhg/0?wx_fmt=png)

滴滴技术

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/1wBZCGiaYqBHxH4cCwCOochEJ8ekFkaFCpZPtJBXXibYk1vt31HhZ7McAeVAryqYqUickFl10bkD5Q7922uSgGEhg/0?wx_fmt=png)

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