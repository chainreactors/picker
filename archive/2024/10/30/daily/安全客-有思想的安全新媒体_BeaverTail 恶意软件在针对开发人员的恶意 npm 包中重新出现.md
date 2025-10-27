---
title: BeaverTail 恶意软件在针对开发人员的恶意 npm 包中重新出现
url: https://www.anquanke.com/post/id/301353
source: 安全客-有思想的安全新媒体
date: 2024-10-30
fetch_date: 2025-10-06T18:46:52.352698
---

# BeaverTail 恶意软件在针对开发人员的恶意 npm 包中重新出现

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

# BeaverTail 恶意软件在针对开发人员的恶意 npm 包中重新出现

阅读量**77091**

发布时间 : 2024-10-29 10:52:05

**x**

##### 译文声明

本文是翻译文章，文章原作者 Ravie Lakshmanan，文章来源：TheHackersNews

原文地址：<https://thehackernews.com/2024/10/beavertail-malware-resurfaces-in.html>

译文仅供参考，具体内容表达以及含义原文为准。

在 2024 年 9 月发布到 npm 注册表的三个恶意软件包中发现了一个名为 BeaverTail 的已知恶意软件，这是一个 JavaScript 下载器和信息窃取器，与朝鲜正在进行的名为 Contagious Interview 的活动有关。

Datadog 安全研究团队正在监控名为 Tenacious Pungsan 的活动，该恶意软件还有 CL-STA-0240 和 Famous Chollima 两个名称。

恶意软件包已无法从软件包注册表中下载，其名称如下

* passports-js，护照的备份副本（118 次下载）
* bcrypts-js，bcryptjs 的篡改副本（81 次下载）
* blockscan-api，ethercan-api 的屏蔽副本（124 次下载）

Contagious Interview（传染性访谈）是指朝鲜民主主义人民共和国（朝鲜）开展的一项为期一年的活动，其中包括诱骗开发人员下载恶意软件包或看似无害的视频会议应用程序，作为编码测试的一部分。它于 2023 年 11 月首次曝光。

这已经不是威胁分子第一次使用 npm 软件包分发 BeaverTail 了。2024 年 8 月，软件供应链安全公司 Phylum 披露了另一批 npm 软件包，它们为部署 BeaverTail 和名为 InvisibleFerret 的 Python 后门铺平了道路。

这些恶意软件包的名称分别是 temp-etherscan-api、etherscan-api、telegram-con、helmet-validate 和 qq-console。这两组软件包的一个共同点是，威胁行为者一直在努力模仿 etherscan-api 软件包，这表明加密货币领域是一个持久的目标。

上个月，Stacklok 说它检测到了新一轮的仿冒软件包–eslint-module-conf 和 eslint-scope-util，这些软件包的目的是收集加密货币，并对被入侵的开发者机器建立持久访问。

Palo Alto Networks 第 42 部门本月早些时候告诉《黑客新闻》，事实证明，利用求职者在网上申请工作机会时的信任感和紧迫感传播恶意软件是一种有效的方式。

这些发现凸显了威胁行为者是如何越来越多地滥用开源软件供应链作为攻击载体来感染下游目标的。

“Datadog表示：”复制和回传合法的npm软件包仍然是威胁行为者在这个生态系统中常用的策略。“这些活动以及更广泛的 Contagious Interview 突出表明，个人开发者仍然是这些与朝鲜有关联的威胁行为者的重要目标。”

本文翻译自TheHackersNews [原文链接](https://thehackernews.com/2024/10/beavertail-malware-resurfaces-in.html)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/301353](/post/id/301353)

安全KER - 有思想的安全新媒体

本文转载自: [TheHackersNews](https://thehackernews.com/2024/10/beavertail-malware-resurfaces-in.html)

如若转载,请注明出处： <https://thehackernews.com/2024/10/beavertail-malware-resurfaces-in.html>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [恶意软件](/tag/%E6%81%B6%E6%84%8F%E8%BD%AF%E4%BB%B6)
* [网络攻击](/tag/%E7%BD%91%E7%BB%9C%E6%94%BB%E5%87%BB)
* [恶意活动](/tag/%E6%81%B6%E6%84%8F%E6%B4%BB%E5%8A%A8)

**+1**1赞

收藏

![](https://p0.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p3.ssl.qhimg.com/t014757b72460d855bf.png)

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