---
title: Tesla Model 3新漏洞：一部智能手机即可把车开走
url: https://www.anquanke.com/post/id/293736
source: 安全客-有思想的安全新媒体
date: 2024-03-12
fetch_date: 2025-10-04T12:09:20.354380
---

# Tesla Model 3新漏洞：一部智能手机即可把车开走

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

# Tesla Model 3新漏洞：一部智能手机即可把车开走

阅读量**83240**

发布时间 : 2024-03-11 10:31:43

**x**

##### 译文声明

本文是翻译文章

译文仅供参考，具体内容表达以及含义原文为准。

该漏洞影响全球超过 100 万辆特斯拉 Model 3 车辆。”

安全研究人员 Talal Haj Bakri 和 Tommy Misk 演示了 如何进行网络钓鱼攻击，以危害Tesla车主的帐户、解锁汽车并启动发动机。值得注意的是，此次攻击与特斯拉应用程序最新版本4.30.6和汽车固件版本11.1 2024.2.7有关。

该研究的作者向特斯拉通报了发现的漏洞，并指出将汽车与新手机连接的程序安全性不足。然而，制造商认为这个错误微不足道。

为了演示攻击，使用了Flipper Zero小工具，但也可以使用其他设备（计算机、Raspberry Pi或 Android 智能手机）进行攻击。

攻击首先在特斯拉充电站部署一个名为“Tesla Guest”的虚假 WiFi 网络。这个SSID通常可以在特斯拉服务中心找到，并且为车主所熟知。连接到虚假网络后，受害者会看到一个钓鱼特斯拉帐户登录页面，他在其中输入他的凭据，该凭据会立即到达攻击者。

![]()

网络钓鱼过程

获得凭据后，攻击者会请求一次性密码以绕过双因素身份验证 (2FA) 并获得对 Tesla 应用程序的访问权限，从而可以实时跟踪车辆的位置。

一旦攻击者获得特斯拉帐户的访问权限，他们就可以添加新的电话密钥。为此，您需要靠近汽车。电话钥匙通过 Tesla 移动应用程序和车主的智能手机工作，提供通过安全蓝牙连接自动锁定和解锁车辆的功能。

值得注意的是，添加新的电话钥匙后，特斯拉车主不会在应用程序中收到相关通知，汽车的触摸屏上也不会显示任何警告。使用新的电话钥匙，攻击者可以解锁车辆并激活其所有系统，让他们像车主一样开车离开。

该攻击在特斯拉 Model 3 上成功进行。研究人员提出，在添加新的电话钥匙时需要物理特斯拉钥匙卡（RFID 卡）来增加额外的身份验证层，以提高安全性。

特斯拉汽车还使用钥匙卡，这是一种薄的 RFID 卡，必须放置在中控台上的 RFID 读取器中才能启动汽车。尽管它们更安全，但如果电话钥匙不可用或电池电量不足，特斯拉将它们视为备用选项。

针对该漏洞，特斯拉表示，相关系统行为是设计使然，特斯拉 Model 3 用户手册并未表明需要 RFID 卡才能添加 Phone Key。特斯拉没有回应置评请求，也没有计划发布软件更新来防止此类攻击。

本文翻译自 原文链接。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/293736](/post/id/293736)

安全KER - 有思想的安全新媒体

本文转载自:

如若转载,请注明出处：

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [漏洞情报](/tag/%E6%BC%8F%E6%B4%9E%E6%83%85%E6%8A%A5)

**+1**4赞

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