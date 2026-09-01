---
title: 【安全速报】8月31日高危漏洞紧急预警
url: https://mp.weixin.qq.com/s/K5l0GEK9z3BjdoN-ftGjWQ
source: Doonsec's feed
date: 2026-08-31
fetch_date: 2026-09-01T06:58:25.622559
---

# 【安全速报】8月31日高危漏洞紧急预警

# 【安全速报】8月31日高危漏洞紧急预警

探知安全
探知安全

探知安全

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

# 【安全速报】8月31日高危漏洞紧急预警

2026年08月31日  |  探知安全

今日焦点

CISA 于 8 月 26 日将 Citrix NetScaler CVE-2026-8452（CVSS 9.8）纳入 KEV，并给出仅 3 天的联邦修复窗口——这是继 CVE-2026-8451 之后两个月内第二个被武器化的 NetScaler 漏洞，PoC 公开后 12 天内已监测到来自 12 个国家、12 个 IP 的 36 次在野利用尝试，落地物是 x.php / z.php Web Shell。同日，WordPress 主题 Avada 与 Fusion Builder 的零点击 RCE（CVE-2026-18431，CVSS 9.8）补丁发布，影响面覆盖百万级站点，且该漏洞由 AI 智能体在约 2 小时内完成挖掘与武器化，补丁窗口正在被 AI 压缩。此外 Zimbra 邮件服务器 CVE-2026-73570（CVSS 8.9）已被 CERT Polska 确认在野利用并落地 JSP Web Shell，Linux 内核 xfrm 提权漏洞 CVE-2026-72137 的利用代码已公开。建议优先排查 NetScaler 网关/AAA 虚拟服务器、公网 WordPress 站点、启用 zimbra-snmp 的邮件服务器与本地提权面。

## 漏洞详情

严重CVE-2026-8452CVSS 9.8

### Citrix NetScaler 堆溢出未认证 RCE（CVSS 9.8·CISA KEV 8/26·3 天修复窗口·已投放 Web Shell）

Citrix NetScaler ADC 与 NetScaler Gateway 的 SAML 认证栈存在堆溢出（内存溢出）缺陷，未认证、无需用户交互，只要设备被配置为 Gateway（SSL VPN、ICA Proxy、CVPN、RDP Proxy）或 AAA 虚拟服务器，攻击者远程发送恶意请求即可实现预认证远程代码执行。Citrix 在 6 月 30 日的公告中仅将其描述为"可能导致不可预测行为与拒绝服务"的高危问题，明显低估了危害——8 月 14 日 WatchTowr 公开技术分析与 PoC，证明该堆溢出可被完整武器化为预认证 RCE，相关 GitHub 仓库数日内收获 58 颗星。威胁情报公司 Previdian（原 KEVIntel）与 Defused Cyber 相继报告在野攻击：攻击者投放名为 x.php、z.php 的 Web Shell，并执行 id、echo 等侦察命令，12 天窗口内记录到 36 次利用尝试，攻击源覆盖瑞士、德国、中国香港、日本、荷兰、俄罗斯、新加坡、土耳其、美国、越南等 12 个国家和地区。CISA 于 8 月 26 日将其纳入 KEV，联邦机构修复截止日为 8 月 29 日。截至 8 月 26 日，Citrix 尚未更新公告正式承认在野利用。

影响范围

NetScaler ADC / NetScaler Gateway 14.1（< 14.1-72.61）、13.1（< 13.1-63.18）、14.1 FIPS（< 72.61）、13.1 FIPS 与 NDcPP（< 13.1-37.272）

**修复建议：**立即升级至 14.1-72.61 / 13.1-63.18 及以上（FIPS 与 NDcPP 版本对应 72.61 / 13.1-37.272）；排查设备上的 x.php、z.php 等异常 Web Shell 文件与异常子进程、异常出站连接；无补丁窗口内先用 ACL 收敛 Gateway 与 AAA 虚拟服务器的公网暴露面

