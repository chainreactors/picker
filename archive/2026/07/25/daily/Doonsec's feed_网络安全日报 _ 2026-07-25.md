---
title: 网络安全日报 | 2026-07-25
url: https://mp.weixin.qq.com/s/ErTM-c2skslTOM7Jol0eIQ
source: Doonsec's feed
date: 2026-07-25
fetch_date: 2026-07-26T05:22:45.267632
---

# 网络安全日报 | 2026-07-25

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/ibWuEZyvfHZFycHs7NyfgxySoPKxLAefFm5pLHA6j6FTBibXlFxWjjZygQfvyTnPqBRwVCmia8otSeaFjBhsKiavE7yoC5kf3Ax8jYjFVnnA5QU/0?wx_fmt=jpeg)

# 网络安全日报 | 2026-07-25

CyberSecurityDaily

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

🔐 网络安全日报

2026年7月25日（星期六） | 数据来源：NVD / CISA KEV / CNVD / CNNVD / Hackread / Infosecurity Magazine / Qualys / The Hacker News / 安全客 / FreeBuf

|  |  |  |  |
| --- | --- | --- | --- |
| 3 极危事件 | 4 高危事件 | 2 中危事件 | 8 关注漏洞 |

|  |  |  |
| --- | --- | --- |
| 📋 | 每日重点摘要 | 5 条 |

**🔴 极危：微软 07-24 单日批披露 8 个云/在线服务高危漏洞，含 3 个 CVSS 10.0（Azure DNS CVE-2026-58275 / Azure Key Vault CVE-2026-62825 / Exchange Online CVE-2026-56191）未认证提权与数据篡改，威胁情报标注 exploit 已可用**

**🔴 极危：俄罗斯 APT Laundry Bear（Void Blizzard）利用 Zimbra 零点击 XSS CVE-2025-66376 窃邮件+绕过 2FA，CISA/NSA/FBI 07-22 联合预警，自 2025-07 已攻陷 10+ 组织**

**🔴 极危：Chaos 勒索 msaRAT 借 Chrome/Edge headless CDP + WebRTC 隐藏 C2（Cisco Talos 07-23），RAT 进程零直连、流量伪装成浏览器访问 Cloudflare/Twilio**

**🟠 高危：Claude Cowork SharedRoot 沙箱逃逸 CVE-2026-46331（约 50 万 macOS 用户）+ macOS Gatekeeper 绕过（已验证 App 静默替换，Apple 不修）+ Origin Energy 200 万客户数据泄露 — AI 平台边界与终端信任双重告急**

**🟡 中危：持续风险 — Check Point 16232 CISA KEV 联邦修补截止今日(07-25) + Citrix 53890 未认证 RCE 持续在野超期 + SharePoint 50522 ED 26-04 截止临近(07-28) + wp2shell 双 CVE 持续利用**

|  |  |  |
| --- | --- | --- |
| 🌐 | 安全热点 | 6 条 |

微软 07-24 单日批披露 8 个云/在线服务高危漏洞，含 3 个 CVSS 10.0（Azure DNS / Azure Key Vault / Exchange Online）未认证提权与数据篡改

📰 Microsoft MSRC / NVD / enigma-global 日情报 · 📅 2026-07-24

微软于 07-24 在 MSRC 单日批披露 8 个影响云与在线服务的高危漏洞，其中三个达到 CVSS 10.0 满分：Azure DNS 缺失授权 CVE-2026-58275、Azure Key Vault 不当认证 CVE-2026-62825、Exchange Online 不当认证 CVE-2026-56191——均为未认证经网络提权/篡改。另含 M365 Copilot 反序列化 RCE CVE-2026-50517（9.9）、Microsoft Account 堆溢出 CVE-2026-56165（9.8）、Surface 输入验证 RCE CVE-2026-54120（9.9）、Azure Red Hat OpenShift 不当授权 CVE-2026-56160（9.1）、Azure AI Search SSRF CVE-2026-56167（8.5）。威胁情报源标注三个 10.0 项『Exploit is confirmed available』，鉴于无认证+网络可达，应假定野外利用迫近或已发生。多数属云端服务，微软大概率已服务端缓解，租户须主动核查与轮换。

俄罗斯 APT Laundry Bear（Void Blizzard）利用 Zimbra 零点击 XSS CVE-2025-66376 窃邮件+绕过 2FA — CISA/NSA/FBI 07-22 联合预警

