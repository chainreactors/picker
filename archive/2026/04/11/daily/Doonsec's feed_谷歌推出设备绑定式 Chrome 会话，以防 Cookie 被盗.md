---
title: 谷歌推出设备绑定式 Chrome 会话，以防 Cookie 被盗
url: https://mp.weixin.qq.com/s/SncRrQA3WN8BjldTdPDDSA
source: Doonsec's feed
date: 2026-04-11
fetch_date: 2026-04-12T04:42:44.007223
---

# 谷歌推出设备绑定式 Chrome 会话，以防 Cookie 被盗

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/BicXBAdicJy7PYribIX6ELuHZYywaJriaeicicDWLNxqibiaEu21RNLwN93jT87VhichS2IFtcTMicHhTFZcqp2pkLicEYKBGFib6zOlTHLqzWY1yWiboQ6M/0?wx_fmt=jpeg)

# 谷歌推出设备绑定式 Chrome 会话，以防 Cookie 被盗

原创

网络安全9527
网络安全9527

安全圈的那点事儿

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

Google 正式宣布在 Chrome 146 版本中面向 Windows 用户推出设备绑定会话C凭据(DBSC)。

据谷歌帐户安全和 Chrome 团队称，此次重大安全更新旨在消除会话劫持，这是攻击者入侵用户帐户的主要方法之一。

该功能还将在即将发布的 macOS 版本中扩展到 macOS，标志着行业从被动威胁检测向主动预防发生了重大转变。

## **Cookie 数据泄露的威胁**

会话窃取通常发生在用户意外下载了窃取信息的恶意软件，例如 LummaC2 系列。一旦进入系统，该恶意软件就会寻找存储在浏览器本地文件中的现有会话 cookie。

由于身份验证 cookie 通常有效期很长，攻击者可以窃取它们来完全绕过密码。过去，仅靠软件几乎不可能阻止恶意软件读取浏览器内存，这迫使安全团队在安全漏洞发生后依赖复杂的检测方法。

![](https://mmbiz.qpic.cn/mmbiz_png/BicXBAdicJy7NykGdaVEqUic3IyMXCBibgEFs45yUDYA0yicEDIwo9GCjwyzWvaRP6rXicjdtLMRH10vTOWoSHPiazyqEy22zctLsYic0HoOPzQDhias/640?wx_fmt=png&from=appmsg)

DBSC 通过将身份验证会话与用户的物理设备绑定，从根本上改变了 Web 安全。该协议依赖于硬件支持的安全模块，例如Windows 上的可信平台模块 (TPM)或 Apple 设备上的安全隔离区。

用户登录时，硬件会生成一个唯一的公钥/私钥对。至关重要的是，私钥永远无法从机器中导出。升级后端以支持DBSC的网站会发出有效期很短的cookie，Chrome必须不断证明其持有私钥才能刷新这些cookie。

如果黑客窃取了会话 cookie，凭据会迅速过期失效，因为攻击者没有受害者的物理硬件密钥。Web开发人员可以无缝实现此功能，因为浏览器会在后台处理复杂的加密操作。

尽管DBSC具有严格的设备绑定功能，但它在设计之初就融入了严密的隐私控制。该协议为每个会话使用完全独立的密钥。

这确保网站无法利用该技术追踪用户在不同网站上的活动或关联其浏览行为。此外，它仅共享证明持有该设备所需的最低限度数据，从而防止该工具被滥用于设备指纹识别。

谷歌与 W3C Web 应用安全工作组共同开发了 DBSC，将其作为一项开放的 Web 标准，并与微软紧密合作，在 Okta 等平台上进行了试验。展望未来，谷歌计划扩展 DBSC 的功能，以保护企业的联合身份和单点登录 (SSO) 环境。

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