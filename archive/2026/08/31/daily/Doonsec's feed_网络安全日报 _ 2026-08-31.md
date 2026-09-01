---
title: 网络安全日报 | 2026-08-31
url: https://mp.weixin.qq.com/s/WqyxD6ey5k7c_Sut7shhCA
source: Doonsec's feed
date: 2026-08-31
fetch_date: 2026-09-01T06:57:45.507397
---

# 网络安全日报 | 2026-08-31

# 网络安全日报 | 2026-08-31

CyberSecurityDaily

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

网络安全日报 | 2026-08-31

2026年8月31日（星期一） | 数据来源：CISA KEV / NVD / MITRE CVE / CVE.org / VulnCheck / ThreatAft / Armis / Ionix / Tenable / Rapid7 / Aviatrix / malwr-analysis / SecureBlink / GitHub / The Hacker News / 安全内参

|  |  |  |  |
| --- | --- | --- | --- |
| 3 极危事件 | 1 高危事件 | 1 中危事件 | 7 关注漏洞 |

|  |  |  |
| --- | --- | --- |
| 🌐 | 安全热点 | 6 条 |

MCP 生态安全危机集中爆发：9+ CVE，CVE-2026-81735 10.0 领衔

📰 来源 ThreatAft / VulnCheck · 📅 日期 2026-08-27~31

Model Context Protocol 服务器生态出现批量漏洞披露，CVE-2026-81735（UI-TARS-desktop @agent-infra MCP，10.0）领衔——mcp-http-server 绑定全部网络接口且无认证，暴露 run\_command 与 filesystem 工具。同批还有 tiger-gh-mcp-server DNS 重绑定（CVE-2026-81100，6.8）、browse-mcp 路径遍历→RCE（CVE-2026-55557，8.7）、Actors MCP Server SSRF→云元数据（CVE-2026-81093，7.8）等，反映大量 MCP 服务器出厂即「无认证、无授权、无输入校验」。

argocd-mcp CVE-2026-82456：CVSS 10.0 完整 ArgoCD 接管

📰 来源 cve.org / ThreatAft / Ionix · 📅 日期 2026-08-29

argocd-mcp 0.8.0 在 HTTP 传输模式下将监听绑定到所有网络接口（0.0.0.0）且不校验调用方凭证，一旦配置了 ARGOCD\_API\_TOKEN，任意可达网络的攻击者可复用运维者 token，通过 create\_application / sync\_application 等工具完全控制 Argo CD 托管的 GitOps 流水线。修复版本 0.9.0（CWE-1327）。

NASA cFS 整数下溢远程漏洞 CVE-2026-82480

📰 来源 cve.org / Tenable / Rapid7 · 📅 日期 2026-08-29~30

NASA 核心飞行软件（cFS）7.0.0–7.0.1 的 cFE Software Bus 组件 CFE\_SB\_GetUserDataLength 函数对 TotalMsgSize/HdrSize 处理存在整数下溢（CWE-189/191），可远程触发，CVSS 3.1 7.4 / 4.0 5.3。厂商 early contact 未回应，目前无官方补丁，需通过网络限制缓解。

JFrog Artifactory 默认配置未授权管理员接管 CVE-2026-82329

📰 来源 cve.org / Armis / Ionix · 📅 日期 2026-08-28

JFrog Artifactory 认证层存在不当认证缺陷（CWE-287），默认配置下未认证网络攻击者可获得管理员权限，进而篡改托管制品、注入后门、窃取源码与密钥。修复版本覆盖 7.111.21 / 7.117.28 / 7.125.20 / 7.133.29 / 7.146.38 / 7.161.20，JFrog 云实例已由厂商修补。

IBM Langflow 与 Yamcs 两例 9.8 分 RCE（A2A 端点 / 模板注入）

📰 来源 NVD / CVE.org / dbugs · 📅 日期 2026-08-28

