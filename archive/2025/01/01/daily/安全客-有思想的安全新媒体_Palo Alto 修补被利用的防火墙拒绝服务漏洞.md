---
title: Palo Alto 修补被利用的防火墙拒绝服务漏洞
url: https://www.anquanke.com/post/id/303131
source: 安全客-有思想的安全新媒体
date: 2025-01-01
fetch_date: 2025-10-06T20:04:40.702407
---

# Palo Alto 修补被利用的防火墙拒绝服务漏洞

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

# Palo Alto 修补被利用的防火墙拒绝服务漏洞

阅读量**62093**

发布时间 : 2024-12-31 09:00:21

**x**

##### 译文声明

本文是翻译文章，文章原作者 Mathew J. Schwartz，文章来源：govinfosecurity

原文地址：<https://www.govinfosecurity.com/palo-alto-patches-exploited-firewall-denial-of-service-flaw-a-27163>

译文仅供参考，具体内容表达以及含义原文为准。

![Palo Alto Patches Exploited Firewall Denial-of-Service Flaw]()

防火墙巨头 Palo Alto Networks 正在推送更新，以修复一个被攻击者利用来破坏客户防火墙的漏洞。

该漏洞存在于运行该公司设备的 PAN-OS 软件中。该公司表示，其云原生 NGFW（即下一代防火墙）并没有受到影响。

“Palo Alto Networks PAN-OS 软件的 DNS 安全功能存在拒绝服务漏洞，未经验证的攻击者可以通过防火墙的数据平面发送恶意数据包，从而重启防火墙。反复尝试触发这种情况将导致防火墙进入维护模式。”

该漏洞被追踪为 CVE-2024-3393。

防火墙管理员报告说，从本周二开始，攻击就开始活跃起来。一位管理员在 Palo Alto Networks Firewall subreddit 上发帖称：“当防火墙阻止恶意 DNS 流量时，该漏洞就会被利用。这种功能由 Palo Alto 产品中的 “高级 DNS 安全 ”功能提供。”

Palo Alto 将该漏洞的严重性评为 “高”，修复的紧迫性为 “中等”。就防火墙而言，该漏洞的 CVSS 值为 8.7。该公司称，其 Prisma Access 安全服务边缘设备 “仅向经过验证的终端用户提供访问 ”时也存在该漏洞，CVSS 值为 7.1。

英国安全专家凯文-博蒙特（Kevin Beaumont）说，攻击者可以利用这个漏洞，不仅让脆弱的设备重启，而且让其崩溃。“如果你对一对 HA Palo Alto 盒子多次运行该漏洞，它们都会崩溃，而且不会重启。如果你不将 DNSSEC 显示到互联网上也没关系，”他在发给 Mastodon 的帖子中说。“修复就是物理重启两个盒子。所以，打补丁吧。”

一位 Palo Alto 防火墙管理员在 Reddit 上发帖说，在他们的防火墙于 12 月 24 日开始重启之前–事后看来，这显然是由于有人利用了这个漏洞–他们看到了一次意外的高可用性故障切换，但日志中除了 Palo Alto 基于 WildFire 云的恶意软件分析产品在自我更新之外，没有任何其他内容，而事实证明这并不是罪魁祸首。

这位管理员说：“圣诞节前夕，由于‘内存不足’，我们发生了一次随机的 HA 故障切换，当时我们肯定觉得很奇怪。我们查看了日志，除了一分钟前发生的 Wildfire 更新外，没有发现任何其他信息，我们怀疑这就是原因所在。教训。Palos 不会自己重启。有烟的地方就有火。”

Palo Alto 说，“必须启用 DNS 安全日志才能影响 PAN-OS 软件”，这是产品 “高级 DNS 安全 ”功能的一部分。

该公司称，该功能利用 “机器学习和众包智能 ”立即采取行动，阻止潜在的零日攻击和新出现的恶意软件。

就漏洞利用而言，公司是否注册了这种许可证似乎并不重要。“一位管理员周五在 Palo Alto Networks Firewall subreddit 上引用 Palo Alto 技术援助中心分享的信息时说：“显然，没有许可证并没有什么区别。你仍然容易受到攻击。因此，我们的建议是打补丁或应用变通方法。”

