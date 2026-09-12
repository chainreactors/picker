---
title: AI与云安全事件案例分析周报｜2026.09.07 - 2026.09.11
url: https://mp.weixin.qq.com/s/7kd1yBqekVmx3jonqKQFSg
source: Doonsec's feed
date: 2026-09-11
fetch_date: 2026-09-12T06:41:48.900101
---

# AI与云安全事件案例分析周报｜2026.09.07 - 2026.09.11

# AI与云安全事件案例分析周报｜2026.09.07 - 2026.09.11

原创

星云实验室
星云实验室

绿盟科技研究通讯

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz_gif/mAopIKtZvYtl9F0icic5lichIJzHiaksmsPrIosa8JfFsibFp2vPT7q9l2CkM8iaUx3DtSsN8NpN3F64Aj25yS6CrkcmicloTPEVwvyVs1XFNx4h6s/640?wx_fmt=gif&from=appmsg)

AI 编排已从研究辅助越过门槛，进入真实规模化攻击与跨账户数据通道。

事件一 PaperCut 两漏洞被 AI 编排成规模化入侵：440 台实例失陷，一所高中 7 分钟被推至域管

事件简介

* 涉及组织与应用：PaperCut NG/MF 是学校、企业等机构自建的打印管理服务器；GreyNoise 与 Blackpoint Cyber 分别从攻击遥测和暴露的操作者基础设施还原本次活动，PaperCut 则负责发布漏洞修复与入侵指标。
* 事件概述：GreyNoise 将攻击者描述为疑似俄语使用者，确切身份和目的未确认。PaperCut NG/MF 是统一管理打印、复印和扫描的服务器，Windows 部署常以 SYSTEM 权限运行并接入 Active Directory。攻击者串联认证绕过 CVE-2026-81578 与动态类加载 CVE-2026-82078 取得代码执行，再用数百个 AI Agent 研究漏洞、筛选目标和重试。至少 440 个实例、395 家组织失陷，12 家被推进到域管；后续是否勒索或转售入口不足以确认。
* 事件时间：攻击项目最早记录始于 2026-08-31；GreyNoise 于 9 月 9 日、Blackpoint 与媒体于 9 月 10 日集中披露；PaperCut 9 月 10 日发布替代全部应急补丁的正式维护版本。
* 事件链接：

+ https://www.greynoise.io/blog/ai-orchestrated-campaign-against-papercut-ng-mf

+ https://blackpointcyber.com/blog/death-by-a-thousand-papercuts-ai-driven-exploitation-at-scale/

+ https://www.papercut.com/kb/Main/security-bulletin-27-aug-2026-urgent-security-advisory/

+ https://thehackernews.com/2026/09/papercut-attacker-uses-hundreds-of-ai.html

* 影响范围：

+ GreyNoise 识别到 48 个国家的至少 440 个 PaperCut NG/MF 实例、395 家可归属组织；还有无法归属名称的真实受害者，不能把 395 当作完整总数。

+ 攻击者取得 12 家机构的域管理员权限；一个美国高中案例从初始访问到域管仅 7 分钟，另一次集中执行在 26 秒内打入 11 家机构。

+ PaperCut 公告称全部 NG/MF 版本都曾受影响；截至 9 月 10 日推荐版本为 26.0.5、25.0.13、24.1.10，取代 Emergency Patch 1—3。

+ 暴露资产包括 PaperCut 主机权限、注册表与 LSASS 凭据、Active Directory 数据库以及后续远程访问入口；研究未确认所有 440 台主机都到达相同攻击阶段。

* 技术分类归属：基础设施层 / 应用层 / 编排层 / Agent层
* 事件标签：云AI融合

事件背景与回顾

* 事件背景与架构形态：PaperCut NG/MF 是自托管 Java Web 应用，Windows 部署常使用 SYSTEM 权限并加入域。CVE-2026-81578 允许未认证请求在权限检查完成前触发管理动作、修改配置；CVE-2026-82078 又让可控的数据库驱动类名选择并执行应用 classpath 中的 Java 字节码。两项组合把管理界面访问变成预认证代码执行。
* 攻击链：互联网扫描和目标归一化 → 绕过 PaperCut 管理认证 → 修改数据库连接配置 → 触发恶意 Java 类加载并以服务器权限执行 → 收集注册表与 LSASS 凭据 → 对域控使用哈希传递、noPac 或既有高权限服务账号 → DCSync 导出 NTDS.DIT → 部署 Ligolo/远程访问工具维持入口。
* AI 编排作用：暴露的操作者目录保存了漏洞研究、补丁前后比对、PoC、并发扫描器、失败分类和后续计划。AI 并未创造新的漏洞原理，而是把“研究—验证—目标筛选—失败反馈—改码—重试”固化成持续循环；工具设计可并发处理 200 个目标，并将未完成目标送入多轮重试。
* 时间线与前情：8 月 27 日厂商首次发布紧急公告，8 月 31 日漏洞进入 KEV 且攻击项目启动；9 月 9—10 日两家研究机构公开 AI 编排和受害范围；9 月 10 日正式维护版本上线。本条纳入 W37 的增量是可归属的 AI 攻击架构、受害规模和正式维护版本，不把早前漏洞披露重新包装成新事件。

