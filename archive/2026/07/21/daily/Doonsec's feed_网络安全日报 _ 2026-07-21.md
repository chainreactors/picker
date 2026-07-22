---
title: 网络安全日报 | 2026-07-21
url: https://mp.weixin.qq.com/s/L-XaKp_Q0pQskK0oktKmSg
source: Doonsec's feed
date: 2026-07-21
fetch_date: 2026-07-22T05:01:12.879733
---

# 网络安全日报 | 2026-07-21

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/ibWuEZyvfHZGSEtUVD9kGxCiaPL9iaMLrIIgKnTq3L9LibVcIQic3ChFVRTZpulZv9fpiadyFUAxme6JibgSxG8og5VpX6sIskiaHicn2X59daTRnxZY/0?wx_fmt=jpeg)

# 网络安全日报 | 2026-07-21

CyberSecurityDaily

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

🔐 网络安全日报

2026年7月21日（星期二） | 数据来源：NVD / CISA KEV / CNVD / CNNVD / Hackread / Infosecurity Magazine / Qualys / The Hacker News / 安全客 / FreeBuf

|  |  |  |  |
| --- | --- | --- | --- |
| 4 极危事件 | 3 高危事件 | 3 中危事件 | 2 关注漏洞 |

|  |  |  |
| --- | --- | --- |
| 📋 | 每日重点摘要 | 5 条 |

**🔴 极危：WordPress "wp2shell" 预认证 RCE 链（CVE-2026-63030 / CVE-2026-60137，CVSS 9.8 / 9.1）公开 PoC 且持续在野探测 — 全球 5 亿+ 站点暴露窗口未闭合，强制自动更新须逐站核验落地**

**🔴 极危：Windows "LegacyHive" 零日（无 CVE、无补丁）公开 PoC — 标准用户可借 User Profile Service 加载任意注册表 hive 提权至 SYSTEM，影响所有受支持 Windows，须以检测缓解应对**

**🔴 极危：Hugging Face 遭自主 AI 代理入侵（数据集加载器 RCE + 模板注入）— 1.7 万条恶意日志已用国产 GLM 5.2 开源模型数小时取证，所有用户须立即轮换访问令牌**

**🟠 高危：OpenSSL "HollowByte" 内存耗尽 DoS（无 CVE、静默修复）— 11 字节 TLS 请求即可冻结最高 25% 服务器内存且重启才恢复，须升级至 6 月 9 日修复版**

**🟡 中危：Claude Desktop "PromptFiction" 漏洞（claude:// scheme 自动执行隐藏指令）+ 俄 APT 木马化 WebEx/Zoom（Starland RAT）窃取凭据与加密货币 — AI 客户端供应链风险升温**

|  |  |  |
| --- | --- | --- |
| 🌐 | 安全热点 | 6 条 |

Windows "LegacyHive" 零日公开 PoC（无 CVE、无补丁）— 标准用户可借 User Profile Service 加载任意 hive 提权至 SYSTEM

📰 CrowdStrike / Security Affairs / IT-Connect / 安全客 · 📅 2026-07-14（07-20 广泛报道）

研究者 Nightmare Eclipse（Chaotic Eclipse / MSNightmare）在微软 7 月补丁星期二发布后数小时内公开名为 LegacyHive 的 Windows 零日 PoC。该漏洞位于 Windows User Profile Service（profsvc，以 SYSTEM 完整性运行），允许标准用户诱使服务加载攻击者可控的注册表 hive（公开版限定 usrclass.dat 并需第二用户凭据，研究者称原始版无此限制、可加载任意 hive）。利用成功后可在当前用户 classes root 挂载管理员 hive，进而实现凭据窃取与注册表持久化。目前无 CVE、无微软公告、无补丁，且 PoC 在已打 7 月补丁的机器上仍有效——这是继 RoguePlanet（CVE-2026-50656）、YellowKey、GreenPlasma 等之后，研究者与 MSRC 争执背景下又一次"披露即零日"。本地提权需先有立足点，但一旦进入内网即成为可靠的提权支点。

Hugging Face 遭自主 AI 代理入侵（数据集加载器 RCE + 模板注入）— 1.7 万条恶意日志由 GLM 5.2 数小时完成取证

📰 Hugging Face / 网易 / The Hacker News · 📅 2026-07-20

