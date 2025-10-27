---
title: 网络犯罪分子滥用Cloudflare隧道以逃避检测并传播恶意软件
url: https://www.anquanke.com/post/id/298775
source: 安全客-有思想的安全新媒体
date: 2024-08-06
fetch_date: 2025-10-06T18:02:33.540668
---

# 网络犯罪分子滥用Cloudflare隧道以逃避检测并传播恶意软件

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

# 网络犯罪分子滥用Cloudflare隧道以逃避检测并传播恶意软件

阅读量**136074**

发布时间 : 2024-08-05 14:47:33

**x**

##### 译文声明

本文是翻译文章，文章原作者 Ravie Lakshmanan，文章来源：The Hacker News

原文地址：<https://thehackernews.com/2024/08/cybercriminals-abusing-cloudflare.html>

译文仅供参考，具体内容表达以及含义原文为准。

网络安全公司警告说，滥用 Clouflare 的 TryCloudflare 免费服务进行恶意软件传播的情况有所增加。

eSentire 和 Proofpoint 都记录了该活动，需要使用 TryCloudflare 创建一个速率限制隧道，该隧道充当管道，通过 Cloudflare 的基础设施将流量从攻击者控制的服务器中继到本地机器。

已经观察到利用此技术的攻击链提供了一系列恶意软件家族，例如 AsyncRAT、GuLoader、PureLogs Stealer、Remcos RAT、Venom RAT 和 XWorm。

初始访问向量是包含ZIP存档的网络钓鱼电子邮件，其中包括一个URL快捷方式文件，该快捷方式文件将邮件收件人引导至托管在TryCloudflare代理的WebDAV服务器上的Windows快捷方式文件。反过来，快捷方式文件执行下一阶段的批处理脚本，负责检索和执行额外的 Python 有效负载，同时显示托管在同一 WebDAV 服务器上的诱饵 PDF 文档以保持诡计。

“这些脚本执行了诸如启动诱饵 PDF、下载其他恶意负载以及更改文件属性以避免检测等操作，”eSentire 指出。

“他们策略的一个关键要素是使用直接系统调用来绕过安全监控工具，解密shellcode层，并部署Early Bird APC队列注入来秘密执行代码并有效地逃避检测。”根据 Proofpoint 的说法，网络钓鱼诱饵是用英语、法语、西班牙语和德语编写的，电子邮件数量从数百到数万封不等，针对来自世界各地的组织。这些主题涵盖了广泛的主题，例如发票、文件请求、包裹递送和税收。

该活动虽然归因于一组相关活动，但并未与特定的威胁行为者或组织相关联，但电子邮件安全供应商评估其出于经济动机。

利用 TryCloudflare 进行恶意目的的行为是在去年首次记录的，当时 Sysdig 发现了一个名为 LABRAT 的加密劫持和代理劫持活动，该活动将 GitLab 中现已修补的关键漏洞武器化，以渗透目标并使用 Cloudflare 隧道掩盖其命令和控制 （C2） 服务器。

此外，使用 WebDAV 和服务器消息块 （SMB） 进行有效负载暂存和交付需要企业将对外部文件共享服务的访问限制为仅允许列出的已知服务器。

Proofpoint 研究人员 Joe Wise 和 Selena Larson 表示：“使用 Cloudflare 隧道为威胁行为者提供了一种使用临时基础设施来扩展其运营的方法，从而提供了及时构建和关闭实例的灵活性。“这使得防御者和传统的安全措施（例如依赖静态阻止列表）变得更加困难。临时 Cloudflare 实例允许攻击者以一种低成本的方法使用辅助脚本进行攻击，同时限制了检测和删除工作的风险。

Spamhaus 项目呼吁 Cloudflare 审查其反滥用政策，因为网络犯罪分子利用其服务来掩盖恶意行为并通过所谓的“依赖信任的服务”（LoTS） 来增强其运营安全性。

该公司表示，它“经常观察到不法分子将他们的域名（已列入[域名阻止列表]）转移到Cloudflare，以掩饰其运营的后端，无论是垃圾邮件域名，网络钓鱼还是更糟的域名。

本文翻译自The Hacker News [原文链接](https://thehackernews.com/2024/08/cybercriminals-abusing-cloudflare.html)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/298775](/post/id/298775)

安全KER - 有思想的安全新媒体

本文转载自: [The Hacker News](https://thehackernews.com/2024/08/cybercriminals-abusing-cloudflare.html)

如若转载,请注明出处： <https://thehackernews.com/2024/08/cybercriminals-abusing-cloudflare.html>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [恶意软件](/tag/%E6%81%B6%E6%84%8F%E8%BD%AF%E4%BB%B6)
* [网络攻击](/tag/%E7%BD%91%E7%BB%9C%E6%94%BB%E5%87%BB)

**+1**0赞

收藏

![](https://p0.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p2.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p0.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=170338)

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