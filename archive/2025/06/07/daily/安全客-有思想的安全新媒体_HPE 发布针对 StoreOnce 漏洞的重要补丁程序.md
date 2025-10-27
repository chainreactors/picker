---
title: HPE 发布针对 StoreOnce 漏洞的重要补丁程序
url: https://www.anquanke.com/post/id/308181
source: 安全客-有思想的安全新媒体
date: 2025-06-07
fetch_date: 2025-10-06T22:50:05.149448
---

# HPE 发布针对 StoreOnce 漏洞的重要补丁程序

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

# HPE 发布针对 StoreOnce 漏洞的重要补丁程序

阅读量**171214**

发布时间 : 2025-06-06 15:04:41

**x**

##### 译文声明

本文是翻译文章，文章来源：webpronews

原文地址：<https://www.deepl.com/zh/translator#en/zh-hans/HPE%20Issues%20Critical%20Patch%20for%20StoreOnce%20Vulnerabilities>

译文仅供参考，具体内容表达以及含义原文为准。

![]()

在针对企业IT环境的关键更新中,Hewlett Packard Enterprise推出了一个安全补丁,解决其StoreOnce备份和重复数据删除解决方案中的多个漏洞,这是许多组织数据保护策略的基石。

这些漏洞共有8个漏洞,包括跟踪为CVE-2025-37093的特别严重的身份验证旁路漏洞,该漏洞可能允许攻击者获得未经授权的访问权限,并可能在受影响的系统上执行远程代码。这一发展在整个行业中引发了涟漪,因为StoreOnce广泛部署在数据中心,以优化备份存储并提高恢复速度。

这个补丁的紧迫性怎么强调都不为过。据The Hacker News报道,这个关键漏洞会带来远程代码执行(RCE)和身份验证绕过的风险,这意味着攻击者可以在没有任何用户交互的情况下破坏系统。此类漏洞是网络犯罪分子的金矿,他们越来越多地针对备份基础设施来破坏恢复过程或提取敏感数据。HPE在发布更新软件方面的迅速反应凸显了情况的严重性,因为未修补的系统可以作为更广泛网络攻击的切入点。

除了CVE-2025-37093之外,其他七个缺陷包括目录遍历攻击,服务器端请求伪造和任意文件删除等风险,每个漏洞都能够破坏数据完整性或系统稳定性。其中一个漏洞,CVE-2025-37094,可以使攻击者删除关键文件,对业务连续性构成直接威胁。正如 HPE 在其支持门户上的官方安全公告中详述的那样,这些问题会影响 4.3.11 之前的 StoreOnce 软件版本,该公司强烈建议立即升级修补版本以降低风险。

将这些漏洞联系在一起的可能性放大了它们的危险。熟练的攻击者可以利用身份验证绕过来获得初始访问,然后利用目录遍历或RCE功能在网络内横向移动。这种情况对于拥有大型互联 IT 环境的企业来说尤其令人担忧,正如 HPE 支持文档中所指出的,单个漏洞可能会导致整个系统妥协。

###

### **紧急行动和缓解战略**

HPE 通过其支持中心提供修补软件,但组织有责任迅速采取行动。这些漏洞没有已知的解决方法,使得版本4.3.11或更高版本的更新不可协商。建议IT团队将易受攻击的StoreOnce系统与不受信任的网络隔离,直到应用补丁,并根据Hacker News的建议监控未经授权的访问或异常活动的迹象。

此外,组织应考虑实施网络分割,以限制攻击者潜在的横向移动。定期审查系统管理和安全协议对于在不断演变的威胁面前保持完整性也至关重要。对于需要帮助的人,HPE 鼓励联系其支持团队,以获取有关更新流程的指导。

###

### **行业影响及前瞻性措施**

这些缺陷的披露凸显了一个更广泛的趋势:备份解决方案,曾经被认为是次要目标,现在是网络犯罪分子的主要目标。随着企业越来越依赖像StoreOnce这样的数据保护平台,保护这些系统变得与保护主要基础设施一样重要。

这一事件提醒IT领导者优先考虑补丁管理和漏洞评估。随着攻击者越来越复杂、积极主动的措施,再加上对供应商警报的快速反应,将成为无情数字威胁时代弹性网络安全战略的关键。

本文翻译自webpronews [原文链接](https://www.deepl.com/zh/translator#en/zh-hans/HPE%20Issues%20Critical%20Patch%20for%20StoreOnce%20Vulnerabilities)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/308181](/post/id/308181)

安全KER - 有思想的安全新媒体

本文转载自: [webpronews](https://www.deepl.com/zh/translator#en/zh-hans/HPE%20Issues%20Critical%20Patch%20for%20StoreOnce%20Vulnerabilities)

如若转载,请注明出处： <https://www.deepl.com/zh/translator#en/zh-hans/HPE%20Issues%20Critical%20Patch%20for%20StoreOnce%20Vulnerabilities>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [漏洞分析](/tag/%E6%BC%8F%E6%B4%9E%E5%88%86%E6%9E%90)
* [每日安全热点](/tag/%E6%AF%8F%E6%97%A5%E5%AE%89%E5%85%A8%E7%83%AD%E7%82%B9)

**+1**0赞

收藏

![](https://p3.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p0.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p3.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=170061)

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

* ##### [无文件 AsyncRAT 活动利用隐蔽的 PowerShell 有效载荷攻击德国用户](/post/id/308562)

  2025-06-18 15:22:31
* ##### [微软 Office 漏洞允许攻击者执行远程代码](/post/id/308412)

  2025-06-12 15:43:53
* ##### [航空公司向国土安全局出售乘客数据](/post/id/308408)

  2025-06-12 15:39:51
* ##### [美国政府疫苗网站被人工智能生成的内容污损](/post/id/308404)

  2025-06-12 15:36:04
* ##### [美国CISA警告 SinoTrack GPS 跟踪器存在远程控制漏洞](/post/id/308398)

  2025-06-12 15:15:38
* ##### [Cyera融资5.4亿美元，估值翻番，致力于人工智能数据保护](/post/id/308391)

  2025-06-12 14:36:27
* ##### [微软修补被阿联酋黑客利用的零日漏洞](/post/id/308384)

  2025-06-12 14:28:52

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