---
title: 重磅！CISA 新增Palo Alto Networks与SonicWall至被利用漏洞名单
url: https://www.anquanke.com/post/id/304497
source: 安全客-有思想的安全新媒体
date: 2025-02-20
fetch_date: 2025-10-06T20:33:14.900999
---

# 重磅！CISA 新增Palo Alto Networks与SonicWall至被利用漏洞名单

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

# 重磅！CISA 新增Palo Alto Networks与SonicWall至被利用漏洞名单

阅读量**62782**

|评论**1**

发布时间 : 2025-02-19 14:38:32

**x**

##### 译文声明

本文是翻译文章，文章原作者 Ravie Lakshmanan，文章来源：TheHackersNews

原文地址：<https://thehackernews.com/2025/02/cisa-adds-palo-alto-networks-and.html>

译文仅供参考，具体内容表达以及含义原文为准。

美国网络安全与基础设施安全局（CISA）周二基于漏洞已被实际利用的证据，将两个影响Palo Alto Networks的 PAN-OS 系统以及SonicWall公司的 SonicOS SSLVPN 系统的安全漏洞，纳入了其已知被利用漏洞（KEV）目录。

以下是这些漏洞的具体信息：

1.CVE-2025-0108（通用漏洞评分系统得分：7.8）—— Palo Alto Networks的 PAN-OS 系统管理 Web 界面中存在一个身份验证绕过漏洞。该漏洞使得具备对管理 Web 界面网络访问权限的未经身份验证的攻击者，能够绕过正常所需的身份验证过程，并调用某些 PHP 脚本。

2.CVE-2024-53704（通用漏洞评分系统得分：8.2）——SSLVPN 身份验证机制中存在一个身份验证不当漏洞，该漏洞允许远程攻击者绕过身份验证。

Palo Alto Networks随后向The Hacker News证实，他们已观察到针对 CVE-2025-0108 漏洞的实际利用尝试。该公司指出，此漏洞可与 CVE-2024-9474 等其他漏洞结合使用，从而实现对未打补丁且未加固的防火墙的未经授权访问。

该公司在一份更新的安全公告中表示：“Palo Alto Networks已观察到，在未打补丁且未加固的 PAN-OS 系统 Web 管理界面上，存在将 CVE-2025-0108 与 CVE-2024-9474 以及 CVE-2025-0111 漏洞结合起来的攻击尝试。”

威胁情报公司 GreyNoise 表示，多达 25 个恶意 IP 地址正在积极利用 CVE-2025-0108 漏洞，自大约一周前该漏洞被检测到以来，攻击者的活动量激增了 10 倍。攻击流量的前三大来源地分别是美国、德国和荷兰。

至于 CVE-2024-53704 漏洞，网络安全公司Arctic Wolf透露，在Bishop Fox公司发布该漏洞的概念验证（PoC）后不久，威胁行为者便开始利用这一漏洞实施攻击。

鉴于这些漏洞已被实际利用，美国联邦政府行政部门（FCEB）的各机构被要求在 2025 年 3 月 11 日前修复这些已识别的漏洞，以保障其网络安全。

本文翻译自TheHackersNews [原文链接](https://thehackernews.com/2025/02/cisa-adds-palo-alto-networks-and.html)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/304497](/post/id/304497)

安全KER - 有思想的安全新媒体

本文转载自: [TheHackersNews](https://thehackernews.com/2025/02/cisa-adds-palo-alto-networks-and.html)

如若转载,请注明出处： <https://thehackernews.com/2025/02/cisa-adds-palo-alto-networks-and.html>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [漏洞情报](/tag/%E6%BC%8F%E6%B4%9E%E6%83%85%E6%8A%A5)

**+1**0赞

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