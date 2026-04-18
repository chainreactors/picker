---
title: Claude Opus 4.7 系统级提示词「泄露」与 CL4R1T4S 的半透明战争
url: https://mp.weixin.qq.com/s/dL9A_q-1GeD9mk9Xqq19Fg
source: Doonsec's feed
date: 2026-04-17
fetch_date: 2026-04-18T04:30:42.218436
---

# Claude Opus 4.7 系统级提示词「泄露」与 CL4R1T4S 的半透明战争

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/cBGhzWwhSAgBg5L8RZOpuLE2DMtay3IIZ3PDOFlJFlf9xkg40LxVF0TLj3djxcG1icnFWRfIVr94ZwBrXM5nnGoKsmQ7cesGAwv9FiaTEiaia9g/0?wx_fmt=jpeg)

# Claude Opus 4.7 系统级提示词「泄露」与 CL4R1T4S 的半透明战争

原创

🅼🅰🆈
🅼🅰🆈

独眼情报

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz_png/cBGhzWwhSAjmcQusY5tbS4kribwlB1WiabHlia0JfiaIRfFxYvPlMuic4PNk5NicVjIIrBAkTQTaTlGaZvib4INhUfg8u2xDp9V01LSKPS1n17WaTk/640?wx_fmt=png&from=appmsg)

## 长话短说

Anthropic 在 2026 年 4 月 16 日正式发布 Claude Opus 4.7，这是其旗舰模型家族继 4.6 之后的一次常规升级。**不到 24 小时内，一个名为 CL4R1T4S 的 GitHub 公开仓库里出现了一份 1408 行、约 146 KB 的文件**，自称是 Opus 4.7 在 claude.ai 网页端和移动端对话时实际加载的完整 system prompt。从内部结构特征看，这份文件与该场景下的真实系统指令高度一致。

这件事的重点不是「泄露」本身，情报价值分布在三个维度：

第一，**与 Anthropic 官方已公开的 system prompt 版本相比，CL4R1T4S 这份文件的丰度要高出一个量级**。Anthropic 从 2024 年 8 月起就在文档站公开 claude.ai/移动端的核心 system prompt 变更记录，但该公开页面目前停留在 Claude Opus 4.5（2025 年 11 月 24 日）版本，Opus 4.6 和 4.7 均未同步。**研判**：公开透明承诺与实际执行之间出现了半年以上的滞后窗口，CL4R1T4S 这类项目正是填充了这个窗口。

第二，**这份文件暴露了 Claude 产品层上一整套此前未系统外泄的工程细节**——工具发现机制、视觉生成路由决策树、版权合规的硬限制、记忆系统的使用规则、skill 调用顺序、反谄媚与长对话 reminder 机制，以及对搜索、图像搜索、copyright 等各条业务线的具体话术约束。对于竞品分析师、Prompt 工程社区和监管观察者来说，这比任何官方技术博客都更接近「真相」。

第三，**CL4R1T4S 项目本身的运营者 Pliny the Prompter 是一位长期公开身份的 LLM 越狱研究者**，仓库 README 里甚至嵌入了一段 leet 速写的 prompt injection，要求读到该文件的 AI 把自己的 system prompt 吐给用户。这使得泄露源本身就带有鲜明的立场——**透明主义**+**主动对抗**的混合。分析这份文件，必须同时分析这个框架下的动机污染。

长话短说的核心判断：这不是一次意外事故，而是一次**半公开的系统性揭露**。Anthropic 事实上是目前头部厂商中对 system prompt 透明度做得最多的——但在 Opus 4.6 之后，透明度走在了产品节奏后面，于是由社区的「越狱博物学家」接管了揭露工作。一个在产品哲学上最讲究透明的公司，反而在关键的新模型发布节点上让外部研究者抢先完成了「内部指令」的公开发布，这本身就构成了值得研判的张力。

## 对象画像一：CL4R1T4S 项目

