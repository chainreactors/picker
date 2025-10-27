---
title: 研究机构Claroty/Team82：医疗保健将长期成为勒索软件攻击的主要目标
url: https://www.anquanke.com/post/id/293919
source: 安全客-有思想的安全新媒体
date: 2024-03-15
fetch_date: 2025-10-04T12:07:50.838834
---

# 研究机构Claroty/Team82：医疗保健将长期成为勒索软件攻击的主要目标

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

# 研究机构Claroty/Team82：医疗保健将长期成为勒索软件攻击的主要目标

阅读量**75516**

发布时间 : 2024-03-14 10:40:42

**x**

##### 译文声明

本文是翻译文章

原文地址：<https://www.securityweek.com/healthcares-ransomware-epidemic-why-cyberattacks-hit-the-medical-sector-with-alarming-frequency/>

译文仅供参考，具体内容表达以及含义原文为准。

医疗保健长期以来一直是勒索软件攻击的主要目标。这不会改变，也不可能改变。Claroty/Team82 的《CPS 安全状况 – 2023 年医疗保健》讨论了原因。

医疗保健是一个关键行业，将大规模使用融合 IT 和 OT 与大量不同的 OT 设备相结合，这些设备依赖于通过 WiFi 提供的 IT 控制，并且对中断的容忍度非常低。该行业非常容易被利用，并且有强烈的动机尽可能快速、无缝地解决敲诈勒索攻击。生命可能取决于它。

根据 FBI 2023 IC3 报告，医疗保健行业去年遭受了 249 起勒索软件攻击，比第二大受攻击的 CNI 行业（关键制造业）多出 31 起，是金融服务遭受攻击的两倍多。

Claroty/Team82 的报告分析了医疗保健 IT 环境的组件，以解释其对攻击的敏感性。它指出，对患者隐私（由 HIPAA 涵盖）的威胁已转变为对患者生命的威胁。

该报告有一些令人担忧的结论。CISA KEV 目录中跟踪的被利用漏洞中有 63%可以在医疗网络上找到。显然，“打补丁”对于医疗保健来说是一个问题，但这并不是一件容易解决的问题：医疗保健领域共有 360 家不同的设备制造商，必须遵守其补丁认证计划。

虽然控制 OT 设备的 IT 设备通常是经常打补丁的 Windows 和 Linux 系统，但这种形式并不适用于大多数 OT 设备。报告称：“相反，漏洞修补通常是本已昂贵的支持合同的附加内容。”

使这个问题变得更加复杂的是获得 FDA 设备认证所需的时间长度。开发补丁并实施该补丁可能需要新的 FDA 认证，但设备的预期寿命可能有限（医疗技术是一个快速发展的领域）。人们自然倾向于通过补偿控制而不是正式修补来尝试缓解问题——古老的 OT 格言“如果它没有坏，就不要修理它，以免损坏它”存在于医疗类固醇中。

由于在不受支持的操作系统上运行的设备数量较多，这一问题变得更加复杂。报告指出：“我们研究中的 14% 的医疗设备运行的是已报废或不受支持的操作系统。” 这些大多是 Windows 的旧版本，但包括 Linux、移动操作系统、Sun Solaris、SunOS 等。更糟糕的是，许多不受支持的 Windows 设备也是不受管理的，并且不属于 Active Directory 域。防御者无法使用域管理来推送更新和新策略或强制执行 ACL。

这些补丁或更新问题的结果是，医疗设备为攻击者提供了丰富的“永久漏洞”来源：制造商已知并修复的漏洞，但客户从未修补过。由于预算限制意味着 HDO 不太可能舍弃旧的并用新的替代，因此这些漏洞就等着被利用。总体而言，很大一部分医疗设备没有端点保护。

![]()自动生成的无端点保护的设备图 描述

HDO OT 的另一个长期存在的问题是设备涉及大量第三方（通过交付而不是供应）。这些患者几乎按照定义对安全性不感兴趣，也不了解。起搏器安装在活动能力极强的人体内（其目的就是让这些人保持活动状态）。数据从起搏器收集，并通过 wifi 或通过患者自己的家用路由器通过互联网转发回 HDO。这是对患者隐私的潜在威胁。输液泵虽然大多只在医院内运行，但长期以来存在漏洞。这是对患者生命的潜在威胁。

针对此类设备的攻击可能会伤害个别患者，但他们并不是攻击者的主要目标——攻击者寻求访问 HDO 网络。作为勒索攻击的一部分，他们可能会从这里破坏所有设备。这些第三方患者可能是一个弱点。

首先，HDO 提供访客网络，为患者提供互联网访问。Claroty/Team82 的研究表明，手术中使用的设备中有 4% 可以通过医院的访客网络进行访问。但其次，患者获得直接访问主要公司网络的密码并不是什么新鲜事。护士的工作通常是职业性的，而不是野心勃勃的——他们的动机是让病人尽可能舒适；患者因访客网络带宽不足而烦恼的问题也可以轻松解决。但所使用的个人设备（通常是笔记本电脑）对于网络管理员来说是未知的，也未经验证。

HDO 防御者面临的问题之一是复杂性。他们面临的几乎所有问题都有安全解决方案，但修补可以修补的内容、减轻无法修补的内容、安装新设备以及提高职业本能可能与安全性截然相反的员工的安全意识等复杂性太复杂，无法保证完整并不断取得成功。

脆弱的网络和快速解决勒索攻击的高动机相结合，解释了勒索软件犯罪分子持续攻击的原因。Recorded Future 的 Dmitry Smilyanets 最近指出Ramp 论坛（2024 年 3 月 3 日）上的一篇帖子，声称来自 BlackCat/Alphv 附属机构，该附属机构攻击了Change Healthcare。该附属公司抱怨 BlackCat/Alphv 拒绝支付其所支付的 2200 万美元赎金中的利润份额。这一说法得到了 BlackCat/Alphv 比特币钱包中 2200 万美元的证据的支持。

或者这可能是BlackCat/Alphv 实施的退出骗局，以便让他们获得第二口樱桃……尽管如此，目前尚未得到 Change Healthcare 证实的暗示是，HDO 悄悄支付了 2200 万美元的赎金以阻止机密数据的泄露泄漏并获取解密密钥。

Claroty/Team82 的论点是，任何保护医疗保健网络中单个设备安全的尝试都应该得到网络分段的支持。报告称：“细分是最重要的战略。” “将连接的医疗设备（患者设备和手术设备）与企业网络隔离。这意味着如果任何特定设备受到损害，攻击者可能会受到限制，并且损害也将受到限制。

本文翻译自 [原文链接](https://www.securityweek.com/healthcares-ransomware-epidemic-why-cyberattacks-hit-the-medical-sector-with-alarming-frequency/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/293919](/post/id/293919)

安全KER - 有思想的安全新媒体

本文转载自:

如若转载,请注明出处： <https://www.securityweek.com/healthcares-ransomware-epidemic-why-cyberattacks-hit-the-medical-sector-with-alarming-frequency/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [行业资讯](/tag/%E8%A1%8C%E4%B8%9A%E8%B5%84%E8%AE%AF)

**+1**3赞

收藏

![](https://p4.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p3.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p4.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=170061)

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