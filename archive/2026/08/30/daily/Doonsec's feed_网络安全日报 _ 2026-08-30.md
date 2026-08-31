---
title: 网络安全日报 | 2026-08-30
url: https://mp.weixin.qq.com/s/i3TgikQJnB_6bC4i-nEs2g
source: Doonsec's feed
date: 2026-08-30
fetch_date: 2026-08-31T07:51:11.180336
---

# 网络安全日报 | 2026-08-30

# 网络安全日报 | 2026-08-30

CyberSecurityDaily

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

网络安全日报 | 2026-08-30

2026年8月30日（星期日） | 数据来源：CISA KEV / NVD / MITRE CVE / CVE.org / PaperCut / BleepingComputer / The Hacker News / CISA / CVETodo / BtCIRT / 安恒威胁情报 / Vercel / Uber / GitHub

|  |  |  |  |
| --- | --- | --- | --- |
| 2 极危事件 | 2 高危事件 | 2 中危事件 | 8 关注漏洞 |

|  |  |  |
| --- | --- | --- |
| 🌐 | 安全热点 | 6 条 |

WordPress 插件危机：五大严重漏洞齐发

📰 来源 The Hacker News / Shield53 · 📅 日期 2026-08-28~29

Wordfence 与 Patchstack 协调披露 WPMU DEV Dashboard（CVE-2026-76581，9.8）、Avada（CVE-2026-18431，9.8）、TranslatePress（CVE-2026-19632，9.8）、Pods（CVE-2026-19598，9.8）与 GiveWP（CVE-2026-82222，10.0）。前四者分别导致未授权管理员接管与 RCE；GiveWP 经反序列化链实现预认证 RCE，影响 10 万+ 站点。

ServiceNow AI 平台三连 CVSS 10.0

📰 来源 CVETodo · 📅 日期 2026-08-27

ServiceNow 同日披露 AI 平台三个满分漏洞：CVE-2026-74820（SQL 注入）、CVE-2026-18885（代码注入）等，均未认证、网络可达、低复杂度、无需用户交互。官方称暂无恶意利用，但其组合已列受影响机构修复队列首位。

Keycloak 账户接管漏洞 CVE-2026-18963

📰 来源 BtCIRT · 📅 日期 2026-08-28

开源 IAM 平台 Keycloak 重置密码流程存在状态校验缺陷（CWE-640），未认证攻击者可绕过邮箱验证直接重置任意账户（含管理员）密码，CVSS 9.1。已修复于 26.4.15 / 26.6.6 / 26.7.2 等版本。

PaperCut 双零日被在野利用，首补遭绕过

📰 来源 BleepingComputer / Hackread · 📅 日期 2026-08-27~28

PaperCut NG/MF 两个零日（CVE-2026-81578，8.8，认证绕过；CVE-2026-82078，9.4，不安全动态类加载）被链式利用实现预认证 RCE；watchTowr 发现首补多路绕过，08-28 发布 Emergency Patch Release 2。

npm 供应链攻击 “Mini Shai-Hulud”

📰 来源 Undercode Testing · 📅 日期 2026-08-29

@7nohe/openapi-react-query-codegen 十个恶意版本通过 CI 触发式发布工作流注入可信身份，加载器窃取云凭证、GitHub Actions 密钥与 AI agent 配置，且全部携带有效 npm provenance 证明，极具迷惑性。

CISA KEV 8/27：ownCloud / Linux 内核 / JFrog 在野利用

📰 来源 CISA · 📅 日期 2026-08-27

CISA 将 CVE-2023-49105（ownCloud 不当认证，9.8）、CVE-2026-53362（Linux 内核 IPv6 内存破坏，7.8）、CVE-2026-66384（JFrog 路径遍历）加入 KEV，均基于在野利用证据；联邦机构须优先修复。

|  |  |  |
| --- | --- | --- |
| 🔥 | 高危漏洞监测 | 8 条 |

CVE-2026-82222CVSS -

**受影响产品：**PHP 反序列化 → RCE（CWE-502）

**漏洞描述：**10.0

**利用状态：**PoC 公开，暂无在野  ·  **补丁状态：**BleepingComputer [3-1]

CVE-2026-81578CVSS -

**受影响产品：**认证绕过（CWE-306）

**漏洞描述：**8.8

**利用状态：**在野利用  ·  **补丁状态：**BleepingComputer [3-2]

CVE-2026-82078CVSS -

**受影响产品：**不安全动态类加载（CWE-470）

**漏洞描述：**9.4

**利用状态：**在野利用  ·  **补丁状态：**BleepingComputer [3-2]

CVE-2026-18885CVSS -

**受影响产品：**代码注入（CWE-94）

**漏洞描述：**10.0

**利用状态：**暂无在野  ·  **补丁状态：**CVETodo [3-3]

CVE-2026-82460CVSS -

**受影响产品：**路径遍历（CWE-22）

**漏洞描述：**9.3 / 9.8

**利用状态：**公开披露  ·  **补丁状态：**CVE.org [3-4]

