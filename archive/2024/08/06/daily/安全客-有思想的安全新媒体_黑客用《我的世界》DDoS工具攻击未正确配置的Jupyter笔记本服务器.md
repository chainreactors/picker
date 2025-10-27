---
title: 黑客用《我的世界》DDoS工具攻击未正确配置的Jupyter笔记本服务器
url: https://www.anquanke.com/post/id/298764
source: 安全客-有思想的安全新媒体
date: 2024-08-06
fetch_date: 2025-10-06T18:02:29.758126
---

# 黑客用《我的世界》DDoS工具攻击未正确配置的Jupyter笔记本服务器

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

# 黑客用《我的世界》DDoS工具攻击未正确配置的Jupyter笔记本服务器

阅读量**127951**

发布时间 : 2024-08-05 14:49:37

**x**

##### 译文声明

本文是翻译文章，文章原作者 Ravie Lakshmanan，文章来源：The Hacker News

原文地址：<https://thehackernews.com/2024/08/hackers-exploit-misconfigured-jupyter.html>

译文仅供参考，具体内容表达以及含义原文为准。

网络安全研究人员披露了一个针对配置错误的Jupyter笔记本的新分布式拒绝服务（DDoS）攻击活动。

这项被云安全公司Aqua命名为Panamorfi的活动，利用一个名为mineping的Java基础工具来发起TCP洪水DDoS攻击。Mineping是一个专为《我的世界》游戏服务器设计的DDoS包。

攻击链涉及利用互联网暴露的Jupyter笔记本实例运行wget命令，从一个名为Filebin的文件共享网站获取ZIP存档。

ZIP文件包含两个Java归档（JAR）文件，conn.jar和mineping.jar，其中前者用于与Discord频道建立连接并触发mineping.jar包的执行。

Aqua研究员阿萨夫·莫拉格表示，“这种攻击旨在通过发送大量TCP连接请求来消耗目标服务器的资源。”“结果会被写入Discord频道。”

这次攻击活动被归因于一个名叫yawixooo的威胁行为者，其GitHub账户中有一个公开仓库，包含一个《我的世界》服务器属性文件。

这并非首次有对手针对可访问互联网的Jupyter笔记本进行攻击。在2023年10月，一个被称为Qubitstrike的突尼斯威胁行为者被观察到入侵Jupyter笔记本，企图非法挖掘加密货币并破坏云环境。

本文翻译自The Hacker News [原文链接](https://thehackernews.com/2024/08/hackers-exploit-misconfigured-jupyter.html)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/298764](/post/id/298764)

安全KER - 有思想的安全新媒体

本文转载自: [The Hacker News](https://thehackernews.com/2024/08/hackers-exploit-misconfigured-jupyter.html)

如若转载,请注明出处： <https://thehackernews.com/2024/08/hackers-exploit-misconfigured-jupyter.html>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [网络攻击](/tag/%E7%BD%91%E7%BB%9C%E6%94%BB%E5%87%BB)
* [DDOS](/tag/DDOS)

**+1**0赞

收藏

![](https://p1.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p0.ssl.qhimg.com/t014757b72460d855bf.png)

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