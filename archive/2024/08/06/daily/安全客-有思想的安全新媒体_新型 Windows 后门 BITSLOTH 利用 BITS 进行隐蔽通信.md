---
title: 新型 Windows 后门 BITSLOTH 利用 BITS 进行隐蔽通信
url: https://www.anquanke.com/post/id/298772
source: 安全客-有思想的安全新媒体
date: 2024-08-06
fetch_date: 2025-10-06T18:02:32.758842
---

# 新型 Windows 后门 BITSLOTH 利用 BITS 进行隐蔽通信

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

# 新型 Windows 后门 BITSLOTH 利用 BITS 进行隐蔽通信

阅读量**70053**

发布时间 : 2024-08-05 14:47:59

**x**

##### 译文声明

本文是翻译文章，文章原作者 Ravie Lakshmanan，文章来源：The Hacker News

原文地址：<https://thehackernews.com/2024/08/new-windows-backdoor-bitsloth-exploits.html>

译文仅供参考，具体内容表达以及含义原文为准。

网络安全研究人员发现了一个以前未记录的 Windows 后门，该后门利用称为后台智能传输服务 （BITS） 的内置功能作为命令和控制 （C2） 机制。

Elastic Security Labs 将新发现的恶意软件菌株代号为 **BITSLOTH**，该实验室于 2024 年 6 月 25 日发现该恶意软件株，与针对南美国家政府未指明外交部的网络攻击有关。正在以名字对象 REF8747 跟踪活动集群。

“在本文发布时，后门的最新版本具有35个处理程序功能，包括键盘记录和屏幕捕获功能，”安全研究人员Seth Goodwin和Daniel Stepanic说。“此外，BITSLOTH 还包含许多不同的功能，用于发现、枚举和命令行执行。”

据评估，该工具自 2021 年 12 月以来一直在开发中，正被威胁行为者用于数据收集目的。目前尚不清楚谁是幕后黑手，尽管源代码分析发现了日志函数和字符串，表明作者可能是说中文的人。

与中国的另一个潜在联系来自一种名为RingQ的开源工具的使用。RingQ 用于加密恶意软件并防止安全软件检测到，然后直接在内存中解密并执行。

2024 年 6 月，AhnLab 安全情报中心 （ASEC） 透露，易受攻击的 Web 服务器正在被利用来放置 Web Shell，然后利用这些 Shell 来提供额外的有效载荷，包括通过 RingQ 的加密货币矿工。这些攻击被归咎于一名讲中文的威胁行为者。

这次攻击还值得注意的是，它使用 STOWAWAY 通过 HTTP 和一个名为 iox 的端口转发实用程序代理加密的 C2 流量，后者之前曾被一个名为 Bronze Starlight（又名 Emperor Dragonfly）的中国网络间谍组织利用，用于 Cheerscrypt 勒索软件攻击。

BITSLOTH 采用 DLL 文件（“flengine.dll”）的形式，通过使用与 Image-Line 关联的合法可执行文件（称为 FL Studio（fl.exe））通过 DLL 侧加载技术进行加载。

研究人员说：“在最新版本中，开发人员添加了一个新的调度组件，以控制BITSLOTH在受害者环境中运行的特定时间。“这是我们在其他现代恶意软件家族（如EAGERBEE）中观察到的特征。

作为一个功能齐全的后门，BITSLOTH能够运行和执行命令，上传和下载文件，执行枚举和发现，并通过键盘记录和屏幕捕获收集敏感数据。

它还可以将通信模式设置为HTTP或HTTPS，删除或重新配置持久性，终止任意进程，从计算机中注销用户，重新启动或关闭系统，甚至从主机中更新或删除自身。该恶意软件的一个定义方面是它使用 Bits 进行 C2。

研究人员补充说：“这种媒介对对手很有吸引力，因为许多组织仍在努力监控BITS网络流量并检测异常的BITS工作。

本文翻译自The Hacker News [原文链接](https://thehackernews.com/2024/08/new-windows-backdoor-bitsloth-exploits.html)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/298772](/post/id/298772)

安全KER - 有思想的安全新媒体

本文转载自: [The Hacker News](https://thehackernews.com/2024/08/new-windows-backdoor-bitsloth-exploits.html)

如若转载,请注明出处： <https://thehackernews.com/2024/08/new-windows-backdoor-bitsloth-exploits.html>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [网络攻击](/tag/%E7%BD%91%E7%BB%9C%E6%94%BB%E5%87%BB)
* [安全热点](/tag/%E5%AE%89%E5%85%A8%E7%83%AD%E7%82%B9)

**+1**3赞

收藏

![](https://p3.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p1.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p3.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=170338)

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