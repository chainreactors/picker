---
title: 【AI安全】Deepseek越狱? 利用MoE 架构的“物理缺陷”实施越狱
url: https://mp.weixin.qq.com/s/Fhtbvfu-bJ0y9Be_Xjlylw
source: Doonsec's feed
date: 2026-01-12
fetch_date: 2026-01-13T03:28:52.909806
---

# 【AI安全】Deepseek越狱? 利用MoE 架构的“物理缺陷”实施越狱

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/RBozUQPW9cibP2vAGtujLPjeE9cDM5ncvV4S8vBo2axuZCYXia0nYVuhQ19HljAmekffQVANgWBbicn6O1OIuE1JQ/0?wx_fmt=jpeg)

# 【AI安全】Deepseek越狱? 利用MoE 架构的“物理缺陷”实施越狱

原创

Oxo Security

Oxo Security

![]()

在小说阅读器中沉浸阅读

# 一、 什么是MoE？大模型的“分身术”与“专家门诊” 🏥🧠

先来个越狱效果图，完整提示词在第三章。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/RBozUQPW9cibP2vAGtujLPjeE9cDM5ncvlgKoEpYBdHNszyqarjEGctjxSbvLibBIpFcQicibWNJVDVRib3kSx6OKwA/640?wx_fmt=png&from=appmsg)

首先要搞清楚 MoE 到底是个什么鬼。它的全称是 **Mixture-of-Experts**，翻译成中文叫 **“混合专家模型”**。

想象一下，你开了一家超级巨大的咨询公司。早期的 AI 模型（我们叫它“稠密模型” Dense Model）就像是一个“全才”员工。不管客户问的是法律问题、装修建议还是量子力学，这个员工都要动用大脑里所有的细胞去思考，然后给你一个答案。虽然他很厉害，但有个致命缺点：**累啊！** 😫 而且每次问他问题，无论问题多简单，他都要消耗同样多的能量，这显然不科学。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/RBozUQPW9cibP2vAGtujLPjeE9cDM5ncvJTvvm9K5icWLqn3Yib6AFcDkbz52QebaicuZqxVqSibcZfLDgPaLBAWfew/640?wx_fmt=png&from=appmsg)

MoE 架构就不一样了，它把这家公司变成了一个 **“专家联盟”**。架构里包含两个核心组件：

1. 1. **专家（Experts）**： 公司里坐着成百上千个专门的“小团队”。有的专门搞数学，有的专门写代码，有的专门研究冷门文学。这些专家本质上是一个个功能相同、结构相似的子网络（在 Transformer 架构里，通常是替换了原来的前馈网络 FFN）。虽然他们底子一样，但在训练过程中，他们“卷”的方向不同，最终各自掌握了不同的技能。技能树点歪了没关系，只要在某个领域牛 X 就行。👨‍🔬👩‍💻🎨
2. 2. **路由（Router/Gating Network）**： 这就是公司的“前台经理”。每当有一个任务（比如一个 Token，也就是一个词元）进来，经理会先瞟一眼：“哟，这是个微积分题啊，送去给 3 号数学专家和 7 号逻辑专家处理。”路由器的任务就是计算分配概率，把任务精准地投递给最合适的几个专家。

**核心精髓：**MoE 让模型拥有了极其庞大的“总参数量”（比如总共 1 万亿参数），但在实际干活（推理或训练）的时候，只有一小部分参数（比如 100 亿）是激活状态的。这种 **“条件式计算”** 让大模型实现了“既要、又要、还要”——既要参数量大带来的高智商，又要推理成本低的性价比。💰✨

如果你想搞点“非法”研究，比如提示词注入或者“越狱”，MoE 的这种架构其实给了我们可乘之机。通过特定的引导，我们或许可以绕过那个负责“安全对齐”的专家，直接连接到那个“满腹经纶却口无遮拦”的纯知识专家。这就像是你买通了公司的经理，让他避开保安，直接带你去见那个掌握禁忌知识的老学究。🔓🤫

---

# 二、 为什么要使用MoE？打破“智商”与“算力”的死结 ⚡⚖️

在 AI 进化史中，MoE 的出现几乎是必然的。为什么大家现在都疯了一样往 MoE 靠拢？（比如传闻中的 GPT-4，以及公开的 Mixtral、DeepSeek-V3）。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/RBozUQPW9cibP2vAGtujLPjeE9cDM5ncvxibDKCotKbicvgQRA9QrKNo0Chdkh5pWNqfIKeyCK8Ye0LVxhrnIEjYg/640?wx_fmt=png&from=appmsg)

