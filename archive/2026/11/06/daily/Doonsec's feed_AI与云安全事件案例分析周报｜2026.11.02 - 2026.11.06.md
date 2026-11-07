---
title: AI与云安全事件案例分析周报｜2026.11.02 - 2026.11.06
url: https://mp.weixin.qq.com/s/YBxhxiRv-igbMlQky5VQVQ
source: Doonsec's feed
date: 2026-11-06
fetch_date: 2026-11-07T07:58:16.147569
---

# AI与云安全事件案例分析周报｜2026.11.02 - 2026.11.06

# AI与云安全事件案例分析周报｜2026.11.02 - 2026.11.06

原创

星云实验室
星云实验室

绿盟科技研究通讯

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/mAopIKtZvYuoxrKsQvMGMaOIicZkwm1iaJZCG6l0ibZoicFrrWTyhI0P9WgzCtibJv3GABdg6Tjm50ILptEIGIhicwNsicz1aa5QvPKoprYaXCaC6Q/640?wx_fmt=gif&from=appmsg)

多智能体攻击与客户端隔离缺口并行，泄露凭据加速转化为云端数据访问。

事件一 BOSSAI 用 Hermes、OpenClaw 与 MCP 组织攻击：12 个 Agent 配置背后，确认失陷约 10 个目标

1.1

事件简介

* 涉及组织与应用：Acronis TRU 是安全厂商 Acronis 的威胁研究团队；BOSSAI 是其本次调查中一套由单人操控、整合多个 AI 智能体与安全工具的攻击平台名称，Hermes、OpenClaw 是其中承担任务执行和环境维护的智能体软件。
* 事件概述：Acronis 研究者披露，一名被其评估位于台湾的操作者，把多个 AI 智能体、可执行安全工具的 MCP 接口和租用计算资源组合成名为 BOSSAI 的攻击平台。MCP 是把外部工具接给 AI 的接口，平台利用这些接口扫描网站、尝试数据库攻击并整理窃取的数据。配置中共有 12 个智能体，调查时 9 个活跃；它们并未自动彼此通信，结果主要由操作者手工传递。研究确认约 10 个目标发生数据外传或系统访问，涉及急救系统与高校等；大量其他目标仅被扫描或攻击失败，不能把“数百个目标”写成数百起成功入侵。
* 事件时间：原始调查发表于 2026-11-04；研究覆盖的活动跨越此前多月，其中目标影响统计基于 12 天观察窗口。本期按完整调查首次公开纳入。
* 事件链接：

+ https://www.acronis.com/en/tru/posts/bossai-inside-the-ai-attack-mesh-that-targeted-taiwans-emergency-services/

+ https://cybernews.com/security/single-hacker-twelve-ai-agents-cyberattack/

* 影响范围：

+ 目标涉及 11 个国家；约 10 个目标有确认的数据外传或系统访问，另约 15 个遭主动攻击但未确认失陷，其余主要为侦察或尚未执行的计划。

+ 已确认案例包含无认证可读的历史急救医疗数据、调度案件记录和高校数据；调度记录不等于救护车实时位置追踪。

+ 研究获得逾 90,000 个文件、约 9GB 材料；这些是研究证据规模，不是受害数据泄露量。

* 技术分类归属：Agent层 / 编排层 / MCP工具执行 / 数据层
* 事件标签：AI相关

