---
title: CISA 警告：Avtech 摄像机漏洞在野外被积极利用
url: https://www.anquanke.com/post/id/298767
source: 安全客-有思想的安全新媒体
date: 2024-08-06
fetch_date: 2025-10-06T18:02:30.727539
---

# CISA 警告：Avtech 摄像机漏洞在野外被积极利用

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

# CISA 警告：Avtech 摄像机漏洞在野外被积极利用

阅读量**71432**

发布时间 : 2024-08-05 14:48:58

**x**

##### 译文声明

本文是翻译文章，文章原作者 Pierluigi Paganini，文章来源：securityaffairs

原文地址：<https://securityaffairs.com/166471/hacking/avtech-camera-vulnerability-exploited.html>

译文仅供参考，具体内容表达以及含义原文为准。

## CISA 警告说，Avtech 摄像头漏洞仍未得到修补，正在野外积极利用。

美国网络安全和基础设施安全局 （CISA） 发布了一份公告，警告 Avtech 摄像头中存在一个漏洞，被跟踪为 CVE-2024-7029（CVSS 基本分数为 8.8），该漏洞已在野外被利用。

攻击者可利用此缺陷，以正在运行的进程的所有者身份注入和执行命令。

*“成功利用此漏洞可能允许攻击者作为正在运行的进程的所有者注入和执行命令，”CISA发布的**公告**中写道。* *“命令可以通过网络注入并在没有身份验证的情况下执行。”*

该漏洞会影响运行固件版本 FullImg-1023-1007-1011-1009 及更早版本的 Avtech AVM1203 IP 摄像机。

该机构表示，怀疑其他 IP 摄像机和 NVR（网络视频录像机）产品的先前版本也受到影响。

Akamai Technologies 的网络安全专家 Larry Cashdollar 向 CISA 报告了该漏洞。

CISA 试图将问题报告给尚未响应请求的供应商。

美国机构建议用户通过以下方式降低利用漏洞 CVE-2024-7029 的风险：

1. 限制控制系统设备的网络暴露，以防止互联网访问。
2. 将控制系统网络和远程设备置于防火墙后面，并将它们与业务网络隔离。
3. 使用 VPN 等安全的远程访问方法，确保它们是最新的并认识到它们的局限性。
4. 在实施防御措施之前，进行彻底的影响分析和风险评估。

已知有多个僵尸网络以 Avtech 设备为目标，包括 Mirai、Death 僵尸网络、Hide ‘N Seek 和 HNS。

本文翻译自securityaffairs [原文链接](https://securityaffairs.com/166471/hacking/avtech-camera-vulnerability-exploited.html)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/298767](/post/id/298767)

安全KER - 有思想的安全新媒体

本文转载自: [securityaffairs](https://securityaffairs.com/166471/hacking/avtech-camera-vulnerability-exploited.html)

如若转载,请注明出处： <https://securityaffairs.com/166471/hacking/avtech-camera-vulnerability-exploited.html>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [漏洞情报](/tag/%E6%BC%8F%E6%B4%9E%E6%83%85%E6%8A%A5)

**+1**0赞

收藏

![](https://p5.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p0.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p5.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=170338)

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

* [CISA 警告说，Avtech 摄像头漏洞仍未得到修补，正在野外积极利用。](#h2-0)

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