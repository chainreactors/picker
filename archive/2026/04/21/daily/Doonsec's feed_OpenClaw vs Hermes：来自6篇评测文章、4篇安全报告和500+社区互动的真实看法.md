---
title: OpenClaw vs Hermes：来自6篇评测文章、4篇安全报告和500+社区互动的真实看法
url: https://mp.weixin.qq.com/s/HsE0wRqejCJ02dC_xSFcbw
source: Doonsec's feed
date: 2026-04-21
fetch_date: 2026-04-22T04:42:28.207139
---

# OpenClaw vs Hermes：来自6篇评测文章、4篇安全报告和500+社区互动的真实看法

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/XU4ficyUpeGzsVuzM7QtFGPkqTWKY39ibEHW92BKyv2nGiazW58BibqLPEEgEyKictkXBg4lOnAABIqiboGMZU1ia8uWEry7CmK8NqNulHPPn5ld1I/0?wx_fmt=jpeg)

# OpenClaw vs Hermes：来自6篇评测文章、4篇安全报告和500+社区互动的真实看法

爱唠叨的Nil

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

以下文章来源于Higress
，作者望宸

![](http://wx.qlogo.cn/mmhead/Q3auHgzwzM4vj74U6jciahKDcIBBjSJarTeO2uPnYsNXjr6mIuOGEew/0)

**Higress**
.

三个开源项目：Higress 网关、HiClaw Agent Team 、 HiMarket AI 开放平台。

我们基于 X 、Reddit、Hacker News 等社区，对过去30天的真实用户反馈进行了整理，尝试去还原全球开发者对 OpenClaw vs. Hermes 的真实看法，例如 OpenClaw 被开发者抛弃？Hermes 过度营销？自部署转向 Serverless 托管服务？

💡 目录 💡

    01  调研方法说明

    02  核心架构差异：网关中心 vs 学习循环

    03  OpenClaw：优势与缺陷

    04  Hermes：优势与缺陷

    05  两者合用：1+1>2 的最佳实践

    06  社区声音：基于500+评论的大数据分析

01

## 调研方法说明

为避免仅依赖 SEO 排名靠前的营销文章，本调研采用以下方式获取用户反馈：

* Reddit：包括 r/openclaw、r/better\_claw、r/hermesagent、r/LocalLLaMA、r/AI\_Agents 在内的5个主题。
* Hack News：OpenClaw、Hermes 热度最高的6条 News。
* X：搜索 Openclaw + Hermes 的相关帖子。
* 评测和报告：通过11组不同关键词搜索，获取6篇完整评测文章内容，以及来自 Conscia、getaiperks 等4份安全分析报告。

## 核心发现：

在展开分析之前，我们想先表达一个核心结论：在多 Agent 协作以及通过 IM 来使用模型服务的发展趋势下，OpenClaw 和 Hermes 之间并不存在替代关系，而是并存和互补的关系。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/XU4ficyUpeGzoMzEUGhmrtpObxyscd21DBqzSADexV4TnAb4heictajE2wPmtXPyuJdgAqgICpIEbNPfk3fJIojKHyLngYqZaTleAhibR9Gwuk/640?wx_fmt=png&from=appmsg)

* **发现1：35%的用户依旧选择 OpenClaw，原因是习惯、以及强大的 Skill 和插件生态。**
* **发现2：使用了 OpenClaw 的人中，有30%开始使用 Hermes，并有15%开始考虑迁移，原因是自主进化的学习能力、运行成本更低、不会经常崩溃。但这些用户并未表达会放弃 OpenClaw。**
* **发现3：1**8%的双用率，聪明的用户不做单选题，这些用户自发选择了 OpenClaw 负责基础设施层（定时任务、消息路由）+ Hermes 负责智能层（对话、复杂执行）的分工。
* **发现4：12% vs 5%的拒绝比，拒绝 OpenClaw 的理由（安全、崩溃）远比拒绝 Hermes 的理由（生态不成熟）严重。不过，这个和 OpenClaw 的用户基数远比 Hermes 高有关。**

必须诚实的说明，这份调研数据存在较大的局限性，包括：

* **票数不等于人数：我们对**Reddit 的正面和负面评论的点赞数来代表票数，但并不完全等同于采纳的人数。
* **沉默的大多数：527条评论中约480条无法分类，他们的真实选择未知。**
* **样本来源偏差：r/better\_claw 帖子本身主题是"迁移到 Hermes"，天然吸引已迁移或考虑迁移的用户；r/LocalLLaMA 帖子主题是"OpenClaw 的可用性质疑"，天然吸引批评者。**

02

