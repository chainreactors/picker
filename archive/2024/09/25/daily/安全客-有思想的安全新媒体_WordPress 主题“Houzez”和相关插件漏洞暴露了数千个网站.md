---
title: WordPress 主题“Houzez”和相关插件漏洞暴露了数千个网站
url: https://www.anquanke.com/post/id/300364
source: 安全客-有思想的安全新媒体
date: 2024-09-25
fetch_date: 2025-10-06T18:25:37.072897
---

# WordPress 主题“Houzez”和相关插件漏洞暴露了数千个网站

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

# WordPress 主题“Houzez”和相关插件漏洞暴露了数千个网站

阅读量**58458**

发布时间 : 2024-09-24 14:23:00

**x**

##### 译文声明

本文是翻译文章，文章原作者 Do son ，文章来源：securityonline

原文地址：<https://securityonline.info/wordpress-theme-houzez-and-associated-plugin-vulnerabilities-expose-thousands-of-sites/>

译文仅供参考，具体内容表达以及含义原文为准。

在广泛使用的 WordPress 主题 Houzez 及其配套插件 Houzez Login Register 中发现了两个严重漏洞。Houzez 的销量超过 46,000 辆，是希望有效管理内容和房产列表的房地产中介的热门选择。新发现的漏洞可能允许未经授权的用户接管运行该主题的 WordPress 网站，从而对企业及其客户构成严重风险。

## CVE-2024-22303 （CVSS 8.8）：Houzez 主题权限提升

安全研究人员在 Houzez 主题中发现了一个**未经身份验证的权限提升漏洞**。此缺陷可能使任何未经身份验证的用户能够提升其权限，并可能通过执行一系列 HTTP 请求来接管 WordPress 网站。

存在此漏洞的原因是处理用户输入的代码缺少适当的授权检查。虽然该主题包括 nonce 检查（一种防止未经授权操作的安全措施），但任何具有 **Subscriber** 角色的用户都可以检索 nonce。如果在站点上启用了用户注册，则即使是未经身份验证的用户也可以注册并获取 nonce 令牌。

此外，主题无法验证使用参数调用操作的用户是否是该账户的实际所有者。这种疏忽允许攻击者重置**任何账户**的密码，包括管理员账户。`houzez_ajax_password_reset``$userID`

## CVE-2024-21743 （CVSS 8.8）：Houzez 登录注册插件漏洞

负责处理用户注册的必需插件 **Houzez Login Register** 也受到权限提升漏洞的影响。该操作使用用户提供的 and 参数调用函数。`houzez_agency_agent_update``wp_update_user()``$agency_user_id``$useremail`

这意味着具有 Subscriber 角色的用户（或未经身份验证的用户，如果启用了注册）可以将任何用户的电子邮件地址更改为受攻击者控制的电子邮件地址。更改电子邮件后，攻击者可以启动密码重置，将重置链接发送给自己并有效地劫持帐户。

如果您的网站使用 Houzez 主题或 Houzez Login Register 插件，则必须将主题和 Houzez Login Register 插件更新到 **3.3.0** 或更高版本。

有关更多详细信息，您可以参考 CVE-2024-22303 和 CVE-2024-21743 的 Patchstack 公告。

本文翻译自securityonline [原文链接](https://securityonline.info/wordpress-theme-houzez-and-associated-plugin-vulnerabilities-expose-thousands-of-sites/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/300364](/post/id/300364)

安全KER - 有思想的安全新媒体

本文转载自: [securityonline](https://securityonline.info/wordpress-theme-houzez-and-associated-plugin-vulnerabilities-expose-thousands-of-sites/)

如若转载,请注明出处： <https://securityonline.info/wordpress-theme-houzez-and-associated-plugin-vulnerabilities-expose-thousands-of-sites/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [漏洞情报](/tag/%E6%BC%8F%E6%B4%9E%E6%83%85%E6%8A%A5)

**+1**0赞

收藏

![](https://p4.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p5.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p4.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=170338)

[安全客](/member.html?memberId=170338)

这个人太懒了，签名都懒得写一个

* 文章
* **823**

* 粉丝
* **1**

### TA的文章

* ##### [严重的GiveWP漏洞（CVE-2024-8353）影响10万WordPress网站](/post/id/300547)

  2024-09-30 15:03:21
* ##### [Patchwork APT 的 Nexe 后门活动曝光](/post/id/300549)

  2024-09-30 15:03:07
* ##### [用户在一次复杂的钓鱼攻击中损失了价值3200万美元的spWETH](/post/id/300551)

  2024-09-30 15:02:50
* ##### [车牌信息成安全漏洞：起亚汽车远程控制风险揭示联网车辆网络安全问题](/post/id/300553)

  2024-09-30 15:02:09
* ##### [严重SQL注入漏洞影响TI WooCommerce Wishlist插件，超10万WordPress网站面临风险](/post/id/300556)

  2024-09-30 15:01:53

### 相关文章

* ##### [Apache Airflow 存在权限漏洞，可导致只读用户获取敏感信息](/post/id/312457)

  2025-09-29 18:05:56
* ##### [Formbricks 存在高危漏洞 (CVE-2025-59934)，攻击者可通过伪造JWT令牌导致未授权的密码重置](/post/id/312451)

  2025-09-29 18:05:05
* ##### [Notepad++ 中存在DLL劫持漏洞（CVE-2025-56383），可导致任意代码执行，且POC已公开](/post/id/312448)

  2025-09-29 18:04:33
* ##### [CISA称黑客利用GeoServer漏洞成功入侵一联邦机构](/post/id/312347)

  2025-09-24 16:45:06
* ##### [SolarWinds紧急发布补丁，修复高危远程代码执行漏洞CVE-2025-26399](/post/id/312357)

  2025-09-24 16:43:11
* ##### [Chrome浏览器存在高危漏洞，可致攻击者窃取敏感信息并引发系统崩溃](/post/id/312366)

  2025-09-24 16:42:08
* ##### [CVE-2025-55241：CVSS评分10.0的Microsoft Entra ID漏洞可能危及全球所有租户](/post/id/312294)

  2025-09-22 18:14:51

### 热门推荐

文章目录

* [CVE-2024-22303 （CVSS 8.8）：Houzez 主题权限提升](#h2-0)
* [CVE-2024-21743 （CVSS 8.8）：Houzez 登录注册插件漏洞](#h2-1)

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