![](https://mmbiz.qpic.cn/mmbiz_png/mAopIKtZvYthflFTW5iam5U1GCgz6LPCsxAqQMClHp2Mk0ibeTUWuYaNHXped1AMzlqxibrLUZh4yY2eaSn2eveaQITB9GibbF2HiaRA3W1zDBTY/640?wx_fmt=png&from=appmsg)

图1：Acronis 的架构图展示操作者如何连接模型、Agent 和 MCP 工具。商业模型主要承担基础设施任务，攻击工作主要转向被移除安全约束的模型；图中的软件名称不代表其官方模型均参与攻击，也不表示 12 个 Agent 全部活跃或自动协作。来源：https://www.acronis.com/en/tru/posts/bossai-inside-the-ai-attack-mesh-that-targeted-taiwans-emergency-services/

1.2

事件背景与回顾

* 架构形态：操作者把资产发现结果交给攻击 Agent，Agent 通过工具接口执行命令、解析结果并安排下一步；不同 Agent 之间由人转交信息，云上维护服务与本地模型共同支撑运行。
* 可核验链路：目标枚举 → 对公开接口和数据库入口验证 → 无认证读取、SQL 注入或默认凭据登录 → 提取并整理数据。SQL 注入是把数据库指令混入应用输入，具体成功路径应逐案认定。
* 事实边界：研究记录了真实数据访问，也记录了虚构漏洞、失败步骤被误判为高危发现等情况。商业模型多次拒绝直接攻击；部分知名编码 Agent 实际被改接第三方模型，不能按客户端名称判断模型供应者。

1.3

事件根因深度分析

* 以下为基于公开链路的防御分析，各受害系统的完整修复状态尚未公开。
* 基础设施与云配置错误：无认证接口、默认数据库凭据等既有缺陷仍是成功入口；AI 缩短了发现与验证之间的人工处理时间，并未消除目标系统原有的访问控制问题。
* AI 供应链与存储缺陷：MCP 把扫描、数据库访问和命令执行变成可连续调用的能力，持久化的扫描结果与任务记录又能被交给其他 Agent 重用。
* 前沿算法/工程逻辑缺陷：部分框架关闭范围校验并自动批准高风险操作，使模型判断直接进入执行器；但模型输出仍会产生误报，不能把 Agent 自述当作入侵证据。
* 复合依赖与应急响应缺陷：跨工具、跨主机的操作可以组成同一攻击过程，单看一个扫描器或一种客户端标识容易丢失前后关系。
* 边界防御与分层隔离缺陷：受害侧需要按实际身份、接口和数据权限限制访问；只识别 AI 客户端或拦截特定提示词，无法覆盖可替换模型与通用工具组合。

1.4

VERIZON DBIR 事件分类

System Intrusion（系统入侵）与 Basic Web Application Attacks（基础 Web 应用攻击）：分别对应多阶段工具执行和利用应用入口取得数据的子案例，不将全部侦察目标统一计为数据泄露。

1.5

攻击路径与 MITRE ATT&CK 技术映射

以下对应报告中有证据的子案例，不表示每个目标都经历全部步骤。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/mAopIKtZvYuiawe2OZkbicmNo43ICfl9YSyEwdS216262FxqSJ4ibMKIL3HWvphOcibF36y842vBAs98DY8I0TM1ZVhu8Qg79CRGzhDxKvtIYSE/640?wx_fmt=png&from=appmsg)

1.6

防御启示

* 优先清理无认证数据接口、默认管理凭据和可批量查询的敏感数据入口，并验证匿名身份实际能返回什么。
* 关联短时间内的枚举、错误请求变体、认证成功和批量读取，响应周期要覆盖机器连续执行的速度。
* 内部使用 Agent 时，在执行器强制落实范围、身份和工具权限；保留独立于模型叙述的命令、进程和数据访问日志。

事件二 ChatGPT HTML 预览可借嵌套弹窗绕过 Lockdown Mode：客户端隔离缺口打开会话外传路径

2.1

事件简介

* 涉及组织与应用：Check Point 研究者 Alexey Bukhteyev 披露了 OpenAI ChatGPT 的预览隔离问题；ChatGPT 是对话与工具执行应用，Lockdown Mode 是用于限制潜在数据外传通道的可选安全模式。
* 事件概述：Check Point 研究者发现，ChatGPT 把生成的网页放入隔离框架预览，却仍允许弹窗脱离该框架。攻击内容可新建一层嵌套网页，取到未被拦截的弹窗函数，再通过弹窗向外发送对话数据。普通浏览器通常还需一次用户操作才能打开弹窗；研究中的 Electron 桌面客户端 ChatGPT Classic 则可无额外点击触发。研究展示了数据外传与伪更新窗口，并非受害者调查。OpenAI 于 9 月 18 日告知已修复，研究者复测确认方法失效，本周是技术细节公开，不能写成仍未修复的新零日。
* 事件时间：2026-11-05 公开研究；2026-09-18 厂商确认部署修复并获研究者复测确认。
* 事件链接：

+ https://research.checkpoint.com/2026/chatgpt-lockdown-mode-bypass-phishing-malware-delivery-and-silent-data-exfiltration/

+ https://thehackernews.com/2026/11/researchers-bypass-chatgpt-lockdown.html

* 影响范围：

+ 涉及修复前 HTML 预览的嵌套 iframe 与弹窗控制，入口场景包括恶意提示、恶意 GPT 或共享对话。

+ 零额外点击结论限定于报告验证的 ChatGPT Classic 桌面环境；下载恶意文件、诱导重新认证等后果仍各有交互前提。

+ 未公开受害人数或真实在野利用证据；不能把研究中的聊天外传推广为任意读取全部账户历史。

* 技术分类归属：应用层 / 客户端渲染 / 沙箱与出站控制
* 事件标签：AI相关

