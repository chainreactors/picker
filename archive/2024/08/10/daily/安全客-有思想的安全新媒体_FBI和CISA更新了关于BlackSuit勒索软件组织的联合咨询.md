---
title: FBI和CISA更新了关于BlackSuit勒索软件组织的联合咨询
url: https://www.anquanke.com/post/id/298981
source: 安全客-有思想的安全新媒体
date: 2024-08-10
fetch_date: 2025-10-06T17:59:20.547807
---

# FBI和CISA更新了关于BlackSuit勒索软件组织的联合咨询

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

# FBI和CISA更新了关于BlackSuit勒索软件组织的联合咨询

阅读量**39451**

发布时间 : 2024-08-09 14:47:14

**x**

##### 译文声明

本文是翻译文章，文章原作者 Pierluigi Paganini，文章来源：securityaffairs

原文地址：<https://securityaffairs.com/166760/hacking/blacksuit-ransomware-group-advisory.html>

译文仅供参考，具体内容表达以及含义原文为准。

## FBI 和 CISA 发布了一份关于 BlackSuit 勒索软件组织的联合公告，该文件最近于 2024 年 7 月提供了 TTP 和 IOC。

CISA 与 FBI 合作，发布了一份关于 BlackSuit 勒索软件组织的联合公告。该公告包括与 BlackSuit 操作相关的最近和历史上观察到的策略、技术和程序 （TTP） 以及妥协指标 （IOC），该操作重塑了 FBI 调查发现的最新 2024 年 7 月的传统 Royal 勒索软件。BlackSuit 勒索软件已针对各种关键基础设施部门，包括商业设施、医疗保健、政府和制造业。该报告是美国政府开展的 #StopRansomware 倡议的一部分，该公告最初发布于 2023 年 3 月 2 日，已更新两次：

* **2023年11月13日：**该公告已更新，以分享新的皇家 TTP 和国际石油公司。
* **2024 年 8 月 7 日：**该公告已更新，以通知网络防御者将“Royal”勒索软件参与者更名为“BlackSuit”。此更新包括与 BlackSuit 勒索软件相关的新 TTP、IOC 和检测方法。“Royal”自始至终都更新为“BlackSuit”，除非提及遗留的皇室活动。将记录更新和新内容。

BlackSuit 攻击者通过多种方法获得对受害者网络的初步访问权限，包括网络钓鱼活动、远程桌面协议 （RDP）（在大约 13.3% 的事件中使用）、利用面向公众的应用程序中的漏洞以及使用访问代理提供的初始访问权限，并从窃取者日志中收集 VPN 凭据。

从历史上看，人们观察到皇家参与者利用 Secure Shell （SSH） 客户端、PuTTY、OpenSSH 和 MobaXterm 进行 C2 通信。`Chisel`

该组织使用 SharpShares 和 SoftPerfect NetWorx 来绘制受害者网络。他们威胁行为者还使用 Mimikatz 和 Nirsoft 工具来窃取凭据和获取密码。此外，他们经常部署 PowerTool 和 GMER 等工具来终止系统进程。

该组织使用后利用工具（如 Cobalt Strike）和恶意软件（如 Ursnif）泄露从受害者网络窃取的数据。

BlackSuit 演员通常要求 100 万美元至 1000 万美元不等的赎金，以比特币支付，并且集体寻求超过 5 亿美元，最高个人要求达到 6000 万美元。他们愿意协商付款金额，这些金额未在最初的赎金票据中指定，而是通过加密后提供的 .onion URL 进行讨论。最近，来自 BlackSuit 演员的直接通信（例如电话或电子邮件）有所增加。像其他团体一样，如果不支付赎金，该团伙会使用 Tor 泄漏站点发布受害者数据。

*“FBI 和 CISA 鼓励组织实施本 CSA 的缓解部分中的建议，以减少勒索软件事件的可能性和影响，”该报告总结道，该报告还提供了妥协指标 （IoC）。*

本文翻译自securityaffairs [原文链接](https://securityaffairs.com/166760/hacking/blacksuit-ransomware-group-advisory.html)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/298981](/post/id/298981)

安全KER - 有思想的安全新媒体

本文转载自: [securityaffairs](https://securityaffairs.com/166760/hacking/blacksuit-ransomware-group-advisory.html)

如若转载,请注明出处： <https://securityaffairs.com/166760/hacking/blacksuit-ransomware-group-advisory.html>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [行业资讯](/tag/%E8%A1%8C%E4%B8%9A%E8%B5%84%E8%AE%AF)

**+1**0赞

收藏

![](https://p2.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p5.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p2.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=170338)

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

* [FBI 和 CISA 发布了一份关于 BlackSuit 勒索软件组织的联合公告，该文件最近于 2024 年 7 月提供了 TTP 和 IOC。](#h2-0)

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