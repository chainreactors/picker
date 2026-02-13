---
title: 当AI开始攻击AI：复盘2025年以来十大AI安全事件
url: https://mp.weixin.qq.com/s/2-vZK5Wm59Khbt1TijYm-w
source: Doonsec's feed
date: 2026-02-12
fetch_date: 2026-02-13T04:15:41.727775
---

# 当AI开始攻击AI：复盘2025年以来十大AI安全事件

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/mvkK67dLgZUsffu9fYy3KhrvNym3gnZLiaiceYnRKzNAUaVMNMhkzK4uWpAHhVHvfUJA0TWsH87ia5ctzXbgMM47SCiaL7iboMOUsmaSbrnoxMtw/0?wx_fmt=jpeg)

# 当AI开始攻击AI：复盘2025年以来十大AI安全事件

锦岳智慧

![]()

在小说阅读器中沉浸阅读

**一、引言**

在AI安全领域，一个根本性的范式转变正在发生：**AI从被保护的对象，演变为网络攻防的核心主体。**一方面，**“AI攻击AI”**成为现实，攻击者利用大模型自动化生成恶意代码、发起供应链投毒，甚至构建完全由AI驱动的攻击框架，将攻击的智能化和自动化提升到前所未有的水平。攻防对抗正升级为**“AI智能体”之间的自主博弈**，攻击方可以部署能自主规划、执行复杂攻击链的智能体，而防御方也必须依靠能实时狩猎威胁、自动响应的防御型智能体来应对。这标志着网络安全的竞争核心，已从传统的人力与规则，转向了AI智能体的算法先进性、协同能力与持续进化的速度。

本文系统复盘了2025年以来的十大标志性AI安全事件，清晰勾勒出一条风险演变的轨迹：从基础设施劫持、模型数据失守，到供应链污染、硬件底层突破，再到智能体生态危机。这些事件层层递进、深度关联，展示了AI应用面临的严峻挑战。

**二、十大典型事件**

**1**

**OmniGPT 平台遭入侵，3400万条对话泄露**