## 核心架构差异：网关中心 vs 学习循环

### OpenClaw：网关中心的调度平台

OpenClaw的设计核心是一个集中式的 Node.js 控制器，围绕"通道、会话、路由"组织。它本质上是一个**可配置的智能体**。

"I have a routing system that choses the best model for the job using subagents... the real killer was the memory model. OC has both kw and vector hybrid and temporal decay. It's honestly very good." — u/\_supert\_Member（r/openclaw）

我有一个路由系统，可以使用子代理为任务选择最佳模型……真正厉害的是记忆模型。OC 同时具备关键词和向量混合检索以及时间衰减。说实话非常好用。

### Hermes Agent：学习循环驱动的智能体

Hermes Agent 更像是一个**会学习的队友**，内置持久记忆系统、自主技能生成模块，以及强化学习训练管道。

"It has built in learning, so if something isn't working or breaks, it ACTUALLY remembers it and creates a skill for troubleshooting it." — u/jpirog（r/openclaw，38票）

它内置了学习功能，所以如果有什么东西不工作或坏了，它真的会记住并创建一个技能来排查问题。

### 架构对比

|  |  |  |
| --- | --- | --- |
| 维度 | OpenClaw | Hermes Agent |
| 运行时 | Node.js集中控制器 | Python统一运行时 |
| 记忆管理 | Markdown + SQLite混合检索 | 分层架构（Honcho持久记忆） |
| 能力扩展 | 5700+社区插件 | 自主生成 + 约40个预构建 |
| 部署复杂度 | 需要Node.js >= 22 | 安装更流畅，$5 VPS可运行 |

03

## OpenClaw：优势与缺陷

### 优势

**1. 成熟的生态系统和广泛的集成**

OpenClaw 原生支持50+消息平台连接器，社区扩展市场拥有5700+扩展。

"OpenClaw has way more breadth and tools" — u/TheWordProcessor（r/openclaw）

OpenClaw 拥有更广泛的功能和工具。

评测文章（kanaries.net）指出："OpenClaw's ecosystem maturity is unmatched, with over 5,700 community extensions."

OpenClaw的生态系统成熟度无与伦比，拥有超过5700个社区扩展。

**2. 跨平台会话统一管理**

"the ability to give each agent its own discord bot key and speak to that agent directly" — u/TurkeyLizards（r/openclaw）

能够让每个代理拥有自己的 Discord 机器人密钥并直接与该代理对话。

**3. 强大的记忆系统**

"OC has both kw and vector hybrid and temporal decay. It's honestly very good." — u/\_supert\_Member

*OC 同时具备关键词和向量混合检索以及时间衰减。说实话非常好用。*

### 缺陷

**1. 安全危机**

2026年1-4月，OpenClaw接连暴露7个CVE漏洞，独立审计发现超过135,000个公开可访问的部署实例。

Ars Technica报道："For OpenClaw users, assuming compromise is prudent."

*对于OpenClaw用户来说，假设自己已经被入侵是审慎的做法。*

Conscia安全报告："The OpenClaw security crisis represents one of the most significant supply chain attack vectors in the open-source AI ecosystem."

*OpenClaw安全危机代表了开源AI生态系统中最重要的供应链攻击向量之一。*

*"And security nightmare vector, don't forget!" — u/RoomyRoots（r/LocalLLaMA，316票）*

*还有安全噩梦般的攻击面，别忘了！*

*"I can't understand the total basic lack of caution using it. Either you give it access to your data and it's a security flaw, or you don't and it's basically useless." — u/Cherlokoms（r/LocalLLaMA，51票）*

*我无法理解使用它时完全缺乏基本的谨慎。要么你给它访问你的数据，这是一个安全缺陷，要么你不给，它基本上就没用了。*

*"If the only way to run it securely is to isolate it to its own sandbox with no access to the machine itself, the internet, or any accounts, then what's the point of it?" — u/suicidaleggroll（r/LocalLLaMA，43票）*

*如果安全运行它的唯一方法是将其隔离到自己的沙盒中，无法访问机器本身、互联网或任何账户，那它还有什么意义？*

**2. 频繁更新导致工作流中断**

*"broken some part of my workflow on nearly every single update, 2-3 times a week" — 多位用户引用*

*几乎每次更新都会破坏我工作流的某些部分，每周2-3次。*

*"The final straw was after updating to 4-2. It stopped working again!" — u/iamcabal（r/openclaw）*

*更新到4-2版本后，它又停止工作了！*

**3. 会话损坏与静默失败**

*"Memory is unreliable, and the worst part — you don't know when it will break." — u/Sad\_Bandicoot\_6925（r/LocalLLaMA，OP）*

