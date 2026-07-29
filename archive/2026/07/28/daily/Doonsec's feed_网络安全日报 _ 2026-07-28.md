---
title: 网络安全日报 | 2026-07-28
url: https://mp.weixin.qq.com/s/4dtF523w5_V0MlrxWJdSMA
source: Doonsec's feed
date: 2026-07-28
fetch_date: 2026-07-29T05:01:10.686741
---

# 网络安全日报 | 2026-07-28

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/ibWuEZyvfHZFSdXptOBcdVIL2DDP13R7uXEBmdcFJFDRmnjbsTU1m2STQOSFD9v0QJfhZ1EPZY9gia8mHibRibtryiaDiaMmrQicicjcpDmpmo3EbVQ/0?wx_fmt=jpeg)

# 网络安全日报 | 2026-07-28

CyberSecurityDaily

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

🔐 网络安全日报

2026年7月28日（星期二） | 数据来源：NVD / CISA KEV / CNVD / CNNVD / Hackread / Infosecurity Magazine / Qualys / The Hacker News / 安全客 / FreeBuf

|  |  |  |  |
| --- | --- | --- | --- |
| 3 极危事件 | 4 高危事件 | 3 中危事件 | 3 关注漏洞 |

|  |  |  |
| --- | --- | --- |
| 📋 | 每日重点摘要 | 5 条 |

**🔴 极危：vBulletin 预认证 RCE CVE-2026-61511（CVSS 9.8）07-27 公开 PoC — 未认证请求直达 PHP eval() 执行任意代码，6.2.1/6.1.6 及更早受影响，6.2.2 补丁已发但未升级站点面临批量失陷**

**🔴 极危：TELESHIM 滥用 Telegram API 作 C2 定向中东政府（Zscaler 新披露）— ISO 侧加载 + MIXEDKEY/BINDCLOAK 二阶载荷，C2 域名 cert.hypersnet[.]com；Clop PTC Windchill CVE-2026-12569 定向勒索与 Chaos msaRAT 浏览器隐藏 C2 仍持续发酵**

**🟠 高危：自动化平台再爆沙箱逃逸 — n8n GHSA-gv7g-jm28-cr3m（CVSS 8.7，07-27 修复）已认证用户可执行 OS 命令；ADFS CVE-2026-56155 07-28 新入 CISA KEV（本地提权）；Citrix 53890 与 Check Point 16232 超期在野持续**

**🟠 高危：差旅凭据拦截升级 — 美/印/沙特酒店与会议中心 Wi-Fi 网关被控，AitM 劫持企业凭据自 06 月持续；可口可乐确认 Fairlife 数据泄露（Anubis 1TB）；CodeRRR LLM 钓鱼工具包驱动墨西哥 WebDAV 投毒**

**🟡 中危：紧迫倒计时到期 — SharePoint CVE-2026-50522 的 CISA ED 26-04 联邦修补与机器密钥轮换大限今日（07-28）到期；Zimbra 66376 与 WordPress wp2shell 双 CVE 超期在野仍活跃**

|  |  |  |
| --- | --- | --- |
| 🌐 | 安全热点 | 6 条 |

vBulletin 预认证 RCE CVE-2026-61511 公开 PoC — 未认证请求直达 PHP eval() 执行任意代码（新披露）

📰 BleepingComputer / The Hacker News / vBulletin · 📅 2026-07-27 ~ 07-28（新披露）

07-27 公开的 PoC 显示：vBulletin 模板引擎在处理特定请求时，未认证攻击者构造的输入可直达 PHP 的 eval() 函数，无需账户或用户交互即以 Web 进程权限执行任意代码。受影响版本为 6.2.1 与 6.1.6 及更早；补丁 6.2.2 已于 07-01 发布，但大量运营方尚未升级。尽管暂未确认野外利用、也未入 CISA KEV，CVSS 9.8 的预认证 RCE 一旦被批量扫描利用，失陷速度极快，论坛承载的用户账户与后台管理即全面暴露。

TELESHIM 借 Telegram API 作 C2 定向中东政府 — ISO 侧加载 + MIXEDKEY/BINDCLOAK 二阶载荷（新披露）

📰 Zscaler ThreatLabz / The Hacker News / 微步在线 · 📅 2026-07-28（新披露）

