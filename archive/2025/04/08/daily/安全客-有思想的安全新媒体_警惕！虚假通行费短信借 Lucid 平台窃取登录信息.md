---
title: 警惕！虚假通行费短信借 Lucid 平台窃取登录信息
url: https://www.anquanke.com/post/id/306253
source: 安全客-有思想的安全新媒体
date: 2025-04-08
fetch_date: 2025-10-06T22:02:42.559218
---

# 警惕！虚假通行费短信借 Lucid 平台窃取登录信息

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

# 警惕！虚假通行费短信借 Lucid 平台窃取登录信息

阅读量**54555**

发布时间 : 2025-04-07 14:50:40

**x**

##### 译文声明

本文是翻译文章，文章原作者 Tushar Subhra Dutta，文章来源：cybersecuritynews

原文地址：<https://cybersecuritynews.com/beware-of-fake-unpaid-toll-message-attack/>

译文仅供参考，具体内容表达以及含义原文为准。

近几个月来，一场针对移动用户的欺骗性网络钓鱼活动显著加剧，该活动以虚假的未支付通行费通知为诱饵，已演变成当前最为复杂的基于短信的凭证窃取操作之一。

这种诈骗手段标志着网络钓鱼方法上的一种策略转变，摒弃了传统的冒充包裹投递通知的方式，转而利用人们对所谓驾驶违规行为可能产生的财务担忧来实施诈骗。

安全研究人员已确认，已有数千名受害者在不知不觉中因这一日益猖獗的骗局而交出了自己的登录凭证。

当毫无防备的受害者收到声称他们有未支付的通行费违规款项、需要立即处理的短信时，攻击便开始了。

这些短信使用了急迫的言辞，威胁称如果收件人不迅速回复，将面临巨额罚款，甚至驾照会被吊销。

与传统的网络钓鱼尝试不同，这些短信最初并不包含任何活跃链接，而是指示收件人直接回复短信，这营造出一种虚假的可信度，并绕过了标准的网络钓鱼检测方法。

Censys 的研究人员发现，一旦受害者回复了这些初始短信，攻击者就会立即展开第二阶段的攻击，发送一个链接到设计得极为逼真的网络钓鱼域名。

这些域名极为精准地模仿了官方的通行费征收机构，甚至还根据受害者的所在地融入了当地的视觉元素。

Censys 团队已追踪到了数以万计的这些恶意域名，发现目标受害者遍布多个国家。

这场网络钓鱼活动规模之大，源于其高度有组织的运营结构，攻击者利用了一种基于订阅的模式，得以广泛传播。

支持这些攻击的基础设施展现出了很强的抵御能力，能够有效应对关停企图，一旦有域名被封锁或举报，新的域名会迅速部署到位以取而代之。

其造成的经济影响不仅局限于个人受害者，因为通过这些活动窃取的凭证常常在被盗后的数小时内就会出现在地下市场上售卖。

### ****Lucid 网络钓鱼即服务平台****

这场活动的核心是 “Lucid”，这是一个综合性的 “网络钓鱼即服务”（PhaaS）平台，它为网络犯罪分子提供了启动复杂网络钓鱼活动的一站式解决方案。

该平台使得即使技术水平不高的攻击者也能够生成看起来真实的网络钓鱼域名，以及为特定地区的通行费管理机构量身定制的登录页面。

该服务会根据受害者的 IP 地址进行动态调整，能够针对特定的地理区域进行精准定位，并为 iOS 和 Android 用户进行设备特定的优化。

Lucid 的技术复杂性包括实施验证机制，该机制会阻止来自目标区域之外的 IP 地址的连接，并防止安全研究人员不通过指定的缩短URL而直接访问这些域名。

支付页面仅向指定地理区域内的受害者显示，这进一步增加了安全公司进行检测和分析的难度。

这个平台是类似服务不断增长的生态系统的一部分，其中包括 Lighthouse、Darcula、EvilProxy 和 W3II 等，所有这些服务都旨在让犯罪分子更轻易地具备网络钓鱼能力。

安全分析师指出，这些通行费诈骗活动的成功率约为 5%，远高于传统的电子邮件网络钓鱼攻击，这证明了这种将短信与定制的网络钓鱼域名相结合的多阶段攻击方式的有效性。

随着这种威胁的不断演变，用户应极度谨慎地对待任何意外收到的通行费违规通知短信，通过独立获取的联系方式直接向官方通行费管理机构进行核实，而不要回复未经请求的短信。

虚假的未支付通行费短信攻击标志着网络钓鱼策略的重大演变，它既利用了心理操纵手段，又运用了复杂的技术，从而达到了前所未有的成功率。

本文翻译自cybersecuritynews [原文链接](https://cybersecuritynews.com/beware-of-fake-unpaid-toll-message-attack/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/306253](/post/id/306253)

安全KER - 有思想的安全新媒体

本文转载自: [cybersecuritynews](https://cybersecuritynews.com/beware-of-fake-unpaid-toll-message-attack/)

如若转载,请注明出处： <https://cybersecuritynews.com/beware-of-fake-unpaid-toll-message-attack/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [行业资讯](/tag/%E8%A1%8C%E4%B8%9A%E8%B5%84%E8%AE%AF)

**+1**2赞

收藏

![](https://p0.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p5.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p0.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=175868)

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

* ##### [国庆重保+攻防演练大考在即！360大模型安全服务专项方案筑牢AI防线](/post/id/312460)

  2025-09-29 18:06:17
* ##### [Meta 旨在打造机器人领域的“Android”，为下一代人形AI提供通用平台](/post/id/312454)

  2025-09-29 18:05:34
* ##### [谷歌新规强制要求：所有安卓应用须在2025年11月1日前全面支持16KB页面大小](/post/id/312429)

  2025-09-29 18:01:37
* ##### [“天网杯”纳米AI视频创作赛圆满落幕，ISC.AI学苑推动“教育AI+”新范式](/post/id/312373)

  2025-09-24 16:42:53
* ##### [第三届“天网杯”网络安全大赛收官，夯实网络安全战略人才基石](/post/id/312360)

  2025-09-24 16:42:36
* ##### [WhatsApp 为 iPhone 和 Android 应用支持消息翻译功能](/post/id/312341)

  2025-09-24 16:38:49
* ##### [Microsoft将在威斯康星州打造“世界最强AI数据中心](/post/id/312314)

  2025-09-22 18:13:49

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