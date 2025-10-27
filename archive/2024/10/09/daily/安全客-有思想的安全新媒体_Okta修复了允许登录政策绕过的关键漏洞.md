---
title: Okta修复了允许登录政策绕过的关键漏洞
url: https://www.anquanke.com/post/id/300612
source: 安全客-有思想的安全新媒体
date: 2024-10-09
fetch_date: 2025-10-06T18:48:42.474888
---

# Okta修复了允许登录政策绕过的关键漏洞

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

# Okta修复了允许登录政策绕过的关键漏洞

阅读量**75711**

发布时间 : 2024-10-08 14:38:38

**x**

##### 译文声明

本文是翻译文章，文章原作者 WAQAS，文章来源：hackread

原文地址：<https://hackread.com/okta-fixes-sign-on-policy-bypass-vulnerability/>

译文仅供参考，具体内容表达以及含义原文为准。

Okta 修复了其 Classic 产品中的一个漏洞，该漏洞允许攻击者绕过登录策略。开采需要有效证件和使用”未知”装置。受影响的用户应查看系统日志。

领先的身份和访问管理提供商Okta最近宣布修补一个影响其Classic产品的重要安全漏洞。该漏洞可能允许攻击者绕过应用程序特定的登录策略，源于2024年7月17日的更新，在2024年10月4日补丁之前，该漏洞仍然可被利用。

该漏洞现已在Okta的生产环境中修复，它可能允许未经授权的用户通过绕过关键安全控制（包括设备类型限制、网络区域和某些身份验证要求）来访问应用程序。

然而，Okta确认，这一脆弱性只影响使用Okta Classic的组织，而且利用取决于多种因素，从而限制了易受系统的范围。

发生了什么

Okta 于 2024 年 9 月 27 日发现了该漏洞，经过内部调查，确定它源自 2024 年 7 月 17 日推出的软件更新。该问题是Okta Classic特有的，影响到配置了特定于应用程序的登录策略的组织，尤其是那些依赖于设备类型限制或平台全局会话策略之外的附加条件的组织。

根据Okta的安全建议，攻击者需要满足几个条件才能成功实施攻击。首先，攻击者需要访问有效的凭据-通过网络钓鱼、凭据填充或暴力攻击。其次，组织必须使用特定于应用程序的登录策略。

最后，攻击者必须使用Okta评定为”未知”用户代理类型的设备或脚本，这可能逃避标准设备类型限制的检测。一旦满足这些条件，攻击者可能已经绕过了通常需要额外认证层或设备验证的登录策略。

Okta 提供了具体的搜索建议，管理员可以使用这些建议来识别其日志中的潜在漏洞利用尝试。这包括查找设备类型标记为“未知”的意外成功身份验证事件。Okta还建议客户搜索不成功的身份验证尝试，这可能表明在成功登录之前发生了基于凭证的攻击。

此外，鼓励各组织监测用户行为中的偏差，如不熟悉的IP地址、地理位置或可能显示未经授权活动的访问时间。

专家评论

身份和访问安全提供商 Pathlock的执行官Piyush Pandey深入探讨了此类漏洞的广泛影响。在接受HackRead.com采访时，Pandey强调了严格的访问风险分析和用户的合规配置的重要性。

“自动密码管理本身不足以保护未经授权的受监管的应用程序访问风险，”潘迪说。“通过专注于严格的访问风险分析和用户的合规配置，包括对第三方身份和访问的严格管理，组织可以显著增强其安全态势，保护敏感数据，并确保符合监管要求。这种积极主动的方法可以保护客户数据和信任，并增强整体的弹性。

潘迪的评论突出表明，组织需要超越基本的密码管理，采用更全面的身份安全方法，特别是在网络攻击日益复杂的情况下。

鼓励受此漏洞影响的组织遵循Okta的详细指导，以确保在所述时间范围内不发生未经授权的访问，并在今后采取更强有力的访问管理做法。

本文翻译自hackread [原文链接](https://hackread.com/okta-fixes-sign-on-policy-bypass-vulnerability/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/300612](/post/id/300612)

安全KER - 有思想的安全新媒体

本文转载自: [hackread](https://hackread.com/okta-fixes-sign-on-policy-bypass-vulnerability/)

如若转载,请注明出处： <https://hackread.com/okta-fixes-sign-on-policy-bypass-vulnerability/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [安全资讯](/tag/%E5%AE%89%E5%85%A8%E8%B5%84%E8%AE%AF)
* [漏洞预警](/tag/%E6%BC%8F%E6%B4%9E%E9%A2%84%E8%AD%A6)
* [漏洞情报](/tag/%E6%BC%8F%E6%B4%9E%E6%83%85%E6%8A%A5)

**+1**0赞

收藏

![](https://p5.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p0.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p5.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=170061)

[安全客](/member.html?memberId=170061)

这个人太懒了，签名都懒得写一个

* 文章
* **2096**

* 粉丝
* **6**

### TA的文章

* ##### [英国通过数据访问和使用监管法案](/post/id/308719)

  2025-06-20 17:11:10
* ##### [CISA警告：严重缺陷（CVE-2025-5310）暴露加油站设备](/post/id/308715)

  2025-06-20 17:09:03
* ##### [大多数公司高估了AI治理，因为隐私风险激增](/post/id/308708)

  2025-06-20 17:05:02
* ##### [研究人员发现了有史以来最大的数据泄露事件，暴露了160亿个登录凭证](/post/id/308704)

  2025-06-20 17:02:15
* ##### [CVE-2025-6018和CVE-2025-6019漏洞利用：链接本地特权升级缺陷让攻击者获得大多数Linux发行版的根访问权限](/post/id/308701)

  2025-06-20 16:59:36

### 相关文章

* ##### [国庆重保+攻防演练大考在即！360大模型安全服务专项方案筑牢AI防线](/post/id/312460)

  2025-09-29 18:06:17
* ##### [Apache Airflow 存在权限漏洞，可导致只读用户获取敏感信息](/post/id/312457)

  2025-09-29 18:05:56
* ##### [Meta 旨在打造机器人领域的“Android”，为下一代人形AI提供通用平台](/post/id/312454)

  2025-09-29 18:05:34
* ##### [Formbricks 存在高危漏洞 (CVE-2025-59934)，攻击者可通过伪造JWT令牌导致未授权的密码重置](/post/id/312451)

  2025-09-29 18:05:05
* ##### [Notepad++ 中存在DLL劫持漏洞（CVE-2025-56383），可导致任意代码执行，且POC已公开](/post/id/312448)

  2025-09-29 18:04:33
* ##### [Morte僵尸网络被披露：正利用路由器与企业应用漏洞，迅速扩张其“加载器即服务”活动](/post/id/312444)

  2025-09-29 18:04:01
* ##### [Akira勒索软件利用SonicWall VPN账户发起急速入侵](/post/id/312438)

  2025-09-29 18:03:28

### 热门推荐

文章目录

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

Copyright © 北京奇虎科技有限公司 三六零数字安全科技集团有限公司 安全KER All Rights Reserved [京ICP备08010314号-66](https://beian.miit.gov.cn/)[![](https://icon.cnzz.com/img/pic.gif)](https://www.cnzz.com/stat/website.php?web_id=1271278035 "站长统计")

微信二维码

**X**![安全KER](https://p0.ssl.qhimg.com/t0151209205b47f2270.jpg)