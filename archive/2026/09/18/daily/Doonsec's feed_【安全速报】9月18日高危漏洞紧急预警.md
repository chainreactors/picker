---
title: 【安全速报】9月18日高危漏洞紧急预警
url: https://mp.weixin.qq.com/s/OUapQ8KZn8TdzttSZt9j7w
source: Doonsec's feed
date: 2026-09-18
fetch_date: 2026-09-19T06:59:23.401265
---

# 【安全速报】9月18日高危漏洞紧急预警

# 【安全速报】9月18日高危漏洞紧急预警

探知安全
探知安全

探知安全

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

# 【安全速报】9月18日高危漏洞紧急预警

2026年09月18日  |  探知安全

今日焦点

本期主线是"存量高危漏洞被升级利用"——Broadcom 7 月底已发布补丁的 VMware vCenter 未认证 RCE 漏洞 CVE-2026-59310（CVSS 9.8）本周被 CISA 确认已加入勒索武器库，德国应急响应机构已观测到 47 国 361 个 IP 失陷并部署 Babuk 系勒索软件；CISA 9 月 16 日一口气将三条在野利用漏洞纳入 KEV：Cisco ISE 满分认证绕过（10.0）、Acronis 备份插件本地提权、Google Pixel 基带零点击提权（无需任何用户交互）。另有 FatPipe VPN 边界设备未认证 root RCE（9.8）与 Cisco FMC 反序列化 root RCE（9.8）两条新披露。建议优先排查：公网可达的 vCenter Syslog 服务与补丁级别、Cisco ISE/ISE-PIC 版本、企业内 Acronis cPanel/Plesk 备份组件。

## 漏洞详情

严重CVE-2026-76460CVSS 10.0

### Cisco ISE 满分认证绕过：一个 API 请求直通管理后台（CVSS 10.0·CISA KEV 9/16·在野利用·修复截止 9/19）

Cisco Identity Services Engine（ISE）存在认证绕过漏洞 CVE-2026-76460（Cisco 官方归类为"特权 API 使用不当"，CVSS 10.0 满分）：ISE 特定 API 端点认证控制不足，未认证远程攻击者发送特制请求即可绕过认证，直接访问设备的 Web 管理界面。ISE 是企业网络准入控制（NAC）与身份策略的核心大脑，管理界面失陷意味着攻击者可篡改准入策略、签发证书、把任意设备"洗白"进内网，或直接以管理平面为跳板横向渗透。

Cisco PSIRT 已确认该漏洞正在被活跃利用，并强烈建议客户立即升级到修复版本；CISA 于 9 月 16 日将其纳入 KEV 目录，联邦文职机构修复截止 9 月 19 日——仅 72 小时窗口。同日 ISE 9 月加固版本中还包含多项安全修复，官方要求一并覆盖。

影响范围

Cisco ISE 与 ISE Passive Identity Connector（ISE-PIC）：3.1 Patch 11 及更早、3.2 Patch 10 及更早、3.3 Patch 11 及更早、3.4 Patch 6 及更早、3.5 Patch 3 及更早

**修复建议：**升级至 3.1 Patch 12 / 3.2 Patch 11 / 3.3 Patch 12 / 3.4 Patch 7 / 3.5 Patch 4；管理界面立即收敛访问来源（仅限管理网段/堡垒机）；排查管理界面异常登录与策略篡改记录，无法排除失陷的按事件响应流程处置并轮换相关管理员凭据

严重CVE-2026-59310CVSS 9.8

### VMware vCenter Syslog 路径遍历 RCE：勒索组织正式接棒（CVSS 9.8·CISA KEV 8/18·勒索软件在野利用·47 国 361 IP 失陷）

VMware vCenter Server 的 Syslog 服务存在路径遍历漏洞 CVE-2026-59310（CWE-22，CVSS 3.1 9.8）：具备网络访问能力的未认证攻击者无需任何凭据即可利用该漏洞执行任意代码。vCenter 是 vSphere 虚拟化环境的集中管理平台，拿下 vCenter 即可触达其管辖的 ESXi 主机与大批虚拟机——快照、备份、恢复路径尽入囊中，这正是勒索攻击者的理想目标。

