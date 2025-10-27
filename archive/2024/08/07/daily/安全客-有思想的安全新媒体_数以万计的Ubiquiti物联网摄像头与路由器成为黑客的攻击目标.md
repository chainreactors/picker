---
title: 数以万计的Ubiquiti物联网摄像头与路由器成为黑客的攻击目标
url: https://www.anquanke.com/post/id/298820
source: 安全客-有思想的安全新媒体
date: 2024-08-07
fetch_date: 2025-10-06T18:02:14.296741
---

# 数以万计的Ubiquiti物联网摄像头与路由器成为黑客的攻击目标

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

# 数以万计的Ubiquiti物联网摄像头与路由器成为黑客的攻击目标

阅读量**82688**

发布时间 : 2024-08-06 11:34:41

**x**

##### 译文声明

本文是翻译文章，文章原作者 Nate Nelson，文章来源：DARKREADING

原文地址：<https://www.darkreading.com/ics-ot-security/20k-ubiquiti-iot-cameras-and-routers-are-sitting-ducks-for-hackers>

译文仅供参考，具体内容表达以及含义原文为准。

研究人员警告称，数以万计的小型办公室/家庭办公室（SOHO）设备，由Ubiquiti公司销售，对一个五年前的漏洞仍然敞开了大门，这些设备在网络上直接暴露于攻击之下。

2019年1月，宽带互联网专家吉姆·特鲁特曼（Jim Troutman）警告称，数十款Ubiquiti物联网（IoT）设备中一个公开的端口正在遭受拒绝服务（DoS）攻击的利用。这个基础性的漏洞，CVE-2017-0938，在CVSS评分系统中被赋予了“高危”的7.5分。

七个月后，Rapid7的研究人员仍能找到近50万台易受攻击的设备。而现在，尽管Ubiquiti早已承认并修复了这个问题，大约2万台设备依然处于脆弱状态，Check Point Research在其最新博客文章中指出。

“我们可以看到其中一些已经被入侵，”Check Point Software的漏洞研究团队负责人拉多斯瓦夫·马德耶（Radoslaw Madej）说，“而且，我所做的设备指纹识别相当基础，很可能还有更多设备（被入侵）。”

Check Point也警告说，除了可能被用于SOHO僵尸网络进行DoS攻击放大之外，被侵入的设备还可能泄露潜在敏感数据。

## 公开的摄像头和路由器可能泄露数据

在探查Ubiquiti设备如G4瞬时相机——一款具备双向音频功能的互联网连接摄像头时，Check Point实际上发现了一个除五年前所揭露的之外的额外暴露进程。

最初暴露的进程位于10001端口，是Ubiquiti发现协议，用于设备与其CloudKey+控制器之间的通信。新发现的特权暴露进程位于7004端口，同样用于设备间的通信。

使用伪造的数据包，Check Point的研究人员发现，无论是与CloudKey+还是其关联设备通信都不需要任何形式的身份验证。进一步地，他们接收到的响应消息包含了关于设备的具体信息，以及所有者的名字和位置。

“实际上，在某些情况下，有一个名字和姓氏，以及Ubiquiti路由器所在的位置，”马德耶回忆说，“所有这些信息……只需要我发送一个数据包就能收到回应。

“如果我想攻击这个实体，对我而言这很容易，因为我了解他们所使用的路由器类型、个人姓名、确切的软件版本和他们的商业地址。我可以找到他们的联系方式，然后打电话给他们说：‘嗨，我是你互联网提供商的人。我需要做一些维护工作。请给我管理员面板的访问权限。’因为我可以向这个人证明自己，提供他们所需的所有信息。”

## 物联网的问题

已打补丁的Ubiquiti产品对基于互联网的攻击有一项防御措施：它们不会响应来自更广泛网络的ping请求，只会响应来自内部IP地址的请求。

尽管这种简单的修复方法易于实现，但在野外仍有数以万计受影响的产品未打补丁。这似乎与Ubiquiti本身关系不大，而是物联网安全普遍存在的问题。

“我们习惯了修补我们的Windows电脑、MacBook、手机等等，但我们还没有真正习惯于应该同样关注我们的物联网设备，无论是Wi-Fi路由器、摄像头、吸尘器、冰箱还是洗衣机，”马德耶说。

“当然，”他补充道，“问题是：终端用户到底应该有多关心这件事。我们生活在一个所有设备都应该默认启用自动更新的时代。我认为这不应该是终端用户的担忧。”

本文翻译自DARKREADING [原文链接](https://www.darkreading.com/ics-ot-security/20k-ubiquiti-iot-cameras-and-routers-are-sitting-ducks-for-hackers)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/298820](/post/id/298820)

安全KER - 有思想的安全新媒体

本文转载自: [DARKREADING](https://www.darkreading.com/ics-ot-security/20k-ubiquiti-iot-cameras-and-routers-are-sitting-ducks-for-hackers)

如若转载,请注明出处： <https://www.darkreading.com/ics-ot-security/20k-ubiquiti-iot-cameras-and-routers-are-sitting-ducks-for-hackers>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [网络攻击](/tag/%E7%BD%91%E7%BB%9C%E6%94%BB%E5%87%BB)
* [网络安全热点](/tag/%E7%BD%91%E7%BB%9C%E5%AE%89%E5%85%A8%E7%83%AD%E7%82%B9)

**+1**0赞

收藏

![](https://p5.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p1.ssl.qhimg.com/t014757b72460d855bf.png)

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

* [公开的摄像头和路由器可能泄露数据](#h2-0)
* [物联网的问题](#h2-1)

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