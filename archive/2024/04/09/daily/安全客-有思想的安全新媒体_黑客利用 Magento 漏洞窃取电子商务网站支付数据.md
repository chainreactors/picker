---
title: 黑客利用 Magento 漏洞窃取电子商务网站支付数据
url: https://www.anquanke.com/post/id/295351
source: 安全客-有思想的安全新媒体
date: 2024-04-09
fetch_date: 2025-10-04T12:15:13.636997
---

# 黑客利用 Magento 漏洞窃取电子商务网站支付数据

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

# 黑客利用 Magento 漏洞窃取电子商务网站支付数据

阅读量**65697**

发布时间 : 2024-04-08 10:33:05

**x**

##### 译文声明

本文是翻译文章

原文地址：<https://thehackernews.com/2024/04/hackers-exploit-magento-bug-to-steal.html>

译文仅供参考，具体内容表达以及含义原文为准。

威胁行为者被发现利用 Magento 的一个严重缺陷向电子商务网站注入持久后门。

该攻击利用了CVE-2024-20720（CVSS 评分：9.1），Adobe 将其描述为“特殊元素的不当中和”案例，可能为任意代码执行铺平道路。

该公司在 2024 年 2 月 13 日发布的安全更新中解决了这个问题。

Sansec 表示，它在数据库中发现了一个“精心设计的布局模板”，该模板被用来自动注入恶意代码以执行任意命令。

该公司表示：“攻击者将 Magento 布局解析器与 beberlei/assert 包（默认安装）结合起来执行系统命令。 ”

“由于布局块与结帐车相关联，因此每当请求 <store>/checkout/cart 时都会执行此命令。”

有问题的命令是sed，它用于插入一个代码执行后门，然后负责提供 Stripe支付浏览器以捕获财务信息并将其泄露到另一个受感染的 Magento 商店。

这一进展正值俄罗斯政府对 6 人提出指控，指控他们至少自 2017 年底以来使用 skimmer 恶意软件窃取外国电子商务商店的信用卡和支付信息。

嫌疑人是丹尼斯·普里马琴科、亚历山大·阿塞耶夫、亚历山大·巴索夫、德米特里·科尔帕科夫、弗拉迪斯拉夫·帕图克和安东·托尔马乔夫。 《未来新闻记录》援引法庭文件报道称，逮捕行动是一年前进行的。

俄罗斯联邦总检察长办公室表示：“结果，该黑客组织成员非法掌握了近 16 万张外国公民支付卡的信息，然后通过影子互联网网站出售这些信息。”

本文翻译自 [原文链接](https://thehackernews.com/2024/04/hackers-exploit-magento-bug-to-steal.html)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/295351](/post/id/295351)

安全KER - 有思想的安全新媒体

本文转载自:

如若转载,请注明出处： <https://thehackernews.com/2024/04/hackers-exploit-magento-bug-to-steal.html>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [网络攻击](/tag/%E7%BD%91%E7%BB%9C%E6%94%BB%E5%87%BB)

**+1**2赞

收藏

![](https://p3.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p5.ssl.qhimg.com/t014757b72460d855bf.png)

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