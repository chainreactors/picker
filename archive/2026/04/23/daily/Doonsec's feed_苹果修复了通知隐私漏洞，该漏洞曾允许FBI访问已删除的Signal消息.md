---
title: 苹果修复了通知隐私漏洞，该漏洞曾允许FBI访问已删除的Signal消息
url: https://mp.weixin.qq.com/s/HMBYweMEslpzOQ8EURKlcA
source: Doonsec's feed
date: 2026-04-23
fetch_date: 2026-04-24T04:52:02.189629
---

# 苹果修复了通知隐私漏洞，该漏洞曾允许FBI访问已删除的Signal消息

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/BicXBAdicJy7MFHU2I6UQkWuiaGxMVu7IePdLB7HYfSe5puiaK8bMU07uNawVaZE0KUemZwhm64vbzzTicP4FutLmv0CibxTbAkdfslBLGdibpja9k/0?wx_fmt=jpeg)

# 苹果修复了通知隐私漏洞，该漏洞曾允许FBI访问已删除的Signal消息

原创

网络安全9527
网络安全9527

安全圈的那点事儿

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

苹果公司于 2026 年 4 月 22 日发布了 iOS 26.4.2 和 iPadOS 26.4.2，以修复一个严重的通知隐私漏洞，该漏洞允许执法部门从 iPhone 中提取 Signal 消息内容——即使在该应用程序已被删除之后。

该漏洞编号为 CVE-2026-28950，源于苹果通知服务中的一个日志记录问题。标记为删除的通知会被意外地保留在设备上，这可能导致敏感消息预览在用户认为已被删除后仍长期存在。苹果通过改进日志框架中的数据脱敏机制解决了这一根本问题。

该漏洞在调查媒体404 Media报道FBI在刑事调查中成功从嫌疑人的iPhone中提取了Signal消息通知内容后引起了公众关注，尽管Signal已从该设备上卸载。保留的通知预览提供了足够的可读内容，对调查人员的取证工作具有重要价值。

## **Signal 称赞苹果的快速响应**

Signal 公开承认了此次修复，并赞扬苹果在问题披露后迅速采取行动。这家加密通讯平台在其 X 平台上发布文章确认，此次更新不仅可以防止已删除应用的通知残留，还会自动清除受影响设备上先前保留的通知数据。

鉴于 Signal 作为隐私保护工具的黄金标准，这一点尤为重要。iOS 自身的通知机制可能会在无意中破坏 Signal在操作系统层面的端到端加密，这一事实凸显了保障设备完整隐私保护体系的复杂性。

此次更新适用于多种苹果硬件：

* iPhone 11 及更新机型
* iPad Pro 12.9 英寸（第三代及更新机型），11 英寸（第一代及更新机型）
* iPad Air 第三代及更新机型
* iPad 第 8 代及更新版本
* iPad mini 第五代及更新版本

使用旧设备的用户可以通过 iOS 18.7.8 和 iPadOS 26.4.2 应用相同的修复程序。

版本号为 23E261 的更新现已推出，大小约为 670–770 MB。请前往“设置”>“常规”>“软件更新”立即安装此补丁。

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