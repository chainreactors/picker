---
title: 攻击者利用新的零日劫持Fortinet防火墙
url: https://www.anquanke.com/post/id/304215
source: 安全客-有思想的安全新媒体
date: 2025-02-13
fetch_date: 2025-10-06T20:34:09.804747
---

# 攻击者利用新的零日劫持Fortinet防火墙

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

# 攻击者利用新的零日劫持Fortinet防火墙

阅读量**72542**

发布时间 : 2025-02-12 15:21:54

**x**

##### 译文声明

本文是翻译文章，文章原作者 Pierluigi Paganini，文章来源：securityaffairs 2

原文地址：<https://securityaffairs.com/174117/hacking/fortinet-fortios-zero-day-exploited.html>

译文仅供参考，具体内容表达以及含义原文为准。

飞塔（Fortinet）公司发出警告，称存在利用现已修复的飞塔操作系统（FortiOS）和飞塔代理（FortiProxy）中的零日漏洞来劫持飞塔防火墙的攻击行为。

飞塔公司警告说，威胁行为者正在利用一个新的零日漏洞（编号为 CVE-2025-24472，通用漏洞评分系统（CVSS）评分为 8.1），在飞塔操作系统和飞塔代理中劫持飞塔防火墙。

该漏洞是一个身份验证绕过问题，远程攻击者可以通过构造恶意的 CSF 代理请求来获取超级管理员权限。

公告中写道：“存在一个‘使用替代路径或通道绕过身份验证’的漏洞（CWE-288），影响飞塔操作系统 7.0.0 至 7.0.16 版本以及飞塔代理 7.2.0 至 7.2.12 版本、7.0.0 至 7.0.19 版本，这可能会使远程攻击者通过精心构造的 CSF 代理请求获取超级管理员权限。”

该漏洞影响飞塔操作系统 7.0.0 至 7.0.16 版本、飞塔代理 7.0.0 至 7.0.19 版本以及飞塔代理 7.2.0 至 7.2.12 版本。飞塔公司已在飞塔操作系统 7.0.17 及更高版本以及飞塔代理 7.0.20/7.2.13 及更高版本中修复了此漏洞。

飞塔公司将这个漏洞添加到了一份与 2024 年 1 月披露的 CVE-2024-55591 漏洞相关的公告中。CVE-2024-55591 漏洞是一个 “使用替代路径或通道绕过身份验证” 的漏洞（CWE-288），影响飞塔操作系统 7.0.0 至 7.0.16 版本以及飞塔代理 7.0.0 至 7.0.19 版本和 7.2.0 至 7.2.12 版本。该漏洞可能使远程攻击者通过对 Node.js WebSocket 模块的精心构造请求来获取超级管理员权限。

公告中写道：“存在一个‘使用替代路径或通道绕过身份验证’的漏洞（CWE-288），影响飞塔操作系统和飞塔代理，这可能会使远程攻击者通过对 Node.js WebSocket 模块的精心构造请求或通过精心构造的 CSF 代理请求获取超级管理员权限。请注意，报告显示此漏洞正在被实际利用。”

威胁行为者利用这些漏洞创建恶意管理员或本地用户，修改防火墙策略，并访问 SSL 虚拟专用网络（VPN）以获取对内部网络的访问权限。

飞塔公司还为此问题提供了临时缓解措施，该公司建议禁用 HTTP/HTTPS 管理界面，或者通过本地入站策略限制能够访问该界面的 IP 地址。

北极狼（Arctic Wolf）公司的研究人员最近观察到了针对飞塔 FortiGate 防火墙的攻击行为，涉及未经授权的登录、账户创建和配置更改。

北极狼公司指出，当前的攻击活动可分为四个不同阶段：

1.漏洞扫描（2024 年 11 月 16 日至 2024 年 11 月 23 日）

2.侦察（2024 年 11 月 22 日至 2024 年 11 月 27 日）

3.SSL VPN 配置（2024 年 12 月 4 日至 2024 年 12 月 7 日）

4.横向移动（2024 年 12 月 16 日至 2024 年 12 月 27 日）

该公司推测，威胁行为者很可能利用了目标系统中的一个零日漏洞。

北极狼公司表示：“在 12 月初，北极狼实验室开始观察到一场涉及飞塔 FortiGate 防火墙设备上可疑活动的攻击活动。通过获取受影响防火墙的管理界面访问权限，威胁行为者能够更改防火墙配置。在被攻陷的环境中，观察到威胁行为者使用 DCSync 提取凭据。虽然此次攻击活动中使用的初始访问向量尚未确定，但北极狼实验室高度确信，鉴于受影响组织的时间线紧凑以及受影响的固件版本情况，很可能存在对零日漏洞的大规模利用。”

北极狼实验室于 2024 年 12 月 12 日向飞塔公司报告了此次攻击活动，飞塔卫士实验室（FortiGuard Labs）于 2024 年 12 月 17 日确认已知晓并展开调查。

本文翻译自securityaffairs 2 [原文链接](https://securityaffairs.com/174117/hacking/fortinet-fortios-zero-day-exploited.html)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/304215](/post/id/304215)

安全KER - 有思想的安全新媒体

本文转载自: [securityaffairs 2](https://securityaffairs.com/174117/hacking/fortinet-fortios-zero-day-exploited.html)

如若转载,请注明出处： <https://securityaffairs.com/174117/hacking/fortinet-fortios-zero-day-exploited.html>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [网络攻击](/tag/%E7%BD%91%E7%BB%9C%E6%94%BB%E5%87%BB)

**+1**3赞

收藏

![](https://p0.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p2.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p0.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=170061)

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