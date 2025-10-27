---
title: 勒索软件团伙 RansomHub 依赖于卡巴斯基 TDSKiller 工具来禁用 EDR
url: https://www.anquanke.com/post/id/300028
source: 安全客-有思想的安全新媒体
date: 2024-09-13
fetch_date: 2025-10-06T18:20:07.226430
---

# 勒索软件团伙 RansomHub 依赖于卡巴斯基 TDSKiller 工具来禁用 EDR

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

# 勒索软件团伙 RansomHub 依赖于卡巴斯基 TDSKiller 工具来禁用 EDR

阅读量**72915**

发布时间 : 2024-09-12 14:52:01

**x**

##### 译文声明

本文是翻译文章，文章原作者 Pierluigi Paganini，文章来源：securityaffairs

原文地址：<https://securityaffairs.com/168296/malware/ransomhub-ransomware-tdskiller-disable-edr.html>

译文仅供参考，具体内容表达以及含义原文为准。

## 研究人员观察到 RansomHub 勒索软件团伙使用 TDSSKiller 工具禁用端点检测和响应 （EDR） 系统。

Malwarebytes ThreatDown 托管检测和响应 （MDR） 团队观察到，RansomHub 勒索软件团伙正在使用 TDSSKiller 工具禁用端点检测和响应 （EDR） 系统。

TDSSKiller 是网络安全公司卡巴斯基开发的用于删除 rootkit 的合法工具，该软件还可以通过命令行脚本或批处理文件禁用 EDR 解决方案。

专家们注意到，勒索软件组织还使用 **LaZagne** 工具来收集凭据。在 MDR 调查的案件中，专家观察到 LaZagne 生成了 60 次文件写入，可能记录了提取的凭据，并执行了 1 次文件删除，可能隐藏了凭据收集活动的痕迹。

*“尽管 TDSSKiller 和 LaZagne 都已被攻击者使用多年，但这是 RansomHub 在其运营中使用它们的首次记录，其中 TTP 未列在 CISA 最近发布的 RansomHub 公告中。”“这些工具是在初始侦察和网络探测之后通过管理员组枚举（例如 `net1 组 'Enterprise Admins' /do）部署的。”`*

RansomHub 使用带有 -dcsvc 标志的 TDSSKiller 尝试禁用关键安全服务，特别是针对 Malwarebytes 反恶意软件服务 （MBAMService）。该命令旨在通过禁用此服务来破坏安全防御。

**命令行**：其中 -dcsvc 标志用于定位特定服务。在这种情况下，攻击者尝试禁用 **MBAMService**。`tdsskiller.exe -dcsvc MBAMService`

![TDSSKiller]()

RansomHub 是一种勒索软件即服务 （RaaS），用于多个威胁行为者的操作。Microsoft 报告称，在 Mustard Tempest 通过 FakeUpdates/Socgholish 感染进行初始访问后，观察到被跟踪为 Manatee Tempest 的威胁行为者在入侵后活动中部署 RansomHub。

专家认为 RansomHub 是 Knight 勒索软件的更名。Knight，也被称为 Cyclops 2.0，于 2023 年 5 月出现在威胁态势中。该恶意软件针对多个平台，包括 Windows、Linux、macOS、ESXi 和 Android。运营商在其 RaaS 运营中使用了双重勒索模型。

这不是安全专家第一次记录卡巴斯基开发的工具的使用情况。

深信服 Cyber Guardian 事件响应团队报告称，LockBit 勒索软件团伙使用 TDSSKiller 的 -dcsvc 参数作为其攻击链的一部分。

攻击者使用合法工具，因为安全解决方案不会阻止它们。

Malwarebytes 分享了这些攻击的入侵指标 （IoC），并建议：

* 通过网络分段隔离关键系统，以限制横向移动。
* 通过实施控制措施来监控和限制易受攻击的驱动程序（如 TDSSKiller），尤其是在使用可疑命令行标志（如 .隔离或阻止已知的滥用模式，同时允许合法使用可以防止 BYOVD 攻击。

本文翻译自securityaffairs [原文链接](https://securityaffairs.com/168296/malware/ransomhub-ransomware-tdskiller-disable-edr.html)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/300028](/post/id/300028)

安全KER - 有思想的安全新媒体

本文转载自: [securityaffairs](https://securityaffairs.com/168296/malware/ransomhub-ransomware-tdskiller-disable-edr.html)

如若转载,请注明出处： <https://securityaffairs.com/168296/malware/ransomhub-ransomware-tdskiller-disable-edr.html>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [网络攻击](/tag/%E7%BD%91%E7%BB%9C%E6%94%BB%E5%87%BB)
* [安全热点](/tag/%E5%AE%89%E5%85%A8%E7%83%AD%E7%82%B9)

**+1**0赞

收藏

![](https://p1.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p1.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p1.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=170338)

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

* ##### [Morte僵尸网络被披露：正利用路由器与企业应用漏洞，迅速扩张其“加载器即服务”活动](/post/id/312444)

  2025-09-29 18:04:01
* ##### [Akira勒索软件利用SonicWall VPN账户发起急速入侵](/post/id/312438)

  2025-09-29 18:03:28
* ##### [DarkCloud信息窃取器现新变种：采用VB6混淆技术并新增加密货币钱包窃取功能，威胁显著升级](/post/id/312435)

  2025-09-29 18:02:53
* ##### [TamperedChef恶意软件兴起：欺诈应用利用经过签名的二进制文件与搜索引擎投毒劫持浏览器](/post/id/312432)

  2025-09-29 18:02:25
* ##### [黑客将SVG文件武器化，用于隐秘投递恶意负载](/post/id/312351)

  2025-09-24 16:44:10
* ##### [ShadowV2僵尸网络利用配置错误的AWS Docker容器构建DDoS攻击租用服务](/post/id/312381)

  2025-09-24 16:40:43
* ##### [npm软件包“fezbox”中被发现新型恶意软件，可利用二维码窃取用户凭据](/post/id/312387)

  2025-09-24 16:40:06

### 热门推荐

文章目录

* [研究人员观察到 RansomHub 勒索软件团伙使用 TDSSKiller 工具禁用端点检测和响应 （EDR） 系统。](#h2-0)

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