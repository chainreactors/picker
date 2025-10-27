---
title: VMware NSX XSS 漏洞允许攻击者注入恶意代码
url: https://www.anquanke.com/post/id/308197
source: 安全客-有思想的安全新媒体
date: 2025-06-07
fetch_date: 2025-10-06T22:50:00.598181
---

# VMware NSX XSS 漏洞允许攻击者注入恶意代码

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

# VMware NSX XSS 漏洞允许攻击者注入恶意代码

阅读量**107664**

发布时间 : 2025-06-06 15:26:57

**x**

##### 译文声明

本文是翻译文章，文章原作者 Guru Baran，文章来源：cybersecuritynews

原文地址：<https://cybersecuritynews.com/vmware-nsx-xss-vulnerability/>

译文仅供参考，具体内容表达以及含义原文为准。

VMware NSX网络虚拟化平台中的多个跨站点脚本(XSS)漏洞可能允许恶意行为者注入和执行有害代码。

2025 年 6 月 4 日发布的安全公告详细介绍了影响 VMware NSX Manager UI、网关防火墙和路由器端口组件的三个不同漏洞,其基本评分从 5.9 到 7.5 不等。

###

### **CVE-2025-22243:在NSX管理器UI中存储的XSS漏洞**

CVE-2025-22243 漏洞是 VMware NSX Manager 用户界面 (UI) 中存储的一个关键存储跨站点脚本 (XSS) 缺陷,CVSSv3 基数得分为 7.5(重要严重性)。

问题源于网络配置字段中输入验证不当,允许持续注入恶意JavaScript有效载荷。

此漏洞影响所有 VMware NSX 4.0.x 至 4.2.x 版本,以及 VMware Cloud Foundation 和 Telco Cloud Infrastructure 等依赖平台。

具有管理权限修改网络设置的攻击者可以在 DNS 名称或 IP 地址描述等字段中嵌入恶意脚本。

当合法管理员通过 NSX Manager UI 查看受损配置时,这些有效载荷会自动执行。

攻击利用管理界面固有的特权升级风险,因为注入的代码在受害者的会话上下文中运行,可能实现凭据盗窃或横向移动。

###

### **CVE-2025-22244:将XSS存储在网关防火墙响应页面中**

CVE-2025-22244 影响 NSX 的网关防火墙 URL 过滤组件,CVSSv3 评分为 6.9(中度严重程度)。

该漏洞允许恶意行为者将脚本注入用户尝试访问被阻止网站时显示的自定义响应页面。这会影响NSX 4.0.x-4.2.x和依赖的云平台。

具有网关防火墙配置权限的攻击者可以修改块页面的 HTML 模板,以包含 <script> 标签或事件处理程序属性。

当用户遇到这些页面时,他们的浏览器在NSX UI域的上下文中执行嵌入式代码,从而实现会话劫持或网络钓鱼攻击。

###

### **CVE-2025-22245:在路由器端口配置中存储XSS**

CVE-2025-22245漏洞(CVSSv3:5.9,中度)位于NSX的路由器端口管理接口中。

端口描述字段的不当消毒可以进行脚本注入,影响NSX 4.0.x-4.2.x部署和集成云平台。具有路由器端口修改权限的恶意行为者可以将 JavaScript 插入到描述元数据中。

当其他用户查看或编辑受损的端口配置时,有效载荷会触发,从而可能拦截网络流量数据或更改路由表。这三个漏洞都存在输入消毒不足和特权访问要求的共同根源。

###

### **补丁可用**

VMware发布了针对受影响产品线中所有三个漏洞的全面补丁。

对于 VMware NSX 部署,用户应立即升级到 4.2.2.1 版,4.2.1 安装版本 4.2.1,4.2.1 版本升级为 4.2.1.4,4.1.x 版本升级为 4.1.2.6 版本。

值得注意的是,VMware 已停止支持 4.0.x 版本,建议迁移到 4.1.2.6 补丁版本。VMware Cloud Foundation 环境需要异步修补到相应的 NSX 版本。

修补过程因 Cloud Foundation 版本而异,5.2.x 需要 NSX 4.2.2.1,早期版本需要 NSX 4.1.2.6。

VMware已经确认,这些漏洞没有变通办法,这使得立即修补成为唯一有效的缓解策略。

组织应该优先考虑这些更新,因为特权升级的可能性以及网络管理界面中存储的跨站点脚本(XSS)攻击的持久性。

本文翻译自cybersecuritynews [原文链接](https://cybersecuritynews.com/vmware-nsx-xss-vulnerability/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/308197](/post/id/308197)

安全KER - 有思想的安全新媒体

本文转载自: [cybersecuritynews](https://cybersecuritynews.com/vmware-nsx-xss-vulnerability/)

如若转载,请注明出处： <https://cybersecuritynews.com/vmware-nsx-xss-vulnerability/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [漏洞分析](/tag/%E6%BC%8F%E6%B4%9E%E5%88%86%E6%9E%90)
* [安全知识](/tag/%E5%AE%89%E5%85%A8%E7%9F%A5%E8%AF%86)

**+1**0赞

收藏

![](https://p5.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p3.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p5.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=170061)

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
* ##### [无文件 AsyncRAT 活动利用隐蔽的 PowerShell 有效载荷攻击德国用户](/post/id/308562)

  2025-06-18 15:22:31
* ##### [起亚厄瓜多尔无钥匙进入系统漏洞导致数千辆车辆被盗](/post/id/308480)

  2025-06-16 15:48:35
* ##### [微软 Office 漏洞允许攻击者执行远程代码](/post/id/308412)

  2025-06-12 15:43:53
* ##### [美国CISA警告 SinoTrack GPS 跟踪器存在远程控制漏洞](/post/id/308398)

  2025-06-12 15:15:38
* ##### [黑客通过恶意简历瞄准求职者](/post/id/308388)

  2025-06-12 14:31:49
* ##### [微软修补被阿联酋黑客利用的零日漏洞](/post/id/308384)

  2025-06-12 14:28:52

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