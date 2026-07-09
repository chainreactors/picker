---
title: 7月8日高危CVE漏洞速报
url: https://mp.weixin.qq.com/s/bAfsWIuRhVac2SmgUvxOlA
source: Doonsec's feed
date: 2026-07-08
fetch_date: 2026-07-09T05:58:26.781360
---

# 7月8日高危CVE漏洞速报

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/nZrMrH4FF0KuheuEVJQMS7OL1XpoOfCT7AqnpG5VcIQSfs1nTJH0iaaxFdQ1nsNUKGSSE5zrbdyYDJzGZRIP47ESOcbfloLXDJLmtXCzmLvc/0?wx_fmt=jpeg)

# 7月8日高危CVE漏洞速报

探知安全

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

安全速报

# 【安全速报】7月8日高危漏洞紧急预警

2026年07月08日  |  探知安全

本期重大威胁：BeyondTrust Remote Support产品线曝出4个严重漏洞，其中2个认证绕过漏洞CVSS评分双双达到9.2可完全接管远程支持设备；Linux内核0-day漏洞BadEpoll（CVE-2026-46242）存在竞态条件+释放后使用双重缺陷，无特权用户可提升至root权限，影响所有5.10+内核的服务器与Android设备；FortiBleed凭证窃取行动（CVE-2026-35616）已收割超1.1亿条FortiGate凭证，INC/Lynx勒索软件组织已确认12+受害者；Opera GX浏览器零点击Mod静默安装漏洞可窃取已登录用户Gmail地址等敏感数据，影响2500万游戏玩家；Ubiquiti UniFi Protect SSRF漏洞CVE-2026-55115 CVSS 9.9可实现低权限用户提权，请立即排查修复。

## 漏洞详情

|  |  |  |
| --- | --- | --- |
| 严重 | CVE-2026-40138 | CVSS 9.2 |

### BeyondTrust Remote Support 双认证绕过漏洞 CVSS 9.2——BT26-03公告4漏洞批量修复·AI辅助发现·历史曾遭WebShell后门利用

2026年7月7日，BeyondTrust发布BT26-03安全公告，一次性修复Remote Support和Privileged Remote Access产品中的4个严重漏洞。其中最核心的是CVE-2026-40138和CVE-2026-40139，两个认证绕过漏洞CVSS评分均达9.2（CVSS 4.0标准）。漏洞位于认证子系统，源于对认证数据的不当验证和处理——网络位置的攻击者无需任何认证凭据，即可发送恶意构造的请求绕过访问控制，获得对远程支持设备的未授权访问，包括具有管理员权限的账户。第三漏洞CVE-2026-40140（CVSS 8.7）为预认证拒绝服务漏洞，第四漏洞CVE-2026-40141（CVSS 8.5）允许低权限认证用户越权访问敏感数据。值得注意的是，这4个漏洞均是在内部安全评估中借助Anthropic Claude Opus 4.8等公开AI模型发现的。BeyondTrust历史上此类产品漏洞曾被反复利用：CVE-2024-12356被用于部署Web Shell、CVE-2026-1731被用于部署后门，凸显远程支持类产品的极高攻击价值。受影响版本为Remote Support 25.3.2及以下、Privileged Remote Access 25.3.2及以下，建议立即升级至RS/PRA 25.3.3或更高版本。

影响范围

BeyondTrust Remote Support 25.3.2及以下版本、Privileged Remote Access 25.3.2及以下版本（全球数千企业MSP/MSSP和IT运维团队部署，政府、金融、医疗行业广泛使用）

修复建议：立即升级至RS/PRA 25.3.3或更高版本；审查远程支持设备的认证配置，确认是否启用受影响认证模块；审计设备访问日志中是否存在异常认证请求；由于历史案例存在后门植入风险，建议对升级前的设备进行安全扫描；限制管理接口仅可信IP白名单访问

|  |  |  |
| --- | --- | --- |
| 严重 | CVE-2026-46242 | CVSS 7.8 |

### Bad Epoll——Linux内核0-day竞态条件+UAF提权·无特权用户直取root·服务器/桌面/Android全面受影响

7月初披露的Linux内核0-day漏洞Bad Epoll（CVE-2026-46242）引发安全社区高度关注。该漏洞位于Linux内核默认启用的epoll事件通知子系统中，本质是竞态条件（Race Condition）与释放后使用（Use-After-Free）的组合缺陷。攻击者只需拥有一个低权限本地账户——无需任何特殊能力或提升的权限——通过对epoll文件描述符进行竞态操作触发UAF，破坏内核内存后在内核上下文中获得任意代码执行，最终实现从普通用户到root的完全提权。影响范围极其广泛：内核5.10至6.11的所有版本均受影响，涵盖RHEL/Ubuntu/Debian/SUSE等企业发行版、Fedora/Arch等桌面发行版、容器宿主机和Kubernetes节点、主流云提供商的云VM镜像，以及2021年以来出货的大多数Android设备。在Android设备上，攻击者仅需应用级或ADB Shell访问即可实现root级完全控制，可访问安全元件、凭据存储和密钥库。漏洞发现者指出Bad Epoll与Anthropic Mythos AI模型此前发现的CVE-2026-43074位于相同内核代码段——AI检测到了第一个漏洞却遗漏了这个密切相关的问题。安全公司评估利用可靠性很高，PoC预计数日内公开，Red Hat、Canonical、Google等厂商正在准备协调补丁发布。

