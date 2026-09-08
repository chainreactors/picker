---
title: 【安全速报】9月7日高危漏洞紧急预警
url: https://mp.weixin.qq.com/s/bcZRXrDIDkJFk6UkSn8LIw
source: Doonsec's feed
date: 2026-09-07
fetch_date: 2026-09-08T06:40:18.533743
---

# 【安全速报】9月7日高危漏洞紧急预警

# 【安全速报】9月7日高危漏洞紧急预警

探知安全
探知安全

探知安全

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

# 【安全速报】9月7日高危漏洞紧急预警

2026年09月07日  |  探知安全

今日焦点

本期两条边界设备攻击链均已实锤在野利用——SonicWall SMA1000 远程接入设备的 SSRF+命令注入链（CVE-2026-83548 + CVE-2026-83549，CVSS 10.0），未认证即可链式打出系统级 RCE，CISA 已纳入 KEV 并给出 9 月 5 日联邦修复截止日，这是该产品线 9 个月内第三次零日攻击链；MikroTik RouterOS 的 MikroTrick 链（CVE-2026-67276 + CVE-2026-86060）利用 SSH 公钥校验缺陷与用户名注入实现免密全接管，CERT Polska 已观测到攻击者创建 ops 后门账户。此外 SolarWinds N-central RMM 平台曝出 CVSS 10.0 预认证 RCE（CVE-2026-86218），一台中招即可波及 MSP 托管的全部下游客户。建议优先排查公网暴露的 SonicWall SMA1000、SSH 对公网开放的 MikroTik 路由器与自托管 N-central 服务器。

## 漏洞详情

严重CVE-2026-83548 + CVE-2026-83549CVSS 10.0

### SonicWall SMA1000 SSRF+命令注入链实现未认证 RCE（CVSS 10.0·CISA KEV 9/2·已确认在野利用）

SonicWall SMA1000 远程接入设备暴露出两个可串联的漏洞：CVE-2026-83548（CVSS 10.0，CWE-918/CWE-441）是 Appliance Work Place 接口的预认证 SSRF——在特定构造的 HTTP 参数下，该端点被诱导充当非预期的正向代理，将请求隧道转发到本应只有管理员在内网可达的 Appliance Management Console（AMC），形成"混淆代理"条件；CVE-2026-83549（CVSS 7.8，CWE-78）是 AMC 中的 OS 命令注入，单独利用需要管理员认证，但经 SSRF 隧道转发后认证检查形同虚设，两者串联即可实现未认证的系统级远程代码执行。SonicWall 在 9 月 1 日通告中确认两个漏洞均在野利用，CISA 于 9 月 2 日将其纳入 KEV 目录，联邦修复截止日 9 月 5 日。值得警惕的是，这是 SMA1000 产品线 9 个月内第三次被在野利用的零日链：2025 年 12 月 CVE-2025-40602，2026 年 7 月 CVE-2026-15409/15410 被 INC 勒索组织用于窃取缓存凭据、会话库与 TOTP 种子——打过 9 月补丁并不能撤销 7 月窗口期已泄露的 MFA 种子。

影响范围

SMA 1000 系列：SMA 6210、SMA 7210（物理）与 SMA 8200v（虚拟，全虚拟化平台），固件 12.4.3-03453 及以下、12.5.0-02835 及以下全部版本

**修复建议：**升级至 12.4.3-03526 或 12.5.0-02952 平台热补丁（注意按分支核对完整 build 号，同分支内既有受影响也有已修复构建）；联系 SonicWall 技术支持对曾运行受影响版本的设备做 IoC 排查；一旦发现入侵痕迹，物理设备重镜像、虚拟设备重新部署，并轮换全部用户/管理员密码、重置 TOTP 令牌

严重CVE-2026-67276 + CVE-2026-86060CVSS 9.2

### MikroTik RouterOS MikroTrick 链免密接管路由器（CVSS 9.2·CERT Polska 9/5 披露·在野利用·SSH 全接管）

