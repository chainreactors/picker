---
title: 黑客利用伪造的 ESET 电子邮件向以色列公司发送 Wiper 恶意软件
url: https://www.anquanke.com/post/id/301104
source: 安全客-有思想的安全新媒体
date: 2024-10-22
fetch_date: 2025-10-06T18:48:00.522078
---

# 黑客利用伪造的 ESET 电子邮件向以色列公司发送 Wiper 恶意软件

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

# 黑客利用伪造的 ESET 电子邮件向以色列公司发送 Wiper 恶意软件

阅读量**95897**

发布时间 : 2024-10-21 14:04:08

**x**

##### 译文声明

本文是翻译文章，文章原作者 Deeba Ahmed，文章来源：hackread

原文地址：<https://hackread.com/hackers-fake-eset-emails-israeli-wiper-malware/>

译文仅供参考，具体内容表达以及含义原文为准。

**黑客假冒 ESET 针对以色列组织实施网络钓鱼攻击。自称来自 ESET 的恶意邮件发送了Wiper 恶意软件。安全研究员 Kevin Beaumont 揭露了這次攻击。ESET 否认直接入侵，并指出合作伙伴参与其中。**

在最近的一次网络攻击中，黑客冒充网络安全公司 ESET，以以色列组织为目标。攻击者冒充总部位于斯洛伐克的 ESET 发送钓鱼邮件，警告收件人国家支持的黑客正在攻击他们的设备。

邮件中包含一个下载不存在的 “ESET Unleashed 程序 ”的链接，该程序声称可以抵御攻击。点击链接后，会下载一个包含清除器恶意软件的 ZIP 文件，旨在清除受感染设备上的数据。

安全研究员凯文-博蒙特（Kevin Beaumont）发出警报，指出黑客已成功入侵 ESET 的防御系统，并在其服务器上托管恶意文件。这些电子邮件被谷歌标记为危险邮件，但许多收件人可能已经上当受骗。

![Hackers Use Fake ESET Emails to Target Israeli Firms with Wiper Malware]()

黑客利用伪造的 ESET 电子邮件向以色列公司发送 Wiper 恶意软件
这封名为 ESET 高级威胁防御团队的电子邮件和名为 ESET Unleashed 的下载文件包含各种 ESET DLL 和一个名为 setup.exe 的文件，并指向以色列的一个合法组织–www.oref.org.il。如果受害者打开 ZIP 文件并运行恶意软件，它就会删除其设备上的文件和数据。然而，该恶意软件需要一台物理 PC 和时间来激活其破坏能力。

博蒙特在博文中写道：“ESET以色列公司肯定遭到了攻击，这东西是假冒的勒索软件，不管出于什么原因，它都会与以色列新闻网站服务器进行对话。”

ESET 在回应这一事件时承认，他们在以色列的合作伙伴公司 Comsecure 发生了安全事件，但否认他们自己的基础架构被入侵。ESET 在 X（推特）上发表的官方声明如下

“我们知道上周发生了一起影响我们在以色列的合作伙伴公司的安全事件。根据我们的初步调查，一个有限的恶意电子邮件活动在十分钟内被阻止。ESET 技术正在阻止该威胁，我们的客户是安全的。ESET 没有受到威胁，目前正与其合作伙伴密切合作，进一步开展调查，我们将继续监控事态发展。”

该网络钓鱼活动专门针对以色列组织内的网络安全人员，表明攻击者的目的是破坏该国的数字防御。邮件是在 10 月 8 日发送的，也就是哈马斯和其他巴勒斯坦武装组织武装入侵以色列周年纪念日的第二天。ESET 安全论坛上的一名用户很快发现了这封可疑邮件并进行了报告。

攻击者很可能是通过安全漏洞或社交工程技术进入了 Comsecure 的基础设施。然后，他们精心设计了与 ESET 官方风格和品牌极为相似的网络钓鱼电子邮件。

目前尚不清楚该活动背后的具体威胁行为者。不过，他们所使用的策略与亲巴勒斯坦组织 Handala 所使用的策略类似，该组织最近针对以色列的组织发动了雨刷恶意软件和其他网络攻击。网络安全公司 Trellix 将 Handala 的攻击描述为复杂的攻击，并认为可能与伊朗有关。

ESET 的仿冒活动现已被阻止，但它凸显了网络钓鱼攻击的持续威胁，并引发了对 ESET 合作伙伴基础设施安全性和未来攻击可能性的担忧。为防止类似攻击，企业应优先验证信息的真实性，并实施先进的安全措施。

本文翻译自hackread [原文链接](https://hackread.com/hackers-fake-eset-emails-israeli-wiper-malware/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/301104](/post/id/301104)

安全KER - 有思想的安全新媒体

本文转载自: [hackread](https://hackread.com/hackers-fake-eset-emails-israeli-wiper-malware/)

如若转载,请注明出处： <https://hackread.com/hackers-fake-eset-emails-israeli-wiper-malware/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [恶意软件](/tag/%E6%81%B6%E6%84%8F%E8%BD%AF%E4%BB%B6)
* [网络攻击](/tag/%E7%BD%91%E7%BB%9C%E6%94%BB%E5%87%BB)

**+1**0赞

收藏

![](https://p3.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p3.ssl.qhimg.com/t014757b72460d855bf.png)

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

* ##### [Morte僵尸网络被披露：正利用路由器与企业应用漏洞，迅速扩张其“加载器即服务”活动](/post/id/312444)

  2025-09-29 18:04:01
* ##### [Akira勒索软件利用SonicWall VPN账户发起急速入侵](/post/id/312438)

  2025-09-29 18:03:28
* ##### [DarkCloud信息窃取器现新变种：采用VB6混淆技术并新增加密货币钱包窃取功能，威胁显著升级](/post/id/312435)

  2025-09-29 18:02:53
* ##### [TamperedChef恶意软件兴起：欺诈应用利用经过签名的二进制文件与搜索引擎投毒劫持浏览器](/post/id/312432)

  2025-09-29 18:02:25
* ##### [黑客将SVG文件武器化，用于隐秘投递恶意负载](/post/id/312351)

  2025-09-24 16:44:10
* ##### [ShadowV2僵尸网络利用配置错误的AWS Docker容器构建DDoS攻击租用服务](/post/id/312381)

  2025-09-24 16:40:43
* ##### [npm软件包“fezbox”中被发现新型恶意软件，可利用二维码窃取用户凭据](/post/id/312387)

  2025-09-24 16:40:06

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