CVE-2026-18963CVSS -

**受影响产品：**弱密码恢复 / 账户接管（CWE-640）

**漏洞描述：**9.1

**利用状态：**暂无在野  ·  **补丁状态：**BtCIRT [3-5]

CVE-2026-70419CVSS -

**受影响产品：**OS 命令注入（CWE-78）

**漏洞描述：**9.1

**利用状态：**暂无在野  ·  **补丁状态：**安恒威胁情报 [3-6]

CVE-2023-49105CVSS -

**受影响产品：**不当认证（CWE-287）

**漏洞描述：**9.8

**利用状态：**KEV 在野  ·  **补丁状态：**CISA [3-7]

|  |  |  |
| --- | --- | --- |
| 📝 | 技术博客精选 | 3 条 |

Aviatrix — GiveWP CVE-2026-82222 攻击链拆解

📰 来源 Aviatrix Threat Research · 📅 日期 2026-08-28

【可学技术】文章给出完整 kill chain 分级（初始访问 T1190 → 有效账户 T1078 → 防御规避 → 执行 T1059.004 → 持久化 T1505.003 → 提权 T1068），剖析 “safe unserialize” 绕过、捐赠流注入恶意序列化对象、bundled 库 gadget 链触发系统命令的路径，并附 MITRE ATT&CK 映射，可直接用于检测规则编写。

Shield53 — WordPress 五大漏洞的生态系统级分析

📰 来源 Shield53 · 📅 日期 2026-08-29

【可学技术】从架构反模式角度解释为何插件重实现用户注册会绕过 WordPress 原生安全配置；归纳 CMS RCE 通用 triad——不可信数据进入反序列化 sink、存储型向量、生产环境遗留的 gadget 链，对防御方做依赖审计与虚拟补丁有可直接复用的方法论。

Undercode — CopyFail CVE-2026-31431：AI 发现的内核页缓存破坏与容器逃逸

📰 来源 Undercode Testing · 📅 日期 2026-08-29

【可学技术】报道 AI 工具 4 个月定位一处潜伏 9 年的内核 crypto 代码页缓存破坏（CVE-2026-31431），被入侵 pod 可破坏 setuid 二进制实现容器逃逸，影响 EKS/GKE/AKS；提供 Pod Security Standards 加固、禁用非必要 eBPF、Falco/Tetragon 运行时检测等可操作手法。

|  |  |  |
| --- | --- | --- |
| 🔧 | 安全工具动态 | 3 条 |

Cybermes — 自主红队 AI Agent 框架

📰 来源 GitHub · 📅 日期 2026-08（v2.0.0）

Zyrexnn 开源的进攻性安全 / 漏洞赏金 / 红队框架（Go + Python），内置 50+ 安全技能与 Hermes 推理引擎；“零误报关卡”要求确定性 HTTP 证据与可复现 PoC；编排 subfinder / httpx / nmap / nuclei / sqlmap / dalfox。仓库：https://github.com/Zyrexnn/Cybermes （PolyForm 非商业许可，仅限授权目标）。

deepsec — Vercel AI 代码安全扫描器

📰 来源 GitHub · 📅 日期 2026-08-18

Vercel 开源的 agent 驱动漏洞扫描器，五阶段流水线（正则扫描 → Agent 调查 → 二次验证 → 元数据丰富 → 导出），可审计整个存量代码库；Apache-2.0，支持 Vercel Sandbox 并行与 CI 集成；自带 DeepsecBench 基准（最佳模型仅发现 30.7% 已知缺陷）。仓库：https://github.com/vercel-labs/deepsec

Uber ADR — Agentic AI 检测与响应框架

📰 来源 GitHub · 📅 日期 2026-08-05

Uber 开源并已在生产环境部署的 AI Agent 安全框架（Apache-2.0），含 ADR Sensor（采集 7+ 编码 Agent 行为轨迹）、ADR-Bench（303 任务 / 133 MCP / 17 种攻击技术）、ADR Detection（双层检测）；论文被 MLSys 2026 接收。仓库：https://github.com/uber/ADR （Prevention 组件未开源）。

|  |  |  |
| --- | --- | --- |
| ⚠️ | 风险事件预警 | 6 条 |

🔴 极危

📰 来源 PaperCut / BleepingComputer / Aviatrix · 📅 日期 2026-08-27 补丁 / 08-28 披露

GiveWP ≤ 4.16.7.1 经反序列化链实现未授权 RCE，4.16.7.2 已修复并清理数据库载荷。因捐赠平台默认配置即暴露，且 WordPress 占比超 40%，实际暴露面极大。

🔴 极危

📰 来源 PaperCut / Huntress / watchTowr · 📅 日期 2026-08-27~28

链式预认证 RCE：CVE-2026-81578（8.8，认证绕过）写配置，CVE-2026-82078（9.4，不安全类加载）加载任意 Java 字节码。Huntress 在两个客户环境复现（charmap.exe 以 SYSTEM 运行），watchTowr 证实首补多路绕过，08-28 发布 Emergency Patch Release 2。

