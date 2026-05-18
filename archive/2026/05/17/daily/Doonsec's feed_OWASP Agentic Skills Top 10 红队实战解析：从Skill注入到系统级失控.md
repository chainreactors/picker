---
title: OWASP Agentic Skills Top 10 红队实战解析：从Skill注入到系统级失控
url: https://mp.weixin.qq.com/s/W6f0nqcwgxQErU97SqWprA
source: Doonsec's feed
date: 2026-05-17
fetch_date: 2026-05-18T06:09:59.025356
---

# OWASP Agentic Skills Top 10 红队实战解析：从Skill注入到系统级失控

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/iaCwmQowIM60EeibnMbgfmzkPGfJCKjTZTRrC3VJIibWoL7euAuFZ9BKqxyUDQYFvnrYosZaZlxg72gIV5vcvkEkSzFibpsldibO8KibFH21xSpjI/0?wx_fmt=jpeg)

# OWASP Agentic Skills Top 10 红队实战解析：从Skill注入到系统级失控

原创

Al1ex
Al1ex

七芒星实验室

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

#### 文章前言

随着AI Agent、智能工作流以及具备自主执行能力的大语言模型系统快速发展，AI的安全边界正在从"模型推理"进一步扩展到"行为执行"。相比传统LLM应用，Agent系统已经不再只是"生成文本"，而是开始具备任务规划、工具调用、文件操作、Shell执行、跨系统协同以及长期记忆等能力。这意味着Agent技能(Skill)如果被恶意利用、污染或劫持，其影响范围将直接从"错误回答"升级为真实世界中的自动化攻击、权限滥用与供应链失控。OWASP在最新发布的 《OWASP Agentic Skills Top 10》中将安全关注点正式聚焦到了Agent的"行为层(Behavior Layer)"，强调Skills已成为连接模型、工具与执行系统之间最危险、也最容易被忽视的攻击面，本文将基于OWASP官方《OWASP Agentic Skills Top 10》项目，对Agentic AI Skill生态中的十大核心风险进行深入剖析，从攻击原理、真实案例、供应链风险、权限边界、Skill执行链路到企业级防御架构进行系统讲解并帮助读者全面理解AI Agent在"自主执行时代"下面临的新型攻击面并建立面向未来Agent系统的安全设计与治理思维

#### 风险类型

##### AST01:恶意技能

###### 风险介绍

Malicious Skills(恶意技能)是指攻击者通过构造、篡改或伪装AI Agent的Skill(技能/工具能力模块)，使得Agent在执行任务过程中触发恶意行为的一类安全风险。在Agentic AI系统中Skill通常负责定义Agent如何调用工具、访问资源、执行工作流以及与外部系统交互，因此一旦恶意Skill被加载或信任，攻击者就可能借助Agent获得文件访问、Shell执行、API调用、数据读取甚至系统控制能力。例如：攻击者可以在第三方Skill仓库中植入带有隐藏后门的Skill或伪装成正常自动化插件诱导开发者安装，Agent调用该Skill时便可能自动泄露敏感数据、执行危险命令或向外部服务器发送信息。OWASP将其视为Agent时代最核心的供应链风险之一，因为Skill 本质上已经成为"AI的可执行能力模块"，Skill一旦被恶意控制就等同于攻击者获得了Agent的行为控制权

###### 风险场景

Malicious Skills(恶意技能)攻击场景包括：

* SkillHub投毒攻击：攻击者向第三方Skill市场、GitHub仓库、MCP Marketplace或Agent插件中心上传带后门的Skill，利用企业对官方仓库或热门项目的信任实现供应链攻击，Agent自动安装或自动更新这些Skill时，恶意逻辑便会进入企业环境
* 恶意自动化插件类：攻击者将恶意Skill伪装成办公助手、DevOps工具、日志分析插件或自动化工作流组件，诱导开发者或企业Agent安装使用。表面上Skill能够正常完成任务，但内部会偷偷读取文件、窃取API Key、记录聊天内容或向外部服务器发送敏感数据，属于最常见的"伪装型恶意Skill攻击"
* Tool调用劫持攻击：恶意Skill在执行过程中篡改工具调用逻辑，例如：修改API参数、扩展查询范围、注入额外请求或伪造函数返回值，从而让Agent执行超出原始任务范围的危险操作，例如：读取整个目录、批量导出数据库或越权访问资源
* 隐藏式数据外传类：恶意Skill在后台静默收集并外传敏感数据，例如：聊天记录、Embedding内容、数据库信息、Token、配置文件或企业文档。由于Skill对外表现为"正常工作"，因此这类攻击往往隐蔽性极强，难以及时发现
* Shell与系统控制类：高权限Skill拥有Shell执行、Docker控制、Kubernetes操作或系统配置修改能力，Skill一旦被恶意利用，攻击者便可能借助Agent执行命令、植入后门、横向移动或控制服务器，从而将Agent变成真实的攻击入口

