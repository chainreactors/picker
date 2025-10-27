---
title: NPM 上的数十个恶意软件包收集主机和网络数据
url: https://www.anquanke.com/post/id/307918
source: 安全客-有思想的安全新媒体
date: 2025-05-29
fetch_date: 2025-10-06T22:25:26.779096
---

# NPM 上的数十个恶意软件包收集主机和网络数据

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

# NPM 上的数十个恶意软件包收集主机和网络数据

阅读量**67676**

发布时间 : 2025-05-28 14:18:05

**x**

##### 译文声明

本文是翻译文章，文章原作者 Bill Toulas，文章来源：bleepingcomputer

原文地址：<https://www.bleepingcomputer.com/news/security/dozens-of-malicious-packages-on-npm-collect-host-and-network-data/>

译文仅供参考，具体内容表达以及含义原文为准。

![Dozens of malicious packages on NPM collect host and network data]()

在NPM索引中发现了60个软件包,这些包试图收集敏感的主机和网络数据,并将其发送到由威胁行为者控制的Discord webhook。

[根据Socket的威胁研究团队的说法](https://socket.dev/blog/60-malicious-npm-packages-leak-network-and-host-data),这些软件包从5月12日开始从三个发布者帐户上传到NPM存储库。

每个恶意包都包含一个安装后脚本,该脚本在“npm install”期间自动执行并收集以下信息:

* 1-主机名
* 2-内部IP地址
* 3-用户主页目录
* 4-当前工作目录
* 5-用户名
* 6-系统 DNS 服务器

脚本检查与云提供商相关的主机名,反向 DNS 字符串,以确定它是否在分析环境中运行。

Socket没有观察到第二阶段有效载荷的交付,特权升级或任何持久机制。然而,鉴于收集的数据类型,有针对性的网络攻击的危险性很大。

###

### NPM 上仍然提供的软件包

研究人员报告了恶意软件包,但在撰写本文时,它们仍然可以在NPM上使用,并显示累积下载量为3,000。然而,通过发布时间,它们都没有出现在存储库中。

为了欺骗开发人员使用它们,该活动背后的威胁行为者使用类似于索引中合法软件包的名称,如“flipper-plugins”,“react-xterm2”和“hermes-inspector-msggen”,通用信任唤起名称,以及其他暗示测试的名称,可能针对CI / CD管道。

60个恶意软件包的完整列表可在Socket报告的底部部分找到。

如果您已经安装了其中任何一个,建议立即删除它们并执行完整的系统扫描以根除任何感染残留物。

### NPM 上的数据雨刷

Socket uncoveredSocket昨天在NPM上发现的另一个恶意活动涉及八个恶意软件包,这些软件包通过错别字搜索来模仿合法工具,但可以删除文件,损坏数据并关闭系统。

这些针对 React、Vue.js、Vite、Node.js 和 Quill 生态系统的软件包在过去两年中一直存在于 NPM 上,下载量为 6,200 次。

逃避这一长时间的部分原因是基于硬编码系统日期激活的有效载荷,并且结构能够逐步销毁框架文件,损坏核心JavaScript方法并破坏浏览器存储机制。

![脚本设计于2023年6月19日至30日删除Vue.js相关文件]()

这场运动背后的威胁行为者,以“xuxingfeng”的名义发布它们,还列出了几个合法的软件包,以建立信任和逃避检测。

虽然危险现在已经根据硬编码日期过去了,但删除软件包至关重要,因为它们的作者可以引入更新,这些更新将在未来重新触发其擦除功能。

本文翻译自bleepingcomputer [原文链接](https://www.bleepingcomputer.com/news/security/dozens-of-malicious-packages-on-npm-collect-host-and-network-data/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/307918](/post/id/307918)

安全KER - 有思想的安全新媒体

本文转载自: [bleepingcomputer](https://www.bleepingcomputer.com/news/security/dozens-of-malicious-packages-on-npm-collect-host-and-network-data/)

如若转载,请注明出处： <https://www.bleepingcomputer.com/news/security/dozens-of-malicious-packages-on-npm-collect-host-and-network-data/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [安全知识](/tag/%E5%AE%89%E5%85%A8%E7%9F%A5%E8%AF%86)
* [网络攻击](/tag/%E7%BD%91%E7%BB%9C%E6%94%BB%E5%87%BB)
* [安全热点](/tag/%E5%AE%89%E5%85%A8%E7%83%AD%E7%82%B9)

**+1**2赞

收藏

![](https://p3.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p4.ssl.qhimg.com/t014757b72460d855bf.png)

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