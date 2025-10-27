---
title: 新型 SideWinder 网络攻击以多国海事设施为目标
url: https://www.anquanke.com/post/id/298602
source: 安全客-有思想的安全新媒体
date: 2024-08-01
fetch_date: 2025-10-06T18:00:02.155514
---

# 新型 SideWinder 网络攻击以多国海事设施为目标

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

# 新型 SideWinder 网络攻击以多国海事设施为目标

阅读量**71989**

发布时间 : 2024-07-31 11:23:33

**x**

##### 译文声明

本文是翻译文章，文章原作者 Ravie Lakshmanan，文章来源：The Hacker News

原文地址：<https://thehackernews.com/2024/07/new-sidewinder-cyber-attacks-target.html>

译文仅供参考，具体内容表达以及含义原文为准。

被称为 SideWinder 的民族国家威胁行为者被归咎于针对印度洋和地中海港口和海上设施的新网络间谍活动。

发现这一活动的黑莓研究和情报团队表示，鱼叉式网络钓鱼活动的目标包括巴基斯坦、埃及、斯里兰卡、孟加拉国、缅甸、尼泊尔和马尔代夫等国家。

SideWinder，也被称为 APT-C-17、Baby Elephant、Hardcore Nationalist、Rattlesnake 和 Razor Tiger，被评估为与印度有关联。它自 2012 年以来一直在运营，经常利用鱼叉式网络钓鱼作为载体来提供触发攻击链的恶意有效载荷。

这家加拿大网络安全公司在上周发表的一份分析报告中表示：“SideWinder利用电子邮件鱼叉式网络钓鱼、文档利用和DLL侧载技术，试图避免检测并提供有针对性的植入物。

最新的一组攻击采用与性骚扰、员工解雇和减薪相关的诱饵，以对接收者的情绪状态产生负面影响，并诱使他们打开诱杀装置 Microsoft Word 文档。

一旦诱饵文件被打开，它就会利用一个已知的安全漏洞（CVE-2017-0199）与一个伪装成巴基斯坦港口和航运总局的恶意域建立联系（“reports.dgps-govtpk[.]com“） 检索 RTF 文件。

反过来，RTF 文档下载了一个利用 CVE-2017-11882 的文档，CVE-2017-11882 是 Microsoft Office 公式编辑器中另一个已有数年历史的安全漏洞，目的是执行负责启动 JavaScript 代码的 shellcode，但前提是确保受感染的系统是合法的并且威胁参与者感兴趣。

目前尚不清楚JavaScript恶意软件提供了什么，尽管最终目标可能是根据SideWinder先前发起的活动收集情报。

“SideWinder威胁行为者继续改善其基础设施，以针对新地区的受害者，”黑莓表示。“其网络基础设施和交付有效载荷的稳步发展表明，在可预见的未来，SideWinder将继续其攻击。”

本文翻译自The Hacker News [原文链接](https://thehackernews.com/2024/07/new-sidewinder-cyber-attacks-target.html)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/298602](/post/id/298602)

安全KER - 有思想的安全新媒体

本文转载自: [The Hacker News](https://thehackernews.com/2024/07/new-sidewinder-cyber-attacks-target.html)

如若转载,请注明出处： <https://thehackernews.com/2024/07/new-sidewinder-cyber-attacks-target.html>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [网络攻击](/tag/%E7%BD%91%E7%BB%9C%E6%94%BB%E5%87%BB)
* [安全热点](/tag/%E5%AE%89%E5%85%A8%E7%83%AD%E7%82%B9)

**+1**0赞

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