IBM Langflow OSS 1.0.0–1.11.1 的 A2A 公开端点在未认证情况下接受并执行用户提交代码（CWE-94，CVE-2026-19286，9.8）；Yamcs 任务控制框架在 5.12.8 / 5.13.2 之前将 templateArgs 经 VarStatement.append 注入 YAML 而未经上下文转义，可注入 org.yamcs.ProcessRunner 服务实现 RCE（CWE-94/470/1336，CVE-2026-55559，9.8）。

Carhartt / ShinyHunters 数据注水经 HIBP 核实真实 12.9M 账户

📰 来源 Aviatrix / Factlen / Bruno Digital · 📅 日期 2026-08-26~29

ShinyHunters 宣称窃取 Carhartt Databricks 平台 50GB+、约 24.8M 邮件地址，Troy Hunt 经 Have I Been Pwned 与 PwnedClaw 分析发现近半数来自 TPC-DS 合成基准数据（tpcds\_sf1000，含 .edu / .org 伪造域名与 1900 年代生日），实际真实账户为 12,933,413 个，含约 1.5 万员工邮箱；Carhartt 已拒绝 330 万美元赎金。

|  |  |  |
| --- | --- | --- |
| 🔥 | 高危漏洞监测 | 7 条 |

CVE-2026-82456CVSS 0.8.0

**受影响产品：**绑定非受限 IP 地址（CWE-1327）

**漏洞描述：**10.0

**利用状态：**公开披露，无认证接管  ·  **补丁状态：**cve.org / ThreatAft

CVE-2026-81735CVSS -

**受影响产品：**缺失身份验证（CWE-306）

**漏洞描述：**10.0

**利用状态：**公开披露，RCE  ·  **补丁状态：**ThreatAft / VulnCheck

CVE-2026-81096CVSS 1.2.6

**受影响产品：**代码生成控制不当（CWE-94）

**漏洞描述：**10.0 / 9.3

**利用状态：**公开披露，沙箱逃逸  ·  **补丁状态：**cve.org / Ionix

CVE-2026-82329CVSS -

**受影响产品：**不当认证（CWE-287）

**漏洞描述：**9.8

**利用状态：**公开披露，默认接管  ·  **补丁状态：**cve.org / Armis

CVE-2026-19286CVSS 1.0.0

**受影响产品：**代码注入（CWE-94）

**漏洞描述：**9.8

**利用状态：**公开披露，A2A 端点 RCE  ·  **补丁状态：**NVD / IBM

CVE-2026-55559CVSS 5.12.8

**受影响产品：**代码注入 / 模板注入（CWE-94/470/1336）

**漏洞描述：**9.8

**利用状态：**公开披露，YAML 注入 RCE  ·  **补丁状态：**CVE.org / dbugs

CVE-2026-82480CVSS 7.0.0

**受影响产品：**整数下溢（CWE-189/191）

**漏洞描述：**7.4 / 5.3

**利用状态：**远程可利用，未修复  ·  **补丁状态：**cve.org / Tenable

|  |  |  |
| --- | --- | --- |
| 📝 | 技术博客精选 | 3 条 |

Aviatrix — Carhartt / ShinyHunters 数据注水验证（TPC-DS 合成数据 + PwnedClaw 检测）

📰 来源 Aviatrix Threat Research · 📅 日期 2026-08

【可学技术】文章给出 Carhartt 泄露的攻击路径（T1190 利用公网应用 → T1552 凭据 → T1005/T1119 自动化收集 → T1567.2 云存储外泄 → T1486/T1491.1 影响），并指出云数据湖普遍将生产数据与 TPC-DS 等测试基准混存，导致泄露影响评估被注水。可直接用于数据安全治理与数据分类分级的核查方法论。

ThreatAft — MCP Server Roundup：9 CVE，CVE-2026-81735 10.0 领衔

📰 来源 ThreatAft · 📅 日期 2026-08-27