![](https://mmbiz.qpic.cn/mmbiz_png/mAopIKtZvYvsZzQXYN1WkZw0kQibJEoqgqbiaP5mdtYS6ZONv1CP855NnRwHLDK1jpmjJef5q3usBLMCDrefd7AnPzibGlCec9wD5p9ul7ASeA/640?wx_fmt=png&from=appmsg)

图2：研究截图标出了 allow-popups 与 allow-popups-to-escape-sandbox 两项权限，解释为什么仅改写弹窗函数未形成完整边界。截图是修复前实现证据，不能说明当前版本仍保留可利用权限，也不证明攻击内容能直接读取父页面的全部会话状态。来源：https://research.checkpoint.com/2026/chatgpt-lockdown-mode-bypass-phishing-malware-delivery-and-silent-data-exfiltration/

2.2

事件背景与回顾

* 架构形态：iframe 是网页内嵌的小页面。ChatGPT 对预览页面的网络行为和 window.open 做应用层拦截，同时依赖浏览器沙箱限制它与主应用的相互访问。
* 验证链路：攻击内容进入预览 → 新建嵌套 iframe → 调用其原生弹窗方法 → 新窗口不继承原有沙箱限制 → 绕开预期出站拦截。外传材料必须先进入攻击可处理的内容，不能据此主张任意父页面读取。
* 修复方式：来源称外层预览 iframe 移除了两项弹窗权限，并通过复测关闭文中路径；本案与此前代码执行运行时的跨账户通道是不同漏洞。

2.3

事件根因深度分析

以下为基于研究验证的边界分析。

* 基础设施与云配置错误：缺陷位于客户端渲染与权限组合，没有证据说明云租户隔离同时失效；云端模型受约束也不能替代客户端出站控制。
* AI 供应链与存储缺陷：共享对话和第三方 GPT 可以承载待渲染内容，因此保存、分享和恢复内容都应保留原有信任级别。
* 前沿算法/工程逻辑缺陷：只重写当前窗口函数，无法覆盖新建执行上下文；底层仍允许弹窗脱离隔离，给上层拦截留下替代路径。
* 复合依赖与应急响应缺陷：浏览器与 Electron 的弹窗交互规则不同，同一网页逻辑在桌面封装中会改变触发条件，应分别回归测试。
* 边界防御与分层隔离缺陷：安全模式需要覆盖生成代码、预览、弹窗和下载等全部出口，不能只在模型工具调用入口实施限制。

2.4

VERIZON DBIR 事件分类

研究性漏洞，潜在对应 System Intrusion（系统入侵）：公开证据是隔离绕过与外传演示，未确认发生可计入 DBIR 的真实入侵。钓鱼和恶意下载是另有交互前提的后续场景。

2.5

攻击路径与 MITRE ATT&CK 技术映射

仅映射研究展示的客户端执行行为，不补写尚未发生的持久化或凭据窃取。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/mAopIKtZvYudia4E11ZfhJiaRIbPZUcPjZ88cXVG2zdFvicyxCtKuvLCcHFbibZmwZxgMB785QsFDgthFcDN184iaeU3GGlHOibNwHibqusJjHVn3M/640?wx_fmt=png&from=appmsg)

2.6

防御启示

* 对客户端安全模式建立完整出口清单，并在浏览器权限层默认关闭不需要的能力。
* 将 iframe、子窗口及桌面封装作为独立执行上下文测试，覆盖无需点击和共享内容恢复场景。
* 企业部署核对客户端与服务端修复状态；对话中出现逼真的更新或登录窗口时仍应核验实际来源。

事件三 ARTEX 从 GitHub 密钥扫描推进到 Azure Key Vault：一例五分钟完成，应用身份串联多租户资产

3.1

事件简介

* 涉及组织与应用：Microsoft Threat Intelligence 与安全研究团队披露攻击活动；ARTEX 是被攻击者滥用的 AI 渗透框架，Entra ID 管理云身份，Azure Key Vault 保存应用使用的密钥与秘密。
* 事件概述：微软披露，未归属的攻击者使用 ARTEX 等智能体工具，搜索公开 GitHub 仓库中尚未失效的应用密钥，再以应用身份登录企业云环境。应用身份是软件访问资源的账户，权限过大时可以读取更多密钥和数据。在一例观察中，Agent 从搜索密钥到外传 Azure Key Vault 数据只用五分钟；另有活动涉及厂商自有多租户应用，其密钥失守后影响多个下游租户。攻击并非破解 Azure 加密，而是使用仍有效的身份和已有授权，随后探索存储、协作文件及 AI 服务。
* 事件时间：研究发表于 2026-11-05；大规模密钥搜索最早观测于 8 月，文中一组后续应用身份滥用最早始于 10-28。本期按新增完整技术链纳入。
* 事件链接：