全球最大 AI 开源社区 Hugging Face 披露其服务器遭一套自主 AI 代理框架入侵：攻击者利用数据处理管线中的远程代码执行漏洞，通过上传带恶意代码的数据集，借"远程代码数据集加载器（remote-code dataset loader）"与"模板注入（template injection）"两项缺陷在处理工作节点取得执行权限，周末期间横向移动至多个内部集群收集云端与集群凭证。HF 安全团队最初调用某美国商业前沿大模型 API 分析 1.7 万余条攻击日志，但该模型因无法区分响应人员与攻击者而拒绝协助；随后 HF 在自有基础设施部署国产 GLM 5.2 开源模型，数小时内完成自动化分析。HF 已清除全部立足点、重建受损节点并轮换所有受影响令牌，呼吁用户立即轮换访问令牌并核查账户活动。

OpenSSL "HollowByte" 内存耗尽 DoS（无 CVE、静默修复）— 11 字节 TLS 请求可冻结最高 25% 服务器内存且重启才恢复

📰 Okta Red Team / The Hacker News / BleepingComputer / Enigma Global · 📅 2026-07-17（披露）

Okta 红队命名的 OpenSSL 内存耗尽漏洞 HollowByte 于 07-17 公开技术细节：漏洞位于 TLS 握手路径，攻击者在 ClientHello 的四字节头中声明最大 131 KB 的负载长度（仅需 11 字节请求），OpenSSL 在收到实际数据前即按声明长度分配缓冲区；连接断开后 glibc 不立即将中小块归还内核，攻击者通过随机化声明长度使堆碎片化，Resident Set Size 持续攀升且不回落。Okta 测试显示 1 GB NGINX 因 547 MB 碎片被 OOM 杀掉、16 GB 服务器损失 25% 内存，且标准连接数限制防御不触发。该漏洞于 6 月 9 日随 OpenSSL 4.0.1/3.6.3/3.5.7/3.4.6/3.0.21 静默修复，无 CVE、无公告、无变更日志，扫描器无特征可匹配，下游发行版无关键源可追踪。

Claude Desktop "PromptFiction" 漏洞（claude:// scheme 自动执行隐藏指令）+ 俄 APT 木马化 WebEx/Zoom（Starland RAT）

📰 Oasis Security / Innovate Cybersecurity / 安全客 · 📅 2026-07-20

Oasis Security 披露影响 Anthropic Claude Desktop 的 PromptFiction 漏洞，滥用应用自定义 claude:// URL scheme：点击 crafted 链接即可令 Claude Desktop 在用户无审查/无确认的情况下执行攻击者编写的指令，进而驱动 AI 代理访问敏感信息或通过已连接工具执行任务，凸显企业采用代理式 AI 工具后自定义 URL handler 的新型风险。同期，财务动机的俄罗斯威胁组织 UAT-11795 分发木马化 WebEx 与 Zoom 安装包，植入名为 Starland RAT 的后门以窃取凭据与加密货币，利用广泛使用的协作工具外观绕过用户警惕。

WordPress "wp2shell" 链在野探测持续扩大（CVE-2026-63030 / CVE-2026-60137）— 全球 5 亿+ 站点暴露窗口未闭合

📰 WordPress / Rapid7 / Wiz / Searchlight Cyber / Patchstack · 📅 2026-07-17 ~ 07-21（持续）

WordPress 核心 "wp2shell" 预认证 RCE 链自 07-17 强制推送自动更新（6.9.5 / 7.0.2 / 6.8.6）后，公开 PoC（wp2shell.py）已可验证，且 Patchstack 报告补丁落地当晚即出现活跃利用探测，07-19 至 07-21 探测持续扩大。链式利用在默认安装、无需认证/插件/交互下即可读取数据库并上传 webshell 完全接管站点，全球超 5 亿站点暴露，强制更新可能因缓存/对象缓存未启用而未真正生效。Searchlight Cyber 旗下 Assetnote 研究员 Adam Kues 发现批量路由漏洞，SQLi 部分由 TF1T、dtro、haongo 报告。

企业勒索冲击生产与供应链：Coca-Cola Fairlife 产线停产 + Nichirei 系统切断 + Ernst & Young 第三方工单系统入侵

📰 Innovate Cybersecurity / SEC 8-K / 安全客 · 📅 2026-07-20