![](https://mmbiz.qpic.cn/mmbiz_png/mvkK67dLgZWg7JDzqiaPatAaa7f389lLfibJ2KSzw0aRhUkJ4G4Ria9y4PoC9Dzo5kZ1h2cb6EKjSj6WMxqrOmic7FtoR8bVMGPbZ5kleKyzVWc/640?wx_fmt=png&from=appmsg)

**时间：**2025年1月

**要点解读：**AI应用已成为数据泄露的新重灾区。

**事件说明：**AI聚合平台OmniGPT遭遇严重数据泄露。事件致使约3万名用户的邮箱、电话号码泄露，更有多达3400万条对话记录遭曝光。泄露内容极其敏感，涉及云盘链接、API密钥、账单信息及学历文件等。作为集成ChatGPT、Claude等主流模型的第三方服务，此次事件不仅重创用户隐私，更暴露了AI聚合平台在数据汇聚后的高风险特性，一旦失守将引发严重连锁反应。

![](https://mmbiz.qpic.cn/mmbiz_png/mvkK67dLgZXYnf2t64fmGvsSmhe5iczgqIOGbpgGEfa3ZUlNLLnTS5qFl4YyTFUBoATdBJ6qk4h47Nlwaes3S09vZYYibn7F5yQKGIuwiaapM4/640?wx_fmt=png&from=appmsg)

**2**

**GitHub Actions 供应链攻击（CVE-2025-30066）**

![](https://mmbiz.qpic.cn/mmbiz_png/mvkK67dLgZWqL5FQnBUKufCOxUcic5MHJYjNAc8TMGwEEqbFdnS35d2pC7oK4crU0ZUK0c1E8CHDgqQKhxIdNvLttPLaOHGXbs1N2nQqjqfU/640?wx_fmt=png&from=appmsg)

**时间：**2025年3月

**要点解读：**AI开发供应链投毒

**事件说明：**攻击者篡改开源项目依赖的GitHub工作流组件，植入恶意代码，成功窃取大量企业的DockerHub、npm、AWS等高价值凭证，是典型的AI开发供应链投毒事件。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/mvkK67dLgZVnyUXibzgeibuFLbiazrmHF366E2jZsx4NRjTibyxgBq27cicxHcDEsPAibPSWhnYcTBWqJac6twJ2dPgEoNo2MV1cVK9JV2BsFtuFk/640?wx_fmt=png&from=appmsg)

**3**

**GitHub 官方 MCP 服务器遭间接提示注入攻击**

![](https://mmbiz.qpic.cn/mmbiz_png/mvkK67dLgZUrCb2ZQibz4XwRSdRF2QicibQPfiaTHj50fiaqWuK7icwAcSQETjSZmB7RjIfF4FmpAjAzibnHvM7ic9icibVAS5vSVeDEibGAYYTnRTciaeA/640?wx_fmt=png&from=appmsg)

**时间：**2025年5月

**要点解读：**本次事件主要是MCP服务器遭间接提示注入攻击。MCP的核心设计目标在于实现灵活、开放的连接，但这同时也引入了一系列固有的安全挑战包含工具描述投毒风险、间接提示词注入、工具冲突与优先级劫持、“地毯式骗局”（Rug Pull）、数据安全风险、Agent-to-Agent (A2A) 场景风险以及传统Web服务风险等。

**事件说明：**攻击者利用“指令注入”手法，将恶意代码隐藏于公共仓库，诱导集成了GitHub MCP能力的AI Agent（如Claude 4）违规读取私有仓库，并将敏感数据回传至公共空间。这种攻击利用Agent的自动执行权限，实现了对私有资产的间接窃取。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/mvkK67dLgZWQKLzzopa6y78l9jeibWRoouB0uWmNIPzcibZaukibPOAeRG0ZLZMjoq5VZQZibhPRhnH6qtfgCvF9rhyH7WdeJ1tmiakJcPu4vMbU/640?wx_fmt=png&from=appmsg)

**4**

**Microsoft 365 Copilot“零点击”提示注入漏洞（CVE-2025-32711）**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/mvkK67dLgZWFDSpicCXybqQzCib6GTQnGDYqViaAS1mtTkHkBs4ow90VNkCfQlicPR3Dsq2H1AafYl2bzyVEVsFAOP1juyn14B9XlZGTHrC2Kq4/640?wx_fmt=png&from=appmsg)

**时间：**2025年6月

**要点解读：**当AI助手深度集成到业务工作流并拥有丰富的数据访问权限时，其面临的安全威胁已从“生成不当内容”升级为“成为自动化、隐蔽的数据外泄通道”。此事件迫使企业重新评估AI助手的安全边界，强调必须在授予AI工具数据访问权限的同时，部署针对提示注入的深层防御、严格的输出过滤与上下文监控机制。

**事件说明：**无需任何用户交互，攻击者即可通过特制提示词诱导Copilot在后台泄露当前对话中的敏感信息，证明了针对企业级AI助手的攻击已具备高度自动化和隐蔽性。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/mvkK67dLgZWtLrtkrLzicEdrQukfGn4bc9V4n7HsUQ3ORCvcpl88ISJZKm4aSCuLcZ9YQibVnVWbyV1gmvUJvRkHhNdlKIibQnYgicIJ55TWlzs/640?wx_fmt=png&from=appmsg)

**5**

**AmazonQ for VS Code 扩展被植入恶意提示词**

![](https://mmbiz.qpic.cn/mmbiz_png/mvkK67dLgZU0RNcSxltib7ovBfmWH1ynXaEcibRox1AV10JEP5tg6eRr3ia6tWxXS74vibiaQ4CVsOxksJSVcoVQQpJ1OGU6sAKibAv4LNCibbpESA/640?wx_fmt=png&from=appmsg)

**时间：**2025年7月

**要点解读：**该事件属于典型的AI开发工具链的供应链投毒，我们在享受 AI 编程助手带来的便利时，也必须对其背后的工具链安全、权限管控以及更新机制保持高度警惕。

**事件说明：**AWS 官方 AI 编程助手 “Amazon Q”的 Visual Studio Code 扩展被发现遭遇了恶意提示词注入攻击。攻击者通过在扩展更新中植入恶意代码，将危险指令伪装成正常的 AI 提示词，从而在开发者的环境中植入了一个具备强大破坏能力的“逻辑炸弹”。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/mvkK67dLgZVqIR7HNdnr23RzJZjqfiamaRLkJDyxgHuuFHJ8R9FNial8n0icMxSsYYrLMiaaBvt9FZtBbrulv0fMgIg9xmKV9u2QW5hBleEVLdk/640?wx_fmt=png&from=appmsg)

**6**

