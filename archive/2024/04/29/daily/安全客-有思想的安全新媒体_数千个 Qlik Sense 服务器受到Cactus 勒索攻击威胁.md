---
title: 数千个 Qlik Sense 服务器受到Cactus 勒索攻击威胁
url: https://www.anquanke.com/post/id/296089
source: 安全客-有思想的安全新媒体
date: 2024-04-29
fetch_date: 2025-10-04T12:14:31.950224
---

# 数千个 Qlik Sense 服务器受到Cactus 勒索攻击威胁

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

# 数千个 Qlik Sense 服务器受到Cactus 勒索攻击威胁

阅读量**74658**

发布时间 : 2024-04-28 11:35:57

**x**

##### 译文声明

本文是翻译文章

原文地址：<https://www.darkreading.com/cyber-risk/more-than-3-000-qlik-sense-servers-vuln-to-cactus-ransomware-attacks>

译文仅供参考，具体内容表达以及含义原文为准。

在安全研究人员警告 Cactus 勒索软件团伙利用 Qlik Sense 数据分析和商业智能 (BI) 平台中的三个漏洞的近五个月后，许多组织仍然容易受到威胁。

Qlik 在 8 月和 9 月披露了这些漏洞。该公司 8 月份的披露涉及 Qlik Sense Enterprise for Windows 多个版本中的两个错误，分别为CVE-2023-41266 和 CVE-2023-41265。这些漏洞一旦串联起来，就会为未经身份验证的远程攻击者提供在受影响的系统上执行任意代码的方法。 9 月，Qlik 披露了CVE-2023-48365，事实证明，该漏洞是 Qlik 对 8 月份前两个缺陷的修复的绕过。

Gartner 将 Qlik 评为市场上顶级数据可视化和 BI 供应商之一。

Qlik 安全漏洞的持续利用

两个月后，Arctic Wolf报告称观察到 Cactus 勒索软件的操作者利用这三个漏洞在目标环境中获得了初步立足点。当时，该安全供应商表示，它正在对多起客户遭遇 Qlik Sense 漏洞攻击的事件做出响应，并警告 Cactus 组织活动正在迅速发展。

即便如此，许多组织似乎还没有收到这份备忘录。 Fox-IT 研究人员于 4 月 17 日进行的扫描发现，共有 5,205 台可通过互联网访问的 Qlik Sense 服务器，其中3,143 台服务器仍然容易受到 Cactus 组织的攻击。其中，396 台服务器似乎位于美国。其他易受攻击的 Qlik Sense 服务器数量相对较多的国家包括意大利（280 台）、巴西（244 台）、荷兰和德国（分别为 241 台和 175 台）。

Fox-IT 是荷兰的安全组织之一，其中包括荷兰漏洞披露研究所 (DIVD)，它们在名为“梅丽莎计划”的支持下合作，以扰乱 Cactus 集团的运营。

发现易受攻击的服务器后，Fox-IT 将其指纹和扫描数据转发给 DIVD，DIVD 然后开始联系易受攻击的 Qlik Sense 服务器的管理员，了解其组织是否面临潜在的 Cactus 勒索软件攻击。在某些情况下，DIVD 直接向潜在受害者发送通知，而在其他情况下，该组织试图通过各自国家的计算机应急响应小组将信息转发给他们。

安全组织正在通知潜在的仙人掌勒索软件受害者

ShadowServer 基金会也正在向面临风险的组织伸出援手。在本周的一份重要警报中，非营利性威胁情报服务将这种情况描述为：如果不采取补救措施，组织很可能会受到损害。

ShadowServer 表示：“如果您收到我们发出的有关在您的网络或选区中检测到易受攻击实例的警报，请同时假设您的实例以及可能的网络已受到损害。” “通过检查是否存在带有 .ttf 或 .woff 文件扩展名的文件来远程确定受感染的实例。”

Fox-IT 表示，已发现至少 122 个 Qlik Sense 实例可能因这三个漏洞而受到损害。其中四十九人在美国； 13 西班牙； 11 意大利；其余的则分布在其他 17 个国家。 Fox-IT 表示：“当远程 Qlik Sense 服务器上出现受损痕迹时，这可能意味着各种情况。”例如，它可能表明攻击者在服务器上远程执行代码，或者它可能只是先前安全事件的产物。

Fox-IT 表示：“重要的是要明白，‘已经受到损害’可能意味着要么勒索软件已经部署，但留下的初始访问工件没有被删除，要么系统仍然受到损害，并可能为未来的勒索软件攻击做好准备。” 。

本文翻译自 [原文链接](https://www.darkreading.com/cyber-risk/more-than-3-000-qlik-sense-servers-vuln-to-cactus-ransomware-attacks)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/296089](/post/id/296089)

安全KER - 有思想的安全新媒体

本文转载自:

如若转载,请注明出处： <https://www.darkreading.com/cyber-risk/more-than-3-000-qlik-sense-servers-vuln-to-cactus-ransomware-attacks>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [漏洞情报](/tag/%E6%BC%8F%E6%B4%9E%E6%83%85%E6%8A%A5)

**+1**3赞

收藏

![](https://p3.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p2.ssl.qhimg.com/t014757b72460d855bf.png)

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

* ##### [Apache Airflow 存在权限漏洞，可导致只读用户获取敏感信息](/post/id/312457)

  2025-09-29 18:05:56
* ##### [Formbricks 存在高危漏洞 (CVE-2025-59934)，攻击者可通过伪造JWT令牌导致未授权的密码重置](/post/id/312451)

  2025-09-29 18:05:05
* ##### [Notepad++ 中存在DLL劫持漏洞（CVE-2025-56383），可导致任意代码执行，且POC已公开](/post/id/312448)

  2025-09-29 18:04:33
* ##### [CISA称黑客利用GeoServer漏洞成功入侵一联邦机构](/post/id/312347)

  2025-09-24 16:45:06
* ##### [SolarWinds紧急发布补丁，修复高危远程代码执行漏洞CVE-2025-26399](/post/id/312357)

  2025-09-24 16:43:11
* ##### [Chrome浏览器存在高危漏洞，可致攻击者窃取敏感信息并引发系统崩溃](/post/id/312366)

  2025-09-24 16:42:08
* ##### [CVE-2025-55241：CVSS评分10.0的Microsoft Entra ID漏洞可能危及全球所有租户](/post/id/312294)

  2025-09-22 18:14:51

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