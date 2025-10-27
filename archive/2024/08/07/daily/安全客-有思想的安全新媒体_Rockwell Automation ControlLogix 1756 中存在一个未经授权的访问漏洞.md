---
title: Rockwell Automation ControlLogix 1756 中存在一个未经授权的访问漏洞
url: https://www.anquanke.com/post/id/298822
source: 安全客-有思想的安全新媒体
date: 2024-08-07
fetch_date: 2025-10-06T18:02:14.781499
---

# Rockwell Automation ControlLogix 1756 中存在一个未经授权的访问漏洞

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

# Rockwell Automation ControlLogix 1756 中存在一个未经授权的访问漏洞

阅读量**61687**

发布时间 : 2024-08-06 11:34:06

**x**

##### 译文声明

本文是翻译文章，文章原作者 Pierluigi Paganini，文章来源：securityaffairs

原文地址：<https://securityaffairs.com/166581/ics-scada/rockwell-automation-controllogix-1756-flaw.html>

译文仅供参考，具体内容表达以及含义原文为准。

跟踪为 CVE-2024-6242（CVSS 基本分数 v4.0 为 7.3）的高严重性安全绕过漏洞会影响 Rockwell Automation ControlLogix 1756 设备。攻击者可以利用此漏洞执行常见的工业协议 （CIP） 编程和配置命令。

“受影响的产品中存在一个漏洞，允许威胁参与者绕过 ControlLogix ® 控制器中的受信任®插槽功能。”“如果在 1756 机箱中的任何受影响的模块上被利用，威胁行为者可能会执行 CIP 命令，修改机箱中 Logix 控制器上的用户项目和/或设备配置。”

该漏洞影响以下版本的 ControlLogix、GuardLogix 和 1756 ControlLogix I/O 模块：

* 1756-EN2TP，A 系列：版本 V10.020
* ControlLogix：版本 V28
* GuardLogix：版本 V31
* 1756-EN4TR：版本 V2
* 1756-EN2T，A/B/C系列（未签名版本）：版本v5.007
* 1756-EN2F，A/B系列（未签名版本）：版本v5.007
* 1756-EN2TR，A/B 系列（未签名版本）：版本 v5.007
* 1756-EN3TR，B 系列（未签名版本）：版本 v5.007
* 1756-EN2T，A/B/C系列（签名版）：版本v5.027
* 1756-EN2F，A/B系列（签名版）：版本v5.027
* 1756-EN2TR，系列 A/B（签名版本）：版本 v5.027
* 1756-EN3TR，B 系列（签名版）：版本 v5.027
* 1756-EN2T，D 系列：版本 V10.006
* 1756-EN2F，C系列：版本V10.009
* 1756-EN2TR，C系列：版本V10.007
* 1756-EN3TR，B 系列：版本 V10.007

Claroty Research – Team82 的研究员 Sharon Brizinov 向罗克韦尔自动化报告了此漏洞。

攻击者需要对设备进行网络访问才能利用此漏洞。如果成功，攻击者可以绕过安全限制并向 PLC CPU 发送提升的命令。

*“Team82 发现并披露了罗克韦尔自动化 ControlLogix 1756 设备中的安全绕过漏洞。我们的技术使我们能够绕过罗克韦尔实施的受信任插槽功能，该功能执行安全策略，并允许控制器拒绝通过本地机箱上不受信任的路径进行通信。“我们发现的漏洞，在它被修复之前，允许攻击者使用CIP路由在1756机箱内的本地背板插槽之间跳转，穿越旨在保护CPU免受不受信任卡侵害的安全边界。”*

罗克韦尔解决了该漏洞，并敦促用户立即应用它。美国 CISA 还发布了一份包含缓解建议的咨询。

*Claroty总结道：“此漏洞有可能使关键控制系统暴露于未经授权的访问中，这些访问源自不受信任的机箱插槽的CIP协议。*

本文翻译自securityaffairs [原文链接](https://securityaffairs.com/166581/ics-scada/rockwell-automation-controllogix-1756-flaw.html)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/298822](/post/id/298822)

安全KER - 有思想的安全新媒体

本文转载自: [securityaffairs](https://securityaffairs.com/166581/ics-scada/rockwell-automation-controllogix-1756-flaw.html)

如若转载,请注明出处： <https://securityaffairs.com/166581/ics-scada/rockwell-automation-controllogix-1756-flaw.html>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [安全热点](/tag/%E5%AE%89%E5%85%A8%E7%83%AD%E7%82%B9)
* [漏洞情报](/tag/%E6%BC%8F%E6%B4%9E%E6%83%85%E6%8A%A5)

**+1**0赞

收藏

![](https://p5.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p5.ssl.qhimg.com/t014757b72460d855bf.png)

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