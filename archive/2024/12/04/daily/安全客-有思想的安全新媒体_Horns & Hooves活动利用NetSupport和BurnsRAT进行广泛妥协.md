---
title: Horns & Hooves活动利用NetSupport和BurnsRAT进行广泛妥协
url: https://www.anquanke.com/post/id/302381
source: 安全客-有思想的安全新媒体
date: 2024-12-04
fetch_date: 2025-10-06T19:37:23.732272
---

# Horns & Hooves活动利用NetSupport和BurnsRAT进行广泛妥协

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

# Horns & Hooves活动利用NetSupport和BurnsRAT进行广泛妥协

阅读量**59617**

发布时间 : 2024-12-03 14:31:35

**x**

##### 译文声明

本文是翻译文章，文章原作者 do son，文章来源：securityonline

原文地址：<https://securityonline.info/hornshooves-campaign-leverages-netsupport-and-burnsrat-for-widespread-compromise/>

译文仅供参考，具体内容表达以及含义原文为准。

![BurnsRAT]()

在卡巴斯基实验室的一份详细报告中，“Horns&Hooves ”活动利用双重 RAT 有效载荷–NetSupport RAT 和 BurnsRAT–入侵了各行各业的系统，成为网络犯罪分子独创性的一个显著实例。该活动以苏联讽刺小说《金牛》（The Golden Calf）中虚构的欺诈组织命名，自 2023 年 3 月启动以来，主要针对俄罗斯的个人、零售商和服务企业。

恶意电子邮件附件的形式是 ZIP 档案，其中包含伪装成商业文件的 JScript 文件，如 “LLC <公司>的建议和价格请求 ”或 “采购请求……”。这些附件通常包含诱饵文档–有时是非常规的 PNG 图像，这是一种用于嵌入和发送有效载荷而不引起怀疑的策略。

![]()
PNG 格式的诱饵文档 | 图片： 卡巴斯基实验室

卡巴斯基实验室指出：“PNG 图像是一种方便的容器，因为即使添加了有效载荷，它们也能继续正确显示。”

该活动的主要有效载荷是合法的远程管理工具 NetSupport Manager (NSM)（已改名为 NetSupport RAT）和一个名为 BurnsRAT 的自定义变种。这些工具为攻击者提供了对被入侵系统的广泛控制，利用其固有的合法性逃避检测。

NetSupport RAT 因其多功能性而成为网络黑客的最爱，它是利用巧妙的感染链部署的。脚本下载 BAT 文件或 PowerShell 脚本，安装 NetSupport 组件（如 client32.exe），配置注册表项以实现持久性，并连接到命令控制服务器。报告指出：“当运行 NetSupport RAT 时，它会与攻击者的服务器建立连接。”

BurnsRAT是一种不太知名但同样危险的工具，在某些情况下与NetSupport RAT一起发布或代替NetSupport RAT发布。该变种利用 DLL 侧载技术劫持合法进程。其有效载荷包括用于远程桌面操作、数据窃取和勒索软件安装的实用程序。

“攻击者分发的 RMS 构建也被称为 BurnsRAT，”这突出表明它具有双重用途，既能促进远程访问，又能充当进一步攻击的发射台。

![Horns&Hooves campaign]()
B 版感染链 | 图片： 卡巴斯基实验室

Horns&Hooves 活动展示了其感染链的适应性，随着时间的推移观察到多个版本的脚本。早期的迭代依赖于 HTA 文件，而后来的版本则采用了带有嵌入式有效载荷的 JScript。

耐人寻味的是，Horns&Hooves 活动与 TA569（又称 Mustard Tempest）的相关活动有相似之处。卡巴斯基实验室发现，Horns&Hooves 中使用的配置文件与之前归因于 TA569 的配置文件几乎完全相同，这加深了人们对共享来源的怀疑。

报告还说：“数值匹配这一事实表明，攻击者使用相同的安全密钥访问 NetSupport 客户端。”

Horns&Hooves 体现了利用合法工具达到恶意目的这一日益增长的趋势。通过将恶意软件伪装成可信软件，攻击者使检测和响应工作复杂化。

网络安全团队必须采取多层防御措施，包括强大的电子邮件过滤、软件行为分析和定期补丁管理。了解 Horns&Hooves 等活动对于应对不断变化的威胁至关重要。

本文翻译自securityonline [原文链接](https://securityonline.info/hornshooves-campaign-leverages-netsupport-and-burnsrat-for-widespread-compromise/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/302381](/post/id/302381)

安全KER - 有思想的安全新媒体

本文转载自: [securityonline](https://securityonline.info/hornshooves-campaign-leverages-netsupport-and-burnsrat-for-widespread-compromise/)

如若转载,请注明出处： <https://securityonline.info/hornshooves-campaign-leverages-netsupport-and-burnsrat-for-widespread-compromise/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [网络攻击](/tag/%E7%BD%91%E7%BB%9C%E6%94%BB%E5%87%BB)
* [恶意活动](/tag/%E6%81%B6%E6%84%8F%E6%B4%BB%E5%8A%A8)

**+1**3赞

收藏

![](https://p3.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p0.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p3.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=173683)

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