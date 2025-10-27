---
title: API NEWS | Booking.com爆出API漏洞
url: https://www.anquanke.com/post/id/289299
source: 安全客-有思想的安全新媒体
date: 2023-06-17
fetch_date: 2025-10-04T11:44:16.228348
---

# API NEWS | Booking.com爆出API漏洞

首页

阅读

* [安全资讯](https://www.anquanke.com/news)
* [安全知识](https://www.anquanke.com/knowledge)
* [安全工具](https://www.anquanke.com/tool)

活动

社区

学院

安全导航

内容精选

* [专栏](/column/index.html)
* [精选专题](https://www.anquanke.com/subject-list)
* [安全KER季刊](https://www.anquanke.com/discovery)
* [360网络安全周报](https://www.anquanke.com/week-list)

# API NEWS | Booking.com爆出API漏洞

阅读量**706038**

发布时间 : 2023-06-16 17:57:51

**x**

##### 译文声明

本文是翻译文章

译文仅供参考，具体内容表达以及含义原文为准。

欢迎大家围观小阑精心整理的API安全最新资讯，在这里你能看到最专业、最前沿的API安全技术和产业资讯，我们提供关于全球API安全资讯与信息安全深度观察。

**本周，我们带来的分享如下：**

1. [http://](https://link.zhihu.com/?target=http%3A//Booking.com)[Booking.com](https://link.zhihu.com/?target=http%3A//Booking.com)爆出API漏洞
2. 谷歌金融APP泄露API敏感数据
3. 一篇关于API安全测试清单的文章
4. 一篇关于“以人为本的修复是确保API安全的关键”文章

##

## Booking.com爆出API漏洞

IT Security Guru最近的调查发现，住宿预订服务[http://](https://link.zhihu.com/?target=http%3A//Booking.com)[Booking.com](https://link.zhihu.com/?target=http%3A//Booking.com)，在登录功能的OAuth实例，可能导致恶意攻击者接管用户的账号，而且黑客也能够以同样的手法，登录[http://](https://link.zhihu.com/?target=http%3A//Booking.com)[Booking.com](https://link.zhihu.com/?target=http%3A//Booking.com)子公司[http://](https://link.zhihu.com/?target=http%3A//Kayak.com)[Kayak.com](https://link.zhihu.com/?target=http%3A//Kayak.com)。[http://](https://link.zhihu.com/?target=http%3A//Booking.com)[Booking.com](https://link.zhihu.com/?target=http%3A//Booking.com)在收到Salt Security的漏洞通报后，已经迅速修复问题，并且确认未有黑客利用该漏洞入侵平台。

OAuth（Open Authorization）是目前的开放身份验证标准，使用户可以允许应用程序读取脸书或Google等账号资料进行身份验证，方便地登录应用程序。研究人员发现[http://](https://link.zhihu.com/?target=http%3A//Booking.com)[Booking.com](https://link.zhihu.com/?target=http%3A//Booking.com)上由于不安全的OAuth设计缺陷，使攻击者有机会接管以脸书登录的账号，而且一旦接管成功，攻击者便可以假冒用户执行任意操作，包括访问所有个人资讯和其他敏感数据。

这项漏洞不只让使用脸书账号登录[http://](https://link.zhihu.com/?target=http%3A//Booking.com)[Booking.com](https://link.zhihu.com/?target=http%3A//Booking.com)的用户受到影响，即便用户是使用Google或其他登录方式创建账号，攻击者同样也可以使用脸书登录功能接管其[http://](https://link.zhihu.com/?target=http%3A//Booking.com)[Booking.com](https://link.zhihu.com/?target=http%3A//Booking.com)账号。攻击者只要向使用Google身份验证的[http://](https://link.zhihu.com/?target=http%3A//Booking.com)[Booking.com](https://link.zhihu.com/?target=http%3A//Booking.com)用户发送恶意连接，由于受害者电子邮件地址相同，[http://](https://link.zhihu.com/?target=http%3A//Booking.com)[Booking.com](https://link.zhihu.com/?target=http%3A//Booking.com)便会自动关联拥有相同电子邮件的账户允许登录。

![]()

研究人员提到，这类OAuth配置错误对公司和用户造成重大影响，攻击者可能会代替受害者提出未经授权的请求、取消预订，或是访问敏感个人资讯，包括预定历史记录、个人喜好或是未来订单。

虽然OAuth2（或其他标准机制）可以增加API安全性，但实现起来可能会很复杂。因此，这提醒API开发人员必须小心谨慎，提高安全意识，确保使用OAuth2时必须正确配置。

##

## 谷歌金融APP泄露API敏感数据

近期来自Approov的报告声称，对谷歌应用商店上的金融应用程序进行了研究。该报告的关键点是，谷歌应用商店上92%的金融应用程序包含可提取的数据，例如API密钥。在这些泄露的应用程序中，泄漏了近四分之一的敏感数据，例如用于支付和货币账户转移的身份验证密钥。该研究基于谷歌应用商店中美国、英国、法国和德国的“前200名”金融服务应用程序。

![]()

Approov使用一个五点框架来识别移动应用程序攻击面：

1. 用户凭据
2. 应用程序完整性
3. 设备完整性
4. API通道完整性
5. 服务漏洞

根据Approov的说法，大多数调查的应用程序在防御针对设备环境的攻击方面都非常薄弱，而且很难对中间人攻击进行有效防护。

中间人攻击（Man-in-the-Middle Attack, MITM）是一种由来已久的网络入侵手段，并且当今仍然有着广泛的发展空间。MITM攻击可以通过拦截正常的网络通信数据，并进行数据篡改和嗅探，而通信的双方却毫不知情。在黑客技术越来越多的运用于以获取经济利益为目标的情况下时，MITM攻击成为对网银、网游、网上交易等最有威胁并且最具破坏性的一种攻击方式。

**小阑建议，预防中间人攻击，可以采取以下措施：**

1. 采用动态ARP检测：DHCP Snooping 等控制操作来加强网络基础设施。
2. 采用传输加密：SSL和TLS可以阻止攻击者使用和分析网络流量。像Google 等公司如今都有高级的网站搜索引擎优化，默认状态下都提供 HTTPS。
3. 使用CASBs云访问安全代理：CASBs 可以提供加密、访问控制、异常保护以及数据丢失保护等一系列功能。
4. 创建RASP实时应用程序自我保护：内置于应用程序中，用来防止实时攻击。
5. 阻止自签名证书：自签名证书很容易伪造，但是目前还没有撤销它们的机制，所以应该使用有效证书颁发机构提供的证书。
6. 强制使用 SSLpinning：这是对抗 MiTM 攻击的另一种方式。使用有效证书颁发机构提供的证书是第一步，它是通过返回的受信任的根证书以及是否与主机名匹配来验证该服务器提供的证书的有效性。通过 SSL pinning可以验证客户端检查服务器证书的有效性。

##

## 关于API安全测试清单

最近外国安全研究员DANA发现了Shieldify的一个GitHub存储库，其中包含一个API安全清单，列出了在设计、测试和发布应用程序编程接口时要考虑的最重要对策。虽然它不是目前最全面的REST API安全测试清单，但它很好地涵盖了蓝队需要考虑的许多重要事项。

![]()

API安全测试清单（部分）如下：

1. 认证和授权：确保API要求身份验证（Authentication）和授权（Authorization）以限制对受保护资源的访问，例如Token-based认证和OAuth 2.0授权。举例：某个API没有进行任何认证和授权措施，攻击者可以通过发送恶意请求来访问该API并窃取敏感数据。
2. 输入验证：对API的输入进行严格检查，避免输入参数中包含恶意代码或SQL注入等攻击代码。举例：某个API没有验证输入参数中的数据类型和长度，攻击者可以将恶意脚本注入字符串参数，并在服务器上执行该脚本。
3. 输出编码：确保对API输出进行适当的编码处理，以避免跨站点脚本（XSS）攻击。举例：某个API没有经过编码处理就直接输出HTML标签，攻击者可以通过发送构造性负载数据，绕过浏览器的安全机制，使其在受害者浏览器上执行。
4. SQL注入防御：确保对API的输入数据进行适当的检查和过滤，避免SQL注入攻击。举例：某个API没有对输入参数进行过滤和转义，攻击者可以通过输入构造性负载数据，修改SQL查询语句，从而跨越数据库查询获取敏感数据。
5. 数据保护：确保对API传输的数据进行加密和解密处理，保护数据传输过程中不被窃取、篡改或重放攻击。举例：某个API采用明文传输，攻击者可以获取API传输的数据包，通过模拟发送恶意数据来模拟合法的请求。
6. 日志监控：确保对API的操作日志进行记录、分析和监控，以便及时发现异常操作和安全事件。举例：某个API没有记录日志，攻击者可以在未被检测到的情况下进行多次恶意请求，导致服务器崩溃或数据泄露。

API安全测试清单非常重要，它可以帮助开发团队充分了解API存在的安全漏洞，并及时解决这些问题，提高API的安全性和可靠性。

##

## 以人为本的修复是确保API安全的关键

本周特别邀请了Secure Code Warrior的CTO Matias Madou接受采访，阐述了以人为本的修复是确保API安全的关键。

Madou表示，如果一个企业想要保证API的安全，不能仅仅依靠自动化和工具来解决问题。因为没有关于管理API行为的标准，所以开发团队必须经过培训后才能够更好地管理API。虽然新的工具可以简化安全团队的工作流程，但是用户使用这些工具所犯的错误是很难被预测的。因此，组织需要不仅仅依靠工具，还要有经过培训的开发人员来对API的安全进行管理。

![]()

例如，假设某个组织开发了一个需要登录的API，他们使用了自动化工具来检查代码中是否存在SQL注入漏洞。但是，这些工具可能无法检测到其他类型的安全问题，例如访问控制或身份验证方面的问题。因此，该组织需要经过培训的开发人员来检查和解决这些问题，以确保API的完整性。

虽然新的工具可以帮助简化安全团队的流程，但是它们无法完全代替人类的思考和分析能力。因此，需要有经验的专业人员来管理API的行为，以及解决可能存在的安全问题。

**小阑分析：**

以人为本的修复是API安全性的关键，因为它能够确保开发人员具备正确的安全知识和技能，并且能够在编写代码时遵循最佳的安全实践，从而有效地预防和解决API安全问题。而且，以人为本的修复方法，可以帮助开发团队更好地理解API的安全需求，并增强对其重要性的认识。经过培训和教育的开发人员，可以更加精通基础的安全知识和最佳实践，从而更好地理解API的安全问题，并且能够在编码期间，来确保API的安全性。

感谢[http://](https://link.zhihu.com/?target=http%3A//APIsecurity.io)[APIsecurity.io](https://link.zhihu.com/?target=http%3A//APIsecurity.io)提供相关内容

###

### **关于星阑**

星阑科技基于AI深度感知和强大的自适应机器学习技术，帮助用户迅速发现并解决面临的安全风险和外部威胁，并凭借持续的创新理念和以实战攻防为核心的安全能力，发展成为国内人工智能、信息安全领域的双料科技公司。**为解决API安全问题，公司从攻防能力、大数据分析能力及云原生技术体系出发，提供全景化API识别、API高级威胁检测、复杂行为分析等能力，构建API Runtime Protection体系。**

星阑科技产品——**萤火 (API Intelligence) 拥有不同应用场景的解决方案**，适配服务器、容器集群、微服务架构以及云平台等多种架构。通过API资产梳理、漏洞管理、威胁监测、开放式数据平台、运营与响应能力，解决企业API漏洞入侵、行为异常、数据泄露等核心风险。

本文翻译自 原文链接。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**星阑科技**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/289299](/post/id/289299)

安全KER - 有思想的安全新媒体

本文转载自:

如若转载,请注明出处：

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [API](/tag/API)

**+1**21赞

收藏

![](https://p0.ssl.qhimg.com/t01ae1a72a720da3a7b.png)星阑科技

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p2.ssl.qhimg.com/t010136e53e1b35516c.png)

[![](https://p0.ssl.qhimg.com/t01ae1a72a720da3a7b.png)](/member.html?memberId=147620)

[星阑科技](/member.html?memberId=147620)

星阑科技

* 文章
* **119**

* 粉丝
* **46**

### TA的文章

* ##### [保护敏感数据的艺术：数据安全指南](/post/id/290760)

  2023-10-18 10:57:25
* ##### [受邀演讲 | 确保数字化生态安全稳健](/post/id/290528)

  2023-09-05 17:48:29
* ##### [技术专题：API资产识别大揭秘（一）](/post/id/290471)

  2023-09-05 17:37:14
* ##### [解密与探究：理解WebSocket协议与报文格式](/post/id/290500)

  2023-08-30 14:36:15
* ##### [创新护航：萤火助力守护数据跨境安全](/post/id/290512)

  2023-08-29 16:10:15

### 相关文章

* ##### [保护敏感数据的艺术：数据安全指南](/post/id/290760)

  2023-10-18 10:57:25
* ##### [受邀演讲 | 确保数字化生态安全稳健](/post/id/290528)

  2023-09-05 17:48:29
* ##### [技术专题：API资产识别大揭秘（一）](/post/id/290471)

  2023-09-05 17:37:14
* ##### [星阑科技受邀专精特新创新策源会，共同探讨网安新生态](/post/id/290481)

  2023-08-29 16:09:31
* ##### [锐意拼搏 开拓奋进 | 星阑科技受邀ISC，共讨数智化生产力变革](/post/id/290475)

  2023-08-22 12:47:46
* ##### [API NEWS | API安全需要重置](/post/id/290291)

  2023-08-15 14:45:10
* ##### [医疗案例分享 | 数据安全流转解决方案](/post/id/290399)

  2023-08-15 14:43:07

### 热门推荐

文章目录

* [Booking.com爆出API漏洞](#h2-1)
* [谷歌金融APP泄露API敏感数据](#h2-3)
* [关于API安全测试清单](#h2-5)
* [以人为本的修复是确保API安全的关键](#h2-7)
  + [关于星阑](#h3-9)

![](https://p0.qhimg.com/t11098f6bcd5614af4bf21ef9b5.png)

安全KER

* [关于我们](/about)
* [联系我们](/note/contact)
* [用户协议](/note/protocol)
* [隐私协议](/note/privacy)

商务合作

* [合作内容](/note/business)
* [联系方式](/note/contact)
* [友情链接](/link)

内容需知

* [投稿须知](https://www.anquanke.com/contribute/tips)
* [转载须知](/note/repost)
* 官网QQ群：568681302

合作单位

* [![安全KER](https://p0.ssl.qhimg.com/t01592a959354157bc0.png)](http://www.cert.org.cn/)
* [![安全KER](https://p0.ssl.qhimg.com/t014f76fcea94035e47.png)](http://www.cnnvd.org.cn/)

Copyright © 北京奇虎科技有限公司 三六零数字安全科技集团有限公司 安全KER All Rights Reserved [京...