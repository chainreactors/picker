---
title: 300页紫队演练实战指南：别再红蓝各打各的
url: https://mp.weixin.qq.com/s/pld8BwiHyydrh_YjwZIdOg
source: Doonsec's feed
date: 2026-10-26
fetch_date: 2026-10-27T07:03:06.638643
---

# 300页紫队演练实战指南：别再红蓝各打各的

# 300页紫队演练实战指南：别再红蓝各打各的

原创

计算机与网络安全
计算机与网络安全

计算机与网络安全

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

[企业网络安全责任制实施办法.docx、网络安全事件报告与处置制度.docx、系统开发安全管理制度.docx、网络安全应急响应与灾难恢复制度.docx、网络安全风险评估管理制度.docx、网络安全责任制实施办法.docx、企业网络安全管理办法.docx、供应链网络安全管理制度.docx、软件供应链安全管理制度.docx、漏洞与补丁管理制度.docx](https://mp.weixin.qq.com/s?__biz=MjM5OTk4MDE2MA==&mid=2655293752&idx=4&sn=542faf284cbe4c38f4d8ca79773c5327&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/sz_mmbiz_png/oCABd1XUc0iaITlicGDnPia3jKSm5ZARRu9OaqHKlZSxIDH93cFNL7YdzWt478cUvynXLQBvQuZFLMbGuRIhxC2PQxBZdicUmGZ8gdQA6SS5nP8/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MjM5OTk4MDE2MA==&mid=2655293752&idx=4&sn=542faf284cbe4c38f4d8ca79773c5327&scene=21#wechat_redirect)

这份材料系统讲解“紫队演练”（Purple Teaming）：红队与蓝队不再彼此隔离，而是共享信息、协同执行攻击、即时验证检测与响应能力，用更短反馈闭环提升防御成熟度。全文可分为三大部分：理论方法、攻防实验、组织运营。

## 紫队如何工作

### 1. 紫队演练的定位

材料先把技术安全测试分为几类：

* **红队**：最接近真实攻击，隐蔽性强，强调业务化目标，检验整体安全态势。
* **假定失陷测试**：假定攻击者已获得某个起点，重点检验检测、响应、遏制能力。
* **渗透测试**：针对特定应用、网络、平台找漏洞，重资产安全弱点。
* **漏洞评估**：偏配置、补丁、弱口令、暴露面，攻击性较弱。
* **紫队**：核心是协作、透明、知识共享。它不追求红队式隐蔽，而是回答：攻击是否被记录？是否告警？是否阻断？蓝队能否调查和响应？

紫队两大收益：

1. **缩短反馈闭环**：攻击一执行，防守方立即验证日志、告警、阻断和流程。
2. **提高测试覆盖**：可把端到端攻击拆成单个技术，也可按真实攻击链验证。

### 2. 两种核心方法

* **原子式紫队**：把攻击链拆成单个技术或过程，逐个测试。灵活、可自动化、适合检测工程、回归测试、工具评估、环境对比和行业对比。
* **场景式紫队**：按攻击时间顺序还原端到端攻击链，检验检测、调查、响应、遏制、流程和人员协同。更真实，但资源投入更高。
* 实际中常混合使用：原子测试快速验证单点检测，场景测试检验整体响应。

### 3. 建立紫队能力

材料强调先判断“ readiness ”：

* 组织是否已有检测响应能力？
* 发现问题后是否有资源改进？
* 是否有人员能消化结果并落地？
* 内部团队还是外部团队？考虑交付周期、频率、新兴威胁响应、成本。
* 所需能力包括沟通、攻击技术、软件开发、威胁情报研究。
* 技术条件包括测试环境、攻击工具、指标共享、实时通信、跟踪平台、结果消费机制。

### 4. 攻防框架

材料重点介绍：

* **TTP**：Tactics 战术、Techniques 技术、Procedures 过程。
* **MITRE ATT&CK**：按战术、技术、子技术、组织、软件、活动、缓解、数据源组织知识库；ATT&CK Navigator 可做覆盖热图。
* **D3FEND**：防御技术框架，含 Model、Harden、Detect、Isolate、Deceive、Evict。
* **CAR**：Cyber Analytics Repository，提供检测分析思路。
* **Cyber Kill Chain**：侦察、武器化、投递、利用、安装、命令控制、目标行动。
* **Diamond Model**：每个攻击事件含对手、能力、基础设施、受害者四要素，并有时间、阶段、结果、方向、方法、资源等元特征；可构建活动线程和活动-攻击图。
* **Pyramid of Pain**：从哈希、IP、域名、网络/主机痕迹、工具到 TTP，越往上检测越难被规避，对攻击者越“痛”。

## 原子式与场景式方法详解

### 1. 原子式方法论

应用场景包括：

* 性能基准对比；
* 不同环境检测能力对比；
* 安全工具评估；
* 自动化与回归测试；
* 行业对比；
* 将攻击链“去链化”，独立测试每个技术。

输入来源：

* 威胁情报与事件报告；
* 红队/攻击测试输出；
* 安全工具宣称能力；
* 安全研究。

材料以“枚举 Domain Admins 组成员”为例，展示同一技术的多种过程：

* `net group "Domain Admins" /domain` 及参数变形、混淆；
* PowerShell ADSI、RSAT、PowerView；
* AdFind；
* 内存执行工具、BOF、Recon-AD、SOCKS+Impacket 等。

关键概念：

* **能力抽象**：不同工具底层可能都走 SAMR、LDAP 等同一能力面，检测应尽量落在更底层、更通用的行为上。
* **攻击复杂度金字塔**：`net.exe` 简单常见，PowerShell、AdFind、内存工具逐级更复杂；检测高复杂度不代表覆盖低复杂度。
* 每个测试用例重点记录：

+ **Telemetry**：是否有高保真、集中化、及时的日志；
+ **Alerting**：是否告警，告警是否准确、可操作；
+ **Prevention**：是否直接或间接阻断。

* 原子测试不适合很好验证聚合检测、风险评分、UEBA、定时扫描等依赖序列或多事件的检测。
* 执行前要做防御预检，如 EICAR 文件、允许列表、日志转发检查；记录执行人、主机、目标、命令、结果等元数据；用雷达图、阶段图、告警潜力图展示结果。
* **微仿真**：介于原子和场景之间，用少量多步行为验证依赖序列的检测。

### 2. 场景式方法论

应用包括：

* 性能基准；
* 攻击熟悉度训练；
* 流程、告警、文档审查；
* 检测工程；
* 评估调查、遏制、响应时间。

场景式强调：

* 规划攻击链，可只覆盖部分阶段，如从假定失陷开始或到横向移动结束；
* 先做遥测审查，确认关键日志存在；
* 可在演练中做“快速修复—复测”的检测改进；
* 输入包括威胁情报过程、既有攻击链、威胁建模数据；
* 威胁建模可使用 STRIDE 等思路。

材料用 ALPHV 勒索攻击案例串起完整场景：

1. 钓鱼邮件 + 密码保护 ZIP + VBScript；
2. VBScript 释放 DLL，`regsvr32`、`rundll32` 执行；
3. 计划任务持久化；
4. `net`、`nltest`、`systeminfo`、`ipconfig` 等发现；
5. 安装 ScreenConnect RMM；
6. BITSAdmin、Certutil、PowerShell 下载 Cobalt Strike；
7. CSharp Streamer 等 C2；
8. SMB、WMI、RDP 横向移动；
9. LSASS 转储、DCSync；
10. 自定义工具收集文件共享数据；
11. Rclone 通过 SFTP 外传；
12. `xcopy`、`wmic` 部署勒索软件、删除 Veeam 备份。

场景式数据捕获更丰富：

* 聚合检测、风险评分、UEBA；
* 告警关联、 pivoting、调查完整攻击链；
* **TTD** 检测时间、**TTI** 调查时间、**TTR** 修复时间、**TTC** 遏制总时间；
* 可绘图展示“告警前进展”“阻断前进展”“已阻止阶段”；
* 可比较多次演练，观察防御是否左移。
* 执行时要处理蓝队透明度、是否允许完整响应、是否“遏制后释放”、是否只记录告警、是否注入假告警触发调查。
* 自定义工具要尽量贴近真实恶意软件行为，同时注意检测痕迹与安全边界。

## 攻击仿真与检测实验

### 1. 实验环境

使用 Splunk Attack Range 搭建实验室，部署：

* 域控、域成员 Windows、Linux、Kali、Zeek、Splunk；
* Sysmon、Aurora EDR、BadBlood、红队工具；
* 通过 Guacamole、RDP、SSH 访问；
* Splunk 查询日志，支持导出、回放、自动化执行 PurpleSharp、Atomic Red Team。

### 2. 遥测来源

* **Windows 事件日志**：Security、System、Application、Forwarded Events、Applications and Services Logs；审计策略类别；Event Viewer XPath、`wevtutil`。
* **PowerShell 日志**：脚本块日志 4104、转录、AMSI；攻击者可降级 PowerShell 2、绕过 AMSI。
* **Sysmon**：进程创建、网络连接、驱动加载、文件创建、注册表、命名管道、WMI、DNS、进程注入等；可配置包含/排除规则；Linux 版也支持。
* **Zeek**：网络日志，如 `ntlm.log`、`kerberos.log`、`dce_rpc.log`、`ldap_search.log`、`dns.log`、`notice.log`；BZAR 插件可映射 ATT&CK。
* **ETW**：控制器、提供者、消费者；可追踪 DNS、LDAP、.NET 等；Sysmon 22 对 DNS 查询做了聚合增强。
* **osquery**：SQL 查询主机状态、计划任务、进程、socket、文件路径、查询包、装饰器、差异日志。
* **YARA**：静态文件和进程内存扫描；规则含 meta、strings、condition；可用于 Mimikatz 等检测。
* **Sigma**：厂商无关 YAML 检测规则，可用 pySigma 转换为 Splunk 等查询。

### 3. Atomic Red Team 实验

场景：开发者构建被污染的 C# 项目，`MSBuild.exe` 执行内联任务，启动编码 PowerShell；随后 PowerShell 下载并反射加载 Seatbelt。

* 使用 Invoke-AtomicRedTeam 执行 atomics；
* ATTiRe 格式记录命令和输出，可导入 VECTR；
* 检测思路：

+ 父进程 `MSBuild.exe` 启动 `powershell.exe`；
+ Splunk 实时告警；
+ 脚本块日志拼接，搜索 `Seatbelt`、`Invoke-Seatbelt`、`.NET Reflection` 加载；
+ 用 AppLocker 阻止 MSBuild、限制脚本、启用 Constrained Language mode。

### 4. MITRE Caldera 实验

用 Caldera 做 Active Directory 侦察：

* 部署 Caldera，使用 Sandcat agent；
* 理解 abilities、executors、facts、parsers、requirements、adversary profiles、operations、planners、obfuscators；
* 创建能力：

+ `nltest /domain_trusts /all_trusts`
+ `nltest /dclist:%USERDOMAIN%`
+ `net group "Domain Admins" /domain`
+ PowerView `Get-DomainComputer -OperatingSystem *server*`
+ PowerView `Get-DomainUser -SPN`

* 检测：

+ 命令行参数规则，如 nltest 侦察 Sigma 转 Splunk；
+ 阈值告警：短时间内多条 AD 侦察命令；
+ 用 SilkService 采集 LDAP ETW 日志，转发 Splunk；
+ 识别 PowerView 生成的 LDAP 过滤器，如 Kerberoastable 用户和服务器枚举。

### 5. Mythic 实验

用 Mythic 完成域控妥协：

* 安装 HTTP/SMB C2 profile、Apollo agent；
* 创建 operation，生成 payload；
* 通过 Jupyter/API 脚本化任务；
* 模拟：

+ 本地管理员 + 域管理员登录；
+ 窃取域管理员 token；
+ 上传 SMB agent 到域控 `ADMIN$`；
+ `wmiexecute` 执行；
+ `link` 建立点对点 SMB 通信；
+ 注入 `mmc.exe`；
+ `mimikatz lsadump::dcsync /all` 执行 DCSync。

* 检测：

+ Sysmon 11 检测 `ADMIN$`/`C:\Windows` 下可执行文件创建；
+ Zeek `smb_files.log` 检测 ADMIN$ 文件上传；
+ `WmiPrvSE.exe -secured -Embedding` 子进程；
+ Splunk lookup 文件限定域控主机；
+ Zeek `dce_rpc.log` 中 `DRSGetNCChanges`，排除域控来源，检测 DCSync。

## 组织、跟踪与报告

### 1. 报告与跟踪

* 演练数据敏感，需考虑访问控制、RBAC、审计日志、保留策略、加密、离线存储。
* 跟踪方式：

+ **工单系统**：Jira 等，适合任务流转、评论、附件、内置指标、API；
+ **Kanban**：To-Do、In Progress、Done、Blocked、Triage、Validation，可设 WIP 限制；
+ **电子表格**：字段包括时间 UTC、测试 ID、名称、战术、技术、执行说明、遥测、告警、阻断、工具、技术领域；
+ **VECTR**：环境、组织、评估、活动、测试用例、报告；支持 Metrics、Heat Map、Resilience Trending、Test Case Drilldown；可导入 ATTiRe。

* 报告分三类受众：

+ **战术**：给 SOC、检测工程、响应人员，含命令、日志、规则、检测建议；
+ **运营**：给安全管理和架构师，含覆盖、差距、ROI、人员流程技术；
+ **战略**：给高管和董事会，含韧性、残余风险、行业对比、投资方向。

* 建议结构：执行摘要、发现与建议、方法与范围、场景走查、技术附录。
* 发现应从“人员、流程、技术”三方面分析：技能、协作、Playbook 完整性、工具覆盖、日志管道、告警质量等。

### 2. 实施紫队职能

* 规划：排期、基础设施、授权、变更控制、定义角色。
* 角色：

+ 攻击队：沟通需求、共享 IoC、执行和记录测试、进度报告、技术研讨；
+ 防御队：监控告警、查询日志、评估遥测/告警/阻断、调查遏制、协作改进；
+ 工程与行政：准备主机、配置工具、允许列表、处理故障、补充日志源。

* 工作坊与访谈：

+ 设定目标与方法；
+ 规划后勤；
+ 收集技术信息；
+ 蓝队访谈：检测理解、调查走查、痛点、协作改进；
+ 收集反馈。

* 成熟化：

+ 攻击自动化与 BAS；
+ 明确自动化产物归属；
+ 告警回归测试：准备依赖、执行、捕获输出、验证告警、关闭工单、创建漏报告警工单、清理；
+ 持续紫队循环：发现、分类、运营化、维护；
+ KPI 要避免“只看数量”：测试过程数、演练次数、发现差距数、新检测数、调优检测数、验证检测数、新自动化攻击数；要防止重数量轻质量。

## 附录与总体结论

附录提供：

* 场景式测试用例完整清单，覆盖初始访问、持久化、发现、C2、横向移动、凭据访问、收集、外传、影响；
* 高价值 Windows 事件 ID，如 4624、4625、4728、4768、4769、4688、4698、7045、5140、5145、4662、5136；
* Sysmon 事件 ID，如进程创建、网络连接、驱动加载、远程线程、进程访问、文件创建、注册表、命名管道、WMI、DNS、文件删除、进程篡改等。

总体结论：紫队演练的价值不在“攻破多少”，而在把攻击行为转化为可验证的检测、阻断、调查和响应改进；原子式适合检测工程和回归，场景式适合检验整体响应；框架提供共同语言，实验环境提供可重复验证，跟踪报告和组织流程决定演练能否真正推动安全成熟。最核心的建议是：先从可执行的小规模演练开始，持续迭代。

实战紫队演练 PDF已上传👇

![](https://res.wx.qq.com/t/wx_fed/we-emoji/res/assets/Expression/Expression_86@2x.png)6000+份资料

📁 安全制度 · 风险评估 · 应急响应 · 零信任 · 供应链安全 · 安全架构
📁 安全意识 · 软件安全 · 研发安全 · 开源 · 数字取证 · 保密/商业秘密

**✅ 以上所有资料，成员可随时下载/查看，每天更新**

[点击立即加入「网络安全运营运维」](https://mp.weixin.qq.com/s?__biz=MjM5OTk4MDE2MA==&mid=2655293752&idx=4&sn=542faf284cbe4c38f4d8ca79773c5327&scene=21#wechat_redirect)

# [立即加入网络安全AI安全群](https://mp.weixin.qq.com/s?__biz=MjM5OTk4MDE2MA==&mid=2655310879&idx=2&sn=f3a969fdcf9dfb95e8e3233ad2b99a58&scene=21#wechat_redirect)

-

预览时标签不可点

阅读原文

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

![...