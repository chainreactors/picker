---
title: SnailLoad 允许攻击者通过测量网络延迟来追踪访问过的网站
url: https://www.anquanke.com/post/id/297599
source: 安全客-有思想的安全新媒体
date: 2024-07-02
fetch_date: 2025-10-06T17:40:37.615437
---

# SnailLoad 允许攻击者通过测量网络延迟来追踪访问过的网站

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

# SnailLoad 允许攻击者通过测量网络延迟来追踪访问过的网站

阅读量**115576**

发布时间 : 2024-07-01 12:27:08

**x**

##### 译文声明

本文是翻译文章

原文地址：<https://thecyberexpress.com/snailload-measuring-network-latency/>

译文仅供参考，具体内容表达以及含义原文为准。

奥地利格拉茨技术大学的研究人员发现了一种名为 SnailLoad 的新型旁道攻击，该攻击利用网络延迟来推断用户活动。SnailLoad 是一种非侵入式攻击技术，攻击者无需直接访问受害者的网络流量即可收集有关受害者访问的网站或观看的视频的信息。

**SnailLoad 漏洞的工作原理**
SnailLoad利用了大多数互联网连接中存在的带宽瓶颈。当用户的设备与服务器通信时，连接的最后一英里通常比服务器的连接慢。攻击者可以测量发送给受害者的数据包的延迟，以推断受害者的连接何时繁忙。

![SnailLoad 漏洞]()
来源：snailload.com
攻击伪装成下载文件或任何网站组件（如样式表、字体、图片或广告）。攻击服务器以蜗牛般的速度发送文件，以监控长时间内的连接延迟。研究人员决定将这项技术命名为“SnailLoad”，因为“除了速度慢之外，SnailLoad 就像蜗牛一样，会留下痕迹，有点令人毛骨悚然。”

攻击不需要在受害者的系统上执行 JavaScript 或代码。它只需要受害者从攻击者控制的服务器加载内容，该服务器以极慢的速度发送数据。通过监控一段时间内的延迟，攻击者可以将模式与特定的在线活动关联起来。

研究人员分享了重现 SnailLoad 攻击所需的条件：

* 受害者与攻击服务器进行通信。
* 通信服务器的互联网连接速度比受害者的最后一英里连接速度更快。
* 如果最后一英里繁忙，攻击者发送给受害者的数据包将会延迟。
* 攻击者通过旁道攻击推断受害者访问过的网站或观看过的视频。

在 SnailLoad 研究论文中详细介绍的相关用户研究中，研究人员联系了当地的本科生和研究生，他们自愿运行采用 SnailLoad 攻击技术的测量脚本。研究人员采取措施确保在任何时候都不会泄露任何个人信息。

此外，研究人员计划在论文发表后销毁收集到的痕迹，并让学生可以随时直接要求删除痕迹或从论文结果中排除他们的痕迹。

研究人员于 3 月 9 日在论文的负责任披露部分向谷歌报告了这种攻击技术，谷歌承认了该问题的严重性。这家科技巨头还表示，正在调查 YouTube 可能的服务器端缓解措施。研究人员在 GitHub 上分享了概念验证以及说明和在线演示。

**蜗牛负荷的影响及缓解措施**
在测试中，SnailLoad 在识别受害者观看的 YouTube 视频方面能够达到高达 98% 的准确率。在对访问量最大的 100 个网站进行指纹识别方面，其准确率也达到了 62.8%。

虽然目前尚未在野外发现，但 SnailLoad 可能会影响大多数互联网连接。缓解措施具有挑战性，因为根本原因是网络基础设施的根本带宽差异。研究人员表示，虽然向网络添加随机噪声会降低攻击的准确性，但它可能会影响性能并给用户带来不便。

本文翻译自 [原文链接](https://thecyberexpress.com/snailload-measuring-network-latency/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/297599](/post/id/297599)

安全KER - 有思想的安全新媒体

本文转载自:

如若转载,请注明出处： <https://thecyberexpress.com/snailload-measuring-network-latency/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [网络攻击](/tag/%E7%BD%91%E7%BB%9C%E6%94%BB%E5%87%BB)

**+1**0赞

收藏

![](https://p4.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p4.ssl.qhimg.com/t014757b72460d855bf.png)

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