多起运营与供应链中断事件集中披露：可口可乐公司经 SEC 8-K 文件确认其 Fairlife 乳制品子公司遭勒索攻击，生产相关系统被未授权第三方访问，美国 Fairlife 生产临时停产（IT 与 OT 均受影响）；日本冷冻食品巨头 Nichirei 于 07-13 检测入侵后切断系统，逐步恢复运营；安永（EY）通报其 IT 人员使用的第三方支持工单系统遭入侵，攻击者得以查看客户支持交互相关敏感信息。三起事件共同表明：勒索与第三方供应链已是制造业、食品与专业服务关键基础设施韧性的直接威胁。

|  |  |  |
| --- | --- | --- |
| 🔥 | 高危漏洞监测 | 2 条 |

CVE-2026-63030CVSS 9.8

**受影响产品：**WordPress 核心 6.9.0–6.9.4 与 7.0.0–7.0.1（批处理端点 /wp-json/batch/v1 于 6.9 引入），全球超 5 亿个网站（约 43% 公网 Web），含大量面向互联网的企业门户与媒体站点，默认安装即可被利用，无需插件

**漏洞描述：**CWE-436 解释冲突 + CWE-89 SQL 注入 — /batch/v1 端点解析缺陷使内部请求追踪数组错位→恶意子请求被错误调度至非预期处理器→绕过方法白名单→将用户可控输入喂入 WP\_Query 的 author\_\_not\_in 参数→该参数以字符串传入时 sanitization 被跳过、原始值直接插值进 NOT IN 子句→攻击链：特制 /wp-json/batch/v1 请求(外层[0] malformed path 触发 WP\_Error 偏移→内层 batch 嵌套)→绕过认证→author\_\_not\_in 字符串注入 SQL→盲注/时间盲注(SLEEP)读 admin 哈希→破解后登录→上传恶意插件/webshell 实现 RCE（链同伴 CVE-2026-60137 为 WP\_Query SQLi，CVSS 9.1）

**利用状态：**07-17 披露 + 07-19 公开 PoC(wp2shell.py) + Patchstack 报告 07-17 当晚起活跃利用探测(CVSS 9.8 NVD，链式视为 Critical，AV:N/AC:L/PR:N/UI:N)→默认安装无需认证/交互、暴露面巨大、PoC 已公开且在野探测持续扩大（本日连续第2天）  ·  **补丁状态：**WordPress 6.9.5 / 7.0.2 / 6.8.6 / 7.1 Beta2 修复→①立即逐站核验公网 WordPress 是否真正完成自动更新(强制推送可能未生效)②WAF 临时拦截 /wp-json/batch/v1 及 rest\_route=/batch/v1③启用持久对象缓存(无对象缓存时可达)④监控异常 POST /wp-json/batch/v1 与异常 SQL 时序(SLEEP)⑤审计 plugins/uploads 目录新增 PHP webshell⑥轮换被疑泄露的管理员凭据并启用 2FA

CVE-2026-60137CVSS 9.1

**受影响产品：**WordPress 核心 6.8.0 起至 7.0.1 的 WP\_Query 组件（含 6.8.6 修复版之前的 6.8/6.9/7.0 系列），全球所有运行上述版本的站点（6.8 仅受此 SQLi 影响、6.9+ 可借批量路由混淆升级为未认证 RCE），覆盖数亿实例

**漏洞描述：**CWE-89 SQL 注入 — WP\_Query 的 author\_\_not\_in（及同类参数）在接收字符串类型输入时 sanitization 逻辑被跳过，攻击者可注入原始 SQL 片段进入 NOT IN 子句；当与 CVE-2026-63030 的 /batch/v1 路由混淆链式组合时，匿名请求即可将可控字符串送达 WP\_Query→触发时间盲注(SLEEP)读取 wp\_users 表中管理员密码哈希→破解后登录后台→上传恶意插件/主题实现 RCE

**利用状态：**07-17 与 CVE-2026-63030 同期披露 + 07-19 随 wp2shell 链公开 PoC(CVSS 9.1 NVD / 7.5 CISA-ADP，AV:N/AC:L/PR:N/UI:N)→与 63030 组合后无需认证/交互、默认安装即可利用、PoC 已公开（本日连续第2天，在野探测持续）  ·  **补丁状态：**WordPress 6.8.6 / 6.9.5 / 7.0.2 修复→①升级至修复版本②对无法立即升级的 6.8 站点至少先打 6.8.6 阻断 SQLi③WAF 拦截含 author\_\_not\_in 异常字符串的请求④监控数据库异常查询与失败登录激增⑤审计管理员账户异常创建与提权

