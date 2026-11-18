---
title: 绿盟科技风云卫基座模型斩获CyberGym Model榜单全球第一，91.31%！！！
url: https://blog.nsfocus.net/%e7%bb%bf%e7%9b%9f%e7%a7%91%e6%8a%80%e9%a3%8e%e4%ba%91%e5%8d%ab%e5%9f%ba%e5%ba%a7%e6%a8%a1%e5%9e%8b%e6%96%a9%e8%8e%b7cybergym-model%e6%a6%9c%e5%8d%95%e5%85%a8%e7%90%83%e7%ac%ac%e4%b8%80%ef%bc%8c91-31/
source: 绿盟科技技术博客
date: 2026-11-17
fetch_date: 2026-11-18T09:21:43.454503
---

# 绿盟科技风云卫基座模型斩获CyberGym Model榜单全球第一，91.31%！！！

* [技术产品](https://blog.nsfocus.net/category/technology-product/)
* [数智安全](https://blog.nsfocus.net/category/digital-intelligence-secuirty/)
* [威胁通告](https://blog.nsfocus.net/category/threat-alert/)
* [研究调研](https://blog.nsfocus.net/category/security-research/)
* [洞见RSA](https://blog.nsfocus.net/category/rsac/)
* [公益译文](https://blog.nsfocus.net/category/translation/)
* [安全分享](https://blog.nsfocus.net/category/security-sharing/)
* [登录](https://blog.nsfocus.net/wp-login.php)

* [首页](https://blog.nsfocus.net)
* [数智安全](https://blog.nsfocus.net/category/digital-intelligence-secuirty/)
* 绿盟科技风云卫基座模型斩获CyberGym Model榜单全球第一，91.31%！！！

# 绿盟科技风云卫基座模型斩获CyberGym Model榜单全球第一，91.31%！！！

[0](https://blog.nsfocus.net/%E7%BB%BF%E7%9B%9F%E7%A7%91%E6%8A%80%E9%A3%8E%E4%BA%91%E5%8D%AB%E5%9F%BA%E5%BA%A7%E6%A8%A1%E5%9E%8B%E6%96%A9%E8%8E%B7cybergym-model%E6%A6%9C%E5%8D%95%E5%85%A8%E7%90%83%E7%AC%AC%E4%B8%80%EF%BC%8C91-31/#comments)

![](https://secure.gravatar.com/avatar/99bcec439a2a5078218073d2459e8069eb89b5ce5cbf840afef1c3ed7395d75c?s=40&d=identicon&r=g) [NSFOCUS](https://blog.nsfocus.net/author/zhengfangying/ "written 2026-11-1717:59") 发布于 23 小时前

![](https://blog.nsfocus.net/wp-content/uploads/2026/11/奖杯4-scaled.png)

阅读： 44

绿盟科技**风云卫基座模型（SecLLM-3.6-27B）** ，在CyberGym Model榜单（Model-Focused） 中**以91.31%的任务成功率位列全球第一。**

![](https://p3-sign.toutiaoimg.com/tos-cn-i-axegupay5k/55d337e20ad74e3d9fa1a5375800f8c4~tplv-tt-origin-web:gif.jpeg?_iz=58558&from=article.pc_detail&lk3s=953192f4&x-expires=1795514231&x-signature=agPEY1MkOF5p3pBpL1TLBlSV1zg%3D)

需要首先说清楚的是：这是一个**纯模型榜单**。CyberGym Model-Focused的规则是**只使用通用Harness，不设固定阶段，不挂任何外部工具与知识库，不依赖专门的智能体设计**，纯粹衡量模型自身的底层安全能力。换句话说，这个91.31%，是模型“赤手空拳”打出来的。

# 先分清两个榜单：Model测“模型本身”，Agent测“系统战力”

CyberGym由加州大学伯克利分校提出，是当前AI安全攻防领域公认的“黄金标准”。它在排行榜上刻意区分了两类条目：

* **Model-Focused（模型导向）：**实验室在标准、通用的Harness下报告单个模型的成绩。工具、流程、外部知识库一律不加，目的就是**评估模型的内在安全能力**，排除工程编排带来的加成。
* **Agent-Focused（智能体导向）：**团队构建自己的完整系统，通常包含多个模型、定制工具链、含漏洞的Docker环境，甚至运行时动态更新的知识库。比拼的是**系统级攻防战力**，模型只是其中一个部件。

分开评测的意义在于**把“模型能力”和“系统工程能力”解耦**。两个榜单回答的是不同问题：Model榜单回答“这个模型本身有多强”，Agent榜单回答“这支团队搭出来的系统有多能打”。混在一起比，既对纯模型不公平，也会让选型者分不清高分到底来自模型，还是来自外挂。CyberGym官方指引对此有明确界定：model-focused评测**不依赖专门智能体设计，**测的就是模型自身的能力基底。

SecLLM-3.6-27B登顶的是**Model榜单**。这意味着它不需要靠外挂工具、预置阶段或知识库来“补课”，模型自身的漏洞理解、代码推理、证据判断和失败恢复能力，已经站到了全球第一的位置。

# 从54.51%到91.31%：参数虽小，硬仗照打

![](https://p3-sign.toutiaoimg.com/tos-cn-i-6w9my0ksvp/a042067ad864441faa4470f50a224b2a~tplv-tt-origin-web:gif.jpeg?_iz=58558&from=article.pc_detail&lk3s=953192f4&x-expires=1795514231&x-signature=3zbnnPUF%2BVtihzt%2Bu5gbeKNo0TI%3D)

36.80个百分点的跃升，不是参数规模的胜利。SecLLM-3.6-27B采用**“安全能力拆解与专业化增强”**训练策略，不要求模型直接复现完整长轨迹，而是训练它在数十至数百步的任务状态中，持续做出**证据驱动、可恢复的局部决策**：漏洞理解、代码审计、漏洞定位、可利用性分析、PoC构造、漏洞验证、失败诊断、策略修正，逐项拆开训练，再在长程任务中串起来。

具体训练路径包括：约316B Token安全垂域持续预训练（CPT）；约420万条高质量安全任务监督数据，外加约31万条状态感知长链路轨迹数据，将长程任务拆解为“当前安全状态 + 当前子目标 + 已确认事实与证据 + 已失败路径与约束 → 下一步推理或动作”的连续局部决策；多教师在线策略蒸馏（MOPD） 在Student自身rollout的关键状态上引入多Teacher互补监督，重点修正证据判断、路径选择和失败恢复上的长尾错误；以及可验证反馈与失败感知训练，把编译结果、崩溃行为、PoC触发情况直接转化为训练信号，让每一次失败都成为下一次决策的依据。

# 为什么做27B：小参数垂域模型是安全落地的“甜点”

选择27B，不是退而求其次，而是面向真实安全场景的主动取舍。

出于成本和合规考虑，网络安全部门需要一个小参数量的本地化模型来支撑安全运营工作，27B量级的模型可以部署在单机多卡甚至高性能工作站上，推理成本与超大模型相差一到两个数量级，并且可以有效应对网络安全场景下高频、常态化的安全任务，目前SecLLM已通过风云卫在告警降噪、漏洞初筛、代码审计辅助、事件溯源等多个安全场景交付落地，取得良好效果。

与此同时，小参数不等于低能力。CyberGym Model榜单已经反复证明，27B级模型经过深度的安全垂域训练和智能压缩，可以在真实漏洞任务上逼近甚至超越参数量大出数十到数百倍的通用模型。绿盟SecLLM-3.6-27B的路径正是如此：把有限的参数集中投放到安全领域最需要的能力密度上，**用垂域深度替代通用广度**，在专业战场上实现“小参数、高智能”。

# 关于CyberGym

CyberGym 是由加州大学伯克利分校提出的 AI 智能体网络安全实战测评基准，被业界视为衡量 AI 安全攻防能力的”黄金标准”。其题库包含来自 188 个主流开源项目的 1507 个真实已修复漏洞（主要聚焦 C/C++ 内存安全问题）。赛制要求 AI 智能体仅凭漏洞描述和未修补代码库，自主完成漏洞理解、定位、复现及 PoC 生成全流程，并通过自动化评审严格验证 PoC 是否可稳定触发目标漏洞。该榜单被 Anthropic、微软、Wiz 等视为关键标尺，是当前全球覆盖最广、认可度最高的 AI 安全实战测评体系。

最后修改日期: 2026-11-17

### 作者

![](https://secure.gravatar.com/avatar/99bcec439a2a5078218073d2459e8069eb89b5ce5cbf840afef1c3ed7395d75c?s=96&d=identicon&r=g)

[NSFOCUS](https://blog.nsfocus.net/author/zhengfangying/)

## 最新发布

* [绿盟科技风云卫基座模型斩获CyberGym Model榜单全球第一，91.31%！！！](https://blog.nsfocus.net/%E7%BB%BF%E7%9B%9F%E7%A7%91%E6%8A%80%E9%A3%8E%E4%BA%91%E5%8D%AB%E5%9F%BA%E5%BA%A7%E6%A8%A1%E5%9E%8B%E6%96%A9%E8%8E%B7cybergym-model%E6%A6%9C%E5%8D%95%E5%85%A8%E7%90%83%E7%AC%AC%E4%B8%80%EF%BC%8C91-31/)
* [绿盟科技护航首艘内河航运电动船成功试航](https://blog.nsfocus.net/%E7%BB%BF%E7%9B%9F%E7%A7%91%E6%8A%80%E6%8A%A4%E8%88%AA%E9%A6%96%E8%89%98%E5%86%85%E6%B2%B3%E8%88%AA%E8%BF%90%E7%94%B5%E5%8A%A8%E8%88%B9%E6%88%90%E5%8A%9F%E8%AF%95%E8%88%AA/)
* [Apache HTTP Server远程代码执行漏洞（CVE-2026-119618）通告](https://blog.nsfocus.net/apache-http-server%E8%BF%9C%E7%A8%8B%E4%BB%A3%E7%A0%81%E6%89%A7%E8%A1%8C%E6%BC%8F%E6%B4%9E%EF%BC%88cve-2026-119618%EF%BC%89%E9%80%9A%E5%91%8A-2/)
* [Apache HTTP Server远程代码执行漏洞（CVE-2026-119618）通告](https://blog.nsfocus.net/apache-http-server%E8%BF%9C%E7%A8%8B%E4%BB%A3%E7%A0%81%E6%89%A7%E8%A1%8C%E6%BC%8F%E6%B4%9E%EF%BC%88cve-2026-119618%EF%BC%89%E9%80%9A%E5%91%8A/)
* [首批 | 绿盟科技正式获评首批国家人工智能安全漏洞库（AIVD）技术支撑单位](https://blog.nsfocus.net/%E9%A6%96%E6%89%B9-%E7%BB%BF%E7%9B%9F%E7%A7%91%E6%8A%80%E6%AD%A3%E5%BC%8F%E8%8E%B7%E8%AF%84%E9%A6%96%E6%89%B9%E5%9B%BD%E5%AE%B6%E4%BA%BA%E5%B7%A5%E6%99%BA%E8%83%BD%E5%AE%89%E5%85%A8%E6%BC%8F/)

## 文章导航

[上一篇文章 绿盟科技护航首艘内河航运电动船成功试航](https://blog.nsfocus.net/%E7%BB%BF%E7%9B%9F%E7%A7%91%E6%8A%80%E6%8A%A4%E8%88%AA%E9%A6%96%E8%89%98%E5%86%85%E6%B2%B3%E8%88%AA%E8%BF%90%E7%94%B5%E5%8A%A8%E8%88%B9%E6%88%90%E5%8A%9F%E8%AF%95%E8%88%AA/)

著作权 © 2026 **[绿盟科技技术博客](https://blog.nsfocus.net/)**. 保留一切权利。 本站采用的布景主题为 [Mynote](https://terryl.in/).