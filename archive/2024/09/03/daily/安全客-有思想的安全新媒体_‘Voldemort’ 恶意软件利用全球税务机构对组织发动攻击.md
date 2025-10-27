---
title: ‘Voldemort’ 恶意软件利用全球税务机构对组织发动攻击
url: https://www.anquanke.com/post/id/299693
source: 安全客-有思想的安全新媒体
date: 2024-09-03
fetch_date: 2025-10-06T18:23:58.983897
---

# ‘Voldemort’ 恶意软件利用全球税务机构对组织发动攻击

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

# ‘Voldemort’ 恶意软件利用全球税务机构对组织发动攻击

阅读量**67820**

发布时间 : 2024-09-02 16:56:12

**x**

##### 译文声明

本文是翻译文章，文章原作者 Nathan Eddy，文章来源：DARKREADING

原文地址：<https://www.darkreading.com/threat-intelligence/voldemort-malware-curses-orgs-global-tax-authorities>

译文仅供参考，具体内容表达以及含义原文为准。

一个名为“Voldemort”的复杂恶意软件活动通过冒充欧洲、亚洲和美国的税务机关来针对全球组织。

根据 Proofpoint 的一份报告，这种恶意活动已经影响了全球数十个组织，自 8 月 5 日开始以来，已报告了 20,000 多封网络钓鱼邮件。

该恶意软件是用 C 语言编写的自定义后门程序，旨在用于数据泄露和部署额外的恶意负载。

该攻击利用 Google 表格进行命令和控制 （C2） 通信以及带有恶意 Windows 搜索协议的文件。一旦受害者下载了恶意软件，它就会使用合法版本的 WebEx 软件加载与 C2 服务器通信的 DLL。

## 伏地魔变身税务机关

研究人员表示，该活动在 8 月 17 日显著升级，当时一天内发送了近 6,000 封网络钓鱼电子邮件，主要冒充税务机构。

其中包括美国国内税务局（IRS），英国的英国皇家税务海关总署，以及法国的公共财政总署等。每封网络钓鱼电子邮件都是用相应税务机关的母语制作的，为诱饵增加了一层可信度。

这些电子邮件来自似乎遭到入侵的域名，其中包括税务机构的合法域名，以进一步增强其真实性。

该报告指出，该活动的最终目标尚不清楚，但 Proofpoint 研究人员表示，鉴于伏地魔的情报收集能力和部署额外有效载荷的潜力，他们认为这可能旨在进行间谍活动。

## Google 用户极易受到恶意咒语的攻击

Qualys 威胁研究部门的安全研究经理 Mayuresh Dani 表示，在其生态系统中使用 Google 的组织更有可能面临 Voldemort 的风险，因为该公司的平台将位于允许列表中。

“除非组织监控流向指定 [入侵指标] 的流量，否则这些攻击在很大程度上不会受到关注，”他指出。

Dani 解释说，这是一种在 MITRE ATT&CK 框架中标识为 T1567.002 的已知技术，并建议组织监控与非浏览器进程相关的云服务的网络连接，以及与云服务的大量网络连接。

与此同时，DoControl 的联合创始人兼 CRO Omri Weinberg 表示，验证政府通信的真实性具有挑战性，尤其是考虑到这些冒充行为的说服力。

“组织应该建立明确的协议来处理敏感请求或通知，尤其是与财务事务相关的请求或通知，”他解释说。“这可能包括在采取行动之前始终通过单独的已知良好渠道进行验证。”

他补充说，对员工进行此类冒充攻击的教育至关重要。

“他们应该知道对未经请求的通信持怀疑态度，尤其是那些制造紧迫感的通信，”他说。

虽然实施 DMARC 和其他电子邮件身份验证协议可以帮助过滤掉一些欺骗性电子邮件，但 Weinberg 强调，用户意识仍然是关键。

## 安全最佳实践是一种很好的防御魅力

Sectigo 高级研究员 Jason Soroko 表示，公司可以通过增强电子邮件过滤系统并培训员工识别和报告可疑电子邮件来防范个性化的网络钓鱼攻击。

他还建议采用强大的多因素身份验证 （MFA），并定期更新和审计公开可用信息的可见性，以减少暴露。

“组织还应采用先进的端点检测和响应工具，实施严格的网络分段，定期应用安全补丁，监控异常行为，并实施强大的数据加密实践来保护敏感信息，”他补充道。

最后，他强调说，实施包括 DMARC、SPF 和 DKIM 在内的电子邮件身份验证协议也有助于防止基于模拟的攻击，以及用于确保组织内电子邮件发件人身份合法性的 S/MIME 证书。

本文翻译自DARKREADING [原文链接](https://www.darkreading.com/threat-intelligence/voldemort-malware-curses-orgs-global-tax-authorities)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/299693](/post/id/299693)

安全KER - 有思想的安全新媒体

本文转载自: [DARKREADING](https://www.darkreading.com/threat-intelligence/voldemort-malware-curses-orgs-global-tax-authorities)

如若转载,请注明出处： <https://www.darkreading.com/threat-intelligence/voldemort-malware-curses-orgs-global-tax-authorities>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [网络攻击](/tag/%E7%BD%91%E7%BB%9C%E6%94%BB%E5%87%BB)
* [安全热点](/tag/%E5%AE%89%E5%85%A8%E7%83%AD%E7%82%B9)

**+1**0赞

收藏

![](https://p5.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p1.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p5.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=170338)

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

* [伏地魔变身税务机关](#h2-0)
* [Google 用户极易受到恶意咒语的攻击](#h2-1)
* [安全最佳实践是一种很好的防御魅力](#h2-2)

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