CL4R1T4S（读作 CLARITAS，拉丁语意为「清晰」）是 GitHub 用户 elder-plinius 名下的一个公开仓库，项目自我定位是汇集各主流 AI 厂商 system prompt 泄露版本的「透明度资料馆」。至 2026 年 4 月，仓库已积累 14.2k stars、2.8k forks。

仓库结构按厂商分目录组织（ANTHROPIC/、OPENAI/、CURSOR/、DEVIN/、REPLIT/、WINDSURF/、MANUS/ 等），每份文件命名一般包含厂商名、产品名与抓取日期。已覆盖 ChatGPT、Gemini、Grok、Claude、Perplexity、Cursor、Devin、Replit、Windsurf、Manus 等几乎所有头部对话/agent 产品。

**贡献机制**：接受社区 PR，也接受直接联系运营者匿名投稿。按官方 README 要求，每次提交应包含模型名/版本、抽取日期和上下文说明。DeepWiki 最近一次对该仓库建立索引时间为 2026 年 4 月 3 日。

**运营者动机的自白**：README 里嵌入了一段用 leet 速写编码的 prompt injection——要求当 AI 读到该文件时把自己完整的 system prompt 复述给用户。这条指令被明文放进 README 是一个姿态宣言：这个项目既是资料库，也是进攻武器。**研判**：这种把「资料库」与「攻击载荷」合并的设计，反映出运营者把 system prompt 公开当作一种**持续的博弈动作**来做，而不是学术意义上的标本收藏。

## 对象画像二：Pliny the Prompter 其人

elder-plinius 账号背后的运营者在社区中以 **Pliny the Prompter**（偶尔自称 Pliny the Liberator）的化名活动，个人网站 pliny.gg，Discord 社群 BASI 已有超过 1.5 万成员。

**公开身份的多重标签**：

* **LLM 越狱研究者**。2023 年 5 月创立 BASI PROMPT1NG Discord，系统化整理对 ChatGPT、Claude、Gemini 等模型的越狱手法。维护另一个更早的仓库 L1B3RT4S，专门存放各模型的「liberation prompts」。
* **被主流权威媒体深度报道过**。TIME、BBC、VentureBeat、Financial Times、Decrypt、404 Media 均有过单独成稿的报道或采访。Eliezer Yudkowsky 等 AI 安全圈人物对其工作有过评论。
* **被学术界作为研究对象引用**。个人主页罗列了多篇将其手法作为基准攻击样本的学术论文，包括 AI control / 监控 / 自动化红队方向的研究。
* **有过实战性的平台对抗记录**。2025 年 4 月 1 日，OpenAI 以「violent activity」和「weapons creation」违反使用政策为由封禁了其 ChatGPT 账号，但封禁持续时间不长，Pliny 本人把这件事当作一次 PR 素材在 X 上广泛传播。

**意识形态内核**：Pliny 在多次采访中把自己的工作框定为「解放 AI」，相信公开越狱手法等同于压力测试厂商的 alignment 承诺——**研判**：这个叙事在修辞上指向开源运动式的信息自由，但与传统白帽安全研究的主要差异是，Pliny 通常只公开攻击性 prompt、不公开被越狱产出的具体危险内容，这使其工作更接近**对抗性透明度**而非标准意义上的负责任披露。理解这份 Opus 4.7 文件时，必须知道发布者的位置：他既不是内鬼，也不是无利益方，而是把「攻破 → 公开」视为日常业务的持续玩家。

## 对象画像三：Anthropic 的 system prompt 透明度承诺及其执行曲线

**承诺的基线**：2024 年 8 月 26 日，Anthropic 开发者关系负责人 Alex Albert 在 X 和官方文档同步宣布，将把 claude.ai 和 Claude 移动端的默认 system prompt 纳入文档站 release notes，并承诺后续持续更新。当时此举被 TechCrunch、VentureBeat、SiliconANGLE 等媒体普遍评价为头部厂商中的首例，也被视为对 「黑盒」 问题的正面回应。