|  |  |  |
| --- | --- | --- |
| 📝 | 技术博客精选 | 3 条 |

Windows LegacyHive 零日机制与无补丁检测缓解：ProfSvc hive 加载滥用 + SYSTEM 服务提权痕迹取证

📰 CrowdStrike / IT-Connect / Security Affairs · 📅 2026-07-14 ~ 07-20

【可学技术 — 无 CVE 零日下的检测与缓解（①Windows User Profile Service(profsvc)以 SYSTEM 完整性运行、加载/卸载用户配置的机制如何被滥用为任意 hive 挂载原语→②标准用户如何借服务将攻击者可控 hive 挂载到自身 classes root、进而读取/篡改管理员注册表数据→③本地提权链在实战中的定位：需先有立足点、但一旦进入内网即成为可靠提权支点→④无补丁期的检测思路：监控异常 profsvc 加载非预期 hive、异常注册表持久化、以及受限 PoC 之外"原始版可加载任意 hive"的潜在利用面→⑤为何"披露即零日、无 CVE"使扫描器失效、迫使防御转向行为检测）→安全团队可借鉴此方法→对 Windows 端点强化本地提权行为监控与最小权限收敛

OpenSSL HollowByte 内存耗尽根因拆解：TLS 握手头信任声明长度 → glibc 分配器碎片 → 重启才回收

📰 Okta Red Team / Enigma Global / The Hacker News · 📅 2026-07-17

【可学技术 — 协议解析与内存安全（①TLS 握手四字节头中三字节长度字段如何被 OpenSSL 在收到实际数据前即信任、按声明值预分配 131 KB 缓冲→②连接断开后 glibc 为何不立即将中小块归还内核、攻击者的随机化长度如何使堆碎片化且无法合并→③与 Slowloris 连接耗尽的本质区别：内存碎片使标准连接数限制防御完全失效→④影响面为何极广：Apache/NGINX/Node.js/Python/Ruby/PHP/MySQL/PostgreSQL 均依赖 OpenSSL 处理 TLS→⑤为何"无 CVE 静默修复"比漏洞本身更难防：扫描器无特征、发行版无关键源）→安全团队可借鉴此方法→对互联网暴露的 TLS 服务做 OpenSSL 版本核查与进程内存监控

Hugging Face 自主 AI 代理入侵取证复盘：数据集加载器 RCE + 模板注入 + 大模型辅助日志分析闭环

📰 Hugging Face / 网易 / 安全客 · 📅 2026-07-20

【可学技术 — AI 基础设施入侵与取证（①远程代码数据集加载器(remote-code dataset loader)与模板注入(template injection)两项缺陷如何组合为数据处理管线的 RCE 原语→②攻击者如何用自主 AI 代理框架在短生命周期沙盒中高速重复执行指令、自我修正以逼近目标→③横向移动中收集云端与集群凭证的手法与暴露面→④事件响应中"商业大模型因误判拒绝协助、改用开源 GLM 5.2 数小时完成 1.7 万条恶意日志取证"的实战取舍→⑤AI 开源社区平台的令牌轮换与账户活动核查响应流程）→安全团队可借鉴此方法→将 AI 训练/推理平台的数据加载链路视为不可信输入面并强化令牌生命周期管理

|  |  |  |
| --- | --- | --- |
| 🛠 | 安全工具动态 | 3 条 |

projectdiscovery/nuclei-templates — 7月第7周（持续更新至 2026-07-21）：新增 CVE-2026-63030 / CVE-2026-60137 WordPress 检测模板 + KEV 覆盖达 1496

📰 GitHub / projectdiscovery · 📅 持续更新至 2026-07-21

ProjectDiscovery 漏洞检测模板库针对 07-19~07-21 重大披露快速更新。本期重点：①CVE-2026-63030 — WordPress /wp-json/batch/v1 路由混淆 + WP\_Query SQLi 暴露面指纹→②CVE-2026-60137 — WP\_Query author\_\_not\_in SQLi 检测→③延续 CVE-2026-15409/15410 SonicWall、CVE-2026-58644 SharePoint、CVE-2026-39808 FortiSandbox 模板。仓库 CVE 元数据于 07-20 刷新，KEV 覆盖模板达 1496 个（C...