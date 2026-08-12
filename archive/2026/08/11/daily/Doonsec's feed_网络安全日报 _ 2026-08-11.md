---
title: 网络安全日报 | 2026-08-11
url: https://mp.weixin.qq.com/s/nb-PoJwCvzQc3NtIOGfCzQ
source: Doonsec's feed
date: 2026-08-11
fetch_date: 2026-08-12T04:00:04.689618
---

# 网络安全日报 | 2026-08-11

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/ibWuEZyvfHZGHWBpHS4EVUrWpwwMJQH1KFeJN5HgHQU0ib3jDMXkWqtW0MNxO4EPx4Xn3TX9SMLuICahpKI0IntGTtYamPuKB1qlVTXIgzpEc/0?wx_fmt=jpeg)

# 网络安全日报 | 2026-08-11

CyberSecurityDaily

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

🔐 网络安全日报

2026年8月11日（星期二） | 数据来源：CISA KEV / NVD / CVE.org / The Hacker News / Wiz / VulnCheck / Tenable / watchTowr / CISA / MS-ISAC / 国家计算机病毒应急处理中心 / SentinelOne / GitHub Advisory / Vulhub / 安全客

|  |  |  |  |
| --- | --- | --- | --- |
| 2 极危事件 | 2 高危事件 | 1 中危事件 | 4 关注漏洞 |

|  |  |  |
| --- | --- | --- |
| 🌐 | 安全热点 | 5 条 |

Metabase SQL 注入 0-day 致 Framework / Tally / n8n / Kilo Code 数据泄露（新进展 / 极危）

📰 The Hacker News / Wiz / BleepingComputer / Metabase 安全公告 / yijinglab · 📅 2026-08-06（披露）~ 08-10（公开 PoC）

Metabase 于 08-06 披露一处已被当作 0-day 利用的临界 SQL 注入漏洞（GHSA-vwf4-m7j8-wcjf，CVSS 10.0，暂未分配 CVE），影响 0.58.0–0.63.4 / 1.58.0–1.63.4 版本，修复版本为 0.58.24 / 0.59.21 / 0.60.17 / 0.61.11 / 0.62.9 / 0.63.5。漏洞位于本就无需认证的密码重置端点 POST /api/session/reset\_password：攻击者对请求中可控输入拼接进应用数据库查询而未参数化，注入 SQL 后操纵会话/凭据状态取得实例管理员权限，进而变更配置、窃取所连数据库存储凭据、读取并导出任意可达数据。Metabase Cloud 自 08-03 遭入侵，Framework（笔记本厂商）与 Tally（表单服务）于 08-07 确认客户 PII（姓名、邮箱、电话、账单地址等）泄露，n8n（08-08）、Kilo Code / Anaconda（08-09）相继确认客户记录未授权访问。Wiz 观测到约 13% 云环境部署自托管 Metabase、其中 25% 直连互联网，Shodan 可见约 2,500 个实例；截至 08-10 中午 UTC 已有公开 PoC 开源。云客户已由厂商自动升级，自托管实例须手动升级、轮换数据库凭据、撤销会话并审查日志。

国家病毒中心预警「Sorry」勒索借 cPanel CVE-2026-41940 攻击 Linux 服务器（新预警 / 极危）

📰 国家计算机病毒应急处理中心 / 央视新闻 / CISA / MS-ISAC / watchTowr · 📅 2026-08-10（预警）~ 持续利用

国家计算机病毒应急处理中心联合计算机病毒防治技术国家工程实验室于 08-10 发布「Sorry」勒索病毒预警，称境内发现多起用户遭攻击事件。该 2026 年新出现的 GO 语言勒索家族针对暴露公网的 Linux Web 服务器，攻击者首先利用 WebPros cPanel 授权问题漏洞（CNNVD-202604-5641、CVE-2026-41940）取得服务器最高管理权限，静默投放并运行病毒、伪装为常见 sshd 进程；随后生成含用户名/主机名/CPU/网络接口的唯一受害标识回传、终止数据库/安全/备份服务、批量窃取业务数据、以 AES 加密文件并加 .sorry 后缀、再用 RSA 加密 AES 密钥，并扫描 22/2222/22222 等 SSH 端口借弱口令向内网横向传播。CVE-2026-41940 是 cPanel/WHM cpsrvd 预认证会话逻辑的认证绕过（CWE-306，Authorization 头 CRLF 注入→会话文件注入 user=root→无需密码取得 root 管理权），watchTowr 已发布完整 PoC；MS-ISAC 指出该漏洞已列入 CISA KEV、自 02-23 即被利用，Shadowserver 监测到 44,000 个 IP 关联主动扫描与利用。国内主流 Linux 发行版含信创系统均受影响，无解密密钥暂无可靠恢复手段。

