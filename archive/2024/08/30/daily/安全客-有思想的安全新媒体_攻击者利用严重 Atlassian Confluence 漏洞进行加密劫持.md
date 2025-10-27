---
title: 攻击者利用严重 Atlassian Confluence 漏洞进行加密劫持
url: https://www.anquanke.com/post/id/299606
source: 安全客-有思想的安全新媒体
date: 2024-08-30
fetch_date: 2025-10-06T18:01:19.728784
---

# 攻击者利用严重 Atlassian Confluence 漏洞进行加密劫持

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

# 攻击者利用严重 Atlassian Confluence 漏洞进行加密劫持

阅读量**62375**

发布时间 : 2024-08-29 15:57:02

**x**

##### 译文声明

本文是翻译文章，文章原作者 Elizabeth Montalbano，文章来源：DARKREADING

原文地址：<https://www.darkreading.com/threat-intelligence/attackers-exploit-critical-atlassian-confluence-flaw-for-cryptojacking>

译文仅供参考，具体内容表达以及含义原文为准。

威胁行为者继续利用 1 月份发现的关键远程代码执行 （RCE） Atlassian 错误，使用新的攻击媒介将目标云环境转变为加密挖掘网络。

Trend Micro 发现了两种独立的攻击，它们利用该漏洞（在 Confluence 数据中心和 Confluence 服务器中被跟踪为 CVE-2023-22527）进行非法加密劫持攻击，耗尽网络资源。该服务器用于 Atlassian Confluence 的企业级部署，Atlassian Confluence 是一个协作和文档平台，专为团队和组织创建、共享和协作处理内容而设计。

发现后，该漏洞在通用漏洞评分系统 （CVSS） 上获得了 10 分（满分 10 分），因此研究人员从一开始就知道它在 从勒索软件到网络间谍的攻击中具有很大的利用潜力。根据 Trend Micro 于 8 月 28 日发布的一篇博文，在发现该漏洞并随后由 Atlassian 修补八个月后，现在可以将加密劫持添加到该列表中。

“这些攻击涉及威胁行为者，这些威胁行为者采用的方法包括部署 shell 脚本和 XMRig 矿工、以 SSH 端点为目标、杀死竞争的加密挖掘进程以及通过 cron 作业保持持久性，”趋势科技威胁研究高级工程师 Abdelrahman Esmail 在帖子中写道。

在过去几个月中，Trend Micro 还发现了数千次利用最高关键 CVE-2023-22527 的其他尝试，因此建议那些使用服务器但尚未修补其环境的人应尽快进行修补。

## CVE-2023-22527 的新攻击媒介

通过滥用 CVE-2023-22527，未经身份验证的攻击者可以实现模板注入，实质上是在受影响的实例上启用 RCE。

Trend Micro 发现了三个威胁行为者利用该漏洞进行加密劫持攻击。但是，博文中仅描述了两种不同的攻击媒介。第一个应用程序利用了面向公众的 Confluence Server 应用程序中的漏洞，对环境进行了初始访问。然后，攻击者通过 ELF 文件有效负载执行 XMRig 矿工，在此过程中劫持系统资源。

第二个攻击向量要复杂得多。据 Trend Micro 称，它使用 shell 脚本通过安全 Shell （SSH） 上的 shell 文件为客户环境中所有可访问的端点执行矿工活动。攻击者下载了 shell 文件并从内存中使用 bash 运行它，然后杀死了所有已知的加密挖矿进程和从 \*/tmp/\* 目录运行的任何进程。然后，他们删除了所有 cron 作业，添加了一个每 5 分钟运行一次的新作业，以检查命令和控制 （C2） 服务器通信。

为避免被发现，攻击者还卸载了阿里云盾等安全服务，同时阻止了阿里云盾 IP 地址。在加密劫持开始之前，攻击者还关闭了系统上存在的其他安全工具。

与此同时，Esmail 在帖子中解释说，攻击者确定了当前机器的 IP 地址并收集了所有可能的用户、IP 地址和密钥的数据，使用这些信息通过 SSH 瞄准其他远程系统以执行进一步的加密挖掘活动。完成此操作后，攻击者通过 SSH 对目标其他主机发起自动攻击，然后通过其他 cron 作业保持对服务器的访问。

“在确保终止或删除所有云监控和安全服务后，攻击者终止了利用 CVE-2023-22527 的入口点进程，并下载 XMRig 矿工以开始挖矿活动，”Esmail 写道。加密挖矿开始后，攻击者就会通过清除日志和 bash 历史记录来删除其活动的所有痕迹。

## 针对 Atlassian Confluence 攻击的进一步缓解措施

及时修补软件、操作系统和应用程序的错误是防止此类漏洞被利用的最有效方法，但 Trend Micro 还为云环境的管理员提出了其他建议。这些措施包括实施网络分段，这可以减少基于漏洞利用的攻击的影响，并且组织应定期进行安全审计和漏洞评估，以帮助在漏洞利用发生之前发现和解决基础设施中的弱点。除此之外，组织应制定可靠的事件响应计划，以确保在发生泄露时做出快速有效的反应。

本文翻译自DARKREADING [原文链接](https://www.darkreading.com/threat-intelligence/attackers-exploit-critical-atlassian-confluence-flaw-for-cryptojacking)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/299606](/post/id/299606)

安全KER - 有思想的安全新媒体

本文转载自: [DARKREADING](https://www.darkreading.com/threat-intelligence/attackers-exploit-critical-atlassian-confluence-flaw-for-cryptojacking)

如若转载,请注明出处： <https://www.darkreading.com/threat-intelligence/attackers-exploit-critical-atlassian-confluence-flaw-for-cryptojacking>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [网络攻击](/tag/%E7%BD%91%E7%BB%9C%E6%94%BB%E5%87%BB)
* [安全热点](/tag/%E5%AE%89%E5%85%A8%E7%83%AD%E7%82%B9)

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

* [CVE-2023-22527 的新攻击媒介](#h2-0)
* [针对 Atlassian Confluence 攻击的进一步缓解措施](#h2-1)

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