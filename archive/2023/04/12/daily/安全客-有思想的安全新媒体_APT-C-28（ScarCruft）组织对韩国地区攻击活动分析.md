---
title: APT-C-28（ScarCruft）组织对韩国地区攻击活动分析
url: https://www.anquanke.com/post/id/288238
source: 安全客-有思想的安全新媒体
date: 2023-04-12
fetch_date: 2025-10-04T11:29:08.223585
---

# APT-C-28（ScarCruft）组织对韩国地区攻击活动分析

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

# APT-C-28（ScarCruft）组织对韩国地区攻击活动分析

阅读量**119658**

发布时间 : 2023-04-11 22:04:05

**x**

##### 译文声明

本文是翻译文章

译文仅供参考，具体内容表达以及含义原文为准。

APT-C-28（ScarCruft），又称Konni，是一个活跃于朝鲜半岛的APT组织，其主要针对周边国家地区的政府机构进行网络攻击活动，以窃取敏感信息为主。该组织的攻击活动最早可追溯到2014年，近年来该组织活动频繁，不断被数个国内外安全团队持续追踪和披露。

近期360高级威胁研究院多次发现该组织针对韩国的定向攻击行动。在本轮攻击中，该组织前后使用“奖励清单”、“支付”等具有诱导性的文件名，同时使用“加密货币”、“通讯录”等诱饵内容诱导用户执行恶意宏文档。宏文档被允许执行后，会从自身下载或者释放CAB载荷并解压执行其中的脚本文件，进行一系列恶意样本的加载，从而对受害者发动网络攻击，达到窃密目的。

本文翻译自 原文链接。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/288238](/post/id/288238)

安全KER - 有思想的安全新媒体

本文转载自:

如若转载,请注明出处：

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

**+1**0赞

收藏

![](https://p3.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p5.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p3.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=168160)

[安全客](/member.html?memberId=168160)

这个人太懒了，签名都懒得写一个

* 文章
* **200**

* 粉丝
* **0**

### TA的文章

* ##### [强强联合！360高级威胁研究院获评华为“优秀合作伙伴”](/post/id/295149)

  2024-03-29 20:30:15
* ##### [【必读】2024数字安全十大技术趋势预测，不容忽视！](/post/id/292293)

  2023-12-30 21:09:43
* ##### [微软推出 Defender 赏金计划，赏金高达20,000 美元](/post/id/291448)

  2023-11-22 10:45:43
* ##### [SiegedSec黑客攻击美国核研究实验室，窃取员工数据](/post/id/291446)

  2023-11-22 10:38:47
* ##### [工信部：关于防范利用Confluence高危漏洞实施勒索攻击的风险提示](/post/id/291442)

  2023-11-21 17:23:55

### 相关文章

* ##### [再添数字政府新名片！深圳“深治慧”平台入选2025数博会创新案例](/post/id/311777)

  2025-09-02 15:37:49
* ##### [掌握AI+安全双刃剑，ISC训练营助你成为企业疯抢的黄金人才！](/post/id/310525)

  2025-07-24 10:24:57
* ##### [ISC.AI 2025国际人工智能发展高峰论坛：凝聚全球共识，点亮AI未来](/post/id/310510)

  2025-07-24 09:47:17
* ##### [ISC.AI大咖来了——国家网络安全守卫者 周鸿祎](/post/id/310504)

  2025-07-24 09:43:28
* ##### [攻击者在“PoisonSeed”钓鱼攻击中通过降级手段绕过FIDO2多因素认证（MFA）](/post/id/310339)

  2025-07-21 17:41:39
* ##### [掌握AI+安全双刃剑，ISC训练营助你成为企业疯抢的黄金人才！](/post/id/309947)

  2025-07-11 16:10:36
* ##### [报名开启！ISC.AI训练营助力AI与数字安全人才培养](/post/id/309827)

  2025-07-10 17:42:56

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