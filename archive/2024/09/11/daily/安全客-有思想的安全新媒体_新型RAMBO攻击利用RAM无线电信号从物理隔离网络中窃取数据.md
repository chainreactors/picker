---
title: 新型RAMBO攻击利用RAM无线电信号从物理隔离网络中窃取数据
url: https://www.anquanke.com/post/id/299952
source: 安全客-有思想的安全新媒体
date: 2024-09-11
fetch_date: 2025-10-06T18:21:04.627535
---

# 新型RAMBO攻击利用RAM无线电信号从物理隔离网络中窃取数据

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

# 新型RAMBO攻击利用RAM无线电信号从物理隔离网络中窃取数据

阅读量**87238**

发布时间 : 2024-09-10 14:18:55

**x**

##### 译文声明

本文是翻译文章，文章原作者 Ravie Lakshmanan，文章来源：The Hacker News

原文地址：<https://thehackernews.com/2024/09/new-rambo-attack-uses-ram-radio-signals.html>

译文仅供参考，具体内容表达以及含义原文为准。

已发现一种新型侧信道攻击，它利用设备的随机存取存储器 （RAM） 发出的无线电信号作为数据泄露机制，对气隙网络构成威胁。

以色列内盖夫本古里安大学软件和信息系统工程系进攻性网络研究实验室的负责人 Mordechai Guri 博士将这项技术的代号命名为 **RAMBO**。

“恶意软件使用软件生成的无线电信号，可以对敏感信息进行编码，例如文件、图像、键盘记录、生物识别和加密密钥，”Guri 博士在新发表的一篇研究论文中说。

“借助软件定义无线电 （SDR） 硬件和简单的现成天线，攻击者可以从远处拦截传输的原始无线电信号。然后可以解码信号并将其转换回二进制信息。

多年来，Guri 博士利用串行 ATA 电缆 （SATAn）、MEMS 陀螺仪 （GAIROSCOPE）、网络接口卡上的 LED （ETHERLED） 和动态功耗 （COVID-bit） ，设计了各种机制来从离线网络中提取机密数据。

研究人员设计的其他一些非常规方法需要通过图形处理单元 （GPU） 风扇 （GPU-FAN） 产生的隐蔽声学信号、内置主板蜂鸣器 （EL-GRILLO） 产生的（超声波），甚至打印机显示面板和状态 LED （PrinterLeak） 产生的隐蔽声音信号，从气隙网络中泄漏数据。

去年，Guri 还演示了 AirKeyLogger，这是一种无硬件射频键盘记录攻击，它将计算机电源的无线电发射武器化，以将实时击键数据泄露给远程攻击者。

“为了泄露机密数据，处理器的工作频率纵，以从电源单元产生一种由击键调制的电磁辐射模式，”Guri 在研究中指出。“可以通过 RF 接收器或带有简单天线的智能手机在几米远的距离内接收击键信息。”

与此类攻击一样，它要求首先通过其他方式（例如流氓内部人员、中毒的 USB 驱动器或供应链攻击）破坏气隙网络，从而允许恶意软件触发隐蔽的数据泄露渠道。

RAMBO 也不例外，因为该恶意软件用于操纵 RAM，使其可以生成时钟频率的无线电信号，然后使用曼彻斯特编码进行编码并传输，以便从远处接收。

编码数据可以包括击键、文档和生物识别信息。然后，另一端的攻击者可以利用 SDR 接收电磁信号，解调和解码数据，并检索泄露的信息。

“该恶意软件利用来自 RAM 的电磁辐射来调制信息并将其向外传输，”Guri 博士说。“拥有无线电接收器和天线的远程攻击者可以接收信息，解调信息，并将其解码为原始二进制或文本表示形式。”

研究发现，该技术可用于以每秒 1,000 位的速度从运行 Intel i7 3.6GHz CPU 和 16 GB RAM 的气隙计算机中泄露数据，每个键 16 位的击键被实时泄露。

“4096 位 RSA 加密密钥可以在 41.96 秒的低速和 4.096 位的高速下泄露，”Guri 博士说。“生物识别信息、小文件 （.jpg） 和小文档（.txt 和 .docx）在低速时需要 400 秒，在快速时需要几秒钟。”

“这表明 RAMBO 隐蔽通道可用于在短时间内泄露相对简短的信息。”

阻止攻击的对策包括对信息传输实施“红黑”区域限制、使用入侵检测系统 （IDS）、监控虚拟机管理程序级内存访问、使用无线电干扰器阻止无线通信以及使用法拉第笼。

本文翻译自The Hacker News [原文链接](https://thehackernews.com/2024/09/new-rambo-attack-uses-ram-radio-signals.html)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/299952](/post/id/299952)

安全KER - 有思想的安全新媒体

本文转载自: [The Hacker News](https://thehackernews.com/2024/09/new-rambo-attack-uses-ram-radio-signals.html)

如若转载,请注明出处： <https://thehackernews.com/2024/09/new-rambo-attack-uses-ram-radio-signals.html>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [网络攻击](/tag/%E7%BD%91%E7%BB%9C%E6%94%BB%E5%87%BB)
* [网络安全热点](/tag/%E7%BD%91%E7%BB%9C%E5%AE%89%E5%85%A8%E7%83%AD%E7%82%B9)

**+1**0赞

收藏

![](https://p3.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p2.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p3.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=170338)

[安全客](/member.html?memberId=170338)

这个人太懒了，签名都懒得写一个

* 文章
* **823**

* 粉丝
* **1**

### TA的文章

* ##### [严重的GiveWP漏洞（CVE-2024-8353）影响10万WordPress网站](/post/id/300547)

  2024-09-30 15:03:21
* ##### [Patchwork APT 的 Nexe 后门活动曝光](/post/id/300549)

  2024-09-30 15:03:07
* ##### [用户在一次复杂的钓鱼攻击中损失了价值3200万美元的spWETH](/post/id/300551)

  2024-09-30 15:02:50
* ##### [车牌信息成安全漏洞：起亚汽车远程控制风险揭示联网车辆网络安全问题](/post/id/300553)

  2024-09-30 15:02:09
* ##### [严重SQL注入漏洞影响TI WooCommerce Wishlist插件，超10万WordPress网站面临风险](/post/id/300556)

  2024-09-30 15:01:53

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