---
title: 360漏洞研究院：Fortinet FortiClientEMS SQL注入漏洞发布
url: https://www.anquanke.com/post/id/293977
source: 安全客-有思想的安全新媒体
date: 2024-03-15
fetch_date: 2025-10-04T12:07:31.348566
---

# 360漏洞研究院：Fortinet FortiClientEMS SQL注入漏洞发布

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

# 360漏洞研究院：Fortinet FortiClientEMS SQL注入漏洞发布

阅读量**109395**

发布时间 : 2024-03-14 19:26:52

**x**

##### 译文声明

本文是翻译文章

原文地址：<https://loudongyun.360.net/leakDetail/YHfsPtDbaq4%3D>

译文仅供参考，具体内容表达以及含义原文为准。

**漏洞信息：**

漏洞编号：CVE-2023-48788

漏洞类型：SQL注入

漏洞等级：严重(9.8)

所属厂商：Fortinet

发布时间：2024-03-14 18:15:14

**漏洞描述：**

Fortinet FortiClientEMS 是一款用于管理和保护 Fortinet FortiClient 客户端安全性的集中式管理平台。

Fortinet FortiClientEMS 平台存在一个 SQL注入漏洞，未经认证的远程攻击者可通过创建恶意日志条目，并向服务器发出精心制作的请求，成功的利用此漏洞可在管理员工作站上执行任意命令。

**影响版本：**

7.2.0 <=FortiClientEMS<=7.2.2

7.0.1 <=FortiClientEMS<=7.0.10

**修复建议：**

 **正式防护方案：**

 官方已修复该漏洞，建议用户更新到安全版本。

安全版本:

FortiClientEMS >= 7.2.3

FortiClientEMS >= 7.0.11

官方链接：https://fortiguard.com/psirt/FG-IR-23-430

**产品侧解决方案：**

 **360资产与漏洞检测管理系统**

360资产与漏洞检测管理系统（天相），是基于安全运营、应急响应需求场景开发的常态化资产威胁管理系统。通过运用资产威胁情报以及先进的资产威胁探测引擎，全面识别、管理组织IT边界，确定资产属性、快速发现安全漏洞、精准定位安全风险。

 **360高级持续性威胁预警系统**

360高级持续性威胁预警系统是360自主研发的通过流量深度分析结合全球威胁情报、攻击行为分析、机器学习、关联分析等新一代安全技术对各类型网络攻击行为进行检测、分析、响应的软硬件一体机产品。

 **360本地安全大脑**

360本地安全大脑是将360云端安全大脑核心能力本地化部署的一套开放式全场景安全运营平台，实现安全态势、监控、分析、溯源、研判、响应、管理的智能化安全运营赋能。

**参考资料：**

https://fortiguard.com/psirt/FG-IR-23-430

<https://nvd.nist.gov/vuln/detail/CVE-2023-48788>

**获取更多情报：**

建议您订阅360漏洞云–漏洞情报服务，获取更多漏洞情报详情以及处置建议，让您的企业远离漏洞威胁。

本文翻译自 [原文链接](https://loudongyun.360.net/leakDetail/YHfsPtDbaq4%3D)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/293977](/post/id/293977)

安全KER - 有思想的安全新媒体

本文转载自:

如若转载,请注明出处： <https://loudongyun.360.net/leakDetail/YHfsPtDbaq4%3D>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [漏洞情报](/tag/%E6%BC%8F%E6%B4%9E%E6%83%85%E6%8A%A5)

**+1**4赞

收藏

![](https://p3.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p1.ssl.qhimg.com/t014757b72460d855bf.png)

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