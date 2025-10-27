---
title: 思科警告 UCS IMC 和 NDFC 系统存在高严重性 SSH 安全漏洞
url: https://www.anquanke.com/post/id/308140
source: 安全客-有思想的安全新媒体
date: 2025-06-06
fetch_date: 2025-10-06T22:47:55.534916
---

# 思科警告 UCS IMC 和 NDFC 系统存在高严重性 SSH 安全漏洞

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

# 思科警告 UCS IMC 和 NDFC 系统存在高严重性 SSH 安全漏洞

阅读量**106097**

发布时间 : 2025-06-05 12:41:03

**x**

##### 译文声明

本文是翻译文章，文章原作者 Ddos，文章来源：securityonline

原文地址：<https://securityonline.info/cisco-warns-of-high-severity-ssh-security-flaws-in-ucs-imc-and-ndfc-systems/#google_vignette>

译文仅供参考，具体内容表达以及含义原文为准。

![思科漏洞,特权升级]()

思科发布了两个高严重性漏洞的安全公告,一个在思科集成管理控制器(IMC)中,另一个在Nexus仪表板结构控制器(NDFC)中,这两个漏洞都对企业基础设施构成严重风险。这些缺陷被追踪为CVE-2025-20261(CVSS 8.8)和CVE-2025-20163(CVSS 8.7),影响数据中心、云环境和边缘部署中使用的各种UCS和Nexus产品。

### **CVE-2025-20261:通过SSH在Cisco UCS IMC(CVSS 8.8)上提升特权**

Cisco IMC 的 SSH 连接处理中的漏洞可能允许经过身份验证的远程攻击者获得提升的权限并修改系统配置。

*“成功的漏洞利用可能允许攻击者访问具有提升权限的内部服务,这可能允许对系统进行未经授权的修改,*[包括在受影响的设备上创建新的管理员帐户的可能性。](https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-ucs-ssh-priv-esc-2mZDtdjM)

此漏洞影响以下 Cisco 产品,如果它们运行易受攻击的软件版本,并且它们接受传入的 SSH 连接到 Cisco IMC:

* UCS B 系列、C 系列、S 系列和 X 系列服务器
* 基于 UCS 平台构建的 Cisco 设备:
  + APIC、Catalyst Center、Secure Endpoint、HyperFlex、Meeting Server 1000、Telemetry Broker 等。

缓解包括禁用 SSH 或串行 LAN (SoL)(如适用)。受影响的系统应升级到修补固件版本,如4.1(3n),4.2(3k)或5.2(2.240073),具体取决于服务器模式。

**[CVE-2025-20163:思科NDFC中的SSH主机密钥验证漏洞](https://securityonline.info/pentest-tools-com-review-your-all-in-one-platform-for-streamlined-penetration-testing-and-vulnerability-management/)(CVSS 8.7)**

第二个问题涉及Cisco Nexus仪表板织物控制器(NDFC),以前称为DCNM。此漏洞允许未经身份验证的远程攻击者通过利用不足的 SSH 主机密钥验证来冒充托管设备。

*“成功的漏洞利用可能允许攻击者冒充托管设备并捕获用户凭据*[,”该咨询警告说。](https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-ndfc-shkv-snQJtjrp)

通过对SSH会话执行机器中间(MitM)攻击,攻击者可以拦截或操纵NDFC与其托管设备之间的通信。

思科在Nexus Dashboard版本3.2(2f)中解决了这个问题。早期版本,包括旧版DCNM版本,都是易受攻击的,应该及时更新。

思科产品安全事件响应小组(PSIRT)*[指出:“思科PSIRT不知道任何公告或恶意使用该漏洞。](https://securityonline.info/pentest-tools-com-review-your-all-in-one-platform-for-streamlined-penetration-testing-and-vulnerability-management/)*

然而,鉴于这些组件提供的访问级别,组织应该将这些视为关键补丁优先级。

本文翻译自securityonline [原文链接](https://securityonline.info/cisco-warns-of-high-severity-ssh-security-flaws-in-ucs-imc-and-ndfc-systems/#google_vignette)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/308140](/post/id/308140)

安全KER - 有思想的安全新媒体

本文转载自: [securityonline](https://securityonline.info/cisco-warns-of-high-severity-ssh-security-flaws-in-ucs-imc-and-ndfc-systems/#google_vignette)

如若转载,请注明出处： <https://securityonline.info/cisco-warns-of-high-severity-ssh-security-flaws-in-ucs-imc-and-ndfc-systems/#google_vignette>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [漏洞分析](/tag/%E6%BC%8F%E6%B4%9E%E5%88%86%E6%9E%90)
* [安全知识](/tag/%E5%AE%89%E5%85%A8%E7%9F%A5%E8%AF%86)
* [安全热点](/tag/%E5%AE%89%E5%85%A8%E7%83%AD%E7%82%B9)
* [漏洞情报](/tag/%E6%BC%8F%E6%B4%9E%E6%83%85%E6%8A%A5)

**+1**0赞

收藏

![](https://p4.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p5.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p4.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=170061)

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