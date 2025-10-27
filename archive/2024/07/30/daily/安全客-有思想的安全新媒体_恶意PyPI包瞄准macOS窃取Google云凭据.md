---
title: 恶意PyPI包瞄准macOS窃取Google云凭据
url: https://www.anquanke.com/post/id/298510
source: 安全客-有思想的安全新媒体
date: 2024-07-30
fetch_date: 2025-10-06T17:40:44.397795
---

# 恶意PyPI包瞄准macOS窃取Google云凭据

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

# 恶意PyPI包瞄准macOS窃取Google云凭据

阅读量**144472**

发布时间 : 2024-07-29 15:07:35

**x**

##### 译文声明

本文是翻译文章，文章原作者 Newsroom，文章来源：The Hacker News

原文地址：<https://thehackernews.com/2024/07/malicious-pypi-package-targets-macos-to.html>

译文仅供参考，具体内容表达以及含义原文为准。

网络安全研究人员在 Python Package Index （PyPI） 存储库上发现了一个恶意包，该包针对 Apple macOS 系统，目的是从一小群受害者中窃取用户的 Google Cloud 凭据。

这个名为“lr-utils-lib”的包在被下架之前总共吸引了 59 次下载。它于 2024 年 6 月初上传到注册表。

“该恶意软件使用预定义的哈希列表来针对特定的macOS机器，并试图收集Google Cloud身份验证数据，”Checkmarx研究员Yehuda Gelb在周五的一份报告中说。“收集的凭据将发送到远程服务器。”

该软件包的一个重要方面是，它首先检查它是否已安装在 macOS 系统上，然后才继续将系统的通用唯一标识符 （UUID） 与 64 个哈希的硬编码列表进行比较。

如果被感染的计算机属于预定义集中指定的计算机，它将尝试访问位于 ~/.config/gcloud 目录中的两个文件，即 application\_default\_credentials.json 和 credentials.db，其中包含 Google Cloud 身份验证数据。

然后，捕获的信息通过 HTTP 传输到远程服务器“europe-west2-workload-422915[.]云函数[.]净。

Checkmarx表示，它还在LinkedIn上发现了一个名为“Lucid Zenith”的虚假个人资料，该个人资料与包裹的所有者相匹配，并谎称自己是Apex Companies的首席执行官，这表明这次攻击可能存在社会工程因素。

目前尚不清楚谁是这场运动的幕后黑手。然而，两个多月前，网络安全公司 Phylum 披露了另一次供应链攻击的细节，该攻击涉及一个名为“requests-darwin-lite”的 Python 包，该包在检查 macOS 主机的 UUID 后也被发现释放其恶意行为。

这些活动表明，威胁行为者对他们想要渗透的macOS系统有先验知识，并且正在竭尽全力确保恶意软件包仅分发给那些特定的机器。

它还说明了恶意行为者用来分发相似包的策略，旨在欺骗开发人员将它们合并到他们的应用程序中。

“虽然目前尚不清楚这次攻击是针对个人还是企业，但这些类型的攻击可能会对企业产生重大影响，”Gelb说。“虽然最初的妥协通常发生在个人开发人员的机器上，但对企业的影响可能是巨大的。

本文翻译自The Hacker News [原文链接](https://thehackernews.com/2024/07/malicious-pypi-package-targets-macos-to.html)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/298510](/post/id/298510)

安全KER - 有思想的安全新媒体

本文转载自: [The Hacker News](https://thehackernews.com/2024/07/malicious-pypi-package-targets-macos-to.html)

如若转载,请注明出处： <https://thehackernews.com/2024/07/malicious-pypi-package-targets-macos-to.html>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [网络攻击](/tag/%E7%BD%91%E7%BB%9C%E6%94%BB%E5%87%BB)
* [安全头条](/tag/%E5%AE%89%E5%85%A8%E5%A4%B4%E6%9D%A1)

**+1**4赞

收藏

![](https://p3.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p2.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p3.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=170338)

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