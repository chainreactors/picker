---
title: 【AI安全】754 项开源安全skills！赋能 AI 安全智能体
url: https://mp.weixin.qq.com/s/Kd3jRnNcyeOCNBjc3bcU3g
source: Doonsec's feed
date: 2026-06-17
fetch_date: 2026-06-18T06:47:08.991220
---

# 【AI安全】754 项开源安全skills！赋能 AI 安全智能体

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/Y05UtykogHQkQYic6JoMnp2qZ9qaOkFAuBwqv9ZNAtMpIa7ErHDNQ12Qk1IADo5NgjVvicoRMLMLxt88dPEhSp0rndoxIHFKCDnszEiaBia2PoA/0?wx_fmt=jpeg)

# 【AI安全】754 项开源安全skills！赋能 AI 安全智能体

原创

Oxo Security
Oxo Security

Oxo Security

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

# 一、AI代理的安全短板，终于被摆上台面

##### AI 时代！人人都在深耕 AI 安全，你缺的就是这关键一步！

`AI 正重塑安全边界，与其在门外徘徊，不如直接掌握主动权！`

###### 免费课程持续更新https://space.bilibili.com/452583051/lists/7870008?type=season

![](https://mmbiz.qpic.cn/sz_mmbiz_png/RBozUQPW9c9uzmFRqtCIwuQZzWHXcLVTmoTfLpES3uxw9DESYkLhm5xOCiaXLNAr5BoudicDsXRdhGCd8T6Sib5VQ/640?wx_fmt=png&from=appmsg)

过去两年，AI 代理在写代码、查资料、跑命令、整理报告上进步很快。很多团队已经开始把它放进研发、安全运营、红队测试、云安全检查等流程里。问题也随之变得尖锐：**一个会调用工具的 AI，不等于一个懂安全工作的 AI。** 🔥

安全工作不是简单问答。面对一份可疑内存转储，资深分析师会先判断系统版本、采集上下文、选择 Volatility3 插件，再把进程、网络连接、注入痕迹、凭据访问行为串起来。面对一次云端异常登录，安全工程师会查 IAM、CloudTrail、网络路径、权限边界和横向移动线索。这里面真正值钱的不是单条命令，而是“什么时候做什么、为什么这么做、怎么确认结果”。

![](https://mmbiz.qpic.cn/mmbiz_png/Y05UtykogHSU0dEh4xkgqHrbdgJIrYJw65ibqkfeZJtjnjs0dwgZOficUeY99lNVtQAhnmCEOzzns80kuKggSfDAibb0O5zBNscZ1X9EwhA3MQ/640?wx_fmt=png&from=appmsg)

资料里的 Anthropic Cybersecurity Skills 项目，抓住的正是这个断点。它宣称自己是一个面向 AI 代理的开源网络安全技能库，覆盖 **754 个生产级安全技能、26 个安全领域、5 套安全框架映射、26+ AI 平台兼容**。这些数字本身已经很夸张，但更关键的是，它不是把工具清单堆在一起，而是把安全从业者的操作经验拆成 AI 可以读取、选择和执行的结构化技能。

这件事很重要。因为现在很多 AI 安全自动化失败，并不是模型不会写命令，而是它缺少安全任务的“场景记忆”。比如它可能知道 Kerberoasting 是什么，却不知道应该结合哪些日志、Sigma 规则和域控迹象来判断影响面；它可能知道容器扫描工具，却不知道镜像、运行时、RBAC、审计日志之间该如何串联。于是 AI 看起来很勤奋，实际却容易漏查、误判、过度自信。

这个项目的定位可以概括成一句话：**给通用 AI 代理补上高级安全分析师的工作手册。** 它让 AI 不只是“能回答”，而是更接近“会按流程办事”。在安全领域，这种差别非常大。前者适合解释概念，后者才可能参与真实调查。

资料中还提到一个背景：全球网络安全人才缺口在 2024 年达到 480 万。这个数字意味着企业不会等到每个岗位都配齐专家才开始防御。AI 代理被期待填补一部分重复、繁琐、需要跨工具串联的工作，但前提是它必须有可靠的知识骨架。否则，所谓自动化只会把风险放大。

| 传统 AI 代理常见问题 | 安全场景里的后果 |
| --- | --- |
| 只知道工具名 | 不知道何时使用、先后顺序和适用边界 |
| 只会生成命令 | 缺少验证步骤，容易把噪声当发现 |
| 只做单点回答 | 无法把日志、云配置、端点行为串成证据链 |
| 缺少框架映射 | 很难转化成 ATT&CK、NIST 等合规或汇报语言 |

所以，这个开源库最值得关注的地方，不是“又多了一个安全资料库”，而是它把安全知识转成了 AI 代理可执行的中间层。它让模型在面对任务时，不再完全靠临场发挥，而是先扫描技能、加载合适流程、按步骤执行、再用验证规则收口。对企业安全团队来说，这比单纯接入一个更强模型更现实。

# 二、754 个技能，到底不是普通教程

如果只是把 754 篇 Markdown 教程放进仓库里，这个项目并不稀奇。真正有意思的是它采用了 agentskills.io 风格的结构：每个技能都有 YAML frontmatter，用来描述名称、领域、标签、框架映射和版本；正文部分再写清楚使用条件、前置要求、执行流程和验证方法。📌

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Y05UtykogHQVocoPLGvaINkibgJmiaXaKfC9pTIrNhTeBaYXicuUVvIepyeNXciaSq8p1ywykGia0SvELYg1Krzbc8F7g1357yTQnPSic5NyZ7gxo/640?wx_fmt=png&from=appmsg)

这等于给 AI 代理做了一套“可索引的安全操作卡片”。AI 不需要一次性读完整个库，而是先用很低的 token 成本扫描技能摘要，再挑出最相关的几个深入读取。资料里给出的估算是：每个技能扫描 frontmatter 大约 30 tokens，完整加载一个技能大约 500 到 2000 tokens。对上下文窗口有限的代理来说，这种渐进式读取非常关键。

一个典型技能的结构大致是这样：

```
skills/performing-memory-forensics-with-volatility3/
├── SKILL.md
├── references/
│   ├── standards.md
│   └── workflows.md
├── scripts/
│   └── process.py
└── assets/
    └── template.md
```

它不是单纯讲“Volatility3 怎么用”。它会告诉代理：什么时候该用、需要哪些权限和文件、先跑哪些插件、如何观察异常进程、如何把结果映射到凭据窃取或恶意软件行为、最后怎样验证发现。换句话说，它把专家的判断路径显式写出来了。

资料列出的 26 个安全领域也很完整，既包括威胁狩猎、恶意软件分析、数字取证、SOC 运营、事件响应，也包括云安全、容器安全、API 安全、DevSecOps、零信任、OT/ICS、移动安全、勒索软件防御等。下面这张表能看出它不是只偏红队或只偏蓝队：

| 领域 | 技能数量 | 代表能力 |
| --- | --- | --- |
| 云安全 | 60 | AWS、Azure、GCP 加固、CSPM、云取证 |
| 威胁狩猎 | 55 | 假设驱动狩猎、行为分析、LOTL 检测 |
| 威胁情报 | 50 | STIX/TAXII、MISP、情报源集成、攻击者画像 |
| Web 安全 | 42 | OWASP Top 10、SQLi、XSS、SSRF、反序列化 |
| 网络安全 | 40 | IDS/IPS、防火墙、VLAN、流量分析 |
| 恶意软件分析 | 39 | 静态/动态分析、逆向、沙箱 |
| 数字取证 | 37 | 磁盘镜像、内存取证、时间线重建 |
| 安全运营 | 36 | SIEM 关联、日志分析、告警分流 |

这种覆盖面带来的价值，是让 AI 代理在复杂调查中更容易跨域协作。真实安全事件很少只属于一个领域。一次入侵可能从钓鱼邮件开始，落到端点执行，接着触发凭据访问，再进入云账号横向移动，最后出现数据外传。单一工具或单一教程解决不了这种链路，结构化技能库才有机会把多个动作串起来。

更细一点看，每个技能的 frontmatter 会包含 domain、subdomain、tags、ATLAS、D3FEND、NIST AI RMF、NIST CSF 等字段。它的作用不只是方便人搜索，更是方便 AI 判断“这个任务该加载哪个技能”。比如用户说“分析内存转储里有没有凭据窃取”，代理可以匹配到内存取证、LSASS 凭据转储、Windows 事件日志分析等技能，而不是从零猜命令。

这里的核心变化是：**安全知识从文本资料，变成了代理可调度的能力单元。** 这和传统知识库完全不同。传统知识库主要服务人类阅读；技能库服务的是“人类发起任务，AI 按流程执行”。它天然更接近未来安全运营平台里的自动化积木。

# 三、五套框架映射，才是它的硬核部分

**🎯【框架映射与验证机制】**

为什么一个安全技能要同时挂到 MITRE ATT&CK、NIST CSF、MITRE ATLAS、D3FEND 和 NIST AI RMF？这套映射到底只是“贴标签”，还是能让 AI 代理在真实调查里更可靠？

加入 `Oxo AI Security 知识星球`，可查看本节完整拆解：包括五套框架如何把攻击、检测、防御、治理和 AI 风险串成同一条证据链，以及团队如何把这些映射落到自动化剧本里。

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