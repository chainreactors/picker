---
title: APT41 恶意软件滥用谷歌日历进行隐蔽的 C2 通信
url: https://www.anquanke.com/post/id/307963
source: 安全客-有思想的安全新媒体
date: 2025-05-30
fetch_date: 2025-10-06T22:23:29.581325
---

# APT41 恶意软件滥用谷歌日历进行隐蔽的 C2 通信

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

# APT41 恶意软件滥用谷歌日历进行隐蔽的 C2 通信

阅读量**166393**

发布时间 : 2025-05-29 14:55:27

**x**

##### 译文声明

本文是翻译文章，文章原作者 Bill Toulas，文章来源：bleepingcomputer

原文地址：<https://www.bleepingcomputer.com/news/security/apt41-malware-abuses-google-calendar-for-stealthy-c2-communication/>

译文仅供参考，具体内容表达以及含义原文为准。

![Google 徽标]()

中国APT41黑客组织使用一种名为“ToughProgress”的新恶意软件,利用Google日历进行命令和控制(C2)操作,将恶意活动隐藏在受信任的云服务后面。

该活动由谷歌的威胁情报小组发现,该组织识别并拆除了攻击者控制的Google日历和工作区基础设施,并引入了有针对性的措施,以防止将来出现此类滥用。

使用Google日历作为C2机制并不是一种新技术[,](https://www.bleepingcomputer.com/news/security/malicious-npm-package-uses-unicode-steganography-to-evade-detection/)Veracode最近报道了Node Package Manager(NPM)索引中的恶意包,遵循类似的策略。

此外,APT41之前以滥用Google服务而闻名,例如在2023年4月的伏地魔恶意软件活动中使用Google Sheets和Google Voldemort malware campaignDrive。

![攻击概述]()

### APT41攻击流

攻击始于向目标发送恶意电子邮件,链接到以前被入侵的政府网站上托管的ZIP存档。

存档包含一个Windows LNK文件,假装为PDF文档,一个伪装成JPG映像文件的主要有效载荷,以及用于解密和启动有效载荷的DLL文件,也伪装成图像文件。

文件“6.jpg”和“7.jpg”是假图像。第一个文件实际上是一个加密的有效载荷,由第二个文件解密,这是当目标点击LNK时启动的DLL文件,“Google解释道。

DLL是“PlusDrop”,一个完全在内存中解密并执行下一阶段“PlusInject”的组件。

接下来,PlusInject在合法的Windows进程“svhost.exe”上执行过程空心,并注入最后阶段“ToughProgress”。

恶意软件连接到硬编码的 Google 日历端点,并在隐藏事件的描述字段中为 APT41 的命令收集特定事件日期。

![APT41的日历事件之一]()

执行它们后,ToughProgress 将结果返回到新的日历事件,以便攻击者可以相应地调整其下一步。

![加密交换]()

**加密交换**
*来源:Google*

由于有效载荷从未触及磁盘,并且C2通信通过合法的云服务进行,因此在受感染的主机上被安全产品标记的可能性很小。

### 扰乱活动

Google 识别了攻击者控制的 Google 日历实例,并终止了所有相关 Workspace 帐户和违规的日历事件。

谷歌的安全浏览块列表也相应地进行了更新,因此用户在访问相关网站时会收到警告,来自这些网站的流量将被阻止在所有科技巨头的产品中。

该报告没有列出任何具体的受损组织或受害者,但谷歌表示,它直接与Mandiant合作通知了他们。谷歌还与受害者分享了ToughProgress样本和交通日志,以帮助他们确定环境中的感染情况。

本文翻译自bleepingcomputer [原文链接](https://www.bleepingcomputer.com/news/security/apt41-malware-abuses-google-calendar-for-stealthy-c2-communication/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/307963](/post/id/307963)

安全KER - 有思想的安全新媒体

本文转载自: [bleepingcomputer](https://www.bleepingcomputer.com/news/security/apt41-malware-abuses-google-calendar-for-stealthy-c2-communication/)

如若转载,请注明出处： <https://www.bleepingcomputer.com/news/security/apt41-malware-abuses-google-calendar-for-stealthy-c2-communication/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [网络安全](/tag/%E7%BD%91%E7%BB%9C%E5%AE%89%E5%85%A8)
* [安全热点](/tag/%E5%AE%89%E5%85%A8%E7%83%AD%E7%82%B9)

**+1**4赞

收藏

![](https://p3.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p5.ssl.qhimg.com/t014757b72460d855bf.png)

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

* ##### [ISC.AI 2025创新独角兽沙盒大赛开启，政产学研共举创新势力](/post/id/308810)

  2025-06-23 17:47:17
* ##### [与“AI”同行，和ISC.AI共启新篇](/post/id/308800)

  2025-06-23 17:37:20
* ##### [手慢无！ISC.AI 2025 早鸟票100张限时6折，赠泡泡玛特乐园门票](/post/id/308736)

  2025-06-20 18:22:35
* ##### [航空公司向国土安全局出售乘客数据](/post/id/308408)

  2025-06-12 15:39:51
* ##### [美国政府疫苗网站被人工智能生成的内容污损](/post/id/308404)

  2025-06-12 15:36:04
* ##### [美国CISA警告 SinoTrack GPS 跟踪器存在远程控制漏洞](/post/id/308398)

  2025-06-12 15:15:38
* ##### [安全行动： 国际刑警组织在打击网络犯罪的重大行动中摧毁了 20,000 多个恶意 IP](/post/id/308395)

  2025-06-12 14:43:06

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