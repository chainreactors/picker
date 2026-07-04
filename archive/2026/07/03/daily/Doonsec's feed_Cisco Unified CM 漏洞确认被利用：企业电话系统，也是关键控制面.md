---
title: Cisco Unified CM 漏洞确认被利用：企业电话系统，也是关键控制面
url: https://mp.weixin.qq.com/s/gtkkp3txJGE_SVYd4k3UAA
source: Doonsec's feed
date: 2026-07-03
fetch_date: 2026-07-04T05:47:26.567513
---

# Cisco Unified CM 漏洞确认被利用：企业电话系统，也是关键控制面

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/nOo5YmK1PHyHaounXN53Q304icaxkeoqws3wdVuaFGWewbZV96jTvJkriaztEnCIL5VtxsmMexfTmZBg8ia3pdtMjkia72zdiapcLia9pYaG8nicmA/0?wx_fmt=jpeg)

# Cisco Unified CM 漏洞确认被利用：企业电话系统，也是关键控制面

原创

tcode
tcode

字节脉搏实验室

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz_png/nOo5YmK1PHxd9SCSN7yA4kPNdHia9V3W5MSuiaKP99Pm8gTxSTBlxuJ4anJsvS0HyZ7xz293QwciaF5IYq4rUMDWfGAdFPvBHF1DKIwqc5rRlM/640?wx_fmt=png&from=appmsg)

    Cisco 在其安全公告中确认，Unified Communications Manager（Unified CM）及相关环境中的 CVE-2026-20230 已出现活跃利用迹象。BleepingComputer 在 2026 年 7 月 2 日跟进报道，指出 Cisco 已确认攻击者正在利用这一此前已修复的漏洞。加拿大网络安全中心等机构也提醒用户和管理员查看 Cisco 公告并尽快应用更新。

    统一通信系统听上去像“电话系统”，但在现代企业里，它往往不只是打电话。它可能负责呼叫路由、终端注册、通讯录联动、会议能力、管理接口、服务账号与内部网络连接。攻击者如果盯上这类系统，目标未必是偷听电话那么单一，更可能是在寻找一个被安全运营低估的基础设施入口。

核心事实

    CVE-2026-20230 与 Cisco Unified CM / Unified CM SME 相关。Cisco 官方公告显示，该漏洞影响特定部署条件下的统一通信环境，并已提供修复版本。公开报道还提到，相关漏洞曾出现公开概念验证信息，随后 Cisco 确认已观察到活跃利用。

影响分析

    企业语音系统有一个特殊风险：它既关键，又经常“不显眼”。

    很多安全团队会重点盯住域控、邮件、VPN、云控制台和公网 Web 服务，但语音系统、视频会议网关、呼叫中心组件、传真网关等通信基础设施，可能由独立团队维护，补丁节奏也不同。它们通常长期稳定运行，改动窗口少，升级验证复杂，于是容易形成“能不动就不动”的惯性。

    问题在于，攻击者并不会按照组织架构来选择目标。只要某个系统有网络可达性、有服务权限、有管理接口、有日志盲区，它就可能成为被利用的节点。统一通信系统一旦受影响，潜在后果可能包括服务中断、配置被篡改、凭据暴露、内部网络侦察，以及对业务沟通连续性的影响。

![](https://mmbiz.qpic.cn/mmbiz_png/nOo5YmK1PHxibfTT6BHGYOGGkWApukbspgxv32t95u7JJ2C0Fp5wfyYG7mA9sotxNj2xf97PwQmdNfeCLpKDPJ2DYiaQIiaQxibVicWHFMhT7jwQ/640?wx_fmt=png&from=appmsg)

企业应对建议

    第一，建立统一通信资产清单。确认是否使用 Cisco Unified CM、Unified CM SME 或相关组件，记录版本、部署位置、管理接口暴露范围、服务启用情况和负责人。

    第二，按 Cisco 官方安全公告核对修复版本。不要只看主版本号，应确认具体维护版本、补丁包和受影响组件。涉及通信系统的升级，应提前安排业务验证窗口，但不应无限期拖延。

    第三，收紧访问面。管理接口、服务接口和后台组件不应暴露给不必要的网络区域。对能访问这些系统的源地址、账号、跳板机和运维通道做最小化控制。

    第四，回溯日志与配置变化。关注异常管理访问、异常服务行为、未知配置变更、非计划重启、异常出站连接和安全设备告警。若日志不足，应优先补齐，而不是等下一次事件再补。

    第五，把通信系统纳入漏洞管理例会。统一通信、视频会议和呼叫中心不应游离在补丁治理之外。它们服务的是业务沟通，本身也应被视为关键业务系统。

事实、推测与观点区分

    事实：Cisco 官方公告确认 CVE-2026-20230 已出现活跃利用；BleepingComputer 在 2026 年 7 月 2 日报道了 Cisco 对该利用情况的确认；相关机构建议用户和管理员应用必要更新。

    推测：公开信息不足以判断攻击规模、攻击者身份或是否已形成大规模自动化利用，因此不宜在没有证据的情况下做归因。

    观点：企业对“电话系统”的安全认知需要升级。今天的统一通信平台已经是关键控制面的一部分，不应被看成只要能通话就算安全的后台系统。

结语

    真正成熟的安全管理，不是只盯最热门的漏洞，而是知道哪些“安静运行的系统”正在支撑业务。Cisco Unified CM 事件提醒我们：攻击者会寻找被低估的入口，防守者也要把资产视野从传统边界扩展到每一类关键基础设施。

关键来源

• Cisco Security Advisory，Cisco Unified Communications Manager Server-Side Request Forgery Vulnerability，2026-06 更新并确认活跃利用：https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-cucm-ssrf-cXPnHcW

• BleepingComputer，2026-07-02，Cisco finally confirms attackers exploiting Unified CM flaw：https://www.bleepingcomputer.com/news/security/cisco-finally-confirms-attackers-exploiting-unified-cm-flaw/

• Canadian Centre for Cyber Security，Cisco security advisory AV26-547 Update 1：https://www.cyber.gc.ca/en/alerts-advisories/cisco-security-advisory-av26-547

• NVD，CVE-2026-20230：https://nvd.nist.gov/vuln/detail/CVE-2026-20230

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/ia3Is12pQKnIPvX43Bm5RTfn38gGrVIvGtiaMrLfFqknYBzOd4wmQb1Ra7InwkMM5Ru09FTZ6ibhcLiagpiannxZdlA/0?wx_fmt=png)

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