【可学技术】系统梳理 MCP 服务器生态的批量漏洞，归纳「无认证 + 绑定全接口 + 暴露危险工具（run\_command / filesystem / 云元数据）」的系统性设计缺陷；给出防御方行动清单：清点全部 MCP 服务器、收敛网络暴露、及时打补丁、绝不将 MCP HTTP 服务器暴露于不可信网络。对 AI Agent 基础设施加固有直接参考价值。

malwr-analysis — 多阶段 PowerShell Loader（Vercel 托管 Grape2.zip，XOR 密钥 "write"，诱饵 "Verification complete!"）

📰 来源 malwr-analysis · 📅 日期 2026-08-08

【可学技术】详细反混淆了一个多阶段载荷链：PowerShell 从 203.188.171.166 与 dorenzaa.com 直接返回，下载 Vercel 托管的 Grape2.zip 并执行 Grape.exe；loader1.txt 以重复密钥 "write" 做 XOR 解码后落地 UltraToolliteSetup.exe；stager 以隐藏窗口运行并弹「Verification complete!」（标题 "Google.com"）作诱饵。附完整 IoC、SHA-256 与文件路径，可用于 SOC 检测规则编写。

|  |  |  |
| --- | --- | --- |
| 🔧 | 安全工具动态 | 3 条 |

Darkmoon（ASCIT31/Dark-Moon）— AI 自主渗透平台

📰 来源 GitHub · 📅 日期 2026（v1.1.0）

ASC-IT（法国）开源的自主渗透测试引擎（Python + TypeScript，GPL-3.0），多 agent 架构编排 Web / 云 / AD / Kubernetes / CMS / 网络专项子 agent，内置 50+ 攻防工具，所有工具调用经 MCP 网关校验与审计；配套隐私网关以确定性脱敏 token 替换真实 IP / 凭据，确保敏感值不出边界。仓库：https://github.com/ASCIT31/Dark-Moon

Strix（usestrix/strix）— AI 渗透与自动修复

📰 来源 GitHub · 📅 日期 2026-08-11（v1.5.3）

usestrix 开源的 agentic 安全平台（Apache-2.0），自主 agent 动态规划扫描路径、执行工具、以真实 PoC 验证漏洞并生成可合并的修复 PR，原生集成 GitHub Actions 等 CI/CD；支持 Web 应用、API 与内部基础设施测试。仓库：https://github.com/usestrix/strix

Shannon（KeygraphHQ/shannon）— 白盒 AI Web / API 渗透

📰 来源 GitHub · 📅 日期 2026-07-04（v1.9.0）

Keygraph 开源的自主白盒 AI 渗透代理（TypeScript，AGPL-3.0），结合源码分析与实际利用，仅将「有可复现 PoC」的漏洞纳入报告；覆盖 OWASP 注入 / XSS / SSRF / 鉴权绕过等，支持认证流测试与 CI/CD。XBOW 基准利用成功率约 96%。仓库：https://github.com/KeygraphHQ/shannon

|  |  |  |
| --- | --- | --- |
| ⚠️ | 风险事件预警 | 5 条 |

🔴 极危

📰 来源 cve.org / ThreatAft / Ionix · 📅 日期 2026-08-29 披露

argocd-mcp 0.8.0 在 HTTP 传输模式下监听 0.0.0.0 且不校验调用方凭证，配置 ARGOCD\_API\_TOKEN 后任意网络可达者即可复用运维 token 创建 / 同步应用，完全控制 GitOps 流水线及其部署的集群工作负载。该 MCP 服务器常运行于 AI 助手可达的内网，暴露面广。

🔴 极危

📰 来源 ThreatAft / VulnCheck / dbugs · 📅 日期 2026-08-27 披露

ByteDance UI-TARS-desktop 的 mcp-http-server 在未指定 host 时默认监听 '::'（全部接口），且认证中间件为可选——@agent-infra/mcp-server-commands 与 mcp-server-filesystem 入口未传入任何中间件，致 run\_command 工具可被任意未认证客户端以服务器运行用户身份执行任意命令，filesystem 服务同样暴露。修复边界为 commit c2ad42e3（PR #1918），但包版本仍为 1.2.4。

