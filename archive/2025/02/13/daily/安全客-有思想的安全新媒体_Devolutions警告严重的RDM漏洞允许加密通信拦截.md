---
title: Devolutions警告严重的RDM漏洞允许加密通信拦截
url: https://www.anquanke.com/post/id/304187
source: 安全客-有思想的安全新媒体
date: 2025-02-13
fetch_date: 2025-10-06T20:34:15.153426
---

# Devolutions警告严重的RDM漏洞允许加密通信拦截

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

# Devolutions警告严重的RDM漏洞允许加密通信拦截

阅读量**52353**

发布时间 : 2025-02-12 11:04:04

**x**

##### 译文声明

本文是翻译文章，文章原作者 do son，文章来源：securityonline

原文地址：<https://securityonline.info/devolutions-warns-of-severe-rdm-vulnerabilities-allowing-encrypted-communication-interception/>

译文仅供参考，具体内容表达以及含义原文为准。

![]()

远程连接管理解决方案的领先供应商 Devolutions 发布了一份安全公告，针对其跨多个平台的远程桌面管理器（RDM）产品所存在的严重漏洞进行了说明。这些漏洞可能会让攻击者拦截并修改加密通信内容，进而有可能危及敏感数据和系统的安全。

这些漏洞源于 RDM 的证书验证逻辑存在缺陷。在 Windows 平台上（漏洞编号为 CVE-2025-1193，通用漏洞评分系统第 4 版（CVSSv4）评分为 8.5），证书验证无法对主机进行有效验证；而在其他平台上（漏洞编号为 CVE-2024-11621，CVSSv4 评分为 8.6），则完全不存在证书验证环节，会在不提示用户的情况下接受任何证书。

公告中提到：“具体而言，在 Windows 平台上，证书验证无法对主机进行验证。在其他平台上，证书验证缺失，会在不向用户发出提示的情况下接受任何证书。”

这些漏洞可能会让攻击者实施中间人攻击，拦截并修改用户与远程系统之间的加密通信流量。这可能会导致凭据被盗取，以及对敏感数据的未经授权访问。

Devolutions 已针对所有受影响的平台发布了补丁。强烈建议用户和管理员立即进行升级：

|  |  |  |
| --- | --- | --- |
| ****平台**** | ****存在漏洞的版本**** | ****已修复版本**** |
| Windows | 2024.3.19 及更早版本 | 2024.3.20.0 及更高版本 |
| macOS | 2024.3.9.0 及更早版本 | 2024.3.10.3 及更高版本 |
| Linux | 2024.3.2.5 及更早版本 | 2024.3.2.9 及更高版本 |
| 安卓 | 2024.3.3.7 及更早版本 | 2024.3.4.2 及更高版本 |
| iOS | 2024.3.3.0 及更早版本 | 2024.3.4.0 及更高版本 |
| PowerShell | 2024.3.6.0 及更早版本 | 2024.3.7.0 及更高版本 |

依赖远程桌面管理器的机构应立即采取行动，以确保其运行的是最新的安全版本。

本文翻译自securityonline [原文链接](https://securityonline.info/devolutions-warns-of-severe-rdm-vulnerabilities-allowing-encrypted-communication-interception/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/304187](/post/id/304187)

安全KER - 有思想的安全新媒体

本文转载自: [securityonline](https://securityonline.info/devolutions-warns-of-severe-rdm-vulnerabilities-allowing-encrypted-communication-interception/)

如若转载,请注明出处： <https://securityonline.info/devolutions-warns-of-severe-rdm-vulnerabilities-allowing-encrypted-communication-interception/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [漏洞情报](/tag/%E6%BC%8F%E6%B4%9E%E6%83%85%E6%8A%A5)

**+1**4赞

收藏

![](https://p5.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p5.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p5.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=170061)

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