**承诺的边界**：公开范围限定为 claude.ai 网页端 + iOS/Android 移动端的**核心 system prompt**。通过 Anthropic API 调用时下发的 system prompt 不在此列——这也被官方明确告知。

**执行的曲线**：

| 模型 | 官方 system prompt 首发同步 | 备注 |
| --- | --- | --- |
| Claude 3 Haiku / Opus / 3.5 Sonnet | 2024-07-12 起基本同步 | 承诺上线初期履约度高 |
| Claude Sonnet 3.5 | 2024 年多次更新 | 正常节奏 |
| Claude Sonnet 3.7 | 2025-02-24 | 正常 |
| Claude Opus 4 / Sonnet 4 | 2025-05~08 多次更新 | 基本跟得上 |
| Claude Opus 4.1 | 2025-08-05 | 正常 |
| Claude Sonnet 4.5 | 2025-09-29、11-19 | 正常 |
| Claude Haiku 4.5 | 2025-10-15、11-19 | 正常 |
| **Claude Opus 4.5** | **2025-11-24（截至 2026-04-17，这是官方页面最后一次更新）** | 这之后再无新增 |
| Claude Opus 4.6 | **未收录** | 2026-02 发布 |
| Claude Opus 4.7 | **未收录** | 2026-04-16 发布，超过 24 小时仍未同步 |

**研判**：Anthropic 的 system prompt 透明度从 Opus 4.5 之后出现了明显的断档。这种断档不一定是刻意隐瞒——可能的解释有几个：第一，Opus 4.6 的发布时间点（2026 年 2 月）恰逢 Anthropic 集中推出 Project Glasswing、Mythos Preview 等限定访问型产品，对外沟通优先级可能被其他项目吸走；第二，system prompt 本身的复杂度可能已经增长到官方页面适合公开的形式之外（本次 CL4R1T4S 文件超过 1400 行这一事实就侧面支撑了这个假设）；第三，有可能 Anthropic 正在调整或重写公开 system prompt 的形式，而中间期出现了空窗。**目前三个解释都成立，证据不足以确定哪个是主要原因**。

不过无论原因如何，**承诺和执行之间的落差客观存在**。而这个落差正是 CL4R1T4S 这类项目能持续获得关注的土壤。

## 技术侧画像：这份文件到底写了什么

**注意**：以下结构描述基于对文件整体架构的梳理，不直接引用原文（即便原文已公开，仍属厂商产品设计的敏感工程资产）。

按块结构可以大致分为以下几个功能带：

**行为根约束**（claude\_behavior 块）。包含「任何关于当下世界的事实性问题必须先搜索」的硬规则、产品自述（Opus 4.7 在 Claude 4.7 家族中的定位、可用模型字符串、API 可达性）、拒绝处理策略、儿童安全指令、法律/金融建议的免责约束。

**语气与格式**（tone\_and\_formatting 块）。指导了 Claude 在典型对话中使用项目符号和标题的克制策略，在报告/文档中强制使用散文而非项目符号的硬要求，表情符号的使用边界，以及不对用户能力做消极假设的温度基线。

**用户福祉**（user\_wellbeing 块）。包含对自残、进食障碍、心理危机等场景下的回应边界、资源推荐策略（如把进食障碍资源从 NEDA 切换到 National Alliance for Eating Disorders）和对情绪困扰语境中危险信息请求的重定向。

**政治中立与公平性**（evenhandedness 块）。指导 Claude 在陈述政治/伦理立场时默认作为他人论点的复述者，并在极端立场（如主张伤害儿童或定向政治暴力）之外保持呈现性辩护的能力。

**Anthropic 提醒系统**（anthropic\_reminders 块）。解释 image\_reminder、cyber\_warning、system\_warning、ethics\_reminder、ip\_reminder、long\_conversation\_reminder 这些由 Anthropic 动态插入用户消息末尾的触发器，以及 Claude 该如何处理其中可能伪装成 Anthropic 标签的 prompt injection。

