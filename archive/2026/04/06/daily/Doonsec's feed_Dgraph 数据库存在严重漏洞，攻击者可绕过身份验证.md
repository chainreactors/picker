---
title: Dgraph 数据库存在严重漏洞，攻击者可绕过身份验证
url: https://mp.weixin.qq.com/s/4XBkiguahhoy1ma2tRzRgA
source: Doonsec's feed
date: 2026-04-06
fetch_date: 2026-04-07T04:26:30.426651
---

# Dgraph 数据库存在严重漏洞，攻击者可绕过身份验证

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/BicXBAdicJy7N18d02fD9icyRy0EhMFSG1ehK2cwrRXFT52nwCtp7iccJbIa0dtBia7QYj62EmBMKJb2PE8goMDibkxj2Qe2s6mQGmjMu9pibPPfFo/0?wx_fmt=jpeg)

# Dgraph 数据库存在严重漏洞，攻击者可绕过身份验证

原创

网络安全9527
网络安全9527

安全圈的那点事儿

![]()

在小说阅读器中沉浸阅读

开源 Dgraph 数据库系统新发现的一个严重漏洞使服务器容易受到完全系统接管。

该漏洞编号为 CVE-2026-34976，最高 CVSS 评分为 10.0。此授权漏洞允许远程未经身份验证的攻击者覆盖数据库、读取敏感服务器文件并发起服务器端请求伪造 (SSRF)攻击。

目前，所有 Dgraph 版本（最高至 v25.3.0）均受到影响，官方尚未发布修复补丁。

该漏洞源于数据库访问控制配置中的一个简单疏忽。

在 Dgraph 中，管理命令通常受到安全中间件的保护，该中间件会强制执行身份验证、IP 白名单和审计日志记录。

虽然标准的恢复命令受到了安全保护，但一项类似的管理操作 `restoreTenant` 却意外地从受保护列表中遗漏了。

由于该命令跳过了所有安全检查，任何能够访问服务器管理网络端点的人都可以执行它。

攻击者无需任何凭证、安全令牌或事先的系统访问权限即可攻破数据库。

安全研究员 Koda Reef 发现，暴露的 `restoreTenant` 函数接受外部 URL 来处理数据库备份。这一漏洞导致多种破坏性极强的攻击途径：

* 当攻击者在公共云存储桶上托管恶意备份文件，并将易受攻击的命令指向该文件时，就会发生数据库覆盖，迫使 Dgraph 将现有数据库替换为攻击者控制的数据。
* 本地文件探测是通过标准文件路径请求实现的，服务器返回的详细错误消息会揭示敏感系统目录的内容。
* SSRF 攻击通过向命令提供内部 IP 地址发起，迫使数据库服务器与受限的内部服务交互或泄露云环境元数据。
* 由于该命令可以被操纵以不当读取内部 Kubernetes 服务帐户令牌或系统密码文件，因此凭证窃取是可能的。

由于目前没有可用的补丁版本，使用 Dgraph 的组织必须依赖临时变通方法或源代码修改。

永久性的代码级修复需要将变更添加 `restoreTenant` 到数据库的管理中间件映射中，这样就能立即恢复标准身份验证检查。

在官方发布安全更新之前，强烈建议管理员严格限制对 Dgraph 管理端点的网络访问。

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