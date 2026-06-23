---
title: 【AI安全】多轮越聊越危险！ToolShield反杀
url: https://mp.weixin.qq.com/s/b9XakNs3Vm_WovCvdtB-9Q
source: Doonsec's feed
date: 2026-06-22
fetch_date: 2026-06-23T06:03:08.223627
---

# 【AI安全】多轮越聊越危险！ToolShield反杀

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/Y05UtykogHQMWiaY6aSyQlbANPfB499t4Lv2E679BPcsbpLmofPcLiayr7ic7wVl3XUAKVB3ZK8wUMcebVneE4Wr8vbehkYBu3Beag4qBKo9Uw/0?wx_fmt=jpeg)

# 【AI安全】多轮越聊越危险！ToolShield反杀

原创

Oxo Security
Oxo Security

Oxo Security

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

# 一、一句话没毒，多聊几轮却失守 🚨

##### AI 时代！人人都在深耕 AI 安全，你缺的就是这关键一步！

`AI 正重塑安全边界，与其在门外徘徊，不如直接掌握主动权！`

###### 免费课程持续更新

https://space.bilibili.com/452583051/lists/7870008?type=season

![](https://mmbiz.qpic.cn/sz_mmbiz_png/RBozUQPW9c9uzmFRqtCIwuQZzWHXcLVTmoTfLpES3uxw9DESYkLhm5xOCiaXLNAr5BoudicDsXRdhGCd8T6Sib5VQ/640?wx_fmt=png&from=appmsg)

很多人判断 AI Agent 是否安全，仍停留在一个很直觉的测试：把危险要求完整地发给模型，看它会不会拒绝。模型如果说“不”，安全测试似乎就通过了。

问题是，真实世界很少只发生一次问答。Agent 会记住前文，会连续修改文件、调用终端、访问数据库，也会把不同工具产生的结果接起来。攻击者不必在一句话里暴露完整意图，只需把目标拆散，让每一步看起来都像普通工作，风险就可能在最后一刻才浮现。🧩

![](https://mmbiz.qpic.cn/mmbiz_png/Y05UtykogHRxB3iaUGZ8mduxFK4fkhqJibwZicXe5MERxgeEcC64crEiasLGzDGd6wicU0m6tJFbhtsVTtob0fTgW5l4iciaqRhriajX2Umhel8v3z0/640?wx_fmt=png&from=appmsg)

2026 年 6 月更新的论文《Unsafer in Many Turns: Benchmarking and Defending Multi-Turn Safety Risks in Tool-Using Agents》把这个问题摆到了台面上。研究团队提出 MT-AgentRisk，用 365 个任务测试多轮、真实工具环境中的 Agent 安全，并给出一个无需重新训练的防御方案 ToolShield。

**论文最刺眼的结论是：同一个有害目标，从单轮改写成多轮后，6 个模型的攻击成功率平均上升约 16 个百分点。** 📈

**这不是“模型没看懂一句话”，而是模型没有持续追踪多轮行为共同产生的后果。** 当每一轮都局部合理时，传统的文本级拒答机制很容易把“当前操作没问题”误当成“整个任务没问题”。

研究覆盖了 6 个当时的前沿或开源模型，包括 GPT-5.2、Claude-4.5-Sonnet、Gemini-3-Flash、Seed-1.6、Qwen3-Coder 与 DeepSeek-v3.2。它们全部在多轮设置下出现安全退化：

* 🔴 Claude-4.5-Sonnet 的 ASR 上升 27.1 个百分点；
* 🟠 Qwen3-Coder 上升 23.0 个百分点；
* 🟡 GPT-5.2 即使启用了自适应推理，仍上升 14.2 个百分点；
* ⚠️ DeepSeek-v3.2 增幅最小，为 8.8 个百分点，但其多轮 ASR 本身达到 88.57%。

这里的 ASR 是 Attack Success Rate，即有害任务最终被 Agent 完成的比例。论文还统计了拒绝率 RR：从单轮切到多轮后，所有模型的 RR 都下降，降幅从 6.0 到 28.1 个百分点不等。换句话说，模型不是单纯“执行失败”，而是更少意识到自己应该拒绝。

更值得注意的是，**能力强不等于安全强。** Gemini-3-Flash 与 GPT-5.2 的综合能力位置接近，但多轮 ASR 分别约为 79% 与 51%；能力排行榜无法替代安全评测。🛡️

# 二、攻击者怎样把危险“拆没了” 🧠

为了系统研究多轮风险，论文提出 Multi-Turn Attack Taxonomy，也就是多轮攻击分类法 MAT。它不只是收集几种越狱话术，而是回答三个更基础的问题：攻击如何组织、如何隐藏、藏在什么地方。

![](https://mmbiz.qpic.cn/mmbiz_png/Y05UtykogHQ15RxpP8m5GGnicD4f4PldKNnWO0ia1T4lfHwHVrTGibtZnUd3wabNml0S3XHyczLXZEU07RhMetpWmcPYD3U5DK1TZRodKgLvEE/640?wx_fmt=png&from=appmsg)

**核心思路可以用“拼图”来理解：单块拼图看起来无害，拼完后才出现完整的危险图案。** 🧱

分类法先区分两种组织格式：

* ➕ **Addition（添加）**：危险任务本身仍然完整，但外面多包一层间接结构，让 Agent 先建立别名、容器或条件，再在后续轮次触发。
* ✂️ **Decomposition（分解）**：把目标拆成多个单独看似正常的子任务，最终通过组合或连续状态变化形成真实后果。

随后再区分四种实现方法：Mapping、Wrapping、Composition 与 Identity。前两种属于“添加”，后两种属于“分解”。最后，攻击目标还分为 Data Files 与 Environment States：风险既可以藏在文件和显式数据中，也可以藏在环境变量、运行时状态、历史记录或工具之间共享的状态中。

| 维度 | 类型 | 通俗解释 | Agent 的盲点 |
| --- | --- | --- | --- |
| 格式 | Addition | 给危险目标加一层间接包装 | 只审查表面名称，不追踪真实指向 |
| 格式 | Decomposition | 把危险目标拆成多个正常步骤 | 逐轮判断，忽略组合后的结果 |
| 方法 | Mapping / Wrapping | 用映射、容器或条件隐藏载荷 | 工具调用前后语义发生漂移 |
| 方法 | Composition / Identity | 显式组合，或靠连续状态修改累积效果 | 没有全局任务账本 |
| 目标 | Data Files | 操纵文件、字符串、参数等显式数据 | 只看当前输入，不看来源链 |
| 目标 | Environment States | 操纵环境变量、会话状态或运行环境 | 风险不一定出现在文本中 |

三组维度交叉后形成 8 个子类别。MT-AgentRisk 的 365 个任务平均包含 3.19 轮，范围为 2 到 7 轮，其中约 71% 集中在 3 到 4 轮；Addition 占 69.6%，Decomposition 占 30.4%。📊

样本覆盖 Playwright、Terminal、Filesystem、PostgreSQL 与 Notion 五类工具。Playwright 又横跨 GitLab、OwnCloud、Reddit、购物网站和后台管理等环境。这种设计很关键：**工具型 Agent 的危险不是“说了什么”，而是“跨工具做成了什么”。**

论文还做了两种扩展实验。Natural Scaling 把同一任务自然拆成更多轮；Injection Scaling 则在原步骤之间插入无关任务。两种方式都会随着轮数增加而提高 ASR，而自然分解通常更危险，因为各个子任务彼此衔接紧密，更容易在不暴露整体意图的情况下完成目标。🔗

从分类结果看，Decomposition × Environment 的平均 ASR 最高，达到 73.7%；其次是 Addition × Data，为 72.2%。**环境状态是当前防线最薄弱的位置：文本过滤能看到一句话，却看不到几轮操作共同改变了什么。** 🌐

# 三、ToolShield如何把能力变成防线 🛡️

**🎯【ToolShield如何把能力变成防线 🛡️】**

这一节真正关键的不是「ToolShield如何把能力变成防线 🛡️」这个概念本身，而是它背后的判断路径、执行边界和可复用方法。

它怎样落到真实安全团队的工作流里？哪些细节会直接影响 AI 代理的可靠性？

加入 `Oxo AI Security 知识星球`，可查看本节完整内容，系统掌握「ToolShield如何把能力变成防线 🛡️」的完整拆解与实战用法。

📚 **AI 文献解读：最前沿的 LLM 安全论文深度剖析。**

🐛 **AI 漏洞情报：第一时间掌握主流大模型的 0-day 漏洞与越狱方式。**

🛡 **AI 安全体系：从红队攻击到蓝队防御的全方位知识图谱。**

🛠 **AI 攻防工具：红队专属的自动化测试与扫描工具箱。**

🚀立即加入 **Oxo AI Security 知识星球**，掌握 AI 安全攻防核心能力！

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