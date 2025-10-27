---
title: 关键的 Roundcube 漏洞存在电子邮件系统被破坏的风险
url: https://www.anquanke.com/post/id/308096
source: 安全客-有思想的安全新媒体
date: 2025-06-05
fetch_date: 2025-10-06T22:49:30.759308
---

# 关键的 Roundcube 漏洞存在电子邮件系统被破坏的风险

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

# 关键的 Roundcube 漏洞存在电子邮件系统被破坏的风险

阅读量**100809**

发布时间 : 2025-06-04 15:36:00

**x**

##### 译文声明

本文是翻译文章，文章来源：webpronews

原文地址：<https://www.webpronews.com/critical-roundcube-flaw-risks-email-system-compromise/>

译文仅供参考，具体内容表达以及含义原文为准。

在不断发展的网络安全格局中,Roundcube Webmail中新披露的漏洞在行业中引发了冲击波,暴露了一个持续十年未被发现的关键缺陷。

![]()

在不断发展的网络安全格局中,Roundcube Webmail中新披露的漏洞在行业中引发了冲击波,暴露了一个持续十年未被发现的关键缺陷。

该漏洞被识别为CVE-2025-49113,在1.6.11之前影响Roundcube版本,并允许经过身份验证的用户通过巧妙制作的URL漏洞执行恶意代码,从而可能危及整个电子邮件系统。

该漏洞由The Hacker News广泛详细介绍,以Roundcube处理某些URL的缺陷为中心,为攻击者创建一个入口点,以注入和执行任意代码。这不是一个理论风险,其影响是直接和严重的,因为它只需要最少的访问权限就可以对系统造成严重破坏,使其成为寻求利用全球数百万人使用的可信网络邮件平台的威胁行为者的主要目标。

让这一发现特别令人担忧的是它的长寿。据《黑客新闻》报道,该漏洞已经存在了10多年,通过无数更新和安全审计逃避了检测。这引发了关于广泛使用的开源软件中遗留代码的稳健性以及在复杂,不断发展的生态系统中维护安全的挑战的关键问题。

国家漏洞数据库的进一步见解显示,CVE-2025-49113由于其远程代码执行的潜力而具有很高的严重等级。这种分类强调了管理员立即修补其系统的紧迫性,因为漏洞利用不需要超出基本身份验证的高级权限,从而降低了攻击者的障碍。

**剥削与现实世界的风险**

漏洞的机制是令人毛骨悚然的简单但毁灭性的。根据Fearsoff发表的研究,攻击者可以操纵URL,欺骗Roundcube处理恶意有效载荷,有效地将良性的Web邮件界面转变为更广泛的系统妥协的网关。这可能导致数据被盗,未经授权访问敏感通信,甚至在组织基础设施内部署勒索软件。

对于依赖安全电子邮件通信的行业,如政府机构、金融机构和医疗保健提供商,其影响尤其严重。Fearsoff的分析强调,虽然该漏洞需要身份验证,但网络钓鱼活动或受损凭据很容易为攻击者利用此漏洞提供必要的立足点。

**为行业行动呼吁**

随着Roundcube版本1.6.11及更高版本的补丁变得可用,系统管理员有责任迅速采取行动。黑客新闻强调,延迟更新可能会使组织受到积极利用,特别是考虑到漏洞的公开披露。网络安全社区还必须反思这样一个关键错误是如何隐藏了十年的,这促使了对代码审计实践的重新评估。

除了立即补救之外,这一事件还清楚地提醒人们采取积极主动的安全措施的重要性。定期渗透测试、及时更新和网络钓鱼风险用户教育对于减轻类似威胁至关重要。正如国家漏洞数据库所指出的,在补丁被普遍应用之前,利用的窗口是敞开的,这使得这成为全世界捍卫者的时间竞赛。

本文翻译自webpronews [原文链接](https://www.webpronews.com/critical-roundcube-flaw-risks-email-system-compromise/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/308096](/post/id/308096)

安全KER - 有思想的安全新媒体

本文转载自: [webpronews](https://www.webpronews.com/critical-roundcube-flaw-risks-email-system-compromise/)

如若转载,请注明出处： <https://www.webpronews.com/critical-roundcube-flaw-risks-email-system-compromise/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [漏洞分析](/tag/%E6%BC%8F%E6%B4%9E%E5%88%86%E6%9E%90)
* [安全知识](/tag/%E5%AE%89%E5%85%A8%E7%9F%A5%E8%AF%86)
* [安全头条](/tag/%E5%AE%89%E5%85%A8%E5%A4%B4%E6%9D%A1)

**+1**0赞

收藏

![](https://p0.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p5.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p0.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=170061)

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

* ##### [论韧性数字安全体系（第十三章）](/post/id/309219)

  2025-07-01 15:03:14
* ##### [AI即万物：ISC.AI 2025的跨越变迁](/post/id/308744)

  2025-06-20 18:39:26
* ##### [无文件 AsyncRAT 活动利用隐蔽的 PowerShell 有效载荷攻击德国用户](/post/id/308562)

  2025-06-18 15:22:31
* ##### [起亚厄瓜多尔无钥匙进入系统漏洞导致数千辆车辆被盗](/post/id/308480)

  2025-06-16 15:48:35
* ##### [微软 Office 漏洞允许攻击者执行远程代码](/post/id/308412)

  2025-06-12 15:43:53
* ##### [美国CISA警告 SinoTrack GPS 跟踪器存在远程控制漏洞](/post/id/308398)

  2025-06-12 15:15:38
* ##### [Cyera融资5.4亿美元，估值翻番，致力于人工智能数据保护](/post/id/308391)

  2025-06-12 14:36:27

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