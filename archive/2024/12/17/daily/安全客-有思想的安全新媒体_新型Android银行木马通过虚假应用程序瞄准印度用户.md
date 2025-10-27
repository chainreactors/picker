---
title: 新型Android银行木马通过虚假应用程序瞄准印度用户
url: https://www.anquanke.com/post/id/302724
source: 安全客-有思想的安全新媒体
date: 2024-12-17
fetch_date: 2025-10-06T19:34:51.135873
---

# 新型Android银行木马通过虚假应用程序瞄准印度用户

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

# 新型Android银行木马通过虚假应用程序瞄准印度用户

阅读量**52149**

|评论**1**

发布时间 : 2024-12-16 10:26:42

**x**

##### 译文声明

本文是翻译文章，文章原作者 do son，文章来源：securityonline

原文地址：<https://securityonline.info/new-android-banking-trojan-targets-indian-users-through-fake-apps/>

译文仅供参考，具体内容表达以及含义原文为准。

McAfee 实验室发现了一种针对印度用户的新型安卓银行木马，该木马利用印度用户对实用程序和银行应用程序的依赖性来窃取敏感的金融信息。这个被检测为Android/Banker的复杂恶意软件已经感染了419台设备，截获了4918条短信，并窃取了623条银行卡和银行相关信息，预计随着活动的发展，数量还会增加。

该恶意软件伪装成实用程序和银行应用程序，通过网络钓鱼活动诱骗用户下载恶意 APK，通常通过 WhatsApp 等平台传播。McAfee解释说：“这种恶意软件伪装成基本服务，如公用事业（如煤气或电力）或银行应用程序，以获取用户的敏感信息”。其中一个变种甚至使用了印度流行的支付平台 PayRup 的徽标，以显示其合法性。

一旦安装，该应用程序：

1. 请求访问短信等个人数据的权限。
2. 以付款为幌子，提示用户输入财务信息。
3. 将窃取的数据发送到命令与控制（C2）服务器，同时显示虚假的 “支付失败 ”消息以维持骗局。

该恶意软件采用了几种先进的策略来逃避检测并最大限度地扩大影响：

* **隐藏应用程序图标**：通过在代码中省略 “android.intent.category.LAUNCHER ”属性，应用程序的图标不会出现在用户的启动器上，使其在安装后更难识别。
* **通过 Supabase 进行数据渗透**： 该恶意软件独特地使用 Supabase（一种开源的后台即服务）来存储窃取的数据。McAfee 调查人员在恶意软件的 Supabase 数据库中发现了 5,558 条记录，其中包括敏感的财务数据，这些数据是通过应用程序代码中暴露的 JSON 网络令牌 (JWT) 访问的。

印度作为 WhatsApp 最大的用户群，使其成为网络钓鱼的主要目标。该木马利用 WhatsApp 消息引诱受害者安装旨在模仿主要金融和公用事业提供商服务的虚假应用程序，例如：

* **Axis Bank (ax\_17.customer)**
* **旁遮普国家银行 (pnb\_5.customer)**
* **煤气和电费支付 (gs\_5.customer, elect\_5.customer)**

McAfee 发现，每个诈骗主题都会产生多个变种，从而扩大了恶意软件的影响范围，并使检测工作变得更加复杂。

与以往的恶意软件活动不同，该木马包含一个管理其 C2 基础设施的移动应用程序，允许操作员直接从其设备发送命令。这一功能使攻击者能够转发截获的短信并管理窃取的数据。

本文翻译自securityonline [原文链接](https://securityonline.info/new-android-banking-trojan-targets-indian-users-through-fake-apps/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/302724](/post/id/302724)

安全KER - 有思想的安全新媒体

本文转载自: [securityonline](https://securityonline.info/new-android-banking-trojan-targets-indian-users-through-fake-apps/)

如若转载,请注明出处： <https://securityonline.info/new-android-banking-trojan-targets-indian-users-through-fake-apps/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [安全资讯](/tag/%E5%AE%89%E5%85%A8%E8%B5%84%E8%AE%AF)
* [网络攻击](/tag/%E7%BD%91%E7%BB%9C%E6%94%BB%E5%87%BB)

**+1**2赞

收藏

![](https://p1.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p4.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p1.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=173683)

[安全客](/member.html?memberId=173683)

这个人太懒了，签名都懒得写一个

* 文章
* **553**

* 粉丝
* **2**

### TA的文章

* ##### [年度盘点：AI+安全双重赋能，360解锁企业浏览器新动力](/post/id/303791)

  2025-01-24 10:00:53
* ##### [IntelBroker 的数字足迹： OSINT 分析揭露网络犯罪分子的行动](/post/id/303788)

  2025-01-24 09:55:58
* ##### [7-Zip 修复了可绕过 Windows MoTW 安全警告的错误，立即修补](/post/id/303776)

  2025-01-24 09:49:56
* ##### [Microsoft 在 Edge Stable 中预览 Game Assist 游戏内浏览器](/post/id/303773)

  2025-01-24 09:43:16
* ##### [ModiLoader 恶意软件利用 CAB 标头批处理文件逃避检测](/post/id/303770)

  2025-01-24 09:36:10

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