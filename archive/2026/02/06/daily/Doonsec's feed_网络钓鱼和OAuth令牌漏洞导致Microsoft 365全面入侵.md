---
title: 网络钓鱼和OAuth令牌漏洞导致Microsoft 365全面入侵
url: https://mp.weixin.qq.com/s/cOEsDXrelY7xCIrznIxMrg
source: Doonsec's feed
date: 2026-02-06
fetch_date: 2026-02-07T04:03:33.598805
---

# 网络钓鱼和OAuth令牌漏洞导致Microsoft 365全面入侵

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/FiapE7wXY1K9sHkSNAqQ70Lo9olhk1ciahEeibvDQJDSwLW7sPo3c3ctOfhzQgVPOoibFCoZcD0H3D3Sj6QgMdkmkk2ER1487YSyzTP0R8sFYSE/0?wx_fmt=jpeg)

# 网络钓鱼和OAuth令牌漏洞导致Microsoft 365全面入侵

O安全研究员
O安全研究员

O安全研究员

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/sz_mmbiz_png/FiapE7wXY1K8EqCibKSyTeqoENsTaojZfBsqXCQbTsBia3VWRg5bP5tRsicbkcB0X3iaxAWuFs1X1nNuFzB4KUloYnR2IGslDNdgV2cpUJOU3FS0/640?wx_fmt=png&from=appmsg)

现代网络应用经常通过看似无害的功能引入意想不到的攻击面，比如订阅通讯、联系表单和重置密码。

虽然单个漏洞单独看似可控，但复杂的对手越来越多地利用这些小缺陷来实现毁灭性的妥协。

电子邮件仍是网络攻击的主要入口，但传统的钓鱼攻击仍难以应对先进的过滤和认证协议。

攻击者通过滥用合法的商业逻辑找到了一种变通方法。通过控面向公众的API端点的输入字段，它们可以强制组织自身基础设施发送恶意邮件。

由于这些消息来自授权服务器，它们通过了严格的认证检查，如SPF和DMARC，直接进入受害者的主要收件箱。

这种技术通过利用组织自身领域内在的信任，有效地规避了检测。

![](https://mmbiz.qpic.cn/mmbiz_png/FiapE7wXY1Kic8vs2lvsojCm3czKoQKqrBvfuOyrD3k0PRC1ztcc6jibz0lQGGHBxmXZObIH175UCVMZQGVs5WGHaLXXY5ZlxZAJfAiasuqrCWA/640?wx_fmt=png&from=appmsg)

Praetorian分析师识别出了这一特定攻击链，指出当该邮件漏洞与第二个漏洞——错误处理不当——结合时，攻击链的严重性会大幅升级。

在许多云环境中，内部服务使用OAuth令牌进行身份验证。当应用程序在调试时显示冗长错误时，错误的请求可能触发响应，从而无意中倾倒这些敏感的认证令牌和栈跟踪。

## **代币劫持的机制**

这次攻略的技术核心依赖于应用环境中对OAuth 2.0持有人令牌的处理不当。

当攻击者故意向API提交不完整或格式错误的JSON负载时，系统无法优雅地降级。它不是通用错误，而是返回一个全面的调试日志给客户端。

该日志包含服务用来与 Microsoft Graph API 通信的活跃 JSON Web 令牌（JWT）。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/FiapE7wXY1KicQ6ia7Wj0TVEQ5tRZbVj0H0OHvVh3XTBg10wfVCibdAovcY0ibYe61FUj8hjhHHh6Wick94iclSdSFmib9KxCokqGpicWn1ia0TYQtL6g/640?wx_fmt=png&from=appmsg)

一旦提取，这些令牌即可即时、经过认证地访问组织资源，无需用户凭证或触发典型登录警报。

根据令牌的范围，攻击者可以悄无声息地窃取 SharePoint 文档、访问敏感的 Teams 聊天记录，或修改 Outlook 日历。

这种持久的立足点使他们能够在代币拥有足够权限的情况下转向更广泛的Azure基础设施。通过反复触发错误条件，攻击者可以收集新的令牌，即使会话结束仍能保持访问权限。

为了有效降低这些风险，安全团队必须对所有公共API执行严格的输入验证，确保仅接受最低必要的参数。

此外，组织应确保生产环境配置为返回通用错误信息，抑制可能无意中泄露内部系统状态或活跃凭证的详细调试信息。

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/dzJiaU8Wt1qwqJgvgiaEEbM4iaLlwQUhMic3TfI1ibRVlBcl7tiblcrRxgzBrF0UMhRtHtSuVfKdgVibQjjB7OoUYIU5w/0?wx_fmt=png)

O安全研究员

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/dzJiaU8Wt1qwqJgvgiaEEbM4iaLlwQUhMic3TfI1ibRVlBcl7tiblcrRxgzBrF0UMhRtHtSuVfKdgVibQjjB7OoUYIU5w/0?wx_fmt=png)

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