---
title: 网络犯罪分子利用Tesla代理和Formbook恶意软件瞄准波兰企业
url: https://www.anquanke.com/post/id/298623
source: 安全客-有思想的安全新媒体
date: 2024-08-01
fetch_date: 2025-10-06T18:00:07.870449
---

# 网络犯罪分子利用Tesla代理和Formbook恶意软件瞄准波兰企业

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

# 网络犯罪分子利用Tesla代理和Formbook恶意软件瞄准波兰企业

阅读量**130617**

发布时间 : 2024-07-31 11:21:02

**x**

##### 译文声明

本文是翻译文章，文章原作者 拉维·拉克什马南，文章来源：The Hacker News

原文地址：<https://thehackernews.com/2024/07/cybercriminals-target-polish-businesses.html>

译文仅供参考，具体内容表达以及含义原文为准。

网络安全研究人员详细介绍了 2024 年 5 月期间针对波兰中小型企业 （SMB） 的广泛网络钓鱼活动，这些活动导致部署了 Agent Tesla、Formbook 和 Remcos RAT 等多个恶意软件家族。

据网络安全公司ESET称，这些活动针对的其他一些地区包括意大利和罗马尼亚。

“攻击者使用以前被入侵的电子邮件帐户和公司服务器，不仅传播恶意电子邮件，而且还托管恶意软件并收集被盗数据，”ESET研究员Jakub Kaloč在今天发布的一份报告中说。

这些活动分布在九波中，以使用名为 DBatLoader（又名 ModiLoader 和 NatsoLoader）的恶意软件加载器来提供最终有效载荷而著称。

这家斯洛伐克网络安全公司表示，这标志着与 2023 年下半年观察到的先前攻击不同，这些攻击利用名为 AceCryptor 的加密器即服务 （CaaS） 来传播 Remcos RAT（又名 Rescoms）。

ESET在2024年3月指出：“在[2023年]下半年，Rescoms成为AceCryptor打包的最普遍的恶意软件家族。“这些尝试中有一半以上发生在波兰，其次是塞尔维亚、西班牙、保加利亚和斯洛伐克。”

攻击的起点是网络钓鱼电子邮件，其中包含带有恶意软件的 RAR 或 ISO 附件，这些附件在打开时会激活一个多步骤过程来下载和启动特洛伊木马。

如果附加了 ISO 文件，它将直接导致 DBatLoader 的执行。另一方面，RAR 存档包含一个混淆的 Windows 批处理脚本，其中包含一个伪装成 PEM 编码的证书吊销列表的 Base64 编码的 ModiLoader 可执行文件。

DBatLoader是一个基于Delphi的下载器，主要用于从Microsoft OneDrive或属于合法公司的受感染服务器下载和启动下一阶段的恶意软件。

无论部署了什么恶意软件，Agent Tesla、Formbook 和 Remcos RAT 都具有窃取敏感信息的能力，使威胁行为者能够“为他们的下一次活动做好准备”。

卡巴斯基透露，由于中小企业缺乏强大的网络安全措施以及有限的资源和专业知识，他们越来越多地成为网络犯罪分子的目标。

“特洛伊木马攻击仍然是最常见的网络威胁，这表明攻击者继续以中小企业为目标，并偏爱恶意软件而不是不需要的软件，”这家俄罗斯安全供应商上个月表示。

“特洛伊木马特别危险，因为它们模仿合法软件，这使得它们更难被发现和预防。它们的多功能性和绕过传统安全措施的能力使它们成为网络攻击者的普遍而有效的工具。

本文翻译自The Hacker News [原文链接](https://thehackernews.com/2024/07/cybercriminals-target-polish-businesses.html)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/298623](/post/id/298623)

安全KER - 有思想的安全新媒体

本文转载自: [The Hacker News](https://thehackernews.com/2024/07/cybercriminals-target-polish-businesses.html)

如若转载,请注明出处： <https://thehackernews.com/2024/07/cybercriminals-target-polish-businesses.html>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [恶意软件](/tag/%E6%81%B6%E6%84%8F%E8%BD%AF%E4%BB%B6)
* [网络安全](/tag/%E7%BD%91%E7%BB%9C%E5%AE%89%E5%85%A8)

**+1**0赞

收藏

![](https://p1.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p0.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p1.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=170338)

[安全客](/member.html?memberId=170338)

这个人太懒了，签名都懒得写一个

* 文章
* **823**

* 粉丝
* **1**

### TA的文章

* ##### [严重的GiveWP漏洞（CVE-2024-8353）影响10万WordPress网站](/post/id/300547)

  2024-09-30 15:03:21
* ##### [Patchwork APT 的 Nexe 后门活动曝光](/post/id/300549)

  2024-09-30 15:03:07
* ##### [用户在一次复杂的钓鱼攻击中损失了价值3200万美元的spWETH](/post/id/300551)

  2024-09-30 15:02:50
* ##### [车牌信息成安全漏洞：起亚汽车远程控制风险揭示联网车辆网络安全问题](/post/id/300553)

  2024-09-30 15:02:09
* ##### [严重SQL注入漏洞影响TI WooCommerce Wishlist插件，超10万WordPress网站面临风险](/post/id/300556)

  2024-09-30 15:01:53

### 相关文章

* ##### [InsydeUEFI 漏洞 (CVE-2025-4275)： 安全启动绕过允许 Rootkits 和无法检测的恶意软件](/post/id/308341)

  2025-06-11 16:00:03
* ##### [假冒验证码基础架构 HelloTDS 使数百万设备感染恶意软件](/post/id/308293)

  2025-06-10 13:21:16
* ##### [威胁行为者针对 Gluestack 软件包发起供应链攻击，每周有超过 95 万次的下载面临风险](/post/id/308258)

  2025-06-09 17:25:59
* ##### [恶意软件攻击 16 个 React Native npm 软件包，100 万次下载面临风险](/post/id/308238)

  2025-06-09 17:01:38
* ##### [ViperSoftX 不断进化： 新的 PowerShell 恶意软件具有隐蔽性和持久性](/post/id/308164)

  2025-06-05 13:29:03
* ##### [阿联酋中央银行要求金融机构放弃短信和 OTP 身份验证](/post/id/308132)

  2025-06-05 12:29:10
* ##### [Lumma 窃取者恶意软件卷土重来，挑战全球打击行动](/post/id/308100)

  2025-06-04 15:42:31

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