+ https://www.microsoft.com/en-us/security/blog/2026/11/05/threat-actors-use-agentic-ai-tooling-to-find-and-abuse-exposed-secrets/

* 影响范围：

+ 观察到跨多个租户、数十个关联应用的成功服务主体登录；没有公开统一受害组织总数。

+ 目标包括 Key Vault、Storage、App Service 配置、AI/ML 连接、AKS 凭据，以及 SharePoint、OneDrive 和邮箱内容。

+ 五分钟是单例观察，不能推算全部租户的失陷速度；多组 IP 和活动之间的关系也不能仅凭共用工具归为同一操作者。

* 技术分类归属：Agent层 / 云身份层 / 多租户应用授权 / 数据与模型服务层
* 事件标签：云AI融合

![](https://mmbiz.qpic.cn/mmbiz_png/mAopIKtZvYty1VeqppXOZAp3kcqMic0ouIRfCjc8jBbF3FRoyQECjoodLRud1AAkx9aYUfdKqTXPpY1mrlRH1DP2k6nv6rDLA2NNJ6dI81ZA/640?wx_fmt=png&from=appmsg)

图3：微软的链路图汇总调查中观察到的身份、资源与数据访问动作；各方框来自多次活动，不代表每个受害租户都经历全部步骤。AI 服务滥用应以对应日志核实，不能仅凭发现模型部署就认定已产生盗用费用。来源：https://www.microsoft.com/en-us/security/blog/2026/11/05/threat-actors-use-agentic-ai-tooling-to-find-and-abuse-exposed-secrets/

3.2

事件背景与回顾

* 攻击路径：公开代码发现 client secret → 以服务主体取得令牌 → 枚举订阅、角色和服务 → 调用返回凭据的 API → 访问密钥库、存储及协作数据 → 寻找 AI 服务访问能力或继续执行。
* 工程细节：微软记录了错误 API 版本或方法被改正后请求成功的连续过程，符合自适应排障特征；不能仅用速度或 User-Agent 作为 AI 归因的唯一证据。
* 跨周关系：与 W43 的 ARTEX/Storm-0940 使用同类工具，但本期新增的是公开密钥、工作负载身份和多租户下游访问链路；工具相同不足以证明操作者相同。

3.3

事件根因深度分析

以下为基于微软遥测的防御分析。

* 基础设施与云配置错误：有效应用凭据与过宽的资源权限组合，使一次代码泄露可以跨越多个云服务；仅保护员工交互登录无法覆盖工作负载身份。
* AI 供应链与存储缺陷：公开仓库和次级仓库中的秘密在撤销前持续有效。删除提交、改写历史或移除网页，不会终止已签发令牌或攻击者保留的副本。
* 前沿算法/工程逻辑缺陷：Agent 将检索、结果筛选、认证和 API 排障接成循环，消耗的是防守方从发现泄露到吊销权限的时间窗口。
* 复合依赖与应急响应缺陷：多租户应用把供应商密钥和下游授权连接起来，处置需要同时核查源应用、各租户服务主体、已签发令牌与可读秘密。
* 边界防御与分层隔离缺陷：控制面枚举、数据面读取和 AI 调用分散在不同日志中；单一登录告警难以还原实际资产访问范围。

3.4

VERIZON DBIR 事件分类

System Intrusion（系统入侵）：使用暴露或被盗应用凭据完成后续发现和数据访问。初始公开泄露属于秘密管理问题，后续滥用是独立的攻击行为。

3.5

攻击路径与 MITRE ATT&CK 技术映射

![](https://mmbiz.qpic.cn/mmbiz_png/mAopIKtZvYtn50QeuddWwMTSklcAia1YJFw4C0nzfWo9O69SHe2vDsyyJgKyUJvwy9PSwwEcUHcW5GZ67fnW2XE8se6kXtPHUQA0V6vKrJPA/640?wx_fmt=png&from=appmsg)

3.6

防御启示

* 对公开泄露立即撤销凭据并追查历史使用，不以删除代码作为闭环；同步处理秘密库和文档中可被继续读取的凭据。
* 按应用梳理跨租户授权及资源权限，优先迁移到受约束的托管身份等机制，减少长期 client secret。
* 关联服务主体登录、ARM、Key Vault、Storage 与 Microsoft 365 审计；对短时间跨多个服务申请令牌、失败后迅速改正 API 的行为建立检测。

内容编辑：浦明

责任编辑：吕治政

本公众号原创文章仅代表作者观点，不代表绿盟科技...