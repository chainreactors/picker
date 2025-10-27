---
title: Gabagool： 利用 Cloudflare R2 的复杂网络钓鱼工具包
url: https://www.anquanke.com/post/id/302024
source: 安全客-有思想的安全新媒体
date: 2024-11-21
fetch_date: 2025-10-06T19:13:58.071114
---

# Gabagool： 利用 Cloudflare R2 的复杂网络钓鱼工具包

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

# Gabagool： 利用 Cloudflare R2 的复杂网络钓鱼工具包

阅读量**45345**

发布时间 : 2024-11-20 14:17:42

**x**

##### 译文声明

本文是翻译文章，文章原作者 do son，文章来源：securityonline

原文地址：<https://securityonline.info/gabagool-a-sophisticated-phishing-kit-exploiting-cloudflare-r2/>

译文仅供参考，具体内容表达以及含义原文为准。

![Gabagool Phishing Kit]()

TRAC Labs 在一份详细的分析报告中揭露了一个名为 Gabagool 的网络钓鱼活动，其目标是企业和政府员工。该活动利用 Cloudflare R2 存储服务的信誉绕过安全措施。

Gabagool 通过入侵员工的电子邮件帐户开始其感染链。被入侵的账户会向其他员工发送钓鱼邮件，在图片或文档中嵌入恶意链接。例如，图片可能标注为 “已收到新传真文档”，其中嵌入的 URL 会引导受害者访问 SharePoint 或 Box 等看似合法的文件共享平台。

“这些电子邮件会提示收件人查看电子邮件中伪装成文档的附件图片。图片中嵌入了一个恶意 URL 短链，利用 tiny.cc 和 tiny.pl，其中包含一个重定向链”。

![]()
重定向 URL | 图片： TRAC 实验室

然而，这些重定向会指向托管在 Cloudflare R2 桶中的钓鱼网页。报告指出：“威胁行为者可以通过在这些桶中托管恶意内容或钓鱼登陆页面，利用 Cloudflare 的可信声誉绕过安全过滤器，从而滥用 Cloudflare R2 桶进行钓鱼。”

Gabagool 网络钓鱼工具包采用混淆的 JavaScript 和复杂的僵尸检测机制来规避安全措施。主要功能包括

* **僵尸检测：** 钓鱼页面使用检测无头浏览器（如 Selenium）、监控鼠标移动和测试禁用 cookies 等检查手段。如果怀疑有僵尸活动，就会将用户重定向到合法网站。
* **凭证收集：** 一旦用户通过了僵尸检查，网络钓鱼页面就会加载凭证收集表单。收集到的凭据在发送到攻击者控制的服务器之前会使用 AES 加密。

Gabagool 活动已经影响了许多组织，尤其是金融和政府等行业。它使用先进的规避技术和可信平台，使其成为一个危险的威胁。

本文翻译自securityonline [原文链接](https://securityonline.info/gabagool-a-sophisticated-phishing-kit-exploiting-cloudflare-r2/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/302024](/post/id/302024)

安全KER - 有思想的安全新媒体

本文转载自: [securityonline](https://securityonline.info/gabagool-a-sophisticated-phishing-kit-exploiting-cloudflare-r2/)

如若转载,请注明出处： <https://securityonline.info/gabagool-a-sophisticated-phishing-kit-exploiting-cloudflare-r2/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [网络攻击](/tag/%E7%BD%91%E7%BB%9C%E6%94%BB%E5%87%BB)

**+1**0赞

收藏

![](https://p5.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p0.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p5.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=173683)

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