时间线值得警惕：Broadcom 7 月 29 日发布补丁（VMSA-2026-0006，同通告还修复 vmdir 认证绕过漏洞 CVE-2026-59309，同为 9.8 分）；8 月初德国应急响应公司 QUIRSO 观测到利用开始，累计报告 47 国 361 个失陷 IP，早期攻击部署反向 SSH 维持驻留；疑似中国背景组织被指在攻击中部署 .babyk 勒索软件并利用 GitHub 上的清理工具抹除痕迹；CISA 8 月 18 日纳入 KEV，9 月 13-15 日更新 KEV 条目明确标记"勒索软件利用"。Shadowserver 近期统计仍有超过 450 台 vCenter 暴露在公网。

影响范围

VMware vCenter Server 9.1.x（< 9.1.0.0300）、9.0.x（< 9.0.2.0100）、8.0（< 8.0 Update 3k，及 8.0 U2f 对应构建）；打包相应 vCenter 构建的 VMware Cloud Foundation 与 vSphere Foundation 同样受影响；7.0 延长支持客户需联系 Broadcom 获取修复

**修复建议：**升级至 9.1.0.0300+ / 9.0.2.0100+ / 8.0 U3k+，原始通告无 workaround；立即将 vCenter（尤其 Syslog 服务端口）移出公网、收敛至管理网络；排查可疑计划任务（cron）、新增管理员账户、伪造 VMware 服务、ESXi 上的 .babyk 加密文件与反向 SSH 外联；确认备份与恢复链路未被篡改

严重CVE-2026-90822CVSS 9.8

### FatPipe VPN 边界设备命令注入：管理接口开放即沦陷（CVSS 9.8·9/17 披露·固件已停更）

FatPipe MPVPN、WARP 与 IPVPN 广域网/VPN 边界设备存在 OS 命令注入漏洞 CVE-2026-90822（CWE-78，CVSS 3.1 9.8，AV:N/AC:L/PR:N/UI:N）：xtremed 守护进程的 AuthFormServlet 端点未对输入做清洗即传入操作系统命令执行函数，能够访问设备管理界面的未认证远程攻击者可直接以 root 权限执行任意命令——完整接管设备、截获或篡改 WAN/VPN 流量、以内网跳板继续渗透。Securifera 于 9 月 17 日发布通告。

缓解因素是受影响的管理界面默认关闭，需管理员显式开启才可达；但风险点同样明确：受影响固件 10.1.2r60p100 已是停止维护（EOL）版本，厂商不再提供常规安全更新。

影响范围

FatPipe MPVPN / WARP / IPVPN 固件 10.1.2r60p100（管理界面处于启用状态的设备）

**修复建议：**联系 FatPipe 支持获取并安装对应机型的当前受支持软件版本；立即将管理访问限制在可信管理网段，配置 WAN ACL 仅放行授权源地址，严禁管理界面暴露公网；暂无升级条件的设备保持管理界面关闭

严重CVE-2026-20242CVSS 9.8

### Cisco FMC 反序列化 root RCE：External Database Access 特性成攻击入口（CVSS 9.8·9/16 披露·需前置条件）

Cisco Secure Firewall Management Center（FMC）External Database Access 特性存在不安全反序列化漏洞 CVE-2026-20242（CWE-502，Cisco 官方 CVSS 3.1 9.8）：该特性对用户提供的 Java 字节流反序列化处理不安全，攻击者向特定 TCP 端口发送构造的序列化 Java 字节流，即可在设备上执行任意命令并提权至 root。这是继 8 月被实战利用的满分认证绕过 CVE-2026-20079 之后，FMC 管理平面一个月内曝出的又一条通向 root 的利用链。

利用存在前置条件：攻击者必须已控制 external database access list 中配置的主机才能触达该端口；若 FMC 管理接口未暴露公网，攻击面显著收窄。但这恰恰要求管理员严格核对该访问列表——列表里任何一台失陷主机都会成为跳板。

影响范围

配置了 External Database Access 特性的 Cisco Secure Firewall Management Center（FMC）Software

**修复建议：**参照 Cisco 9 月 16 日安全通告升级至各分支修复版本；立即审计 external database access list，仅保留可信主机并移除不再需要的条目；确认 FMC 管理接口不暴露公网，必要时限制 External Database Access 对应 TCP 端口的访问来源；对访问列表内主机做失陷排查

高危CVE-2026-87886CVSS 未公布

### Acronis 备份组件默认权限缺陷：本地低权限提至 root（CISA KEV 9/16·定向攻击在野·修复截止 10/7）

Acronis Backup 存在不安全默认权限漏洞 CVE-2026-87886（"Incorrect Default Permissions"）：问题出在 Acronis Backup for cPanel & WHM 插件与 Acronis Backup extension for Plesk 扩展——默认文件权限配置过于宽松，低权限本地攻击者可篡改备份服务使用的文件，进而以提升后的（root 级）权限执行代码。Acronis 确认该漏洞已在有限的定向攻击中被利用，CISA 9 月 16 日将其纳入 KEV，联邦机构修复截止 10 月 7 日。

