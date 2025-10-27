---
title: 黑客利用 WP-Automatic 插件漏洞在 WordPress 网站上创建管理员帐户
url: https://www.anquanke.com/post/id/296080
source: 安全客-有思想的安全新媒体
date: 2024-04-29
fetch_date: 2025-10-04T12:14:36.070952
---

# 黑客利用 WP-Automatic 插件漏洞在 WordPress 网站上创建管理员帐户

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

# 黑客利用 WP-Automatic 插件漏洞在 WordPress 网站上创建管理员帐户

阅读量**85482**

发布时间 : 2024-04-28 11:13:43

**x**

##### 译文声明

本文是翻译文章

译文仅供参考，具体内容表达以及含义原文为准。

威胁参与者正试图积极利用 WordPress 的 ValvePress 自动插件中的一个关键安全漏洞，该漏洞可能允许网站被接管。

该缺陷的编号为CVE-2024-27956，CVSS 评分为 9.9 分（满分 10 分）。它影响 3.92.0 之前的所有插件版本。该问题已在 2024 年 2 月 27 日发布的3.92.1 版本中得到解决，尽管发行说明中没有提及。

WPScan 表示：“这个漏洞是一个 SQL 注入 (SQLi) 缺陷，会造成严重威胁，因为攻击者可以利用它来获得对网站的未经授权的访问、创建管理员级用户帐户、上传恶意文件，并可能完全控制受影响的网站。”在本周的警报中说。

据 Automattic 旗下公司称，该问题根源于该插件的用户身份验证机制，可以轻松绕过该机制，通过特制请求对数据库执行任意 SQL 查询。

在迄今为止观察到的攻击中，CVE-2024-27956 被用于未经授权的数据库查询，并在易受影响的 WordPress 网站上创建新的管理员帐户（例如，以“xtw”开头的名称），然后可以利用这些帐户进行后续攻击。剥削行为。

这包括安装可以上传文件或编辑代码的插件，表明试图将受感染的站点重新用作舞台。

WPScan 表示：“一旦 WordPress 网站遭到入侵，攻击者就会通过创建后门和混淆代码来确保其访问的长期性。” “为了逃避检测并保持访问，攻击者还可能重命名易受攻击的 WP-Automatic 文件，从而使网站所有者或安全工具难以识别或阻止该问题。”

有问题的文件是“/wp-content/plugins/wp-automatic/inc/csv.php”，它被重命名为“/wp-content/plugins/wp-automatic/inc/csv65f82ab408b3.php”。

也就是说，威胁行为者这样做可能是为了阻止其他攻击者利用已经在他们控制下的网站。

CVE-2024-27956由 WordPress 安全公司 Patchstack 于 2024 年 3 月 13 日公开披露。此后，已在野外检测到超过 550 万次将该漏洞武器化的攻击尝试。

此次披露是由于 Icegram Express 的电子邮件订阅者（ CVE-2024-2876，CVSS 分数：9.8）、Forminator（CVE-2024-28890，CVSS 分数：9.8）和用户注册（CVE-2024-28890，CVSS 分数：9.8）等插件中披露了严重错误。 2024-2417，CVSS 分数：8.8），可用于从数据库中提取密码哈希等敏感数据、上传任意文件以及授予身份验证器用户管理权限。

Patchstack 还警告Poll Maker 插件中存在未修补的问题（CVE-2024-32514，CVSS 评分：9.9），该问题允许经过身份验证的攻击者（具有订户级及以上访问权限）在受影响站点的服务器上上传任意文件，从而导致远程代码执行。

本文翻译自 原文链接。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/296080](/post/id/296080)

安全KER - 有思想的安全新媒体

本文转载自:

如若转载,请注明出处：

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

**+1**2赞

收藏

![](https://p4.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p4.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p4.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=170338)

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