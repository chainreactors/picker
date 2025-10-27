---
title: RVTools供应链攻击：Bumblebee恶意软件通过可信的VMware实用程序交付
url: https://www.anquanke.com/post/id/307527
source: 安全客-有思想的安全新媒体
date: 2025-05-20
fetch_date: 2025-10-06T22:23:49.217934
---

# RVTools供应链攻击：Bumblebee恶意软件通过可信的VMware实用程序交付

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

# RVTools供应链攻击：Bumblebee恶意软件通过可信的VMware实用程序交付

阅读量**59176**

发布时间 : 2025-05-19 16:21:01

**x**

##### 译文声明

本文是翻译文章，文章原作者 Ddos，文章来源：securityonline

原文地址：<https://securityonline.info/rvtools-supply-chain-attack-bumblebee-malware-delivered-via-trusted-vmware-utility/>

译文仅供参考，具体内容表达以及含义原文为准。

![RVTools 大黄蜂恶意软件]()

ZeroDay Labs的网络安全从业者和威胁分析师Aidan Leon披露了涉及值得信赖的VMware实用程序RVTools的复杂供应链攻击。该漏洞短暂地将流行的IT管理工具转变为恶意软件分发向量,提供Bumblebee加载器的自定义变体 – 一种经常用于勒索软件操作和初始访问活动的臭名昭着的有效载荷。

当Microsoft Defender for Endpoint在一名员工试图安装RVTools后不久标记可疑行为时发现了这一事件。[describes](https://zerodaylabs.net/rvtools-bumblebee-malware/)*正如Leon所描述的那样:“在启动安装程序的瞬间,Defender标记了一个可疑文件:version.dll,它试图从与安装程序本身相同的目录中执行。*

这种活动立即被认为是RVTools的非典型活动,促使进行更深入的调查。

可疑文件的哈希被提交给VirusTotal,[antivirus](https://securityonline.info/mcafee-premium-review-all-around-protection-for-your-digital-life-but-is-it-the-best/)其中71个防病毒引擎中有33个检测到它是恶意的。该恶意软件被归类为大黄蜂装载机变体,[exploitation](https://securityonline.info/hostedscan-review-proactive-vulnerability-management-for-a-bulletproof-digital-presence/)以其在提供Cobalt [ransomware](https://securityonline.info/bitdefender-premium-security-review-the-ultimate-all-in-one-security-privacy-fortress/)Strike等后利用框架和促进勒索软件部署方面的作用而闻名。

*“恶意软件似乎是大黄蜂加载器的自定义变体,该加载器以威胁行为者在初始访问场景中使用而闻名。*

进一步的元数据增加了一层超现实的混淆,条目如下:

* + 英文名称:Hydrarthrus
  + 公司名称: Enlargers pharmakos submatrix
  + 产品: 无二矿瑜伽士

* + 描述: 象形无法分组的clyfaker duturalness

莱昂指出*,“这些超现实的术语是故意混淆和试图分散注意力……可能暗示’犯罪之神’ –* 尽管这仍然是推测性的。

调查证实,RVTools的受损版本包含一个版本。dll在早期的干净版本中不存在。值得注意的是,RVTools网站在发现后不久就下线了,并在返回后开始提供一个较小,干净的文件,其哈希值与官方版本相匹配 – 暂时妥协的有力证据。

![]()

*“这似乎是暂时的、有针对性的供应链妥协。*

ZeroDay Labs迅速采取行动遏制和中和威胁:

* 对受感染端点进行全防御扫描
* 恶意版本的检疫。
* dll验证现有的RVTools设施
* 向内部检测小组提交国际奥委会
* 供应商通知

本文翻译自securityonline [原文链接](https://securityonline.info/rvtools-supply-chain-attack-bumblebee-malware-delivered-via-trusted-vmware-utility/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/307527](/post/id/307527)

安全KER - 有思想的安全新媒体

本文转载自: [securityonline](https://securityonline.info/rvtools-supply-chain-attack-bumblebee-malware-delivered-via-trusted-vmware-utility/)

如若转载,请注明出处： <https://securityonline.info/rvtools-supply-chain-attack-bumblebee-malware-delivered-via-trusted-vmware-utility/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [漏洞](/tag/%E6%BC%8F%E6%B4%9E)
* [安全知识](/tag/%E5%AE%89%E5%85%A8%E7%9F%A5%E8%AF%86)

**+1**3赞

收藏

![](https://p5.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p5.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p5.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=170061)

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
* ##### [起亚厄瓜多尔无钥匙进入系统漏洞导致数千辆车辆被盗](/post/id/308480)

  2025-06-16 15:48:35
* ##### [微软 Office 漏洞允许攻击者执行远程代码](/post/id/308412)

  2025-06-12 15:43:53
* ##### [人工智能可能修复帮助传播了 15 年的漏洞](/post/id/308401)

  2025-06-12 15:19:33
* ##### [美国CISA警告 SinoTrack GPS 跟踪器存在远程控制漏洞](/post/id/308398)

  2025-06-12 15:15:38
* ##### [黑客通过恶意简历瞄准求职者](/post/id/308388)

  2025-06-12 14:31:49
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