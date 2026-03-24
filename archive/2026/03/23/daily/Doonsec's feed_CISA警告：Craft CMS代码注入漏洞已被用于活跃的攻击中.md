---
title: CISA警告：Craft CMS代码注入漏洞已被用于活跃的攻击中
url: https://mp.weixin.qq.com/s/XUZN6YN-AYSxRNpVRh7bJg
source: Doonsec's feed
date: 2026-03-23
fetch_date: 2026-03-24T04:13:35.561183
---

# CISA警告：Craft CMS代码注入漏洞已被用于活跃的攻击中

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/BicXBAdicJy7NCAicgib6ibHp35lDgNeOFLlc2ozSjNOTILZ4R66zlq3ewxf8jf471PARiaNQvj875sbVV04ddPB4vapLxvklRn4mWWM9RTFv8zTc/0?wx_fmt=jpeg)

# CISA警告：Craft CMS代码注入漏洞已被用于活跃的攻击中

原创

网络安全9527
网络安全9527

安全圈的那点事儿

![]()

在小说阅读器中沉浸阅读

美国网络安全和基础设施安全局 (CISA) 已正式将影响 Craft CMS 的一个严重漏洞添加到其已知利用漏洞 (KEV) 目录中。

该代码注入漏洞被追踪为 CVE-2025-32432，目前正被广泛用于各种攻击中。

使用此内容管理系统的组织应立即采取缓解措施，以防止潜在的系统安全漏洞。

CVE-2025-32432是在事件响应调查中发现的，其 CVSS v3.1 严重性评分最高为 10.0，被标记为严重威胁。

该漏洞允许未经身份验证的远程攻击者在受影响的服务器上执行任意代码。

这种高影响、低复杂度的攻击向量会影响 Craft CMS 的多个主要版本，特别是 3.x、4.x 和 5.x 版本分支。

根本原因在于对不受信任的输入处理不当，根据 CWE-94 分类，这是代码生成控制不当的问题。

从技术角度来看，该漏洞利用了 Craft CMS 资产转换生成功能中不安全的反序列化问题。

攻击者可以利用这一点，注入一个自定义的 PHP 对象，该对象会被应用程序不安全地反序列化。

该攻击链涉及通过精心构造的 URL 请求将恶意 PHP 有效载荷植入会话文件中。

接下来，攻击者利用 Yii 框架的行为小工具链，攻击 generate-transform 端点上的 PhpManager 组件。

攻击者利用对象注入技术，强迫应用程序处理被污染的文件，从而执行注入的代码，并赋予攻击者完全的远程代码执行能力。

目前尚不清楚勒索软件组织是否正在利用此漏洞进行勒索活动。

然而，该漏洞的预认证特性以及概念验证漏洞的可用性，使其成为威胁行为者的理想目标。

防御者应积极监控环境，以发现未经授权的 webshell 部署或可疑的反向 shell 连接，这些都是成功入侵后常见的后渗透活动。

为了缓解这一严重威胁，开发人员发布了安全更新，解决了不安全的反序列化漏洞。

该漏洞影响 Craft CMS 版本，范围从 3.0.0 到 3.9.14，4.0.0 到 4.14.14，以及 5.0.0 到 5.6.16。

管理员必须尽快将安装升级到已修补的版本，其中包括 3.9.15、4.14.15 和 5.6.17 版本。

这些更新也对之前记录在案的漏洞 CVE-2023-41892 进行了额外的修复。

根据具有约束力的操作指令 (BOD) 22-01，联邦民事行政部门机构有义务保护其网络免受这种特定威胁。

CISA 于 2026 年 3 月 20 日正式将此漏洞添加到 KEV 目录中，并设定了严格的补救期限，即 2026 年 4 月 3 日。

所有组织都应使用 KEV 目录来确定漏洞管理的优先级。管理员必须应用供应商补丁、遵循云服务指南，或者在无法立即采取缓解措施的情况下停止使用产品。

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