Zbtlink 路由器出厂预置后门 ENDLESSDOORS（CVE-2026-66747，CVSS 9.3）（新披露 / 高危）

📰 VulnCheck / SentinelOne / The Hacker News / Shield53 · 📅 2026-08-05（VulnCheck）~ 08-10（广泛披露）

VulnCheck 于 08-05 披露，至少 21 款 Zbtlink 路由器固件自出厂起内置一个名为 ENDLESSDOORS 的持久远程控置植入（CVE-2026-66747，CVSS 9.3 v4 / 9.8 v3，CWE-506 嵌入式恶意代码）。该植入源自开源工具 ycsunjane/rctl，以 OpenWrt 包 librctl.so 编译进固件，开机以 root 启动并伪装为内核线程 kworker；不监听端口，而是每约 35 秒经明文 TCP 向硬编码 C2（命令通道 7000、交互式 root shell 回调 7001）信标，无任何认证与传输加密，命令处理器将收到的任意字符串直接交给 popen() 以 uid=0 执行，保留字 rctlbash 可返回交互式 root shell。因通道无认证且无加密，任何能接管 C2 地址、占据网络路径（DNS/路由劫持）或抢注失效备用域名者均可取得未授权 root RCE。涉及 Zbtlink / ZBT / Wiflyer / ZBTWiFi 等品牌、全球 10 万+ 设备在网，经白标渠道流入市场。厂商已于 07-31 前悄然下架受影响固件并承诺修补；鉴于「出厂即预置后门」的性质，处置以隔离与更换受信固件/硬件为主，而非普通打补丁。

Dokploy 部署平台命令注入集群集中披露（CVE-2026-72872 等，CVSS 9.9）（新预警 / 高危）

📰 Tenable / NVD / Vulhub · 📅 2026-08-10（集中披露）

开源自托管部署/PaaS 平台 Dokploy 于 08-10 被集中披露一组 CVSS 9.9 的 OS 命令注入漏洞（CVE-2026-72872 / 72869 / 72868 / 72865 / 72864），覆盖 git clone 的 Bitbucket owner/repository 参数、backup.restoreBackupWithLogs、destination.testConnection 的 rclone 注入、compose 路径、以及 docker-container-terminal WebSocket 越权等多个功能。以 CVE-2026-72872 为例，攻击者可在 git clone 时借可控仓库参数注入命令、在部署主机执行任意命令；CVE-2026-72868 更可由 Member 角色经 rclone shell 注入升级至主机 root。这类漏洞使暴露在公网的 Dokploy 管理面板面临「接管部署服务器→横向至所托管业务」的主机级失陷风险，与本期「互联网暴露管理平面」主线高度一致。建议升级至官方最新版本、在补丁可用前限制管理面板仅 VPN/受信任网段可达、并最小化 Member 等角色权限。

消费级 IoT 与运维工具命令注入集中披露：Xiaomi 音箱 xiaoai-patch、crontab-ui 等（新披露 / 中危）

📰 Tenable / NVD · 📅 2026-08-10（集中披露）

Tenable 于 08-10 集中披露一批 OS 命令注入类漏洞，除 Dokploy 集群外，还包括面向消费设备的 Xiaomi 智能音箱补丁项目 duhow/xiaoai-patch（CVE-2026-72580，/mute、/unmute 端点将用户可控 silent 参数直接传入系统命令，Critical）以及 alseambusher/crontab-ui 任务调度面板（CVE-2026-72589 经 /crontab 的 env\_vars 参数 URL 编码换行注入、CVE-2026-72590 经 /import 导入特制 .db 文件覆盖数据库，均为 Critical）。这类漏洞的共同点是用户输入未经净化即抵达 OS 命令或数据库导入路径，未认证或低权限即可在受影响设备上执行任意命令。消费 IoT 与小微运维工具常默认暴露管理接口、且固件/版本更新滞后，是家庭与小企业网络的隐性攻击面，须及时升级并将管理接口隔离于不可信网络。