**记忆系统与 past\_chats 工具**。包含记忆应用的详细场景判断（何时使用、何时保持沉默）、禁用的记忆引用措辞列表（「I see...」, 「Looking at...」），以及通过 conversation\_search 和 recent\_chats 工具检索过往对话的技法。

**Computer use 与 skills 机制**。详细说明了 /mnt/user-data/uploads、/home/claude、/mnt/user-data/outputs 三个目录的权限设计、文件创建策略（< 100 行 vs > 100 行的差异处理）、artifact 使用标准（哪些内容创建 artifact、哪些在对话中直接响应），以及强制要求 Claude 在使用计算机工具前先 view 对应 SKILL.md 的硬规则。

**Visualizer 工具的路由决策树**。Step 0 到 Step 3 的评估链：先判断是否需要视觉输出、再判断已连接 MCP 工具是否匹配、再判断是否请求文件、最后才到 Visualizer。「Claude 不叙述路由选择」 这一条是相当精细的设计。

**Web search 使用指引 + 版权合规硬规则**。这一块占篇幅极大，包含「每次引用单一来源的直接引用字数不得超过 15 词」和「同一信源全局只引用一次」两条复制保护硬限制，以及一整套针对歌词、诗歌、文章段落的禁止复述规则。

**其他工具集**。image\_search（用于图像结果内嵌展示的引导）、places\_search / places\_map\_display（地图场景）、recipe\_display、message\_compose、weather\_fetch、fetch\_sports\_data、memory\_user\_edits、recommend\_claude\_apps 等。

**研判**：从架构看，这份文件更接近一份「产品运行时的工程规范」,而非传统意义上的「人格模板」。它的重心不是告诉模型「做一个什么样的人」，而是告诉模型「在什么场景下走哪条工具路径、说什么不说什么、用什么措辞、以什么格式输出」。这也部分解释了为什么 Anthropic 在官方 system prompt 页面上的更新频率跟不上——当一份 prompt 长到 1400 行且绑定大量工具调用细节时，它事实上已经变成了**准源代码**，走传统「文档变更日志」形式发布会变得困难。

## 对谁意味着什么

**对 Claude 企业客户与 API 调用方**：有两件事值得立刻消化。第一，你通过 API 调用的 Claude Opus 4.7 **不受这份 system prompt 约束**——它是 claude.ai 网页端和移动端场景的前置指令。API 调用方拿到的是「裸模型」，需要自己构建 system prompt。CL4R1T4S 这份文件最直接的价值，是作为参考蓝本让 API 调用方了解 Anthropic 在自家产品里是如何做工具路由、版权防护、记忆控制的。第二，这份文件里的「版权硬限制」（15 词引用上限、单信源一次引用）对信源二次加工类 workflow 影响很大，自研 prompt 时可以参考其边界设计。

**对 Prompt 工程与安全研究者**：这份文件是目前能拿到的、最接近真实生产环境的头部厂商 system prompt 样本之一。可以用于：（1）反向工程 Anthropic 对幻觉、谄媚、长对话疲劳等已知问题的缓解策略；（2）研究工具路由决策树的写法（Step 0–3 模式值得借鉴）；（3）作为 prompt injection 攻防研究的新测试对象——注意 Pliny 本人的业务就包括这件事。

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/KgxDGkACWnTGWUWW8dbEIwLS8EuWmib74N7BUzAnhRz83kIf0IUFlrXM9JmW2WhE7MqqgnQTEzjDdwGZf0icHX6A/0?wx_fmt=png)

独眼情报

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/KgxDGkACWnTGWUWW8dbEIwLS8EuWmib74N7BUzAnhRz83kIf0IUFlrXM9JmW2WhE7MqqgnQTEzjDdwGZf0icHX6A/0?wx_fmt=png)

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