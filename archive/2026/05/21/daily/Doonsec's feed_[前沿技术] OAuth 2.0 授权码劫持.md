---
title: [前沿技术] OAuth 2.0 授权码劫持
url: https://mp.weixin.qq.com/s/1EAxFUpvo4zAV6Vb2NqJCA
source: Doonsec's feed
date: 2026-05-21
fetch_date: 2026-05-22T06:03:36.639050
---

# [前沿技术] OAuth 2.0 授权码劫持

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/BasqgWRklkQGh8mn9QxcNZHT4xCRezTicqHLmkOgRbEaDicLtNNbY02ibCnDVRb7HskGygwOIRCSQrKeE4g87JUuhwUVsz5uuc9L13zF6u8btQ/0?wx_fmt=jpeg)

# [前沿技术] OAuth 2.0 授权码劫持

原创

Pik安全实验室
Pik安全实验室

Pik安全实验室

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

0x00 介绍

OAuth 2.0 是互联网最广泛使用的授权框架，Google、Facebook、GitHub 等全部基于它构建第三方登录。然而配置错误可导致严重的账户劫持——攻击者获取用户的授权码或 Token，以受害者身份登录。本文梳理 OAuth 2.0 的关键攻击面。

0x01 OAuth 流程回顾

Authorization Code Flow: 用户→Client→Authorization Server→重定向→Client用code换token。

0x02 攻击手法

redirect\_uri 劫持

最常见的 OAuth 漏洞。如果服务端未严格校验 redirect\_uri，攻击者可劫持授权码。

# 正常流程
GET /authorize?client\_id=app&redirect\_uri=https://app.com/callback

# 攻击: 篡改 redirect\_uri
GET /authorize?client\_id=app&redirect\_uri=https://evil.com/callback
→ 授权码发到攻击者服务器

# 绕过手法
redirect\_uri=https://app.com.evil.com/callback    # 子域名
redirect\_uri=https://app.com@evil.com/callback     # @ 解析差异
redirect\_uri=https://app.com/callback?next=@evil.com
redirect\_uri=https://app.com//evil.com/callback

CSRF 绑定绕过

state 参数用来防 CSRF，不校验时攻击者可将自己的授权码绑定到受害者会话。

PKCE 缺失利用

没有 PKCE 的授权码流程，恶意应用可拦截回调获取 code。

scope 提升

攻击者请求比预期更多的 scope，如从 read 提升到 write/delete。

0x03 修复

严格白名单校验 redirect\_uri + 强制 state 参数 + 使用 PKCE + 最小权限 scope。

本文仅作安全研究与学习用途，用于非法行为后果自行承担。

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/RBwZuZBV3fSt1n0yS8EEGgiaDF2WgPfMeiaGOMly1wWQQUlwiclwJDFJAZFGmeSroT0oLpGETAeKwiaPBeY1whYoOA/0?wx_fmt=png)

Pik安全实验室

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/RBwZuZBV3fSt1n0yS8EEGgiaDF2WgPfMeiaGOMly1wWQQUlwiclwJDFJAZFGmeSroT0oLpGETAeKwiaPBeY1whYoOA/0?wx_fmt=png)

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