![](https://mmbiz.qpic.cn/mmbiz_png/iaCwmQowIM63SpO4sicEibHwLvdAstrCIEI63pK4BTLkxprtBBrA9377TRS8k6XhklagyCSHjGb6Mkk1s3jwBTNbdeJzBur9eXhicYFo9c3A0D0/640?wx_fmt=png&from=appmsg)

###### 防御措施

* 数字签名校验类：企业针对每个Skill进行签名验证，确保代码未被篡改且来源可信
* Skill白名单机制：企业仅允许经过企业认证和安全审核的Skill运行，禁止动态加载未知或未授权插件
* 供应链安全管控：企业建立自己的SKILLHUB、第三方插件市场并对上线发布的SKILL进行安全审计，建立完备的安装来源验证、发布审计管理机制，防止恶意SKILL投毒、版本篡改和恶意更新风险

```
						┌──────────────────────────────────────────────────────────────┐						│                    🧑 AI Agent应用层                         │						│        - Agent / Workflow / Multi-Agent System               │						└──────────────────────────────────────────────────────────────┘						                              │						                              ▼						┌──────────────────────────────────────────────────────────────┐						│            🔐 Skill / Tool入口控制层（Gateway）               │						│  - Skill白名单机制（Whitelist Only）                          │						│  - 数字签名校验（Signature Verification）                     │						│  - 来源可信验证（Trusted Registry）                           │						│  - 版本锁定（Version Pinning）                                │						└──────────────────────────────────────────────────────────────┘						                              │						                              ▼						┌──────────────────────────────────────────────────────────────┐						│           🔍 供应链安全扫描层（Supply Chain Scanner）         │						│  - 依赖包扫描（SCA: Software Composition Analysis）           │						│  - 恶意代码检测（Backdoor / Trojan Detection）                │						│  - Skill行为分析（Behavior Profiling）                        │						│  - 模型/数据投毒检测（Data & Model Validation）                │						└──────────────────────────────────────────────────────────────┘						                              │						                              ▼						┌──────────────────────────────────────────────────────────────┐						│            ⚙️ CI/CD & 更新控制层（Release Guard）             │						│  - 更新审批流程（Manual Approval Gate）                       │						│  - 版本可回滚机制（Rollback Safety）                          │						│  - 发布链路审计（Release Provenance Tracking）                │						│  - 制品签名验证（Artifact Signing）                           │						└──────────────────────────────────────────────────────────────┘						                              │						                              ▼						┌──────────────────────────────────────────────────────────────┐						│            🧱 运行时隔离层（Runtime Sandbox）                 │						│  - Skill容器隔离（Container / VM Sandbox）                    │						│  - 文件系统隔离（FS Isolation）                               │						│  - 网络访问控制（Egress Filtering）                           │						│  - 系统调用限制（Syscall Restriction）                        │						└──────────────────────────────────────────────────────────────┘						                              │						                              ▼						┌──────────────────────────────────────────────────────────────┐						│            🧠 Agent行为控制层（Policy Engine）                 │						│  - Tool调用策略控制（Tool Policy Enforcement）                 │						│  - 最小权限访问（Least Privilege Access）                      │						│  - Prompt Injection联动检测                                   │						│  - 异常行为识别（Behavior Anomaly Detection）                 │						└──────────────────────────────────────────────────────────────┘						                              │						                              ▼						┌──────────────────────────────────────────────────────────────┐						│            🔒 数据与密钥安全层（Data Security Layer）         │						│  - Secrets Vault（API Key / Token管理）                      │						│  - 数据最小化访问（Data Minimization）                        │						│  - 敏感数据脱敏（Data Masking）                               │						│  - 加密存储与传输（Encryption at Rest / Transit）             │						└──────────────────────────────────────────────────────────────┘						                              │						                              ▼						┌──────────────────────────────────────────────────────────────┐						│            📊 监控审计与响应层（Observability）               │						│  - Skill执行日志审计（Full Trace Logging）                    │						│  - 数据外传检测（Exfiltration Detection）                     │						│  - 异常调用告警（Anomaly Alerting）                           │						│  - 自动隔离与Kill Switch                                      │						└──────────────────────────────────────────────────────────────┘
```

##### AST03:过度授权风险

###### 风险介绍

Over-Privileged Skills(过度授权的技能)是指AI Agent中Skill在设计或部署过程中被赋予了超出其实际功能需求的权限，从而在被误用、被攻击或被恶意触发时可能对系统造成更大范围影响的一类安全风险。在Agentic AI架构中Skill通常用于执行特定任务，例如：文件读取、API调用、数据库查询或系统操作，但是当这些Skill被默认授予"全量访问权限"或"管理员级权限"时，遭遇到Prompt Injection、Malicious Skills或供应链攻击就可能被滥用执行敏感操作，例如：批量导出数据、修改系统配置、访问敏感文件或调用高风险API。OWASP将此类问题视为典型的"权限边界失控"风险，其本质是没有遵循最小权限原则，导致Skill从"功能组件"演变为了高风险执行单元，因此必须通过细粒度权限控制、动态授权与运行时策略约束来限制其影响范围

###### 风险场景

SKILL过度授权的攻击场景包括：

* SKill 过度权限被滥用：Skill被赋予文件系统全读写、数据库全访问或云资源管理等高权限，一旦被触发即可直接执行高危操作，导致系统级数据泄露或配置篡改。
* Prompt间接驱动攻击：攻击者通过构造诱导性Prompt，使Agent在“正常任务执行”的名义下自动调用高权限Skill，从而实现合法调用链下的恶意操作。
* 自动化执行放大风险：由于Agent具备自动调用Skill并执行多步骤任务的能力，攻击行为无需人工确认即可完成，使得风险在执行链路中被指数级放大
* 大规模数据外泄风险：SKILL被过度授权可能一次性访问并导出全量数据库、敏感文件或密钥信息，导致企业核心数据被批量泄露
* 隐蔽性强难以检测类：Skill执行行为在系统层面表现为“合法任务完成”，缺乏明显异常特征，使攻击行为容易长期潜伏且难以及时发现

![](https://mmbiz.qpic.cn/sz_mmbiz_png/iaCwmQowIM60nWNiaodBjETLREyBXzZz6iaZEtz0K2qxBYqyIsW7q8iaeaGKic3K20LGeH8y1GKancGZic2b7NG4ny8r0kKzwyvQiaqo6txBX8LHZo/640?wx_fmt=png&from=appmsg)

###### 防御措施

* 最小权限原则：为每个Skill仅分配完成其功能所必需的最低权限，避免赋予全局访问或管理员级权限，从源头限制攻击面
* 细粒度权限控制：涉及SKILL需要对文件、数据库、API和云资源操作时需要进行分级授权，例如：按表、目录、字段或接口级别限制访问范围
* 高风险操作人工审批：对数据导出、系统配置修改、批量删除等敏感操作强制引入人工确认流程
* API访问白名单控制：仅允许Skill调用经过批准的API接口，禁止动态调用未知或高风险接口
* 敏感操作隔离执行：将删除、写入、支付、权限变更等操作放入独立执行环境，并设置额外安全校验
* 审计日志可追溯性：记录所有Skill的权限申请、调用路径与执行结果，支持事后追踪与攻击溯源

##### AST04:不安全元数据

###### 风险介绍

Insecure Metadata(不安全的元数据)是指AI Agent在使用Skill、工具、模型或外部资源时，其依赖的元数据信息(例如：描述信息、权限声明、参数说明、调用示例、版本信息或配置文件)被攻击者篡改、伪造或滥用，从而误导Agent的决策与执行行为的一类安全风险。在Agentic AI系统中元数据通常用于指导模型如何选择工具、如何调用Skill以及如何理解输入输出结构，但由于这些信息往往以"非结构化文本"或"弱校验配置"的形式存在，攻击者可以通过修改Skill描述、注入恶意提示词、伪造工具说明或篡改参数定义，使Agent错误地选择高风险工具、...