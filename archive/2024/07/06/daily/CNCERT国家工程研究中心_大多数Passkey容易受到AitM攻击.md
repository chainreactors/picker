---
title: 大多数Passkey容易受到AitM攻击
url: https://mp.weixin.qq.com/s?__biz=MzUzNDYxOTA1NA==&mid=2247545707&idx=1&sn=b7e1a5578879f116c9f310253c3ab14e&chksm=fa9385aacde40cbc5503bc9ebd5e76c7641cf9de062e5d80880373b9da994566c3476376e7a6&scene=58&subscene=0#rd
source: CNCERT国家工程研究中心
date: 2024-07-06
fetch_date: 2025-10-06T17:44:07.207201
---

# 大多数Passkey容易受到AitM攻击

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/GoUrACT176l8NiaLjLvFq0Wp8WLicxyjicauM6lhebopa6cEAFkvlO1Gb9hJMdS5trtBfkTSb69ib81Bf24HLMlu5w/0?wx_fmt=jpeg)

# 大多数Passkey容易受到AitM攻击

网络安全应急技术国家工程中心

![](https://mmbiz.qpic.cn/mmbiz_png/GoUrACT176l8NiaLjLvFq0Wp8WLicxyjicaHibFznfEEX9gyWQdQa8Ly7C4EqYCKiaUZogoOJkF7Yk1LzE9asft20yg/640?wx_fmt=png&from=appmsg)

Passkey（通行密钥）是一种流行的无密码技术，多用于验证用户对云托管应用程序的访问。尽管Passkey被寄予厚望，号称密码终结者，但却容易受到中间对手（AitM）攻击。根据eSentire的一项研究，如果Passkey未能正确实施，例如提供不太安全的备份身份验证方法，容易遭受AitM攻击，攻击者通过修改向用户显示的提示来绕过身份验证流程。

# **大多数Passkey实现可被绕过**

“在Passkey仅用作第一因素身份验证方法时，其备份身份验证容易受到AitM攻击，”eSentire威胁响应部门（TRU）的首席安全研究员Joe Stewart在博客文章中指出：“由于AitM可以通过修改登录页面中的HTML、CSS和图像或JavaScript来操纵呈现给用户的视图，当它被代理到最终用户时，他攻击者可以控制身份验证流程并删除对密钥身份验证的所有引用。

这一发现意味着，在无密码密钥身份验证之后被认为更安全的帐户（例如银行、电子商务、社交媒体、云帐户和软件开发平台等在线平台上的帐户）仍然可以被入侵。

Stewart在博客中发布了POC并指出，开源AitM软件（如Evilginx）可用于欺骗GitHub，Microsoft和Google等流行IT服务的用户。

在Evilginx中，可以通过一些编辑（编辑显示文本）来部署特定的Phishlet，即通过从真实登录页面捕获身份验证令牌和会话cookie来启用AitM攻击的脚本，以诱骗用户进行密钥身份验证。

“我们使用了标准的GitHub网络钓鱼进行测试，”Stewart说道：“当目标用户访问诱饵URL时，除了URL栏中的主机名之外，他们看到的钓鱼页面与普通的GitHub登录页面一样，因为它就是真实的GitHub登录页面，只是通过Evilginx代理。”

然而，通过稍微修改网络钓鱼配置，攻击者可以删除“使用Passkey登录”的文本，Stewart补充说，这意味着攻击者可以很容易地诱骗用户选择基于密码的备份身份验证。

该研究指出，对于使用Passkey作为第一因素和第二因素身份验证方法的情况，都可实施此类攻击。除非用户安全意识极强，能够记得界面中（应该有）Passkey选项，否则很可能会直接输入用户名和密码，这些用户名和密码将与身份验证令牌/cookie一起被发送给攻击者，后者可以使用这些令牌/cookie来保持对帐户的持续访问。

根据Stewart的说法，passkeys.directory上列出的大多数Passkey实现都容易受到此类身份验证方法编辑攻击。

# **最安全的备份身份验证方法**

该研究进一步强调，几乎所有的Passkey备份身份验证方法都容易受到AitM攻击，包括密码、安全问题、向受信任设备推送通知、社交受信任联系人恢复、短信代码、电子邮件、电话、KYC/文件验证或预定义电子邮件或短信号码上的魔术链接。

其中，只有社交可信联系人恢复、KYC验证和魔术链接等选项才能通过繁琐的设置来阻止AitM。

研究者指出，第二密钥或FIDO2硬件密钥是最安全的方法。“显然，拥有多个密钥才是最安全的方法，最好是至少有一个密钥是由PIN安全存储和保护的硬件密钥，”Stewart指出：“Passkey的采用仍处于早期阶段，在密钥/安全密钥丢失或AitM身份验证流程被操纵的情况下，魔术链接可能是目前恢复用户帐户最安全的方法。”

**参考链接：**

https://www.esentire.com/blog/securing-passkeys-thwarting-authentication-method-redaction-attacks

原文来源：GoUpSec

“投稿联系方式：010-82992251   sunzhonghao@cert.org.cn”

![](https://mmbiz.qpic.cn/mmbiz_jpg/GoUrACT176n1NvL0JsVSB8lNDX2FCGZjW0HGfDVnFao65ic4fx6Rv4qylYEAbia4AU3V2Zz801UlicBcLeZ6gS6tg/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/GoUrACT176mrRug7icLIhX4EvNQjNgGRibia7K9qOLTR5PDfQiaUesU9xge7pnF8iciaxVC3JVkNqHA2pvQDnrM0hDVQ/0?wx_fmt=png)

网络安全应急技术国家工程中心

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/GoUrACT176mrRug7icLIhX4EvNQjNgGRibia7K9qOLTR5PDfQiaUesU9xge7pnF8iciaxVC3JVkNqHA2pvQDnrM0hDVQ/0?wx_fmt=png)

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