---
title: Siemens SINEC NMS发现严重漏洞：权限提升与远程代码执行
url: https://www.anquanke.com/post/id/309682
source: 安全客-有思想的安全新媒体
date: 2025-07-11
fetch_date: 2025-10-06T23:16:40.288967
---

# Siemens SINEC NMS发现严重漏洞：权限提升与远程代码执行

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

# Siemens SINEC NMS发现严重漏洞：权限提升与远程代码执行

阅读量**54757**

发布时间 : 2025-07-10 16:17:13

**x**

##### 译文声明

本文是翻译文章，文章原作者 Ddos，文章来源：securityonline

原文地址：<https://securityonline.info/critical-flaws-found-in-siemens-sinec-nms-privilege-escalation-and-remote-code-execution-risks/>

译文仅供参考，具体内容表达以及含义原文为准。

![]()

Siemens发布了关于其工业环境网络管理系统SINEC NMS的严重安全通告，详细列出了多个高危漏洞。受影响的版本包括所有4.0版本之前的SINEC NMS。如果被利用，攻击者可能会获得管理权限、执行任意代码或在关键基础设施网络中提升特权。

通告警告称：“版本4.0之前的Siemens SINEC NMS受到多个漏洞的影响，这些漏洞可能允许攻击者提升权限并执行任意代码。”

这些漏洞的CVSS v3.1基础评分高达9.8，被认为是关键漏洞，尤其是在SINEC NMS常被用于监控和管理工业网络的运营技术（OT）环境中。

SINEC NMS是Siemens为数字化企业提供的网络管理平台，能够集中配置、监控和管理工业网络。该平台广泛应用于制造业、能源和基础设施行业，成为攻击者寻求破坏或渗透OT环境的重要目标。

### **CVE-2025-40736 – 关键功能缺少身份验证**

这是最严重的漏洞，CVSS v3.1评分为9.8。该漏洞暴露了一个端点，允许未授权修改管理凭证。攻击者可以重置超级管理员密码，从而完全控制NMS系统。

Siemens透露：“这可能允许未授权的攻击者重置超级管理员密码并完全控制应用程序。”

该漏洞由ZDI-CAN-26569跟踪，代表了无需任何用户交互即可直接完全危害系统的路径。

### **CVE-2025-40735 – SQL注入**

这是一个经典且危险的Web漏洞，SQL注入缺陷允许未授权的远程攻击者在系统的后端数据库上执行任意SQL查询。

Siemens表示：“受影响的设备容易受到SQL注入攻击。这可能允许未授权的远程攻击者在服务器数据库上执行任意SQL查询。”

由于此漏洞可能导致敏感数据泄露或篡改配置记录，特别是与其他漏洞结合时，带来了严重的风险。

### C**VE-2025-40737 & CVE-2025-40738 – 通过恶意ZIP文件提取进行路径遍历**

这两个漏洞源于ZIP文件提取过程中未正确验证文件路径。攻击者通过精心构造恶意归档文件，可以将任意文件写入受限目录，并可能执行具有提升权限的代码。

Siemens表示：“这可能允许攻击者将任意文件写入受限位置，并可能执行具有提升权限的代码。”

这两个漏洞分别被跟踪为ZDI-CAN-26571和ZDI-CAN-26572，CVSS v3.1评分均为8.8。

### Siemens的建议

Siemens已发布SINEC NMS v4.0版本来修复所有已知漏洞。建议客户立即升级。

对于无法立即应用更新的系统，西门子建议遵循其操作安全指南，并确保设备的网络访问安全。

一般的安全做法包括：

* 限制仅信任的用户和网络段的访问
* 遵循Siemens的工业安全指南
* 监控日志，防止未经授权的配置更改

本文翻译自securityonline [原文链接](https://securityonline.info/critical-flaws-found-in-siemens-sinec-nms-privilege-escalation-and-remote-code-execution-risks/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/309682](/post/id/309682)

安全KER - 有思想的安全新媒体

本文转载自: [securityonline](https://securityonline.info/critical-flaws-found-in-siemens-sinec-nms-privilege-escalation-and-remote-code-execution-risks/)

如若转载,请注明出处： <https://securityonline.info/critical-flaws-found-in-siemens-sinec-nms-privilege-escalation-and-remote-code-execution-risks/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [安全资讯](/tag/%E5%AE%89%E5%85%A8%E8%B5%84%E8%AE%AF)
* [漏洞情报](/tag/%E6%BC%8F%E6%B4%9E%E6%83%85%E6%8A%A5)

**+1**5赞

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