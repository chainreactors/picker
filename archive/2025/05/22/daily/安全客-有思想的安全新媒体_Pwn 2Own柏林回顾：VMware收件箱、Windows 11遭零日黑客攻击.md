---
title: Pwn 2Own柏林回顾：VMware收件箱、Windows 11遭零日黑客攻击
url: https://www.anquanke.com/post/id/307599
source: 安全客-有思想的安全新媒体
date: 2025-05-22
fetch_date: 2025-10-06T22:26:52.352006
---

# Pwn 2Own柏林回顾：VMware收件箱、Windows 11遭零日黑客攻击

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

# Pwn 2Own柏林回顾：VMware收件箱、Windows 11遭零日黑客攻击

阅读量**78699**

发布时间 : 2025-05-21 15:21:28

**x**

##### 译文声明

本文是翻译文章，文章原作者 Ddos，文章来源：securityonline

原文地址：<https://securityonline.info/pwn2own-berlin-recap-vmware-esxi-windows-11-hacked-with-zero-days/>

译文仅供参考，具体内容表达以及含义原文为准。

![Pwn2Own 获奖者,VMware ESXi 黑客]()

图片来源:Zeroday Initiative

著名的黑客竞赛Pwn2Own 2025柏林最近结束了,网络安全研究人员通过利用各种平台和技术的一系列零日漏洞,获得了总计1,078,750美元的奖金。

在这次精英竞赛中,artificial intelligence参与者将目光投向了人工智能、Web浏览器、虚拟化平台、本地特权升级、服务器、企业应用程序、云原生/容器环境和汽车系统等企业技术。根据竞争规则,所有目标设备都运行最新的操作系统,并应用了最新的安全补丁。

仅在第一天,研究人员就获得了26万美元的奖励。到第二天,又为20个新发现的零日漏洞获得了435,000美元。最后一天,研究人员通过再利用8个零日获得了额外的383,750美元。

在每次成功演示工作漏洞后,供应商将获得一个90天的窗口,以便在漏洞详细信息公开之前发布安全补丁。然而,在涉及难以补救的异常复杂的缺陷的情况下,供应商可能会与研究人员协商延期以延迟披露。

比赛中最高的单一奖励(15万美元)授予STAR Labs的Nguyen Hoang Thach。他通过整数溢出漏洞成功地破坏了VMware的ESXi虚拟机管理程序,Broadcom发布了赏金。

个人支出第二高,流向了Viettel网络安全团队。他们执行了从 Oracle VirtualBox 客户机到主机系统的突破,随后将身份验证旁路与不安全的反序列化漏洞捆绑在一起,以攻击 Microsoft SharePoint。

排在第三位的是反向战术团队,该团队利用VMware虚拟机管理程序中整数溢出和未初始化变量错误的组合来赚取112,000美元。

值得注意的是,在比赛期间,Mozilla [Firefox浏览器中发现了两个0day漏洞。](https://securityonline.info/hostedscan-review-proactive-vulnerability-management-for-a-bulletproof-digital-presence/)作为回应,Mozilla发布了更新来解决这些缺陷,特别是Firefox v138.0.4,Firefox ESR 128.10.1,Firefox ESR 115.23.1和最新版本的Firefox for Android – 解决了CVE-2025-4918和CVE-2025-4919。

本文翻译自securityonline [原文链接](https://securityonline.info/pwn2own-berlin-recap-vmware-esxi-windows-11-hacked-with-zero-days/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/307599](/post/id/307599)

安全KER - 有思想的安全新媒体

本文转载自: [securityonline](https://securityonline.info/pwn2own-berlin-recap-vmware-esxi-windows-11-hacked-with-zero-days/)

如若转载,请注明出处： <https://securityonline.info/pwn2own-berlin-recap-vmware-esxi-windows-11-hacked-with-zero-days/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [安全资讯](/tag/%E5%AE%89%E5%85%A8%E8%B5%84%E8%AE%AF)
* [安全热点](/tag/%E5%AE%89%E5%85%A8%E7%83%AD%E7%82%B9)

**+1**2赞

收藏

![](https://p3.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p5.ssl.qhimg.com/t014757b72460d855bf.png)

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