🟠 高危

📰 来源 Ghost Protocol / CISA · 📅 日期 2026-08-29

Berlin 州政府确认遭勒索，攻击者宣称窃取 5.79 TB / 约 144 万文件，归因于 Rhysida；涉及 8 月 7–12 日行政网络数据外流，市政府拒绝支付。德国已累计 9 起 Rhysida 受害者。

🟠 高危

📰 来源 Undercode Testing · 📅 日期 2026-08-29

十个恶意版本借 CI 触发式发布工作流以可信身份签发，加载器窃取云凭证、GitHub Actions 密钥与 AI agent 配置，且全部携带有效 npm provenance 证明，可绕过敏感审查。

🟡 中危

📰 来源 CISA / The Hacker News · 📅 日期 2026-08-27 KEV

ownCloud 不当认证漏洞（CVSS 9.8）被加入 CISA KEV 后，证实遭利用于窃取某菲律宾研究机构敏感核资料；影响 owncloud/core 10.6.0 – <10.13.1。

🟡 中危

📰 来源 DanSec Daily / BleepingComputer · 📅 日期 2026-08-29

医疗药品分销巨头 McKesson 披露第三方应用未授权访问与数据窃取事件，ShinyHunters 据称窃取患者数据并勒索；同期 Hasbro、ATF 亦披露相关安全事件。

|  |  |  |
| --- | --- | --- |
| 📎 | 参考来源 | 20 条 |

1. Aviatrix — GiveWP CVE-2026-82222 RCE 攻击链分析：https://aviatrix.ai/threat-research-center/givewp-wordpress-donation-plugin-cve-2026-82222-rce

2. Shield53 — 五大 WordPress 严重漏洞的 CMS 生态系统分析：https://news.shield53.com/five-critical-wordpress-flaws-cvss-98100-demand-immediate-patching-across-cms-ecosystem

3. Undercode Testing — CopyFail CVE-2026-31431 与 8/29 网络安全态势综述：https://undercodetesting.com/august-29-2026-a-day-of-reckoning-in-cybersecurity-ransomware-surge-ai-powered-exploits-and-supply-chain-attacks-video

1. Cybermes（AI 红队框架）：https://github.com/Zyrexnn/Cybermes

2. deepsec（Vercel AI 代码扫描）：https://github.com/vercel-labs/deepsec

3. Uber ADR（Agentic AI 检测与响应）：https://github.com/uber/ADR

1. GiveWP CVE-2026-82222（BleepingComputer）：https://www.bleepingcomputer.com/news/security/givewp-wordpress-donation-plugin-flaw-lets-hackers-execute-server-commands/

2. PaperCut CVE-2026-81578 / CVE-2026-82078（BleepingComputer）：https://www.bleepingcomputer.com/news/security/papercut-releases-second-emergency-patch-for-exploited-flaws/

3. ServiceNow AI CVE-2026-18885 / CVE-2026-74820（CVETodo）：https://cvetodo.com/news/cisa-adds-linux-kernel-jfrog-artifactory-and-owncloud-flaws-to-kev-catalog-as-servicenow-discloses-t

4. Cloud Commander CVE-2026-82460（CVE.org）：https://www.cve.org/CVERecord?id=CVE-2026-82460

5. Keycloak CVE-2026-18963（BtCIRT）：https://btcirt.bt/critical-keycloak-account-takeover-vulnerability-cve-2026-18963-20260828006

6. Dell Cloud Disaster Recovery CVE-2026-70419（安恒威胁情报）：https://ti.dbappsecurity.com.cn/security-info/bulletin?id=16442

7. ownCloud CVE-2023-49105（CISA KEV）：https://www.cisa.gov/news-events/alerts/2026/08/27/cisa-adds-three-known-exploited-vulnerabilities-catalog

8. WordPress 波及其他四项 CVE-2026-76581 / CVE-2026-18431 / CVE-2026-19632 / CVE-2026-19598（mangodeveloper）：https://mangodeveloper.com/articles/five-wordpress-plugins-and-themes-hit-with-critical-flaws-one-scores-perfect-100

9. CISA KEV 8/27 Linux 内核 CVE-2026-53362 / JFrog CVE-2026-66384（CVETodo）：https://cvetodo.com/news/cisa-adds-linux-kernel-jfrog-artifactory-and-owncloud-flaws-to-kev-catalog-as-servicenow-discloses-t

10. CISA KEV 8/26 NetScaler CVE-2026-8452 等六项（Infosecurity Magazine）：https://www.infosecurity-magazine.com/news/cisa-kev-microsoft-citrix/

11. npm 供应链 “Mini Shai-Hulud” @7nohe（Undercode）：https://undercodetesting.com/august-29-2026-a-day-of-reckoning-in-cybersecurity-ransomware-surge-ai-powered-exploits-and-supply-chain-attacks-video

12. Berlin 州政府 Rhysida 勒...