MikroTik RouterOS 曝出 6 个漏洞，其中两个串联为免密全接管链 MikroTrick：CVE-2026-67276（CVSS 9.2，CWE-287）——SSH 公钥认证只比对 RSA 密钥的类型和模数（modulus），完全遗漏了指数（exponent）校验，攻击者只要知道目标用户的用户名和授权 RSA 公钥模数，即可构造一把自选指数的新密钥伪造有效签名，在不持有私钥的情况下以该用户身份打开 SSH 命令通道；CVE-2026-86060（CVSS 9.2，CWE-269）——SSH 登录路径对以禁止字符开头（如 -2）的用户名处理失当，可将会话的 RouterOS 策略掩码改写为完整管理员权限。CERT Polska 确认至少自 9 月 2 日起针对 SSH 暴露公网的设备存在活跃攻击，成功入侵的痕迹包括创建名为 ops 的高权限后门账户，日志特征为 login failure for user -2 from via ssh 与 user added by ssh:-2@，已归因的成功攻击源 IP 为 82.192.72.4，尝试源为 103.102.31.18。同批修复的还有 bandwidth-test 服务认证前内存泄露/崩溃（CVE-2026-67277，CVSS 8.8）、SSH 认证前 rekey 写文件（CVE-2026-67279）、WebFig 未认证任意文件读（CVE-2026-67281）与 X.509 签名校验缺陷（CVE-2026-67278）。MikroTik 于 9 月 3 日静默推送修复，并首次动用手机 App 推送全量告警。

影响范围

RouterOS：7.x 稳定版 < 7.24.2、7.x 长期支持版 < 7.23.4、6.x 长期支持版 < 6.49.21、7.25 早期 beta；受影响面覆盖 SSH、bandwidth-test、X.509 处理与 WebFig 组件

**修复建议：**立即升级至 7.24.2 / 7.23.4 / 6.49.21 / 7.25beta3 及以上；升级后在日志中检查 Flagged 状态（新版本内置的入侵痕迹检测）、排查 ops 等未知账户、计划任务、脚本、代理设置与隧道配置；将 SSH/WebFig/bandwidth-test 服务限制为仅管理网段可达；日志出现 -2 登录失败或 ops 账户的设备按已入侵处置

严重CVE-2026-86218CVSSv4 10.0

### SolarWinds N-central 预认证 RCE（CVSSv4 10.0·9/6 披露·RMM 管理平面·MSP 供应链风险）

SolarWinds（N-able）N-central 远程监控与管理（RMM）平台存在预认证远程代码执行漏洞 CVE-2026-86218，CVSSv4 评分 10.0 满分，归类为静态代码注入（CWE-96）：攻击者可控输入未经充分净化即进入服务端执行上下文，未认证攻击者仅需网络可达即可在 N-central 服务器上执行任意代码，无需凭据、无需交互。N-central 是 MSP 管理下游客户终端的核心平面，集中负责代理部署、补丁调度、脚本执行与远程访问——单台服务器失守即等于把攻击面一次性铺到全部托管客户，与 2021 年 Kaseya VSA 供应链事件的传播模型同构。N-able 于 9 月 6 日发布 2026.3 Hotfix 4（build 2026.3.1.14）修复，公告称暂未确认生产环境被利用，但这是 N-central 两个月内第二个严重漏洞——此前的认证绕过漏洞 CVE-2026-18577 已于 8 月被 CISA 纳入 KEV，RMM 平台在披露与在野利用之间的窗口期历来极短。

影响范围

N-able N-central 所有 2026.3.1.14 之前的版本（自托管部署为主）；托管云环境 NCOD 已由厂商统一修补

**修复建议：**自托管实例立即升级至 2026.3.1.14（HF4，支持从 2025.4 / 2026.1 / 2026.2 / 2026.3 / HF1-HF3 直接升级；注意 HF3 build 2026.3.1.13 仍不含本修复）；无法立即修补时将 Web 管理接口（8443）置于 VPN/防火墙白名单之后并监控异常访问；确认托管环境 NCOD 补丁状态并保持账户与角色权限卫生

严重CVE-2026-20212CVSS 9.8

### Cisco Nexus 9000 Silicon One 交换机未认证 Root RCE（CVSS 9.8·9/2 披露·数据中心骨干设备）

