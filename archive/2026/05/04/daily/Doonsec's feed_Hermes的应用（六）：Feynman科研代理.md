---
title: Hermes的应用（六）：Feynman科研代理
url: https://mp.weixin.qq.com/s/Gcf2KfvOVU4APegzzAIjSQ
source: Doonsec's feed
date: 2026-05-04
fetch_date: 2026-05-05T04:56:41.068920
---

# Hermes的应用（六）：Feynman科研代理

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/2PhZXrB0gN5GeaiaY1ThbJibInmiaFJ8DtrSbIEtmzCTdMul43bBHWTrbWN1UfXrWJ2YpkvnCbxFWygiaXH4CLktbqoLlZiag3AGtFGrzaVKCDZc/0?wx_fmt=jpeg)

# Hermes的应用（六）：Feynman科研代理

原创

MicroPest
MicroPest

MicroPest

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

Feynman，**一个开源的AI研究智能体 (AI research agent)，俗称【科研代理】。它由四个AI智能体（研究员、评审员、撰写员、核实员）组成，能自动进行文献综述、论文审计、实验复现等复杂的科研任务。**

**一、出题**

**在Hermes中安装好此项技能。给它出题：**

**题目：“稀疏自编码器（Sparse Autoencoders）提取的 LLM 特征是否真正可解释？——对 Anthropic、DeepMind、OpenAI 三家方法论的横向审计”。**

**根据用户提问，利用Hermes 与 Feynman**

**│**

**├── Researcher 规范激活 → 搜索三家论文、GitHub 开源库、技术博客**

**│**

**├── Reviewer 规范激活 → 在发现每篇论文时即开始评估方法学缺陷**

**│**

**├── Writer 规范激活 → 实时构建结构化证据表（三家方法论 × 可解释性维度）**

**│**

**└── Verifier 规范激活 → 边收集边验证引用链接的有效性**

**结果：预期的输出结构，一份完整的横向审计报告，包含：**

**三家方法论对比矩阵（Researcher + Writer 协作）**

**可解释性共识与分歧地图（Researcher + Reviewer 协作）**

**开源代码与论文声明的一致性审计（Verifier 主导）**

**剩余开放问题与技术债务（Reviewer + Writer 协作）**

****二、Hermes和Feynman给出的结果****

![](https://mmbiz.qpic.cn/mmbiz_png/2PhZXrB0gN65zGQfqw8zXicJWrfQw7LCAlWf9ckSu4jm6ibXJuwGXq5WM1IAAmtWqlFPw4QFNVDqH3VvO8Picruu4mPZGHFdwTozYbLwHDdKhU/640?wx_fmt=png&from=appmsg)

****通过：****

1. 执行摘要

2. 数据收集过程

3. Anthropic 方法论详述

4. DeepMind 方法论评估

5. OpenAI 方法论评估

6. 三家方法论对比矩阵

7. 共识与分歧

8. 代码 vs 论文一致性审计（Anthropic）

9. 遗留问题与技术债

10. 结论：审计表明，Anthropic 在稀疏自编码器可解释性领域处于领先且唯一系统化的地位，其方法论、开源实现、评估体系均完备；DeepMind 与 OpenAI 目前未公开同等规模的 SAE 项目，可能选择了不同的可解释性路径。未来应关注 SAE 的自动化评估、效率优化及跨模型迁移能力。

三、四个智能体是如何工作的

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2PhZXrB0gN6Q0ZQwPOxEL8IabrvCwHsAgecwCYOCzGaf1CFw0NwwS6N3rw5A0Y0RHC8vyUbtslVFjzhQpBblCf6xXly50ngdibgXlqeGpicFA/640?wx_fmt=png&from=appmsg)

Feynman 四代理系统是一个高度专业化、面向科研工作流的多智能体协作框架。四个智能体各司其职，通过文件而非消息进行数据交换，确保职责分离、可追溯和质量可控。

1. Researcher（研究员）

    角色定位：证据收集者，不进行分析或结论，只负责从多种来源（学术论文、网页、代码仓库）检索、筛选和组织信息。

2. Reviewer（评审员）

    角色定位：模拟严格的同行评审，评估证据质量、方法论严谨性、逻辑一致性，为后续撰写提供修改意见。

3. Writer（写作者）

    角色定位：将研究笔记转化为连贯、结构化、学术风格的文本。

4. Verifier（验证员）

    角色定位：质量门控，确保交付物的正确性、完整性、可信度，防止未验证声明流入最终输出。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2PhZXrB0gN5ZMCVvtBvxmpvaNDZyBx7yeqgnbYOmhcOYAsyN9VzMzHiady1cWzic2oPmLHQAx8pxF2b5pdGLrsO8K2JcAu1XyjahR9YZicF7ibg/640?wx_fmt=png&from=appmsg)

四、定位

Feynman 框架明确以科研产出为目标，强制遵循 IMRaD 结构、引用溯源、同行评审、事实验证，这些正是学术写作的核心流程。相比于通用 LLM agent，它更像一个“科研生产线”——每个环节都有质检，最终产品的可信度大幅提升。

    但更精确的说法是：Feynman 是一套科研工作流编排框架，其四个 agent 共同构成了一个完整的科研代理系统。 单个 agent 单独存在时并不具备完整科研能力；必须组合使用才能发挥价值。

    💎 总结

    Feynman 代表了科研自动化的重要方向：通过角色分离与强制验证来降低错误率。如果你的任务需要高可信度、可复现、有完整来源链（如本次稀疏自编码器横向审计），Feynman 是最佳选择。如果只是简单查询或快速写作，它可能略显笨重。

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/2hnvgPYNzpI857XC5Kft3W5TyR4cickrqaIUibKveibjF4531l9HGGu8dISFz0Yr6OUkCHfulChWC2acVmh4b39dg/0?wx_fmt=png)

MicroPest

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/2hnvgPYNzpI857XC5Kft3W5TyR4cickrqaIUibKveibjF4531l9HGGu8dISFz0Yr6OUkCHfulChWC2acVmh4b39dg/0?wx_fmt=png)

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