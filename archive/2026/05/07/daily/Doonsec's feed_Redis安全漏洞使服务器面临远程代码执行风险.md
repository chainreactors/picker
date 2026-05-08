---
title: Redis安全漏洞使服务器面临远程代码执行风险
url: https://mp.weixin.qq.com/s/QZeZEgJpfixnzFgeV3OF1g
source: Doonsec's feed
date: 2026-05-07
fetch_date: 2026-05-08T04:52:29.459211
---

# Redis安全漏洞使服务器面临远程代码执行风险

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/BicXBAdicJy7O5DvZZPb8upRL1SUiaUkOCyKwbiayD9IkTluFpbBiagq9VzVDY6ZKKGsTRnr5LATQTNggOKFTNggesxVdVOia2Wp1jibTHg69rbs9I/0?wx_fmt=jpeg)

# Redis安全漏洞使服务器面临远程代码执行风险

原创

网络安全9527
网络安全9527

安全圈的那点事儿

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

Redis 已披露并修复了五个安全漏洞，其中四个被评为高危漏洞，这些漏洞可能允许经过身份验证的攻击者在受影响的 Redis 服务器上实现远程代码执行 (RCE)。

该安全公告由 Redis 首席信息安全官 Riaz Lakhani 于 2026 年 5 月 5 日发布，涵盖了 CVE-2026-23479、CVE-2026-25243、CVE-2026-25588、CVE-2026-25589 和 CVE-2026-23631。

## **Redis安全漏洞暴露服务器**

CVE-2026-23479 的 CVSS 评分为 7.7（高危），涉及 Redis 的 unblock 客户端流程中的释放后使用漏洞。

当被阻塞的客户端在重新执行被阻塞的命令时被驱逐，已认证用户可能会触发内存损坏，进而导致远程代码执行。根本原因是 processCommandAndResetClient 函数中的错误处理不当。

CVE-2026-25243，评分为7.7（高危），影响Redis RESTORE命令。已认证用户可以提供精心构造的序列化有效载荷来触发无效的内存访问，从而可能导致任意代码执行。

成功利用该漏洞可能导致系统完全被攻陷、数据被窃取或服务中断。

CVE-2026-25588 和 CVE-2026-25589 的评级均为 7.7（高危），并将RESTORE 命令漏洞扩展到 Redis 模块。CVE-2026-25588 影响 RedisTimeSeries 模块，而 CVE-2026-25589 影响 RedisBloom 模块。

在这两种情况下，经过身份验证的攻击者都可以构造恶意序列化的有效载荷，以触发无效的内存访问，并在 Redis 服务器的上下文中实现远程代码执行 (RCE)。

CVE-2026-23631，评级为 6.1（中等），是一个 Lua 释放后使用漏洞。已认证的用户可以利用主从同步机制触发内存损坏，从而可能导致远程代码执行。

此缺陷专门影响配置了只读功能的 Redis 副本，并且存在于所有启用了 Lua 脚本的 Redis 版本中。

多个独立研究人员和安全团队发现了这些漏洞，其中一些是通过 Wiz ZeroDay.Cloud 平台发现的。CVE-2026-23479 由 Xint Code 团队（Tim Becker、Jacob Newman 和 Juno IM）报告。

CVE-2026-25243 的发现来自 Emil Lerner（双重释放漏洞）和 Joseph Surin（整数溢出和越界读取漏洞）。CVE-2026-25588 由 Team Skateboarding Dog（Joseph Surin、John Stephenson 和 Annie Nie）发现。Daniel Firer 和 Joseph Surin 报告了 CVE-2026-25589，而 Yoni Sherez 发现了 CVE-2026-23631。

**受影响版本及修复方案**

所有五个 CVE 漏洞均影响 Redis OSS/CE 和 Redis Software 版本，最高版本为 8.0.6（含 8.0.6）。已修复的版本包括 Redis OSS/CE 版本 6.2.22、7.2.14、7.4.9、8.2.6、8.4.3 和 8.6.3。对于 Redis Software，已修补的版本包括 8.0.10-64、7.22.2-79、7.8.6-253、7.4.6-279 和 7.2.4-153。

RedisTimeSeries v1.12.14/v1.10.24/v1.8.23 和 RedisBloom v2.8.20/v2.6.28/v2.4.23 中提供了模块特定的修复程序。Redis Cloud 客户已受到保护，补丁程序已自动部署。

所有自行管理的 Redis 部署都应立即升级到修复版本。其他最佳实践包括：使用防火墙和网络策略限制网络访问、强制执行强身份验证、启用保护模式、将用户权限限制为仅必要的命令，以及监控异常行为，例如意外的服务器崩溃、未知命令执行或 Redis 数据库的异常网络流量。

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/pcgSUGCDdKJ7zaD2SCDB9F4cHqDTEwJ6wULzhqNKntCMGN2NHYIx7TEicwiaxRTcQaBahVjqwpL96mEw0LBVMRAA/0?wx_fmt=png)

安全圈的那点事儿

向上滑动看下一个

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/pcgSUGCDdKJ7zaD2SCDB9F4cHqDTEwJ6wULzhqNKntCMGN2NHYIx7TEicwiaxRTcQaBahVjqwpL96mEw0LBVMRAA/0?wx_fmt=png)

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