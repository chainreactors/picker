---
title: TamperedChef恶意软件兴起：欺诈应用利用经过签名的二进制文件与搜索引擎投毒劫持浏览器
url: https://www.anquanke.com/post/id/312432
source: 安全客-有思想的安全新媒体
date: 2025-09-30
fetch_date: 2025-10-02T12:03:39.425056
---

# TamperedChef恶意软件兴起：欺诈应用利用经过签名的二进制文件与搜索引擎投毒劫持浏览器

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

# TamperedChef恶意软件兴起：欺诈应用利用经过签名的二进制文件与搜索引擎投毒劫持浏览器

阅读量**42841**

发布时间 : 2025-09-29 18:02:25

**x**

##### 译文声明

本文是翻译文章，文章原作者 Ddos，文章来源：securityonline

原文地址：<https://securityonline.info/tamperedchef-malware-rises-deceptive-apps-use-signed-binaries-and-seo-poisoning-to-hijack-browsers/>

译文仅供参考，具体内容表达以及含义原文为准。

![]()

Effect威胁情报团队发现新一轮TamperedChef恶意软件活动，该活动利用**数字签名二进制文件、欺骗性打包和浏览器劫持程序**，将恶意软件伪装成日常生产力工具进行分发。此次活动围绕两个被植入木马的应用程序展开：**ImageLooker.exe 和Calendaromatic.exe** ，两者均通过自解压归档文件传播。

调查始于2025年9月底，当时微软Defender标记了一个**潜在有害应用程序（PUA）**。Field Effect表示：“PUA（可能不具有明显恶意但表现出侵入性行为的软件）可作为更严重威胁的有效投递机制。”

ImageLooker和Calendaromatic均以**自解压7-Zip归档文件**形式分发，以绕过基础安全控制。Field Effect指出：“这些可执行文件使用NeutralinoJS构建——这是一个轻量级桌面框架，允许执行任意JavaScript代码。它通过欺骗性广告和搜索引擎操纵进行传播。”

研究人员将这些二进制文件与TamperedChef活动关联，该活动此前以植入木马的生产力应用而闻名。报告解释：“Calendaromatic已通过恶意软件样本库与TamperedChef活动关联……TamperedChef使用多个数字签名者和PUA来重定向流量、修改浏览器设置，并为恶意软件下载提供便利。”

参与分发的恶意软件发布者包括**CROWN SKY LLC、APPSOLUTE有限责任公司、OneStart Technologies LLC、Sunstream Labs**等实体——这些实体此前已被指参与分发植入木马的生产力工具、浏览器劫持程序和滥用住宅代理。

该活动大量使用混淆和隐蔽编码技术。Field Effect报告称：“恶意软件利用**Unicode同形异义字**在看似良性的API响应中编码载荷，从而绕过基于字符串的检测和特征匹配。”

1. **利用CVE-2025-0411漏洞**绕过Windows Mark of the Web保护机制；
2. 使用\*\*–install、–enableupdate、–fullupdate等命令行标志\*\*实现持久化；
3. 与calendaromatic[.]com和movementxview[.]com建立C2通信；
4. 窃取浏览器数据、存储的凭证和会话信息。

受害者通过**SEO投毒和欺骗性广告**被引诱。Field Effect解释：“威胁行为者通过创建关键词堆砌的着陆页，在‘免费PDF编辑器’‘Windows日历应用’或‘图片查看器下载’等查询中排名靠前，从而操纵搜索引擎结果。”

这些虚假网站模仿合法软件门户，展示信任徽章、伪造评论和下载计数器，诱使用户下载恶意安装程序。

TamperedChef活动例证了PUA如何被武器化，成为恶意软件分发生态系统的一部分，模糊了“滋扰软件”与全面网络犯罪之间的界限。攻击者通过结合**数字签名二进制文件、混淆技术、同形异义字编码和欺骗性分发**，成功绕过基于信誉的防御并利用用户信任。

Field Effect警告：“TamperedChef活动表明，威胁行为者正在通过武器化潜在有害应用程序、滥用数字代码签名和部署隐蔽编码技术，不断进化其投递机制。”

本文翻译自securityonline [原文链接](https://securityonline.info/tamperedchef-malware-rises-deceptive-apps-use-signed-binaries-and-seo-poisoning-to-hijack-browsers/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/312432](/post/id/312432)

安全KER - 有思想的安全新媒体

本文转载自: [securityonline](https://securityonline.info/tamperedchef-malware-rises-deceptive-apps-use-signed-binaries-and-seo-poisoning-to-hijack-browsers/)

如若转载,请注明出处： <https://securityonline.info/tamperedchef-malware-rises-deceptive-apps-use-signed-binaries-and-seo-poisoning-to-hijack-browsers/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [安全资讯](/tag/%E5%AE%89%E5%85%A8%E8%B5%84%E8%AE%AF)
* [网络攻击](/tag/%E7%BD%91%E7%BB%9C%E6%94%BB%E5%87%BB)

**+1**0赞

收藏

![](https://p0.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p5.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p0.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=171771)

[安全客](/member.html?memberId=171771)

这个人太懒了，签名都懒得写一个

* 文章
* **545**

* 粉丝
* **5**

### TA的文章

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