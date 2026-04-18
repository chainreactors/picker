---
title: Windows截图工具漏洞允许攻击者通过网络执行欺骗操作
url: https://mp.weixin.qq.com/s/TOFhVZjiVT9H5f3HsePOyQ
source: Doonsec's feed
date: 2026-04-17
fetch_date: 2026-04-18T04:26:09.073296
---

# Windows截图工具漏洞允许攻击者通过网络执行欺骗操作

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/BicXBAdicJy7Mia3HvIETTySdjK0fdAibHKU6OsKs28bxWQgvW5g12lpcGJ7F3mJib8mlolPHlG0Y0hsMgPxcj0dRzjbKBABqRk29o2ibHOSSyNJI/0?wx_fmt=jpeg)

# Windows截图工具漏洞允许攻击者通过网络执行欺骗操作

原创

网络安全9527
网络安全9527

安全圈的那点事儿

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

微软已修复 Windows 截图工具中一个中等严重程度的安全漏洞，该漏洞可能允许恶意行为者窃取用户凭据。

该欺骗漏洞编号为 CVE-2026-33829，已于 2026 年 4 月 14 日的安全更新中正式修复。

该漏洞由 Blackarrow（Tarlogic）的安全研究人员发现并报告，凸显了Windows 环境中应用程序 URL 处理程序持续存在的风险。

CVE-2026-33829 的 CVSS 3.1 评分为 4.3，被归类为向未经授权的参与者暴露敏感信息 (CWE-200)。

该漏洞存在于 Windows 截图工具处理深度链接的方式中。具体来说，该应用程序在 `ms-screensketch` 正确处理 URI 架构时未能验证输入。

根据微软和 Blackarrow 提供的漏洞披露信息，攻击者可以利用此弱点强制建立经过身份验证的服务器消息块 (SMB) 连接，连接到远程的、攻击者控制的服务器。

## **欺骗漏洞暴露了截图工具**

虽然该漏洞利用需要用户交互，但攻击复杂度较低。以下是基于已发布的概念验证的攻击链运作方式：

* **恶意链接创建：**攻击者使用该参数构造特定的网页链接 `ms-screensketch: edit` 。
* **欺骗性路由：**该链接将 filePath 参数指向恶意外部 SMB 服务器。
* **用户交互：**攻击者诱骗受害者点击钓鱼邮件或被入侵网站上的链接，提示用户确认启动截图工具程序。
* **哈希窃取：**一旦获得批准，截图工具就会连接到远程服务器以获取伪造文件，在后台悄悄泄露用户的 NTLMv2 密码哈希值。
* **未经授权的访问：**攻击者捕获此哈希值，并可利用它在网络上以被入侵用户的身份进行身份验证。

安全专家警告称，这种漏洞极易被用于社交工程攻击。攻击者可以发送看似合法的网页，诱骗用户裁剪公司壁纸或编辑工牌照片。

虽然截图工具会在用户的屏幕上正常打开，使请求看起来无害，但NTLM 身份验证却是在不可见的情况下进行的。

虽然成功利用漏洞会导致机密性丧失，但攻击者无法更改数据（完整性）或使系统崩溃（可用性）。

微软指出，该漏洞利用代码的成熟度目前尚未得到证实，实际利用的可能性仍然“很低”。目前尚无任何关于该漏洞被实际利用的报告。

## **受影响的系统**

该漏洞的详细信息已发布在 GitHub 上，它会影响各种 Microsoft 操作系统，包括 2012 年至 2025 年的多个版本的 Windows 10、Windows 11 和 Windows Server。

为保护网络免受 CVE-2026-33829 的攻击，组织应实施以下缓解策略：

* 立即应用微软于 2026 年 4 月 14 日发布的官方安全补丁。
* 在网络边界阻止出站 SMB 流量（端口 445），以防止 NTLM 哈希与外部服务器通信。
* 教育员工了解点击未知链接和不加质疑地批准网络浏览器应用程序启动提示的危险性。

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