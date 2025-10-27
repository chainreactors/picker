---
title: 在VMWare NSX中发现多个存储的XSS漏洞-立即修补
url: https://www.anquanke.com/post/id/308161
source: 安全客-有思想的安全新媒体
date: 2025-06-06
fetch_date: 2025-10-06T22:47:50.945121
---

# 在VMWare NSX中发现多个存储的XSS漏洞-立即修补

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

# 在VMWare NSX中发现多个存储的XSS漏洞-立即修补

阅读量**97410**

发布时间 : 2025-06-05 13:24:48

**x**

##### 译文声明

本文是翻译文章，文章原作者 Ddos，文章来源：securityonline

原文地址：<https://securityonline.info/multiple-stored-xss-vulnerabilities-discovered-in-vmware-nsx-patch-now/>

译文仅供参考，具体内容表达以及含义原文为准。

![VMware NSX, XSS 漏洞]()

Broadcom发布了重要的更新,解决了VMware NSX中三个新披露的漏洞,所有这些漏洞都使用户暴露于存储跨站点脚本(XSS)攻击。这些缺陷(如CVE-2025-22243、CVE-2025-22244和CVE-2025-22245)影响了一系列VMware产品,包括VMware NSX、VMware Cloud Foundation和VMware Telco Cloud Platform。

根据Broadcom的咨询这些漏洞是私人报告的,并且源于NSX接口关键组件中的“不当输入验证”。这些缺陷可能允许经过身份验证的攻击者注入持久的恶意JavaScript代码,这些代码在毫无戒心的管理员或用户访问特定配置面板时执行。

* **CVE-2025-22243 – NSX Manager UI 中的 XSS(CVSS 7.5 – 重要严重程度)**
  具有修改网络设置权限的威胁行为者可能会将恶意脚本注入管理器 UI。*“具有创建或修改网络设置权限的恶意行为者可能能够注入在查看网络设置时执行的恶意代码*[,”该咨询解释说。](https://support.broadcom.com/web/ecx/support-content-notification/-/external/content/SecurityAdvisories/0/25738)
* **CVE-2025-22244 – 网关防火墙中的XSS(CVSS 6.9 – 中度严重程度)**
  此漏洞允许通过网关防火墙界面内的 URL 过滤响应页面注入代码。*“一个可以访问创建或修改响应页面以过滤URL的恶意行为者可能能够注入恶意代码,当其他用户尝试访问过滤后的网站时,这些代码会被执行。*
* **CVE-2025-22245 – 路由器端口中的XSS(CVSS 5.9 – 中度严重程度)**
  在路由器端口配置中存储的 XSS 可以允许在其他用户检查路由器设置时触发攻击。*“具有创建或修改路由器端口权限的恶意行为者可能能够注入当其他用户尝试访问路由器端口时被执行的恶意代码。*

Broadcom列出了多个产品线中的所有易受攻击的版本。受影响的NSX版本包括4.2.x,4.2.1.x,4.1.x和4.0.x,固定版本可用于:

* ①NSX 4.2.x → 4.2.2.1
* ②NSX 4.2.1.x → 4.2.1.4
* ③NSX 4.1.x 和 4.0.x → 4.1.2.6

对于 VMware Cloud Foundation (v5.0–5.2) 的用户,Broadcom 建议使用 [KB88287](https://knowledge.broadcom.com/external/article?legacyId=88287) 中的指导,将 NSX 同步修补到 4.2.2.1 或 4.1.2.6 版本。电信云用户被转介到 [KB396986](https://knowledge.broadcom.com/external/article/396986) 以获取升级路径。

[虽然没有公开利用报告](https://securityonline.info/hostedscan-review-proactive-vulnerability-management-for-a-bulletproof-digital-presence/),但敦促管理员立即修补受影响的系统,特别是因为缺陷需要特权访问,并可用于开发后或横向移动场景。

本文翻译自securityonline [原文链接](https://securityonline.info/multiple-stored-xss-vulnerabilities-discovered-in-vmware-nsx-patch-now/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/308161](/post/id/308161)

安全KER - 有思想的安全新媒体

本文转载自: [securityonline](https://securityonline.info/multiple-stored-xss-vulnerabilities-discovered-in-vmware-nsx-patch-now/)

如若转载,请注明出处： <https://securityonline.info/multiple-stored-xss-vulnerabilities-discovered-in-vmware-nsx-patch-now/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [漏洞](/tag/%E6%BC%8F%E6%B4%9E)
* [安全知识](/tag/%E5%AE%89%E5%85%A8%E7%9F%A5%E8%AF%86)
* [安全头条](/tag/%E5%AE%89%E5%85%A8%E5%A4%B4%E6%9D%A1)

**+1**0赞

收藏

![](https://p2.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p0.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p2.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=170061)

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

* ##### [论韧性数字安全体系（第十三章）](/post/id/309219)

  2025-07-01 15:03:14
* ##### [AI即万物：ISC.AI 2025的跨越变迁](/post/id/308744)

  2025-06-20 18:39:26
* ##### [起亚厄瓜多尔无钥匙进入系统漏洞导致数千辆车辆被盗](/post/id/308480)

  2025-06-16 15:48:35
* ##### [微软 Office 漏洞允许攻击者执行远程代码](/post/id/308412)

  2025-06-12 15:43:53
* ##### [人工智能可能修复帮助传播了 15 年的漏洞](/post/id/308401)

  2025-06-12 15:19:33
* ##### [美国CISA警告 SinoTrack GPS 跟踪器存在远程控制漏洞](/post/id/308398)

  2025-06-12 15:15:38
* ##### [Cyera融资5.4亿美元，估值翻番，致力于人工智能数据保护](/post/id/308391)

  2025-06-12 14:36:27

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