为了修复这个漏洞，该厂商已经部署了一系列针对 11.1.x、10.2.x 和 10.1.x 版本的 PAN-OS 更新。“PAN-OS 10.1.14-h8、PAN-OS 10.2.10-h12、PAN-OS 11.1.5、PAN-OS 11.2.3 以及所有后续 PAN-OS 版本都修复了这个问题，”它说。“注意：PAN-OS 11.0 已于 11 月 17 日到期，因此我们不打算为该版本提供修复。”

该公司还详细介绍了公司在能够打补丁之前可以采用的临时缓解措施。

Palo Alto表示，使用受影响的PAN-OS版本的DNS Security的Prisma Access客户应根据他们使用的是Panorama还是Strata Cloud Manager防火墙管理工具，采用这两种解决方法中的一种。这些临时解决办法分别涉及将 DNS 安全日志日志严重性设置为 “无”，或完全禁用 DNS 安全日志。在供应商发布修复程序后，用户需要记住重新启用这些功能。

该公司承诺在两周内发布 Prisma Access。该公司表示：“我们将在 1 月 3 日和 1 月 10 日的周末分两个阶段对受影响的客户进行升级。”

博蒙特说，Palo Alto的漏洞与最近在运行Fortinet设备的FortiOS软件中发现的一个完全不同的零日漏洞相似。对于Fortinet产品来说，该漏洞可被 “非管理数据包 ”利用，导致FortiOS内存耗尽并进入failopen状态，”他说，“这指的是当设备的入侵检测系统的原始socket进入内存不足模式时。”

博蒙特说，Palo Alto的漏洞看起来与最近在运行Fortinet设备的FortiOS软件中发现的一个完全不同的零日漏洞相似。对于Fortinet产品来说，该漏洞可被 “非管理数据包 ”利用，从而导致FortiOS内存不足并进入failopen状态，”他说。这指的是当入侵检测系统的原始套接字缓冲区满了，无法再检测数据包时，设备会进入内存不足模式。设备可以设置为 “失效打开 ”模式，允许更多数据包通过而不进行检查，或者设置为 “失效关闭 ”模式，阻止所有数据包，直到 IPS 检查重新上线。

Beaumont 说：“我只是想扩大一下范围–我知道一家电信公司正在使用这两个漏洞进行拒绝服务，一个电子犯罪团伙基本上使用了防火墙非管理零日，这是另一种升级。”

他说，与 Palo Alto 漏洞一样，FortiOS 漏洞也可以通过将仍然支持的设备更新到最新版本的操作系统来修复。

攻击边缘设备是犯罪集团和民族国家集团经常采用的一种策略（见：Palo Alto报告防火墙被利用未知漏洞）。

本文翻译自govinfosecurity [原文链接](https://www.govinfosecurity.com/palo-alto-patches-exploited-firewall-denial-of-service-flaw-a-27163)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/303131](/post/id/303131)

安全KER - 有思想的安全新媒体

本文转载自: [govinfosecurity](https://www.govinfosecurity.com/palo-alto-patches-exploited-firewall-denial-of-service-flaw-a-27163)

如若转载,请注明出处： <https://www.govinfosecurity.com/palo-alto-patches-exploited-firewall-denial-of-service-flaw-a-27163>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [漏洞](/tag/%E6%BC%8F%E6%B4%9E)
* [漏洞情报](/tag/%E6%BC%8F%E6%B4%9E%E6%83%85%E6%8A%A5)

**+1**4赞

收藏

![](https://p0.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p2.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p0.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=173683)

[安全客](/member.html?memberId=173683)

这个人太懒了，签名都懒得写一个

* 文章
* **553**

* 粉丝
* **2**

### TA的文章

* ##### [年度盘点：AI+安全双重赋能，360解锁企业浏览器新动力](/post/id/303791)

  2025-01-24 10:00:53
* ##### [IntelBroker 的数字足迹： OSINT 分析揭露网络犯罪分子的行动](/post/id/303788)

  2025-01-24 09:55:58
* ##### [7-Zip 修复了可绕过 Windows MoTW 安全警告的错误，立即修补](/post/id/303776)

  2025-01-24 09:49:56
* ##### [Microsoft 在 Edge Stable 中预览 Game Assist 游戏内浏览器](/post/id/303773)

  2025-01-24 09:43:16
* ##### [ModiLoader 恶意软件利用 CAB 标头批处理文件逃避检测](/post/id/303770)

  2025-01-24 09:36:10

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