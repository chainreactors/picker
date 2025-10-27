---
title: 针对 Chrome 浏览器扩展程序网络钓鱼活动的新细节被披露
url: https://mp.weixin.qq.com/s?__biz=MzI0MDY1MDU4MQ==&mid=2247580965&idx=1&sn=7b271d77d7ae3794e77995267c934acf&chksm=e9146d1fde63e4097053f87e00d408e479510a2c67f11147c47b8735ea28cd8466e12a464d04&scene=58&subscene=0#rd
source: 嘶吼专业版
date: 2025-01-25
fetch_date: 2025-10-06T20:11:06.135055
---

# 针对 Chrome 浏览器扩展程序网络钓鱼活动的新细节被披露

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/wpkib3J60o2iczWfib6GrgzGeGiaSWecJUtV0meBD2qfjzrUoKqaKUiaGSBE7x10U2OPlDKyABRA2d1hFoPYdLflwmQ/0?wx_fmt=jpeg)

# 针对 Chrome 浏览器扩展程序网络钓鱼活动的新细节被披露

胡金鱼

嘶吼专业版

![](https://mmbiz.qpic.cn/mmbiz_gif/wpkib3J60o297rwgIksvLibPOwR24tqI8dGRUah80YoBLjTBJgws2n0ibdvfvv3CCm0MIOHTAgKicmOB4UHUJ1hH5g/640?wx_fmt=gif)

有关针对 Chrome 浏览器扩展程序开发人员的网络钓鱼活动的新细节近期被披露，该活动导致至少 35 个扩展程序被入侵，以注入数据窃取代码，其中包括来自网络安全公司 Cyberhaven 的扩展程序。

尽管最初的报告主要集中在 Cyberhaven 的安全扩展上，但随后的调查显示，相同的代码已被注入到至少 35 个扩展中，总共约有 2,600,000 人使用。从目标开发者对 LinkedIn 和 Google Groups 的报告来看，最新的攻击活动于 2024 年 12 月 5 日左右开始。然而，有安全研究人员发现早期命令和控制子域早在 2024 年 3 月就已存在。

# ![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2iczWfib6GrgzGeGiaSWecJUtVTCoHkULXatTf8wYazBefNeicWc5vKnx3Qr0RGbXBkvg7Gsu5uKtP8gQ/640?wx_fmt=png&from=appmsg)欺骗性的 OAuth 攻击链

攻击首先会直接或通过与其域名关联的支持电子邮件发送给 Chrome 扩展程序开发人员的网络钓鱼电子邮件。从看到的电子邮件来看，该活动使用了以下域名来发送网络钓鱼电子邮件：

supportchromestore.com

forextensions.com

chromeforextension.com

这封网络钓鱼电子邮件看起来像是来自 Google，声称该扩展程序违反了 Chrome Web Store 政策，有被删除的风险。

“我们不允许扩展程序具有误导性、格式不良、非描述性、不相关、过多或不适当的元数据，包括但不限于扩展程序描述、开发者名称、标题、图标、屏幕截图和宣传图片，”钓鱼邮件中写道。

具体来说，该扩展程序的开发人员会相信其软件的描述包含误导性信息，并且必须同意 Chrome 网上应用店政策。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2iczWfib6GrgzGeGiaSWecJUtVjicXyIDuAv7nl4G0gzgichkP1HAEL3ViaKh3ibSR4Z4lG7mwwicadVrtmGQ/640?wx_fmt=png&from=appmsg)

攻击中使用的网络钓鱼电子邮件

如果开发人员点击嵌入的“转到策略”按钮来了解他们违反了哪些规则，他们就会被带到 Google 域上的恶意 OAuth 应用程序的合法登录页面。该页面是 Google 标准授权流程的一部分，旨在安全向第三方应用授予访问特定 Google 帐户资源的权限。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2iczWfib6GrgzGeGiaSWecJUtVfqCFsbCwpIIScWby6lKwVzBQ9CmyVC1byzeOftDJTTaPpbOK0YzSjw/640?wx_fmt=png&from=appmsg)

恶意认证请求

