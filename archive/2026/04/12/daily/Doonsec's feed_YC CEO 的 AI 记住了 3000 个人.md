---
title: YC CEO 的 AI 记住了 3000 个人
url: https://mp.weixin.qq.com/s/gAEi_zRvrThcIBKsTqUytA
source: Doonsec's feed
date: 2026-04-12
fetch_date: 2026-04-13T04:53:50.218464
---

# YC CEO 的 AI 记住了 3000 个人

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/MGmpoYTX6rhVTYSYYo0wvxYu8PzytQleu3sd9vVUliaUjDJrnYkjvXxcIz1I8cNKSVEs6CsibdUdMFY4iboVTFLPlVpBGCHCKuxfPT3AialnrNA/0?wx_fmt=jpeg)

# YC CEO 的 AI 记住了 3000 个人

原创

AI安全工坊
AI安全工坊

AI安全工坊

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

最近，Garry Tan 在 X 上发了一条推文，附了一个 GitHub 链接。

没有长文预告，没有产品发布会，就一句话：「这是我每天用的 AI 系统，源码全在这了。」

5300 个 star，几天而已。

Garry Tan，Y Combinator 现任 CEO。就是那个孵化了 Airbnb、Stripe、Dropbox、Reddit 的 YC。

一个管着几千家创业公司的人，把自己的 AI 记忆系统开源了。

这事本身就够有意思了。但真正让我坐直的，是他开源的那个东西叫什么 -- **GBrain**，全名 Garry's Opinionated OpenClaw/Hermes Agent Brain。

这个名字里藏着两个关键词。

**OpenClaw** -- 今年最火的开源 AI 助手项目，25 万 star，本地优先。

**Hermes Agent** -- NousResearch 今年新推出的 AI Agent 框架，6 万多 star，核心卖点是"会自己进化"。

GBrain 是什么？用 Garry Tan 自己的话说：他在用 OpenClaw 的时候，开始往一个 Markdown 仓库里塞东西。一个人一家公司一页纸，上面是当前认知，下面是时间线。结果越塞越多，滚雪球一样长到了一万多个文件。

然后他把这套东西抽象成了一个独立项目，设计成可以给 OpenClaw、Hermes Agent、或者任何 AI Agent 当"记忆层"用。甚至不用 Agent，它自己就能跑。

---

## 先说 GBrain：一个人的数字记忆

GBrain 的 README 开头第一句话是这么写的：

> Your AI agent is smart but it doesn't know anything about your life. GBrain fixes that.

翻译过来：你的 AI 很聪明，但它对你的人生一无所知。

这句话戳到了一个真实的痛点。

你跟 ChatGPT 聊天，每次都得重新解释你是谁、在做什么、上次聊到哪了。烦。它很聪明，但那个聪明跟你没关系，是通用的。

GBrain 做的事情很直接：把你的数字生活灌进一个向量数据库，让 AI 在回答你之前先去检索。

哪些数据？看它内置的集成：

| 数据源 | 怎么进来的 |
| --- | --- |
| 电话录音 | Twilio + OpenAI Realtime，挂完电话自动生成脑页 |
| 邮件 | Gmail 收集器，自动提取实体和关键信息 |
| X/推特 | 时间线 + 提及 + 删除记录 |
| 日历 | Google Calendar，每天生成可搜索的日程页 |
| 会议纪要 | Circleback 转录，自动关联参会人 |

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/MGmpoYTX6rjMHsA0ibF9O0CBvtMo130ehIIQNPJpEpnDaOMA8puXiaAeyvhjclhdOkq6qPO33xgJjVrtlKjniakia7ZPW1pUWPa7ydCib7EsbSLw/640?from=appmsg)

然后搜索怎么做？不是简单的关键词匹配。GBrain 同时跑关键词搜索和语义向量搜索，然后用一个叫 RRF 的算法把两种结果融合排序。还会自动扩展你的查询 -- 你搜一个词，它帮你想三个近义表达一起搜。

举个例子：你搜"什么时候应该忽略常识"，纯关键词搜不到一篇叫《天才的公交车票理论》的文章 -- 但向量搜索能找到，因为语义是相关的。

Garry Tan 在 README 里写了几个他自己的真实用法：

> "谁应该被邀请来晚餐，认识 Pedro 和 Diana 的人？" -- 从 3000 多个人物页面中交叉检索社交图谱
>
> "我说过哪些关于羞耻感和创始人表现之间关系的话？" -- 搜索的是你自己的思考，不是互联网
>
> "30 分钟后我要见 Jordan，帮我准备一下" -- 自动拉出档案、共同历史、近期动态、待处理事项

看到没？这不是"帮我查个天气"那种 AI 助手。这是一个真正了解你社交网络、知道你在想什么、能帮你准备会议的系统。

技术上有几个让我意外的点：

**轻**。技术栈是 TypeScript + Bun，默认用 PGLite（嵌入式 Postgres 17.5，跑在 WASM 里），2 秒启动。不需要 Docker，不需要 Supabase 账号。你的脑子跑在本地。

**薄壳胖技能**。他管这个叫 Thin Harness, Fat Skills -- 核心引擎很薄，所有能力定义在 Markdown 文件里。想加一个新技能？写个 .md 文件。他说 "Markdown is code"，在他的系统里，Markdown 文件就是安装程序、就是配置文件、就是技能定义。

**睡觉也在干活**。GBrain 有一个"梦境循环" -- 你睡了，Agent 还在后台跑。扫描所有对话、补充缺失的实体、修复引用、整理记忆。他的原话："I wake up and the brain is smarter than when I went to sleep."

他的脑子里装了什么？一万多个文件，3000 多个人的档案（每个人一页，持续更新），13 年的日历，280 多份会议记录，还有 300 多个他自己的原创想法。

