---
title: 以加密货币钱包为目标的恶意 PyPI 软件包：aiocpa 活动曝光
url: https://www.anquanke.com/post/id/302336
source: 安全客-有思想的安全新媒体
date: 2024-12-03
fetch_date: 2025-10-06T19:33:11.910166
---

# 以加密货币钱包为目标的恶意 PyPI 软件包：aiocpa 活动曝光

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

# 以加密货币钱包为目标的恶意 PyPI 软件包：aiocpa 活动曝光

阅读量**68782**

发布时间 : 2024-12-02 14:46:21

**x**

##### 译文声明

本文是翻译文章，文章原作者 do son，文章来源：securityonline

原文地址：<https://securityonline.info/malicious-pypi-package-targets-cryptocurrency-wallets-aiocpa-campaign-exposed/>

译文仅供参考，具体内容表达以及含义原文为准。

![]()

ReversingLabs 公司的网络安全研究人员通过 PyPI 存储库发现了一种针对加密货币钱包的隐秘供应链攻击。这个名为 aiocpa 的恶意软件包伪装成一个合法的加密客户端工具，向攻击者暴露了敏感的用户信息。ReversingLabs 立即向 PyPI 报告了这一威胁，并最终将其删除。

ReversingLabs 先进的机器学习威胁检测平台于 11 月 21 日识别出了该恶意软件包。与典型的错别字抢注或冒充攻击不同，aiocpa 背后的威胁行为者采用了一种更微妙的方法。他们发布了自己的加密客户端软件包，以建立用户信任，然后再通过恶意更新来危害用户。

ReversingLabs 的报告指出：“普通开发人员在进行安全评估时……无法判断这个软件包是否可疑。”

![Malicious PyPI crypto]()
恶意 GitHub 账户详细信息 | 图片： ReversingLabs

恶意代码隐藏在 aiocpa 的 utils/sync.py 文件中，采用了多层混淆，如 Base64 编码和 zlib 压缩。解混淆后，研究人员发现了一个围绕 CryptoPay 初始化函数的包装器，将加密货币交易代币等敏感数据外泄到远程 Telegram 机器人。

这种策略性利用在 0.1.13 和 0.1.14 版的 aiocpa 中更加明显，其中偷偷添加了恶意功能。值得注意的是，这些代码并未出现在软件包的 GitHub 代码库中，从而规避了传统的源代码审计。

攻击者还试图接管现有的 PyPI 软件包付费，这凸显了软件供应链攻击中日益增长的威胁载体。正如 ReversingLabs 所指出的：“你能检测到这种变化吗？它会自动传播到你的软件解决方案中吗？”

ReversingLabs 强调，即使是拥有合法贡献者的维护良好的项目也无法避免受到攻击。这个案例更加说明了高级安全评估的重要性，因为传统方法已经不能满足需要。

报告总结道：“需要将专用工具纳入开发流程，以帮助预防这些威胁并降低相关风险。”

本文翻译自securityonline [原文链接](https://securityonline.info/malicious-pypi-package-targets-cryptocurrency-wallets-aiocpa-campaign-exposed/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/302336](/post/id/302336)

安全KER - 有思想的安全新媒体

本文转载自: [securityonline](https://securityonline.info/malicious-pypi-package-targets-cryptocurrency-wallets-aiocpa-campaign-exposed/)

如若转载,请注明出处： <https://securityonline.info/malicious-pypi-package-targets-cryptocurrency-wallets-aiocpa-campaign-exposed/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [网络攻击](/tag/%E7%BD%91%E7%BB%9C%E6%94%BB%E5%87%BB)
* [恶意活动](/tag/%E6%81%B6%E6%84%8F%E6%B4%BB%E5%8A%A8)

**+1**3赞

收藏

![](https://p2.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p3.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p2.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=173683)

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