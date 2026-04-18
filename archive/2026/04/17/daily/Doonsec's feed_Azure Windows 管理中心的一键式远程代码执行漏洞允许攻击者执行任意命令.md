---
title: Azure Windows 管理中心的一键式远程代码执行漏洞允许攻击者执行任意命令
url: https://mp.weixin.qq.com/s/0yTOZmgF73e67DzwzdNHoA
source: Doonsec's feed
date: 2026-04-17
fetch_date: 2026-04-18T04:26:12.215198
---

# Azure Windows 管理中心的一键式远程代码执行漏洞允许攻击者执行任意命令

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/BicXBAdicJy7PXl0PdMp98lfEtyMrviaxicHtqICiaqUZ6VNNqUbz6tn8M68d6GabOz5zxCjbA90wexzg3SGFWA2GWMTVHqicOMUmxoBCk7rGaWw8/0?wx_fmt=jpeg)

# Azure Windows 管理中心的一键式远程代码执行漏洞允许攻击者执行任意命令

原创

网络安全9527
网络安全9527

安全圈的那点事儿

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

Windows Admin Center 是一款本地部署的基于浏览器的管理工具，IT 管理员可以使用它通过集中式图形界面管理 Windows 服务器、客户端和集群。

Cymulate 研究实验室发现的这一新发现的严重漏洞，允许攻击者在 Azure 集成和本地 WAC 部署中实现未经身份验证的一键式远程代码执行 (RCE)。

攻击者只需诱骗受害者访问篡改过的网址，即可秘密执行任意命令并接管目标网络。

这些漏洞已于 2025 年 8 月 22 日负责任地披露给微软。报告发布后，微软成功地应用了服务器端补丁来保护所有 Azure 管理的实例。

由于此修复是在服务端实施的，因此云客户无需任何手动操作即可自动受到保护。

但是，使用本地 WAC 部署的组织必须主动将其系统更新到最新版本，以修复漏洞并防止漏洞被利用。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/BicXBAdicJy7MIezdkFsvZZunjg4W6ibOSqtuV8waUDyzVkBwbm4B3ZYxb2dEic2mwNv8KJIVicuQRwNStMf1zT7iaZDqGLsmZf5ZsUZ9icic8avJEA/640?wx_fmt=png&from=appmsg)

## **导致此次攻击的核心漏洞**

根据 Cymulate Research Labs 发布的技术报告，该攻击链依赖于三个底层架构缺陷，攻击者将这些缺陷结合起来以达到最大影响：

* 基于响应的跨站脚本攻击 (XSS) 允许攻击者将任意 JavaScript 代码注入到 Azure 门户流程和本地错误处理机制中。
* 不安全的重定向处理导致 WAC 接受外部控制的网关 URL 而没有进行适当的验证，从而使威胁行为者能够劫持合法的应用程序流进行欺骗和网络钓鱼攻击。
* 本地部署环境中不安全的凭据存储会将敏感的 Azure 访问令牌和刷新令牌直接保存在浏览器的本地存储中，使其容易受到 XSS 漏洞的直接窃取。

该研究强调了不同的攻击路径和后果，具体取决于Windows 管理中心环境的部署方式。

![](https://mmbiz.qpic.cn/mmbiz_png/BicXBAdicJy7Nyoo4vd3T3Y9jgVibg7M1hPhrgVrEykDtTZSUThk9f4oZibrKibVHibibrYrXu3kR59VxsTjZsmOxYHc69x5g2130lLbqkk1yY1Te4/640?wx_fmt=png&from=appmsg)

* Azure 托管环境允许攻击者构造看似真实的 URL，其中包含恶意有效载荷，从而引发虚假的基本身份验证或 NTLM 身份验证，悄无声息地从受信任的 Microsoft 来源窃取用户凭据。
* 本地部署会带来更高的安全隐患，因为威胁行为者可以强制网关在托管服务器上执行任意 PowerShell 命令。
* 连接的本地网关会暴露存储的 Azure 令牌，从而促进横向移动，使攻击者能够获得受害者的完整云权限和租户控制权。

## **漏洞利用链的实际应用**

Cymulate 的研究人员证明，整个攻击链只需要极少的用户交互。

![](https://mmbiz.qpic.cn/mmbiz_png/BicXBAdicJy7MK5Uq9IXMtrWSrqHeqMicICtZO2nZzPmUEJ0GypVdISRzQbYZSx9jf8b3rCacZuFFNZSN1icAdC45ibAYuItSpicBWUQEBvmNkOqk/640?wx_fmt=png&from=appmsg)

攻击者需要注册一个有效的域名，获取一个可信的Web证书，并伪造一个WAC网关URL。然后，这个恶意链接可以通过钓鱼邮件、伪装链接或自动Web重定向进行传播。

一旦毫无戒心的受害者点击链接，WAC应用程序就会自动将流量重定向到攻击者控制的服务器。随后，恶意服务器会返回一条精心构造的错误消息，其中包含隐藏的脚本。

由于应用程序未能正确清理传入的响应，恶意代码直接在具有高度特权的 WAC 浏览器环境中执行。

此次漏洞利用清楚地表明，开发人员必须严格验证客户端输入和服务器响应，以防止复杂的攻击。虽然 Azure 托管的 WAC 客户已经受到保护，但内部网络的安全风险仍然十分严峻。

Cymulate Research Labs 强烈建议所有管理本地 Windows Admin Center 部署的安全团队立即升级到最新的、已打补丁的 Microsoft 版本。

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