严重CVE-2026-18431CVSS 9.8

### WordPress Avada + Fusion Builder 零点击 RCE（CVSS 9.8·百万级站点·AI 智能体 2 小时挖出）

Wordfence 于 8 月底披露 Avada 主题与 Fusion Builder 插件的漏洞链 CVE-2026-18431，CVSS 9.8。该链串联了授权校验缺陷、输入验证不足、信任边界混淆与文件处理问题共 6 个环节，最终把一个公开可访问的 WordPress 端点变成未认证任意 PHP 执行：零点击、无需任何凭据，一次 HTTP 请求即可完全控制站点——拖库、创建管理员账号、挂马或篡改页面。补丁于 8 月 26 日随 Avada 7.16.1 与 Fusion Builder 3.16.1 发布，披露时尚未发现在野利用，但利用门槛极低，需按"即将被武器化"对待。Avada 累计销量超过 100 万份，是最主流的商业 WordPress 主题之一；前提是 Avada 与 Fusion Builder 同时启用，但凡是尚未升级的老站点都在射程内，尤其是由外部建站公司维护、更新节奏不固定的营销站与电商站（WooCommerce 场景下 RCE 往往直通支付数据与客户 PII）。本期另一看点是发现方式：Wordfence 内部智能体框架 Argus 从定位漏洞、复现到生成 PoC 全程约 2 小时——研究员找得更快，攻击者的自动化同样更快，基于"人工披露节奏"建立的补丁窗口假设已经失效。

影响范围

Avada 主题 ≤ 7.16 且 Fusion Builder 插件 ≤ 3.16（两者同时启用可被完整利用），Avada 累计销量超 100 万份

**修复建议：**立即双升——Avada 至 7.16.1、Fusion Builder 至 3.16.1，只升级其中一个仍存在风险；全量盘点 WordPress 资产（含 staging、测试与历史子域）；无法立即升级时部署 WAF 虚拟补丁，拦截针对 Avada/Fusion Builder 端点的异常请求

高危CVE-2026-73570CVSS 8.9

### Zimbra 邮件服务器 SMTP 命令注入未认证 RCE（CVSS 8.9·CISA KEV 8/21·CERT Polska 确认在野利用）

Zimbra Collaboration Suite（ZCS）的 zimbra-snmp 可选组件所附带的 swatchdog 监控服务，在处理 SNMP 通知时对不可信输入净化不足，构成 OS 命令注入（CWE-78）。攻击者无需任何凭据与用户交互，只需向目标服务器发送一封精心构造的 SMTP 请求，即可以 zimbra 用户权限执行任意系统命令。CVSS v3.1 评分 8.9（AV:N/AC:H/PR:N/UI:N/S:C/C:H/I:H/A:L）。由于 swatchdog 在装上 zimbra-snmp 后默认运行，凡是启用 snmp\_notify 的实例都处于暴露状态。CERT Polska 本周发布通报确认在野利用活动：真实攻击已在 Jetty Web 应用目录写入 JSP Web Shell 以实现持久化；CISA 已于 8 月 21 日将其纳入 KEV。邮件服务器被打穿意味着员工邮箱、通讯录、凭据与内网入口一并失守，且 Zimbra 长期是重点目标——此前俄罗斯关联组织 Laundry Bear 就曾利用 CVE-2025-66376 投递 ZimReaper 窃取邮件通信。

影响范围

Zimbra Collaboration Suite（ZCS）10.1.20 之前全部版本，且安装了可选组件 zimbra-snmp 并启用 SNMP 通知（snmp\_notify）

**修复建议：**立即升级至 ZCS 10.1.20 或更高版本；排查 /var/log/zimbra.log 中的异常服务启停记录，检查近 30 天内 /opt/zimbra/jetty/webapps/、/opt/zimbra/jetty\_base/webapps/ 与 /tmp/ 下由 zimbra 账户创建的文件（重点找 JSP Web Shell）；发现入侵迹象及时上报国家 CERT

