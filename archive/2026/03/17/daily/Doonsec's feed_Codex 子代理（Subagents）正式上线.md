---
title: Codex 子代理（Subagents）正式上线
url: https://mp.weixin.qq.com/s/NAd_w_k8yf4MNZXB2VlH0g
source: Doonsec's feed
date: 2026-03-17
fetch_date: 2026-03-18T04:19:45.322859
---

# Codex 子代理（Subagents）正式上线

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/A79OztZnWVkJWHJABGHmY8fGvk9kcDV7bpiciaqiawicVWzOOtKZVVg2uSswDxzdKJA8N8gGSKKohRDoGqNGd6GDQXgFj4gwW2GBlxHJQelKKQs/0?wx_fmt=jpeg)

# Codex 子代理（Subagents）正式上线

原创

AGI患者
AGI患者

云晞科技Sec

![]()

在小说阅读器中沉浸阅读

# Codex 子代理（Subagents）正式上线：AI 解 CTF 的时代要变天了

> 当 AI 学会了「分工协作」，CTF 竞赛的格局正在被悄然改写。

---

![](https://mmbiz.qpic.cn/mmbiz_jpg/A79OztZnWVkDiakbIiawbdtFmc7MsIUAd5bISIZO0nPUJiamRzm9OV61KmJu4jCHucGtlfAsGVIyFrlBCEc4oRm805yPDFEowQPwQmESuFT3AQ/640?wx_fmt=jpeg&from=appmsg)

## 一、一个长期存在的痛点

做过 CTF 的人都知道，一道综合题的解题流程往往是漫长的链式作业。以密码学方向为例：你需要先识别加密算法，再分析密文结构，接着尝试密钥推导，最后才能执行解密拿到 flag。逆向工程更不用说——从二进制反编译、控制流分析、反混淆、到定位关键逻辑并编写 exploit，每一步都高度依赖前一步的输出。

过去用 AI Agent 做这些事，不管是 Claude Code 还是 Codex，本质上都是**单线程作业**：一个 Agent 走完全部流程。探索笔记、测试日志、栈回溯信息不断堆积，上下文窗口被噪声淹没，Agent 的推理质量随之肉眼可见地滑坡。

这个问题，OpenAI 刚刚给出了一个极具说服力的答案。

## 二、Subagents：一个大脑，一支团队

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/A79OztZnWVlib3F8GicdI7TM5v3gPLFtJz67p3NmiagA8BicZnLdzNbygQS9ia5829ADIN0JCrmBjSXO37icVsHRLYib62UdaIMDQlY2IAupy63eAA/640?wx_fmt=jpeg&from=appmsg)

Codex 最新发布了**子代理（Subagents）**功能。核心思路简洁有力——不再让一个 Agent 单打独斗，而是由主代理（Main Agent）根据任务需求，**派生多个专业化子代理并行工作**。每个子代理拥有独立干净的上下文，各自完成分配到的子任务后，再将精炼的结果汇报给主代理进行最终综合。

打个比方：过去是一个全栈工程师从前端写到后端、从测试写到部署；现在是一个技术总监坐镇指挥，前端、后端、测试各有专人负责，最后由总监把所有人的成果整合交付。

**上下文不再是瓶颈，每个子代理都在一张白纸上工作。**

官方给出的使用方式非常直观，你甚至不需要做任何复杂配置，直接在 prompt 中描述你的分工需求即可。比如：

> "Review this branch with parallel subagents. Spawn one for security risks, one for test gaps, one for maintainability. Wait for all three, then summarize."

Codex 会自动派生 3 个子代理同时工作，各自从不同维度审查代码，最后由主代理汇总出一份干净的综合报告。

## 三、模型选择与推理强度：精细化的调度能力

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/A79OztZnWVms0eqH6iclMTJeIASpkFEVBalTTaib3APjFLrXicNQiczzA2QXl0ia50ES7OOzwW6zYnTibBnb8r0dZKfFPjWxsx3HSD9ich2FjGibzIA/640?wx_fmt=jpeg&from=appmsg)

Subagents 真正有意思的地方在于，你可以为不同子代理指定不同的模型和推理强度：

**gpt-5.4** 适合作为主代理，负责复杂逻辑判断、歧义消解和最终决策；**gpt-5.3-codex-spark** 则为速度优化，适合用于执行扫描、探索和快速摘要的工作代理。推理强度也可以分档控制——high 用于复杂边界分析，medium 作为默认平衡点，low 则在速度优先的场景下使用。

一个典型的调度模式是：主代理使用 gpt-5.4 + high reasoning 坐镇决策，同时派出 3 个 spark 子代理以 low reasoning 并行扫描代码库，快速收集信息后交由主代理深度分析和综合。

