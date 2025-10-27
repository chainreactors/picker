---
title: GhostStripe：黑客迫使特斯拉自动驾驶仪违反交通规则
url: https://www.anquanke.com/post/id/296655
source: 安全客-有思想的安全新媒体
date: 2024-05-22
fetch_date: 2025-10-06T16:48:55.134477
---

# GhostStripe：黑客迫使特斯拉自动驾驶仪违反交通规则

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

# GhostStripe：黑客迫使特斯拉自动驾驶仪违反交通规则

阅读量**88287**

发布时间 : 2024-05-21 11:37:38

**x**

##### 译文声明

本文是翻译文章

原文地址：<https://www.securitylab.ru/news/548398.php>

译文仅供参考，具体内容表达以及含义原文为准。

来自新加坡的一个科学家团队 开发了 一种干扰自动驾驶汽车的方法，这些自动驾驶汽车使用计算机视觉来识别路标。新的 GhostStripe 技术可能对特斯拉和百度 Apollo 司机造成危险。

GhostStripe 背后的主要想法是使用 LED 在路标上创建灯光图案。这些图案是人眼看不见的，但它们会迷惑汽车摄像头。该攻击包括在相机触发时 LED 快速闪烁不同颜色，导致图像出现扭曲。

由于 CMOS 相机数字快门的特性，会出现失真。配备此快门的相机分阶段扫描图像，闪烁的 LED 在每个扫描阶段产生不同的阴影。结果是图像与现实不符。例如，停车标志的红色在每条扫描线上可能看起来不同。

![]()

当这样的扭曲图像进入基于深度神经网络的汽车分类器时，系统无法识别该标志并且无法对其做出正确响应。类似的攻击方法已经存在，但研究团队能够获得稳定且可重复的结果，使这种攻击在现实环境中变得实用。

研究人员开发了两种版本的攻击：

* GhostStripe1不需要访问车辆，并使用跟踪系统实时监控车辆的位置。这使您可以动态调整 LED 的闪烁，以便不识别该标志。
* GhostStripe2需要对车辆进行物理访问。在这种情况下，相机的电源线上安装了转换器，记录图像扫描的瞬间并精确控制启动时间。这使您可以攻击特定车辆并控制标志识别的结果。

该团队使用百度 Apollo 设备中使用的 Leopard Imaging AR023ZWDR 相机在真实道路上测试了该系统。测试是在停车标志、让行标志和限速标志处进行的。 GhostStripe1 的成功率为 94%，GhostStripe2 的成功率为 97%。

影响攻击有效性的因素之一是强烈的环境照明，这会降低攻击的有效性。研究人员指出，为了成功进行攻击，攻击者必须仔细选择时间和地点。

有一些对策可以减少脆弱性。例如，您可以将 CMOS 相机替换为带有传感器的数字快门，该传感器可以一次拍摄整个图像，或者随机扫描各层。额外的摄像头也可能会降低成功攻击的可能性或需要更复杂的方法。另一种措施可能是训练神经网络来识别此类攻击。

本文翻译自 [原文链接](https://www.securitylab.ru/news/548398.php)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/296655](/post/id/296655)

安全KER - 有思想的安全新媒体

本文转载自:

如若转载,请注明出处： <https://www.securitylab.ru/news/548398.php>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [人工智能](/tag/%E4%BA%BA%E5%B7%A5%E6%99%BA%E8%83%BD)

**+1**2赞

收藏

![](https://p4.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p5.ssl.qhimg.com/t014757b72460d855bf.png)

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

* ##### [人工智能可能修复帮助传播了 15 年的漏洞](/post/id/308401)

  2025-06-12 15:19:33
* ##### [浅析新型网络犯罪DeepSeek AI实战应用](/post/id/305102)

  2025-03-18 10:38:20
* ##### [360SRC x Hacking Group丨「奇御」AI安全技术沙龙议题征集！](/post/id/302279)

  2024-11-28 17:43:31
* ##### [从误用到滥用： 人工智能风险与攻击](/post/id/300992)

  2024-10-17 11:00:07
* ##### [一种用于网络钓鱼攻击的生成式人工智能恶意软件](/post/id/300410)

  2024-09-25 14:16:34
* ##### [苹果加入美国政府对人工智能安全的自愿承诺](/post/id/298565)

  2024-07-31 11:23:56
* ##### [Vanta筹集1.5亿美元，加速其AI产品创新](/post/id/298358)

  2024-07-25 15:02:41

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