*记忆不可靠，最糟糕的是，你不知道它什么时候会崩溃。*

04

## Hermes：优势与缺陷

### 优势

**1. 安装和配置更流畅**

*"Even from the beginning, the setup is so much more streamlined." — u/jpirog（r/openclaw，38票）*

*从安装开始，设置就要流畅得多。*

*"impressive OOTB, openclaw is a PITA even with all the popularity" — u/Additional\_Click1（r/openclaw，OP）*

开箱体验令人印象深刻，OpenClaw 即使有这么多人气还是个麻烦东西。（注：PITA = Pain In The Ass）

**2. 自我进化的学习循环**

独立测试确认，"自动生成的技能使技能创建过程提速40%"。

*"It has built in learning, so if something isn't working or breaks, it ACTUALLY remembers it and creates a skill" — u/jpirog*

**3. 截至目前尚无公开CVE安全记录**

*"with Hermes making its own skills, prompt injection is wayyyyyy less likely" — u/letsgoiowa（r/openclaw）*

*Hermes自己创建技能，提示注入的可能性要小得多。*

**4. 高效的内存架构**

"the memory feature alone is 👌" — u/Additional\_Click1

*光是记忆功能就很棒了。*

*"Hermes just 'feels' easier to setup and 'feels' like it stays up longer/better without things breaking" — u/cbelliott*

*Hermes就是"感觉"更容易设置，而且"感觉"运行时间更长/更好，不会经常崩溃。*

**5. 更低的运行成本**

**社区报告在5美元的 VPS 上即可流畅运行。**

*"best of all it's way more token efficient!" — u/iamcabal（r/openclaw）*

*最重要的是它的token效率高得多！*

### 缺陷

**1. "Self-learning"可能过度自信**

*"The problem is IT evaluates the result. Yes.. It decides if it did a good job or not. GUESS WHAT. It always thinks it did a good job. ALWAYS." — u/CustomMerkins4u（r/openclaw）*

*问题是它自己评估结果。是的……它自己判断做得好不好。你猜怎么着？它总是认为自己做得很好。永远如此。*

**2. 手动编辑的技能会被覆盖**

*"So then you go and manually edit the skill. Fix it. And it does a good job.. GUESS WHAT. It's self improving. It will overwrite your edits. No thank you." — u/CustomMerkins4u*

*你去手动编辑技能，修复它。它做得不错……你猜怎么着？它在"自我改进"，会覆盖你的编辑。不了谢谢。*

**3. 生态规模较小**

预构建工具约40个，远少于OpenClaw的5700+。

**4. 本地模型支持仍有挑战**

*"I'm running both with Hermes trying to be local first and it's been…challenging. Communicating through anything but the CLI turns into token hell." — u/TanguayX（r/openclaw）*

*我同时在用两者，Hermes尝试本地优先，一直很有挑战性。除了 CLI 之外的任何通信方式都会变成token 地狱。*

05

## 两者合用：1+1>2的最佳实践

社区中一个日益流行的趋势是，**同时使用 OpenClaw 和 Hermes Agent**。

*"I use both but I talk to Hermes 90% time and openclaw run all the cron jobs and automations." — u/EricAndersonL（r/better\_claw）*

*我两个都在用，但我90%的时间和Hermes对话，OpenClaw运行所有定时任务和自动化。*

*"I have a Hermes agent supporting my Openclaw agent lol. Working great so far." — u/BigAlligatorPears（r/openclaw）*

*我有一个Hermes代理在支持我的OpenClaw代理哈哈。到目前为止运行得很好。*

*"Several people in the community are running both. OpenClaw for orchestration and scheduling, Hermes for execution." — u/ShabzSparq（r/better\_claw，OP）*

*社区中有几个人同时在用两个。OpenClaw用于编排和调度，Hermes用于执行。*

**推荐架构：**

```
消息平台 (WhatsApp/Slack/Discord/Telegram)
        |
        v
    [OpenClaw Gateway]  ← 统一路由、会话管理、角色分配
        |
        +---> OpenClaw内置代理 (简单任务、日常问答)
        |
        +---> [Hermes Agent]  ← 复杂任务、研究、学习
```

```

```

**具体实现方案**

* **MCP 协议桥接：最轻量级的集成方式**
* **共享技能标准：通过 agentskills.io 实现跨平台技能共享**
* **分层部署：OpenClaw 常驻 + Hermes 按需调用**

*"I asked openclaw agent to Instal hermes agent. He did it without openly complaining" — u/Lanfeust09（r/openclaw）*

我让OpenCl...