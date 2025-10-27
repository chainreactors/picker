---
title: 新型 Linux 恶意软件 ”sedexp” 利用 udev 规则隐藏信用卡盗刷器
url: https://www.anquanke.com/post/id/299475
source: 安全客-有思想的安全新媒体
date: 2024-08-27
fetch_date: 2025-10-06T18:00:44.623624
---

# 新型 Linux 恶意软件 ”sedexp” 利用 udev 规则隐藏信用卡盗刷器

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

# 新型 Linux 恶意软件 ”sedexp” 利用 udev 规则隐藏信用卡盗刷器

阅读量**60738**

发布时间 : 2024-08-26 14:27:25

**x**

##### 译文声明

本文是翻译文章，文章原作者 Ravie Lakshmanan，文章来源：The Hacker News

原文地址：<https://thehackernews.com/2024/08/new-linux-malware-sedexp-hides-credit.html>

译文仅供参考，具体内容表达以及含义原文为准。

网络安全研究人员发现了一种新的隐蔽 Linux 恶意软件，它利用一种非常规技术在受感染系统上实现持久性并隐藏信用卡盗取器代码。

该恶意软件归因于出于经济动机的威胁行为者，Aon 的 Stroz Friedberg 事件响应服务团队将其代号为 **sedexp**。

“这种高级威胁自 2022 年以来一直活跃，隐藏在众目睽睽之下，同时为攻击者提供反向外壳能力和高级隐藏策略，”研究人员 Zachary Reichert、Daniel Stein 和 Joshua Pivirotto 说。

恶意行为者不断即兴创作和改进他们的交易技巧，并转向新技术来逃避检测，这并不奇怪。

sedexp 值得注意的是它使用 udev 规则来保持持久性。Udev 是设备文件系统的替代品，它提供了一种机制，可以根据设备的属性识别设备，并配置规则以在设备状态发生变化时做出响应，即设备入或移除。

udev 规则文件中的每一行都至少有一次键值对，从而可以按名称匹配设备，并在检测到各种设备事件时触发某些操作（例如，在连接外部驱动器时触发自动备份）。

“匹配规则可以指定设备节点的名称，添加指向节点的符号链接，或者在事件处理过程中运行指定的程序，”SUSE Linux 在其文档中指出。“如果未找到匹配的规则，则使用默认设备节点名称创建设备节点。”

sedexp 的 udev 规则 — ACTION==“add”， ENV{MAJOR}==“1”， ENV{MINOR}==“8”， RUN+=“asedexpb run：+” — 设置为每当加载 /dev/random（对应于设备次要编号 8）时运行恶意软件，这通常在每次重新启动时发生。

换句话说，RUN 参数中指定的程序在每次系统重启后执行。

该恶意软件具有启动反向 shell 以促进远程访问受感染主机的功能，以及修改内存以从 ls 或 find 等命令中隐藏任何包含字符串“sedexp”的文件。

Stroz Friedberg 表示，在它调查的实例中，该功能已被用于隐藏 Web shell、更改的 Apache 配置文件和 udev 规则本身。

“该恶意软件被用来在 Web 服务器上隐藏信用卡抓取代码，表明专注于经济利益，”研究人员说。“sedexp 的发现表明，除了勒索软件之外，出于经济动机的威胁行为者已经越来越复杂。”

本文翻译自The Hacker News [原文链接](https://thehackernews.com/2024/08/new-linux-malware-sedexp-hides-credit.html)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/299475](/post/id/299475)

安全KER - 有思想的安全新媒体

本文转载自: [The Hacker News](https://thehackernews.com/2024/08/new-linux-malware-sedexp-hides-credit.html)

如若转载,请注明出处： <https://thehackernews.com/2024/08/new-linux-malware-sedexp-hides-credit.html>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [网络攻击](/tag/%E7%BD%91%E7%BB%9C%E6%94%BB%E5%87%BB)
* [网络安全热点](/tag/%E7%BD%91%E7%BB%9C%E5%AE%89%E5%85%A8%E7%83%AD%E7%82%B9)

**+1**0赞

收藏

![](https://p4.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p5.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p4.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=170338)

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