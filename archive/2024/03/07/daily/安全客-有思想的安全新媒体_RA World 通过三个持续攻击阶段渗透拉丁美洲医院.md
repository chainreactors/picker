---
title: RA World 通过三个持续攻击阶段渗透拉丁美洲医院
url: https://www.anquanke.com/post/id/293631
source: 安全客-有思想的安全新媒体
date: 2024-03-07
fetch_date: 2025-10-06T17:08:38.934339
---

# RA World 通过三个持续攻击阶段渗透拉丁美洲医院

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

# RA World 通过三个持续攻击阶段渗透拉丁美洲医院

阅读量**75102**

发布时间 : 2024-03-06 10:16:01

**x**

##### 译文声明

本文是翻译文章

译文仅供参考，具体内容表达以及含义原文为准。

三个持续的攻击阶段已成为阴险勒索软件的标志。

趋势科技 最近发现了 来自 RA World 勒索软件组织（也称为 RA Group）的新一波活动。该组织早在 2023 年 4 月就开始进行恶意活动，并在其存在期间成功攻击了位于美国、德国、印度和台湾的许多组织，主要是医疗保健和金融领域的组织。

研究人员透露，最新一波 RA World 攻击针对的是拉丁美洲的多家医疗机构。这些攻击分几个阶段进行，以增加成功行动的总体机会。

* 初始访问。攻击首先是黑客通过域控制器渗透计算机系统。编辑组策略 (GPO) 在这里发挥着关键作用，它允许攻击者在受害者的系统上设置自己的规则。
* 第 1 阶段（Stage1.exe）。一旦渗透到系统中，病毒就会使用“Stage1.exe”文件来评估网络并为进一步攻击做好准备，其中包括检查域控制器并准备复制病毒的下一阶段。
* 第 2 阶段（Stage2.exe）。在此阶段，病毒将自身复制到网络上的其他计算机并开始准备加密文件。“Stage2.exe”负责在目标网络内传播恶意代码，为发起主要攻击奠定基础。
* 第 3 阶段（Stage3.exe）。这是病毒激活的最后阶段，对受感染计算机上的文件进行加密并要求赎金来恢复它们。它使用复杂的加密技术，使用户和系统无法访问文件。

![]()
RA World多阶段攻击方案

此外，该恶意软件可以以特殊的安全模式重新启动系统，从而避免被防病毒软件检测到。它还会在执行攻击后消除其存在的痕迹，使研究人员更难分析。

为了最大限度地降低成为 RA World 攻击受害者之一的风险，建议采用最佳安全实践：限制管理权限、及时更新所使用的软件、定期数据备份、与电子邮件和网站交互时小心谨慎，以及对公司员工进行网络安全基础知识培训。

使用集成的安全方法可以显着增强系统的潜在访问点，从而从质量上提高对企业的保护。

本文翻译自 原文链接。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/293631](/post/id/293631)

安全KER - 有思想的安全新媒体

本文转载自:

如若转载,请注明出处：

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [勒索攻击](/tag/%E5%8B%92%E7%B4%A2%E6%94%BB%E5%87%BB)

**+1**5赞

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

* ##### [Gunra Ransomware集团声称从美国医院泄露了40 TB数据](/post/id/308534)

  2025-06-17 16:00:49
* ##### [勒索软件组织攻击药物滥用治疗服务机构](/post/id/303119)

  2024-12-30 11:11:06
* ##### [勒索软件攻击暴露了 560 万 Ascension 患者的数据](/post/id/302957)

  2024-12-24 10:53:52
* ##### [被武器化的 Windows 工具 Wevtutil.exe 在新型攻击中被利用](/post/id/302321)

  2024-12-02 11:19:00
* ##### [CyberVolk：模糊在行动主义、勒索软件和地缘政治之间的黑客主义集体](/post/id/302214)

  2024-11-27 10:44:25
* ##### [德国大型药品批发商遭勒索攻击，欲扰乱超6000家药房供应](/post/id/301584)

  2024-11-06 10:55:18
* ##### [8Base 勒索软件团伙声称窃取大众汽车大量文件并威胁公布](/post/id/301054)

  2024-10-18 11:21:49

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