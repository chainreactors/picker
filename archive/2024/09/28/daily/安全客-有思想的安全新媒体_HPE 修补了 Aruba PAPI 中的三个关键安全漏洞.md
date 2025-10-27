---
title: HPE 修补了 Aruba PAPI 中的三个关键安全漏洞
url: https://www.anquanke.com/post/id/300484
source: 安全客-有思想的安全新媒体
date: 2024-09-28
fetch_date: 2025-10-06T18:22:33.080921
---

# HPE 修补了 Aruba PAPI 中的三个关键安全漏洞

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

# HPE 修补了 Aruba PAPI 中的三个关键安全漏洞

阅读量**150958**

发布时间 : 2024-09-27 14:28:44

**x**

##### 译文声明

本文是翻译文章，文章原作者 伊恩·汤姆森，文章来源：theregister

原文地址：<https://www.theregister.com/2024/09/26/hpe_aruba_patch_papi/>

译文仅供参考，具体内容表达以及含义原文为准。

运行AOS-8和AOS-10的Aruba接入点需要紧急打补丁，因为HPE为其网络子公司接入点中的三个关键漏洞发布了修复程序。

这些问题将允许未经身份验证的攻击者通过向UDP端口8211发送精心构造的数据包来在Aruba系统上执行代码。该端口是操作系统专有的访问协议接口（PAPI），这将为恶意人员提供对设备的特权访问。

这三个漏洞——CVE-2024-42505、CVE-2024-42506 和 CVE-2024-42507——在CVSS严重性评分中均被评为9.8（满分10分）。

这些漏洞影响AOS 10.6.x.x版本（包括10.6.0.2及之前版本）以及Instant AOS 8.12.x.x版本（8.12.0.1及更早版本）。HPE还警告说，已经停止支持的代码，包括AOS 10.5和10.3，以及Instant AOS-8.11及其之前的版本也受到影响，并建议升级这些系统以获得保护。

“通过启用cluster-security命令可以防止运行Instant AOS-8.x代码的设备被利用这些漏洞。”HPE在其安全警报中建议。“对于AOS-10设备来说，这不是一个选项，而应该从所有不受信任的网络中阻止对UDP端口8211的访问。”这不是PAPI今年首次被发现存在严重问题。早在五月份，Aruba就在公开的概念验证利用代码发布后修复了系统中的四个关键漏洞，并在不到一周后又发布了更多补丁。

这些补丁对于美国军方内的系统管理员尤为关切。早在2020年，Aruba就因成为五角大楼的首选供应商而取得重大胜利，当时军方与思科关系破裂并开始更换其设备。

HPE感谢Erik de Jong发现了这些漏洞，他是一名兼职漏洞研究员，日常工作是荷兰电信公司DELTA Fiber的安全官员。这些漏洞是通过Bugcrowd提交的，他表示自己的业余爱好帮助他还清了一部分房贷。

在发布时，HPE表示尚未发现有任何迹象表明这些问题已在野外被利用。然而，随着补丁的发布，鉴于问题的严重性，这种情况可能会发生变化。®

本文翻译自theregister [原文链接](https://www.theregister.com/2024/09/26/hpe_aruba_patch_papi/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/300484](/post/id/300484)

安全KER - 有思想的安全新媒体

本文转载自: [theregister](https://www.theregister.com/2024/09/26/hpe_aruba_patch_papi/)

如若转载,请注明出处： <https://www.theregister.com/2024/09/26/hpe_aruba_patch_papi/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [网络安全热点](/tag/%E7%BD%91%E7%BB%9C%E5%AE%89%E5%85%A8%E7%83%AD%E7%82%B9)
* [漏洞情报](/tag/%E6%BC%8F%E6%B4%9E%E6%83%85%E6%8A%A5)

**+1**0赞

收藏

![](https://p2.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p2.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p2.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=170338)

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