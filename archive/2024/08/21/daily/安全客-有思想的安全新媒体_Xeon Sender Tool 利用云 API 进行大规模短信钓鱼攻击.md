---
title: Xeon Sender Tool 利用云 API 进行大规模短信钓鱼攻击
url: https://www.anquanke.com/post/id/299307
source: 安全客-有思想的安全新媒体
date: 2024-08-21
fetch_date: 2025-10-06T18:00:40.346993
---

# Xeon Sender Tool 利用云 API 进行大规模短信钓鱼攻击

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

# Xeon Sender Tool 利用云 API 进行大规模短信钓鱼攻击

阅读量**58307**

发布时间 : 2024-08-20 11:41:57

**x**

##### 译文声明

本文是翻译文章，文章原作者 Ravie Lakshmanan，文章来源：The Hacker News

原文地址：<https://thehackernews.com/2024/08/xeon-sender-tool-exploits-cloud-apis.html>

译文仅供参考，具体内容表达以及含义原文为准。

恶意行为者正在使用名为 Xeon Sender 的云攻击工具，通过滥用合法服务进行大规模的短信、网络钓鱼和垃圾邮件活动。

“攻击者可以使用Xeon通过多个软件即服务（SaaS）提供商发送消息，使用服务提供商的有效凭据，”SentinelOne安全研究员Alex Delamotte在与The Hacker News分享的一份报告中说。

用于促进 SMS 消息大规模分发的服务示例包括 Amazon Simple Notification Service （SNS）、Nexmo、Plivo、Proovl、Send99、Telesign、Telnyx、TextBelt、Twilio。

这里需要注意的是，该活动不会利用这些提供商的任何固有弱点。相反，该工具使用合法的 API 进行批量短信垃圾邮件攻击。

它加入了 SNS Sender 等工具，这些工具已日益成为发送批量短信钓鱼消息并最终从目标捕获敏感信息的一种方式。

通过 Telegram 和黑客论坛分发，其中一个旧版本归功于一个专门用于广告破解黑客工具的 Telegram 频道。最新版本可作为ZIP文件下载，它归因于一个名为Orion Toolxhub（oriontoolxhub）的Telegram频道，该频道有200名成员。

Orion Toolxhub 创建于 2023 年 2 月 1 日。它还免费提供其他软件，用于暴力攻击、反向 IP 地址查找以及其他软件，例如 WordPress 网站扫描器、PHP Web Shell、比特币剪刀和一个名为 YonixSMS 的程序，该程序声称提供无限的短信发送功能。

Xeon Sender 也称为 XeonV5 和 SVG Sender。基于 Python 的程序的早期版本早在 2022 年就已被检测到。此后，它被几个威胁行为者重新用于他们自己的目的。

“该工具的另一个化身托管在带有 GUI 的 Web 服务器上，”Delamotte 说。“这种托管方法消除了潜在的访问障碍，使技能较低的参与者能够适应运行 Python 工具并对其依赖项进行故障排除。”

无论使用何种变体，Xeon Sender 都为其用户提供了一个命令行界面，可用于与所选服务提供商的后端 API 进行通信并编排批量 SMS 垃圾邮件攻击。

这也意味着威胁参与者已经拥有访问端点所需的必要 API 密钥。构建的 API 请求还包括发件人 ID、消息内容以及从文本文件中存在的预定义列表中选择的电话号码之一。

Xeon Sender 除了其 SMS 发送方法外，还集成了验证 Nexmo 和 Twilio 帐户凭据、为给定国家/地区代码和区号生成电话号码以及检查提供的电话号码是否有效的功能。

尽管缺乏与该工具相关的技巧，但SentinelOne表示，源代码中充满了模棱两可的变量，如单个字母或字母加一个数字，使调试更具挑战性。

Delamotte 说：“Xeon Sender 主要使用特定于提供商的 Python 库来制作 API 请求，这带来了有趣的检测挑战。“每个库都是独一无二的，提供商的日志也是如此。团队可能很难检测到对特定服务的滥用。

“为了抵御像Xeon Sender这样的威胁，组织应该监控与评估或修改短信发送权限或分发列表的异常更改相关的活动，例如大量上传新的收件人电话号码。”

本文翻译自The Hacker News [原文链接](https://thehackernews.com/2024/08/xeon-sender-tool-exploits-cloud-apis.html)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/299307](/post/id/299307)

安全KER - 有思想的安全新媒体

本文转载自: [The Hacker News](https://thehackernews.com/2024/08/xeon-sender-tool-exploits-cloud-apis.html)

如若转载,请注明出处： <https://thehackernews.com/2024/08/xeon-sender-tool-exploits-cloud-apis.html>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [网络攻击](/tag/%E7%BD%91%E7%BB%9C%E6%94%BB%E5%87%BB)
* [网络安全热点](/tag/%E7%BD%91%E7%BB%9C%E5%AE%89%E5%85%A8%E7%83%AD%E7%82%B9)

**+1**0赞

收藏

![](https://p3.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p1.ssl.qhimg.com/t014757b72460d855bf.png)

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