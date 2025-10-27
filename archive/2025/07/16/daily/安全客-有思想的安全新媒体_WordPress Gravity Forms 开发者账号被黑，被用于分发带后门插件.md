---
title: WordPress Gravity Forms 开发者账号被黑，被用于分发带后门插件
url: https://www.anquanke.com/post/id/310087
source: 安全客-有思想的安全新媒体
date: 2025-07-16
fetch_date: 2025-10-06T23:39:02.314521
---

# WordPress Gravity Forms 开发者账号被黑，被用于分发带后门插件

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

# WordPress Gravity Forms 开发者账号被黑，被用于分发带后门插件

阅读量**59175**

发布时间 : 2025-07-15 18:22:41

**x**

##### 译文声明

本文是翻译文章，文章原作者 Bill Toulas，文章来源：bleepingcomputer

原文地址：<https://www.bleepingcomputer.com/news/security/wordpress-gravity-forms-developer-hacked-to-push-backdoored-plugins/>

译文仅供参考，具体内容表达以及含义原文为准。

![]()

知名 WordPress 插件 Gravity Forms 遭遇疑似供应链攻击，其官网提供的手动安装包被植入后门。

**Gravity Forms 是一款付费插件，用户可用于创建联系表单、支付表单等多种在线表单。根据官方统计数据，该插件目前部署于约 100 万个网站上，其中包括 Airbnb、Nike、ESPN、联合国儿童基金会（UNICEF）、Google 以及耶鲁大学等知名组织。**

### 插件被植入远程代码执行后门

WordPress 安全公司 PatchStack 表示，今天早些时候他们收到报告，称从 Gravity Forms 官网下载的插件在运行过程中产生了异常网络请求。

在分析过程中，研究人员确认他们从官方渠道下载到的插件文件中包含恶意内容，具体位于 `gravityforms/common.php` 文件内。进一步检查发现，该文件会向可疑域名 `gravityapi.org/sites` 发起 POST 请求。

此外，插件还会收集大量网站元数据，如网址、后台地址、主题、已安装插件列表、PHP 和 WordPress 版本等，并将这些信息传输至攻击者控制的服务器。随后服务器返回经过 base64 编码的 PHP 恶意代码，保存为 `wp-includes/bookmark-canonical.php` 文件。

这段恶意代码伪装成 WordPress 内容管理工具，实际上是一段无需身份验证即可触发的远程代码执行后门。其通过 `handle_posts()、handle_media()、handle_widgets()` 等函数在初始化期间被调用，并最终通过 `eval()` 执行用户输入的恶意代码。

PatchStack 警告：“这些函数可以由未认证用户通过 `__construct -> init_content_management -> handle_requests -> process_request` 这一执行链触发，进而实现远程代码执行。”

### RocketGenius 回应并发布善后公告

Gravity Forms 的开发商 RocketGenius 在获悉问题后确认，受影响的仅为 **7 月 10 日至 11 日** 期间，通过 **手动下载或 composer 安装方式** 获取的 Gravity Forms 版本 2.9.11.1 和 2.9.12。

RocketGenius 强调，Gravity Forms 插件内置的 Gravity API 服务（用于许可管理、自动更新和插件安装）未受到此次攻击影响。通过该服务下载安装的插件包均为安全版本。

不过，恶意代码在感染网站后会执行多项操作，包括：

* 阻止插件自动更新
* 连接攻击者服务器下载额外恶意负载
* 创建具有完全权限的管理员账号，以控制整站

**开发方建议所有在此期间下载或安装过相关版本插件的管理员立即重新安装干净版本，并使用特定方法检查网站是否存在感染迹象。据 PatchStack 分析，攻击所用的相关恶意域名注册于 7 月 8 日。**

### 安全建议

* 管理员应尽快替换受感染版本的插件
* 使用安全扫描工具检查网站文件完整性和异常管理员账号
* 避免通过不受信渠道手动下载插件包

此次事件凸显了 WordPress 插件供应链风险的现实威胁，也再次提醒开发者和站点运营者需高度警惕手动安装包的安全性。

本文翻译自bleepingcomputer [原文链接](https://www.bleepingcomputer.com/news/security/wordpress-gravity-forms-developer-hacked-to-push-backdoored-plugins/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/310087](/post/id/310087)

安全KER - 有思想的安全新媒体

本文转载自: [bleepingcomputer](https://www.bleepingcomputer.com/news/security/wordpress-gravity-forms-developer-hacked-to-push-backdoored-plugins/)

如若转载,请注明出处： <https://www.bleepingcomputer.com/news/security/wordpress-gravity-forms-developer-hacked-to-push-backdoored-plugins/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [安全资讯](/tag/%E5%AE%89%E5%85%A8%E8%B5%84%E8%AE%AF)
* [网络攻击](/tag/%E7%BD%91%E7%BB%9C%E6%94%BB%E5%87%BB)

**+1**8赞

收藏

![](https://p4.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p5.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p4.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=171771)

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