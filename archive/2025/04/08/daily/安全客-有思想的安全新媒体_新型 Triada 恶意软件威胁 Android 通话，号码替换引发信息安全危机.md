---
title: 新型 Triada 恶意软件威胁 Android 通话，号码替换引发信息安全危机
url: https://www.anquanke.com/post/id/306245
source: 安全客-有思想的安全新媒体
date: 2025-04-08
fetch_date: 2025-10-06T22:02:44.172813
---

# 新型 Triada 恶意软件威胁 Android 通话，号码替换引发信息安全危机

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

# 新型 Triada 恶意软件威胁 Android 通话，号码替换引发信息安全危机

阅读量**247318**

发布时间 : 2025-04-07 11:26:13

**x**

##### 译文声明

本文是翻译文章，文章原作者 Tushar Subhra Dutta，文章来源：cybersecuritynews

原文地址：<https://cybersecuritynews.com/new-triada-malware-attacking-android-devices/>

译文仅供参考，具体内容表达以及含义原文为准。

Triada 恶意软件家族出现了一种复杂的新变种，其目标瞄准 Android 设备，具备拦截和修改拨出电话的能力。

在拨打电话时，这种恶意软件会悄然用欺诈性号码替换掉合法的电话号码，将用户的通话重定向到收费高昂的号码上，或者能够窃听敏感的通话内容。

该恶意软件在后台秘密运行，使得大多数用户完全没有意识到自己的通话正在被操控。

初始感染通常通过非官方应用商店和受感染的应用程序发生，这些应用程序在安装时请求过多的权限。

一旦安装成功，该恶意软件就会利用权限提升漏洞获取系统级别的访问权限，从而能够监控和修改 Android 系统的电话子系统。

攻击者在设计这种攻击手段时展现出了相当高的技术水平。

卡巴斯基的研究人员在调查了电信运营商报告的不异常呼叫重定向模式后，发现了这一威胁。

他们的分析显示，该恶意软件使用了一种前所未见的技术来挂钩Android拨号器框架，这标志着移动设备威胁能力有了重大的发展变化。

在东欧，已有数千台设备遭到了感染，而且感染情况正逐渐蔓延到西欧和北美。

因欺诈性的高额收费电话造成的经济损失估计已超过 200 万美元，此外，在被拦截的商务通话中，还存在敏感信息被泄露的额外风险。

### ****感染机制分析****

其感染机制依赖于通过将恶意代码注入拨号器进程来利用 Android 电话服务。

@Overridepublic Boolean onOutgoingCall(String number, Intent intent) {

String modifiedNumber = checkAndReplaceNumber(number);

intent.putExtra(“android.intent.extra.PHONE\_NUMBER”, modifiedNumber);

return true;}

当用户拨打电话时，恶意软件会拦截拨出的号码，并将其与一个由远程控制的目标号码及其替换号码的数据库进行比对。

这种技术使得攻击者能够有选择地针对特定的组织或个人，同时通过随机抽样来避免被检测到。

卡巴斯基公司建议用户只从授权经销商处购买智能手机，并部署如卡巴斯基Android版本等安全解决方案来检测此类威胁。

随着 Triada 恶意软件能力的不断演变，它一直提醒着人们，移动生态系统中存在着供应链方面的漏洞。

本文翻译自cybersecuritynews [原文链接](https://cybersecuritynews.com/new-triada-malware-attacking-android-devices/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/306245](/post/id/306245)

安全KER - 有思想的安全新媒体

本文转载自: [cybersecuritynews](https://cybersecuritynews.com/new-triada-malware-attacking-android-devices/)

如若转载,请注明出处： <https://cybersecuritynews.com/new-triada-malware-attacking-android-devices/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [恶意软件](/tag/%E6%81%B6%E6%84%8F%E8%BD%AF%E4%BB%B6)

**+1**2赞

收藏

![](https://p4.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p2.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p4.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=175868)

[安全客](/member.html?memberId=175868)

这个人太懒了，签名都懒得写一个

* 文章
* **376**

* 粉丝
* **1**

### TA的文章

* ##### [mavinject.exe 遭利用，黑客绕过安全防线入侵系统](/post/id/306961)

  2025-04-28 10:48:18
* ##### [Docker 惊现新型加密挖矿攻击，借 Teneo 平台开辟恶意获利新路径](/post/id/306959)

  2025-04-28 10:39:59
* ##### [Cloudflare 隧道遭滥用，恶意 RAT 传播威胁加剧](/post/id/306957)

  2025-04-28 10:34:35
* ##### [xrpl.js 库遭供应链攻击，超 290 万次下载用户私钥成窃取目标](/post/id/306953)

  2025-04-28 10:29:02
* ##### [恶意后门借 ViPNet 更新渗透，俄罗斯多行业数据安全拉响警报](/post/id/306951)

  2025-04-28 10:22:13

### 相关文章

* ##### [InsydeUEFI 漏洞 (CVE-2025-4275)： 安全启动绕过允许 Rootkits 和无法检测的恶意软件](/post/id/308341)

  2025-06-11 16:00:03
* ##### [假冒验证码基础架构 HelloTDS 使数百万设备感染恶意软件](/post/id/308293)

  2025-06-10 13:21:16
* ##### [威胁行为者针对 Gluestack 软件包发起供应链攻击，每周有超过 95 万次的下载面临风险](/post/id/308258)

  2025-06-09 17:25:59
* ##### [ViperSoftX 不断进化： 新的 PowerShell 恶意软件具有隐蔽性和持久性](/post/id/308164)

  2025-06-05 13:29:03
* ##### [Lumma 窃取者恶意软件卷土重来，挑战全球打击行动](/post/id/308100)

  2025-06-04 15:42:31
* ##### [DragonForce 勒索软件集团利用定制负载和全球勒索活动攻击英国零售商](/post/id/307089)

  2025-05-06 14:34:45
* ##### [勒索软件对制造业的威胁日益加剧](/post/id/307053)

  2025-04-30 14:12:31

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