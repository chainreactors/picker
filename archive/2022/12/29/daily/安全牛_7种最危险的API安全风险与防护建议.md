---
title: 7种最危险的API安全风险与防护建议
url: https://mp.weixin.qq.com/s?__biz=MjM5Njc3NjM4MA==&mid=2651121097&idx=1&sn=774cf4d7ab629547798689d892e2b19b&chksm=bd14551a8a63dc0c2a8082ac579da76967a71526cfecf337101935ab5537a6a63aaab3275a3d&scene=58&subscene=0#rd
source: 安全牛
date: 2022-12-29
fetch_date: 2025-10-04T02:40:22.880337
---

# 7种最危险的API安全风险与防护建议

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/kuIKKC9tNkAtSNcMCW9afZNHiaHFHGQOicbKG1NX1qLbuAHoQW2OcpicauS3xNBojphWng6tfAIolZsIoLM9z82vA/0?wx_fmt=jpeg)

# 7种最危险的API安全风险与防护建议

安全牛

当今社会已进入一个信息广泛互联和共享的时代，API技术逐渐成为了现代数字业务环境的基础组成，也是企业数字化转型发展战略实现的核心要素。几乎所有的企业都依赖API进行服务连接、传输数据和控制系统。然而，API的爆炸性应用也极大地扩展了企业的攻击面，增加了企业对API安全性的需求。

**API安全的现状**

Salt Security是一家API安全公司，它提供了一个整体保护平台来防止API攻击，并使用机器学习和AI来自动连续地识别和保护API。根据Salt Security2022年最新发布的《API安全趋势调查报告》数据显示：

* 2022年，平均每个受访企业的API数量较去年增长82%。同时，恶意API流量占比约为2.1%，比去年激增117%；
* API攻击正在引发严重的安全问题，有94%的受访者表示他们在过去一年内遇到过API安全问题；
* 近一半（47%）的受访者表示，他们在企业应用的API中检测出安全漏洞；38%的受访企业遭遇过API引发的身份安全问题，31%的受访企业遭遇过API引发的敏感数据泄露和隐私安全事件；
* 40%的受访者表示将努力解决API应用安全问题，但只有11%的受访者表示，目前已经使用了针对性技术来进行API安全测试和保护工作。

以上研究结果表明，有很多企业还没有对API面临的安全威胁保持足够的重视。但实际上，它们可能难以承受自己的商誉和诚信受到API安全事件带来的损害。因此，所有企业都需要努力解决API的安全问题，确保对网络中最常见和最严重的API安全威胁进行补救。

**API安全风险与防护建议**

API安全不仅仅是修复单个漏洞的问题。相反，它需要IT团队的全面关注。他们必须从更广泛的角度解决API网络安全缺口。任何API中的某一个安全问题都可能导致不必要的后果。 以下整理了一些最危险的API安全风险和防护建议。

风险一

影子API、僵尸API

影子API是目前API安全中最为突出的问题，由于API的使用率激增，企业往往无法全部跟踪管理，因此，一些API无法及时进行维护更新，从而成为了被恶意黑客公开利用的漏洞。

与影子API类似，僵尸API对组织来说也是一个巨大的安全风险，其通常指的是旧的、很少使用的API版本。由于僵尸API很少得到安全团队的注意，所以也给了犯罪分子恶意利用的可乘之机。

**防护建议**

及时维护更新API库存表可以尽可能减少影子API或僵尸API的存在。为此，组织必须要求IT团队跟踪和监视所有正在运行的API，以查找未解决的漏洞、故障或错误配置。组织还可以利用自动化API安全工具（如AppTrana）进行API库存跟踪。此外，所有开发人员和相关人员都应该确保所有API都有规范的文档进行说明和映射。

风险二

不安全的资源展示

一些API需要向客户端显示可用资源列表以供使用者及时了解。该列表可能包括“用户”或“小部件”等元素，当通过浏览器查看时，这些元素会以有组织的“分页”（paginated）方式呈现。虽然这听起来很有帮助，但任何展示资产信息（explicit information，如用户的PII数据和资源列表）的API都容易遭受来自攻击者的数据抓取，并从中提取敏感信息，例如受影响的web应用程序使用情况、客户电子邮件列表等等。

**防护建议**

可以限制展示分页和资源列表的显示，以避免数据被恶意抓取。例如为查看特定资源的API调用指定一个时间段。或者，为用户设置API访问密钥，并限制API密钥可能被使用的次数，超过次数将撤销访问并阻止API连接。

风险三

未经身份验证的API

很多企业中存在大量历史遗留应用程序，因此，使用API而不进行身份验证是目前很常见的现象。这些未经身份验证的API一旦公开暴露，就会对企业的应用系统安全构成威胁。虽然如何管理遗留API本身就是一种风险，但让未经身份验证的API获取敏感数据（如PII）对于企业将是一个更大的安全隐患，甚至会产生法规遵从和合规性方面的问题。

**防护建议**

强制进行API身份验证，以防止未经请求的API访问敏感数据资源。虽然它可能不是一个完善的解决方案，但实现身份验证可以控制API的访问范围，也能帮助IT管理人员在恶意访问尝试的情况下识别出访问入口点。IT团队还应该定期进行API检查，以确保足够的API安全性，特别是在升级遗留应用程序或报废与这些API相关的老旧设备时。

