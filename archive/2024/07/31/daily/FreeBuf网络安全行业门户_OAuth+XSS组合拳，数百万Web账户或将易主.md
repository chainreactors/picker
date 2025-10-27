---
title: OAuth+XSS组合拳，数百万Web账户或将易主
url: https://www.freebuf.com/news/407325.html
source: FreeBuf网络安全行业门户
date: 2024-07-31
fetch_date: 2025-10-06T17:43:48.873866
---

# OAuth+XSS组合拳，数百万Web账户或将易主

[![freeBuf](/images/logoMax.png)](/)

主站

分类

云安全

AI安全

开发安全

终端安全

数据安全

Web安全

基础安全

企业安全

关基安全

移动安全

系统安全

其他安全

特色

热点

工具

漏洞

人物志

活动

安全招聘

攻防演练

政策法规

[报告](https://www.freebuf.com/report)[专辑](/column)

* ···
* [公开课](https://live.freebuf.com)
* ···
* [商城](https://shop.freebuf.com)
* ···
* 用户服务
* ···

行业服务

政 府

CNCERT
CNNVD

会员体系（甲方）
会员体系（厂商）
产品名录
企业空间

[知识大陆](https://wiki.freebuf.com/page)

搜索

![](/freebuf/img/7aa3bf7.svg) ![](/freebuf/img/181d733.svg)

创作中心

[登录](https://www.freebuf.com/oauth)[注册](https://www.freebuf.com/oauth)

官方公众号企业安全新浪微博

![](/images/gzh_code.jpg)

FreeBuf.COM网络安全行业门户，每日发布专业的安全资讯、技术剖析。

![FreeBuf+小程序](/images/xcx-code.jpg)

FreeBuf+小程序把安全装进口袋

[![](https://image.3001.net/images/20231020/1697804527_653270ef7570cc7356ba8.png)](https://wiki.freebuf.com)

OAuth+XSS组合拳，数百万Web账户或将易主

* ![]()
* 关注

* [资讯](https://www.freebuf.com/news)

OAuth+XSS组合拳，数百万Web账户或将易主

2024-07-30 11:25:26

所属地 上海

关键的 API 安全漏洞（在跟踪和记录网络用户活动的 Hotjar 服务和广受欢迎的 Business Insider 全球新闻网站中发现的）利用现代身份验证标准复活了一个长期存在的漏洞，使数百万用户面临账户被接管的风险。

API 安全公司 Salt Security 的 Salt Labs 发现，通过将 OAuth 标准与这两个网站的跨站脚本 (XSS) 漏洞相结合，攻击者有可能暴露敏感数据，并冒充 100 多万个网站的合法用户开展恶意活动。

![](https://image.3001.net/images/20240730/1722309333_66a85ad5c13d851306065.png!small)Hotjar 是一款通过记录用户活动来分析行为的工具，是对谷歌分析（Google Analytics）的补充，它为 100 多万个网站提供服务，其中包括 Adobe、微软、松下、哥伦比亚、RyanAir、迪卡侬、T-Mobile 和任天堂等知名品牌。

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

# OAuth # xss攻击 # XSS漏洞

本文为 独立观点，未经授权禁止转载。
如需授权、对文章有疑问或需删除稿件，请联系 FreeBuf
客服小蜜蜂（微信：freebee1024）

被以下专辑收录，发现更多精彩内容

+ 收入我的专辑

+ 加入我的收藏

展开更多

相关推荐

![]()

关 注

* 0 文章数
* 0 关注者

文章目录

现代身份验证标准

Hotjar 攻击

利用移动登录

![](/images/logo_b.png)

本站由阿里云 提供计算与安全服务

### 用户服务

* [有奖投稿](https://www.freebuf.com/write)
* [提交漏洞](https://www.vulbox.com/bounties/detail-72)
* [参与众测](https://www.vulbox.com/projects/list)
* [商城](https://shop.freebuf.com)

### 企业服务

* [安全咨询](https://company.freebuf.com)
* [产业全景图](https://www.freebuf.com/news/307349.html)
* [企业SRC](https://www.vulbox.com/service/src)
* [安全众测](https://www.vulbox.com/)

### 合作信息

* [斗象官网](https://www.tophant.com/)
* [广告投放](https://www.freebuf.com/articles/444331.html)
* [联系我们](https://www.freebuf.com/articles/444332.html)

### 关于我们

* [关于我们](https://www.freebuf.com/news/others/864.html)
* 微信公众号
* [新浪微博](http://weibo.com/freebuf)

### 战略伙伴

* [![](https://image.3001.net/images/20191017/1571306518_5da83c1686dd9.png)](http://www.aliyun.com/?freebuf)

### FreeBuf知识大陆

![](https://image.3001.net/images/20250703/1751535036_68664dbcae34ac40bb9e7.png)

扫码把安全装进口袋

* [斗象科技](https://www.tophant.com/)
* [FreeBuf](https://www.freebuf.com)
* [漏洞盒子](https://www.vulbox.com/)
* [斗象智能安全](https://ai.tophant.com/)
* [免责条款](https://www.freebuf.com/dis)
* [协议条款](https://my.freebuf.com/AgreeProtocol/duty)

Copyright © 2025 WWW.FREEBUF.COM All Rights Reserved
[沪ICP备2024099014号](https://beian.miit.gov.cn/#/Integrated/index) | [沪公安网备
![](https://image.3001.net/images/20200106/1578291342_5e12d08ec2379.png)](http://www.beian.gov.cn/portal/registerSystemInfo?recordcode=31011502009321)