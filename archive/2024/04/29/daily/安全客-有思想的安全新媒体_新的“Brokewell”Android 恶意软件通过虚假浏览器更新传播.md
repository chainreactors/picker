---
title: 新的“Brokewell”Android 恶意软件通过虚假浏览器更新传播
url: https://www.anquanke.com/post/id/296083
source: 安全客-有思想的安全新媒体
date: 2024-04-29
fetch_date: 2025-10-04T12:14:34.709025
---

# 新的“Brokewell”Android 恶意软件通过虚假浏览器更新传播

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

# 新的“Brokewell”Android 恶意软件通过虚假浏览器更新传播

阅读量**68319**

发布时间 : 2024-04-28 11:19:48

**x**

##### 译文声明

本文是翻译文章

原文地址：<https://thehackernews.com/2024/04/new-brokewell-android-malware-spread.html>

译文仅供参考，具体内容表达以及含义原文为准。

虚假浏览器更新被用来推送一种名为Brokewell的先前未记录的 Android 恶意软件。

荷兰安全公司 ThreatFabric在周四发布的一份分析报告中表示： “Brokewell 是一种典型的现代银行恶意软件，恶意软件内置了数据窃取和远程控制功能。”

据说该恶意软件正在积极开发中，添加新命令来捕获触摸事件、屏幕上显示的文本信息以及受害者启动的应用程序。

伪装成 Google Chrome、ID Austria 和 Klarna 的 Brokewell 应用程序列表如下：

jcwAz.EpLIq.vcAZiUGZpK（谷歌浏览器）
zRFxj.ieubP.lWZzwlluca（ID 奥地利）
com.brkwl.upstracking（克拉纳）
与最近的其他同类 Android 恶意软件家族一样，Brokewell 能够绕过 Google 施加的限制，这些限制阻止侧载应用程序请求辅助服务权限。

该银行木马一旦首次安装并启动，就会提示受害者向无障碍服务授予权限，随后利用该服务自动授予其他权限并执行各种恶意活动。

这包括在目标应用程序顶部显示覆盖屏幕以窃取用户凭据。它还可以通过启动WebView并加载合法网站来窃取 cookie，然后拦截会话 cookie 并将其传输到攻击者控制的服务器。

[![安卓恶意软件]( "安卓恶意软件")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhDFe4Qim0hJi7mtotLxngwrAosY81EGUxWGyMUYHVMm96SwNYbITY5gmTXDHSlO6_H2bqmtvy8xhn7awZHIafHuRzI-QoDaH5sU96wRMkxQApXITeONtcHG5BofsnUhyevzN7iYkTLCIuVkVOM96ndTuqGhBgodGBaFYnFbYmnrRPah_UIAL7DoaGCDpQh/s728-rw-e365/malware.png)

Brokewell 的其他一些功能包括录制音频、截屏、检索通话记录、访问设备位置、列出已安装的应用程序、记录设备上发生的每个事件、发送短信、拨打电话、安装和卸载应用程序的能力，甚至禁用辅助服务。

威胁行为者还可以利用恶意软件的远程控制功能来实时查看屏幕上显示的内容，并通过点击、滑动和触摸与设备进行交互。

据说 Brokewell 是一位名为“Baron Samedit Marais”的开发人员的作品，负责管理“Brokewell Cyber​​ Labs”项目，该项目还包括在 Gitea 上公开托管的 Android Loader。

该加载程序被设计为充当释放器，使用之前由释放器即服务 (DaaS) 产品（如SecuriDropper ）采用的技术来绕过 Android 版本 13、14 和 15 中的可访问权限限制，并部署木马植入程序。

默认情况下，通过此过程生成的加载程序应用程序的包名称为“com.brkwl.apkstore”，尽管用户可以通过提供特定名称或启用随机包名称生成器来配置此名称。

该加载程序的免费可用性意味着它可能会受到其他想要绕过 Android 安全保护的威胁行为者的欢迎。

ThreatFabric 表示：“其次，目前提供此功能作为独特功能的现有‘Dropper-as-a-Service’产品可能​​会关闭其服务或尝试重组。”

“这进一步降低了希望在现代设备上分发移动恶意软件的网络犯罪分子的进入门槛，使更多的参与者更容易进入该领域。”

本文翻译自 [原文链接](https://thehackernews.com/2024/04/new-brokewell-android-malware-spread.html)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/296083](/post/id/296083)

安全KER - 有思想的安全新媒体

本文转载自:

如若转载,请注明出处： <https://thehackernews.com/2024/04/new-brokewell-android-malware-spread.html>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

**+1**1赞

收藏

![](https://p3.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p1.ssl.qhimg.com/t014757b72460d855bf.png)

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