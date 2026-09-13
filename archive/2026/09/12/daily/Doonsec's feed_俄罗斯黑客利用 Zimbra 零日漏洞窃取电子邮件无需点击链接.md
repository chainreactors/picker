---
title: 俄罗斯黑客利用 Zimbra 零日漏洞窃取电子邮件无需点击链接
url: https://mp.weixin.qq.com/s/SA8fH7tDZ3YJEVaRXhsE3A
source: Doonsec's feed
date: 2026-09-12
fetch_date: 2026-09-13T06:58:55.600756
---

# 俄罗斯黑客利用 Zimbra 零日漏洞窃取电子邮件无需点击链接

# 俄罗斯黑客利用 Zimbra 零日漏洞窃取电子邮件无需点击链接

Khan安全团队

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

以下文章来源于威胁情报Z分析
，作者Z

![](https://wx.qlogo.cn/mmhead/j8cooK2zCqoqY1ibzIuH0db0U6NFgdx4PahHyU6OOprunMrA5RzXbibpMcUA18kVOibjEK1IK7HQ28/0)

**威胁情报Z分析**
.

国际网络安全威胁情报，地缘政治事件分析。

只需打开或预览一封恶意邮件，与俄罗斯有关联的黑客就能入侵存在漏洞的Zimbra网络邮件服务器。此次攻击无需点击链接或下载附件，漏洞利用程序会在邮件出现在网络邮件客户端后立即运行。

Proofpoint公司将此次活动归因于TA488，这是一个与俄罗斯结盟的间谍组织，也被称为Laundry Bear和Void Blizzard。该公司与美国国家安全局（NSA）和联邦调查局联合安全咨询委员会（JSAC）的报告协调发布了调查结果，而一份联合政府咨询报告则将该组织描述为受国家支持，并专注于为俄罗斯收集情报。

根据该安全公告（PDF），该组织的目标包括乌克兰政府机构、美国政府和国防组织、核设施、科研机构以及欧洲的实体。Proofpoint公司表示，该组织至少从2025年7月起就一直在利用此前未知的Zimbra漏洞，比公开披露的时间至少早了五个月。

打开电子邮件会触发攻击

当收件人在存在漏洞的 Zimbra 网络邮件客户端中打开或预览邮件时，嵌入在邮件 HTML 正文中的恶意 JavaScript 代码会自动执行。这些邮件使用通用的商业主题，并从攻击者控制的 Proton Mail 地址或在先前攻击中被盗用的帐户发送。

该漏洞编号为CVE-2025-66376，影响 Zimbra 对 HTML 和 CSS 内容的处理。攻击者将危险代码拆分成多个片段，这些片段可以绕过邮件清理程序，从而使浏览器在显示邮件时能够重新构建并执行这些片段。

一旦激活，Proofpoint 追踪到的名为 ZimReaper 的恶意软件会收集受害者的电子邮件地址、浏览器保存的密码、双因素身份验证的验证码以及 Zimbra 安装信息。它还会搜索组织的地址目录，并试图导出长达 90 天的电子邮件。

TA488随后创建了一个名为“ZimbraWeb”的应用程序密码，该密码可以通过IMAP、POP3或SMTP协议提供持续的邮箱访问，而无需受害者进行正常的双因素身份验证。窃取的信息通过DNS请求和网络流量传输到攻击者控制的服务器。

被攻破的邮箱也帮助该组织接触到了新的目标。从合法账户发送的邮件更容易显得可信，这为TA488提供了另一条向政府和商业机构发送攻击邮件的途径。

“这些邮件使用通用诱饵，无需目标用户点击链接或打开附件。跨站脚本攻击直接嵌入在邮件的HTML正文中，一旦受害者在存在漏洞的Zimbra网页邮件客户端中打开或预览邮件，攻击就会立即触发。无需用户进行任何其他交互。”

![](https://mmbiz.qpic.cn/sz_mmbiz_png/0LGiaGIrzXunibudArgdtMHTK7f1vyTFscE6PEP9sf4CHYvqatpLIiaueSGt9abe1PCpewJOO1LC7fljCgQ7NicwCsYvzmNicHN2icTeEDkPicyzow/640?wx_fmt=png&from=appmsg)

Zimbra补丁将于2025年11月起提供。

Zimbra 于 2025 年 11 月修复了 CVE-2025-66376 漏洞，修复程序包含在 ZCS 10.1.13 和 10.0.18 版本中。该漏洞于 2026 年 1 月被公开记录，此时距离 TA488 开始利用该漏洞作为零日漏洞已过去数月。

管理员应更新所有暴露的 Zimbra 服务器，并检查/opt/zimbra/log/audit.log创建应用程序密码的请求，特别是名为“ZimbraWeb”的条目。该联合公告还建议撤销应用程序密码和双因素身份验证临时代码，重置用户密码，并检查报告中发布的指标。

预览时标签不可点

![]()

微信扫一扫
关注该公众号

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/aPmkR80bcV3JwGBDpU6XB9v8QmVNuqicT4vSSnibBesxWSwrwSORopnXEPcjahRUcLrTDK5MszhYG4ho8icFMuXMg/0?wx_fmt=png)

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