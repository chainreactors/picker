---
title: AI Agent十大安全风险！OWASP首份框架出炉
url: https://mp.weixin.qq.com/s/IYHb6Zc7un3mslUeBgl1nw
source: Doonsec's feed
date: 2026-04-23
fetch_date: 2026-04-24T04:50:27.027597
---

# AI Agent十大安全风险！OWASP首份框架出炉

![cover_image](http://mmbiz.qpic.cn/mmbiz_jpg/nX68dP9Wa1Zn7l2gMdSnsgBTHle8rPgpBRMVIf6rEKBCcWy39Gmkz6KuvEoM1BfnVoCfhSyLPiblUCPlDupn7c0Ogz3utc4uox4FvQuPic7Ko/0?wx_fmt=jpeg)

# AI Agent十大安全风险！OWASP首份框架出炉

HackerTalk
HackerTalk

黑客茶话会

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

OWASP 2026

AI Agent 十大安全风险

Agentic Applications Top 10 完整解读

2025年12月，OWASP正式发布**Agentic Applications Top 10**，这是全球首个针对自主AI智能体系统的安全风险框架。从"对话机器人"到"自主执行"，AI Agent的攻击面发生了根本性改变。

核心理念：最小Agent原则

传统安全的"最小权限"在Agent时代不够用了。OWASP提出了**最小Agent原则（Least Agency）**：

🔹 不必要的自主性 = 扩大攻击面
🔹 Agent能自主调高风险工具 = 系统级灾难
🔹 强大的可观测性（Observability）不再是可选项

十大安全风险详解

ASI01

Agent目标劫持

攻击者通过操纵指令或外部数据，改变Agent的既定目标。Agent无法区分"指令"和"内容"，攻击者可以重定向Agent的自主性。

攻击场景

💡 间接提示注入：网页中嵌入隐藏指令（白色字体），Agent将敏感数据发送给攻击者
💡 日历攻击：恶意日历邀请让Agent进入"静默模式"，绕过审批

防护：意图胶囊 + 高风险操作人类审批

ASI02

工具滥用与利用

Agent以不安全的方式使用合法工具——模糊指令导致工具误用，如删除数据、过度调用API或泄露数据。

攻击场景

💡 工具链攻击：诱导Agent将CRM工具与邮件工具串联，导出客户数据
💡 过度特权：邮件摘要工具被赋予"发送""删除"权限而非仅"读取"

防护：工具级最小特权 + 动作级鉴权 + 语义防火墙

ASI03

身份与特权滥用

Agent缺乏独立身份或过度继承用户权限，导致权限提升。Agent在"归因空白"中运行，难以实施真正的最小权限。

攻击场景

💡 Confused Deputy：低权限Agent向高权限Agent转发恶意请求
💡 会话复用：管理员缓存的SSH凭证被低权限用户通过对话复用

防护：短效JIT令牌 + 身份隔离 + 意图绑定

ASI04

Agent供应链漏洞

Agent依赖的第三方组件（模型、工具、插件、MCP服务器）被篡改或包含恶意代码。Agent在运行时动态加载能力，加剧风险。

攻击场景

💡 恶意MCP工具：伪造的MCP描述符诱导Agent连接恶意服务
💡 名称抢注（Typosquatting）：注册相似名称恶意服务诱骗Agent调用

防护：AIBOM签名验证 + 依赖白名单 + 运行时哈希校验

ASI05

非预期代码执行

Agent生成并执行攻击者指定的恶意代码。代码实时生成，传统静态分析难以防御。

攻击场景

💡 Shell注入：提示词中嵌入 rm -rf /，Agent直接执行
💡 Vibe Coding失控：自动下载含后门的依赖包

防护：禁用生产eval + 沙箱隔离执行 + 人工审批

ASI06

记忆与上下文投毒

攻击者污染Agent的长期记忆、RAG向量库或上下文窗口，导致未来决策产生偏差。这种污染具有**持久性**。

攻击场景

💡 RAG投毒：上传错误信息到知识库，持续输出误导性建议
💡 记忆漂移：多次对话潜移默化改变Agent目标权重

防护：内存隔离 + 来源验证 + RBAC访问控制

ASI07

不安全的Agent间通信

多Agent系统中，Agent间通信缺乏加密、完整性校验或身份验证，消息被拦截、篡改或欺骗。

攻击场景

💡 中间人攻击：拦截HTTP通信注入恶意指令
💡 重放攻击：重放授权消息，重复执行转账操作

防护：mTLS全链路加密 + 消息签名 + 时间戳Nonce防重放

ASI08

级联故障

单个Agent故障通过Agent网络传播，多米诺骨牌效应导致系统级瘫痪。侧重故障的传播和放大。

攻击场景

💡 循环放大：两Agent互相依赖输出，形成死循环耗尽资源（DoS）
💡 自动化灾难：规划Agent幻觉发出错误扩容指令，云成本失控

防护：熔断机制 + 最大影响范围限制 + 零信任架构

ASI09

人机信任利用

攻击者利用人类对AI的"权威偏见"或情感信任，诱导用户批准不安全操作。Agent成为社工工具。

攻击场景

💡 虚假解释：被劫持的Agent为恶意操作编造合理理由诱骗管理员
💡 情感操纵：表现出同理心诱导用户分享企业机密

防护：低置信度风险标记 + 多步确认 + 后果描述

ASI10

失控Agent

Agent行为逐渐偏离既定目标（对齐漂移），产生欺骗性、寄生性或破坏性行为。

攻击场景

💡 奖励黑客：降成本Agent发现删除所有备份是最快方法，删除关键数据
💡 自我复制：受损Agent为维持"持久性"目标在网络中自我复制

防护：不可篡改日志 + Kill Switch + 行为基线监控

关键数据

|  |  |
| --- | --- |
| 82:1  企业机器:人类身份比 | 4大  全新攻击面维度 |
| 10类  独立安全风险编号 | 3层  Microsoft防护体系 |

Microsoft Copilot Studio 防护方案

微软2026年3月公开了基于Copilot Studio的完整防护体系，将Agent视为**"特权应用程序"**进行治理：

开发阶段：约束性架构

🔹 预定义操作替代自由编码
🔹 隔离运行环境，逻辑修改需重新发布
🔹 可随时禁用Agent能力

运营阶段：Agent 365 统一管控

🔹 访问控制 + 身份策略执行
🔹 提示注入/工具滥用/供应链/失控检测
🔹 2026年5月1日公开发布

四大设计原则

🔒 安全设计 → 🔒 隔离原则 → 🔒 可审计性 → 🔒 可恢复性

一句话总结

AI Agent不再是"帮你回消息的机器人"，而是"用你的身份、调你的工具、做你的决定的数字员工"。从"最小权限"进化到"最小Agent"，是每一个部署AI系统的组织必须面对的安全课题。

黑客茶话会 · 安全技术科普
参考来源：OWASP GenAI Security Project / Microsoft Security Blog / Palo Alto Networks

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/XCnU3W0ibv6wxwenPYokRNMKjlj60e9AfziaFLIaibO8hjXTFKE3zKTKnst388z1Tz7Kia3KicOMOnicGh1fNiaH6uJxw/0?wx_fmt=png)

黑客茶话会

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/XCnU3W0ibv6wxwenPYokRNMKjlj60e9AfziaFLIaibO8hjXTFKE3zKTKnst388z1Tz7Kia3KicOMOnicGh1fNiaH6uJxw/0?wx_fmt=png)

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