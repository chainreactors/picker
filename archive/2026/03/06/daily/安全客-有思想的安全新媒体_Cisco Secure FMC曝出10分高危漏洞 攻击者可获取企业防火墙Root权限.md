---
title: Cisco Secure FMC曝出10分高危漏洞 攻击者可获取企业防火墙Root权限
url: https://www.anquanke.com/post/id/315023
source: 安全客-有思想的安全新媒体
date: 2026-03-06
fetch_date: 2026-03-07T03:54:52.112739
---

# Cisco Secure FMC曝出10分高危漏洞 攻击者可获取企业防火墙Root权限

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

# Cisco Secure FMC曝出10分高危漏洞 攻击者可获取企业防火墙Root权限

阅读量**21368**

发布时间 : 2026-03-06 10:51:30

**x**

##### 译文声明

本文是翻译文章，文章原作者 Ddos ，文章来源：securityonline

原文地址：<https://securityonline.info/critical-10-0-cvss-flaw-in-cisco-secure-fmc-hands-hackers-root-access-to-enterprise-firewalls/>

译文仅供参考，具体内容表达以及含义原文为准。

![]()

网络安全研究人员在 **Cisco Secure Firewall Management Center (FMC) 软件**中发现一处**高危漏洞**。该平台是企业统一安全策略的管理核心，相当于整个企业网络的安全 “神经中枢”。

该漏洞编号为 **CVE-2026-20131**，CVSS 评分达到**满分 10.0**，属于无需认证即可远程代码执行（RCE） 的顶级风险漏洞。

---

Cisco Secure FMC 是一款集中管理平台，管理员可通过单一界面监控和控制防火墙、应用策略与入侵防御系统。而此次漏洞直接威胁到该平台管理控制台的**核心安全**。

该漏洞存在于 FMC 软件的**Web 管理界面**中，根源是系统对来自网络的输入数据流处理不当。

根据官方公告描述：**该漏洞源于对用户提供的 Java 字节流存在不安全反序列化问题**。未认证的远程攻击者只需**向受影响设备的 Web 管理界面发送精心构造的序列化 Java 对象**，即可利用该漏洞。

一旦利用成功，后果将是**毁灭性**的：

**攻击者可在设备上执行任意代码，并直接提升权限至 Root 管理员权限。**

获取 FMC 的 Root 权限后，攻击者可随意篡改安全策略、关闭防火墙防护，并以此为跳板对企业内部基础设施进行**横向渗透**。

---

该漏洞影响范围广泛，涉及思科多款安全管理产品：

* **Cisco Secure FMC Software**：所有部署环境均受影响，与具体设备配置无关
* **Cisco Security Cloud Control (SCC)**：同样存在漏洞，但作为 SaaS 服务，思科已启动自动维护修复，**用户无需任何操作**

思科产品安全事件响应团队（PSIRT）表示，目前**暂未发现该漏洞在野利用或恶意攻击案例**。但由于**不存在可缓解该漏洞的临时解决方案**，企业必须**立即采取修复措施**。

本文翻译自securityonline [原文链接](https://securityonline.info/critical-10-0-cvss-flaw-in-cisco-secure-fmc-hands-hackers-root-access-to-enterprise-firewalls/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/315023](/post/id/315023)

安全KER - 有思想的安全新媒体

本文转载自: [securityonline](https://securityonline.info/critical-10-0-cvss-flaw-in-cisco-secure-fmc-hands-hackers-root-access-to-enterprise-firewalls/)

如若转载,请注明出处： <https://securityonline.info/critical-10-0-cvss-flaw-in-cisco-secure-fmc-hands-hackers-root-access-to-enterprise-firewalls/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [安全资讯](/tag/%E5%AE%89%E5%85%A8%E8%B5%84%E8%AE%AF)
* [漏洞情报](/tag/%E6%BC%8F%E6%B4%9E%E6%83%85%E6%8A%A5)

**+1**0赞

收藏

![](https://p5.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p5.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p5.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=171771)

[安全客](/member.html?memberId=171771)

这个人太懒了，签名都懒得写一个

* 文章
* **1060**

* 粉丝
* **6**

### TA的文章

* ##### [Django发布安全补丁 修复拒绝服务与权限类漏洞](/post/id/315047)

  2026-03-06 10:56:33
* ##### [攻击者借日历邀请入侵 Perplexity Comet 浏览器并泄露敏感数据](/post/id/315044)

  2026-03-06 10:54:37
* ##### [伊朗关联黑客瞄准监控摄像头漏洞](/post/id/315041)

  2026-03-06 10:54:12
* ##### [癌症中心研究数据遭黑客攻击120万人信息受影响](/post/id/315038)

  2026-03-06 10:53:46
* ##### [Outlook.com为何大量误拦正常商业邮件](/post/id/315035)

  2026-03-06 10:53:13

### 相关文章

* ##### [Django发布安全补丁 修复拒绝服务与权限类漏洞](/post/id/315047)

  2026-03-06 10:56:33
* ##### [攻击者借日历邀请入侵 Perplexity Comet 浏览器并泄露敏感数据](/post/id/315044)

  2026-03-06 10:54:37
* ##### [伊朗关联黑客瞄准监控摄像头漏洞](/post/id/315041)

  2026-03-06 10:54:12
* ##### [癌症中心研究数据遭黑客攻击120万人信息受影响](/post/id/315038)

  2026-03-06 10:53:46
* ##### [Outlook.com为何大量误拦正常商业邮件](/post/id/315035)

  2026-03-06 10:53:13
* ##### [Coruna席卷全球威胁格局的高性能iOS漏洞利用工具包](/post/id/315032)

  2026-03-06 10:52:45
* ##### [Grammarly 从文字纠错转向文学模仿](/post/id/315029)

  2026-03-06 10:52:13

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