Zscaler ThreatLabz 披露新型 TELESHIM 后门，以中等至较高置信度归因东亚背景攻击者，针对中东政府机构。攻击链始于含合法 ASUSTek 程序的 ISO 文件，经 DLL 侧加载执行 TELESHIM——该后门滥用 Telegram Bot API 轮询指令，将 C2 流量伪装成正常 Telegram 调用以规避检测；随后投放 MIXEDKEY（借机器卷序列号派生密钥解密）与 BINDCLOAK（伪装微软加密提供程序）二阶载荷。行动集中在 07-07~07-09、UTC 04:00–12:00，锁定外交与能源领域，C2 域名 cert.hypersnet[.]com 应被阻断。

酒店与会议中心 Wi-Fi 网关被控，中间人劫持企业凭据 — 美/印/沙特持续活跃（新披露）

📰 SecurityWeek / 威胁情报 · 📅 2026-07-28（新披露）

攻击者入侵美国、印度、沙特多地酒店与会议中心的 Wi-Fi 网关，借中间人（AitM）技术拦截流量、窃取商务旅客的企业凭据，活动自 2026-06 起持续至今。共享场地（酒店、会展）的网络常被企业员工在差旅中高频使用，网关被控后可在用户无感情况下注入、劫持会话并收割 VPN/邮件/内部系统凭据。赴上述地区参会出差的人员面临主动凭据拦截风险，企业应向员工下发紧急差旅安全提示并强制隧道化访问。

可口可乐确认 Fairlife 数据泄露 — Anubis 勒索攻击后续，1TB 数据被窃（新进展）

📰 SecurityWeek / BleepingComputer · 📅 2026-07-16 ~ 07-28（新进展）

可口可乐确认其乳制品子公司 Fairlife 发生数据泄露——源自 07-16 披露的 Anubis 勒索软件攻击（当时美国 Fairlife 工厂生产一度暂停）。Anubis 团伙声称窃取 1TB 数据并于 07-20 在泄露站列出 Fairlife。此次正式泄露确认扩大了该事件的范围，成为 2026 年消费/食品行业供应链勒索的又一标志性案例，提醒制造与零售企业应将 OT/IT 融合环境下的备份隔离与勒索响应纳入常态化演练。

暴露服务器暴露 LLM 辅助钓鱼工具包 CodeRRR，驱动墨西哥 WebDAV 投毒（新披露）

📰 Rapid7 / The Hacker News · 📅 2026-07-28（新披露）

Rapid7 从一名钓鱼运营者（代号 CodeRRR）暴露的服务器中恢复了 1,048 个文件，将一套 LLM 辅助工具包与正在进行的 WebDAV 投递活动关联：该活动经伪造的墨西哥政府证件查询站点，向 Windows 用户投递 .NET 信息窃取器。面板约 5.5 天记录 77,098 次请求、来自 3,892 个独立 IP，其中墨西哥占 82.5%；README、诱饵模板与活动映射文件均带有 LLM 生成特征。这印证『AI 降低钓鱼工业化门槛』趋势——防御侧需对政府/银行仿冒域名、WebDAV 异常下载与 .NET 窃密行为做针对性检测。

n8n 修复表达式沙箱逃逸 GHSA-gv7g-jm28-cr3m（CVSS 8.7）— 已认证用户可逃逸沙箱执行 OS 命令（新披露）

📰 n8n / Security Joes / The Hacker News · 📅 2026-07-27 ~ 07-28（新披露）

n8n 披露并修复表达式沙箱逃逸漏洞 GHSA-gv7g-jm28-cr3m（CVSS 8.7）：Security Joes 在审计其 02-2026 对 CVE-2026-27577 的修复时发现新绕过——任何具备工作流创建/修改权限的已认证用户，可借构造表达式逃逸沙箱、以 n8n 进程权限执行操作系统命令。修复版本为 2.31.5 与 2.32.1，2.31.x 与 2.32.x 两条线全部旧版本均受影响。自动化平台常以较高权限运行并持有内部 API 凭据，此类沙箱逃逸对 CI/CD 与内部编排构成直接威胁。

|  |  |  |
| --- | --- | --- |
| 🔥 | 高危漏洞监测 | 3 条 |

CVE-2026-61511CVSS 9.8

**受影响产品：**vBulletin 论坛系统（版本 6.2.1 及 6.1.6 更早，全球大量部署的开源社区/企业论坛平台，承载用户账户、私密消息与后台管理，是凭据窃取与后续内网横向的高价值入口）

**漏洞描述：**CWE-94 代码注入（模板引擎 eval 滥用）— vBulletin 模板引擎在处理特定请求时，未认证攻击者构造的请求可直达 PHP 的 eval() 函数执行任意 PHP 代码，无需账户或任何用户交互。攻击链：特制 HTTP 请求触发模板解析路径 → 未净化的模板片段被传入 eval() → 以 Web 服务进程权限执行任意命令。补丁 6.2.2 已于 07-01 发布，但仍有大量运营方未完成升级，暴露面持续存在。