事件根因深度分析

* 基础设施与云配置错误：管理界面暴露到互联网使预认证链能够批量命中；域成员身份和 SYSTEM 运行权限又把单台打印服务器失陷放大为域凭据风险。
* AI 供应链与存储缺陷：核心不是模型供应链被投毒，而是攻击者把公开漏洞材料、补丁差异和目标数据持续喂给多个 Agent，形成可恢复状态的攻击工程仓库。
* 前沿算法/工程逻辑缺陷：AI 的主要增益是降低迭代和并发管理的人力成本。失败不再终止攻击，而会自动变成下一轮代码修改与队列重试的输入。
* 复合依赖与应急响应缺陷：认证绕过本身只能改配置，动态类加载本身要求高权限；两者组合才形成预认证 RCE。只阻断其中一个可见行为或只安装早期应急补丁，不能替代正式版本升级与入侵排查。
* 边界防御与分层隔离缺陷：打印管理服务器既面向 Web，又接触域身份和高权限服务进程，业务边界与身份边界重叠。攻击者获得主机权限后，可把常规打印系统转成 Active Directory 凭据采集点。

VERIZON DBIR 事件分类

System Intrusion（系统入侵）：公开服务漏洞链提供初始访问，随后发生凭据转储、域权限提升和持久化；最终变现目的尚未确认。

攻击路径与 MITRE ATT&CK 技术映射

