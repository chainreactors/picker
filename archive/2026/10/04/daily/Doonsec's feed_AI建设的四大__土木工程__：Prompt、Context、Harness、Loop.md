---
title: AI建设的四大\"土木工程\"：Prompt、Context、Harness、Loop
url: https://mp.weixin.qq.com/s/UcZFyn3l4RgohvhuORk8rA
source: Doonsec's feed
date: 2026-10-04
fetch_date: 2026-10-05T07:54:08.734395
---

# AI建设的四大\"土木工程\"：Prompt、Context、Harness、Loop

# AI建设的四大"土木工程"：Prompt、Context、Harness、Loop

原创

GGDog Sec
GGDog Sec

GGDog Sec

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

这几年 AI 圈的新词换得很快：先是 Prompt Engineering（提示词工程），然后是 Context Engineering（上下文工程），2026 年又冒出 Harness Engineering 和 Loop Engineering。招聘里也跟着出现了 prompt engineer、context engineer 之类的说法。

这些词并不是互相替代的。更准确的看法是：它们描述的是**同一件事的不同层级**——人怎样让大模型可靠地干活。层级越往外，人越少亲自下指令，越多地去设计“让模型自己干活的系统”。

下面按时间顺序逐个说明：怎么流行起来的、核心思想、基本技术、适用场景，以及和前一个概念的关系。

![](https://mmbiz.qpic.cn/mmbiz_png/ibzqXRd1seStPKOUkSNycscxXicA3IrTXbxWOnvrUkbwtHbMVlCMB7fvBDFphfcIMTFnu7nceGSlT4QNNR2xI0Ubshm8qcialfYOuOCvD4ic6zI/640?wx_fmt=png&from=appmsg)

                                                            图 1：四个概念的时间

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ibzqXRd1seStuxgAfnWy6aWibCCGGzMV3cR0TibjB09E6UcBx4YqW9ibLnYIHcQD1P4H09kx9EjibQUL9lXJby6fcYp3nBGUZK38bzOAv3vNWSHs/640?wx_fmt=png&from=appmsg)

    图 2：从内到外，关注的单位越来越大：一条指令 → 一次调用 → 一次运行 → 多次运行

---

## 一、Prompt Engineering：把一句话写好

怎么流行起来的

2020 年 5 月，OpenAI 发布 GPT-3 论文《Language Models are Few-Shot Learners》，展示了一个当时很新的现象：不用重新训练模型，只要在输入里写清任务、再给几个示例，模型就能完成新任务。这让“输入怎么写”第一次变成了一门值得研究的手艺。

2022 年 1 月，Google 的研究者发表思维链（Chain-of-Thought）论文，发现在示例里写出推理步骤，能明显提升模型做数学和推理题的表现。2022 年 11 月 ChatGPT 上线后，普通人都开始和模型对话，“提示词”成了大众话题。2023 年春，Anthropic 一则“Prompt Engineer and Librarian”的招聘广告给出 17.5 万—33.5 万美元的年薪区间，被 Bloomberg 等媒体广泛报道，prompt engineer 一度被当成新职业。

需要说明：Prompt Engineering 这个词没有一个公认的“首创者”，它是随着 GPT-3 到 ChatGPT 这段时间逐渐通用起来的。

核心思想

模型的输出质量很大程度取决于输入的写法。同一个模型，问法不同，结果可以差很多。

基本技术

* 写清角色、任务、约束和输出格式；
* 给示例（few-shot）；
* 让模型分步思考（思维链）；
* 把复杂任务拆成几步，分几次问。

适用场景

一次性的问答、写作、翻译、分类、信息提取。对个人和刚接触 AI 的公司，这是投入最小、见效最快的一层。

局限

它只关注“一段话”。任务一旦需要大量资料、调用工具或多轮执行，光把话写好就不够了。模型变强后，很多提示词技巧也在变得不那么必要。

---