📰 CISA / NSA / FBI / Media Defense / BleepingComputer · 📅 2026-07-22 ~ 07-25（持续）

CISA、NSA、FBI 及多国伙伴于 07-22 发布联合网络 advisory，警告俄罗斯国家支持 APT 组织 Laundry Bear（微软追踪为 Void Blizzard）正利用 Zimbra Collaboration Suite 的零点击 XSS 漏洞 CVE-2025-66376（CWE-79，Classic UI 中 CSS @import 指令净化不当）实施钓鱼窃密。受害者仅需在企业 ZCS Web 邮件中查看恶意邮件，内嵌 JavaScript 即自动执行，通过名为 Ulej 的聚合外泄能力自动收集并回传最近 90 天邮件、邮箱地址、密码、GAL 与 2FA 令牌，并生成新的 Zimbra 应用密码（app passcode）以绕过 MFA 持久访问。自 2025 年 7 月已成功攻陷 10+ 组织（国防工业基地、政府、执法、能源、媒体等），数据经 DNS A 记录与 HTTPS 外传至 Flowerbed 框架。CVE-2025-66376 已于 2025-11 修复、2026-03 入 CISA KEV。

Chaos 勒索 msaRAT 借 Chrome/Edge headless CDP + WebRTC 隐藏 C2 — Cisco Talos 07-23 披露『Living off the Browser』

📰 Cisco Talos / Help Net Security / The Hacker News · 📅 2026-07-23

Cisco Talos 于 07-23 披露归属于 Chaos 勒索团伙（RaaS，2025-02 起活跃）的新型 Rust RAT——msaRAT。其最大特点是『绝不直连网络』：RAT 进程仅绑定 127.0.0.1，通过启动 Chrome/Edge 无头实例并经 Chrome DevTools Protocol（CDP）驱动浏览器，借 WebRTC DataChannel + Twilio TURN 中继建立 C2——网络侧看到的仅是浏览器访问 Cloudflare Workers、Google STUN 与 Twilio 中继，攻击者真实服务器地址从不出现在流量中，双层加密（DTLS + ChaCha-Poly1305）令检测极为困难。投递为伪装成 Windows 更新的 update\_ms.msi（curl 经 443 明文 HTTP 下载→自定义动作将 lib.dll 载入内存）。检测要点：告警由安装包/服务/非交互父进程启动、带 --headless=new 与 --remote-debugging-port 的浏览器，以及无可见窗口的 WebRTC 会话。Talos 已发布 ClamAV 签名。

Claude Cowork SharedRoot 沙箱逃逸 CVE-2026-46331（Accomplish AI，约 50 万 macOS 用户）— 宿主机全盘 R/W 挂载 + pedit COW 提权

📰 Accomplish AI / The Hacker News / FreeBuf · 📅 2026-07-23

Accomplish AI 于 07-23 披露 Claude Cowork 本地会话沙箱逃逸链 SharedRoot：Agent 在 macOS 应用内以登录用户运行，实际工作在 Apple Virtualization 的 Linux VM 中，但根守护进程 coworkd 将整个宿主机文件系统（/）以读写方式挂载进 VM 的 /mnt/.virtiofs-root（仅 guest-root 可见）。攻击链：创建用户/网络命名空间获得 CAP\_NET\_ADMIN→加载 guest 内核 net/sched 的 act\_pedit 子系统并触发 CVE-2026-46331（pedit COW，内存破坏）获取 guest-root→经全盘 virtiofs 挂载读写 Mac 文件（SSH 密钥、云凭据、主目录），无需任何权限弹窗。影响约 50 万本地会话用户。Anthropic 以『Informative』结案、未发补丁，仅将 Cowork 默认改为云端执行；仍运行本地会话的用户依旧暴露。研究者指出 net/sched 子系统持续产生同类提权，修补单一漏洞会立即被下一个重启用。

macOS Gatekeeper 被曝绕过：已验证 App 可静默替换为恶意副本，Apple 认定不构成漏洞不予修复

📰 The Register / Mysk / FreeBuf · 📅 2026-07-24

