---
title: 黑客可以接管 Ecovacs 家用机器人来监视它们的主人
url: https://www.anquanke.com/post/id/299479
source: 安全客-有思想的安全新媒体
date: 2024-08-27
fetch_date: 2025-10-06T18:00:45.507052
---

# 黑客可以接管 Ecovacs 家用机器人来监视它们的主人

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

# 黑客可以接管 Ecovacs 家用机器人来监视它们的主人

阅读量**68360**

发布时间 : 2024-08-26 14:27:13

**x**

##### 译文声明

本文是翻译文章，文章原作者 Pierluigi Paganini，文章来源：securityaffairs

原文地址：<https://securityaffairs.com/167508/hacking/researchers-hacked-ecovacs-devices.html>

译文仅供参考，具体内容表达以及含义原文为准。

## 最近，研究人员警告说，Ecovacs 制造的真空吸尘器和割草机机器人可能会被黑客入侵以监视其所有者，该公司将对其进行修复。

在最近的 Def Con 黑客会议上，安全研究人员 Dennis Giese 和 Braelynn **解释说**，攻击者可以利用 Ecovacs 制造的真空和割草机机器人的缺陷来监视其所有者。

研究人员分析了以下设备：科沃斯 Deebot 900 系列、科沃斯 Deebot N8/T8、科沃斯 Deebot N9/T9、科沃斯 Deebot N10/T10、科沃斯 Deebot X1、科沃斯 Deebot T20、科沃斯 Deebot X2、科沃斯 Goat G1、科沃斯 Spybot Airbot Z1、科沃斯 Airbot AVA 和科沃斯 Airbot ANDY。

![]()

专家们发现了一系列漏洞，这些漏洞可能允许威胁行为者通过蓝牙接管设备的摄像头和麦克风。专家指出，机器人没有灯来指示它们的摄像头和麦克风已打开。

*“他们的安全真的、真的、真的、真的很糟糕，”吉斯**告诉** TechCrunch。*

研究人员在 Ecovacs 机器人中发现的问题之一允许 450 英尺内的任何人都可以通过蓝牙控制该设备。一旦攻击者获得了对设备的控制权，他们就可以通过其 Wi-Fi 连接远程访问机器人。然后，他们可以检索敏感数据，如 Wi-Fi 凭据、保存的房间地图，甚至访问摄像头和麦克风。

Giese 解释说，科沃斯割草机机器人的蓝牙一直处于激活状态，而扫地机器人在开机后仅启用 20 分钟，在自动重启期间每天启用一次，这使得它们更难被黑客入侵。虽然理论上某些型号在摄像头开启时每五分钟播放一次音频警报，但黑客可以轻松删除此文件，从而使其在不被发现的情况下进行操作。

这两位研究人员还发现了 Ecovacs 设备的其他几个问题。他们发现，即使在用户删除其帐户后，数据和身份验证令牌仍保留在 Ecovacs 的云服务器上，这可能允许未经授权访问机器人扫地机，并可以监视二手购买该设备的个人。此外，割草机机器人具有以明文形式存储在设备内的防盗 PIN，攻击者可以轻松获取和滥用它。此外，一旦 Ecovacs 机器人遭到入侵，它就有可能被用来入侵附近的其他 Ecovacs 机器人。

最初，科沃斯的一位发言人告诉 TechCrunch，该公司不会解决研究人员发现的漏洞。

几周后，供应商宣布将解决这些问题。

本文翻译自securityaffairs [原文链接](https://securityaffairs.com/167508/hacking/researchers-hacked-ecovacs-devices.html)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/299479](/post/id/299479)

安全KER - 有思想的安全新媒体

本文转载自: [securityaffairs](https://securityaffairs.com/167508/hacking/researchers-hacked-ecovacs-devices.html)

如若转载,请注明出处： <https://securityaffairs.com/167508/hacking/researchers-hacked-ecovacs-devices.html>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [网络攻击](/tag/%E7%BD%91%E7%BB%9C%E6%94%BB%E5%87%BB)
* [网络安全热点](/tag/%E7%BD%91%E7%BB%9C%E5%AE%89%E5%85%A8%E7%83%AD%E7%82%B9)

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

* [最近，研究人员警告说，Ecovacs 制造的真空吸尘器和割草机机器人可能会被黑客入侵以监视其所有者，该公司将对其进行修复。](#h2-0)

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