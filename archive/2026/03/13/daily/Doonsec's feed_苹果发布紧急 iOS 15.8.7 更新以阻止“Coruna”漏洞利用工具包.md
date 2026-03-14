---
title: 苹果发布紧急 iOS 15.8.7 更新以阻止“Coruna”漏洞利用工具包
url: https://mp.weixin.qq.com/s/13lZ6yeDA0uUd26ySWyR4A
source: Doonsec's feed
date: 2026-03-13
fetch_date: 2026-03-14T04:06:12.868271
---

# 苹果发布紧急 iOS 15.8.7 更新以阻止“Coruna”漏洞利用工具包

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/BicXBAdicJy7ObYw14bS49IdKOCYFQEYDuYlCr74xeeLXmibKhDwBmIDyT17Z4VD845vZWW8vpsmtZqOKgYBMrvWPH3TzYiblnv8O8blTTibecxY/0?wx_fmt=jpeg)

# 苹果发布紧急 iOS 15.8.7 更新以阻止“Coruna”漏洞利用工具包

原创

网络安全9527
网络安全9527

安全圈的那点事儿

![]()

在小说阅读器中沉浸阅读

苹果公司推出了紧急安全更新 iOS 15.8.7 和 iPadOS 15.8.7，以保护旧款 iPhone 和 iPad 用户免受名为 Coruna 漏洞利用工具包的复杂威胁。

该关键补丁于 2026 年 3 月 11 日发布，将之前为运行 iOS 16 和 iOS 17 的新设备发布的几个主要安全修复程序向后移植。

由于老旧硬件无法升级到最新的操作系统，苹果偶尔会提供关键更新来修复严重缺陷。

最新版本修复了设备内核和 WebKit 引擎中的四个不同漏洞，攻击者可以将这些漏洞串联起来执行恶意代码并破坏未修补的系统。

## **Coruna漏洞利用工具包威胁**

Coruna漏洞利用工具包利用已知的内存损坏和释放后使用漏洞。

攻击者通过恶意构造的网络内容攻击用户，可以触发这些漏洞，从而绕过安全沙箱。

一旦脱离沙箱，该漏洞就会攻击设备的内核以提升权限，从而使攻击者能够完全控制被入侵的 iPhone 或 iPad。

为了解决这个问题，苹果公司已将四项关键修复程序移植到 iOS 15 生态系统中。

此次更新修复了一个内核漏洞和 WebKit（苹果的浏览器引擎，为 Safari 和所有 iOS 上的第三方浏览器提供支持）中的三个缺陷。修复的漏洞包括：

* **CVE-2023-41974（内核）：** 此漏洞由 Félix Poulin-Bélanger 发现，允许恶意应用程序以最高内核权限执行任意代码。苹果通过改进内存管理解决了此问题。该修复程序最初于 2023 年 9 月在 iOS 17 中发布。
* **CVE-2024-23222（WebKit）：** 一个严重的类型混淆漏洞，恶意构造的网页内容处理可能导致任意代码执行。苹果公司改进了安全检查以修复此漏洞，该漏洞最初于 2024 年 1 月在 iOS 17.3 中针对较新的设备进行了修复。
* **CVE-2023-43000 (WebKit)：** 此漏洞利用了释放后使用（use-after-free）机制，当用户访问恶意网页时，可能导致内存损坏。苹果公司通过改进内存管理缓解了此威胁。该补丁于 2023 年 7 月首次随 iOS 16.6 发布。
* **CVE-2023-43010（WebKit）：** 另一个与处理恶意网页内容相关的内存处理问题，也可能导致内存损坏。此问题已通过改进内存处理得到解决，最初于 2023 年 12 月在 iOS 17.2 中修复。

## **受影响的设备**

此紧急更新专为不再符合 iOS 主线更新条件的旧款苹果设备而设计。受影响的设备包括：

* iPhone 6s（所有型号）。
* iPhone 7（所有型号）。
* iPhone SE（第一代）。
* iPad Air 2。
* iPad mini（第四代）。
* iPod touch（第七代）。

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