|  |  |  |
| --- | --- | --- |
| 🔥 | 高危漏洞监测 | 4 条 |

CVE-2026-41940CVSS 10.0

**受影响产品：**cPanel & WHM（所有受支持版本，修复版本 11.86.0.41 / 11.110.0.97 / 11.118.0.63 / 11.126.0.54 / 11.130.0.19 / 11.132.0.29 / 11.134.0.20 / 11.136.0.5）及 WP Squared（< 136.1.7）。cPanel 是全球主流 Linux 虚拟主机/服务器管理面板，估计全球约 150–200 万实例暴露，是 Web 托管与 MSP 的核心管理平面，常直连互联网。

**漏洞描述：**CWE-306 缺失认证 + CWE-93 CRLF 注入——cpsrvd 服务的预认证会话逻辑对 Authorization 头输入净化不足，攻击者发送含编码 CRLF 的特制请求，将 user=root 等属性注入磁盘临时会话文件，再触发会话重载使系统接受注入值，无需密码即取得完整 root 管理权限。攻击链为『未认证远程攻击者 → 向 cpsrvd 发送含 CRLF 注入的 Authorization 头 → 注入 user=root 至会话文件 → 触发会话重载 → 以 root 接管 WHM/cPanel → 经合法 WHM 功能实现主机级 RCE』。watchTowr 已发布完整 PoC，仅需少量 HTTP 请求、无需有效凭据。

**利用状态：**已在野利用，被「Sorry」勒索软件团伙及 Mr Rot13 等用于入侵 Linux Web 服务器并投放 GO 语言勒索病毒（.sorry 后缀）；Shadowserver 监测到 44,000 个 IP 关联主动扫描与利用活动。已列入 CISA KEV（MS-ISAC/CIS 确认）。CVE 本身由 cPanel 于 2026-04-28 紧急修补，但利用自 2026-02-23 即已开始，公开披露后利用激增。  ·  **补丁状态：**cPanel 已于 2026-04-28 发布紧急补丁（各分支修复版本见上）；①立即升级至对应分支修复版本②无法立即升级则限制 2082/2083/2086/2087/2095/2096 端口仅受信任 IP/VPN 访问，或停用 cpsrvd、cpdavd 服务③升级后轮换 root 密码、API token、SSL 私钥、SSH 密钥、数据库密码等全部凭据④监控 /api/session 异常与新增管理员账户

CVE-2026-72872CVSS 9.9

**受影响产品：**Dokploy（开源自托管部署/PaaS 平台）经 Bitbucket owner/repository 参数的 git clone 路径；Dokploy 广泛用于自托管应用部署，管理面板常暴露，托管业务直接运行于其上。

**漏洞描述：**CWE-78 OS 命令注入——在通过 Bitbucket owner/repository 参数执行 git clone 时，用户可控的仓库参数未经净化即传入系统命令，攻击者可注入恶意命令，在部署主机上以高权限执行任意命令。攻击链为『攻击者（经暴露的部署接口）→ 构造恶意 Bitbucket owner/repository 参数 → git clone 路径命令注入 → 主机命令执行 → 控制部署服务器』。与同期披露的 Dokploy 命令注入集群（CVE-2026-72869/72868/72865/72864，均 9.9）同源。

**利用状态：**2026-08-10 披露（Tenable / NVD / Vulhub），CVSS 9.9（AV:N/AC:L/PR:N/UI:N 类高危利用条件）；暂未列入 CISA KEV，但同类高危需立即处置。公开披露后暴露实例面临主机级失陷风险。  ·  **补丁状态：**升级至官方最新发布版本；①在补丁可用前限制 Dokploy 管理面板暴露（仅 VPN/受信任网段）②禁用或严格审计 git clone/restore/testConnection 等高危操作③监控异常命令执行与外出连接

CVE-2026-72869CVSS 9.9

**受影响产品：**Dokploy 经 backup.restoreBackupWithLogs 的 databaseName 参数的已认证 OS 命令注入；Dokploy 部署主机直接承载所托管业务，失陷即主机 root。