在该平台上，攻击者托管了一个名为“隐私策略扩展”的恶意 OAuth 应用程序，该应用程序要求受害者授予通过其帐户管理 Chrome Web Store 扩展程序的权限。OAuth 授权页面上写道：“当您允许此访问时，隐私政策扩展程序将能够：查看、编辑、更新或发布您有权访问的 Chrome Web Store 扩展程序、主题、应用程序和许可证。”

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2iczWfib6GrgzGeGiaSWecJUtVbHsHIJ0HoKzXXIXtcibiaJgog3uXUxfc8e0o1kY8IeeZ25ErwgVFotMw/640?wx_fmt=png&from=appmsg)

权限审批提示

多重身份验证无助于保护帐户，因为不需要 OAuth 授权流程中的直接批准，并且该过程假设用户完全了解他们授予的权限范围。

Cyberhaven 在事后分析报告中解释说：“该员工遵循标准流程，无意中授权了这个恶意第三方应用程序。”

据了解，该员工启用了 Google 高级保护，并对其帐户进行了 MFA，但没有收到 MFA 提示。该员工的 Google 凭据没有受到损害。

一旦威胁者获得了扩展程序开发人员帐户的访问权限，他们就会修改扩展程序以包含两个恶意文件，即“worker.js”和“content.js”，其中包含从 Facebook 帐户窃取数据的代码。

被劫持的扩展程序随后作为“新”版本发布在 Chrome 网上应用店上。虽然 Extension Total 正在跟踪受此网络钓鱼活动影响的 35 个扩展程序，但攻击中的 IOC 表明，目标数量要多得多。

据 VirusTotal 称，威胁者预先注册了目标扩展的域名，即使他们没有遭受攻击。虽然大多数域名是在 11 月和 12 月创建的，但威胁者在 2024 年 3 月就测试了此攻击。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2iczWfib6GrgzGeGiaSWecJUtVFR15UtvCs3lEnicsPYVGB2WTHPPqVGbUk7yPFmSTUibWJgyaRhD5nMhQ/640?wx_fmt=png&from=appmsg)

网络钓鱼活动中早期使用的子域

# ![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2iczWfib6GrgzGeGiaSWecJUtVTCoHkULXatTf8wYazBefNeicWc5vKnx3Qr0RGbXBkvg7Gsu5uKtP8gQ/640?wx_fmt=png&from=appmsg)

对受感染机器的分析表明，攻击者的目标是中毒扩展程序用户的 Facebook 帐户。具体来说，数据窃取代码试图获取用户的 Facebook ID、访问令牌、帐户信息、广告帐户信息和企业帐户。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2iczWfib6GrgzGeGiaSWecJUtVsRMJUtSGoJWGXgSibyXicW2tPwhwwAMuM8ZncwGHdIfhf4DCZ7EhGCBA/640?wx_fmt=png&from=appmsg)

Facebook 数据被劫持的扩展程序窃取

此外，恶意代码还专门针对受害者在 Facebook.com 上的交互添加了鼠标点击事件监听器，寻找与平台的双因素身份验证或验证码机制相关的二维码图像。此举旨在绕过 Facebook 帐户的 2FA 保护，并允许威胁者劫持该帐户。

被盗信息将与 Facebook cookie、用户代理字符串、Facebook ID 和鼠标单击事件打包在一起，并渗透到攻击者的命令和控制 (C2) 服务器。威胁者一直通过各种攻击途径瞄准 Facebook 企业帐户，从受害者的信用直接付款到他们的帐户，在社交媒体平台上运行虚假信息或网络钓鱼活动，或者通过将其访问权限出售给其他人来货币化。

参考及来源：https://www.bleepingcomputer.com/news/security/new-details-reveal-how-hackers-hijacked-35-google-chrome-extensions/

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2iczWfib6GrgzGeGiaSWecJUtVJwwIXJQd0MIb7N5eVJc0NiaDS9p1PmFD0dmJpCAxfibVuqq8nAlKfkicQ/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2iczWfib6GrgzGeGiaSWecJUtVEEw1EicbLmcvb6zgPPiaGA7uPQia3Q2MeJEibqebtzSraxJgiald5yMTGAw/640?wx_fmt=png&from=appmsg)

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o29QZSgjKMjM7j822AuVv1iaicmoBhDlvJq1s41w5yIxoicDK9AsOGHLnQYkqq95ibWgq3OqvvXEO1qBVg/0?wx_fmt=png)

嘶吼专业版

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o29QZSgjKMjM7j822AuVv1iaicmoBhDlvJq1s41w5yIxoicDK9AsOGHLnQYkqq95ibWgq3OqvvXEO1qBVg/0?wx_fmt=png)

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