---
title: 严重的Samliify NSO缺陷允许攻击者以管理员身份登录
url: https://www.anquanke.com/post/id/307644
source: 安全客-有思想的安全新媒体
date: 2025-05-23
fetch_date: 2025-10-06T22:27:06.450833
---

# 严重的Samliify NSO缺陷允许攻击者以管理员身份登录

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

# 严重的Samliify NSO缺陷允许攻击者以管理员身份登录

阅读量**104181**

发布时间 : 2025-05-22 15:08:23

**x**

##### 译文声明

本文是翻译文章，文章原作者 比尔 图拉斯，文章来源：bleepingcomputer

原文地址：<https://www.bleepingcomputer.com/news/security/critical-samlify-sso-flaw-lets-attackers-log-in-as-admin/>

译文仅供参考，具体内容表达以及含义原文为准。

![登录提示]()

已经发现了一个关键的Samlify身份验证旁路漏洞,该漏洞允许攻击者通过向合法签名的SAML响应注入未签名的恶意断言来冒充管理员用户。

Samlify是一个高级身份验证库,可帮助开发人员将SAML SSO和Single Loot-Out(SLO)集成到Node.js应用程序中。它是使用SAML构建或连接到身份提供商(IdP)和服务提供商(SP)的流行工具。

该库被SaaS平台,为内部工具实施SSO的组织,与Azure AD或Okta等企业身份提供商集成的开发人员以及联合身份管理场景中使用。它非常受欢迎,每周在npm上下载量超过20万次。

该缺陷,[跟踪为CVE-2025-47949](https://nvd.nist.gov/vuln/detail/CVE-2025-47949),是一个关键(CVSS v4.0得分:9.9)签名包装缺陷,影响2.10.0之前所有版本的Samlify。

正如EndorLabs在报告中解释的那样,Samlify正确验证了提供用户身份的XML文档已签名。尽管如此,它还是会从XML的一部分中读取虚假的断言。

通过拦截或通过公共元数据持有有效签名的 SAML 响应的攻击者可以对其进行修改,以利用库中的解析漏洞并作为其他人进行身份验证。

攻击者会获取这个合法签名的 XML 文档并对其进行操作。他们在文档中插入第二个恶意的SAML断言,“EndorLabs解释道。

“此恶意断言包含目标用户的身份(例如,管理员的用户名)。

“关键部分是原始文档中的有效签名仍然适用于XML结构的良性部分,但SP的易受攻击的解析逻辑将无意中处理未签名的恶意断言。

这是一个完整的 SSO 旁路,允许未经授权的远程攻击者执行权限升级并作为管理员登录。

攻击者不需要用户交互或特权,唯一的要求是访问有效签名的 XML blob,这使得利用相对简单。

为了降低风险,建议用户升级到本月早些时候发布的Samlify版本2.10.0。

请注意,GitHub仍然提供2.9.1作为最新版本,npm hosts但npm在编写时托管安全使用的2.10.0。

目前还没有关于在野外积极利用CVE-2025-47949的报告,但建议受影响的用户立即采取行动并保护他们的环境。

本文翻译自bleepingcomputer [原文链接](https://www.bleepingcomputer.com/news/security/critical-samlify-sso-flaw-lets-attackers-log-in-as-admin/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/307644](/post/id/307644)

安全KER - 有思想的安全新媒体

本文转载自: [bleepingcomputer](https://www.bleepingcomputer.com/news/security/critical-samlify-sso-flaw-lets-attackers-log-in-as-admin/)

如若转载,请注明出处： <https://www.bleepingcomputer.com/news/security/critical-samlify-sso-flaw-lets-attackers-log-in-as-admin/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [漏洞分析](/tag/%E6%BC%8F%E6%B4%9E%E5%88%86%E6%9E%90)
* [安全知识](/tag/%E5%AE%89%E5%85%A8%E7%9F%A5%E8%AF%86)
* [网络攻击](/tag/%E7%BD%91%E7%BB%9C%E6%94%BB%E5%87%BB)
* [网络安全热点](/tag/%E7%BD%91%E7%BB%9C%E5%AE%89%E5%85%A8%E7%83%AD%E7%82%B9)

**+1**3赞

收藏

![](https://p4.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p0.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p4.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=170061)

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

* ##### [Morte僵尸网络被披露：正利用路由器与企业应用漏洞，迅速扩张其“加载器即服务”活动](/post/id/312444)

  2025-09-29 18:04:01
* ##### [Akira勒索软件利用SonicWall VPN账户发起急速入侵](/post/id/312438)

  2025-09-29 18:03:28
* ##### [DarkCloud信息窃取器现新变种：采用VB6混淆技术并新增加密货币钱包窃取功能，威胁显著升级](/post/id/312435)

  2025-09-29 18:02:53
* ##### [TamperedChef恶意软件兴起：欺诈应用利用经过签名的二进制文件与搜索引擎投毒劫持浏览器](/post/id/312432)

  2025-09-29 18:02:25
* ##### [黑客将SVG文件武器化，用于隐秘投递恶意负载](/post/id/312351)

  2025-09-24 16:44:10
* ##### [ShadowV2僵尸网络利用配置错误的AWS Docker容器构建DDoS攻击租用服务](/post/id/312381)

  2025-09-24 16:40:43
* ##### [npm软件包“fezbox”中被发现新型恶意软件，可利用二维码窃取用户凭据](/post/id/312387)

  2025-09-24 16:40:06

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