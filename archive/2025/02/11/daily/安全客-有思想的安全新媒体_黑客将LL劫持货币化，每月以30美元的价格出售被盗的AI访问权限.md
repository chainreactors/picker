---
title: 黑客将LL劫持货币化，每月以30美元的价格出售被盗的AI访问权限
url: https://www.anquanke.com/post/id/304030
source: 安全客-有思想的安全新媒体
date: 2025-02-11
fetch_date: 2025-10-06T20:34:53.338976
---

# 黑客将LL劫持货币化，每月以30美元的价格出售被盗的AI访问权限

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

# 黑客将LL劫持货币化，每月以30美元的价格出售被盗的AI访问权限

阅读量**57956**

发布时间 : 2025-02-10 14:24:18

**x**

##### 译文声明

本文是翻译文章，文章原作者 Deeba Ahmed，文章来源：hackread

原文地址：<https://hackread.com/hackers-monetize-llmjacking-selling-stolen-ai-access/>

译文仅供参考，具体内容表达以及含义原文为准。

大语言模型劫持（LLMjacking）攻击瞄准 DeepSeek，导致云成本飙升。Sysdig 公司揭示，如今已出现了一个大语言模型访问权限的黑市，其中运营反向代理（ORP）的人员提供对被盗账户的未经授权访问。一起来了解攻击者是如何窃取访问权限并将大语言模型的使用货币化的。

自 2024 年 5 月首次发现大语言模型劫持攻击以来，Sysdig 威胁研究团队（TRT）观察到此类攻击迅速演变，其范围已扩大到诸如 DeepSeek 这样的新型大语言模型。据报道，在 DeepSeek – V3 发布仅几天后，它就被整合到了 ORP 实例中，这显示出攻击者适应的速度之快。

### ****对 DeepSeek API 密钥的利用以及大语言模型劫持的货币化****

研究人员称，类似地，DeepSeek – R1 发布后不久也被纳入了这些平台。多个 ORP 平台上发现充斥着 DeepSeek 的 API 密钥，这表明该新模型正遭到积极利用。

由于基于云的大语言模型使用成本高昂，大语言模型劫持攻击指的是攻击者入侵账户，从而免费使用这些昂贵的服务。根据 TRT 的最新发现，大语言模型劫持已成为一种成熟的攻击手段，在线社区中人们正积极分享相关工具和技术。

他们观察到，大语言模型劫持的货币化趋势正在上升，通过 ORP（OpenAI 反向代理）出售大语言模型的访问权限，据报道，有一个实例每月以 30 美元的价格出售访问权限。运营者往往低估了与大语言模型使用相关的成本，而研究人员注意到，在一个实例中，仅仅运行了 4.5 天，就产生了近 5 万美元的成本，其中 Claude 3 Opus 的使用成本最为高昂。

![Hackers Monetize LLMjacking, Selling Stolen AI Access for $30 per Month]()

### ****资源利用规模****

在观察到的所有 ORP 平台上，总的令牌（大语言模型生成的单词、字符集或单词 / 标点组合）使用量超过了 20 亿，这凸显了资源被利用的规模。受害者是合法账户持有人，他们的凭证已被盗取。

使用 ORP 仍然是大语言模型劫持的常用方法。ORP 服务器作为各种大语言模型的反向代理，可以通过 Nginx 或诸如 TryCloudflare 这样的动态域名进行暴露，有效地掩盖了攻击者的来源。这些代理通常包含从不同提供商（如 OpenAI、Google AI 和 Mistral AI）窃取的大量 API 密钥，使攻击者能够向他人提供大语言模型的访问权限。

研究人员在博客文章中指出：“Sysdig TRT 发现，有十几台代理服务器使用了从包括 OpenAI、AWS 和 Azure 等许多不同服务中窃取的凭证。大语言模型的高昂成本，正是网络犯罪分子（如下例中的犯罪分子）选择窃取凭证而不是付费使用大语言模型服务的原因。”

### ****利用大语言模型劫持的在线社区****

像 4chan 和 Discord 这样的在线社区，为通过 ORP 分享大语言模型访问权限提供了便利。Rentry.co 网站则被用于分享工具和服务。研究人员在蜜罐环境中的大语言模型提示日志里，发现了众多 ORP 代理，有些使用自定义域名，另一些则使用 TryCloudflare 隧道，这些都可追溯到攻击者控制的服务器。

凭证盗窃是大语言模型劫持的一个重要方面，攻击者瞄准易受攻击的服务，并使用验证脚本识别用于访问机器学习服务的凭证。公共存储库也会提供暴露的凭证。为了实现隐私和隐蔽性，攻击者常常对 ORP 进行定制修改，以访问被盗账户。

为应对大语言模型劫持攻击，保护访问密钥并实施强大的身份管理至关重要。最佳实践包括避免硬编码凭证、使用临时凭证、定期轮换访问密钥，以及监测暴露的凭证和可疑的账户行为。

本文翻译自hackread [原文链接](https://hackread.com/hackers-monetize-llmjacking-selling-stolen-ai-access/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/304030](/post/id/304030)

安全KER - 有思想的安全新媒体

本文转载自: [hackread](https://hackread.com/hackers-monetize-llmjacking-selling-stolen-ai-access/)

如若转载,请注明出处： <https://hackread.com/hackers-monetize-llmjacking-selling-stolen-ai-access/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [网络攻击](/tag/%E7%BD%91%E7%BB%9C%E6%94%BB%E5%87%BB)

**+1**17赞

收藏

![](https://p0.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p2.ssl.qhimg.com/t014757b72460d855bf.png)

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