Cisco Nexus 9000 系列搭载 Silicon One 芯片的交换机存在未认证远程代码执行漏洞 CVE-2026-20212（CVSS 9.8，CWE-1327）：Silicon One 硬件抽象层的服务绑定到默认三层 VRF 的不受限 IP 上，导致 TCP 端口 43210、43211 在默认配置下从网络可达。能访问这两个端口的攻击者发送特制数据包即可触发以 root 权限执行的任意代码——无凭据要求、无用户交互、低攻击复杂度；同一缺陷还可使 S1HAL 进程崩溃导致设备整机重载，直接造成数据中心网络中断。受影响的是 10 款 Silicon One 型号（含 N9336C-SE1、N9K-C9804、N9K-C9808 及多款 Nexus Smart Switch），可通过 show module 命令核对设备 PID；其他 Nexus 9000 型号、ACI 模式与 Nexus 3000/7000 不受影响。Cisco 于 9 月 2 日披露，暂未观测到在野利用或公开 PoC（漏洞在 TAC 支持案例中发现），但同批 IOS XR 加固通告将 7 个 CVE 打包（其中 CVE-2026-20274 与 CVE-2026-20279 同为 CVSS 9.8 且全部版本无临时缓解），叠加 Sygnia 披露的 Fire Ant 组织在 IOS XR 路由器长期潜伏的背景，核心网络设备正成为重点攻击面。

影响范围

Nexus 9000 搭载 Silicon One ASIC 的 10 款型号：N9324C-SE1U、N9348Y2C6D-SE1U、N9364E-SG2-O、N9364E-SG2-Q、N9396T12C-SE1、N9348Y12C-SE1、N9396Y12C-SE1、N9336C-SE1、N9K-C9804、N9K-C9808；NX-OS 10.3(1) 至 10.6(3s)

**修复建议：**用 Cisco Software Checker 查询各设备的修复版本（已确认 10.6(4)+ 修复）并升级；过渡期部署 iACL 拒绝到 TCP 43210/43211 端口的入站流量，可叠加 Live Protect 临时防护 lp00031；先在实验环境验证 iACL 再上生产，避免误伤管理流量；IOS XR 设备按公告核对 SMU 可用性并规划升级

高危CVE-2026-85046CVSS 8.8

### Chrome V8 引擎零日漏洞在野利用（CVSS 8.8·2026 年第 6 个 Chrome 零日·9/5 紧急修复）

Google 于 9 月 5 日发布 Chrome 152.0.7977.82/.83（Windows/macOS）与 152.0.7977.82（Linux）紧急更新，修复 V8 JavaScript 与 WebAssembly 引擎中的类型混淆零日漏洞 CVE-2026-85046（CVSS 8.8），Google 已确认存在在野利用。该漏洞由研究员 Salvatore Gulizia 于 8 月 4 日报告，攻击者只需诱导用户访问恶意或被污染的网页，即可在沙箱内执行任意代码；V8 类型混淆可构造 JS 堆内任意读写原语，存在配合沙箱逃逸实现完全接管的可能性。同批更新还修复了 V8、Compositing、WebGL、Skia 与 DevTools 中的 10 个高危问题（类型混淆、UAF、越界等）。这是 2026 年第 6 个被在野利用的 Chrome 零日，CISA 在补丁发布当日将其纳入 KEV 目录。浏览器覆盖全终端，是水坑攻击与定向钓鱼的标准入口，全员升级没有例外。

影响范围

Windows/macOS/Linux 平台上 152.0.7977.82 之前的所有 Chrome 版本；基于 Chromium 内核的浏览器（Edge 等）需同步跟进上游补丁

**修复建议：**立即升级至 152.0.7977.82/.83 或更高版本并重启浏览器确认（chrome://settings/help）；企业通过管理策略强制推送更新并盘点未升级终端；临时缓解可启用站点隔离、收缩攻击面策略；监控针对 V8 漏洞的利用特征与异常渲染进程行为

高危CVE-2026-6471CVSS 7.2

### PostgreSQL PostGREShell：REPLICATION 权限 12 年来可直达操作系统级 RCE（CVSS 7.2·CWE-862·9/1 技术细节公开）

Cyera Research 披露代号为 PostGREShell 的漏洞 CVE-2026-6471（CVSS 7.2，CWE-862 授权缺失）：PostgreSQL 逻辑解码功能在创建复制槽时，将客户端指定的输出插件名直接传给动态加载器，未做路径校验——持有 REPLICATION 属性的非超级用户账户可指定任意文件路径（含 ../ 穿越、绝对路径），诱使服务器 dlopen 加载并执行该文件，代码以运行 PostgreSQL 的操作系统账户（通常为 postgres）权限执行。Windows 上可经 SMB UNC 路径直接从攻击者控制的机器加载库而无需落盘，Linux/macOS 在启用 NFS automount 时同理。Cyera 的演示插件可将复制账户重写为超级用户并安装三种重启后依然存活的持久化后门。该缺陷自 2014 年 PostgreSQL 9.4 引入逻辑解码起已存在 12 年；CDC 管道、备用库、pgBackRest/Barman 等备份工具的账户普遍持有 REPLICATION 权限，实际暴露面远大于" rogue 超级用户"威胁模型。修复版 8 月 13 日已发布，9 月 1 日技术分析公开后利用门槛显著降低。