影响范围

Linux内核 5.10-6.11 所有版本（企业服务器、桌面发行版、容器/K8s节点、云VM、2021年后出货的Android设备；全球数十亿设备受影响）

修复建议：优先处理多租户服务器和容器宿主机（不受信本地用户与敏感负载共存环境）；监控内核更新邮件列表，待发行版厂商发布补丁后立即应用；临时措施：在暴露窗口期限制关键系统上的本地Shell访问；Android设备管理：企业MDM应在Google发布安全补丁后加速OTA更新；全面审计环境中运行内核5.10+的系统，按多租户和暴露程度排序修复优先级

|  |  |  |
| --- | --- | --- |
| 严重 | CVE-2026-35616 | CVSS 9.1 |

### FortiBleed——FortiClient EMS访问控制漏洞收割超1.1亿凭证·43万防火墙被扫·INC/Lynx勒索软件12+受害者已确认

Orca Security于2026年7月2日发布FortiBleed攻击活动深度分析报告，揭露了一场规模空前的Fortinet凭证窃取行动。攻击者利用FortiClient EMS产品的访问控制漏洞CVE-2026-35616（CVSS 9.1，无需认证）大规模收割FortiGate防火墙管理凭证。攻击手法极具隐蔽性：攻击者在FortiGate设备上部署名为FortigateSniffer的自定义Golang数据包嗅探器，滥用FortiOS原生的diagnose sniffer packet命令被动拦截认证流量，覆盖RADIUS、NTLM、Kerberos等24种协议，不触发传统入侵检测系统。统计数据显示，攻击者已扫描430,000余台面向互联网的FortiGate防火墙，窃取超过1.1亿条凭证，获得409个目标的管理员权限，导致354个组织完全域沦陷，约12,000台设备被部署嗅探器。SOCRadar威胁研究团队将攻击活动溯源至INC Ransom和Lynx RaaS勒索软件组织——攻击者同时登录了两者的勒索谈判面板，受害者数据存在重叠。截至7月7日攻击仍处于活跃状态，已确认12+起勒索软件部署事件，数百端点被加密。受影响行业集中在制造业、科技和物流领域，地域分布在拉美和亚太地区。CISA已于2026年4月6日将CVE-2026-35616列入KEV目录，但大量组织仍未完成修补。

影响范围

FortiClient EMS 7.4.5至7.4.6版本（43万+FortiGate防火墙被扫描；制造业、科技、物流行业重灾区；拉美和亚太地区高发）

修复建议：立即升级FortiClient EMS至7.4.7或更高版本，或为受影响版本应用带外热修复；紧急轮换所有FortiGate管理基础设施凭证（VPN/RADIUS/NTLM/Kerberos/管理员账户）；审计是否存在未经授权的adminin后门管理员账户；将FortiClient EMS端口8013限制为仅可信IP白名单；在所有FortiGate管理接口上启用多因素认证；封锁C2基础设施IP 83.138.53.110及关联Tor出口节点；部署FortigateSniffer入侵指标进行威胁狩猎

|  |  |  |
| --- | --- | --- |
| 高危 | Opera GX P1 | P1最高级 |

### Opera GX浏览器零点击Mod静默安装漏洞——通用CSS注入逐字符窃取Gmail地址·2500万游戏玩家面临数据泄露

2026年7月6日披露的Opera GX浏览器严重漏洞被评为Bug Bounty最高级别P1（赏金5000美元），影响约2500万游戏玩家用户。漏洞利用Opera GX的GX Mod自动安装机制——Mod文件使用.crx格式，安装管道会自动下载并启用Mod且完全不需要用户批准或点击。攻击者只需在恶意网页中加载指向恶意.crx文件的隐藏iframe，Mod即可在数秒内静默安装。由于Mod的CSS会被应用到用户访问的每一个页面（通用CSS注入），攻击者可利用CSS属性选择器逐字符探测页面元素属性值——通过检测匹配时从攻击者服务器加载背景图片的行为，逐字符重建完整数据。研究人员在概念验证中成功从Google账户页面重建了已登录用户的完整Gmail地址（使用3字符片段约15万条CSS规则）。整个过程为完全零点击：受害者访问恶意页面、Mod自动安装、JavaScript重定向浏览器至目标页面、CSS开始泄露数据，整个攻击在用户注意到通知栏并点击移除按钮之前即可完成。该自动安装行为可追溯至2023年Renwa的研究发现，当时Opera修复了地址栏伪造但保留了底层自动安装机制。Opera GX 130.0.5847.89版本已修复此漏洞，Opera声称未发现野外利用痕迹。同日披露的还有隐身模式加载.crx文件导致浏览器崩溃的关联问题，影响范围更广至普通版Opera浏览器但尚未修复。