安全研究者 Talal Haj Bakry 与 Tommy Mysk 披露 macOS Gatekeeper 信任缓存缺陷：从网页下载、已运行过一次（通过初始验证被标记为『可信』）的应用，可用 tar 归档→删除原程序→原地解压恶意版本的方式被静默替换，macOS 不会重新授权——系统将恢复的应用视为『本地构建』而跳过验证。攻击需先获得当前用户级代码执行（恶意脚本、npm/Homebrew 供应链、AI Agent 提示注入等），不影响 Mac App Store 应用（归 root 所有）。一旦恶意『双胞胎』就位，可在熟悉应用名称/图标下弹出更具欺骗性的权限请求。Apple 于 07-14 关闭该案件，结论是『不构成安全漏洞』、超出 Gatekeeper 设计范围（仅在首次启动时验证、不持续监控用户自有文件），不予修复。研究者建议用户审批敏感权限时保持警惕，并指权限弹窗应显示可执行文件的代码签名身份/TeamID。

澳大利亚能源巨头 Origin Energy 确认 200 万客户数据遭未授权访问与披露 — 攻击者开启 14 天勒索倒计时

📰 Xinhua / SMH / 7NEWS / Origin Energy · 📅 2026-07-22 ~ 07-24（持续）

澳大利亚最大电力零售商 Origin Energy（服务 480 万客户）于 07-22 承认调查潜在安全事件，疑似黑客声称窃取约 200 万客户数据；《澳大利亚人报》收到含姓名、地址、邮箱、生日、账单历史的 50 条样本。07-23 公司经 ASX 确认发生『未授权访问与披露』，影响数据含姓名、地址、出生日期、联系电话及信用卡后四位或银行账号后三位（公司先称不含完整卡/银行信息，后修正为含部分）。自称『John Doe』的攻击者通过 7NEWS 爆料线索要 14 天内联系『解决此事』，否则公开全部数据，并附倒计时时钟，构成典型勒索/数据泄露敲诈。公司未收到赎金要求、已通报 ACSC 与 AFP，CEO 致歉。该事件凸显关键能源基础设施客户数据的大规模暴露风险。

|  |  |  |
| --- | --- | --- |
| 🔥 | 高危漏洞监测 | 8 条 |

CVE-2026-58275CVSS 10.0

**受影响产品：**Microsoft Azure DNS（Azure 平台域名解析服务，为无数云部署提供名称解析，是企业云环境的服务发现、流量路由与资源管理核心基础组件；一旦被控可篡改 DNS 记录、重定向流量、接管 Azure 资源）

**漏洞描述：**CWE-862 缺失授权（Missing Authorization）— Azure DNS 在处理特定网络请求时缺少授权校验，未认证远程攻击者（CVSS:3.1/AV:N/AC:L/PR:N/UI:N，网络可达、复杂度低、无需权限与用户交互）可直接越权执行通常仅特权用户可进行的操作，实现权限提升。由于 Azure DNS 承载企业云环境的域名解析与流量路由，攻击者成功利用即可操纵 DNS 记录、将流量重定向至恶意基础设施或获取 Azure 资源控制权，进而波及下游依赖解析的服务。

**利用状态：**07-24 微软 MSRC 单日批披露（与 Azure Key Vault / Exchange Online 等同期），CVSS 10.0 满分、未认证网络可达；威胁情报源（enigma-global 日情报告）标注『Exploit is confirmed available』，社媒已有活跃讨论与武器化迹象——鉴于满分评分 + 无认证 + 网络可达，野外利用迫在眉睫或已经发生。Azure 为云端托管服务，微软可能已部署服务端缓解。  ·  **补丁状态：**Azure DNS 为云端托管服务，微软侧大概率已推送服务端修复；租户侧应立即：①核查 Azure DNS 配置（记录集、委派、解析策略）是否有未授权变更②启用 Azure Monitor / Defender for DNS 审计与告警，监控异常记录修改与解析偏离③对关键域名启用 DNSSEC 与解析监控④以最小权限收拢对 DNS 区域的管理访问⑤对依赖 Azure DNS 的关键业务做解析冗余与可用性预案。

CVE-2026-62825CVSS 10.0

**受影响产品：**Microsoft Azure Key Vault（Azure 密钥保管库，集中存储企业云应用的加密密钥、机密 secrets 与证书，是云安全架构的信任根；一旦被攻破将暴露组织在整个 Azure 租户内部署的全部密钥与机密）

