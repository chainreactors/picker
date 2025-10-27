---
title: 【安全圈】OAuth+XSS组合拳，数百万Web账户或将易主
url: https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652063225&idx=3&sn=acbd453e3ae2f13ac610263fae6ce432&chksm=f36e69b9c419e0aff24ad99b733455497222fbb399c01b817ca0145b1359e0ab88abcb232b32&scene=58&subscene=0#rd
source: 安全圈
date: 2024-08-01
fetch_date: 2025-10-06T18:05:06.317549
---

# 【安全圈】OAuth+XSS组合拳，数百万Web账户或将易主

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGyliakke3Sicz40hwdQH3Ip9FUcib4d1OXUxIKu7luwDpqeZWwUnyJYjQHtQhEniaNPW6jC3IFEkFDhMOIw/0?wx_fmt=jpeg)

# 【安全圈】OAuth+XSS组合拳，数百万Web账户或将易主

安全圈

![](https://mmbiz.qpic.cn/sz_mmbiz_png/aBHpjnrGylgOvEXHviaXu1fO2nLov9bZ055v7s8F6w1DD1I0bx2h3zaOx0Mibd5CngBwwj2nTeEbupw7xpBsx27Q/640?wx_fmt=png&from=appmsg "微信图片_20230927171534.png")

**关键词**

安全漏洞

关键的 API 安全漏洞（在跟踪和记录网络用户活动的 Hotjar 服务和广受欢迎的 Business Insider 全球新闻网站中发现的）利用现代身份验证标准复活了一个长期存在的漏洞，使数百万用户面临账户被接管的风险。

API 安全公司 Salt Security 的 Salt Labs 发现，通过将 OAuth 标准与这两个网站的跨站脚本 (XSS) 漏洞相结合，攻击者有可能暴露敏感数据，并冒充 100 多万个网站的合法用户开展恶意活动。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGyliakke3Sicz40hwdQH3Ip9FUcUtEfp2JKEIRjj6EUqT522wLq8eq1bIOzpxTfAUn5xbYRZc7mLSuMRg/640?wx_fmt=jpeg&from=appmsg)Hotjar 是一款通过记录用户活动来分析行为的工具，是对谷歌分析（Google Analytics）的补充，它为 100 多万个网站提供服务，其中包括 Adobe、微软、松下、哥伦比亚、RyanAir、迪卡侬、T-Mobile 和任天堂等知名品牌。

"由于 Hotjar 解决方案的性质，它收集的数据可能包括大量个人敏感数据，如姓名、电子邮件、地址、私人信息、银行详细信息，甚至在某些情况下还包括凭证。”Salt Labs 博客文章中关于这项研究的帖子说。

另外，在 Business Insider 网站上发现的另一个同样危险的漏洞也可被利用来执行跨站脚本 (XSS) 攻击，并接管该网站上的账户，而该网站在全球拥有数百万用户。

研究人员警告说，同样的漏洞组合可能在互联网大范围内潜伏，这使得更多的在线服务可能面临同样的问题。

## 现代身份验证标准

OAuth 是一个相对较新的标准，越来越多地被用于无缝跨网站认证，因为它是许多网站中“用 Facebook 登录”或“用 Google 登录”功能背后的引擎而被人熟知。该标准驱动着负责网站间身份验证切换的机制，允许网站间共享用户数据。但该标准在实施过程中被错误配置，从而创建了跨越多个站点的严重漏洞，影响众多网站。

XSS 作为最常被利用和最古老的网络漏洞之一，它允许攻击者将恶意代码注入合法的网页或应用程序中，以便在网站访问者的浏览器中执行脚本，用于数据盗窃等。

Salt Security 公司副总裁 Yaniv Balmas 表示，一个成功利用结合了这两种攻击手段的攻击者将获得与受害者相同的权限和功能。换句话说，潜在的风险将等同于普通系统用户实际能够进行的操作。

Salt Labs 于 3 月 20 日发现了 Business Insider 网站上的漏洞，并立即通知了该公司，该公司在 3 月 30 日修复了漏洞。而 Hotjar 的漏洞是在 4 月 17 日发现的，披露后两天就得到了缓解。

Salt 研究人员认为，允许攻击者利用 OAuth 和 XSS 组合的漏洞可能在其他网站上潜伏而未被发现，从而使数百万毫无戒心的用户面临潜在的账户被接管风险。

“我们坚信这是一个非常普遍的问题，而且很有可能许多其他在线服务也存在同样的问题。” Balmas 说。

## Hotjar 攻击

鉴于 XSS 已经存在了很长时间，大多数网站都有针对利用这种漏洞攻击的内置保护措施。Salt 的研究人员利用 OAuth 在 Hotjar 和 Business Insider 网站的两个独立实例中避开了这些保护。

研究人员操纵了 Hotjar 的社交登录功能，该功能重定向到 Google，通过 OAuth 接收秘密令牌以完成 Hotjar 上的认证。该令牌是一个包含秘密代码的 URL，JavaScript 代码可以读取该 URL，从而创建了一个 XSS 漏洞。

“为了将 XSS 与这个新的社交登录功能结合起来并实现有效的利用，我们使用 JavaScript 代码在新窗口中启动一个新的 OAuth 登录流程，然后从该窗口读取令牌，” 帖子中说。“使用这种方法，JavaScript 代码会在 Google 打开一个新标签页，Google 会自动将用户重定向回 [Hotjar 网站]，并在 URL 中加入 OAuth 代码。”