![](https://mmbiz.qpic.cn/mmbiz_jpg/A79OztZnWVkXvV52hjJJuAhnvPZpGlUHX7onSibZ8xqBbDsLxqnxQ0A19qT4oM78XKdicPc3Qo8u2lyZeMmaCYE0BfLFrDXUFVCQDgKGo7zSk/640?wx_fmt=jpeg&from=appmsg)

Codex 还内置了三种开箱即用的代理类型：**default**（通用型）、**worker**（执行型，偏向实现任务）、**explorer**（探索型，偏向阅读和扫描）。如果这些还不够，你可以在项目的 `.codex/agents/` 目录下用 TOML 文件定义完全自定义的代理：

```
name = "security-reviewer"
description = "Scans for security vulnerabilities"
developer_instructions = "Focus only on security risks. Report findings clearly."
model = "gpt-5.3-codex-spark"
model_reasoning_effort = "high"
```

## 四、当 Subagents 遇上 CTF：质变正在发生

现在让我们回到 CTF 的语境中，看看 Subagents 到底意味着什么。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/A79OztZnWVnGNROlP51ChcLMdLxAclOWB3tEHXRw09Eh5sj6pJM3bicqR4lvUmZxp7KG2bzZ2QghxhfpyZxCesibbRQho6fMzoWeCPzx7sIJ8/640?wx_fmt=png&from=appmsg)

### 密码学方向

过去一个 Agent 要完成的链路是：识别算法 → 分析密文结构 → 推导密钥 → 执行解密。这条链路上每一步都在消耗上下文窗口，后期 Agent 往往已经"忘了"前期的关键发现。

有了 Subagents，主代理可以这样调度：

* **子代理 A（Explorer）**：专注识别加密算法类型，扫描已知密码学特征
* **子代理 B（Worker）**：并行对密文结构进行统计分析，寻找规律
* **子代理 C（Worker）**：基于前两者的发现，尝试密钥空间搜索或已知攻击向量
* **主代理**：综合所有子代理的结果，做出最终判断并执行解密

每个子代理的上下文都是纯净的，不会被其他任务的日志噪声污染。

### 逆向工程方向

逆向题更是 Subagents 的理想战场。一个复杂的逆向题可以被分解为：

* **子代理 A**：反编译并分析程序控制流
* **子代理 B**：识别反调试和混淆技术
* **子代理 C**：定位关键验证逻辑和 flag 校验函数
* **主代理**：汇总分析结果，编写最终的 exploit 或 keygen

在过去的单 Agent 模式下，光是把一个大型二进制文件的反编译输出塞进上下文就已经捉襟见肘了。而现在，每个子代理只需要关注自己负责的那一块，分析深度和准确率都大幅提升。

### Pwn / Web / Misc 方向

思路类似——任何可以拆解为独立子任务的方向都能受益。Web 题中，一个子代理扫描端点和参数，一个分析鉴权逻辑，一个寻找注入点；Pwn 题中，一个分析保护机制，一个寻找漏洞原语，一个构造 ROP 链。

**核心原则是：如果工作可以被拆分为独立的模块，Subagents 就是正确的工具。**

## 五、Subagents + Skills：AI 解 CTF 的绝对优势

如果说 Subagents 解决了「协作」和「上下文」的问题，那么 **Skills（技能系统）** 则解决了「专业能力边界」的问题。两者结合，构成了 AI 解 CTF 的绝对优势。

Skills 让你可以为 Agent 预置领域知识和工具链——比如一个专门用于处理 ELF 二进制分析的 Skill，一个封装了常见密码学攻击（Padding Oracle、CBC Bit Flipping、RSA 低指数攻击等）的 Skill，一个集成了 z3 约束求解器的 Skill。

当 Skills 和 Subagents 协同工作时，你得到的不再是一个「什么都懂一点但什么都不精」的通用 Agent，而是一支**各有绝活的专家团队**：

* 主代理读题、理解题意、制定攻略
* 密码学子代理携带密码学 Skill，专攻加解密
* 逆向子代理携带逆向 Skill，专攻二进制分析
* Exploit 子代理携带 Pwn Skill，专攻漏洞利用

**每个子代理都是细分领域的专家，而不是一个被迫身兼数职的疲惫全栈选手。**

这种架构带来的优势是碾压性的：

1. **上下文零损耗**——每个子代理独立工作，不存在信息互相干扰的问题
2. **并行加速**——多个分析任务同时进行，总耗时大幅缩短
3. **专业深度**——Skills 让每个子代理在自己的领域内达到专家级水准
4. **可扩展性**——新的题型只需要新增对应的 Skill 和子代理配置

对于 CTF 战队来说，这意味着你可以构建一套「AI 参赛系统」，用 TOML 文件定义好各方向的专家代理，比赛时主代理自动分发题目到对应的专业子代理，实现近乎全自动化的协作解题。

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/nNzOrpxNkNOexrWpDgDYXpYTLbLrl7RhtCuwTAdmvLKiaF0kN9rgKnvsq0GYhnCY3w34I63n5U9ocibeG87eFCqg/0?wx_fmt=png)

云晞科技Sec

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/nNzOrpxNkNOexrWpDgDYXpYTLbLrl7RhtCuwTAdmvLKiaF0kN9rgKnvsq0GYhnCY3w34I63n5U9ocibeG87eFCqg/0?wx_fmt=png)

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