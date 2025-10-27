---
title: 挪威国家网络安全中心建议放弃 SSLVPN 和 WebVPN
url: https://www.anquanke.com/post/id/296604
source: 安全客-有思想的安全新媒体
date: 2024-05-21
fetch_date: 2025-10-06T16:49:10.881367
---

# 挪威国家网络安全中心建议放弃 SSLVPN 和 WebVPN

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

# 挪威国家网络安全中心建议放弃 SSLVPN 和 WebVPN

阅读量**75281**

发布时间 : 2024-05-20 10:52:57

**x**

##### 译文声明

本文是翻译文章

原文地址：<https://thecyberexpress.com/replacement-of-sslvpn-and-webvpn/>

译文仅供参考，具体内容表达以及含义原文为准。

挪威国家网络安全中心 (NCSC) 发布了一项建议，建议各组织使用更安全的替代方案替换 SSLVPN 和 WebVPN 解决方案，因为过去多次利用边缘网络设备中的漏洞，导致攻击者能够破坏企业网络。

国家网络安全中心（NCSC）是挪威安全局的一个分支机构，作为挪威的主要联络机构，负责协调国家预防、检测和应对网络攻击的工作，并提供战略指导和技术支持，以加强网络安全国家网络安全总体态势。这包括进行风险评估、传播威胁情报以及在公共和私营部门推广最佳实践。

NCSC 的指南旨在通过倡导过渡到更强大、更安全的远程访问协议来增强组织（特别是关键基础设施部门内的组织）的安全态势。

用安全替代方案替代 SSLVPN 和 WebVPN
NCSC 的建议基于这样的认识：SSL VPN 和 WebVPN 虽然通过 SSL/TLS 协议通过互联网提供安全远程访问，但由于固有的漏洞而多次成为攻击目标。

这些解决方案创建了一个“加密隧道”来保护用户设备和VPN服务器之间的连接。然而，恶意行为者利用这些漏洞导致 NCSC 建议组织迁移到具有 Internet 密钥交换 (IKEv2) 的 Internet 协议安全 (IPsec)。

带有 IKEv2 的 IPsec 是 NCSC 推荐的安全远程访问替代方案。该协议使用定期刷新的密钥来加密和验证每个数据包。尽管承认没有任何协议完全没有缺陷，但 NCSC 认为，带有 IKEv2 的 IPsec 显着减少了安全远程访问事件的攻击面，特别是因为与 SSLVPN 相比，它对配置错误的容忍度较低。

NCSC 强调立即启动过渡进程的重要性。鼓励受《安全法》约束或被归类为关键基础设施的组织在 2024 年底之前完成过渡，并敦促所有其他组织在 2025 年之前完成过渡。

采用 IPsec 而非其他协议的建议并非挪威独有。包括美国和英国在内的其他国家也认可了类似的指导方针，强调了全球对 IPsec 与 IKEv2 提供的增强安全性的共识。

作为一项预防措施，NCSC 还建议在无法实施 IPsec 连接的地方使用移动或移动宽带 5G 作为替代方案。

建议遵循有关利用的早期通知
上个月，挪威国家网络安全中心发布了一份关于针对 SSLVPN 产品的针对性攻击活动的通知，其中攻击者利用了用于为关键基础设施供电的 Cisco ASA VPN 中的多个零日漏洞。该活动自 2023 年 11 月起就开始观察。

该通知主要针对关键基础设施企业，警告称，虽然该活动的进入向量未知，但至少存在一个或多个零日漏洞，可能允许外部攻击者在某些条件下绕过身份验证、入侵设备并授予自己管理权限特权。

该通知分享了几项防范攻击的建议，例如阻止对匿名服务（VPN 提供商和 Tor 出口节点）和 VPS 提供商等不安全基础设施的服务的访问。思科发布了重要的安全更新来解决这些漏洞。

先前的通知还建议企业从 SSLVPN/无客户端 VPN 产品类别切换到采用 IKEv2 的 IPsec，因为此类 VPN 产品中存在严重漏洞，无论 VPN 提供商如何。 NCSC 建议需要帮助的企业联系其所在部门的 CERT 或 MSSP。

本文翻译自 [原文链接](https://thecyberexpress.com/replacement-of-sslvpn-and-webvpn/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/296604](/post/id/296604)

安全KER - 有思想的安全新媒体

本文转载自:

如若转载,请注明出处： <https://thecyberexpress.com/replacement-of-sslvpn-and-webvpn/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [行业资讯](/tag/%E8%A1%8C%E4%B8%9A%E8%B5%84%E8%AE%AF)

**+1**2赞

收藏

![](https://p2.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p2.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p2.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=170061)

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