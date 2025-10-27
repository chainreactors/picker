---
title: 微软揭露与俄罗斯有关的“GooseEgg”恶意软件
url: https://www.anquanke.com/post/id/295879
source: 安全客-有思想的安全新媒体
date: 2024-04-24
fetch_date: 2025-10-04T12:14:53.509745
---

# 微软揭露与俄罗斯有关的“GooseEgg”恶意软件

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

# 微软揭露与俄罗斯有关的“GooseEgg”恶意软件

阅读量**64926**

发布时间 : 2024-04-23 10:10:10

**x**

##### 译文声明

本文是翻译文章

原文地址：<https://therecord.media/russia-gru-malware-gooseegg-microsoft>

译文仅供参考，具体内容表达以及含义原文为准。

微软的研究人员表示，他们发现了俄罗斯国家资助的黑客用来窃取受感染网络中凭证的恶意工具。

该恶意软件名为 GooseEgg，利用了管理打印过程的 Windows Print Spooler 服务中标记为CVE-2022-38028的漏洞。研究人员表示， GooseEgg 似乎是其追踪的“森林暴雪”组织所独有的，该组织与俄罗斯军事情报机构 GRU 有关联。

根据该报告，Forest Blizzard（也称为 Fancy Bear 和 APT28）至少自 2020 年 6 月起就一直在针对乌克兰、西欧和北美的国家、非政府、教育和交通组织部署恶意软件。

研究人员表示：“在森林暴雪行动中使用 GooseEgg 是一个独特的发现，安全提供商之前从未报道过。”

微软观察到，在获得对目标设备的访问权限后，Forest Blizzard 使用 GooseEgg 来提升网络内的权限。 GooseEgg 本身是一个简单的启动器应用程序，但它允许攻击者执行其他操作，例如远程执行代码、安装后门以及通过受感染的网络横向移动。

该公司于 2022 年修复了 Print Spooler 安全漏洞。“为了组织的安全，我们敦促尚未实施这些修复的客户尽快实施”，微软表示。

除了 CVE-2022-38028 之外，Forest Blizzard 还利用了其他错误，例如CVE-2023-23397，它影响 Windows 设备上所有版本的 Microsoft Outlook 软件。

12 月初，微软警告称，森林暴雪早在 2022 年 4 月起就一直试图利用 Microsoft Outlook 漏洞对 Microsoft Exchange 服务器内的电子邮件帐户进行未经授权的访问。

GRU 黑客通常以战略情报资产为目标，例如美国、欧洲和中东的政府、能源、交通和非政府组织。

微软还观察到森林暴雪的目标是媒体组织、信息技术公司、体育组织和教育机构。

本文翻译自 [原文链接](https://therecord.media/russia-gru-malware-gooseegg-microsoft)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/295879](/post/id/295879)

安全KER - 有思想的安全新媒体

本文转载自:

如若转载,请注明出处： <https://therecord.media/russia-gru-malware-gooseegg-microsoft>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

**+1**4赞

收藏

![](https://p4.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p4.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p4.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=170338)

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