## 二、Context Engineering：决定模型“看到什么”

怎么流行起来的

2025 年 6 月 19 日，Shopify CEO Tobi Lütke 在 X 上说，他更喜欢“context engineering”这个词，因为它更准确地描述了核心技能：“提供所有上下文，让任务对大模型来说有可能被解决”。6 月 25 日，Andrej Karpathy 转发支持，并补充说：在工业级的大模型应用里，context engineering 是“在上下文窗口里为下一步填入恰好合适的信息”的艺术与科学。随后一周内 LangChain、Simon Willison 等纷纷发文跟进。

2025 年 9 月 29 日，Anthropic 发表《Effective context engineering for AI agents》，把它定义为“在推理时筛选和维护最优信息集合的策略”，并明确说 context engineering 是 prompt engineering 的自然延续。

核心思想

模型每次回答，只能依据它“此刻看到的那些 token”。所以真正要设计的不只是一段指令，而是**整个上下文窗口里放什么、不放什么**。Anthropic 那篇文章强调：上下文是有限资源，塞得越多不一定越好，信息太长太杂，模型反而会“分心”。目标是用尽量少、但信号最强的信息，让模型做对。

基本技术

* 检索增强生成（RAG）：根据问题去知识库里找相关资料放进来；
* 规则文件：如 AGENTS.md、CLAUDE.md，把项目约定写成文件，每次自动加载；
* 工具说明：告诉模型有哪些工具、什么时候用（如 MCP）；
* 记忆与压缩：对话太长时做摘要，把关键信息记到外部笔记，需要时再读回来；
* 子智能体：让子任务在独立的上下文里跑完，只把结论交回来。