这不是 demo。这是一个 YC CEO 的真实工作系统。

---

## 再说 Hermes Agent：一个会自己变强的 AI

GBrain 管记忆。那谁来"想"？

这就是 Hermes Agent 的位置。

NousResearch 去年 7 月创建了这个仓库，但真正开始发版是今年 3 月 -- 一个月内从 v0.2 迭代到 v0.8，7 个版本，速度很猛。

它的定位用一句话说：**The agent that grows with you -- 跟你一起成长的 Agent。**

听着像营销口号？拆开看看它到底做了什么。

第一，**自动创建技能**。你重复做了几次某个工作流，它会识别出模式，自动把这个模式固化成一个技能。下次遇到类似任务，直接用。而且技能会在使用中自我改进 -- 不是固定的脚本，是活的。

第二，**三层记忆**。当前对话是短期记忆，跨会话积累是长期记忆，还有一层是它对你这个人的理解（用了一个叫 Honcho 的用户建模系统）。越用越懂你。

第三，**不绑定终端**。Telegram、Discord、Slack、WhatsApp、Signal、命令行 -- 统一一个 gateway 进程，在哪都能找到它。对话跨平台连续，你在 Telegram 上说到一半，到命令行继续，它知道你在聊什么。

第四，**模型无关**。Nous Portal、OpenRouter（200 多个模型）、OpenAI、Google AI Studio，随便切。一条命令 `hermes model` 就换了，不用改代码。

而且它有一个功能我觉得很说明问题 -- **OpenClaw 迁移**。一条命令 `hermes claw migrate`，把你在 OpenClaw 里的人设、记忆、技能、API Key 全部导过来。

这意味着什么？Hermes Agent 显然想接住 OpenClaw 的用户。你可以把它理解成同一个赛道的新玩家，但带着更激进的野心 -- 不只是管理你的工具，而是让工具自己学会怎么管理你的事。

团队背景也值得一提。NousResearch 不是突然冒出来的草台班子 -- Hermes 系列大模型在 HuggingFace 上下载超过 3300 万次。Paradigm 领投了 5000 万美元 A 轮。CEO Jeffrey Quesnelle 密歇根大学 CS 硕士，联创 Karan Malhotra 斯坦福 ML 研究员。

而且，5 美元 VPS 就能跑。

---

## 拼在一起看：个人 AI 的完整拼图

现在把两个项目放在一起。

GBrain 的 README 里有一段专门解释它和 OpenClaw/Hermes Agent 的关系：

| 层 | 存什么 | 怎么查 |
| --- | --- | --- |
| **GBrain** | 人物、公司、会议、想法、媒体 | `gbrain search` 、`gbrain query` |
| **Agent 记忆** | 偏好、决策、操作配置 | `memory_search` |
| **会话上下文** | 当前对话 | 自动 |

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/MGmpoYTX6riaOhXjwdLac1EqWqEacX38DQibIul1JFBSMtJx9XW3fOib564GSUX2Iib3fzZCJVGDia1fpVKKVCDcUKk8CiavSHhEglicRicj4Nic3mLg/640?from=appmsg)

三层都要查。GBrain 管世界知识（你认识谁、知道什么），Agent 记忆管运行状态（你的偏好和决策），会话管当下。

之前看过一篇文章讲 OpenClaw + Claude Code 的实践 -- 一个独立开发者一天 94 次代码提交，30 分钟完成 7 个 PR。他总结的核心问题是：「Codex 和 Claude Code 对你的业务一无所知。它们只看到代码，看不到完整的业务图景。上下文窗口是固定的，塞满代码就没空间放业务上下文了。」

GBrain 解决的正是这个问题。但它的野心更大 -- 不只是业务上下文，是**人生上下文**。你的 AI 不只知道你的代码仓库，它知道你上周跟谁开了会、你在推特上关注什么话题、你三年前对某个概念的看法是什么。

再叠加 Hermes Agent 的自进化 -- 它不只记住了这些，它会从中学到新的工作模式。

这两个项目单独看，各有意思。放在一起看，你看到的是一个信号：**个人 AI Agent 正在从"聊天工具"变成"第二大脑"。**

---

## 这件事的信号

「这不就是极客的玩具吗？」

两年前也许是。但看看现在：

* • MCP 协议安装量突破 9700 万，所有主流 AI 厂商已适配
* • 全球生成式 AI 企业采用率 88%，一年前是 71%
* • Hermes Agent 一个月 7 个版本，从 v0.2 到 v0.8

Garry Tan 在推文里把 GBrain 称为「memex 愿景的实现」。Memex 是 1945 年 Vannevar Bush 提出的概念 -- 一个能存储和检索你所有阅读、通信和思考的设备。

81 年后，一个 YC CEO 用 TypeScript 和 Markdown 文件做到了。源码全开源。

不管你是不是开发者，信号很清楚：**AI 助手的下一步不是更聪明，而是更懂你。**

那些还在每次对话都从零开始的 AI 产品，护城河在哪？

---

*GBrain: https://github.com/garrytan/gbrain*

*Hermes Agent: https://github.com/NousResearch/hermes-agent*

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/BibeFvVBkRA8RWa5pyic1Xob8V1UxQjOHLAx5qbkPJ2gibKpIQpRw4ogjL6jE9xIxc26o12ZRTBvPaLQNjxXDAO5g/0?wx_fmt=png)

AI安全工坊

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/BibeFvVBkRA8RWa5pyic1Xob8V1UxQjOHLAx5qbkPJ2gibKpIQpRw4ogjL6jE9xIxc26o12ZRTBvPaLQNjxXDAO5g/0?wx_fmt=png)

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