代码会读取新标签页中的 URL 并从中提取 OAuth 凭证。一旦攻击者获得了受害者的代码，他们就可以在 Hotjar 中启动一个新的登录流程，用受害者的代码替换他们的代码，从而完全接管账户，因此可能暴露 Hotjar 收集的所有个人数据。

## 利用移动登录

研究人员还设法利用了 Business Insider 网站代码中集成的社交登录功能，特别是通过移动身份验证，该功能会打开一个新的 Web 浏览器对用户进行身份验证。用户在网络上完成身份验证后，会被重定向到一个端点，而其凭证将作为参数通过网络发送到移动站点。

这个端点仅创建用于支持使用移动应用程序进行身份验证，容易受到 XSS 攻击。因此，如果攻击者能够从 URL 中读取凭证，就可以实现账户接管。

“我们需要做的是编写 JavaScript 代码，启动登录流程，等待令牌在 URL 中可见，然后读取该 URL，”帖子中说。“如果受害者点击了该链接，他们的凭证将被传递给恶意域。”

Balmas 强调，虽然在 Hotjar 和 Business Insider 网站上发现的具体漏洞已经得到缓解，但其他网站上也可能存在类似的潜在漏洞，这就意味着网站管理员在实施 OAuth 时需要十分小心，以免被用于类似的攻击场景。

他说："在实施任何新技术时需要考虑很多问题，当然也包括安全问题。考虑到所有可能选项的可靠实施应该是安全的，不应该让攻击者有机会滥用这种攻击载体"。

参考来源：https://www.darkreading.com/endpoint-security/oauth-xss-attack-millions-web-users-account-takeover

***END***

阅读推荐

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGylgTTuYibxDr5sTw6UZTOEkmzMpiawrG56u6yj3PM65KQDxYPoRp9dibODE5XJubgM8ibhNTuOGEXtuodA/640?wx_fmt=jpeg)[【安全圈】五男子使用“AI换脸”技术破解平台认证篡改系统数据牟取暴利被判刑](http://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652063207&idx=1&sn=41e4599574d805efa935881e461bbd5f&chksm=f36e69a7c419e0b1f87b23bba461c5353d6cb89b17dd55a3a49a799451ace1753eedc1300520&scene=21#wechat_redirect)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/aBHpjnrGylgTTuYibxDr5sTw6UZTOEkmzianBW3hxpjIFQch2g2L0lgJJabFXq6EmYIcUjnzdLzM5WFufcOAFmuA/640?wx_fmt=png)[【安全圈】Chrome漏洞致1500万Windows用户密码丢失！](http://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652063207&idx=2&sn=790e8e8c9ee504d963cf86d34278d612&chksm=f36e69a7c419e0b1b7ed716da65cb03c6b7660637b8ba41dc8874cf578159d9ed7294a7d9d5e&scene=21#wechat_redirect)

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGylgTTuYibxDr5sTw6UZTOEkmzdNkWZN1NzkKfhIl0yInnPaCwXFUvlWCTmIhbHs400xRvCEDgIhH71w/640?wx_fmt=jpeg)[【安全圈】防不胜防：黑客可利用 AI 通过 HDMI 线远程窃取屏幕信息](http://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652063207&idx=3&sn=778a5a174d446786aff7e6f1ba6d31d3&chksm=f36e69a7c419e0b15f39843961a43d4bf2afb964368adfb789068814bb214f5c9c04de2e0bda&scene=21#wechat_redirect)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/aBHpjnrGylgTTuYibxDr5sTw6UZTOEkmzQhfTTiawhJHxicXB2RwjiakURH6L3Rlt4h58lDLicJUxugoLaVSTXjHDnQ/640?wx_fmt=png)[【安全圈】黑客攻击 HFS 服务器以投放恶意软件和 Monero 矿工](http://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652063207&idx=4&sn=22e9ea970a9deefd91fd06ebe5efca00&chksm=f36e69a7c419e0b1172ae40c23acd17b4dbbbd2b00b6064452063ba627d8893008a7827e88a2&scene=21#wechat_redirect)

![](https://mmbiz.qpic.cn/mmbiz_gif/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCEft6M27yliapIdNjlcdMaZ4UR4XxnQprGlCg8NH2Hz5Oib5aPIOiaqUicDQ/640?wx_fmt=gif)

![](https://mmbiz.qpic.cn/mmbiz_png/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCEDQIyPYpjfp0XDaaKjeaU6YdFae1iagIvFmFb4djeiahnUy2jBnxkMbaw/640?wx_fmt=png)

**安全圈**

![](https://mmbiz.qpic.cn/mmbiz_gif/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCEft6M27yliapIdNjlcdMaZ4UR4XxnQprGlCg8NH2Hz5Oib5aPIOiaqUicDQ/640?wx_fmt=gif)

←扫码关注我们

**网罗圈内热点 专注网络安全**

**实时资讯一手掌握！**

![](https://mmbiz.qpic.cn/mmbiz_gif/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCE3vpzhuku5s1qibibQjHnY68iciaIGB4zYw1Zbl05GQ3H4hadeLdBpQ9wEA/640?wx_fmt=gif)

**好看你就分享 有用就点个赞**

**支持「****安全圈」就点个三连吧！**

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/aBHpjnrGylhgCQcCZBwQrSQRLABhjrXviafAj0avc5c69t69K1YymAruIaZWzXPqbGPourlnuu8pfibV0ebgqV9g/0?wx_fmt=png)

安全圈

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/aBHpjnrGylhgCQcCZBwQrSQRLABhjrXviafAj0avc5c69t69K1YymAruIaZWzXPqbGPourlnuu8pfibV0ebgqV9g/0?wx_fmt=png)

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