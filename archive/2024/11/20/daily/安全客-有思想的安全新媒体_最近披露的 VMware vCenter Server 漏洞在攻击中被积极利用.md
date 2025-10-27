---
title: 最近披露的 VMware vCenter Server 漏洞在攻击中被积极利用
url: https://www.anquanke.com/post/id/302000
source: 安全客-有思想的安全新媒体
date: 2024-11-20
fetch_date: 2025-10-06T19:15:06.347564
---

# 最近披露的 VMware vCenter Server 漏洞在攻击中被积极利用

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

# 最近披露的 VMware vCenter Server 漏洞在攻击中被积极利用

阅读量**55568**

发布时间 : 2024-11-19 14:57:31

**x**

##### 译文声明

本文是翻译文章，文章原作者 Pierluigi Paganini，文章来源：securityaffairs

原文地址：<https://securityaffairs.com/171147/security/vmware-vcenter-server-bugs-actively-exploited.html>

译文仅供参考，具体内容表达以及含义原文为准。

![]()

**Broadcom 警告称，威胁者正在积极利用追踪为 CVE-2024-38812 和 CVE-2024-38813 的两个 VMware vCenter Server 漏洞。**

Broadcom 警告称，CVE-2024-38812 和 CVE-2024-38813 这两个 VMware vCenter Server 漏洞正在被恶意利用。

“更新公告指出，博通公司确认，CVE-2024-38812和CVE-2024-38813漏洞已在野外被利用。”

vCenter Server 是 VMware 虚拟化和云计算软件套件的关键组件。它是 VMware 虚拟化数据中心的集中式综合管理平台。

9 月中旬，Broadcom 发布了安全更新，以解决 VMware vCenter Server 中一个可能导致远程代码执行的关键漏洞（CVE-2024-38812，CVSS 得分：9.8）。

该漏洞是一个堆溢出漏洞，存在于 DCERPC 协议的实现中。

该公告称：“拥有 vCenter Server 网络访问权限的恶意行为者可能会通过发送特制网络数据包触发该漏洞，从而导致远程代码执行。”

该公司还解决了 vCenter Server 中的一个权限升级漏洞，该漏洞被追踪为 CVE-2024-38813。

该公告称：“拥有 vCenter Server 网络访问权限的恶意行为者可通过发送特制网络数据包触发该漏洞，将权限升级到 root。”

TZL 团队的 zbl & srs 在 2024 Matrix Cup 比赛期间发现了这两个漏洞，并将漏洞报告给了 Broadcom。

该公司指出：“这些漏洞是内存管理和损坏问题，可用于攻击 VMware vCenter 服务，可能允许远程执行代码。”

虚拟化巨头通过发布以下版本解决了这些漏洞：

* vCenter Server 8.0 U3b 和 7.0 U3s
* VMware Cloud Foundation 5.x（已在 8.0 U3b 中作为异步补丁修复）
* VMware Cloud Foundation 4.x（作为异步修补程序在 7.0 U3s 中得到修复）

6 月份，VMware 解决了多个 vCenter Server 漏洞，远程攻击者可利用这些漏洞实现远程代码执行或权限升级。

两个堆溢出漏洞（分别跟踪为 CVE-2024-37079 和 CVE-2024-37080）影响 DCERPC 协议的实施。

本文翻译自securityaffairs [原文链接](https://securityaffairs.com/171147/security/vmware-vcenter-server-bugs-actively-exploited.html)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/302000](/post/id/302000)

安全KER - 有思想的安全新媒体

本文转载自: [securityaffairs](https://securityaffairs.com/171147/security/vmware-vcenter-server-bugs-actively-exploited.html)

如若转载,请注明出处： <https://securityaffairs.com/171147/security/vmware-vcenter-server-bugs-actively-exploited.html>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [漏洞](/tag/%E6%BC%8F%E6%B4%9E)
* [网络攻击](/tag/%E7%BD%91%E7%BB%9C%E6%94%BB%E5%87%BB)

**+1**0赞

收藏

![](https://p2.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p3.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p2.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=173683)

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