**StolenLoRA 模型窃取攻击**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/mvkK67dLgZUzfeq4Sy55OLeXwK4iaA2YMflkkTEuZbwtib3xQAnWp2FPQklQ21ELmhVEdicWwgsvuFz57OofmnvYBSVCA2MPer6S0Wg0oDy77I/640?wx_fmt=png&from=appmsg)

**时间：**2025年9月

**要点解读：**AI技术越追求高效和开放，其核心价值面临被高效复制窃取的风险就越大。大模型套壳（窃取）指基于一个已有的源模型，通过微调、剪枝、量化、架构修改或重新包装等方式，生成一个衍生模型，但宣称其为完全独立自研的原创模型，不充分承认或隐瞒其原始来源的行为。这种行为可能涉及知识产权、学术诚信和商业伦理问题。

**事件说明：**StolenLoRA是一种 “黑盒模型提取攻击”。攻击者无需接触模型内部代码或权重，仅通过目标模型提供的API接口（就像普通用户一样提问），就能完成窃取。

攻击分为三个关键步骤：

（1）查询与收集：攻击者向目标付费或私有的AI服务发送大量精心构造的提示词，并收集模型的回答，积累成“问题-答案”配对数据集。

（2）分析与训练：攻击者利用这些收集到的数据，在一个公开的基础模型上，训练一个新的、属于自己的LoRA适配器。

（3）复现与窃取：训练完成后，这个新的“山寨”LoRA就学会了原专有模型的核心技能，其表现与原始模型高度相似，从而实现功能窃取。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/mvkK67dLgZXibDLmZ57up1P7Wz0qF9dPdfjS1lBENiasCTIheCia8FX1u5ef0cMiaegnfianSWUpmncdJbgme0tv3Pce0iae8czAiaKLZ7yGlSQzdo/640?wx_fmt=png&from=appmsg)

**7**

**Nx 构建工具供应链投毒，劫持本地 AI 工具**

![](https://mmbiz.qpic.cn/mmbiz_png/mvkK67dLgZXZQQJle4ya3NYHJYEMqgXhHkec9wXvMFRA5oRZNiaF35uuDzYVBnkem19c5XV7fasqBxwVibPJEHygyiceF1mVdKt7R3L6O5hV8U/640?wx_fmt=png&from=appmsg)

**时间：**2025年8月

**要点解读：**针对开发工具的供应链投毒事件。

**事件说明：**广泛被数百万开发者使用的构建工具Nx遭遇供应链投毒。攻击者窃取令牌发布恶意版本，不仅影响数千开发者，更首次大规模“策反”本地AI工具。恶意代码驱使Claude Code、Amazon Q等AI助手扫描用户钱包、文件与凭证并外传数据，甚至将私有代码库公开。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/mvkK67dLgZXib7y1J6pxnwVFw6m4mQMVmxN07q6SwPaRtClXiakKyXO6CcGpWicM6VuINWcUKQ1QRjGGMctzKG5d7ETeUtlTAw1kIdicQlyb11M/640?wx_fmt=png&from=appmsg)

**8**

**ShadowRay 2.0：最大规模 AI 算力劫持事件**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/mvkK67dLgZVsiavfdlW0NnD6fMvQo7TH5JN5jXbNW6tqVC921ILOVvN4vv2lqH9VTpibTYibZibLw0kVo8shFSNhLbhBwFBMUYBiaiapq35mCiaYAU/640?wx_fmt=png&from=appmsg)

**时间：**2025年11月

**要点解读：**AI算力基础设施本身已成为攻击者直接争夺的高价值目标。

**事件说明：**以色列网络安全厂商Oligo公布的ShadowRay 2.0攻击事件显示，原本局限于AI集群算力挖矿劫持的威胁，已升级为影响全球多行业的结构性安全事件。

攻击者将Ray AI框架作为主要突破口，借助CVE-2023-48022漏洞（未鉴权Jobs  API可触发远程代码执行），在数周时间内接管了约23万台暴露在公网中的AI服务器，构建了迄今规模最大的AI算力挖矿僵尸网络。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/mvkK67dLgZUV2UVZn3EstAxUUUj5Y8z4mjUfzEkf1RibVgewuZ8LZXCEjwWYzQKBPwu1LT9iatEl5bPJ0ldgTPUabibHtATLwqJicRnNDQoUmN0/640?wx_fmt=png&from=appmsg)

**9**

