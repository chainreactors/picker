---
title: O2 UK修复了从呼叫元数据中泄露移动用户位置的错误
url: https://www.anquanke.com/post/id/307667
source: 安全客-有思想的安全新媒体
date: 2025-05-23
fetch_date: 2025-10-06T22:27:01.948209
---

# O2 UK修复了从呼叫元数据中泄露移动用户位置的错误

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

# O2 UK修复了从呼叫元数据中泄露移动用户位置的错误

阅读量**104248**

发布时间 : 2025-05-22 15:31:00

**x**

##### 译文声明

本文是翻译文章，文章原作者 比尔 图拉斯，文章来源：bleepingcomputer

原文地址：<https://www.bleepingcomputer.com/news/security/o2-uk-patches-bug-leaking-mobile-user-location-from-call-metadata/>

译文仅供参考，具体内容表达以及含义原文为准。

![天线]()

O2 UK实施VoLTE和WiFi呼叫技术的缺陷可能允许任何人通过呼叫目标来暴露一个人和其他标识符的一般位置。

安全研究员丹尼尔·威廉姆斯(Daniel Williams)发现了这个问题。自2023年2月以来,O2英国网络可能存在该漏洞,并于昨天得到解决。

O2 UK是Virgin Media O2旗下的英国电信服务提供商。截至2025年3月,该公司报告称,英国各地拥有近2300万移动客户和580万宽带客户,使其成为该国主要提供商之一。

2017年3月,该公司推出了IP多媒体子系统(IMS)服务,标有“4G通话”,以提高通话时的音频质量和线路可靠性。

然而,正如威廉姆斯在分析此类呼叫期间的流量时发现的那样,通信方之间交换的信号消息(SIP Headers)过于冗长和揭示,包括IMSI,IMEI和单元格位置数据。

“我从网络得到的回复非常详细和漫长,与我以前在其他网络上看到的任何东西都不同,”威廉姆斯解释道。

“这些消息包含信息,例如O2(Mavenir UAG)使用的IMS / SIP服务器以及版本号,C ++服务在出现问题时处理呼叫信息时偶尔出现的错误消息,以及其他调试信息。

![SIP Headers 中暴露的信息]()

**SIP Headers 中暴露的信息**
*资料来源:mastdatabase.co.uk*

##

## 通过呼叫定位用户

使用根植的Google Pixel 8上的网络信号大师(NSG)应用程序,Williams拦截了在通话过程中交换的原始IMS信号消息,并解码了单元格ID以找到呼叫接收者连接到的最后一个蜂窝塔。

然后,他使用公共工具提供蜂窝塔图来查找塔的地理坐标。

![定位细胞塔]()

**定位细胞塔**
*资料来源:mastdatabase.co.uk*

对于塔层密集的城市地区,精度将达到100平方米(1076平方英尺)。在农村地区,地理定位将变得不那么精确,但仍然可以揭示目标。

威廉姆斯发现,当目标在国外时,这个技巧也有效,因为他在丹麦哥本哈根找到了一个测试对象。

![跟踪丹麦的一个人]()

**跟踪丹麦的一个人**
*资料来源:mastdatabase.co.uk*

##

## O2 UK确认修复

威廉姆斯说,他于2025年3月26日和27日多次联系O2 UK,报告他的发现,没有得到任何答复。

最后,他今天早些时候从O2英国公司直接确认这个问题已经解决,他通过测试证实了这一点。

维珍媒体发言人在给BleepingComputer的一份声明中证实,已经实施了修复程序,并指出客户不必采取任何行动来保护自己。

“我们的工程团队已经工作并测试了数周的修复程序 – 我们可以确认这现在已经完全实施,测试表明修复已经有效,我们的客户不需要采取任何行动,”维珍媒体O2告诉BleepingComputer。

BleepingComputer询问O2是否已知该漏洞被利用,以及他们是否计划相应地通知客户,但我们没有收到答案。

本文翻译自bleepingcomputer [原文链接](https://www.bleepingcomputer.com/news/security/o2-uk-patches-bug-leaking-mobile-user-location-from-call-metadata/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/307667](/post/id/307667)

安全KER - 有思想的安全新媒体

本文转载自: [bleepingcomputer](https://www.bleepingcomputer.com/news/security/o2-uk-patches-bug-leaking-mobile-user-location-from-call-metadata/)

如若转载,请注明出处： <https://www.bleepingcomputer.com/news/security/o2-uk-patches-bug-leaking-mobile-user-location-from-call-metadata/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [漏洞分析](/tag/%E6%BC%8F%E6%B4%9E%E5%88%86%E6%9E%90)
* [安全知识](/tag/%E5%AE%89%E5%85%A8%E7%9F%A5%E8%AF%86)
* [漏洞情报](/tag/%E6%BC%8F%E6%B4%9E%E6%83%85%E6%8A%A5)

**+1**2赞

收藏

![](https://p2.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p0.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p2.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=170061)

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

* [通过呼叫定位用户](#h2-1)
* [O2 UK确认修复](#h2-3)

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