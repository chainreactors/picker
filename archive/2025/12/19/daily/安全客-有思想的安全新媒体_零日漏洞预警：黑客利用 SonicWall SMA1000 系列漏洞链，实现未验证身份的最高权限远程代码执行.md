---
title: 零日漏洞预警：黑客利用 SonicWall SMA1000 系列漏洞链，实现未验证身份的最高权限远程代码执行
url: https://www.anquanke.com/post/id/313863
source: 安全客-有思想的安全新媒体
date: 2025-12-19
fetch_date: 2025-12-20T03:13:28.525898
---

# 零日漏洞预警：黑客利用 SonicWall SMA1000 系列漏洞链，实现未验证身份的最高权限远程代码执行

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

# 零日漏洞预警：黑客利用 SonicWall SMA1000 系列漏洞链，实现未验证身份的最高权限远程代码执行

阅读量**18298**

发布时间 : 2025-12-19 17:27:02

**x**

##### 译文声明

本文是翻译文章，文章原作者 Ddos，文章来源：securityonline

原文地址：<https://securityonline.info/zero-day-warning-hackers-chain-sonicwall-sma1000-flaws-for-unauthenticated-root-rce/>

译文仅供参考，具体内容表达以及含义原文为准。

![]()

飞塔（SonicWall）公司针对其高端远程访问设备发布紧急安全公告，并为其中一个漏洞发布了补丁。该漏洞本身危害程度看似一般，却是构成毁灭性攻击链的最后一环，黑客借助这条攻击链，可全面掌控企业网络。

这个编号为 CVE – 2025 – 40602 的漏洞，影响 SMA1000 系列安全接入网关。这类设备对管理远程办公人员的网络连接至关重要。该漏洞的通用漏洞评分系统（CVSS）评分为 6.6 分，但真正的危险在于黑客对它的利用方式。

从表面来看，该漏洞被定义为 “因飞塔 SMA1000 设备管理控制台权限校验机制存在缺陷，引发的本地权限提升漏洞”。通常情况下，这类漏洞意味着攻击者得先侵入系统内部，才能够实施破坏行为。

但飞塔公司的安全公告揭示了更严峻的情况，黑客正将该漏洞与此前披露的一个高危漏洞结合起来发起攻击，造成了极具破坏性的后果。

公告中警示：“重要提示：经报告，该漏洞会与 CVE – 2025 – 23006 漏洞（CVSS 评分为 9.8 分）协同利用，进而实现无需验证身份、获取最高权限的远程代码执行操作。”

通过将这两个漏洞串联成攻击链，攻击者先借助前者绕过身份验证环节，再利用新曝光的漏洞提升自身权限至最高级别。如此一来，即便没有有效的用户名和密码，黑客也能顺利夺取企业网络的 “核心控制权”。

该漏洞仅影响特定版本的 SMA1000 系列设备，具体为固件版本 12.4.3 – 03093 及更早版本、12.5.0 – 02002 及更早版本。

飞塔公司已督促用户立刻安装补丁修复漏洞，并发布了对应平台的热修复程序（版本号分别为 12.4.3 – 03245 和 12.5.0 – 02283）以填补安全漏洞。

对于暂时无法停机更新的机构，飞塔公司给出了严格的临时防护方案，即严控管理接口。管理员需 “关闭面向公网的 SSL 虚拟专用网络管理接口和安全外壳协议访问权限”，同时仅允许特定虚拟专用网络通道或内部 IP 地址访问设备。

本文翻译自securityonline [原文链接](https://securityonline.info/zero-day-warning-hackers-chain-sonicwall-sma1000-flaws-for-unauthenticated-root-rce/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/313863](/post/id/313863)

安全KER - 有思想的安全新媒体

本文转载自: [securityonline](https://securityonline.info/zero-day-warning-hackers-chain-sonicwall-sma1000-flaws-for-unauthenticated-root-rce/)

如若转载,请注明出处： <https://securityonline.info/zero-day-warning-hackers-chain-sonicwall-sma1000-flaws-for-unauthenticated-root-rce/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [安全资讯](/tag/%E5%AE%89%E5%85%A8%E8%B5%84%E8%AE%AF)
* [漏洞情报](/tag/%E6%BC%8F%E6%B4%9E%E6%83%85%E6%8A%A5)

**+1**0赞

收藏

![](https://p2.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p2.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p2.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=171771)

[安全客](/member.html?memberId=171771)

这个人太懒了，签名都懒得写一个

* 文章
* **830**

* 粉丝
* **6**

### TA的文章

* ##### [CVE-2025-37164（CVSS 评分 10.0）：未验证身份即可远程执行代码，HPE OneView 漏洞或致数据中心遭完全控制](/post/id/313860)

  2025-12-19 17:27:54
* ##### [零日漏洞预警：黑客利用 SonicWall SMA1000 系列漏洞链，实现未验证身份的最高权限远程代码执行](/post/id/313863)

  2025-12-19 17:27:02
* ##### [RTO challan 诈骗事件解析：虚假交通罚单 + 恶意 VPN 组合攻击的盗刷原理](/post/id/313869)

  2025-12-19 17:26:53
* ##### [百亿美元转向：OpenAI 洽谈亚马逊巨额融资 —— 但暗藏硅谷式附加条件](/post/id/313874)

  2025-12-19 17:25:55
* ##### [开发者的胜利：社区强烈反对后，GitHub 推迟自托管运行器收费计划](/post/id/313856)

  2025-12-19 17:25:31

### 相关文章

* ##### [CVE-2025-37164（CVSS 评分 10.0）：未验证身份即可远程执行代码，HPE OneView 漏洞或致数据中心遭完全控制](/post/id/313860)

  2025-12-19 17:27:54
* ##### [RTO challan 诈骗事件解析：虚假交通罚单 + 恶意 VPN 组合攻击的盗刷原理](/post/id/313869)

  2025-12-19 17:26:53
* ##### [百亿美元转向：OpenAI 洽谈亚马逊巨额融资 —— 但暗藏硅谷式附加条件](/post/id/313874)

  2025-12-19 17:25:55
* ##### [开发者的胜利：社区强烈反对后，GitHub 推迟自托管运行器收费计划](/post/id/313856)

  2025-12-19 17:25:31
* ##### [2025 年 Chrome 零日漏洞遭在野利用：全面深度分析](/post/id/313877)

  2025-12-19 17:23:30
* ##### [Kubernetes 安全预警：Headlamp 漏洞（CVE-2025-14269）致未授权用户可劫持 Helm 集群](/post/id/313879)

  2025-12-19 17:21:53
* ##### [启动初期攻击：华擎、华硕、微星主板存在 UEFI 漏洞，攻击者可通过 PCIe 绕过操作系统安全机制](/post/id/313882)

  2025-12-19 17:21:12

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