---
title: 思科 IMC 漏洞攻击者利用提升的权限访问内部服务
url: https://www.anquanke.com/post/id/308205
source: 安全客-有思想的安全新媒体
date: 2025-06-07
fetch_date: 2025-10-06T22:49:58.132032
---

# 思科 IMC 漏洞攻击者利用提升的权限访问内部服务

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

# 思科 IMC 漏洞攻击者利用提升的权限访问内部服务

阅读量**123465**

发布时间 : 2025-06-06 15:42:33

**x**

##### 译文声明

本文是翻译文章，文章原作者 Kaaviya，文章来源：cybersecuritynews

原文地址：<https://cybersecuritynews.com/cisco-imc-privilege-escalation-vulnerability/>

译文仅供参考，具体内容表达以及含义原文为准。

[思科集成管理控制器(IMC)](https://cybersecuritynews.com/cisco-imc-command-injection-vulnerability/)中的一个重大漏洞,允许恶意行为者在未经适当授权的情况下获得提升的权限并访问内部服务。

这种漏洞给依赖思科服务器管理基础设施的企业网络带来了巨大风险,可能使攻击者能够破坏关键系统和敏感数据。

###

### **思科 IMC 特权升级缺陷**

思科IMC漏洞(CVE-2025-20261)被归类为权限升级漏洞,利用了管理控制器Web界面中身份验证和授权机制的弱点。

攻击者可以利用不适当的输入验证和不充分的访问控制来绕过安全限制并执行具有管理权限的命令。

该漏洞影响用于系统配置和监控的 RESTful API 端点,允许未经授权的用户操作服务器设置并访问受限功能。

[技术分析显示](https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-ucs-ssh-priv-esc-2mZDtdjM),漏洞针对/redfish/v1/ API端点,其中会话验证不足使攻击者能够通过精心制作的HTTP请求升级其权限。

当 IMC 未能根据基于角色的访问控制 (RBAC) 策略正确验证用户凭据时,特别是在涉及 JSON Web Token (JWT) 操作和会话劫持技术的场景中,该漏洞会显示。

利用此漏洞可能对使用受影响的 Cisco IMC 系统的组织产生深远的影响。

获得提升权限的攻击者可以访问基板管理控制器(BMC)功能,使他们能够修改BIOS设置,访问带外管理接口,并可能安装持久固件级恶意软件。

这种级别的访问绕过了传统的安全控制,可以为攻击者提供跨网络基础设施横向移动的立足点。

该漏洞特别威胁到部署Cisco UCS(统一计算系统)服务器的数据中心环境。

利用此漏洞的攻击者可以访问思科集成管理控制器的IPMI(智能平台管理接口)功能,使他们能够监控系统运行状况,访问虚拟媒体服务,并可能拦截通过管理网络传输的敏感数据。

![]()

### **缓解战略**

使用受影响的 Cisco IMC 系统的组织应立即实施全面的安全措施,以减轻与此漏洞相关的风险。

主要缓解涉及更新到最新的固件版本,以解决身份验证绕过和权限升级缺陷。

网络管理员应配置适当的网络分割,以将管理接口与生产网络隔离,并实现所有管理访问的多因素身份验证(MFA)。

额外的安全强化措施包括禁用IMC接口上不必要的服务,实施严格的防火墙规则以限制对TCP端口80、443和623的访问(用于通过LAN的IPMI),以及定期审核具有管理权限的用户帐户。

组织还应监控其安全信息和事件管理(SIEM)系统中的可疑活动,特别是关注对/api/端点的异常API调用以及未经授权访问基于Web的管理界面的尝试。

本文翻译自cybersecuritynews [原文链接](https://cybersecuritynews.com/cisco-imc-privilege-escalation-vulnerability/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/308205](/post/id/308205)

安全KER - 有思想的安全新媒体

本文转载自: [cybersecuritynews](https://cybersecuritynews.com/cisco-imc-privilege-escalation-vulnerability/)

如若转载,请注明出处： <https://cybersecuritynews.com/cisco-imc-privilege-escalation-vulnerability/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [漏洞分析](/tag/%E6%BC%8F%E6%B4%9E%E5%88%86%E6%9E%90)
* [安全知识](/tag/%E5%AE%89%E5%85%A8%E7%9F%A5%E8%AF%86)
* [安全热点](/tag/%E5%AE%89%E5%85%A8%E7%83%AD%E7%82%B9)
* [漏洞情报](/tag/%E6%BC%8F%E6%B4%9E%E6%83%85%E6%8A%A5)

**+1**0赞

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

* ##### [Apache Airflow 存在权限漏洞，可导致只读用户获取敏感信息](/post/id/312457)

  2025-09-29 18:05:56
* ##### [Formbricks 存在高危漏洞 (CVE-2025-59934)，攻击者可通过伪造JWT令牌导致未授权的密码重置](/post/id/312451)

  2025-09-29 18:05:05
* ##### [Notepad++ 中存在DLL劫持漏洞（CVE-2025-56383），可导致任意代码执行，且POC已公开](/post/id/312448)

  2025-09-29 18:04:33
* ##### [CISA称黑客利用GeoServer漏洞成功入侵一联邦机构](/post/id/312347)

  2025-09-24 16:45:06
* ##### [SolarWinds紧急发布补丁，修复高危远程代码执行漏洞CVE-2025-26399](/post/id/312357)

  2025-09-24 16:43:11
* ##### [Chrome浏览器存在高危漏洞，可致攻击者窃取敏感信息并引发系统崩溃](/post/id/312366)

  2025-09-24 16:42:08
* ##### [CVE-2025-55241：CVSS评分10.0的Microsoft Entra ID漏洞可能危及全球所有租户](/post/id/312294)

  2025-09-22 18:14:51

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