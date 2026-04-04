---
title: TP-Link 多个漏洞使攻击者能够触发拒绝服务攻击并导致路由器崩溃
url: https://mp.weixin.qq.com/s/Pkn3e0RZ3ZNYV7iPhWPLmw
source: Doonsec's feed
date: 2026-04-03
fetch_date: 2026-04-04T04:12:08.668240
---

# TP-Link 多个漏洞使攻击者能够触发拒绝服务攻击并导致路由器崩溃

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/BicXBAdicJy7OjmTohK58LU4aArzoiaENAHNicjeTJPllpeUf1tHaZLSbWDZ5pToOfWC4jfjZUiaH3LMyqUFUxYb54bJSR0nq0aDuNWmpBhRQ4wY/0?wx_fmt=jpeg)

# TP-Link 多个漏洞使攻击者能够触发拒绝服务攻击并导致路由器崩溃

原创

网络安全9527
网络安全9527

安全圈的那点事儿

![]()

在小说阅读器中沉浸阅读

TP-Link Tapo C520WS 智能安防摄像头存在多个高危漏洞。如果这些漏洞被利用，攻击者可能触发拒绝服务 (DoS) 攻击、导致设备崩溃或完全绕过身份验证。

TP-Link 已发布紧急固件更新以解决这些关键的安全漏洞。当安全摄像头或连接的路由器因拒绝服务攻击而离线时，会立即造成物理安全盲区。

因此，对于依赖 Tapo C520WS 进行主动监控和财产监控的用户来说，修补这些漏洞尤为重要。

## **TP-Link 的多个漏洞**

已发现的漏洞中最严重的是 CVE-2026-34121，其 CVSS v4.0 评分为 8.7。此漏洞涉及摄像头 DS 配置服务的 HTTP 处理中的身份验证绕过。

由于 JSON 请求中解析和授权逻辑不一致，同一网段上的未经身份验证的攻击者可以很容易地绕过安全检查。

通过在特权请求中附加豁免操作，黑客可以执行受限配置更改并改变设备状态，而无需有效的登录凭据。

除了身份验证绕过漏洞外，研究人员还发现了几个缓冲区溢出漏洞，这些漏洞可被利用来使设备崩溃或强制突然重启，从而导致完全拒绝服务。

**CVE-2026-34118、CVE-2026-34119、CVE-2026-34120：**这些基于堆的溢出缺陷（CVSS 7.1）源于 HTTP 和流式输入中糟糕的边界验证。

攻击者可以发送精心构造的有效载荷，导致HTTP POST 解析、分段请求追加或异步视频流处理期间内存损坏。

**CVE-2026-34122：**在 DS 配置服务中发现的此基于堆栈的溢出漏洞（CVSS 7.1）允许攻击者提供过长的配置参数来使服务崩溃。

**CVE-2026-34124：**此路径扩展溢出漏洞的 CVSS 评级为 7.1，发生在 HTTP 请求解析逻辑中。

系统会检查原始请求长度，但无法考虑路径规范化期间的大小增加，从而允许相邻攻击者触发系统中断。

这些漏洞专门影响运行固件版本低于 1.2.4 Build 260326 Rel. 24666n 的 Tapo C520WS v2.6。

强烈建议用户立即应用最新的固件补丁。设备未打补丁会导致未经 授权的配置更改和持续崩溃。

您可以直接从 TP-Link 官方支持页面下载更新后的固件，或在配套的移动应用程序中检查更新。TP-Link 指出，如果忽略这些更新，由此造成的安全后果，他们概不负责。

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