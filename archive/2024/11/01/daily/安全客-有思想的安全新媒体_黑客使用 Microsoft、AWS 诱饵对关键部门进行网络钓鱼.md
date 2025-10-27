---
title: 黑客使用 Microsoft、AWS 诱饵对关键部门进行网络钓鱼
url: https://www.anquanke.com/post/id/301438
source: 安全客-有思想的安全新媒体
date: 2024-11-01
fetch_date: 2025-10-06T19:15:12.695486
---

# 黑客使用 Microsoft、AWS 诱饵对关键部门进行网络钓鱼

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

# 黑客使用 Microsoft、AWS 诱饵对关键部门进行网络钓鱼

阅读量**60157**

发布时间 : 2024-10-31 10:53:19

**x**

##### 译文声明

本文是翻译文章，文章原作者 Waqas，文章来源：hackread

原文地址：<https://hackread.com/russian-cozy-bear-hackers-phish-microsoft-aws-lures/>

译文仅供参考，具体内容表达以及含义原文为准。

**黑客 Cozy Bear 正在针对全球 100 多个组织开展新的网络钓鱼活动。这种复杂的攻击使用伪装成合法文档的签名 RDP 文件来获取远程访问权限并窃取敏感数据。了解如何保护自己和组织免受这种威胁。**

微软透露，威胁行为者 Cozy Bear（或 APT29、UNC2452 和 Midnight Blizzard）针对全球 100 多个组织发起了新的网络钓鱼活动。

该活动自 2024 年 10 月 22 日开始，涉及针对性极强的电子邮件，旨在诱骗用户打开恶意文件，最终让攻击者获取敏感信息。

攻击者主要针对政府、国防、学术界和非政府组织等关键部门的组织。这与 “舒适熊 ”之前针对掌握有价值情报的实体的模式一致。

**这次有什么新变化？**

Cozy Bear 使用了一种前所未见的方法，涉及已签名的远程桌面协议（RDP）配置文件。这些看似无害的文件会作为钓鱼邮件的附件发送，通常会伪装成与微软、亚马逊网络服务（AWS）和零信任概念有关的诱饵。这些电子邮件的编排非常复杂，甚至会冒充微软员工以提高可信度。

**它是如何运作的？**

根据微软在发布前与 Hackread.com 共享的博文，当用户打开恶意 RDP 文件时，会与 Cozy Bear 控制的服务器建立连接。

通过这种连接，攻击者可以访问受害者设备上的各种资源，包括文件、连接的外设、剪贴板数据，甚至是身份验证功能。攻击者可以利用这种访问权限安装恶意软件、窃取敏感数据，甚至在 RDP 会话关闭后仍能保持持续访问权限。

**有什么风险？**

攻击成功的潜在后果非常严重。Cozy Bear 可能会获取政府机密信息、知识产权和属于不同组织的敏感数据。被入侵的设备还可能被用作进一步攻击的发射台，有可能将感染扩散到其他连接的系统。

![Russian Cozy Bear Hackers Phish Critical Sectors with Microsoft, AWS Lures]()
总部位于加利福尼亚州普莱森顿的 SlashNext Email Security+ 公司首席执行官帕特里克-哈里斯（Patrick Harr）对最近的事态发展发表了评论，并警告企业注意日益复杂的网络钓鱼攻击。

“这次攻击再次凸显了网络钓鱼仍然是对企业最危险的威胁，这就是为什么企业不仅要持续培训用户，还必须在电子邮件、协作和消息应用程序中直接采用人工智能检测和网络钓鱼沙箱来检测恶意链接和文件，”Patrick 建议说。

“这些新的复杂攻击（其中许多是人工智能生成的）可以躲过当前的安全电子邮件网关（SEG），甚至是 Office 版的 Microsoft Defender。企业防御的唯一方法就是利用人工智能在成功入侵之前阻止这些攻击。”

微软与 CERT-UA 和亚马逊已经确认了这一正在进行的活动，并正在努力通知受影响的客户。网络安全专家敦促企业和个人提高警惕，尤其是在处理包含附件或远程访问请求的电子邮件时。

此外，启用多因素身份验证、使用抗网络钓鱼的身份验证方法以及向用户宣传这些网络钓鱼技术也是减少这种攻击的重要步骤。

本文翻译自hackread [原文链接](https://hackread.com/russian-cozy-bear-hackers-phish-microsoft-aws-lures/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/301438](/post/id/301438)

安全KER - 有思想的安全新媒体

本文转载自: [hackread](https://hackread.com/russian-cozy-bear-hackers-phish-microsoft-aws-lures/)

如若转载,请注明出处： <https://hackread.com/russian-cozy-bear-hackers-phish-microsoft-aws-lures/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [网络攻击](/tag/%E7%BD%91%E7%BB%9C%E6%94%BB%E5%87%BB)

**+1**0赞

收藏

![](https://p0.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p2.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p0.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=170061)

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