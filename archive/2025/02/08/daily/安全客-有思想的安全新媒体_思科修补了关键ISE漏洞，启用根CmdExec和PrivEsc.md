---
title: 思科修补了关键ISE漏洞，启用根CmdExec和PrivEsc
url: https://www.anquanke.com/post/id/303920
source: 安全客-有思想的安全新媒体
date: 2025-02-08
fetch_date: 2025-10-06T20:33:52.782196
---

# 思科修补了关键ISE漏洞，启用根CmdExec和PrivEsc

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

# 思科修补了关键ISE漏洞，启用根CmdExec和PrivEsc

阅读量**583069**

发布时间 : 2025-02-07 10:36:42

**x**

##### 译文声明

本文是翻译文章，文章原作者 Ravie Lakshmanan，文章来源：TheHackersNews

原文地址：<https://thehackernews.com/2025/02/cisco-patches-critical-ise.html>

译文仅供参考，具体内容表达以及含义原文为准。

思科已发布更新，以修复身份服务引擎（ISE）存在的两个严重安全漏洞。这些漏洞可能使远程攻击者在易受攻击的设备上执行任意命令并提升权限。

以下为相关漏洞：

* **CVE – 2025 – 20124（CVSS 评分：9.9）**：思科 ISE 的一个应用程序编程接口（API）存在不安全的 Java 反序列化漏洞，这使得经过身份验证的远程攻击者能够以 root 用户身份在受影响设备上执行任意命令。
* **CVE – 2025 – 20125（CVSS 评分：9.1）**：思科 ISE 的一个 API 存在授权绕过漏洞，持有有效只读凭证且经过身份验证的远程攻击者可借此获取敏感信息、更改节点配置并重启节点。

攻击者可通过向某个未明确说明的 API 端点发送精心构造的序列化 Java 对象或 HTTP 请求，利用上述任意一个漏洞，进而实现权限提升与代码执行。

**网络安全方面**：
思科称这两个漏洞相互独立，且没有可缓解漏洞影响的临时解决方案。以下版本已修复这些漏洞：

* 思科 ISE 软件版本 3.0（需迁移至修复版本）
* 思科 ISE 软件版本 3.1（在 3.1P10 版本中修复）
* 思科 ISE 软件版本 3.2（在 3.2P7 版本中修复）
* 思科 ISE 软件版本 3.3（在 3.3P4 版本中修复）
* 思科 ISE 软件版本 3.4（不存在此漏洞）

德勤安全研究人员丹・马林（Dan Marin）和塞巴斯蒂安・拉杜莱亚（Sebastian Radulea）因发现并报告这些漏洞而获赞誉。

尽管这家网络设备巨头表示尚未察觉到这些漏洞被恶意利用的情况，但仍建议用户及时更新系统，以获得最佳防护。

本文翻译自TheHackersNews [原文链接](https://thehackernews.com/2025/02/cisco-patches-critical-ise.html)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/303920](/post/id/303920)

安全KER - 有思想的安全新媒体

本文转载自: [TheHackersNews](https://thehackernews.com/2025/02/cisco-patches-critical-ise.html)

如若转载,请注明出处： <https://thehackernews.com/2025/02/cisco-patches-critical-ise.html>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [漏洞情报](/tag/%E6%BC%8F%E6%B4%9E%E6%83%85%E6%8A%A5)

**+1**13赞

收藏

![](https://p1.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p5.ssl.qhimg.com/t014757b72460d855bf.png)

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