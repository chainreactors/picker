---
title: 帕洛阿尔托网络公司警告XSS漏洞，并使用SEARCH漏洞代码
url: https://www.anquanke.com/post/id/307595
source: 安全客-有思想的安全新媒体
date: 2025-05-22
fetch_date: 2025-10-06T22:26:53.046528
---

# 帕洛阿尔托网络公司警告XSS漏洞，并使用SEARCH漏洞代码

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

# 帕洛阿尔托网络公司警告XSS漏洞，并使用SEARCH漏洞代码

阅读量**33383**

发布时间 : 2025-05-21 15:18:48

**x**

##### 译文声明

本文是翻译文章，文章原作者 Ddos，文章来源：securityonline

原文地址：<https://securityonline.info/palo-alto-networks-warns-of-xss-flaw-with-poc-exploit-code/>

译文仅供参考，具体内容表达以及含义原文为准。

![GlobalProtect XSS, PAN-OS 安全]()

Palo Alto Networks发布了一个反映跨站点脚本(XSS)漏洞的安全公告,该漏洞被跟踪为CVE-2025-0133,影响其PAN-OS软件中的GlobalProtect网关和门户组件。该漏洞允许攻击者制作看似合法的钓鱼链接,并可以在经过身份验证的用户的浏览器中执行恶意JavaScript。

虽然默认配置下的CVSS基数为5.1(Low),但启用Clientless VPN时风险增加到6.9(Medium)。

*根据咨询:“Palo Alto Networks PAN-OS软件的GlobalProtect网关和门户功能中反映的跨站点脚本(XSS)漏洞,可以在经过身份验证的Captive Portal用户浏览器的上下文中执行恶意JavaScript,*当他们点击经特殊制作的链接时。

这使得该漏洞特别适用于网络钓鱼活动和凭据窃取场景,特别是在使用无客户端VPN功能的环境中。

*“此漏洞的完整性影响仅限于使攻击者能够创建似乎托管在GlobalProtect门户上的网络钓鱼和凭证窃取链接*,”该公司补充说。

*此漏洞特别适用于“具有启用的 GlobalProtect 网关或门户的 PAN-OS 防火墙配置”。*以下 PAN-OS 版本受到影响:

* 云NGFW:所有版本
* PAN-OS 11.2: 11.2.7 之前的版本
* PAN-OS 11.1:11 之前的版本
* PAN-OS 10.2:10.17 之前的版本
* PAN-OS 10.1:所有版本

需要注意的是,Prisma Access 不受影响。

截至目前*,“Palo Alto Networks exploitation*不知道任何恶意利用这个问题”。但是,该漏洞可以使用概念验证漏洞漏洞。

解决方案是升级到未受影响的PAN-OS版本:

* PAN-OS 11.2:升级到11.2.7或更高版本(ETA 2025年6月)
* PAN-OS 11.1: 升级到 11.11 或更高版本(ETA 2025年7月)
* PAN-OS 10.2:升级到10.2.17或更高版本(ETA 2025年8月)
* PAN-OS 10.1:升级到10.2.17或更高版本(ETA 2025年8月)。请记住,PAN-OS 10.1支持有限,并于2025年8月达到软件EOL。
* 对于所有其他不受支持的 PAN-OS 版本,建议升级到受支持的固定版本。

对于具有威胁防护订阅的客户,可以显著缓解。“威胁 ID 510003 和 510004(在应用程序和威胁内容版本 8970 中引入)vulnerability”可以阻止此漏洞的攻击。这些威胁ID已经“在阻止攻击的Prisma Access上启用”。

此外,禁用无客户端VPN是减少此漏洞严重程度的可行解决方法。有关全面细节,Palo Alto Networks 建议查看安全咨询 [PAN-SA-2025-0005。](https://security.paloaltonetworks.com/PAN-SA-2025-0005)

本文翻译自securityonline [原文链接](https://securityonline.info/palo-alto-networks-warns-of-xss-flaw-with-poc-exploit-code/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/307595](/post/id/307595)

安全KER - 有思想的安全新媒体

本文转载自: [securityonline](https://securityonline.info/palo-alto-networks-warns-of-xss-flaw-with-poc-exploit-code/)

如若转载,请注明出处： <https://securityonline.info/palo-alto-networks-warns-of-xss-flaw-with-poc-exploit-code/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [安全热点](/tag/%E5%AE%89%E5%85%A8%E7%83%AD%E7%82%B9)

**+1**3赞

收藏

![](https://p5.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p5.ssl.qhimg.com/t014757b72460d855bf.png)

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

* ##### [ISC.AI 2025创新独角兽沙盒大赛开启，政产学研共举创新势力](/post/id/308810)

  2025-06-23 17:47:17
* ##### [与“AI”同行，和ISC.AI共启新篇](/post/id/308800)

  2025-06-23 17:37:20
* ##### [手慢无！ISC.AI 2025 早鸟票100张限时6折，赠泡泡玛特乐园门票](/post/id/308736)

  2025-06-20 18:22:35
* ##### [航空公司向国土安全局出售乘客数据](/post/id/308408)

  2025-06-12 15:39:51
* ##### [美国政府疫苗网站被人工智能生成的内容污损](/post/id/308404)

  2025-06-12 15:36:04
* ##### [美国CISA警告 SinoTrack GPS 跟踪器存在远程控制漏洞](/post/id/308398)

  2025-06-12 15:15:38
* ##### [安全行动： 国际刑警组织在打击网络犯罪的重大行动中摧毁了 20,000 多个恶意 IP](/post/id/308395)

  2025-06-12 14:43:06

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