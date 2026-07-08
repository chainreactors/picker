---
title: BeyondTrust 修复了远程支持和 PRA 中的关键身份验证绕过漏洞
url: https://mp.weixin.qq.com/s/h__oS3_urFF3uKcCpj-W4Q
source: Doonsec's feed
date: 2026-07-07
fetch_date: 2026-07-08T05:01:10.932945
---

# BeyondTrust 修复了远程支持和 PRA 中的关键身份验证绕过漏洞

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/BicXBAdicJy7MnrZBib9fcBY3JY04vQnicvyNTknCfXEZiaQ5aWf70Dy58o7BuSSx6O3ic6eKQXKiciciayUGAbHiaqpbMfmOqgKSyXTWjMtFHf6p5ncs/0?wx_fmt=jpeg)

# BeyondTrust 修复了远程支持和 PRA 中的关键身份验证绕过漏洞

原创

网络安全9527
网络安全9527

安全圈的那点事儿

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

BeyondTrust 发布了更新，以解决影响远程支持 (RS) 和特权远程访问 (PRA) 产品的两个严重安全漏洞。如果这些漏洞被成功利用，未经身份验证的攻击者可能会控制易受攻击的设备。

漏洞列表如下：

* **CVE-2026-40138**（CVSS 评分：9.2）- BeyondTrust Remote Support 和 Privileged Remote Access 的身份验证子系统中存在预身份验证漏洞，该漏洞源于身份验证数据的验证不当，可能允许位于网络中的攻击者绕过访问控制并获得对设备的未经授权的访问权限，包括具有提升权限的账户。
* **CVE-2026-40139**（CVSS 评分：9.2）- BeyondTrust Remote Support 的身份验证子系统中存在预身份验证漏洞，该漏洞源于身份验证请求处理不当，可能允许未经身份验证的远程攻击者绕过访问控制并获得对设备的未经授权的访问权限，包括具有提升权限的账户。
* **CVE-2026-40140**（CVSS 评分：8.7）- 网络通信子系统中的预身份验证漏洞，源于对客户端提供的输入验证不足，可能允许未经身份验证的远程攻击者触发拒绝服务情况，从而影响设备可用性。
* **CVE-2026-40141**（CVSS 评分：8.5）- BeyondTrust Remote Support and Privileged Remote Access 的 Web 应用程序组件中存在漏洞，该漏洞源于对用户提供的输入验证不足，可能允许权限有限的已认证攻击者访问超出其授权范围的非预期资源或数据。

值得注意的是，CVE-2026-40138 和 CVE-2026-40139 的成功利用取决于是否启用了特定的身份验证配置。而 CVE-2026-40141 的利用（如果发生）仅限于具有特定权限的账户。

BeyondTrust 表示，所有这些漏洞都是在持续的安全评估过程中内部发现的，并借助了公开可用的 AI 模型（如 Anthropic Claude Opus 4.8）及其专有的研究工具。

声明称：“最严重的漏洞可能允许未经身份验证的远程攻击者绕过访问控制，并在特定配置下获得对设备的未经授权的访问权限。其他漏洞可能导致服务中断、意外数据访问，以及在某些特定配置下，已认证用户获得更高的访问权限，从而影响系统完整性。”

这些问题已在以下版本中得到解决——

* 远程支持 RS 25.3.2 或更低版本（已在 RS 25.3.3 及更高版本中修复）
* 特权远程访问 PRA 25.3.2 或更低版本（已在 PRA 25.3.3 及更高版本中修复）

BeyondTrust并未提及目前已被利用的漏洞。然而，RS和PRA产品中的安全漏洞（CVE-2024-12356和CVE-2026-1731）过去曾多次被利用来部署Web Shell和后门，因此用户必须尽快应用修复程序。

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