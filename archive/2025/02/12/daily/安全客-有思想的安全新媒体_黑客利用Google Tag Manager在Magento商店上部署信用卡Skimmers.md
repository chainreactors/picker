---
title: 黑客利用Google Tag Manager在Magento商店上部署信用卡Skimmers
url: https://www.anquanke.com/post/id/304109
source: 安全客-有思想的安全新媒体
date: 2025-02-12
fetch_date: 2025-10-06T20:32:32.774692
---

# 黑客利用Google Tag Manager在Magento商店上部署信用卡Skimmers

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

# 黑客利用Google Tag Manager在Magento商店上部署信用卡Skimmers

阅读量**52933**

发布时间 : 2025-02-11 15:01:51

**x**

##### 译文声明

本文是翻译文章，文章原作者 Ravie Lakshmanan，文章来源：TheHackersNews

原文地址：<https://thehackernews.com/2025/02/hackers-exploit-google-tag-manager-to.html>

译文仅供参考，具体内容表达以及含义原文为准。

据观察，威胁行为者一直在利用谷歌标签管理器（Google Tag Manager，简称 GTM）向基于 Magento 的电子商务网站投放信用卡信息窃取恶意软件。

网站安全公司 Sucuri 表示，该代码看似是用于网站分析和广告目的的典型 GTM 及谷歌分析脚本，但其中包含一个经过混淆处理的后门，攻击者可借此获得持续访问权限。

截至撰写本文时，发现多达三个网站感染了所涉的 GTM 标识符（GTM – MLHK2N68），较 Sucuri 最初报告的六个有所减少。GTM 标识符指的是一个容器，其中包含各种跟踪代码（如谷歌分析、Facebook 像素代码）以及在满足特定条件时触发的规则。

进一步分析显示，该恶意软件从 Magento 数据库表 “cms\_block.content” 加载，GTM 标签包含一段经过编码的 JavaScript 有效载荷，充当信用卡信息窃取器。

安全研究员普佳・斯里瓦斯塔瓦（Puja Srivastava）称：“此脚本旨在收集用户在结账过程中输入的敏感数据，并将其发送到攻击者控制的远程服务器。”

该恶意软件一旦执行，就会从结账页面窃取信用卡信息，并将其发送到外部服务器。

这并非 GTM 首次被用于恶意目的。2018 年 4 月，Sucuri 披露该工具被用于恶意广告活动，旨在通过弹出窗口和重定向为运营者创收。

就在此次事件曝光的几周前，该公司还详细披露了另一起针对 WordPress 的攻击活动，攻击者可能利用插件漏洞或入侵的管理员账户安装恶意软件，将网站访问者重定向到恶意网址。

上周，美国司法部（DoJ）还宣布对两名罗马尼亚人安德烈・法加拉斯（Andrei Fagaras）和塔马斯・科洛兹瓦里（Tamas Kolozsvari）提出指控，他们涉嫌参与支付卡信息窃取活动。

他们因在路易斯安那州东区三个不同地点持有信息窃取设备，被指控三项访问设备欺诈罪。

如果罪名成立，他们每项罪名都将面临最高 15 年监禁、最高三年的监督释放、最高 25 万美元的罚款，以及 100 美元的强制特别评估费。

本文翻译自TheHackersNews [原文链接](https://thehackernews.com/2025/02/hackers-exploit-google-tag-manager-to.html)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/304109](/post/id/304109)

安全KER - 有思想的安全新媒体

本文转载自: [TheHackersNews](https://thehackernews.com/2025/02/hackers-exploit-google-tag-manager-to.html)

如若转载,请注明出处： <https://thehackernews.com/2025/02/hackers-exploit-google-tag-manager-to.html>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [网络攻击](/tag/%E7%BD%91%E7%BB%9C%E6%94%BB%E5%87%BB)

**+1**3赞

收藏

![](https://p2.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p3.ssl.qhimg.com/t014757b72460d855bf.png)

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