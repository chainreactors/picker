---
title: 黑客可滥用Entra代理ID管理员角色劫持服务主体
url: https://mp.weixin.qq.com/s/rVu7Furv422qDwcxQxwWNA
source: Doonsec's feed
date: 2026-04-25
fetch_date: 2026-04-26T04:55:57.516632
---

# 黑客可滥用Entra代理ID管理员角色劫持服务主体

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/BicXBAdicJy7Ps1uQ85sHlZ3Q2yib9elkzGb3NQ4ly63NO7HlHuG5TrQzBMupIcPtu94aEQmdF6KziaSM5YPwHs5qceJQ8n9WjzA13vBlnTHQls/0?wx_fmt=jpeg)

# 黑客可滥用Entra代理ID管理员角色劫持服务主体

原创

网络安全9527
网络安全9527

安全圈的那点事儿

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

微软Entra代理身份平台近期发现了一个严重的权限越界漏洞。新引入的代理ID管理员角色允许账户劫持任意服务主体，并在整个租户范围内提升权限。

截至 2026 年 4 月，微软已在所有云环境中完全修复了此问题。

## **权限边界是如何被打破的**

Microsoft Agent Identity Platform 是一项预览功能，它使用蓝图、代理身份和代理用户为人工智能代理提供身份。

为了管理这些非人类实体，微软引入了代理 ID 管理员角色。根据微软文档，该角色的权限范围严格限定于仅管理与代理相关的对象。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/BicXBAdicJy7Mdz1WBtbXMfzGZgEK1oNic1lY3CIibPuQpjwncfdydKD7RUYu3d9YtOZTgm0x9nIZ1v6Ho4knEbJicq0InCMiaNOdybDnibgM0lgRU/640?wx_fmt=png&from=appmsg)

然而，由于代理身份是建立在标准应用程序和服务主体原语之上的，因此出现了一个关键的范围差距。

Silverfort 的研究人员发现，更新代理身份所有者等操作允许管理员修改租户中任何服务主体的所有权。

具有代理 ID 管理员角色的用户可以将自己指定为完全不相关的、具有高权限的服务主体的所有者。

一旦确定了所有权，攻击者就可以生成新的凭据并以目标应用程序的身份进行身份验证。

如果被入侵的服务主体拥有较高的目录角色或具有高影响力的 Graph API 权限，则此接管原语可直接导致环境完全被入侵。

![](https://mmbiz.qpic.cn/mmbiz_png/BicXBAdicJy7NxNzCVI9s5IBXDHJxAEFxWDElZh0I6JYtgGriayDenYLrRdvibjwFicI2VzBBNHowDxiaZgyGQ0NjYlpdFIeSxWM7Bc0rRegyjLAM/640?wx_fmt=png&from=appmsg)

利用此漏洞的攻击者自然会瞄准网络中最具影响力的非人类身份。

根据 Silverfort 的研究，组织应主动识别具有管理员级别目录角色的服务主体，并对其进行适当的保护。

管理员可以使用 Azure CLI 和 jq 来查询Microsoft Graph API以查找这些易受攻击的配置。

以下脚本用于发现具有特权目录角色的服务主体。

![](https://mmbiz.qpic.cn/mmbiz_png/BicXBAdicJy7ODndWXvqHtv3XtQ6goVFoAGibKzVyeELjmsQdDtFT14w64ibU59tD5gAnBm1uxEhniatic9sx1D0Eg0qthkVxyS0tREFt522vDW8k/640?wx_fmt=png&from=appmsg)

微软承认了该问题，并部署了一个修复程序，以防止代理 ID 管理员角色管理非代理服务主体的所有者。

虽然眼前的威胁已经解除，但服务主体所有权滥用的潜在风险仍然是一条高价值的攻击途径。

安全团队必须积极监控其审计日志，以发现涉及向服务主体添加所有者或凭证的成功事件。

由于许多租户至少包含一个特权服务主体，因此将这些身份视为关键基础设施对于防止未来的权限提升攻击至关重要。

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