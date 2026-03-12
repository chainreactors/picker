---
title: SAP发布重要安全更新 修复高危远程代码执行漏洞
url: https://www.anquanke.com/post/id/315127
source: 安全客-有思想的安全新媒体
date: 2026-03-11
fetch_date: 2026-03-12T04:06:53.495090
---

# SAP发布重要安全更新 修复高危远程代码执行漏洞

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

# SAP发布重要安全更新 修复高危远程代码执行漏洞

阅读量**21837**

发布时间 : 2026-03-11 13:56:58

**x**

##### 译文声明

本文是翻译文章，文章原作者 Ddos ，文章来源：securityonline

原文地址：<https://securityonline.info/critical-alert-saps-latest-security-update-fixes-9-8-cvss-rce-and-deserialization-flaws/>

译文仅供参考，具体内容表达以及含义原文为准。

![]()

SAP 于 2026 年 3 月发布月度安全补丁，在全产品生态中修复**15 个全新安全漏洞**。本次更新尤为关键，其中包含**两个高危漏洞**，若未及时修复，可能导致**远程代码执行**或**系统完全沦陷**。

安全团队应优先处理以下两个 **CVSS 评分超 9.0** 的漏洞：

**[CVE-2019-17571] SAP 报价管理保险模块（FS-QUO）**

该漏洞 **CVSS 评分 9.8**，源于 Log4j 1.2 中过时的 `SocketServer` 类。

攻击者可利用该漏洞实现**不受信数据反序列化**，当系统监听外部网络流量时，可直接触发**远程代码执行（RCE）**。

**[CVE-2026-27685] SAP NetWeaver 企业门户管理**

本次更新修复一处**不安全反序列化漏洞**，**CVSS 评分 9.1**。

拥有上传权限的用户可上传恶意内容触发漏洞，对目标主机的**机密性、完整性、可用性**造成毁灭性影响。

除关键漏洞外，多款应用也获得重要安全更新：

**供应链管理拒绝服务漏洞 [CVE-2026-27689]**

高危漏洞（**CVSS 7.7**），属于**不受控资源消耗**问题。

已认证攻击者可通过大循环参数反复调用特定功能，耗尽系统资源，导致**全线业务中断**。

**NetWeaver AS for ABAP**

核心组件获得多项更新，修复：

* 服务端请求伪造（**SSRF**）[CVE-2026-24316]
* 权限校验缺失 [CVE-2026-24309、CVE-2026-27688]
* 反馈通知中的 **SQL 注入** [CVE-2026-27684]

**SAP Business One（任务服务）**

存在 **DOM 型跨站脚本（XSS）** 漏洞 [CVE-2026-0489]，攻击者可在用户浏览器中执行恶意脚本。

**SAP GUI 的 DLL 劫持漏洞**

使用 Windows 且启用 GuiXT 的用户需更新 [CVE-2026-24317]，防止攻击者通过恶意 **DLL** 执行未授权代码。

### 漏洞等级统计

* **Critical（严重）**：2 个

  影响：**远程代码执行（RCE）、系统沦陷**
* **High（高危）**：1 个

  影响：**拒绝服务（DoS）**
* **Medium（中危）**：11 个

  影响：**SSRF、SQL 注入、XSS、DLL 劫持**
* **Low（低危）**：1 个

  影响：权限校验缺失

本文翻译自securityonline [原文链接](https://securityonline.info/critical-alert-saps-latest-security-update-fixes-9-8-cvss-rce-and-deserialization-flaws/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/315127](/post/id/315127)

安全KER - 有思想的安全新媒体

本文转载自: [securityonline](https://securityonline.info/critical-alert-saps-latest-security-update-fixes-9-8-cvss-rce-and-deserialization-flaws/)

如若转载,请注明出处： <https://securityonline.info/critical-alert-saps-latest-security-update-fixes-9-8-cvss-rce-and-deserialization-flaws/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [安全资讯](/tag/%E5%AE%89%E5%85%A8%E8%B5%84%E8%AE%AF)
* [漏洞情报](/tag/%E6%BC%8F%E6%B4%9E%E6%83%85%E6%8A%A5)

**+1**0赞

收藏

![](https://p0.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p3.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p0.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=171771)

[安全客](/member.html?memberId=171771)

这个人太懒了，签名都懒得写一个

* 文章
* **1080**

* 粉丝
* **6**

### TA的文章

* ##### [侧边栏里的间谍假冒AI浏览器插件窃取90万用户数据](/post/id/315092)

  2026-03-11 14:01:17
* ##### [Kubernetes安全预警Ingress-Nginx注入漏洞可致集群密钥全局泄露](/post/id/315095)

  2026-03-11 14:00:47
* ##### [Budibase存在高危漏洞 可导致生产环境密钥全面泄露](/post/id/315099)

  2026-03-11 14:00:25
* ##### [Radware推出Alteon Protect实现云级ADC应用安全防护](/post/id/315102)

  2026-03-11 14:00:03
* ##### [研究人员打造AI智能体 可全自动实施诈骗通话](/post/id/315106)

  2026-03-11 13:59:37

### 相关文章

* ##### [侧边栏里的间谍假冒AI浏览器插件窃取90万用户数据](/post/id/315092)

  2026-03-11 14:01:17
* ##### [Kubernetes安全预警Ingress-Nginx注入漏洞可致集群密钥全局泄露](/post/id/315095)

  2026-03-11 14:00:47
* ##### [Budibase存在高危漏洞 可导致生产环境密钥全面泄露](/post/id/315099)

  2026-03-11 14:00:25
* ##### [Radware推出Alteon Protect实现云级ADC应用安全防护](/post/id/315102)

  2026-03-11 14:00:03
* ##### [研究人员打造AI智能体 可全自动实施诈骗通话](/post/id/315106)

  2026-03-11 13:59:37
* ##### [黑客利用微软Teams诱骗员工开放远程访问权限](/post/id/315110)

  2026-03-11 13:59:13
* ##### [微软推出365 E5升级套件与Agent 365 AI管控平台](/post/id/315113)

  2026-03-11 13:58:42

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