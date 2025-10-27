---
title: UserPro 插件漏洞允许帐户被接管
url: https://www.anquanke.com/post/id/296740
source: 安全客-有思想的安全新媒体
date: 2024-05-24
fetch_date: 2025-10-06T16:48:51.999081
---

# UserPro 插件漏洞允许帐户被接管

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

# UserPro 插件漏洞允许帐户被接管

阅读量**85373**

发布时间 : 2024-05-23 11:30:45

**x**

##### 译文声明

本文是翻译文章

原文地址：<https://www.infosecurity-magazine.com/news/userpro-plugin-flaw-allows-account/>

译文仅供参考，具体内容表达以及含义原文为准。

UserPro 插件是由 DeluxeThemes 开发的 WordPress 流行社区和用户配置文件工具，被发现存在重大安全漏洞。

该插件被超过 20,000 个网站使用，使用户能够创建可定制的前端配置文件和社区网站。

Patchstack 发现了插件密码重置机制中的严重缺陷，特别是在 userpro\_process\_form 函数中，该缺陷允许未经身份验证的用户在某些条件下更改其他用户的密码。

该漏洞编号为 CVE-2024-35700，是由于密码重置过程中使用的“密钥”处理不当造成的。该功能无法正确验证密钥，从而使攻击者能够利用这种疏忽并获得对用户帐户的未经授权的访问。

UserPro 插件的漏洞被认为是严重的，因为它允许潜在的攻击者使用密钥集更改用户的密码，这通常在用户请求重置密码时使用。

攻击者可以通过启动密码重置，然后在合法用户完成该过程之前拦截或操纵密钥来利用此漏洞。

Patchstack 警告说：“请注意，在默认安装和激活 UserPro 插件时，无需特定要求或配置即可重现此漏洞。”

该公司于 2024 年 5 月 21 日将该问题添加到其漏洞数据库中，并于第二天发布了公开公告。此漏洞存在于 UserPro 插件的所有版本中，最高版本为 5.1.8。供应商迅速做出回应，于 2024 年 4 月 29 日发布了修补版本 5.1.9。

Patchstack 建议所有 UserPro 用户立即将其插件更新到至少版本 5.1.9。

“这里讨论的漏洞强调了保护插件各个方面安全的重要性，特别是那些旨在更改用户密码的漏洞” Patchstack 写道。 “始终确保传递给关键函数以更新用户密码的对象或变量已经过验证并事先经过检查。”

本文翻译自 [原文链接](https://www.infosecurity-magazine.com/news/userpro-plugin-flaw-allows-account/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/296740](/post/id/296740)

安全KER - 有思想的安全新媒体

本文转载自:

如若转载,请注明出处： <https://www.infosecurity-magazine.com/news/userpro-plugin-flaw-allows-account/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [漏洞情报](/tag/%E6%BC%8F%E6%B4%9E%E6%83%85%E6%8A%A5)

**+1**1赞

收藏

![](https://p3.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p4.ssl.qhimg.com/t014757b72460d855bf.png)

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