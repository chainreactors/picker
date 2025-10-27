---
title: CoGUI Phish Kit模仿知名公司攻击用户并窃取凭据
url: https://www.anquanke.com/post/id/307199
source: 安全客-有思想的安全新媒体
date: 2025-05-09
fetch_date: 2025-10-06T22:23:38.000290
---

# CoGUI Phish Kit模仿知名公司攻击用户并窃取凭据

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

# CoGUI Phish Kit模仿知名公司攻击用户并窃取凭据

阅读量**85555**

发布时间 : 2025-05-08 15:41:43

**x**

##### 译文声明

本文是翻译文章，文章原作者 图沙尔 苏布拉 杜塔，文章来源：cybersecuritynews

原文地址：<https://cybersecuritynews.com/cogui-phish-kit-impersonate-well-known-companies/>

译文仅供参考，具体内容表达以及含义原文为准。

自2024年10月以来,一个名为CoGUI的复杂网络钓鱼框架已成为一个重大威胁,主要针对日本的组织提供数百万条网络钓鱼消息。

该套件冒充流行的消费者和金融品牌,包括亚马逊,PayPay,乐天和各种金融机构,以欺骗用户泄露敏感信息。

活动量从数十万到数千万条,[根据竞选量](https://cybersecuritynews.com/new-phishing-campaign-attacking-investors/),日本已成为最具针对性的国家之一。

网络钓鱼攻击使用精心制作的电子邮件,模仿可信品牌的合法通信。

这些消息通常会产生紧迫感,促使收件人单击导致伪造身份验证页面的嵌入式URL。

一旦定向到这些页面,受害者将被要求输入他们的凭据和付款信息,然后由攻击者收集。

最近几个月,威胁行为者甚至利用了时事,一些运动在美国政府宣布互惠关税后使用以关税为主题的诱惑。

[identified](https://www.proofpoint.com/us/blog/threat-insight/cogui-phish-kit-targets-japan-millions-messages)Proofpoint研究人员在2024年12月发现了CoGUI网络钓鱼试剂盒,此后一直在跟踪其演变和部署。

研究人员指出,总消息量在2025年1月达到顶峰,仅当月就观察到超过1.72亿条消息。

根据Proofpoint的分析,虽然日本组织仍然是主要目标,但也观察到一些针对澳大利亚,新西兰,加拿大和美国用户的活动。

[evasion techniques](https://cybersecuritynews.com/vipersoftx-evasion-analysis/)CoGUI特别危险的是其复杂的规避技术以及窃取数据的全面性。

![]()

除了用户名和密码之外,网络钓鱼套件还旨在捕获支付卡详细信息,为受害者带来重大财务风险。

这一活动与日本金融厅最近关于网络钓鱼活动增加导致金融盗窃的报道一致。

## 先进的逃生技术

[defense](https://cybersecuritynews.com/proactive-phishing-defense/)CoGUI套件采用多层防御规避,使其特别难以检测。

其规避策略的核心是复杂的浏览器分析,可以收集信息,包括IP地址的地理位置,浏览器语言配置,浏览器类型和版本,屏幕尺寸,操作系统平台和设备类型。

这种分析有两个目的:针对特定受害者和逃避自动分析系统。

当潜在受害者访问CoGUI钓鱼页面时,该工具包首先评估浏览器是否符合其目标标准。

如果配置文件验证得到满足,[它提供旨在窃取凭据的钓鱼页面。](https://cybersecuritynews.com/trellix-unveils-new-phishing-simulator/)但是,如果验证失败,受害者将被重定向到与冒充品牌相匹配的合法网站,从而有效地掩盖了攻击尝试。

例如,如果phish欺骗“Amazon.co.jp”并且验证失败,访问者将无缝地重定向到合法的日本亚马逊网站,不会留下任何企图攻击的痕迹。

这种针对受害者目标和逃沙的复杂方法,加上地理围栏和头部击剑技术,证明了为什么CoGUI在其活动中如此成功,以及为什么Proofpoint评估它可能被多个主要针对日语威胁行为者使用。

本文翻译自cybersecuritynews [原文链接](https://cybersecuritynews.com/cogui-phish-kit-impersonate-well-known-companies/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/307199](/post/id/307199)

安全KER - 有思想的安全新媒体

本文转载自: [cybersecuritynews](https://cybersecuritynews.com/cogui-phish-kit-impersonate-well-known-companies/)

如若转载,请注明出处： <https://cybersecuritynews.com/cogui-phish-kit-impersonate-well-known-companies/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [安全资讯](/tag/%E5%AE%89%E5%85%A8%E8%B5%84%E8%AE%AF)

**+1**1赞

收藏

![](https://p4.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p3.ssl.qhimg.com/t014757b72460d855bf.png)

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

* [先进的逃生技术](#h2-0)

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