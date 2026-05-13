---
title: PHP SOAP 扩展存在严重漏洞，可导致远程代码执行攻击
url: https://mp.weixin.qq.com/s/wB1Nto61yY1wymP3O27sYg
source: Doonsec's feed
date: 2026-05-12
fetch_date: 2026-05-13T05:45:13.093105
---

# PHP SOAP 扩展存在严重漏洞，可导致远程代码执行攻击

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/BicXBAdicJy7PLVkGFBpVyv5h5BaqRAzNrM3FMGsxDJOrQXSZBwBW3DKKHpRSWtfKnFYyOwKIXH5yQmJQPIJDZ3S0Mhlc8lAYa6P6jiaP3grtk/0?wx_fmt=jpeg)

# PHP SOAP 扩展存在严重漏洞，可导致远程代码执行攻击

原创

网络安全9527
网络安全9527

安全圈的那点事儿

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

PHP 核心字符串处理和 ext-soap 组件中发现了一系列严重的漏洞，使众多 Web 服务器面临被完全控制的直接风险。

虽然 SOAP 扩展程序在内存损坏缺陷方面有着臭名昭著的历史，但这一最新发现已经越过了红线，构成了未经身份验证的远程代码执行 (RCE)。

GitHub 安全团队现在正与时间赛跑，因为 PHP 维护人员正在部署紧急补丁，以防止攻击者将存在漏洞的服务器变成被攻破的资产。

最严重的漏洞，编号为 CVE-2026-6722，是PHP SOAP 扩展中的一个高危 释放后使用漏洞。

该漏洞源于扩展程序如何处理使用 id 和 href 属性在 XML 图中对对象进行去重的方式。

## **PHP SOAP 的其他缺陷**

解析 XML 文档时，该扩展程序会将纯 PHP 对象存储在全局哈希映射中，但严重地未能增加其引用计数。

通过利用Apache 映射机制，攻击者可以通过覆盖现有的映射条目来故意释放这些对象。

这种内存操作允许攻击者重新利用已释放的内存段，从而导致危险的内存损坏。

正如安全研究员 Brett Gervasoni 所证明的那样，攻击者可以通过随后分配纯字符串来高度控制这部分释放的内存，最终将漏洞升级为完全远程代码执行。

除了 RCE 漏洞之外，PHP 安全团队还通过 GitHub 修复了另外四个中等严重程度的漏洞。

开发者iluuu1994牵头开展了所有新披露漏洞的修复工作。

CVE-2026-7261 涉及 SoapServer 在处理会话持久化对象时存在的另一个释放后使用 (Use-After-Free) 问题。

 如果头节点的处理函数失败或抛出异常，则该对象会被错误地释放，但仍会写入会话存储。

CVE-2026-7262 是一个在 Apache: Map 节点解码过程中触发的空指针解引用漏洞。

攻击者通过发送一个特制的、缺少值节点的 XML 请求，可以持续地使 PHP 进程崩溃，从而导致拒绝服务攻击。

CVE-2026-7258 暴露了原生 urldecode() 函数中的越界读取漏洞。

由于在评估十六进制字符时缺少类型转换，负字节值可能会在某些平台（例如 NetBSD）上导致段错误。

CVE-2026-6104 影响 mbstring 扩展：解析包含嵌入 NUL 字节的编码名称会导致全局缓冲区溢出。

此信息泄露漏洞可以读取超出预期范围的信息，但不能直接利用该漏洞执行代码。

这些漏洞会影响多个正在积极支持的 PHP 分支，包括 SOAP 相关缺陷和 urldecode() 错误。

受影响的版本包括 PHP 8.2.31、8.3.31、8.4.21 和 8.5.6 之前的版本。mbstring 漏洞仅影响 8.4.21 和 8.5.6 之前的版本。

强烈建议管理员立即更新其 PHP 环境。

由 iluuu1994、iliaal 和 ndossche 在 GitHub 上贡献的补丁现已集成到 PHP 版本 8.2.31、8.3.31、8.4.21 和 8.5.6 中。

升级到这些已修补的版本可以安全地解决内存处理错误和越界读取问题，从而保护服务器免受拒绝服务攻击和远程代码执行攻击。

使用 SOAP 扩展的组织必须优先部署此补丁，以充分保护关键基础设施。

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