影响范围

Opera GX浏览器 130.0.5847.89之前所有版本（全球约2500万游戏玩家用户；关联崩溃问题影响普通版Opera浏览器）

修复建议：立即更新Opera GX至130.0.5847.89或更高版本（访问opera://about确认版本）；检查浏览器中是否存在未知的GX Mod并移除；关注普通版Opera浏览器隐身模式崩溃问题的修复进展；建议游戏玩家群体通过官方渠道更新，勿从第三方下载站获取浏览器安装包

|  |  |  |
| --- | --- | --- |
| 高危 | CVE-2026-55115 | CVSS 9.9 |

### UniFi Protect SSRF权限提升 CVSS 9.9——低权限网络用户可提权至完全控制·企业安防监控系统沦陷风险

7月2日披露的Ubiquiti UniFi Protect应用服务端请求伪造漏洞CVE-2026-55115，CVSS评分高达9.9，属于严重级别。攻击者仅需网络访问权限和低权限账户即可利用SSRF漏洞实现权限提升，最终获得对UniFi Protect安防监控系统的完全控制。UniFi Protect是Ubiquiti面向企业和家庭用户的视频监控管理平台，广泛部署于零售、酒店、教育、企业办公等场景。漏洞的攻击向量包括利用SSRF访问内部网络资源、绕过网络隔离、读取云凭证元数据等。虽然该漏洞需要低权限账户作为前提，但在实际部署环境中，UniFi Protect的低权限用户账户通常易于获取。结合此前UniFi产品线频繁曝出的严重漏洞——包括6月披露的UniFi OS三漏洞链CVSS 10.0×3、5月的LiteSpeed cPanel符号链接越权等——建议所有UniFi用户将此视为紧急安全事件处理。Ubiquiti已在最新固件版本中修复此漏洞，具体修复版本号需参见官方安全公告。

影响范围

Ubiquiti UniFi Protect Application受影响版本（零售、酒店、教育、企业办公等场景广泛部署的视频监控管理平台）

修复建议：立即升级UniFi Protect至官方最新修复版本；审计UniFi Protect系统中的低权限账户，移除不必要的账户和访问权限；限制UniFi Protect管理接口仅可信内网IP访问；部署网络分段策略隔离安防监控网络与核心业务网络；关注Ubiquiti官方安全公告获取精确修复版本号

紧急提醒

本期最高优先级两项：BeyondTrust CVE-2026-40138/40139 CVSS 9.2双认证绕过，企业远程支持基础设施面临未授权接管风险，且该产品历史漏洞多次被用于WebShell和后门植入；Linux内核Bad Epoll 0-day CVE-2026-46242 影响所有内核5.10+的服务器和Android设备，补丁仍在开发中，多租户服务器和容器宿主机需立即限制本地Shell访问。FortiBleed凭证窃取行动（CVE-2026-35616）仍在活跃进行中，43万FortiGate防火墙被扫描、1.1亿凭证已泄露，使用Fortinet产品的组织必须立即执行凭证轮换和EMS升级。Opera GX和UniFi Protect漏洞同样不可忽视：前者代表消费者端零点击攻击的新范式，后者延续了Ubiquiti产品线的高危漏洞频发趋势。本期五个漏洞覆盖企业远程访问、操作系统内核、网络安全设备、消费端浏览器和安防监控系统，攻击面极广，建议安全团队按优先级逐项排查修复。

处置建议

1. BeyondTrust Remote Support/PRA用户立即升级至25.3.3或更高版本，审计设备访问日志，扫描是否存在历史后门或WebShell残留

2. Linux服务器管理员立即审计所有运行内核5.10+的系统，多租户环境限制本地Shell访问，密切监控发行版安全公告准备补丁部署

3. Fortinet FortiClient EMS用户立即升级至7.4.7+，紧急轮换所有FortiGate管理基础设施凭证，审计是否存在adminin后门账户

4. Opera GX用户更新至130.0.5847.89或更高版本，检查并移除未知GX Mod

5. UniFi Protect用户升级至官方最新固件，审计低权限账户，部署网络分段隔离安防监控网络

觉得有用？点击右下角**在看**，让更多人看到

探知安全 · 每日推送最新漏洞资讯

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