**漏洞描述：**CWE-78 OS 命令注入——backup.restoreBackupWithLogs 在处理 databaseName 参数时未净化用户输入，已认证攻击者可注入命令，在部署主机上以高权限执行任意命令并导致主机级 RCE。攻击链为『已认证攻击者 → 调用 restoreBackupWithLogs 并构造恶意 databaseName → 命令注入 → 部署主机任意命令执行』。属 Dokploy 08-10 集中披露的命令注入集群之一。

**利用状态：**2026-08-10 披露（Tenable / NVD / Vulhub），CVSS 9.9；需认证但利用门槛低，与同批集群共享根因（用户输入抵达 OS 命令）。  ·  **补丁状态：**升级至官方最新版本；①在补丁可用前限制管理面板暴露②严格审计备份恢复类高危操作③监控异常命令执行与外出连接

CVE-2026-72868CVSS 9.9

**受影响产品：**Dokploy 经 destination.testConnection 的 rclone shell 注入；可由 Member 角色升级至部署主机 root（CVE-2026-72864 同为该平台 WebSocket 越权，Member→任意容器 root）。

**漏洞描述：**CWE-78 OS 命令注入——Member 角色用户经 destination.testConnection 功能传入的 rclone 相关参数未净化，触发 shell 注入，可借 Member 权限升级至部署主机 root。与 CVE-2026-72872 等同批 Dokploy 命令注入集群，反映平台多个功能共享「用户输入直接抵达 shell」的根因。

**利用状态：**2026-08-10 披露（Tenable / NVD / Vulhub），CVSS 9.9；Member 角色即可触发、无需管理员权限，利用门槛低，暴露实例风险高。  ·  **补丁状态：**升级至官方最新版本；①最小化 Dokploy 角色权限（Member 不应具备主机级操作）②限制管理面板暴露③监控 rclone/shell 异常调用

|  |  |  |
| --- | --- | --- |
| 📝 | 技术博客精选 | 3 条 |

Metabase SQLi 逆向实战：用 AI 加速漏洞定位与防御（Wiz）

📰 Wiz Research · 📅 2026-08-10

【可学技术 — 用 AI 加速漏洞逆向与防御（①补丁比对手法：下载受影响 v0.58.22 与修复 v0.58.24 的 JAR，反编译 Clojure 相关类、对相关字节码 diff 与开源源码关联，定位 SQLi 补丁点②根因：reset\_password 流程对用户可控 user-id 未做正整数校验即用于 DB 查询，补丁以 pos-int? 守卫并记 warn 截断攻击链③防御侧产物：基于 patch diff 快速产出检测规则，而无须公开完整 PoC④检测模式：POST /api/session/reset\_password 返回 HTTP 400 后再 GET /api/user/current 返回 200 的两步日志特征，作为 WAF/反向代理/代理日志的狩猎规则）】

ZBT ENDLESSDOORS 固件后门取证与检测（VulnCheck）

📰 VulnCheck Advisory · 📅 2026-08-05（持续分析）

【可学技术 — 供应链固件后门取证（①伪装识别：植入以 kworker 进程名掩盖，真内核线程无可执行路径与网络套接字，live 进程比对可发现 librctl.so 与 /usr/sbin/kworker、/etc/kworker.cfg、/etc/init.d/skworker 等工件②信标 IOC：每约 35 秒明文 TCP 信标至硬编码 C2（端口 7000/7001），可据固定间隔外出会话做南北向流量狩猎③检测规则：VulnCheck 同步发布 Suricata / Snort / YARA 规则，YARA 针对 librctl.so 与 rctlbash 关键字④处置：提取固件镜像比对是否仍含 rctl 包，重刷受信 OpenWrt 并验证 librctl.so 缺失， perimeter 阻断 C2 域名/IP）】

cPanel/WHM 认证绕过到 RCE 完整利用链与 PoC 解析（watchTowr Labs）

📰 watchTowr Labs · 📅 2026-08（CVE-2026-41940）

【可学技术 — 认证绕过类利用链构造（①手法：cpsrvd 预认证会话逻辑对 Authorization 头净化不足，编码 CRLF 注入可将 user=root 等属性写入磁盘会话文件，触发会话重载即取得 root...