风险四

未经授权的API

对所有API进行强制身份验证本身并非一个完善的、有包容性的解决方案。安全团队还应该实现对API的授权访问管理，以将安全风险降至最低。使用经过身份验证但未经授权的API是IT团队经常难以解决的固有API安全风险。攻击者可以通过各种方法（例如枚举用户标识符）获得经过身份验证的访问，而不考虑拟攻击用户的权限级别，从而大量利用此类未经合理授权的API。

**防护建议**

应用程序开发人员经常忽略对API进行合理授权，而经过身份验证的用户就可以对API执行任何预期的操作。因此，防止这种未经授权的API访问需要开发人员实现安全检查，例如用户ID或创建访问控制列表，以限制通过身份验证的用户访问不属于他们的API数据。

风险五

公开暴露的API密钥

当不同的应用系统进行交互时，就需要通过API进行连接，这时候就需要一个密钥进行安全性确认。开发人员应该在整合这些应用时，保证密钥的安全性。但是很多开发人员为了工作方便，会在开发过程中将API认证密钥直接嵌入到API中，但是之后也未及时删除。一旦这个API密钥被攻击者查询获得，就能够以关联合法用户的身份，进行各种非法操作。

**防护建议**

一般的做法应该是只将密钥暴露给指定的用户。而从长远来看，在开发阶段就有效规范安全管理流程可以防止密钥泄露和恶意抓取等API应用威胁。

风险六

API监控不足

API监控不足也可归因于企业对API应用安全性的忽视。当API应用缺少监控时，会给潜在的攻击者足够的时间来建立对受损API的访问并保持长期连接。这种隐形攻击可能导致企业财产、商誉和数据资产的损失。根据OWASP的说法，组织检测修复漏洞的平均时间约为200多天，因此IT人员需要在更短时间里发现API应用的异常情况。

**防护建议**

企业要对API的应用安全问题提高警惕。常规的API日志记录不应该局限于API请求。相反地，它必须涵盖用户行为分析并存储大约一年的日志。组织必须定期开展API安全应用审计，以确保足够的API日志记录和安全的日志存储。

风险七

应用服务器安全性差

不安全的应用服务器可能泄漏大量数据，不安全或配置错误的API应用也反映出组织存在巨大的网络安全缺口。当开发人员未能部署基本的安全措施（如实现HTTPS通信）时，通常会出现此问题。不幸的是，许多web应用程序仍然支持HTTP通信，这样就会轻易暴露API密钥等敏感数据。由于web浏览器并不直接处理API，像HTTPS-redirect（重定向）这样的特性在这里不能受到任何保护。

**防护建议**

采用HTTPS-only-like方法是防止应用服务意外数据暴露的关键。开发人员还可以通过部署负载均衡设备，实现利用SSL来加密数据和阻止不安全的HTTP请求。

**参考资料**

**https://latesthackingnews.com/2022/12/21/are-these-7-security-gaps-in-your-apis/**

**《API安全趋势调查报告》：****https://salt.security/api-security-trends**

相关阅读

[敏感数据保护的基石：API资产发现与管理](http://mp.weixin.qq.com/s?__biz=MjM5Njc3NjM4MA==&mid=2651116102&idx=2&sn=64c03c65bfc0ed3438183e0ae4a11ba4&chksm=bd1462958a63eb83a4054b42eb3359583cb588ab4fbd19bb9fc99b049de16d5f164d249a23b2&scene=21#wechat_redirect)

[API应用数量已近2亿，如何应对API蔓延的安全风险与挑战？](http://mp.weixin.qq.com/s?__biz=MjM5Njc3NjM4MA==&mid=2651119607&idx=1&sn=ac6b26bb8668cb2ea394e7f47f67982d&chksm=bd146f248a63e632568673a701febf3b49fc4b57d9d4870148d81745cc268d4371ce4000f27c&scene=21#wechat_redirect)

![](https://mmbiz.qpic.cn/mmbiz_gif/kuIKKC9tNkAZYNibk7aDDd0hAkQGzOfLPfjXUPaypbuDrr5exabqWXmSOeZVUZtP6zqw9YGWib9xNQdvx1iaCicTUA/640?wx_fmt=gif&wxfrom=5&wx_lazy=1)

合作电话：18311333376

合作微信：aqniu001

投稿邮箱：editor@aqniu.com

![](https://mmbiz.qpic.cn/mmbiz_gif/kuIKKC9tNkAfZibz9TQ8KWj4voxxxNSGMAGiauAWicdDiaVl8fUJYtSgichibSzDUJvsic9HUfC38aPH9ia3sopypYW8ew/640?wx_fmt=gif&wxfrom=5&wx_lazy=1)

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/kuIKKC9tNkBZmyIrtuKu5NvaM1vicN8Y6b8TFgIImLsIf7G7sbQcuymdibuezvQtS7YgVtEibUWQlqXsxiaviagrB9A/0?wx_fmt=png)

安全牛

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/kuIKKC9tNkBZmyIrtuKu5NvaM1vicN8Y6b8TFgIImLsIf7G7sbQcuymdibuezvQtS7YgVtEibUWQlqXsxiaviagrB9A/0?wx_fmt=png)

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