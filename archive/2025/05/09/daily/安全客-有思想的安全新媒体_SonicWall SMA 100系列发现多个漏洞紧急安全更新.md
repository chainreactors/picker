---
title: SonicWall SMA 100系列发现多个漏洞紧急安全更新
url: https://www.anquanke.com/post/id/307211
source: 安全客-有思想的安全新媒体
date: 2025-05-09
fetch_date: 2025-10-06T22:23:33.039053
---

# SonicWall SMA 100系列发现多个漏洞紧急安全更新

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

# SonicWall SMA 100系列发现多个漏洞紧急安全更新

阅读量**83567**

发布时间 : 2025-05-08 16:04:51

**x**

##### 译文声明

本文是翻译文章，文章原作者 Ddos，文章来源：securityonline

原文地址：<https://securityonline.info/multi-vulnerabilities-found-in-sonicwall-sma-100-series-prompt-urgent-security-update/>

译文仅供参考，具体内容表达以及含义原文为准。

SonicWall发布了安全公告,详细说明了影响其安全移动访问(SMA)100系列产品的多个漏洞。该咨询强调了三个重要的身份验证后漏洞,这些漏洞可能允许攻击者破坏受影响的系统。

[vulnerabilities](https://securityonline.info/hostedscan-review-proactive-vulnerability-management-for-a-bulletproof-digital-presence/)该咨询概述了以下关键漏洞:

* **CVE-2025-32819:身份验证后SSLVPN用户任意文件删除漏洞。**此漏洞允许具有 SSLVPN 用户权限的远程身份验证攻击者绕过路径遍历检查并删除任意文件。这可能导致重新启动到工厂默认设置,导致重大中断。此漏洞的CVSS评分为8.8,表明严重程度很高
* **[vulnerability](https://securityonline.info/pentest-tools-com-review-your-all-in-one-platform-for-streamlined-penetration-testing-and-vulnerability-management/)CVE-2025-32820:身份验证后SSLVPN用户路径遍历漏洞。**此漏洞使具有 SSLVPN 用户权限的远程身份验证攻击者能够注入路径遍历序列,使 SMA 设备上的任何目录都可写。[此漏洞的](https://securityonline.info/pentest-tools-com-review-your-all-in-one-platform-for-streamlined-penetration-testing-and-vulnerability-management/) CVSS 评分为 8.3。
* **CVE-2025-32821:身份验证后SSLVPN管理远程命令注入漏洞。**此漏洞允许具有 SSLVPN 管理权限的远程身份验证攻击者注入 shell 命令参数以在设备上上传文件。此漏洞的 CVSS 评分为 6.7。

[vulnerabilities](https://securityonline.info/hostedscan-review-proactive-vulnerability-management-for-a-bulletproof-digital-presence/)这些漏洞影响以下 SonicWall SMA 100 系列产品:SMA 200、210、400、410 和 500v,特别是那些运行版本 10.2.11-75sv 和更早版本。

[需要注意的是](https://psirt.global.sonicwall.com/vuln-detail/SNWLID-2025-0011)*,“SonicWall SSL VPN SMA1000系列产品不受这些漏洞的影响。*

SonicWall强烈建议受影响的SMA 100系列产品的用户升级到固定版本,以解决这些漏洞。固定版本为10.2.1.15-81sv及更高。

除了升级之外,SonicWall 还建议将以下解决方法作为安全措施:

* + **启用多因素身份验证(MFA**):SonicWall强调“MFA具有防止凭证盗窃的宝贵保护,并且是良好安全态势的关键衡量标准。该咨询进一步澄清了“无论MFA是直接在设备上还是在组织中的目录服务上启用的,它都是有效的。
  + **在 SMA100 上启用 WAF。**
  + **重置密码:** 重置可能通过 Web 界面登录设备的任何用户的密码。

本文翻译自securityonline [原文链接](https://securityonline.info/multi-vulnerabilities-found-in-sonicwall-sma-100-series-prompt-urgent-security-update/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/307211](/post/id/307211)

安全KER - 有思想的安全新媒体

本文转载自: [securityonline](https://securityonline.info/multi-vulnerabilities-found-in-sonicwall-sma-100-series-prompt-urgent-security-update/)

如若转载,请注明出处： <https://securityonline.info/multi-vulnerabilities-found-in-sonicwall-sma-100-series-prompt-urgent-security-update/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [安全资讯](/tag/%E5%AE%89%E5%85%A8%E8%B5%84%E8%AE%AF)

**+1**2赞

收藏

![](https://p3.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p1.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p3.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=170061)

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