影响范围

PostgreSQL 14.24 / 15.19 / 16.15 / 17.11 / 18.5 之前的全部受支持分支版本（缺陷自 9.4 即存在，9.x-13 等已停支持分支同样含漏洞代码需迁移）；利用条件：wal\_level = logical + 存在 REPLICATION 权限账户

**修复建议：**升级至 18.5 / 17.11 / 16.15 / 15.19 / 14.24（2026-08-13 发布）；审计 pg\_roles 中 rolreplication=true 的账户并回收不必要的 REPLICATION 权限；盘点 pg\_replication\_slots 使用的第三方插件（wal2json、decoderbufs 等），升级后需将其显式加入新增的 output\_plugin\_libraries 白名单（默认仅 pgoutput、test\_decoding）否则逻辑解码将中断；过渡期在 pg\_hba.conf 限制复制连接来源，阻断数据库服务器的出站 SMB（445）与 NFS（2049）

## 紧急提醒

本期最高优先级是两条已实锤在野利用的边界设备攻击链：SonicWall SMA1000（CVSS 10.0 SSRF + 命令注入，KEV 截止日 9 月 5 日已过）与 MikroTik MikroTrick（免密 SSH 全接管）。边界设备是攻击者最爱的入口——SMA1000 九个月三次零日链、7 月那次已被 INC 勒索组织用来抽取 TOTP 种子，意味着只打补丁不排查等于给入侵者留后门；MikroTik 的 ops 后门账户和 -2 日志特征给了我们难得的确定性 IoC，逐台核对成本很低、收益极高。第二优先级是 SolarWinds N-central 的 CVSS 10.0 预认证 RCE——RMM 管理平面单点失守即横向铺满全部托管客户，Kaseya 事件的教训历历在目，且该平台 8 月刚上过 KEV。第三是覆盖面问题：Chrome V8 零日要求全终端当天升级，PostgreSQL 则需要所有用 CDC/备份工具的团队审计 REPLICATION 账户。请按公网 SMA1000 → 公网 SSH 的 MikroTik → 自托管 N-central → Silicon One Nexus 9000 → Chrome 全员 → PostgreSQL REPLICATION 审计的顺序排查。

## 处置建议

① SonicWall SMA1000 核对固件完整 build 号，升级至 12.4.3-03526 / 12.5.0-02952；联系 SonicWall 支持 IoC 排查，发现入侵即重镜像/重部署并轮换全部密码、重置 TOTP；7 月曾暴露公网的设备即使已打 9 月补丁，也要按 TOTP 种子可能已泄露处置（重新绑定全部 MFA）

② MikroTik 路由器升级至 7.24.2 / 7.23.4 / 6.49.21 / 7.25beta3；检查 Flagged 状态、删除 ops 等未知账户、排查计划任务/脚本/代理/隧道；SSH 与 WebFig 限制为管理网段可达；日志出现 -2 登录失败或 82.192.72.4 / 103.102.31.18 来源的设备立即隔离处置

③ 自托管 SolarWinds N-central 立即升级至 2026.3.1.14（HF3 2026.3.1.13 不含本修复）；无法立即升级时将 8443 管理口置于 VPN/白名单之后；托管环境确认 NCOD 补丁状态

④ Cisco Nexus 9000 用 show module 核对 PID 是否属于 10 款 Silicon One 型号，运行 Cisco Software Checker 确定修复版本并升级；过渡期部署 iACL 封禁 TCP 43210/43211，叠加 Live Protect lp00031；IOS XR 设备核对 SMU 升级路径

⑤ Chrome 全终端升级至 152.0.7977.82/.83 并重启浏览器验证版本；企业用管理策略强制推送并盘点滞留终端；基于 Chromium 的其他浏览器同步跟进上游补丁

⑥ PostgreSQL 升级至 18.5 / 17.11 / 16.15 / 15.19 / 14.24；审计并回收非必要 REPLICATION 权限；升级后将第三方逻辑解码插件显式加入 output\_plugin\_librari...