---
title: AntiDot Android木马：新的MaaS恶意软件记录屏幕，拦截短信，并窃取财务数据
url: https://www.anquanke.com/post/id/308722
source: 安全客-有思想的安全新媒体
date: 2025-06-21
fetch_date: 2025-10-06T22:53:01.647818
---

# AntiDot Android木马：新的MaaS恶意软件记录屏幕，拦截短信，并窃取财务数据

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

# AntiDot Android木马：新的MaaS恶意软件记录屏幕，拦截短信，并窃取财务数据

阅读量**75754**

发布时间 : 2025-06-20 18:09:21

**x**

##### 译文声明

本文是翻译文章，文章原作者 Ddos，文章来源：securityonline

原文地址：<https://securityonline.info/antidot-android-trojan-new-maas-malware-records-screens-intercepts-sms-steals-financial-data/>

译文仅供参考，具体内容表达以及含义原文为准。

![]()

瑞士网络安全公司 [PRODAFT](https://catalyst.prodaft.com/public/report/antidot/overview) 公布了有关涉及名为 AntiDot 的 Android 木马的广泛恶意活动的详细调查结果。据专家称，该恶意软件已经在 3,775 次单独的攻击中感染了超过 273 台设备，并积极部署在旨在窃取个人和财务信息的计划中。

开发和传播 AntiDot 的背后是名为 LARVA-398 的威胁组织，主要由经济动机驱动。该恶意软件通过地下在线论坛通过“恶意软件即服务”（MaaS） 模型进行分发，并用于针对特定国家/地区和语言社区的攻击。传播通过恶意广告网络和高度定制的网络钓鱼活动进行。

AntiDot 作为一种多功能监控工具销售。它可以记录设备的屏幕、拦截 SMS 消息并从第三方应用程序中提取数据。该特洛伊木马基于使用商业加壳程序进行混淆处理的 Java 程序，这使得检测和逆向工程变得复杂。恶意负载分三个阶段解压缩，从目标设备上安装的 APK 文件开始。

AntiDot 的一个显着特点是它滥用 Android MediaProjection API 和辅助功能服务，这使攻击者能够实时监控屏幕、执行键盘记录、远程控制设备和观察用户行为。在安装过程中，恶意软件会请求可访问性权限并部署包含僵尸网络核心逻辑的恶意 DEX 文件。

当受害者启动加密货币或与支付相关的应用程序时，AntiDot 会用从其命令和控制 （C2） 服务器获取的虚假登录页面替换合法屏幕。这种覆盖技术用于窃取登录凭据。此外，该木马将自己设置为默认 SMS 应用程序，拦截入站和出站消息、跟踪呼叫并根据预定义规则重定向或阻止它们。

此外，AntiDot 会监控系统通知，删除或隐藏可能引起怀疑的警报。所有受感染的设备都通过基于 MeteorJS 框架开发的 C2 面板进行管理。该面板具有用于分析已安装的应用程序、配置攻击参数、查看受感染的设备、管理网络连接的模块，甚至还包括一个内置的帮助部分。

该平台表现出高度的适应性，并且显然是通过对移动设备的持续控制来进行金融剥削而设计的，尤其是在具有本地化语言偏好的地区。值得注意的是，AntiDot 利用 WebView 注入并模仿合法银行和支付应用程序的界面，使其对用户的隐私特别危险。

本文翻译自securityonline [原文链接](https://securityonline.info/antidot-android-trojan-new-maas-malware-records-screens-intercepts-sms-steals-financial-data/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/308722](/post/id/308722)

安全KER - 有思想的安全新媒体

本文转载自: [securityonline](https://securityonline.info/antidot-android-trojan-new-maas-malware-records-screens-intercepts-sms-steals-financial-data/)

如若转载,请注明出处： <https://securityonline.info/antidot-android-trojan-new-maas-malware-records-screens-intercepts-sms-steals-financial-data/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [安全资讯](/tag/%E5%AE%89%E5%85%A8%E8%B5%84%E8%AE%AF)
* [网络攻击](/tag/%E7%BD%91%E7%BB%9C%E6%94%BB%E5%87%BB)

**+1**0赞

收藏

![](https://p2.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p2.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p2.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=171771)

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