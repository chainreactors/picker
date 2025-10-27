---
title: 勒索软件Eldorado正在入侵 VMware ESXi 环境
url: https://www.anquanke.com/post/id/297769
source: 安全客-有思想的安全新媒体
date: 2024-07-11
fetch_date: 2025-10-06T17:38:34.293875
---

# 勒索软件Eldorado正在入侵 VMware ESXi 环境

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

# 勒索软件Eldorado正在入侵 VMware ESXi 环境

阅读量**192320**

发布时间 : 2024-07-10 19:32:58

**x**

##### 译文声明

本文是翻译文章，文章原作者 Nathan Eddy，文章来源：DARKREADING

原文地址：<https://www.darkreading.com/endpoint-security/eldorado-ransomware-target-vmware-esxi>

译文仅供参考，具体内容表达以及含义原文为准。

![1971 年凯迪拉克 Eldorado 的引擎盖装饰]()

自 3 月份以来，基于 Go 的勒索软件即服务 (RaaS) Eldorado 一直针对 Windows 和 VMware ESXi 环境（主要在美国的教育、房地产和医疗保健领域）。

根据成功渗透到该行动中的 Group-IB 的报告，该勒索软件首先出现在 RAMP 论坛上，分发适用于 Windows 和 Linux 的版本并宣传其联盟计划，希望吸引熟练的合作伙伴加入该组织。

报告指出，Eldorado 允许附属机构定制其攻击，例如指定要加密的目录，以及针对 Windows 上的网络共享，而 Linux 定制仅限于设置要加密的目录。

他们补充说，开发人员正在利用 Go 程序将代码交叉编译为本机的、自包含的二进制文件的能力。

Group-IB 研究人员写道： “勒索软件使用 Golang 实现跨平台功能，使用 Chacha20 进行文件加密，使用 Rivest Shamir Adleman-Optimal 非对称加密填充 (RSA-OAEP) 进行密钥加密。它可以使用服务器消息块 (SMB) 协议加密共享网络上的文件。”

该勒索软件还会删除卷影副本以防止恢复，避开关键系统文件以维持系统功能，并设置为自我删除以逃避检测。

## 埃尔多拉多强化“靠土地谋生”战略

Sectigo 产品高级副总裁 Jason Soroko 表示，Eldorado 通过“因地制宜”的策略增强了其逃避能力，这意味着它利用了受感染系统上已有的原生合法工具。

“Windows WMI 和 PowerShell 就是例子，”他解释道。“这些工具可用于横向移动或加密资源。”

他补充说，可以在 Windows 中配置 Eldorado，以不影响某些对正常运行至关重要的文件，例如 DLL。

“该恶意软件的 Windows 变种似乎具有高度可配置性，这就是为什么我们会看到同一种恶意软件的攻击方法存在不同的变化，”Soroko 说。

他说，目前看来，攻击背后的动机是金钱，拒绝服务攻击并不是主要动机。但 Critical Start 网络威胁研究高级经理 Callie Guenther 表示，Eldorado 在加密文件之前关闭并加密虚拟机 (VM) 的能力可能会严重影响业务连续性和数据可用性。

她补充道：“对 VMware ESXi 的关注凸显了不断演变的威胁形势，攻击者越来越多地瞄准虚拟化环境来最大化造成损害。”

## 野心勃勃的威胁行为者及其路线图

Menlo Security 的网络安全专家 Ngoc Bui 表示，感染多个操作系统的能力始终值得注意，因为它扩大了攻击范围。

“然而，值得注意的是加密方法的结合以及从头开始创建勒索软件，”他解释道。“这向我发出信号，他们队伍中可能存在经验丰富的勒索软件编码员。”

他补充说，这些人很可能是有代价的，这表明该团伙背后可能也有良好的资源。

Bui 表示：“接下来的几个月值得关注，看看他们的能力、他们实际上会做什么以及他们能吸引多少分支机构。”

他建议各组织确保其威胁情报分析师正在监视该团伙，并与其他业务部门共享可操作的情报，以防止可能发生的感染。

对于主动防御，“确保您的系统已修补，使用更强大的身份验证形式，并继续监视此恶意软件的迹象，”Soroko 建议道。

本文翻译自DARKREADING [原文链接](https://www.darkreading.com/endpoint-security/eldorado-ransomware-target-vmware-esxi)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/297769](/post/id/297769)

安全KER - 有思想的安全新媒体

本文转载自: [DARKREADING](https://www.darkreading.com/endpoint-security/eldorado-ransomware-target-vmware-esxi)

如若转载,请注明出处： <https://www.darkreading.com/endpoint-security/eldorado-ransomware-target-vmware-esxi>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [网络攻击](/tag/%E7%BD%91%E7%BB%9C%E6%94%BB%E5%87%BB)
* [每日安全热点](/tag/%E6%AF%8F%E6%97%A5%E5%AE%89%E5%85%A8%E7%83%AD%E7%82%B9)
* [安全头条](/tag/%E5%AE%89%E5%85%A8%E5%A4%B4%E6%9D%A1)

**+1**3赞

收藏

![](https://p4.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p2.ssl.qhimg.com/t014757b72460d855bf.png)

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

* [埃尔多拉多强化“靠土地谋生”战略](#h2-0)
* [野心勃勃的威胁行为者及其路线图](#h2-1)

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