严重CVE-2026-72137CVSS 9.8

### Linux 内核 xfrm double-free 本地提权至 root（CVSS 9.8·利用代码已公开）

Linux 内核 xfrm 子系统的 nat\_keepalive\_send() 函数存在 double-free 缺陷（CWE-415）：当 IPv4 或 IPv6 发送辅助函数报告错误时，该函数会释放网络数据包缓冲区 skb，而这种清理只有在 skb 尚未进入输出路径时才安全；一旦协议栈已接管该缓冲区，再次释放即造成重复释放，进而导致内存破坏并提权至 root。该缺陷于 2024 年 6 月引入，2026 年 7 月在上游完成修复。Nebula Security（NebuSec）于 8 月 27 日公开完整漏洞利用源码与演示视频，并已在最新的 Ubuntu 26.04 上完成提权演示。CVSS 9.8，目前尚未确认实际在野利用，但"公开 PoC + 本地提权"的组合会迅速被纳入各类提权工具包与容器逃逸链，普通用户权限即可拿到 root 的风险必须当作紧急项处理。

影响范围

在 2024 年 6 月至 2026 年 7 月窗口内、携带存在缺陷 nat\_keepalive 代码的内核构建版本（NebuSec 公开研究以 Ubuntu 7.0.0-28 构建为靶标并在 Ubuntu 26.04 上完成演示）

**修复建议：**立即更新至包含上游修复的内核版本并重启生效，主流发行版已通过例行更新推送修复内核；无法及时修补时限制本地与容器访问、监控异常权限变更与提权行为

高危CVE-2026-18963CVSS 9.1

### Keycloak 重置密码流程校验缺陷可接管任意账户（CVSS 9.1·未认证·含管理员账户）

开源身份与访问管理服务器 Keycloak 的 reset-credentials 认证流程存在状态校验不当，被归类为忘记密码场景下的弱密码恢复机制（CWE-640）。攻击者向 reset-credentials 端点发送精心构造的请求，认证会话会被直接推进到"更新密码"阶段，而本应通过邮件下发的 action token 完全不再需要。结果是未认证攻击者无需任何用户交互，即可重置任意用户（包括管理员账户）的密码，实现完整账户接管。CVSS 9.1（由 Red Hat 作为 CNA 评定）。补丁随上游 26.7.2（8 月 19 日发布）提供，Red Hat 于 8 月 18 日发布 4 份 errata（RHSA-2026:56519/56520/56523/56524）；截至 8 月 24 日尚未发现在野利用与公开 PoC。Keycloak 通常是企业 SSO 的信任根，一旦越过边界，攻击者拿到的是其背后所有的业务系统。

影响范围

上游 Keycloak 26.7.2 之前版本；Red Hat Build of Keycloak（RHBK）26.4（operator bundle < 26.4.15-1、镜像 < 26.4-23）与 26.6（operator bundle < 26.6.6-1、镜像 < 26.6-12）

**修复建议：**立即升级上游至 26.7.2、RHBK 至 26.4.15 / 26.6.6；无法立即升级时，在所有 realm 关闭"Forgot password"功能（Realm settings → Login → Forgot password，每个 realm 都要设置）；同时关注同批修复的 CVE-2026-15571（可预测的 account-linking 哈希导致账户接管）

满分CVE-2026-69836CVSS 10.0

### Microsoft Entra ID 反序列化 RCE（CVSS 10.0 满分·微软澄清未在野利用·已完全缓解·用户无需操作）

