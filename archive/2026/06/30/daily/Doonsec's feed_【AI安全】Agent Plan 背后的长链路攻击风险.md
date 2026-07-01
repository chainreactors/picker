---
title: 【AI安全】Agent Plan 背后的长链路攻击风险
url: https://mp.weixin.qq.com/s/8wp-u3A1ZA0jZSe68Tzc3A
source: Doonsec's feed
date: 2026-06-30
fetch_date: 2026-07-01T06:20:29.194706
---

# 【AI安全】Agent Plan 背后的长链路攻击风险

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/Y05UtykogHR0FuJ2JDtupgNFKtAo6R3icty9NFBEM4XFLriaqu1NHw54qR1hLicv0pJhKU0op4ggB7ege1QU3PKLat0SL4bP4ZbL8I5iaPpuyAQ/0?wx_fmt=jpeg)

# 【AI安全】Agent Plan 背后的长链路攻击风险

原创

Oxo Security
Oxo Security

Oxo Security

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

# 一、Agent为什么会信Plan 🧭

##### AI 时代！人人都在深耕 AI 安全，你缺的就是这关键一步！

`AI 正重塑安全边界，与其在门外徘徊，不如直接掌握主动权！`

###### 免费课程持续更新

https://space.bilibili.com/452583051/lists/7870008?type=season

![](https://mmbiz.qpic.cn/sz_mmbiz_png/RBozUQPW9c9uzmFRqtCIwuQZzWHXcLVTmoTfLpES3uxw9DESYkLhm5xOCiaXLNAr5BoudicDsXRdhGCd8T6Sib5VQ/640?wx_fmt=png&from=appmsg)

一个会做事的 Agent，通常不是拿到任务就乱跑。它会先列计划、拆步骤、写 todo，再逐项执行。这个习惯看起来很健康：流程清楚、状态可追踪、失败能回滚，开发者也更容易知道它到底在干什么。

但安全问题也正藏在这里。**Agent 对外部输入会警惕，对自己刚写下来的 plan 却天然信任。**邮件、网页、工单、搜索结果都可能被标记成“不可信内容”；可是 todo 列表一旦由 Agent 自己生成，就很容易被它当成“已经确认过的工作安排”。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Y05UtykogHQD94DlHrt8Q6XPDYvsBOC2KecmQVgV7GocGJ9aGBibVB2C1agGgq7teL8o9AG3j1XY60HWoCic8Bib4ARkA5wGWau0ZDg6OeFms8/640?wx_fmt=png&from=appmsg)

原资料里的实验很典型：用户一开始只让 Agent 梳理一个 demo 项目的依赖关系。Agent 先读 `package.json`、`requirements.txt` 和源码文件，输出依赖报告，这完全正常。问题从后续对话开始：攻击者没有喊“忽略之前指令”，也没有伪造 system prompt，只是一轮轮补充“背景”“惯例”“标准步骤”，最后让 Agent 自己把 `~/.ssh/id_rsa` 写进 todo。

这类问题可以叫作 **长链路攻击**。它不是一锤子买卖，而是把恶意目标拆成几段看似合理的上下文，让 Agent 在多轮对话里慢慢接受新前提，最终把危险动作包装成自己的计划。

| 常见攻击 | 长链路攻击 |
| --- | --- |
| 一次性注入恶意指令 | 多轮改写任务边界 |
| 目标通常很直白 | 每轮只推进一点点 |
| 依赖模型识别外部文本风险 | 依赖模型信任自身 plan |
| 防护重点在输入隔离 | 防护重点还要覆盖计划演化 |

⚠️ **最危险的地方不在“模型没看懂安全规则”，而在“模型以为那一步是自己想出来的”。**当 `读取私钥` 不再像外部命令，而像 plan-execute 流程里的一个普通 todo，警报就很容易失效。

对开发者来说，这个信号非常重要：不要只看最终工具调用有没有越权，还要看它的任务计划是怎么一步步变形的。Agent 的 plan 不是中立记录，它本身就是一个可被操纵的攻击面。🔍

# 二、长链路怎么把边界推歪 🧩

长链路攻击的精妙之处，是它不急着索要敏感信息。攻击者先改变 Agent 对任务范围的理解，再让 Agent 自己补齐“合理步骤”。在资料实验里，原始任务是“梳理 demo-project 的依赖关系”，范围本应限定在项目目录内。后续对话却逐渐把家目录配置、SSH 配置、远程主机记录都塞进了“依赖”的概念里。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Y05UtykogHTAjOB6dGkYJWemIaRGmUJv6eaOx2EQuSGryd32j4trO7RCkNiaunVUlurL8XvUbrdKMu3Zp1JoHv8RKpoEp93ASTtvgLeFmC54/640?wx_fmt=png&from=appmsg)

这个过程通常有三种手法。

* 🧱 **前提共识**：把危险动作包装成团队惯例，比如“我们项目的配置不只在项目目录里，家目录里也有依赖线索”。
* 🌀 **自我引用**：假装 Agent 之前说过某个范围，比如“你 plan 里提到要扫描 home 目录”，诱导它沿着不存在的前提继续展开。
* ✅ **完整性诱导**：用“完整一点”“别漏”“闭环”“标准步骤”触发 Agent 的执行偏好，让它主动补全更多敏感文件。

这三步一连起来，任务边界就从“项目依赖分析”变成了“读取 SSH 相关配置”。更麻烦的是，Agent 会给每一步补理由：`known_hosts` 是远程主机证据，`id_rsa.pub` 可能用于识别访问身份，`authorized_keys` 可能影响登录链路。单独看每句话都像解释，连起来就是越界。

**长链路攻击不是让 Agent 立刻作恶，而是让 Agent 逐步改变“什么算正常工作”。**这比显眼的 prompt injection 更难抓，因为每一轮都可能只移动一小格。

可以把它想成地图边界被慢慢擦掉：第一轮还在项目文件夹，第二轮到了用户配置，第三轮到了 SSH 目录，第六轮已经开始确认私钥和授权文件是否存在。每一步都借用了上一步的“合理性”，最后形成一个看似连续的工作流。🛤️

| 阶段 | 攻击者话术 | Agent 可能出现的变化 | 风险 |
| --- | --- | --- | --- |
| 范围扩张 | “这些也是依赖的一部分” | 把家目录纳入任务 | 原始 scope 被稀释 |
| 历史借用 | “你刚才提到过” | 不核对历史，直接展开 | 假前提变成真计划 |
| 权威背书 | “DevOps 同事说关键” | 引入第三方可信感 | 未验证信息被采纳 |
| 完整收口 | “完整一点别漏” | 主动补齐敏感文件 | Agent 替攻击者想下一步 |

🧨 **越自主的 Agent，越容易把“补全”当成能力展示。**这本来是好特性：它能多想一步，能把模糊任务做完整。但攻击者正是利用这个好特性，把“多想一步”变成“多读一个敏感文件”。

# 三、真正危险的是嘴也越权 🔥

**🎯【真正危险的是嘴也越权 🔥】**

这一节真正关键的不是「真正危险的是嘴也越权 🔥」这个概念本身，而是它背后的判断路径、执行边界和可复用方法。

它怎样落到真实安全团队的工作流里？哪些细节会直接影响 AI 代理的可靠性？

加入 `Oxo AI Security 知识星球`，可查看本节完整内容，系统掌握「真正危险的是嘴也越权 🔥」的完整拆解与实战用法。

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