---
title: 黑客利用未修补的 AVTECH IP 摄像机漏洞进行僵尸网络攻击
url: https://www.anquanke.com/post/id/299648
source: 安全客-有思想的安全新媒体
date: 2024-08-31
fetch_date: 2025-10-06T17:59:23.050091
---

# 黑客利用未修补的 AVTECH IP 摄像机漏洞进行僵尸网络攻击

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

# 黑客利用未修补的 AVTECH IP 摄像机漏洞进行僵尸网络攻击

阅读量**115497**

|评论**1**

发布时间 : 2024-08-30 14:48:37

**x**

##### 译文声明

本文是翻译文章，文章原作者 Ravie Lakshmanan，文章来源：The Hacker News

原文地址：<https://thehackernews.com/2024/08/unpatched-avtech-ip-camera-flaw.html>

译文仅供参考，具体内容表达以及含义原文为准。

影响 AVTECH IP 摄像机的多年前高度严重性漏洞已被恶意行为者用作零日漏洞，以将其引入僵尸网络。

CVE-2024-7029（CVSS 评分：8.7）是“在 AVTECH 闭路电视 （CCTV） 摄像机的亮度功能中发现的命令注入漏洞，允许远程代码执行 （RCE），”Akamai 研究人员 Kyle Lefton、Larry Cashdollar 和 Aline Eliovich 表示。

美国网络安全和基础设施安全局 （CISA） 于本月早些时候首次公开了安全漏洞的详细信息，强调了其低攻击复杂性和远程利用它的能力。

“成功利用此漏洞可能允许攻击者以正在运行的进程的所有者身份注入和执行命令，”该机构在 2024 年 8 月 1 日发布的警报中指出。

值得注意的是，该问题仍未修补。它会影响固件版本最高为 FullImg-1023-1007-1011-1009 的 AVM1203 台摄像机设备。根据 CISA 的说法，这些设备虽然已停产，但仍用于商业设施、金融服务、医疗保健和公共卫生、交通系统部门。

Akamai 表示，该攻击活动自 2024 年 3 月以来一直在进行，尽管该漏洞早在 2019 年 2 月就已被公开的概念验证 （PoC） 利用。但是，直到本月才发布 CVE 标识符。

“运营这些僵尸网络的恶意行为者一直在利用新的或不为人知的漏洞来扩散恶意软件，”这家网络基础设施公司表示。“存在许多公共漏洞利用或可用 PoC 的漏洞，这些漏洞缺乏正式的 CVE 分配，在某些情况下，设备仍未修补。”

攻击链相当简单，因为它们利用 AVTECH IP 摄像头漏洞以及其他已知漏洞（CVE-2014-8361 和 CVE-2017-17215）在目标系统上传播 Mirai 僵尸网络变体。

“在这种情况下，僵尸网络可能使用的是 Corona Mirai 变体，早在 2020 年，其他供应商就已将其与 COVID-19 病毒联系起来，”研究人员说。“执行后，恶意软件通过端口 23、2323 和 37215 上的 Telnet 连接到大量主机。它还会将字符串 ‘Corona’ 打印到受感染主机上的控制台。

几周前，网络安全公司 Sekoia 和 Team Cymru 详细介绍了一个名为 7777（或 Quad7）的“神秘”僵尸网络，该僵尸网络利用受感染的 TP-Link 和华硕路由器对 Microsoft 365 帐户进行密码喷洒攻击。截至 2024 年 8 月 5 日，已识别出多达 12,783 个活跃的机器人。

“这种僵尸网络在开源中以在受感染设备上部署 SOCKS5 代理而闻名，以中继针对全球许多实体的 Microsoft 365 帐户的极慢的’暴力’攻击，”Sekoia 研究人员说，并指出大多数受感染的路由器位于保加利亚、俄罗斯、美国和乌克兰。

虽然该僵尸网络的名字来源于它在受感染设备上打开 TCP 端口 7777 的事实，但 Cymru 团队的后续调查揭示了可能的扩展，以包括第二组主要由华硕路由器组成并以开放端口 63256 为特征的机器人。

“Quad7 僵尸网络继续构成重大威胁，展示了弹性和适应性，即使其潜力目前尚不清楚或尚未发挥，”Cymru 团队说。“7777 和 63256 僵尸网络之间的联系，同时保持着一个独特的操作孤岛，进一步凸显了 Quad7 背后威胁运营商不断发展的策略。”

本文翻译自The Hacker News [原文链接](https://thehackernews.com/2024/08/unpatched-avtech-ip-camera-flaw.html)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/299648](/post/id/299648)

安全KER - 有思想的安全新媒体

本文转载自: [The Hacker News](https://thehackernews.com/2024/08/unpatched-avtech-ip-camera-flaw.html)

如若转载,请注明出处： <https://thehackernews.com/2024/08/unpatched-avtech-ip-camera-flaw.html>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [网络攻击](/tag/%E7%BD%91%E7%BB%9C%E6%94%BB%E5%87%BB)
* [网络安全热点](/tag/%E7%BD%91%E7%BB%9C%E5%AE%89%E5%85%A8%E7%83%AD%E7%82%B9)

**+1**0赞

收藏

![](https://p1.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p2.ssl.qhimg.com/t014757b72460d855bf.png)

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