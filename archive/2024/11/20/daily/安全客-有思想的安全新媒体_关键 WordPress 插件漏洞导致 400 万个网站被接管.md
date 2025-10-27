---
title: 关键 WordPress 插件漏洞导致 400 万个网站被接管
url: https://www.anquanke.com/post/id/301978
source: 安全客-有思想的安全新媒体
date: 2024-11-20
fetch_date: 2025-10-06T19:15:12.335690
---

# 关键 WordPress 插件漏洞导致 400 万个网站被接管

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

# 关键 WordPress 插件漏洞导致 400 万个网站被接管

阅读量**48813**

发布时间 : 2024-11-19 10:41:49

**x**

##### 译文声明

本文是翻译文章，文章原作者 Elizabeth Montalbano，文章来源：darkreading

原文地址：<https://www.darkreading.com/cloud-security/critical-wordpress-plugin-flaw-4m-sites-takeover>

译文仅供参考，具体内容表达以及含义原文为准。

![WordPress logo displayed on mobile device screen next to homepage of WordPress website displayed on laptop screen]()

安装在 400 多万个网站上的一个 WordPress 插件存在一个脚本漏洞，可能会被用于对多个网站发起大规模自动攻击，从而导致网站被完全管理接管。

Wordfence公司的研究人员称这个身份验证绕过漏洞是他们发现的 “最严重的漏洞之一”，他们在本月早些时候在Really Simple Security公司的一个为网站提供WordPress安全功能的插件中发现了这个漏洞。该漏洞的关键 CVSS 得分为 9.8，影响到 9.0.0 至 9.1.1.1 版本的 Really Simple Security Pro 和 Pro Multisite 插件。

Wordfence安全研究员Istvan Marton在帖子中写道：“当启用双因素身份验证（2FA）功能时，攻击者可以通过该漏洞远程访问网站上的任何账户，包括管理员账户。”

据 Wordfence 称，该漏洞的存在是由于双因素 REST API 操作中 “check\_login\_and\_get\_user ”函数的用户检查错误处理不当造成的。此外，由于该漏洞是可编写脚本的，因此可以通过自动化方式同时对多个 WordPress 网站进行攻击。

鉴于该漏洞的严重性，Wordfence 在 11 月 6 日发现该漏洞后迅速采取行动，与 Really Simple Security 团队合作缓解该漏洞。在立即向供应商披露该漏洞后，Wordfence 于 11 月 12 日公开发布了 9.1.2 版本的修补更新。然后，在Wordfence的建议下，Really Simple Security在两天后强制更新了所有运行该插件的网站。

尽管如此，Wordfence仍建议任何使用该插件的网站管理员确认该插件是否已自动更新到补丁版本，因为 “没有有效许可证的网站可能没有自动更新功能”，Marton在帖子中指出。

**新的 “真正简单的安全 ”功能引入漏洞**

Really Simple Security 插件的前身是 Really Simple SSL；它在最新的重大版本更新中更名为 Really Simple SSL，同时还扩展了该插件的登录保护、漏洞检测和 2FA 等安全功能。

在这次更新中，添加 2FA 的功能之一 “被不安全地实施”，从而引入了漏洞，攻击者可以创建一个简单的请求来访问任何开启了 2FA 的用户账户。

具体来说，该插件使用 Rsssl\_Twoo\_Factor\_On\_Board\_Api 类中的 skip\_onboarding()函数来处理通过 REST API 进行的身份验证，一旦失败就会返回 WP\_REST\_Response 错误。然而，这并没有在函数中进行处理，这 “意味着即使在非ce无效的情况下，函数处理仍会继续，并调用 authenticate\_and\_redirect()，”Marton 写道。他写道：”这将根据请求中传递的用户 ID 对用户进行身份验证，即使该用户的身份尚未得到验证。

最终，这使得威胁行为者有可能绕过身份验证，访问运行漏洞插件版本的网站上的任意账户。

Marton解释说：“一如既往，身份验证绕过漏洞和由此导致的对高权限用户账户的访问，使威胁行为者很容易完全攻陷有漏洞的WordPress网站并进一步感染它。”

**Wordfence： 传播信息，检查插件**

由于 WordPress 平台作为数百万网站的基础被广泛使用，因此它及其插件尤其是威胁行为者最喜欢攻击的目标，这让他们很容易接触到广泛的攻击面。攻击者尤其喜欢利用安装量大的单个插件，因此，像在 Really Simple Security 插件中发现的漏洞这样的漏洞就成了有吸引力的攻击目标。

尽管大多数使用该插件的网站应该已经进行了更新，但 Wordfence 仍建议用户传播消息，以确保由于该漏洞的严重性而尽可能广泛地覆盖补丁。

Marton在帖子中写道：“如果你知道有人在自己的网站上使用这些插件，我们建议你与他们分享这个警告，以确保他们网站的安全，因为这个漏洞会带来巨大的风险。”

本文翻译自darkreading [原文链接](https://www.darkreading.com/cloud-security/critical-wordpress-plugin-flaw-4m-sites-takeover)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/301978](/post/id/301978)

安全KER - 有思想的安全新媒体

本文转载自: [darkreading](https://www.darkreading.com/cloud-security/critical-wordpress-plugin-flaw-4m-sites-takeover)

如若转载,请注明出处： <https://www.darkreading.com/cloud-security/critical-wordpress-plugin-flaw-4m-sites-takeover>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [漏洞](/tag/%E6%BC%8F%E6%B4%9E)
* [漏洞情报](/tag/%E6%BC%8F%E6%B4%9E%E6%83%85%E6%8A%A5)

**+1**0赞

收藏

![](https://p1.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p4.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p1.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=173683)

[安全客](/member.html?memberId=173683)

这个人太懒了，签名都懒得写一个

* 文章
* **553**

* 粉丝
* **2**

### TA的文章

* ##### [年度盘点：AI+安全双重赋能，360解锁企业浏览器新动力](/post/id/303791)

  2025-01-24 10:00:53
* ##### [IntelBroker 的数字足迹： OSINT 分析揭露网络犯罪分子的行动](/post/id/303788)

  2025-01-24 09:55:58
* ##### [7-Zip 修复了可绕过 Windows MoTW 安全警告的错误，立即修补](/post/id/303776)

  2025-01-24 09:49:56
* ##### [Microsoft 在 Edge Stable 中预览 Game Assist 游戏内浏览器](/post/id/303773)

  2025-01-24 09:43:16
* ##### [ModiLoader 恶意软件利用 CAB 标头批处理文件逃避检测](/post/id/303770)

  2025-01-24 09:36:10

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