---
title: 警惕Anubis：高级勒索软件瞄准医疗保健及其他领域
url: https://www.anquanke.com/post/id/304839
source: 安全客-有思想的安全新媒体
date: 2025-03-01
fetch_date: 2025-10-06T21:55:53.072600
---

# 警惕Anubis：高级勒索软件瞄准医疗保健及其他领域

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

# 警惕Anubis：高级勒索软件瞄准医疗保健及其他领域

阅读量**90701**

|评论**1**

发布时间 : 2025-02-28 11:05:13

**x**

##### 译文声明

本文是翻译文章，文章原作者 do son，文章来源：securityonline

原文地址：<https://securityonline.info/beware-of-anubis-advanced-ransomware-targets-healthcare-and-beyond/>

译文仅供参考，具体内容表达以及含义原文为准。

![Anubis ransomware]()

一个名为 Anubis的新型勒索软件组织已经出现，该组织采用双重勒索策略，并在勒索软件即服务（RaaS）模式下开展活动。根据 KELA 的一份报告，这个组织至少从 2024 年 11 月起就开始活跃，在 RAMP 和 XSS 等网络犯罪论坛上都能发现他们的踪迹。

2024 年 11 月 13 日，一名受害者报告了一起网络安全事件，表明该组织在 2024 年 12 月正式 “亮相” 之前就已经在实施攻击了，Anubis也因此首次受到关注。从那以后，Anubis扩大了其业务范围，向网络犯罪分子提供了多种附属项目，包括：

1.Anubis勒索软件（分成比例 80/20）—— 一种经典的勒索软件即服务模式，附属成员可获得赎金支付的 80%。

2.数据勒索（分成比例 60/40）—— 通过威胁公开被盗数据来获利。

3.访问权限变现（分成比例 50/50）—— 将企业访问凭证出售给勒索软件操作者。

根据 KELA 的报告，Anubis勒索软件具备先进的功能，包括：

1.加密算法：使用 ChaCha+ECIES 加密算法。

2.跨平台攻击目标：影响 Windows、Linux、网络附加存储（NAS）和 ESXi 等环境。

3.权限提升：获取 “NT AUTHORITY\SYSTEM” 权限。

4.横向移动：可在不同域之间自我传播。

5.管理界面：通过基于网络的面板进行控制。

这些特点表明，Anubis并非业余组织的行为，而是一个高度结构化的勒索软件服务组织。

除了基于加密的攻击手段外，Anubis还采用了复杂的勒索机制，包括：

1.调查性新闻手法：

（1）根据被盗取的企业数据撰写 “调查性文章”。

（2）将文章发布在一个隐藏的、设有密码保护的页面上。

（3）通知受影响的监管机构（如GDPR、HHS、ICO等）以增加压力。

2.谈判与威胁：

（1）受害者会接到直接电话，被告知遭受了攻击。

（2）如果他们拒绝支付赎金，所有被盗取的数据将被公开泄露。

Anubis已经宣称攻击了来自多个行业（包括医疗保健和建筑行业）的四名受害者：

1.Pound Road Medical Centre（PRMC，澳大利亚）——2024 年 11 月 13 日报告了一起数据泄露事件，涉及医疗记录和澳大利亚医疗保险信息。

2.Summit Home Health（加拿大）——2024 年 12 月 29 日，Anubis免费泄露了从该机构盗取的医疗数据。

3.Comercializadora S&E Perú—— 一家秘鲁建筑公司，其数据在 2024 年 12 月被泄露。

4.一家未透露名称的美国工程公司 —— 最新的受害者，于 2025 年 2 月 25 日被曝光。

值得注意的是，四名受害者中有两名来自医疗保健行业，这凸显了Anubis可能对关键行业的关注。

KELA 的分析表明，基于以下几点，Anubis的操作者可能是其他勒索软件组织的前附属成员：

1.结构完善的勒索方法。

2.在勒索软件开发方面的技术成熟度。

3.使用详细的调查式曝光受害者的策略。

该组织在俄语网络犯罪论坛上活动，这进一步支持了Anubis可能与之前的勒索软件犯罪集团存在关联的理论。

本文翻译自securityonline [原文链接](https://securityonline.info/beware-of-anubis-advanced-ransomware-targets-healthcare-and-beyond/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/304839](/post/id/304839)

安全KER - 有思想的安全新媒体

本文转载自: [securityonline](https://securityonline.info/beware-of-anubis-advanced-ransomware-targets-healthcare-and-beyond/)

如若转载,请注明出处： <https://securityonline.info/beware-of-anubis-advanced-ransomware-targets-healthcare-and-beyond/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [网络攻击](/tag/%E7%BD%91%E7%BB%9C%E6%94%BB%E5%87%BB)

**+1**2赞

收藏

![](https://p5.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p0.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p5.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=175868)

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