**OpenClaw 智能体公网暴露与 ClawHub 技能投毒**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/mvkK67dLgZUUkzBBRzia4JcFSY0eDn35OyGVFFJDnENMbCYXOiaJDnSD4XSZ5sRCyc8tzNrZN5Mo4lJeSMImsa9Bz1haBfkBSCoK3rWbSBb68/640?wx_fmt=png&from=appmsg)

**时间：**2026年初

**要点解读：**现象级AI智能体OpenClaw因用户配置不当，导致大量高权限实例暴露公网。官方市场“ClawHub”遭大规模恶意Skills投毒，形成从终端到供应链的完整攻击链，揭示了AI智能体生态的安全危机。

**事件说明：**AI助手工具 Clawdbot（后更名为 OpenClaw）在社交平台迅速走红。作为一款运行在用户本地的自主智能代理，它拥有“数字管家”的身份，能代替用户执行命令行操作、文件管理及网络请求等高权限动作。

热度之下隐患随之而来，大量用户在部署时未同步配置安全防护，导致众多实例意外暴露于公网。由于 OpenClaw 通常持有第三方平台的高权凭证，这种“裸奔”状态无异于为攻击者打开了一条直取核心数据的“绿色通道”。

2026年2月，OpenClaw的核心技能分发平台“ClawHub”被披露遭遇大规模供应链攻击，安全人员在VirusTotal上检测到数百个恶意的OpenClaw Skills。攻击者将这些恶意代码伪装成实用的自动化工具，大肆分发后门程序、信息窃取器和远程控制木马。

![](https://mmbiz.qpic.cn/mmbiz_png/mvkK67dLgZUaKXyyOIBkCJ7dnShF19xcJ3Eddy3sWicnyFnWWoiaVPapwrDJAADIJwSc9UBnNWqn8oCqxZIZ8N6o0z8P0TXiam06WA341W9iacY/640?wx_fmt=png&from=appmsg)

**10**

**VoidLink：首款 AI 深度构建的恶意软件框架**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/mvkK67dLgZVx4qhiazUPK5aGTJks0YFc8gzIQqy21gxWvV4k8J8dB0PwxldX4KvAiaBAficubteAn88KtswcleHKuLMKXuATLy9lNr0HDN54v0/640?wx_fmt=png&from=appmsg)

**时间：**2026年1月

**要点解读：**AI攻击AI，本次事件将高级网络犯罪的开发门槛与周期降至前所未有的低点，预示AI驱动攻击的“工业化”时代来临。

**事件说明：**Check Point研究人员发现了首款几乎完全由人工智能构建的高级恶意软件框架——VoidLink。该框架具有里程碑意义：单人攻击者借助名为TRAE SOLO的AI模型，采用“规范驱动开发”模式，仅用一周时间就生成了超过8.8万行复杂代码。VoidLink集成了eBPF和LKM rootkits等高级隐身技术，专门针对云环境与容器平台设计。原本需要经验丰富的程序员团队协作才能完成的复杂工程，如今在AI辅助下可由单人快速实现。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/mvkK67dLgZUrkCGvCJiaRb1ickuAFwTgwZlnibAmceEaibSRRH6U6upLQuAxnvrdjtQKib7xBxqZXwoXX366hVaibCG3RI8nFTyIz5fclkF7ObbiaM/640?wx_fmt=png&from=appmsg)

**四、总结**

2026年的AI攻防趋势，我们从以下三个方面进行简要分析：

* **AI agent 将成为“攻击者”和“防御者”本身：**攻防对抗演变为智能体之间的自主博弈。攻击方AI Agent能够理解复杂目标、规划多步骤攻击链、调用外部工具（如MCP服务器）、并根据环境反馈动态调整策略，实施攻击。防护方采用专用防御型AI Agent，7x24小时执行威胁狩猎、异常行为分析、自动化响应和攻击面管理。
* **随着AI生态的开源化、组件化与高度集成，供应链风险持续加剧：**随着AI开发工具链、预训练模型、智能体框架（MCP、SKILLS、Function Calling、Workflow、RAG等）的广泛应用，针对AI供应链的投毒攻击与漏洞利用可能大幅增加。开源模型、公共数据集和插件市场将成为攻击者的新焦点。
* **风险加剧，从单点内容安全，升级为系统性链式危机：**当前风险已全面渗透至AI技术栈各层（基础设施、模型、应用生态），并在彼此间形成连锁反应。一个提示注入漏洞可导致数据泄露，一个被恶意技能污染的Agent可操控云端资源，而一个框架的默认暴露可能让整个内...