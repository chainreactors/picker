---
title: BeyondTrust 修复高危认证绕过：远程支持平台，必须按关键资产管理
url: https://mp.weixin.qq.com/s/tUytHq_2maqP1VlBOkQ_jQ
source: Doonsec's feed
date: 2026-07-08
fetch_date: 2026-07-09T05:57:26.484398
---

# BeyondTrust 修复高危认证绕过：远程支持平台，必须按关键资产管理

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/nOo5YmK1PHyfqCGPPWhB39Cx9qbLWewZ6j1QSI78FRBhuMQARux2aTsyclXlM7LuR2RuumcxwfyibkVzJIqaauYiaBqr4ot8cFPuMLIAxQUpU/0?wx_fmt=jpeg)

# BeyondTrust 修复高危认证绕过：远程支持平台，必须按关键资产管理

原创

tcode
tcode

字节脉搏实验室

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz_png/nOo5YmK1PHzXyz6tSIKf6F0VYDYZQZ9SjqZVfpDwjejpqRChV1Lr5ckeb9HZotzhCVamM35sgeicgO4w8AZbY9Dcicnm7jr7Z4WKIm1aXR9eA/640?wx_fmt=png&from=appmsg)

    如果企业里有一类系统最不适合“晚点再补”，远程支持和特权远程访问平台一定排在前面。

    原因很直接：它们不是普通业务系统，而是管理员、运维、服务商进入内部环境的入口。一旦这个入口本身出现认证绕过或权限边界问题，攻击者可能不需要先拿到某个员工账号，就能接近更高价值的管理面。

    7 月 7 日，多家安全媒体跟进 BeyondTrust 官方公告中的 RS 与 PRA 漏洞，就是一个典型提醒。

事件概述

    BeyondTrust 官方安全公告 BT26-03 显示，Remote Support（RS）和 Privileged Remote Access（PRA）受到多项漏洞影响，严重级别从 Critical 到 High 不等。其中最值得优先关注的是两类预认证阶段的认证缺陷，可能导致未认证攻击者在特定配置下绕过访问控制并获得对设备的未授权访问。

    官方公告列出的漏洞包括 CVE-2026-40138、CVE-2026-40139、CVE-2026-40140 和 CVE-2026-40141。BeyondTrust 称这些问题由内部安全研究发现，并表示在修复前没有证据表明已被外部利用。

    从修复信息看，云端客户已由厂商处理；自托管客户需要确认是否已安装相应安全汇总补丁，或升级到 RS/PRA 25.3.3 及以上版本。受影响版本以官方公告为准。

核心事实

    事实：官方公告确认 RS/PRA 受多项漏洞影响，其中 CVE-2026-40138 与 CVE-2026-40139 为 Critical，CVSS v4 分数为 9.2；CVE-2026-40140 与 CVE-2026-40141 为 High。漏洞影响 Remote Support 与 Privileged Remote Access 的认证、网络通信或 Web 组件。

    事实：BleepingComputer 于 2026 年 7 月 7 日跟进报道，强调这类问题涉及远程支持与特权访问平台，若被成功利用，可能造成设备控制权和权限边界风险。

    事实：BeyondTrust 表示没有证据显示这些漏洞在修复前已被利用。这里应避免把“高危”直接写成“已被大规模攻击”。

    推测：由于 RS/PRA 属于远程运维和特权访问入口，公开披露后被扫描、验证和纳入攻击者目标清单的概率较高。这个判断基于同类产品历史被攻击者重点关注的经验，不等同于本次漏洞已有利用证据。

    观点：企业不应只把它当作一次普通漏洞修补，而应把远程运维平台纳入关键资产管理、暴露面管理和特权账号治理。

影响分析

    第一层影响是入口风险。远程支持平台通常连接服务台、运维人员、外部供应商和内部主机。如果该入口出现预认证阶段缺陷，攻击链的前置条件会显著降低。

    第二层影响是横向移动风险。即使攻击者最初只触达一个管理平台，只要平台能够发起远程会话、调用特权账号或访问敏感主机，就可能扩大影响范围。

    第三层影响是审计盲区。很多企业会重点监控 VPN、邮箱、终端告警，却忽视远程运维平台自己的登录、会话、授权变更和插件行为。越是“可信管理工具”，越容易被默认放行。

![](https://mmbiz.qpic.cn/mmbiz_png/nOo5YmK1PHzV2yzOmt103QIuUQT6dwzolAarE76v8lBhCHG4Be1gmcdXNsGf1VdfyZTXjJpsjnv7EFhJQE8fuL6mNCibICmR62PGM9tkzLMg/640?wx_fmt=png&from=appmsg)

企业应对建议

    1. 立即确认资产范围：排查是否使用 BeyondTrust Remote Support 或 Privileged Remote Access，区分云端和自托管部署，核对版本、补丁状态和自动更新状态。

    2. 优先处理自托管实例：按官方公告安装安全汇总补丁，或升级到 RS/PRA 25.3.3 及以上版本。不要只依赖漏洞扫描器的泛化判断，最终以产品控制台和厂商文档为准。

    3. 收紧管理面暴露：远程运维平台不应直接暴露给不受信网络。可通过 VPN、零信任访问、源地址限制、管理网段隔离等方式减少可达面。

    4. 复核特权账号和会话：检查近期是否存在异常登录、异常远程会话、管理员账号变更、策略变更、异常插件或集成调用。

    5. 把远程支持平台纳入高价值系统监控：包括补丁 SLA、配置基线、日志集中、异常会话告警、管理员最小权限和第三方运维账号生命周期管理。

    6. 准备降级方案：如果短期无法升级，应评估是否能临时限制入口、关闭非必要集成、收紧外部访问，避免关键入口长时间处于高风险状态。

结语

    这次事件的重点不是“某个厂商又修了几个漏洞”，而是提醒企业重新审视远程运维平台的位置。

    它们一端连着人，一端连着系统，中间还常常握有高权限。这样的系统一旦出现认证或权限边界问题，影响就不会停留在单点设备上。

    补丁要打，暴露面要收，日志要看，更重要的是把远程支持和特权访问平台当成关键基础设施来管。

关键来源

• BeyondTrust 官方公告 BT26-03，Issue Date：2026-06-21，Updated On：2026-06-21：https://www.beyondtrust.com/trust-center/security-advisories/bt26-03

• BleepingComputer，2026-07-07 04:12 AM，BeyondTrust warns of critical flaws in remote access software：https://www.bleepingcomputer.com/news/security/beyondtrust-warns-of-critical-flaws-in-remote-access-software/

• NVD，CVE-2026-40139：https://nvd.nist.gov/vuln/detail/CVE-2026-40139

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