**利用状态：**07-27 公开概念验证 PoC 显示未认证请求即可触发 PHP eval() 实现任意代码执行；受影响版本 6.2.1 / 6.1.6 及更早。vBulletin 已于 07-01 发布 6.2.2 修复，但大量站点尚未升级，暂未确认野外利用，也未列入 CISA KEV。CVSS 9.8 的预认证 RCE 意味着一旦公开扫描批量利用开始，失陷速度将极快。  ·  **补丁状态：**升级至 vBulletin 6.2.2 及以上；升级前在网络层临时限制管理/模板接口暴露；监控异常 PHP 进程执行与 webshell 落地；对论坛服务器启用 WAF 规则拦截可疑模板解析请求；审计历史访问日志排查是否已被探测或利用。

GHSA-gv7g-jm28-cr3mCVSS 8.7

**受影响产品：**n8n 工作流自动化平台（2.31.x 与 2.32.x 全系列受影响，企业常用于编排自动化任务、调用内部 API 与凭据，常以较高进程权限运行，是自动化供应链中的高价值节点）

**漏洞描述：**CWE-265 权限/沙箱边界不当（表达式沙箱逃逸）— n8n 的表达式沙箱本应隔离不可信表达式，但 Security Joes 在审计 02-2026 对 CVE-2026-27577 的修复时发现绕过：任何具备工作流创建/修改权限的已认证用户，可借构造的表达式逃逸沙箱、以 n8n 进程权限执行操作系统命令。所有 2.31.x 与 2.32.x 旧版本均受影响。

**利用状态：**n8n 于 07-27 披露并修复 GHSA-gv7g-jm28-cr3m（CVSS 8.7），Security Joes 在审计其 02-2026 对 CVE-2026-27577 的修复时发现该绕过。修复版本为 2.31.5 与 2.32.1，2.31.x 与 2.32.x 两条线的全部旧版本均受影响。已认证用户即可触发，攻击门槛低。  ·  **补丁状态：**升级至 n8n 2.31.5 / 2.32.1 及以上；收敛工作流创建/修改权限至必要最小集合；对 n8n 运行进程启用降权与容器隔离；监控异常子进程（如 bash/sh 由 node 进程派生）；审计工作流表达式与执行历史排查越权命令执行。

CVE-2026-56155CVSS 7.5

**受影响产品：**Microsoft Active Directory Federation Services（ADFS，企业身份联合与 SSO 核心，签发票据/令牌，是通往全域身份与信任链的关键基础设施）

**漏洞描述：**CWE-1220 访问控制粒度不足（Insufficient granularity of access control）— ADFS 在授权判定中存在粒度缺陷，已授权攻击者（具备一定本地/域访问前提）可借此实现本地权限提升，进一步逼近域身份信任根。CISA 于 07-28 将其纳入 KEV，要求联邦机构按 BOD 26-04 紧急处置。

**利用状态：**CISA 于 07-28 将 CVE-2026-56155 新加入 Known Exploited Vulnerabilities 目录（due date 07-28），标注为已遭利用。与同期 ADFS/SharePoint/SonicWall/FortiSandbox 一批 7 月 KEV 同为身份与边缘基础设施高危信号，需优先处置暴露或高信任的联合服务器并在重建前保留认证/审计证据。  ·  **补丁状态：**应用微软 07 月安全更新修复 ADFS 访问控制粒度缺陷；将 ADFS 服务器置于仅允许可信管理访问的网络之后；在重建/处置前保留 ADFS 审计事件与令牌签发日志；审查异常令牌签发与声明活动；对面向互联网的联合端点启用严格 MFA 与持续验证。

|  |  |  |
| --- | --- | --- |
| 📝 | 技术博客精选 | 3 条 |

TELESHIM 滥用 Telegram API 作 C2 的流量伪装与检测（Zscaler ThreatLabz）：ISO 侧加载 + Bot 轮询 + MIXEDKEY/BINDCLOAK 二阶解密

📰 Zscaler ThreatLabz / 微步在线 · 📅 2026-07-28

