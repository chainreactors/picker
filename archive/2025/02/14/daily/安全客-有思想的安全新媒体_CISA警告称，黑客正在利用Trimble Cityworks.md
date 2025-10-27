---
title: CISA警告称，黑客正在利用Trimble Cityworks
url: https://www.anquanke.com/post/id/304314
source: 安全客-有思想的安全新媒体
date: 2025-02-14
fetch_date: 2025-10-06T20:33:15.097174
---

# CISA警告称，黑客正在利用Trimble Cityworks

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

# CISA警告称，黑客正在利用Trimble Cityworks

阅读量**254765**

发布时间 : 2025-02-13 16:18:02

**x**

##### 译文声明

本文是翻译文章，文章原作者 Prajeet Nair，文章来源：govinfosecurity

原文地址：<https://www.govinfosecurity.com/hackers-are-exploiting-trimble-cityworks-cisa-warns-a-27485>

译文仅供参考，具体内容表达以及含义原文为准。

![Hackers Are Exploiting Trimble Cityworks, CISA Warns]()

美国网络安全与基础设施安全局（CISA）担心，对 Cityworks 平台漏洞的利用可能会扰乱各类地方政府服务。（图片来源： shutterstock 图库）

黑客正在利用一个被政府机构广泛使用的基础设施管理系统中的严重漏洞，该漏洞可使攻击者在微软 IIS Web 服务器上执行远程代码。

美国网络安全与基础设施安全局（CISA）命令联邦民用机构在 2 月 28 日前修复天宝（Trimble）公司的 Cityworks 平台中被追踪为 CVE-2025-0994 的严重漏洞。

根据天宝公司的网站介绍，Cityworks 服务器资产管理系统是 “一个以地理信息系统（GIS）为核心的解决方案，供地方政府、公用事业公司、机场和公共工程部门在整个生命周期内管理和维护基础设施”。黑客正在利用这一漏洞，引发了人们对关键服务可能受到干扰的担忧。

总部位于科罗拉多州的天宝公司披露了这一漏洞，并警告用户存在远程代码执行攻击的风险。该漏洞源于一个反序列化漏洞，这使得威胁行为者能够未经授权访问系统并部署恶意负载。

美国网络安全与基础设施安全局将该漏洞列入了其已知被利用漏洞目录，敦促管理员立即安装安全更新，并检查系统是否存在被入侵的迹象。

天宝公司的调查证实，存在未经授权试图入侵特定 Cityworks 部署系统的行为。一些本地安装的系统存在 IIS 身份权限过高以及附件目录配置错误的问题。

此次安全公告突出了多个入侵指标（IOC），包括恶意文件的 SHA256 哈希值、暂存 IP 地址以及 Cobalt Strike（一款渗透测试工具）的命令与控制域名。

攻击者正在使用经过混淆处理的 JavaScript 有效负载和基于 Rust 语言的恶意软件加载器，以便在被攻陷的服务器上保持持久控制。

建议使用 Cityworks 系统的联邦机构和地方政府采取以下措施：

1.分别为 15.x（15.8.9 版本）和 23.x（23.10 版本）应用最新补丁，这两个版本的补丁分别于 1 月 28 日和 29 日发布。

2.检查 IIS 身份权限，确保其不具备域或本地管理员权限。

3.限制附件目录的访问权限，以防止未经授权的修改。

本文翻译自govinfosecurity [原文链接](https://www.govinfosecurity.com/hackers-are-exploiting-trimble-cityworks-cisa-warns-a-27485)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/304314](/post/id/304314)

安全KER - 有思想的安全新媒体

本文转载自: [govinfosecurity](https://www.govinfosecurity.com/hackers-are-exploiting-trimble-cityworks-cisa-warns-a-27485)

如若转载,请注明出处： <https://www.govinfosecurity.com/hackers-are-exploiting-trimble-cityworks-cisa-warns-a-27485>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [网络攻击](/tag/%E7%BD%91%E7%BB%9C%E6%94%BB%E5%87%BB)

**+1**4赞

收藏

![](https://p4.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p4.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p4.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=170061)

[安全客](/member.html?memberId=170061)

这个人太懒了，签名都懒得写一个

* 文章
* **2096**

* 粉丝
* **6**

### TA的文章

* ##### [英国通过数据访问和使用监管法案](/post/id/308719)

  2025-06-20 17:11:10
* ##### [CISA警告：严重缺陷（CVE-2025-5310）暴露加油站设备](/post/id/308715)

  2025-06-20 17:09:03
* ##### [大多数公司高估了AI治理，因为隐私风险激增](/post/id/308708)

  2025-06-20 17:05:02
* ##### [研究人员发现了有史以来最大的数据泄露事件，暴露了160亿个登录凭证](/post/id/308704)

  2025-06-20 17:02:15
* ##### [CVE-2025-6018和CVE-2025-6019漏洞利用：链接本地特权升级缺陷让攻击者获得大多数Linux发行版的根访问权限](/post/id/308701)

  2025-06-20 16:59:36

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