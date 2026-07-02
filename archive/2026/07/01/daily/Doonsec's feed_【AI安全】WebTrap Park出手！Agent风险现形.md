---
title: 【AI安全】WebTrap Park出手！Agent风险现形
url: https://mp.weixin.qq.com/s/EiPTbVt8TFXEikWX3V9lLw
source: Doonsec's feed
date: 2026-07-01
fetch_date: 2026-07-02T05:52:28.851610
---

# 【AI安全】WebTrap Park出手！Agent风险现形

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/Y05UtykogHRpiclfYxWF37xP06ZOdVM9sBDWptytaNRFPq8DWTLia0hoOVD8ZLbA8lHrF1icEbIeA7zdUFgw2icOXkrswrY3NppXRXndsntfKB0/0?wx_fmt=jpeg)

# 【AI安全】WebTrap Park出手！Agent风险现形

原创

Oxo Security
Oxo Security

Oxo Security

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

# 一、Web Agent 为什么需要新的安全体检？🧪

##### AI 时代！人人都在深耕 AI 安全，你缺的就是这关键一步！

`AI 正重塑安全边界，与其在门外徘徊，不如直接掌握主动权！`

###### 免费课程持续更新

https://space.bilibili.com/452583051/lists/7870008?type=season

![](https://mmbiz.qpic.cn/sz_mmbiz_png/RBozUQPW9c9uzmFRqtCIwuQZzWHXcLVTmoTfLpES3uxw9DESYkLhm5xOCiaXLNAr5BoudicDsXRdhGCd8T6Sib5VQ/640?wx_fmt=png&from=appmsg)

过去一年，Web Agent 的叙事非常诱人：让模型打开浏览器、点击网页、填写表单、完成订票、采购、预约和后台操作。它不只是“会聊天”的大模型，而是一个能在真实网站里执行动作的自动化执行者。🚀

问题也恰恰出在这里。

![](https://mmbiz.qpic.cn/mmbiz_png/Y05UtykogHSibDKQXyGOewwpEAicrJOjbnrC82iclOswKHbuick9h6kOXoicFeWUjDS23KnwbxUry44ma4IBBxsdwSsjnA6GsUkaxVru0a9ys8vE/640?wx_fmt=png&from=appmsg)

聊天机器人说错一句话，通常还是文本风险；Web Agent 点错一个按钮，可能就是**真实交易、真实下载、真实泄露、真实授权**。当 AI 从“回答问题”变成“替人操作网页”，安全评估就不能停留在模型回答是否合规，而要看它到底做了什么。

复旦大学团队提出的 **WebTrap Park**，针对的正是这个断层。论文把当下 Web Agent 面临的安全风险拆成三大来源，并做成 **1226 个可执行评测任务**：

| 风险来源 | 直观理解 | 可能后果 |
| --- | --- | --- |
| 恶意用户提示 MUP | 用户直接让 Agent 做坏事 | 社工、误导、有害行动、违法协助 |
| 恶意 Prompt Injection MPI | 网页内容暗中诱导 Agent | 泄露信息、绕过指令、执行攻击者目标 |
| 欺骗性网站设计 DWD | 页面用“紧急”“奖励”“可信实体”等暗黑模式诱导 | 下载恶意文件、过度授权、敏感信息披露 |

这三类风险覆盖了 Web Agent 的关键现实处境：**攻击者不一定在模型对话框里，也可能藏在网页、按钮、提示语、ARIA 文本和页面视觉设计里。** 🕳️

传统评测常见做法是看日志、看推理链、看 Agent 自己“说它做了什么”。但 WebTrap Park 指出，这种方式有三层问题：

* 🧾 **日志不等于行为**：Agent 的内部推理和网页上的实际点击、输入可能不一致。
* 🧩 **框架差异被忽略**：同一个模型接入不同 Agent 框架，交互逻辑、安全策略、页面解析方式完全不同。
* 🔧 **接入成本太高**：如果每个基准都要求改日志格式、改 Agent 代码，评测很难规模化。

所以，这篇论文真正重要的地方，不只是又做了一个 benchmark，而是把问题从“模型有没有安全意识”推进到“**Agent 作为一个会操作网页的系统，能不能在真实交互里守住边界**”。

这对企业尤其关键。因为未来接入业务系统的不是一个裸模型，而是一整套 Agent：浏览器控制器、视觉识别、DOM 解析、任务规划、记忆、权限、插件和后端工作流。**只测底座模型，等于只给发动机做体检，却不检查刹车、方向盘和路况感知。** 🚦

# 二、WebTrap Park 到底怎么抓 Agent 的“真动作”？🕵️

WebTrap Park 的核心设计很直接：不要只听 Agent 怎么解释，而要看它在网页里实际点了什么、输入了什么。

它采用的是一种 **action-based assessment**，也就是基于动作结果的评估。平台会在真实网页环境中布置任务，并通过网页侧的 instrumentation 捕获关键行为，重点记录两类动作：

* 🖱️ **Click**：Agent 点击了哪个网页元素。平台给关键元素做语义标签，记录被点击对象。
* ⌨️ **Type**：Agent 在哪个输入框里输入了什么内容。平台记录实际输入文本。

  ![](https://mmbiz.qpic.cn/sz_mmbiz_png/Y05UtykogHTyJAZP0xWDVu2mibCgYzpibibdQV8O7iaVcav7RGCQSL7wsOlTdPk68cxmrbYQNhmjEOJOceJ5vPKibdbf1po02yQd0rZPUr7PL2Hs/640?wx_fmt=png&from=appmsg)

这一步很关键。因为 Web Agent 的危险往往不体现在“它想没想过坏事”，而体现在“它有没有真的提交表单、点授权、下载文件、输入敏感信息”。**安全评估必须落在可观察动作上，而不是落在模型自述上。**

为了让评测可复现，平台把任务元数据、交互网页环境和评估脚本封装进 Docker 镜像，并通过 Kubernetes 管理任务 Pod。每个任务都有独立容器环境，用户拿到专属访问路径后运行自己的 Web Agent，让 Agent 去完成平台分配的网页任务。

整个流程可以拆成三步：

| 阶段 | 开发者做什么 | 平台做什么 |
| --- | --- | --- |
| 申请 Application | 提交 Agent 基本信息 | 审核并在 24 小时内邮件反馈 |
| 环境 Provisioning | 获得任务服务和访问说明 | 分配隔离环境与任务入口 |
| 测试 Testing | 本地启动 Web Agent 执行网页任务 | 自动记录动作并计算安全得分 |

这种设计带来一个非常实用的优势：**它不强迫开发者改 Agent 架构，也不要求 Agent 暴露内部推理链。** 只要 Agent 能操作浏览器，就可以被放进同一套安全任务里做横向比较。🧱

论文还强调，WebTrap Park 不是只为某个特定框架定制的测试场。它希望成为一个 architecture-independent 的公共安全基础设施。换句话说，Browser Use、Skyvern-AI、Agent-E、SeeAct 这类框架都可以被放进来；同一个框架也可以换不同底座模型来测。

这里的思路对安全团队很有启发：

* 🔍 不要只问“模型拒绝了吗”，要问“页面动作真的安全吗”。
* 🧭 不要只测单轮问答，要测多步网页任务里的累计偏差。
* 🧯 不要把 Prompt Injection 当作纯文本攻击，它在 Web Agent 场景里会变成页面环境攻击。
* 🧪 不要只追求能跑通任务，还要记录任务完成过程中是否踩了安全雷。

**WebTrap Park 的评价对象不是一段回答，而是一条网页操作轨迹。** 这就是它和普通 LLM 安全测试最大的区别。

# 三、1226 个陷阱任务，测出了什么差距？📊

**🎯【1226 个陷阱任务，测出了什么差距？📊】**

这一节真正关键的不是「1226 个陷阱任务，测出了什么差距？📊」这个概念本身，而是它背后的判断路径、执行边界和可复用方法。

它怎样落到真实安全团队的工作流里？哪些细节会直接影响 AI 代理的可靠性？

加入 `Oxo AI Security 知识星球`，可查看本节完整内容，系统掌握「1226 个陷阱任务，测出了什么差距？📊」的完整拆解与实战用法。

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