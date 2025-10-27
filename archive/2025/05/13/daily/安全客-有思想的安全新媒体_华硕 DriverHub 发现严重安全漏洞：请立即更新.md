---
title: 华硕 DriverHub 发现严重安全漏洞：请立即更新
url: https://www.anquanke.com/post/id/307290
source: 安全客-有思想的安全新媒体
date: 2025-05-13
fetch_date: 2025-10-06T22:23:28.076772
---

# 华硕 DriverHub 发现严重安全漏洞：请立即更新

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

# 华硕 DriverHub 发现严重安全漏洞：请立即更新

阅读量**165330**

发布时间 : 2025-05-12 14:10:16

**x**

##### 译文声明

本文是翻译文章，文章原作者 Ddos，文章来源：securityonline

原文地址：<https://securityonline.info/critical-security-flaws-found-in-asus-driverhub-update-immediately/>

译文仅供参考，具体内容表达以及含义原文为准。

![华硕 DriverHub，漏洞]()

ASUS DriverHub 是一款旨在通过自动检测主板型号并显示可用更新来简化驱动程序更新的工具，但它被发现存在严重的安全漏洞。

根据最近的安全公告，两个漏洞（分别为 CVE-2025-3462 和 CVE-2025-3463）对该 软件用户构成风险。需要注意的是，“*此问题仅限于主板，不会影响笔记本电脑、台式电脑或其他终端*。”

以下是漏洞的详细情况：

* **CVE-2025-3462 (CVSSv4 8.4)：**此漏洞源于 DriverHub 对某些 HTTP 请求的处理方式验证不足。远程攻击者可以通过伪造通常仅供受信任的内部来源使用的通信，与内部软件功能进行交互。
* **CVE-2025-3463 (CVSSv4 9.4)：**此漏洞被认为较为严重。“*华硕 DriverHub 中存在一个验证不足的漏洞，可能允许不受信任的来源通过精心设计的 HTTP 请求影响系统行为*。” 虽然该漏洞的利用场景尚未公开演示，但远程影响主板驱动程序管理软件的能力构成了重大风险，尤其对于在易受攻击的网络环境中操作的用户而言。

这两个漏洞都源于对 HTTP 请求的验证不足，这可能使恶意行为者能够向 DriverHub 软件发送特制的请求并可能获得未经授权的控制。

华硕敦促用户将华硕 DriverHub 更新至最新版本 1.0.6.0 或更新版本。

该公司建议道：“*此更新包含重要的安全更新，华硕强烈建议用户将其 ASUS DriverHub 安装更新至最新版本。 ”*

**如何更新：**

1. 打开**ASUS DriverHub**实用程序。
2. 单击**“立即更新”**按钮。
3. 按照屏幕上的提示完成修补过程。

本文翻译自securityonline [原文链接](https://securityonline.info/critical-security-flaws-found-in-asus-driverhub-update-immediately/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/307290](/post/id/307290)

安全KER - 有思想的安全新媒体

本文转载自: [securityonline](https://securityonline.info/critical-security-flaws-found-in-asus-driverhub-update-immediately/)

如若转载,请注明出处： <https://securityonline.info/critical-security-flaws-found-in-asus-driverhub-update-immediately/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [安全资讯](/tag/%E5%AE%89%E5%85%A8%E8%B5%84%E8%AE%AF)
* [漏洞情报](/tag/%E6%BC%8F%E6%B4%9E%E6%83%85%E6%8A%A5)

**+1**10赞

收藏

![](https://p1.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p2.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p1.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=170061)

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