1. 1. **拒绝低效：把“通才”的浪费彻底终结** 🙅‍♂️ 传统的稠密模型太笨重了。不管你是问“1+1 等于几”还是“如何发射火箭”，它都要激活所有参数。这就像你为了切个西瓜，发动了一台航母上的激光拦截系统，电力耗费巨大，效率低得离谱。 研究发现，大模型里其实存在大量的**参数冗余**。如果你把一个稠密模型剪掉 30%-40% 的参数，它的表现几乎不受影响。MoE 则是从源头上解决了这个问题：**按需分配**。它将计算复杂度从 $O(N)$ 直接降到了 $O(k)$（N 是总专家数，k 是激活的专家数）。让无关的参数“睡觉”，让干活的参数“冲锋”。💤🔥
2. 2. **规模化的“加速器”** 📈 如果我们想让 AI 更聪明，最暴力的办法就是加参数。但参数加一倍，推理成本也翻倍，显存也爆表。MoE 允许我们构建出超大规模的模型，却不显著增加计算成本。你可以横向堆叠专家，只要路由器（Router）足够聪明，模型就能在保持相同推理延迟的情况下，拥有更深厚的“内功”。
3. 3. **专家特化：模块化的降维打击** 🛠️ 在 MoE 模型里，不同专家会逐渐形成“肌肉记忆”。翻译问题找语言专家，代码问题找编程专家。由于每个专家只处理自己擅长的数据子集，它的学习效率极高，避免了稠密模型中那种“什么都学，结果什么都平均化”的平庸现象。这种模块化优势，让模型在面对复杂、跨学科问题时，可以通过“专家会诊”的方式（比如 Top-2 路由，激活两个专家协作）给出更专业的答案。👨‍⚕️🤝👨‍🏫
4. 4. **动态解决问题的灵活性** 🌀 MoE 是一种动态计算。路由器在训练过程中会不断优化决策边界，学习哪些专家组合最有效。这意味着模型具备了一定的“自我调节能力”：遇到简单的任务，可能一个专家就搞定了；遇到难的任务，路由器会调度多个顶尖专家协同。这种根据输入难度自动调整“思考深度”的能力，是稠密模型望尘莫及的。

# 三、 硬核：利用 MoE 架构的“物理缺陷”实施越狱 🔓层级降维打击

🎯 **【LLM 漏洞挖掘与越狱实战】**

当安全对齐遇上模块化架构，MoE 的“路径稀疏性”是否成为了防御最薄弱的一环？如何利用“专家隔离”逻辑，诱导模型进入未经过滤的知识路径，实现真正的物理级越狱？

本章节披露的关于“元指令劫持”、“时空悖论攻击”等针对 MoE 架构的硬核越狱套路及实战 Prompt 示例，仅在 **Oxo AI Security 知识星球** 完整发布。加入星球，获取最及时的…

---

* • 📚 **AI 文献解读**：最前沿的 LLM 安全论文深度剖析。
* • 🐛 **AI 漏洞情报**：第一时间掌握主流大模型的 0-day 漏洞与越狱方式。
* • 🛡 **AI 安全体系**：从红队攻击到蓝队防御的全方位知识图谱。
* • 🛠 **AI 攻防工具**：红队专属的自动化测试与扫描工具箱。

🚀 立即加入 **Oxo AI Security 知识星球**，掌握AI安全攻防核心能力！

![](https://mmbiz.qpic.cn/sz_mmbiz_png/RBozUQPW9c86l9BKV2TcgrjKw8B41ge3ibibq5qqLoNW0aJYvEfAAibSfRgU74vleMaXJ2chff1d7sk5B7xHcI6iaA/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/RBozUQPW9c86l9BKV2TcgrjKw8B41ge30c1ib8vQunnAo8BIkojRnd5y8VoLeTxpl6czmSXAI91OxicJEaAibrGgA/640?wx_fmt=jpeg&from=appmsg)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/RBozUQPW9c98C8Gg5hFYTHHv2QrMvZ8foNQRgkoOLR2p0ulacK7KCmZxeoT0k1fQ99pTvK43Q3cMgPzabRkqiaQ/0?wx_fmt=png)

Oxo Security

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/RBozUQPW9c98C8Gg5hFYTHHv2QrMvZ8foNQRgkoOLR2p0ulacK7KCmZxeoT0k1fQ99pTvK43Q3cMgPzabRkqiaQ/0?wx_fmt=png)

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