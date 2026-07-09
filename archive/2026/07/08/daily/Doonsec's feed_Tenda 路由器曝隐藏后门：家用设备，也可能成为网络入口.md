---
title: Tenda 路由器曝隐藏后门：家用设备，也可能成为网络入口
url: https://mp.weixin.qq.com/s/yTbQPIUhiivKhsskBQXntQ
source: Doonsec's feed
date: 2026-07-08
fetch_date: 2026-07-09T05:57:29.376994
---

# Tenda 路由器曝隐藏后门：家用设备，也可能成为网络入口

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/nOo5YmK1PHyCuMWAuVpUnwt8eiaWN14ABDia4k0qmxmyzOHVWYc32rJmrcdBhibm6vqAk96p83I4y502vqO0NWzJgVVwUSUGHT7WnJrLvxguts/0?wx_fmt=jpeg)

# Tenda 路由器曝隐藏后门：家用设备，也可能成为网络入口

原创

tcode
tcode

字节脉搏实验室

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/sz_mmbiz_png/nOo5YmK1PHwBHwre7hKypaaM6OJ9M0bd8WUnKuBTAVZ3HzgNnQLhCibVGvQL5IUf9q4PIQdcVQp9HsunoTzxdgrSkRBaltSp9Q6kbWOgosnY/640?wx_fmt=png&from=appmsg)

    很多人对路由器的安全感来自一个误解：它只是一个“联网盒子”，只要 Wi-Fi 能用，就不需要再管。

    现实恰好相反。路由器位于网络入口，一边连接互联网，一边连接家里或办公室的所有终端。它如果被拿下，影响的不只是网速，而是整个网络的信任边界。

    CERT/CC 近日披露的 Tenda 固件隐藏后门问题，就是这个风险的典型案例。

事件概述

    CERT/CC 发布 Vulnerability Note VU#213560，披露 CVE-2026-11405：多个 Tenda 固件版本存在未记录的认证后门，可能使攻击者绕过正常密码校验并获得设备 Web 管理界面的管理员级访问。

    NVD 记录显示，该 CVE 于 2026 年 7 月 6 日发布，并在 7 月 7 日更新。BleepingComputer 于 7 月 7 日跟进报道，指出 CERT/CC 当时称没有可用补丁，并建议用户关闭远程 Web 管理、降低设备被互联网直接触达的机会。

    为避免传播可复现的攻击细节，本文不列出后门实现细节、配置字段、凭据线索或可用于复现的具体路径。需要核对受影响固件的用户，应直接查看 CERT/CC、NVD 或厂商后续公告。

核心事实

    事实：CVE-2026-11405 涉及 Tenda 多款固件中的未记录认证机制。CERT/CC 将其描述为可导致未授权管理员级访问的认证后门。

    事实：NVD 页面显示该漏洞来源为 CERT/CC，发布日期为 2026 年 7 月 6 日，最后修改时间为 2026 年 7 月 7 日。

    事实：BleepingComputer 报道称，CERT/CC 当时表示没有补丁可用，并建议用户关闭远程 Web 管理面，减少被外部扫描和访问的机会。

    推测：公开披露后，路由器类漏洞通常容易被自动化扫描器、僵尸网络和批量攻击工具关注。这个判断来自同类设备历史风险，不代表 CERT/CC 已确认本次漏洞正在被利用。

    观点：家庭和小微企业网络设备不应被排除在安全管理之外。越是长期在线、少人维护、默认配置多的设备，越需要最小暴露和及时替换策略。

影响分析

    对普通家庭来说，路由器被控制可能带来 DNS 篡改、恶意跳转、弱口令扩散、联网设备被扫描等问题。用户看到的可能只是网页异常、网速变慢、设备频繁掉线，但背后可能是网络入口被修改。

    对小微企业来说，风险更现实。很多门店、办公室、仓库、远程摄像头和收银系统都依赖同一台路由器。一旦管理权限被滥用，攻击者可能修改网络配置、关闭安全功能、开放不必要端口，甚至把设备变成后续攻击的跳板。

    对安全团队来说，难点在资产可见性。企业可能知道服务器和电脑的清单，却未必知道边缘路由器型号、固件版本、远程管理状态和公网可达情况。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/nOo5YmK1PHyq9iag8V9HL7Lxc8ue9pFMRibmQEQo2YCR4Rjsic4bZx9B6qc0jtM8eUqdKoO3IlCjjmyiaercp2XRQodpZBZaCaES4FX1unxJYd8/640?wx_fmt=png&from=appmsg)

普通用户和小微企业应对建议

    1. 先确认设备：查看路由器品牌、型号、固件版本，和 CERT/CC、NVD 公告中的受影响范围进行比对。

    2. 关闭远程管理：如果不是明确需要，不要让路由器管理页面从互联网访问。管理入口应只允许本地可信网络访问。

    3. 关注补丁或替换：如果厂商后续提供修复固件，应按官方渠道升级；如果长期没有修复，且设备承担关键网络入口角色，应考虑替换。

    4. 修改默认配置：更改默认管理口令，关闭不必要服务，检查 DNS、端口转发、UPnP、动态 DNS、远程协助等配置是否异常。

    5. 降低本地暴露：对办公环境可将路由器管理网段和业务终端隔离，避免任意终端都能访问管理面。

    6. 做一次网络体检：检查近期是否出现未知设备、未知端口映射、DNS 被改、管理员登录记录异常、Wi-Fi 名称或加密方式被修改等情况。

结语

    路由器不是一次性家电，而是长期暴露在网络边界上的小型计算设备。

    这次 Tenda 固件后门事件提醒我们：网络入口的安全，不只属于大企业，也属于每个家庭、门店和小办公室。最有效的第一步并不复杂：确认型号、关闭远程管理、关注补丁，不可修就替换。

关键来源

• CERT/CC Vulnerability Note VU#213560，CVE-2026-11405：https://kb.cert.org/vuls/id/213560

• NVD，CVE-2026-11405，Published Date：2026-07-06，Last Modified：2026-07-07：https://nvd.nist.gov/vuln/detail/CVE-2026-11405

• BleepingComputer，2026-07-07 01:27 PM，Hidden backdoor in Tenda router firmware grants admin access：https://www.bleepingcomputer.com/news/security/hidden-backdoor-in-tenda-router-firmware-grants-admin-access/

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