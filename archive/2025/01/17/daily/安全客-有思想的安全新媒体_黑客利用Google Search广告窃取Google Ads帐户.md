---
title: 黑客利用Google Search广告窃取Google Ads帐户
url: https://www.anquanke.com/post/id/303555
source: 安全客-有思想的安全新媒体
date: 2025-01-17
fetch_date: 2025-10-06T20:07:06.470854
---

# 黑客利用Google Search广告窃取Google Ads帐户

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

# 黑客利用Google Search广告窃取Google Ads帐户

阅读量**117274**

发布时间 : 2025-01-16 10:15:05

**x**

##### 译文声明

本文是翻译文章，文章原作者 Sergiu Gatlan，文章来源：bleepingcomputer

原文地址：<https://www.bleepingcomputer.com/news/security/hackers-use-google-search-ads-to-steal-google-ads-accounts/>

译文仅供参考，具体内容表达以及含义原文为准。

![Google Ads]()

具有讽刺意味的是，网络犯罪分子现在利用谷歌搜索广告来推广钓鱼网站，窃取广告客户在谷歌广告平台上的凭证。

攻击者在谷歌搜索上运行冒充谷歌广告的广告，以赞助商结果的形式将潜在受害者重定向到托管在谷歌网站上但看起来像谷歌广告官方主页的虚假登录页面，并要求他们在那里登录自己的账户。

谷歌网站被用来托管钓鱼网页，因为它允许攻击者伪装他们的虚假广告，因为URL（sites.google.com）与谷歌广告的根域相匹配，可以完全冒充。

![Fake ad impersonating Google Ads]()
冒充谷歌广告的虚假广告（Malwarebytes 实验室）

“的确，除非您的登陆页面（最终 URL）与相同的域名相匹配，否则您不能在广告中显示 URL。”Malwarebytes 研究部高级总监 Jérôme Segura 说：“虽然这是一条旨在防止滥用和冒充的规则，但却很容易被绕过。”

“回过头来看这个广告和谷歌网站页面，我们发现这个恶意广告并没有严格违反规则，因为sites.google.com使用了相同的根域ads.google.com。换句话说，它被允许在广告中显示这个网址，因此使它与谷歌公司发布的同一广告没有区别。”

据遭受过这些攻击或亲眼目睹过这些攻击的人说，这些攻击包括多个阶段：

1. 受害者将其谷歌账户信息输入钓鱼页面。
2. 网络钓鱼工具包收集唯一标识符、cookie 和凭证。
3. 受害者可能会收到一封电子邮件，显示从一个不寻常的地点（巴西）登录。
4. 如果受害者未能阻止这一尝试，就会通过不同的 Gmail 地址向 Google Ads 帐户添加新的管理员。
5. 威胁行为者疯狂消费，并锁定受害者（如果可以的话

![Attack flow]()
攻击流程（Malwarebytes 实验室）

至少有三个网络犯罪团伙是这些攻击的幕后黑手，其中包括很可能在巴西活动的讲葡萄牙语者、使用香港（或中国）广告商账户的亚洲威胁行为者，以及很可能由东欧人组成的第三个团伙。

Malwarebytes 实验室发现了这一正在进行的活动，并认为犯罪分子的最终目的是在黑客论坛上出售窃取的账户，并利用其中一些账户使用相同的网络钓鱼技术发动未来的攻击。

“这是我们追踪到的最恶劣的恶意广告行动，已经触及谷歌业务的核心，很可能影响到他们全球成千上万的客户。我们一直在日以继夜地报告新的事件，但仍不断发现新的事件，甚至在本报告发布时也是如此，”塞古拉补充说。

“具有讽刺意味的是，开展广告活动的个人和企业很有可能没有使用广告拦截器（以查看自己和竞争对手的广告），这使他们更容易上当受骗。”

被盗的谷歌广告账户深受网络犯罪分子的追捧，他们经常将这些账户用作其他攻击的燃料，这些攻击还滥用谷歌搜索广告来推送恶意软件和各种骗局。

“我们明令禁止旨在欺骗他人以窃取其信息或进行诈骗的广告。我们的团队正在积极调查这个问题，并迅速加以解决。”当被要求提供更多有关攻击的细节时，谷歌告诉 BleepingComputer。

在整个 2023 年，谷歌还阻止或删除了 2.065 亿条违反其虚假陈述政策的广告。此外，谷歌还删除了超过 34 亿条广告，限制了超过 57 亿条广告，并暂停了超过 560 万个广告客户账户。

本文翻译自bleepingcomputer [原文链接](https://www.bleepingcomputer.com/news/security/hackers-use-google-search-ads-to-steal-google-ads-accounts/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/303555](/post/id/303555)

安全KER - 有思想的安全新媒体

本文转载自: [bleepingcomputer](https://www.bleepingcomputer.com/news/security/hackers-use-google-search-ads-to-steal-google-ads-accounts/)

如若转载,请注明出处： <https://www.bleepingcomputer.com/news/security/hackers-use-google-search-ads-to-steal-google-ads-accounts/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [网络攻击](/tag/%E7%BD%91%E7%BB%9C%E6%94%BB%E5%87%BB)
* [恶意活动](/tag/%E6%81%B6%E6%84%8F%E6%B4%BB%E5%8A%A8)

**+1**6赞

收藏

![](https://p4.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p0.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p4.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=173683)

[安全客](/member.html?memberId=173683)

这个人太懒了，签名都懒得写一个

* 文章
* **553**

* 粉丝
* **2**

### TA的文章

* ##### [年度盘点：AI+安全双重赋能，360解锁企业浏览器新动力](/post/id/303791)

  2025-01-24 10:00:53
* ##### [IntelBroker 的数字足迹： OSINT 分析揭露网络犯罪分子的行动](/post/id/303788)

  2025-01-24 09:55:58
* ##### [7-Zip 修复了可绕过 Windows MoTW 安全警告的错误，立即修补](/post/id/303776)

  2025-01-24 09:49:56
* ##### [Microsoft 在 Edge Stable 中预览 Game Assist 游戏内浏览器](/post/id/303773)

  2025-01-24 09:43:16
* ##### [ModiLoader 恶意软件利用 CAB 标头批处理文件逃避检测](/post/id/303770)

  2025-01-24 09:36:10

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