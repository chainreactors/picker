---
title: 木马化的KeePass用于部署Cobalt Strike并窃取凭据
url: https://www.anquanke.com/post/id/307531
source: 安全客-有思想的安全新媒体
date: 2025-05-20
fetch_date: 2025-10-06T22:23:48.056619
---

# 木马化的KeePass用于部署Cobalt Strike并窃取凭据

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

# 木马化的KeePass用于部署Cobalt Strike并窃取凭据

阅读量**63863**

发布时间 : 2025-05-19 16:24:01

**x**

##### 译文声明

本文是翻译文章，文章原作者 Ddos，文章来源：securityonline

原文地址：<https://securityonline.info/trojanized-keepass-used-to-deploy-cobalt-strike-and-steal-credentials/>

译文仅供参考，具体内容表达以及含义原文为准。

![KeePass木马 恶意攻击]()

最近,WithSecure的Threat Intelligence团队发现了一个复杂的恶意软件活动,其中开源密码管理器KeePass被木相传以提供Cobalt Strike有效载荷并窃取敏感凭据。

*“这不仅是一个无证的恶意软件加载器,这也是我们在开源报告中观察到的第一个例子,即一个木占领密码管理器……*[同时被用作装载机和凭证窃取工具。](https://labs.withsecure.com/publications/keepass-trojanised-in-advanced-malware-campaign)

被破坏的KeePass安装程序 – 被识别为KeePass-2.56-Setup.exe – 是通过恶意广告系列提供的,这些活动诱使用户从虚假的类似域下载。可执行文件与有效证书签名,并模仿了真正的KeePass安装程序的行为,使检测变得极其困难。

执行后,恶意软件(由WithSecure称为KeeLoader)将两个修改的可执行文件(KeePass.exe和ShInstUtil.exe)放入用户目录,并设置基于注册表的持久性机制。恶意文件(db.idx),加密并伪装成JPG,使用自定义加载器在内存中解密,并作为Cobalt Strike信标执行。

![KeePassMalware 运动]()

KeeLoader 执行流程

虽然KeePass似乎正常运行,*但它从数据库中秘密记录凭据并将其导出到。kp文件:“帐户,登录名,密码,[information](https://securityonline.info/bitdefender-premium-security-review-the-ultimate-all-in-one-security-privacy-fortress/)网站和评论信息也以CSV格式导出为%localappdata%作为<RANDOM\_INTEGER>.kp。*

攻击基础设施广泛:

* Fake KeePass域名,如keepaswrd[.]com,keegass[.]com和KeePass[.]me
* 通过Bing和DuckDuckGo搜索广告进行恶意
* 通过多个假域重定向链
* 来自NameCheap等提供商的SSL证书,模仿合法的KeePass签名

该活动在多个版本上发展,*隐身和复杂性不断增加:“创建的二进制文件几乎与合法版本相同……恶意功能只有在密码数据库打开后才会显现。*

虽然由于使用Loader-as-a-Service和Bulletproof Hosting,归因仍然具有挑战性,[但WithSecure发现与Black](https://securityonline.info/bitdefender-premium-security-review-the-ultimate-all-in-one-security-privacy-fortress/) Basta和BlackCat等勒索软件组相关的重叠Cobalt Strike水印。赎金票据类似于Akira勒索软件,但包括通过洋葱邮件联系,*暗示可能试图由前附属公司“独奏”:“这是不寻常的……一种现实的可能性,[威胁行为者以前在勒索软件](https://securityonline.info/bitdefender-premium-security-review-the-ultimate-all-in-one-security-privacy-fortress/) – 即服务特许经营中工作,但在这种情况下,试图’独奏’。*‘

WithSecure总结说,该活动可能是由在勒索软件生态系统中运营的资源丰富的初始访问代理精心策划的。

*如果勒索软件可以比作杂草……支撑许多勒索软件事件的“即服务”生态系统可以等同于根源,确保持续的持久性和传播。*

敦促组织在安装前验证哈希,避免非官方下载源,并密切监控软件行为,即使对于已知应用程序也是如此。

本文翻译自securityonline [原文链接](https://securityonline.info/trojanized-keepass-used-to-deploy-cobalt-strike-and-steal-credentials/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/307531](/post/id/307531)

安全KER - 有思想的安全新媒体

本文转载自: [securityonline](https://securityonline.info/trojanized-keepass-used-to-deploy-cobalt-strike-and-steal-credentials/)

如若转载,请注明出处： <https://securityonline.info/trojanized-keepass-used-to-deploy-cobalt-strike-and-steal-credentials/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [安全资讯](/tag/%E5%AE%89%E5%85%A8%E8%B5%84%E8%AE%AF)
* [漏洞](/tag/%E6%BC%8F%E6%B4%9E)
* [安全知识](/tag/%E5%AE%89%E5%85%A8%E7%9F%A5%E8%AF%86)

**+1**3赞

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