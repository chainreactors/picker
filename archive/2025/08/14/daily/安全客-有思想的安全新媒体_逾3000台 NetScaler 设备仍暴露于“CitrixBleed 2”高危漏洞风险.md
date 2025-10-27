---
title: 逾3000台 NetScaler 设备仍暴露于“CitrixBleed 2”高危漏洞风险
url: https://www.anquanke.com/post/id/311147
source: 安全客-有思想的安全新媒体
date: 2025-08-14
fetch_date: 2025-10-07T00:18:05.396777
---

# 逾3000台 NetScaler 设备仍暴露于“CitrixBleed 2”高危漏洞风险

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

# 逾3000台 NetScaler 设备仍暴露于“CitrixBleed 2”高危漏洞风险

阅读量**78994**

发布时间 : 2025-08-13 16:33:53

**x**

##### 译文声明

本文是翻译文章，文章原作者 Sergiu Gatlan，文章来源：bleepingcomputer

原文地址：<https://www.bleepingcomputer.com/news/security/over-3-000-netscaler-devices-left-unpatched-against-actively-exploited-citrixbleed-2-flaw/>

译文仅供参考，具体内容表达以及含义原文为准。

![]()

超过3300台 Citrix NetScaler 设备仍未修复关键漏洞，存在遭黑客入侵风险

在补丁发布近两个月后，全球仍有超过3300台 Citrix NetScaler 设备未修补一处可让攻击者劫持用户会话、绕过身份验证的高危漏洞。

该漏洞编号为 **CVE-2025-5777**，被称为“**CitrixBleed 2**”，属于越界内存读取漏洞，由输入验证不足导致。受影响的设备包括配置为网关（VPN 虚拟服务器、ICA Proxy、CVPN、RDP Proxy）或 AAA 虚拟服务器的系统。未经身份验证的攻击者可远程访问受限内存区域。

成功利用该漏洞后，威胁行为者能够窃取会话令牌、凭据及其他敏感数据，从而劫持用户会话并绕过多因素身份验证（MFA）。

在该漏洞披露不到两周后，针对 **CVE-2025-5777** 的概念验证（PoC）漏洞利用代码已被公开，而早在 PoC 发布数周前，就有安全机构发现该漏洞已在零日攻击中被积极利用。

两年前，类似的 Citrix 安全漏洞“CitrixBleed”曾被黑客大规模利用，对 NetScaler 设备发起入侵，并在受害网络内部横向移动，导致勒索软件攻击和针对政府机构的重大数据泄露事件。

周一，互联网安全非营利机构 Shadowserver 基金会的安全分析师报告称，仍有 3,312 台 Citrix NetScaler 设备易受正在进行的 **CVE-2025-5777** 攻击威胁。

Shadowserver 还发现，有 4,142 台设备未修补另一处高危漏洞（**CVE-2025-6543**）。Citrix 表示，该漏洞已被用于拒绝服务（DoS）攻击，并被列为“正在遭到积极利用”的安全缺陷。**CVE-2025-6543** 属于内存溢出漏洞，可导致程序控制流异常及服务中断。

![]()

荷兰国家网络安全中心（NCSC）在周一警告称，自今年 5 月初起，攻击者已将该漏洞作为零日漏洞利用，对荷兰多家关键机构发起入侵。

“NCSC 已确认，荷兰多家关键机构遭到通过 Citrix NetScaler **CVE-2025-6543** 漏洞的成功攻击，”该机构表示，“NCSC 评估，这些攻击由一个或多个行动手法高级的威胁组织实施。漏洞在被利用时属于零日状态，攻击者还主动清除了痕迹，以掩盖对受害机构的入侵。”

虽然 NCSC 并未公开受影响机构的名称，但荷兰公共检察署（Openbaar Ministerie）在 7 月 18 日于接到 NCSC 警告后披露遭遇数据泄露。此次攻击造成该机构业务严重受扰，其电子邮件服务器直到近期才恢复运行。

美国网络安全与基础设施安全局（CISA）也已将上述两处漏洞加入“正在被利用的已知漏洞”目录，要求联邦机构在 1 天内完成针对 **CVE-2025-5777** 的防护措施，并在 7 月 21 日前修补 **CVE-2025-6543** 漏洞。

本文翻译自bleepingcomputer [原文链接](https://www.bleepingcomputer.com/news/security/over-3-000-netscaler-devices-left-unpatched-against-actively-exploited-citrixbleed-2-flaw/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/311147](/post/id/311147)

安全KER - 有思想的安全新媒体

本文转载自: [bleepingcomputer](https://www.bleepingcomputer.com/news/security/over-3-000-netscaler-devices-left-unpatched-against-actively-exploited-citrixbleed-2-flaw/)

如若转载,请注明出处： <https://www.bleepingcomputer.com/news/security/over-3-000-netscaler-devices-left-unpatched-against-actively-exploited-citrixbleed-2-flaw/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [安全资讯](/tag/%E5%AE%89%E5%85%A8%E8%B5%84%E8%AE%AF)
* [漏洞情报](/tag/%E6%BC%8F%E6%B4%9E%E6%83%85%E6%8A%A5)

**+1**3赞

收藏

![](https://p1.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p0.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p1.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=171771)

[安全客](/member.html?memberId=171771)

这个人太懒了，签名都懒得写一个

* 文章
* **545**

* 粉丝
* **5**

### TA的文章

* ##### [国庆重保+攻防演练大考在即！360大模型安全服务专项方案筑牢AI防线](/post/id/312460)

  2025-09-29 18:06:17
* ##### [Apache Airflow 存在权限漏洞，可导致只读用户获取敏感信息](/post/id/312457)

  2025-09-29 18:05:56
* ##### [Meta 旨在打造机器人领域的“Android”，为下一代人形AI提供通用平台](/post/id/312454)

  2025-09-29 18:05:34
* ##### [Formbricks 存在高危漏洞 (CVE-2025-59934)，攻击者可通过伪造JWT令牌导致未授权的密码重置](/post/id/312451)

  2025-09-29 18:05:05
* ##### [Notepad++ 中存在DLL劫持漏洞（CVE-2025-56383），可导致任意代码执行，且POC已公开](/post/id/312448)

  2025-09-29 18:04:33

### 相关文章

* ##### [国庆重保+攻防演练大考在即！360大模型安全服务专项方案筑牢AI防线](/post/id/312460)

  2025-09-29 18:06:17
* ##### [Apache Airflow 存在权限漏洞，可导致只读用户获取敏感信息](/post/id/312457)

  2025-09-29 18:05:56
* ##### [Meta 旨在打造机器人领域的“Android”，为下一代人形AI提供通用平台](/post/id/312454)

  2025-09-29 18:05:34
* ##### [Formbricks 存在高危漏洞 (CVE-2025-59934)，攻击者可通过伪造JWT令牌导致未授权的密码重置](/post/id/312451)

  2025-09-29 18:05:05
* ##### [Notepad++ 中存在DLL劫持漏洞（CVE-2025-56383），可导致任意代码执行，且POC已公开](/post/id/312448)

  2025-09-29 18:04:33
* ##### [Morte僵尸网络被披露：正利用路由器与企业应用漏洞，迅速扩张其“加载器即服务”活动](/post/id/312444)

  2025-09-29 18:04:01
* ##### [Akira勒索软件利用SonicWall VPN账户发起急速入侵](/post/id/312438)

  2025-09-29 18:03:28

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