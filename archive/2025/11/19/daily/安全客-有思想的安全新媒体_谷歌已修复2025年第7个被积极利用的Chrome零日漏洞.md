---
title: 谷歌已修复2025年第7个被积极利用的Chrome零日漏洞
url: https://www.anquanke.com/post/id/313261
source: 安全客-有思想的安全新媒体
date: 2025-11-19
fetch_date: 2025-11-20T03:08:22.524615
---

# 谷歌已修复2025年第7个被积极利用的Chrome零日漏洞

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

# 谷歌已修复2025年第7个被积极利用的Chrome零日漏洞

阅读量**25166**

发布时间 : 2025-11-19 17:40:10

**x**

##### 译文声明

本文是翻译文章，文章原作者 Bill Mann，文章来源：cyberinsider

原文地址：<https://cyberinsider.com/google-fixes-seventh-actively-exploited-chrome-zero-day-of-2025/>

译文仅供参考，具体内容表达以及含义原文为准。

![]()

谷歌已发布 Chrome 浏览器安全更新，修复其 **V8 JavaScript 引擎** 中的两个高危漏洞，其中 **CVE-2025-13223** 已被证实存在 **在野利用**。这是今年修复的第 **7 个 Chrome 零日漏洞**。

该新修复的漏洞由谷歌威胁分析小组（TAG）的 Clément Lecigne 于 2025 年 11 月 12 日报告，是 V8 引擎中的 **类型混淆漏洞**。V8 作为处理 JavaScript 和 WebAssembly 的引擎，负责 Chrome 网页内容的执行。谷歌确认该漏洞已被利用，但攻击的性质和范围细节将在多数用户完成补丁更新后公布。

类型混淆漏洞源于程序在错误假设对象类型的情况下分配或访问内存，可能导致意外行为或内存损坏。在浏览器环境中，攻击者可通过精心构造的 HTML 或 JavaScript 内容利用此类漏洞触发 **堆损坏**。成功利用后，攻击者可在浏览器上下文中执行远程代码，若与其他漏洞结合，还可能实现 **沙箱逃逸** 或更广泛的系统入侵。

1. **Linux 和 Windows** 用户需更新至 **142.0.7444.175**
2. **macOS** 用户需更新至 **142.0.7444.176**

当前稳定版用户已开始推送更新，未来几天至几周内将覆盖更广泛用户群体。

另一个高危漏洞 **CVE-2025-13224** 同样涉及 V8 引擎中的类型混淆问题，由谷歌内部“Big Sleep”安全团队于 10 月 9 日提前报告。

谷歌 Chrome 占据全球桌面浏览器 **60% 以上市场份额**，是现代网络交互的核心工具。鉴于其广泛应用及在企业与消费环境中的深度集成，被积极利用的 Chrome 漏洞对全球数百万用户构成重大安全风险。

![]()

此次零日漏洞是 2025 年持续曝光的关键浏览器漏洞之一。今年已修复的 Chrome 零日漏洞包括多个 V8 及相关组件的类型混淆和内存损坏漏洞，其中多个由 TAG 或谷歌内部研究团队发现。V8 引擎作为频繁攻击目标，凸显其复杂性及作为攻击面的吸引力。

为降低被利用风险，强烈建议用户立即将 Chrome 更新至最新稳定版本：

1. 打开 Chrome 设置 > 关于 Chrome
2. 浏览器将自动检查更新，安装后重启即可
3. 建议启用 **自动更新** 以确保及时接收补丁

本文翻译自cyberinsider [原文链接](https://cyberinsider.com/google-fixes-seventh-actively-exploited-chrome-zero-day-of-2025/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/313261](/post/id/313261)

安全KER - 有思想的安全新媒体

本文转载自: [cyberinsider](https://cyberinsider.com/google-fixes-seventh-actively-exploited-chrome-zero-day-of-2025/)

如若转载,请注明出处： <https://cyberinsider.com/google-fixes-seventh-actively-exploited-chrome-zero-day-of-2025/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [安全资讯](/tag/%E5%AE%89%E5%85%A8%E8%B5%84%E8%AE%AF)
* [漏洞情报](/tag/%E6%BC%8F%E6%B4%9E%E6%83%85%E6%8A%A5)

**+1**0赞

收藏

![](https://p3.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p0.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p3.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=171771)

[安全客](/member.html?memberId=171771)

这个人太懒了，签名都懒得写一个

* 文章
* **706**

* 粉丝
* **6**

### TA的文章

* ##### [SnowSoul勒索软件样本分析：加密机制与解密研究](/post/id/313279)

  2025-11-19 21:35:35
* ##### [Windows 11 新增云重建与时间点还原系统恢复工具](/post/id/313271)

  2025-11-19 17:41:26
* ##### [Thunderbird新增原生支持，实现对Microsoft Exchange账户的全面兼容](/post/id/313267)

  2025-11-19 17:41:08
* ##### [Cloudflare全球服务中断，引发互联网大面积瘫痪——多家主流网络平台无法访问](/post/id/313258)

  2025-11-19 17:40:41
* ##### [谷歌已修复2025年第7个被积极利用的Chrome零日漏洞](/post/id/313261)

  2025-11-19 17:40:10

### 相关文章

* ##### [Windows 11 新增云重建与时间点还原系统恢复工具](/post/id/313271)

  2025-11-19 17:41:26
* ##### [Thunderbird新增原生支持，实现对Microsoft Exchange账户的全面兼容](/post/id/313267)

  2025-11-19 17:41:08
* ##### [Cloudflare全球服务中断，引发互联网大面积瘫痪——多家主流网络平台无法访问](/post/id/313258)

  2025-11-19 17:40:41
* ##### [macOS平台曝出“Nova”钱包窃取程序：通过替换Ledger/Trezor应用为钓鱼克隆版来窃取用户助记词](/post/id/313255)

  2025-11-19 17:39:45
* ##### [新型.NET加载器“隐匿窃密者”通过高级隐写术将LokiBot窃密木马植入BMP/PNG图片](/post/id/313252)

  2025-11-19 17:38:46
* ##### [npm供应链攻击预警：黑客利用Adspect伪装技术与虚假加密货币验证码同时欺骗用户与安全研究人员](/post/id/313249)

  2025-11-19 17:37:58
* ##### [SolarWinds Serv-U 中存在严重漏洞（CVSS 9.1），可导致已认证的管理员实现远程代码执行并完成路径绕过](/post/id/313245)

  2025-11-19 17:37:15

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