🔴 极危

📰 来源 cve.org / Ionix / VulnCheck · 📅 日期 2026-08-27 披露

ToolUniverse ≤ 1.2.6 的 python\_code\_executor 工具以拒绝列表而非允许列表做沙箱检查，攻击者可通过字符串属性查找或已许可模块走到字面值基类并枚举子类，获取 subprocess 模块引用；且每调用参数可在检查前放宽导入白名单。HTTP / MCP 服务器默认绑定所有接口、开启调试且无认证，任意可达者即以服务器进程身份执行代码。修复版本 1.3.0（增加 bearer token、默认回退 loopback、强化属性检查）。

🟠 高危

📰 来源 Aviatrix / Factlen / Bruno Digital · 📅 日期 2026-08-13 公开 / 08-26 核实

ShinyHunters 入侵 Carhartt 的 Databricks 分析平台并外泄 50GB+ 数据，宣称约 24.8M 邮件地址；经 Troy Hunt（Have I Been Pwned）与 PwnedClaw 核实，其中近半数为 TPC-DS 合成基准数据（tpcds\_sf1000，含伪造 .edu / .org 域名与 1900 年代生日），真实受影响账户为 12,933,413 个（含约 1.5 万员工邮箱）。Carhartt 已拒绝 330 万美元赎金，事件凸显云数据湖「生产 + 测试数据混存」的核验与治理风险。

🟡 中危

📰 来源 SecureBlink / News4Hackers / BleepingComputer · 📅 日期 2026-08-28 报备（关联 03-28 攻击）

Hasbro 通过被入侵的员工账户访问了员工个人与财务信息，于 08-28 向马萨诸塞州总检察长办公室提交泄露通知，该州记录 436 名居民受影响，暴露字段含社会保障号（SSN）、金融账户、支付卡号与驾照信息。Hasbro 全球员工约 4,600–5,000 人，实际规模更大但未披露；该事件与其 03-28 网络攻击（致系统下线、约 2,500 万美元营收损失）时间相关但公司未正式关联。

|  |  |  |
| --- | --- | --- |
| 📎 | 参考来源 | 20 条 |

1. Aviatrix — Carhartt / ShinyHunters 数据注水验证：https://aviatrix.ai/threat-research-center/carhartt-shinyhunters-databricks-breach-verification-2026

2. ThreatAft — MCP Server Roundup（9 CVE，CVE-2026-81735 10.0 领衔）：https://threataft.com/articles/mcp-server-ecosystem-roundup-cvss-10-9-cves

3. malwr-analysis — 多阶段 PowerShell Loader 分析：https://malwr-analysis.com/2026/08/08/investigating-a-multi-stage-powershell-loader/

1. Darkmoon（AI 自主渗透平台）：https://github.com/ASCIT31/Dark-Moon

2. Strix（AI 渗透与自动修复）：https://github.com/usestrix/strix

3. Shannon（白盒 AI Web / API 渗透）：https://github.com/KeygraphHQ/shannon

1. argocd-mcp CVE-2026-82456（CVE.org）：https://www.cve.org/CVERecord?id=CVE-2026-82456

2. argocd-mcp CVE-2026-82456（ThreatAft 分析）：https://threataft.com/articles/argocd-mcp-cve-2026-82456-unauthenticated-takeover

3. NASA cFS CVE-2026-82480（CVE.org）：https://www.cve.org/CVERecord?id=CVE-2026-82480

4. NASA cFS CVE-2026-82480（Tenable）：https://www.tenable.com/cve/CVE-2026-82480

5. JFrog Artifactory CVE-2026-82329（CVE.org）：https://www.cve.org/CVERecord?id=CVE-2026-82329

6. JFrog Artifactory CVE-2026-82329（Armis）：https://cve.armis.com/CVE-2026-82329

7. IBM Langflow CVE-2026-19286（N...