影响范围

Acronis Backup for cPanel & WHM 插件；Acronis Backup extension for Plesk 扩展

**修复建议：**使用上述组件的主机立即升级至 Acronis 官方通告中的修复版本；排查备份服务相关文件与目录的异常修改、新增 SUID 文件与可疑计划任务；共享主机环境尤其注意租户隔离与最小权限配置

高危CVE-2026-58704CVSS 8.8

### Google Pixel 基带零点击提权：不用点链接也能中招（CVSS 8.8·CISA KEV 9/16·定向攻击在野·修复截止 9/19）

Google 9 月 15 日发布 2026 年 9 月 Pixel 安全更新（共修复 110 个漏洞），其中蜂窝基带（Cellular Modem）漏洞 CVE-2026-58704 已被在野利用：基带代码逻辑错误导致权限检查被绕过，攻击者在无线电邻近范围（proximal/adjacent）内即可实现远程提权——全程不需要机主点击链接或打开文件，属于典型的零点击攻击路径，也是间谍软件最青睐的漏洞类型。Google 表示有迹象表明该漏洞正被"有限的定向利用"，未披露攻击者身份与攻击目标。CISA 9 月 16 日纳入 KEV（NVD 口径 CVSS 3.1 8.8，Google 公告口径 8.0），联邦机构修复截止 9 月 19 日。

影响范围

Google Pixel 设备（9 月安全更新前版本；本次 Pixel 公告覆盖 Pixel 6 至 Pixel 11 系列，全球版本号 CP3A.260905.009）

**修复建议：**立即升级系统，安全补丁级别达到 2026-09-05 或更高（设置 → 安全和隐私 → 系统和更新）；企业统一管理的 Pixel 机队通过 MDM 尽快推送；敏感岗位人员设备优先处理

## 紧急提醒

本期最高优先级是 VMware vCenter 勒索链（CVE-2026-59310）。原因有三：第一，攻击者已经换代——从早期部署反向 SSH 驻留的渗透团伙，升级为直接加密的勒索组织，CISA 已在 KEV 条目中正式标记勒索利用，47 国 361 个失陷 IP 说明这不是个案而是规模化扫描；第二，补丁已发布近 50 天，公网仍有 450+ 台 vCenter 裸奔，"补了就安全"的错觉正在让运维团队放松排查——打了补丁不等于清掉了已植入的后门，7 月 29 日后从未做入侵排查的环境必须补做；第三，vCenter 的位置决定量级，一台失陷可能拖垮整个虚拟化集群与备份链路。其次是 Cisco ISE 满分认证绕过，9/19 截止日在即且确认在野利用，网络准入中枢失陷的后果是全域信任模型崩塌。请按：vCenter 补丁与入侵排查 → ISE 版本升级 → Acronis/FMC/Pixel 更新 的顺序处置。

## 处置建议

① VMware vCenter 逐台盘点（含灾备/实验环境），升级至 9.1.0.0300+ / 9.0.2.0100+ / 8.0 U3k+；公网暴露的 Syslog 服务端口立即下线收敛；7 月 29 日后未做过排查的环境，按 IoC 清单核查 cron 任务、新增管理员账户、.babyk 文件与反向 SSH 外联，命中即启动事件响应

② Cisco ISE/ISE-PIC 升级至 3.1 Patch 12 / 3.2 Patch 11 / 3.3 Patch 12 / 3.4 Patch 7 / 3.5 Patch 4（9/19 截止）；管理界面收敛至管理网段，审计异常登录与准入策略变更记录

③ FatPipe MPVPN/WARP/IPVPN 用户核对固件是否为 10.1.2r60p100，联系厂商获取受支持版本；管理界面保持关闭或严格限制来源，WAN ACL 只放行授权地址

④ Cisco FMC 升级至 9/16 通告对应修复分支；审计 external database access list 并清理不可信条目，限制相关 TCP 端口访问来源，确认管理接口未暴露公网

⑤ 部署 Acronis Backup for cPanel & WHM / for Plesk 的主机升级修复版本，排查备份相关文件的异常改动；共享主机收紧目录权限

⑥ 全员 Pixel 设备升级至 2026-09-05 补丁级别（9/19 截止），企业通过 MDM 推送；同一批 9 月更新还应覆盖 Android 安全公告中的其余修复

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