【可学技术 — 合法 SaaS API 滥用型 C2 的检测（①为何用 Telegram Bot API 作 C2：将指令轮询伪装成正常 Telegram 调用，传统基于 IP/域名的 IOC 几乎失效、且可穿越多数出口防火墙→②ISO 侧加载初始载体如何借助合法 ASUSTek 程序加载恶意 DLL，并配套磁盘写入/虚拟机检测逃避沙箱→③MIXEDKEY 如何用机器卷序列号派生密钥解密最终载荷、BINDCLOAK 如何伪装微软加密提供程序文件隐藏自身→④防御检测点：异常 DLL 侧加载、服务器上的 Telegram API 调用、高频计划任务与 C2 域名 cert.hypersnet[.]com 阻断）→安全团队可借鉴→对政府/能源行业部署 Telegram API 出向审计、侧加载行为 EDR 告警与 IoC 阻断

SonicWall SMA1000 CVE-2026-15409/15410 漏洞链深度解析（cnblogs）：从未认证 SSRF 到 Root RCE 的完整攻击路径

📰 cnblogs / 安全研究 · 📅 2026-07-28

【可学技术 — 边界设备 SSRF→RCE 链路构造（①CVE-2026-15409 未认证 SSRF 位于 /wsproxy 端点，host 参数缺乏内网地址校验，bmID=-3389 前缀触发缺校验分支，借 WebSocket 隧道访问仅 localhost 可达的内部服务→②硬编码 Erlang RPC Cookie 如何让隧道无需认证即与内部应用交互、经 CouchDB 默认凭证获低权限文件读写→③CVE-2026-15410 remove\_hotfix 路径穿越代码注入：将热修复参数构造为 ../../../../tmp/stage.sh 写入恶意脚本，ctrl-service 以 root 执行→④权限演进：无→网络访问→couchdb 账户→root RCE）→安全团队可借鉴→对暴露的 VPN/安全设备收敛管理接口、审计内部服务调用、升级至修复固件 12.4.3-03453 / 12.5.0-02835 及以上

银狐样本深度逆向（kafan）：无文件落地 + PoolParty 注入 + BYOVD 致盲 EDR 的多层规避架构

📰 kafan / 瞬犀安全 · 📅 2026-07-24 ~ 07-28（持续跟踪）

【可学技术 — 终端防御致盲与无文件对抗（①IOCP 线程池注入 PoolParty 变种 7 结合句柄劫持，将恶意行为打散到正常系统线程池，破坏基于行为链的 XDR/EDR 关联→②NTDLL 代码段替换（Unhooking）绕过用户态 API 挂钩 + 加载漏洞驱动（BYOVD）从内核态削弱安全软件，实现双向 EDR 致盲→③双重压缩加密 Shellcode 多级反射式注入 + 白进程 DLL 侧加载 + COM 劫持实现高隐蔽持久化→④libwebsockets 多协议加密 C2 与内存中线程执行，全程无文件落地）→安全团队可借鉴→启用基于虚拟化的安全（VBS/HVCI）抵御 BYOVD、对合法签名进程异常子进程与内存写入做行为告警、强化驱动加载白名单

|  |  |  |
| --- | --- | --- |
| 🛠 | 安全工具动态 | 3 条 |

projectdiscovery/nuclei-templates — 7月第14周（更新至 2026-07-28）：新增 CVE-2026-61511（vBulletin）/ CVE-2026-56155（ADFS KEV）/ GHSA-gv7g-jm28-cr3m（n8n）检测

📰 GitHub / projectdiscovery · 📅 持续更新至 2026-07-28

ProjectDiscovery 漏洞检测模板库针对本期新鲜高危项快速更新。本期重点：①CVE-2026-61511 — vBulletin 模板引擎 eval 预认证 RCE 暴露面与 webshell 落地检测→②CVE-2026-56155 — ADFS 访问控制粒度缺陷（07-28 新入 KEV）暴露面检测→③GHSA-gv7g-jm28-cr3m — n8n 表达式沙箱逃逸暴露面检测。用途：安全团队立即扫描公网 vBulletin 资产、企业 ADFS 联合服务器与 n8n 自动化平台。`nuclei -tags kev` 可优先扫在野利用漏洞。

nomi-sec/PoC-in-GitHub — 7月更新（持续至 2026-07-28）：汇总 CVE-2026-61511（vBulletin）/ GHSA-gv7g-jm28-cr3m（n8n）/ CVE-2026-56155（ADFS）最新公开 PoC

📰 GitHub / nomi-sec · 📅 持续更新至 2026-07-28

社区维护的 PoC 与公开 exploit 合集，按周更新。本期纳入：①CVE-2026-61511 — vBulletin 预认证 RCE 公开 PoC（07-27）②GHSA-gv7g-jm28-cr3m — n8n 沙箱逃逸相关利用③CVE-2026-56155 — ADFS 提权（07-...