**漏洞描述：**CWE-287 不当认证（Improper Authentication）— Azure Key Vault 的认证机制存在缺陷，未能正确校验访问者身份或可被诱骗将未认证请求当作合法且特权化的请求接受（可能源于认证处理器的逻辑错误、特定 API 端点的绕过或错误配置导致的身份伪造），使未认证远程攻击者（CVSS:3.1/AV:N/AC:L/PR:N/UI:N）能够越权提升权限。由于 Key Vault 保管着密钥、机密与证书，该绕过直击云安全架构核心，影响范围跨整个 Azure 部署。

**利用状态：**07-24 微软 MSRC 单日批披露，CVSS 10.0 满分、未认证网络可达；威胁情报标注『Exploit is confirmed available』。无认证要求 + 网络可达 + Key Vault 内容高价值，使其成为极具吸引力的目标，应假定已遭活跃利用。Azure 为云端托管服务，微软可能已服务端缓解。  ·  **补丁状态：**Azure Key Vault 为云端服务，微软侧大概率已推送服务端修复；租户侧应立即：①轮换 Key Vault 中存储的全部密钥、机密与证书（假定可能被暴露）②审查访问策略 access policies / RBAC 与日志，核查异常访问③启用 Key Vault 诊断日志与 Defender for Key Vault 告警④对高敏感机密启用软删除 + 清除保护⑤以私有端点网络隔离与最小权限收敛暴露面。

CVE-2026-56191CVSS 10.0

**受影响产品：**Microsoft Exchange Online（微软托管的企业邮件、日历与协作服务，承载全球海量企业组织的邮件通信与敏感信息，是商业通信机密性与完整性的核心）

**漏洞描述：**CWE-287 不当认证（Improper Authentication）— Exchange Online 存在认证缺陷，使未认证远程攻击者（CVSS:3.1/AV:N/AC:L/PR:N/UI:N）能够越权执行数据篡改（tampering）。攻击者可借此操纵邮件内容、拦截消息或未经授权访问邮箱数据，对企业通信的机密性与完整性造成严重冲击，且无需合法凭据即可触发。

**利用状态：**07-24 微软 MSRC 单日批披露，CVSS 10.0 满分、未认证网络可达；威胁情报标注『Exploit is confirmed available』。Exchange Online 在企业环境无处不在，成为间谍活动与金融动机团伙的共同高优先级目标，应假定已遭活跃利用。Exchange Online 为云端服务，微软可能已服务端缓解。  ·  **补丁状态：**Exchange Online 为云端服务，微软侧大概率已推送服务端修复；租户侧应立即：①监控异常 Exchange 活动（异常邮件规则、转发、登录与邮件访问）②审查邮件流规则 mail flow rules 与邮箱权限③启用统一审计日志与告警④对敏感操作启用条件访问与防钓鱼 MFA⑤定期对特权邮箱与合规检索做异常狩猎。

CVE-2026-56167CVSS 8.5

**受影响产品：**Microsoft Azure AI Search（Azure 认知搜索 / AI 搜索服务，为 RAG、向量检索与企业知识库提供索引与查询能力，常接入内部文档、数据库与敏感数据源）

**漏洞描述：**CWE-918 服务端请求伪造（SSRF）— Azure AI Search 存在 SSRF 漏洞，已授权攻击者（CVSS:3.1/AV:N/AC:L/PR:L/UI:N）可诱导服务端发起非预期的内部请求，从而越权提升权限。由于搜索服务常连接内部数据源与元数据端点，SSRF 可被用于访问云元数据（如 IMDS）、内部管理接口或横向触达内网资源。

**利用状态：**07-24 微软 MSRC 单日批披露，CVSS 8.5（High），已授权攻击者经网络提升权限。需已授权上下文，武器化门槛高于未认证项，但 Azure AI Search 在 RAG / 企业知识库场景广泛部署，内部数据暴露风险显著。  ·  **补丁状态：**Azure AI Search 为云端服务，微软侧大概率已推送服务端修复；租户侧应：①审查搜索服务的数据源连接与网络配置，禁用不必要的公网访问②以私有端点收敛访问面③对 IMDS / 内部元数据做网络隔离④监控异常出站请求与索引器数据源变更⑤最小权限配置索引器凭据。

CVE-2026-56165CVSS 9.8

**受影响产品：*...