微软于 8 月 20 日前后披露云身份服务 Entra ID（原 Azure Active Directory）的满分漏洞 CVE-2026-69836，CVSS 10.0，根因是不可信数据反序列化（CWE-502），未授权攻击者可经网络执行代码，由微软首席安全工程师 Robert Fitzpatrick 发现并报告。需要特别澄清一处信息：微软公告最初在"Exploitability Assessment"中将 Exploited 标为 Yes，8 月 21 日经 The Hacker News 问询后更正为 No，并明确声明"该漏洞未在野外被利用"、"已由微软完全缓解，使用该服务的客户无需采取任何额外操作"。本期将其列入并非要求打补丁，而是提示一类结构性风险：Entra ID 是企业全域身份的信任根，同类反序列化缺陷一旦成立即为跨租户级灾难，值得跟踪微软后续的技术复盘，并借机复核租户内的异常令牌签发、应用凭据变更与管理员操作审计日志。

影响范围

Microsoft Entra ID（原 Azure AD）云服务；微软称漏洞已在服务端完全缓解，客户无需操作

**修复建议：**无需用户侧补丁动作；建议导出并复核近期令牌签发、应用凭据变更与管理员操作日志，关注 MSRC 后续技术说明与处置公告

## 紧急提醒

本期最高优先级只有一个：Citrix NetScaler CVE-2026-8452。CISA 给出的联邦修复窗口只有 3 天，这在 KEV 目录里属于罕见信号；更关键的是时间线——Citrix 6 月 30 日修、WatchTowr 8 月 14 日公开 PoC、8 月 26 日即入 KEV，中间不到两周，攻击者的落地物是 x.php / z.php Web Shell，意味着被打穿的不只是一台 VPN 网关，而是整个内网入口，且危机波及 12 个国家和地区的机构。它与两个月前一个披露 24 小时内即被利用的 CVE-2026-8451 一起，说明 NetScaler 已经成为"披露即武器化"的固定靶场。第二梯队是 Avada 零点击 RCE 与 Zimbra 邮件服务器在野利用：前者一次请求打穿整站、影响面百万级且补丁刚发布、覆盖率极低；后者直接把员工邮箱与内网入口打包交出去。请按 NetScaler 网关/AAA → 公网 WordPress → 启用 zimbra-snmp 的邮件服务器 → Linux 内核本地提权面 → Keycloak 身份系统的顺序排查，先止血再谈加固。

## 处置建议

① NetScaler ADC / Gateway 立即升级至 14.1-72.61 / 13.1-63.18（FIPS 与 NDcPP 对应 72.61 / 13.1-37.272），并全量排查 x.php、z.php 等 Web Shell 与异常子进程、异常出站连接

② 公网 WordPress 站点双升 Avada 至 7.16.1 与 Fusion Builder 至 3.16.1，staging、测试与历史子域一并盘点，无法立即升级先上 WAF 虚拟补丁

③ Zimbra 升级至 10.1.20，核查 /var/log/zimbra.log 异常服务启停，以及 /opt/zimbra/jetty\*/webapps/、/tmp/ 近 30 天内由 zimbra 账户新建的文件（重点排查 JSP Web Shell）

④ Linux 主机与镜像更新至包含 xfrm nat\_keepalive 上游修复的内核并重启，重点覆盖 Ubuntu 26.04 等新版本，同时收敛低权限账户与容器逃逸面

⑤ Keycloak 升级至 26.7.2（RHBK 对应 26.4.15 / 26.6.6），未升级前关闭所有 realm 的"Forgot password"，并复核 8 月以来管理员账户的异常密码重置记录

⑥ Entra ID 无需补丁动作，但建议复核近期令牌签发、应用凭据变更与管理员操作日志，并跟踪 MSRC 后续技术说明

觉得有用？点击右下角**在看**，让更多人看到

预览时标签不可点

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/ayPnpNqYCJKbeG52l1HMrttVrHhaGYKtDOWalO9FcwwVTzzCKhpg0BEKR4eZdo8JXdrv6n8RZAOgtnmcEPgvHg/0?wx_fmt=png)

微信扫一扫可打开此内容，
使用完整服务

：
，
，
，
，
，
，
，
，
，
，
，
，
。

视频
小程序
赞
，轻点两下取消赞
在看
，轻点两下取消在看
分享
留言
收藏
听过