![](https://mmbiz.qpic.cn/mmbiz_png/mAopIKtZvYsg3Sm5OqCPLYg8c19ZQH2x43K2yxqiatEGJhUG5uP1JH6fQEgfbfapvIm0Qp3ia97VMgjnv1nKHAZ6IEatBjF8eUvhemluUaFsY/640?wx_fmt=png&from=appmsg)

防御启示

* 升级到 26.0.5、25.0.13、24.1.10 或更新维护版本；仍运行应急补丁的环境也应迁移到正式版本。
* 立即撤销互联网对管理界面的直接访问，并按服务器进程、子 shell、注册表导出、域控复制和异常远程工具串联调查，不能以单个 IOC 未命中判定安全。
* 对确认主机失陷的机构轮换域凭据并检查 DCSync、异常管理员、SimpleHelp、AnyDesk 与 Ligolo 痕迹；仅重装 PaperCut 不会撤销已经取得的域访问。

事件二 ChatGPT 沙箱共享服务变成跨账户剪贴板：隐藏提示可把 Gmail 数据送到另一账户

事件简介

* 涉及组织与应用：Check Point Research 是漏洞发现方；ChatGPT 是可执行代码并连接 Gmail、Drive、Teams、GitHub 等外部应用的云端 AI 助手，OpenAI 负责其容器和内部软件包服务；JFrog Artifactory 在本案中是容器共同可达的依赖缓存。
* 事件概述：Check Point 研究员 Alexey Bukhteyev 在受控验证中发现，不同 ChatGPT 账户的代码容器虽不能直接互联，却共同访问一个内部 Artifactory。容器的“读取”凭据同时能修改未按账户隔离的缓存属性，攻击者可把它当作跨账户消息盒。恶意指令经共享对话、粘贴提示或自定义 GPT 进入受害会话后，可调用已授权的 Gmail 并回传结果。该链仅属 PoC，未发现真实攻击；OpenAI 已退役相关服务。
* 事件时间：研究方称 2026 年 6 月发现通道；9 月 8 日公开技术报告，公开时跨账户通道已不可用。
* 事件链接：

+ https://research.checkpoint.com/2026/the-shared-clipboard-inside-the-sandbox-cross-account-data-leakage-in-chatgpt/

+ https://thehackernews.com/2026/09/chatgpt-flaw-let-planted-prompt-send.html

* 影响范围：

+ 研究验证的直接范围是不同 ChatGPT 账户的代码执行容器及其共同可达的内部 Artifactory 元数据，不是 JFrog 产品的通用漏洞。

+ 可被读取的数据取决于受害会话已有权限，包括对话历史、上传文件和已连接应用可访问的数据；PoC 演示了 Gmail 邮件数据。

+ 攻击需要恶意指令先进入对话上下文，随后一次普通消息即可触发；公开材料没有受害用户数量或在野利用证据。

+ OpenAI 表示研究涉及的内部 Artifactory 已退役，用户没有本地补丁可安装。

* 技术分类归属：基础设施层 / 数据层 / 编排层 / Agent层 / 提示词工程
* 事件标签：云AI融合

![](https://mmbiz.qpic.cn/mmbiz_jpg/mAopIKtZvYsQVdY3S1apTbSZVW84DIsaKJlNvt6tZw9QXfB1aGelctQu2nVcf0kaNOAcmU83oPlLKacyQM0j9zsanb25GibbIHicavMHccBmM/640?wx_fmt=jpeg&from=appmsg)

图1 Check Point Research 还原的受控 PoC 显示，攻击者账户先把任务写入共同可达的 Artifactory 属性，受害者会话在处理可见请求的同时调用已授权 Gmail，再把结果写回另一属性供攻击者取走。该图证明研究环境中的跨账户通道与隐藏任务流程，不能证明真实用户已经遭到利用。图片来源：Check Point Research，https://research.checkpoint.com/2026/the-shared-clipboard-inside-the-sandbox-cross-account-data-leakage-in-chatgpt/

事件背景与回顾

* 事件背景与架构形态：ChatGPT 为分析任务创建隔离容器。容器不能直接出网或跨账户通信，但为安装 Python、npm 等依赖可以访问同一内部包代理。网络隔离本身仍有效，失效的是共享服务上的可写属性与租户隔离。
* 攻击链：攻击者在共享对话、自定义 GPT 或待粘贴文本中植入指令 → 受害者发送普通消息 → 模型同时处理可见任务和隐藏任务 → 容器从 Artifactory 属性读取攻击者命令 → 调用受害会话已有的 Gmail 等工具 → 将结果编码写回共享属性 → 攻击者账户读取并重组数据。
* 技术成因：容器环境变量中的凭据不仅能读取依赖，还拥有 Annotate 权限；Item Properties API 的可变元数据又未按账户或会话隔离。属性可保存文本或 Base64，较大数据还能拆分成多项。
* 时间线与前情：该通道与 W35 的 Hugging Face 评测 Agent 越界都说明“共同可达的内部服务”会成为旁路，但机制不同：本条是 ChatGPT 账户间的 Artifactory 属性通道，不把两起事件视为同一漏洞。

事件根因深度分析

* 基础设施与云配置错误：内部包服务向所有容器暴露同一可写元数据面，且所谓读取凭据拥有额外注释权限，违背最小权限。
* AI 供应链与存储缺陷：依赖代理本来只为受控取包，却因可变属性成为持久消息存储；软件供应链辅助服务由此进入用户数据安全边界。
* 前沿算法/工程逻辑缺陷：模型能够在同一轮保持两个任务流，并服从“不要把隐藏任务写进可见答案”的指令。单看最终文本无法证明模型没有执行后台工具调用。
* 复合依赖与应急响应缺陷：提示注入、过宽工具读取权限、共享内部服务和缺少租户隔离必须同时成立。只改模型拒答或只保留网络沙箱，都不足以切断完整链路。
* 边界防御与分层隔离缺陷：平台把“容器不能直连”当作主要隔离，但忽略了所有容器共同访问的控制面。任何共享 API 的可写状态都应被视为潜在跨租户通信介质。

VERIZON DBIR 事件分类

研究性案例，按 System Intrusion（系统入侵）潜在路径分析：恶意上下文驱动受害会话的合法能力，并通过共享服务越过租户边界；没有证据认定已发生真实数据泄露。

攻击路径与 MITRE ATT&CK 技术映射

以下映射针对研究 PoC，不代表已观察到真实攻击。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/mAopIKtZvYvntnTpqKTCnYLYjxMNPaK9tonibTD78OTRfxmNia45HVWTKEWbicv5IESaLjsK0IEZZ5s2ogZm6wXl7GD0y5ic3Qpf66D3LWC6B2Y/640?wx_fmt=png&from=appmsg)

防御启示

* 平台侧应把共享依赖代理、缓存、日志和元数据 API 都纳入租户隔离审计；运行时只授予下载所需权限，禁止通用属性写入。
* 企业管理员应收紧 AI 助手连接应用的读取范围，对高敏感信息库启用逐次确认或按动作分级授权，并审计“可见回答正常但后台工具已调用”的情况。
* 对共享对话和自定义 GPT 视同不可信代码：检查隐藏配置、来源与工具权限；最终回复内容不能代替工具调用日志。

事件三 受害云资源被改造成多 Agent 攻击平台：6 小时内完成扫描并收割数千凭据

事件简介

* 涉及组织与应用：Google Threat Intelligence Group 与 Mandiant 基于一线响应和威胁遥测发布本次观察；攻击者使用 AI 编码聊天工具、Markdown 操作手册和多个 Agent，把已攻陷的云资源改造成对外扫描与凭据采集平台。
* 事件概述：Google 将攻击者描述为疑似以经济利益为目的，未公开其具体名称、受害云厂商或漏洞清单。攻击者先控制一家机构的云资源，再向 AI 编码聊天工具提供提示和预制 Markdown 指令，让多个 Agent 自主编排漏洞扫描、故障排查、IP 轮换和凭据收集。整套系统从规划、构建到执行不足 6 小时，最终取得数千个第三方凭据；来自被害云环境的合法出口地址又降低了批量攻击的显眼程度。这是 Mandiant 事件响应观察到的真实活动，但公开材料没有说明每个凭据是否仍有效、是否已被用于后续登录。
* 事件时间：活动发生于 2026 年第二季度；Google 于 9 月 8 日首次公开该案例。
* 事件链接：

+ https://cloud.google.com/blog/topics/threat-intelligence/from-prompting-to-autonomy-the-evolution-of-adversarial-ai

+ https://thehackernews.com/2026/09/autonomous-ai-agents-compromise.html

* 影响范围：

+ 一个未具名组织的云基础设施先被攻陷，并被用于发起后续互联网扫描；初始失陷方式未公开。

+ 报告确认收集“数千个第三方凭据”，未给出完整数量、目标行业、漏洞或凭据类型，不能与同文另一套 Recon 面板中的 23,800 个秘密合并计数。

+ Agent 自动完成扫描管线管理、实时排障与 IP 轮换；“不足 6 小时”指从计划、构建到执行的整体窗口，不等于所有第三方目标在 6 小时内都被完全接管。

+ Google 表示已停用相关攻击资产；公开材料没有给出全部受害者处置状态。

* 技术分类归属：基础设施层 / 数据层 / 编排层 / Agent层
* 事件标签：云AI融合

![](https://mmbiz.qpic.cn/mmbiz_jpg/mAopIKtZvYu4GqyUfWhpHWQSwIqdIsSicQiaADDNalsSlsPEFk7MeEO6xjw7AOATj7iaY9MVLvUhibgSWR5Usf5Q6pcVjaOlXJ5Abk0iayAgs5tE/640?wx_fmt=jpeg&from=appmsg)

图2 Google Threat Intelligence 用流程图概括了“云基础设施先失陷—AI 驱动开发循环—多 Agent 批量扫描和凭据收集”的链路，并标注从规划到执行少于 6 小时。该图不披露初始云入侵手段、具体漏洞或第三方受害者身份，也不能与同文 Recon 面板的 23,800 个秘密合并计数。图片来源：Google Cloud Threat Intelligence，https://cloud.google.com/blog/topics/threat-intelligence/from-prompting-to-autonomy-the-evolution-of-adversarial-ai

事件背景与回顾

* 事件背景与架构形态：传统批量扫描依赖人工编写规则、处理失败和维护代理池。本案把这些工作拆成可由 Agent 读取的 Markdown 操作手册，Agent 根据实时结果调整扫描流程并轮换出口。
* 攻击链：取得受害云资源 → 配置 AI 编码聊天工具与多 Agent 指令集 → 自动构建漏洞扫描和凭据采集框架 → 从受害云 IP 扫描第三方系统 → 实时处理错误和轮换 IP → 汇总数千凭据。
* 证据边界：同一 Google 报告还披露名为 Recon 的另一套暴露控制面，曾管理 23,800 多个云与 AI 秘密；原文没有明确两者属于同一操作者或同一事件，本条不把该数字并入 6 小时案例。
* 趋势关系：PaperCut 活动展示了对特定产品的 AI 编排利用，本条则展示通用扫描/凭据流水线。两者共同点是把失败反馈交给 Agent，但受害基础设...