![](https://mmbiz.qpic.cn/mmbiz_png/ibzqXRd1seSsx3xz0L0QjM91miac7GZMDNLsWX6ASNYFdKEJt8somwEEqNopQ46yfm8DDMBgJvIy4fcULVt4zAGETR5UueR1shrcRvLSRS64o/640?wx_fmt=png&from=appmsg)

  图 3：Prompt Engineering 优化一段话；Context Engineering 决定窗口里放哪些信息

适用场景

企业知识库问答、客服、需要读大量文档的分析任务、多轮对话的助手。对公司来说，“把内部资料整理成模型能用的形式”基本就是这一层的工作。

和 Prompt Engineering 的关系

包含关系。提示词仍然是上下文的一部分，只是不再是全部。Prompt Engineering 管“怎么说”，Context Engineering 管“给它看什么”。

---

## 三、Harness Engineering：给模型搭一套“工作环境”

怎么流行起来的

2026 年 2 月 5 日，HashiCorp 联合创始人 Mitchell Hashimoto 在博客《My AI Adoption Journey》里写道：他不确定行业里有没有公认的说法，自己把这件事叫作“harness engineering”——**每当发现 AI 智能体犯了一个错，就花时间做一个工程上的修补，让它以后再也不犯这个错。**

6 天后（2 月 11 日），OpenAI 工程师 Ryan Lopopolo 发表《Harness engineering: leveraging Codex in an agent-first world》，介绍团队用五个月、几乎不手写代码、全部由 Codex 生成一个内部产品的经验：工程师的主要工作变成了设计环境、明确意图、搭建反馈回路。3 月 10 日，LangChain 的 Vivek Trivedy 发表《The Anatomy of an Agent Harness》，给出后来被广泛引用的公式：**Agent = Model + Harness**——模型之外的所有代码、配置和执行逻辑都算 harness。4 月 2 日，Thoughtworks 的 Birgitta Böckeler 在 martinfowler.com 发文，从“引导（guides）”和“检测（sensors）”两个角度整理了编码智能体的 harness。

说明：harness（原意“挽具”）在软件里早有“测试 harness”等用法；Harness Engineering 作为专门说法是 2026 年 2 月后才流行的，各家对边界的划分不完全一致。

核心思想

模型本身只会“读文字、吐文字”。要让它真正干活——读写文件、运行代码、打开浏览器、跑测试——需要在它外面搭一整套环境。而且这套环境要能**自动告诉它哪里做错了**，让它自己改，而不是靠人一遍遍纠正。

![](https://mmbiz.qpic.cn/mmbiz_png/ibzqXRd1seSt6MiaobtmPeY8W1YsUDKUnMF0D5CQLR4BEiapiaf7pGkRw2F1r2hnUfbyib5aMaboOjl5CsUoE86eHiaibuibPX7L3PR2oFJGzbbcP6k/640?wx_fmt=png&from=appmsg)

  图 4：一次 Agent 运行内部的 harness：规则 + 工具 + 自动检查，失败信息反馈给模型

基本技术

* 规则文件（AGENTS.md）：每一条都对应一个曾经犯过的错；
* 工具与沙箱：终端、文件系统、浏览器，以及限制它能动什么的权限；
* 自动检查：单元测试、Lint、类型检查、截图比对，失败时把报错直接喂回模型；
* 钩子（hooks）：在特定时机强制执行某些动作，比如提交前必须跑测试；

适用场景

AI 编程智能体（Claude Code、Codex、Cursor 等）是最典型的场景；也适用于任何需要模型“动手操作”的任务，比如自动处理表格、操作内部系统。

和 Context Engineering 的关系

包含关系。Böckeler 在文章里直接说，为编码智能体搭 harness 是 context engineering 的一种具体形式。区别在于：Context Engineering 主要关注“一次调用看到什么”；Harness Engineering 关注“一整次智能体运行”——它在循环里调用工具、拿到结果、再调用模型，harness 要管住整个过程，包括可执行的工具和硬性的检查，而不只是信息。

---

## 四、Loop Engineering：设计“替你下指令”的系统

怎么流行起来的

这是四个里最新的说法，出现在 2026 年 6 月初，前后不过几天：

* 6 月 2 日，Claude Code 负责人 Boris Cherny 在一次访谈中说：“我已经不再给 Claude 写提示了，我有一些循环在运行，是它们在给 Claude 下指令……我的工作是写循环。”
* 6 月 7 日，OpenClaw 作者 Peter Steinberger 发帖：“你不该再亲自提示编程智能体了，你应该设计会去提示智能体的循环。”
* 同一时间（6 月 7—8 日，因时区不同各处记录不一），Google 工程师 Addy Osmani 发表博客《Loop Engineering》，把这件事命名并定义为：“不再由你亲自去提示智能体，而是设计一个替你做这件事的系统。”

这之前已有铺垫：2025 年 7 月，Geoffrey Huntley 公开了“Ralph Wiggum”技巧——用一个 shell 循环反复把同一个任务文件喂给编码智能体；2026 年 3—5 月，Claude Code、Codex 等工具陆续加入定时运行（/loop）和“直到满足条件才停”（/goal）之类的命令。6 月下旬吴恩达在 The Batch 里称它为“一个热门流行词”；7 月 Gergely Orosz 在 The Pragmatic Engineer 收集了大量一线反馈，其中也有不少质疑。

需要特别说明：**Loop Engineering 目前没有公认的严格定义**。一篇 2026 年 8 月发到 arXiv 的论文（Lulla 等，投稿 ASE 2026 研讨会、尚在评审）专门梳理了相关讨论，结论是：大家对“一个好循环应该包含什么”看法比较一致，但对它算不算新东西争议很大——有人认为这就是“换了皮的 cron 定时任务”，也有人认为它只是过渡阶段，很快会被工具内置。还有人用 loop engineering 指单次运行内部的“思考—行动—观察”循环，和上面的用法不同。本文采用 Osmani 和这篇论文的主流用法。

核心思想

前三层，人始终是那个“发下一条指令”的人。Loop Engineering 把这个角色也交出去：人设计一个循环，由它决定什么时候启动智能体、做什么、怎么验收、什么时候停、什么时候找人。论文里的概括是：harness 装备的是“一次运行”，loop 管理的是“随时间反复发生的多次运行”。

![](https://mmbiz.qpic.cn/mmbiz_png/ibzqXRd1seSviaApHcOM8QSOcuuHdE0OyGjk1oV2ULY9icwfvIa3agm5Dr9v6MeAz22YkxibdYyTJNibiaYFpqv8ZgfuUAicegRyprbWZrQ96OJpeY/640?wx_fmt=png&from=appmsg)

图 5：一个典型的 loop：触发 → 读状态 → 计划 → 执行 → 检查 → 判断是否停止或升级给人

基本技术

按 Osmani 和上述论文的归纳，一个像样的循环通常包括：

* 触发器：定时（每天早上跑一次）或事件（CI 失败、新开了 issue）；
* 机器可检查的停止条件：如“test/auth 下的测试全部通过且 Lint 干净”；
* 状态文件：记录做过什么、还剩什么，因为模型每次都会“忘记”，所以记忆要放在磁盘上；
* 生成与验收分离：写代码的智能体和打分的智能体分开，避免“自己批改自己的作业”；
* 并行隔离：如 git worktree，让多个智能体互不踩文件；
* 预算和刹车：限制 token 花费、检测“原地打转”，超出就停下交给人。

适用场景

重复、可验证的工作：每日 issue 分类、修复不稳定的测试、批量依赖升级、渐进式代码迁移。前提是结果能被机器自动判断对错；判断不了的，循环跑得越快，堆积的待审工作越多。

和 Harness Engineering 的关系

包含关系。循环里的每一次“执行”，内部就是一个带 harness 的智能体运行。Osmani 的原话是：Loop Engineering 在 harness 之上“再高一层”。

需要注意的问题

Osmani 本人也有保留：token 成本可能失控；无人看管的循环也在无人看管地犯错；产出越快，人对系统的理解越容易跟不上。上述论文扫描了 3.6 万多个开源仓库，确认 217 个在运行智能体循环，多是自动审 PR 和定时整理 issue。总体看，这个领域还很早，收益多来自个人经验分享，缺少系统性证据。

---

## 五、四者放在一起看

四者的嵌套关系见图 2，对比如下：

|  | Prompt | Context | Harness | Loop |
| --- | --- | --- | --- | --- |
| 流行时间 | 2020—2023 | 2025 年中 | 2026 年 2 月 | 2026 年 6 月 |
| 关注单位 | 一条指令 | 一次模型调用 | 一次 Agent 运行 | 反复的多次运行 |
| 核心问题 | 怎么说 | 给它看什么 | 给它什么工具和检查 | 谁来触发、何时停 |
| 典型产物 | 提示词模板 | 知识库、规则文件、记忆 | 工具、测试、钩子、权限 | 定时任务、停止条件、状态文件、预算 |
| 人的角色 | 每次亲自提问 | 准备资料 | 搭环境、补规则 | 设计流程、处理升级 |

几点补充：

1. **外层不取代内层。**

   一个循环里仍然有 harness，harness 里仍然要管上下文，上下文里仍然有提示词。学习顺序也应该从内往外。
2. **越往外，越依赖“能自动验收”。**

   提示词写得一般，人看一眼就能改；循环无人值守，验收标准写不清，错误就会被放大。
3. **名词会继续变。**

   2026 年 7 月已有人发文称“Loop Engineering 已死，进入 Graph Engineering”。与其追名词，不如弄清每一层要解决的具体问题。

预览时标签不可点

不喜欢

![]()

微信扫一扫
关注该公众号

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/MfzQWQrwshBcIYlNv52yH4dKhZx5TvmwNLKmKiajbPbmsjrRgcebV83tMJP6DLDJsbE34otCpG854JhQoNTfLKg/0?wx_fmt=png)

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