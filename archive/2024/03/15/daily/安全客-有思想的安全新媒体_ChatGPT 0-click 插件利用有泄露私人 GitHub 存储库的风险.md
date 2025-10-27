---
title: ChatGPT 0-click 插件利用有泄露私人 GitHub 存储库的风险
url: https://www.anquanke.com/post/id/293915
source: 安全客-有思想的安全新媒体
date: 2024-03-15
fetch_date: 2025-10-04T12:07:52.626866
---

# ChatGPT 0-click 插件利用有泄露私人 GitHub 存储库的风险

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

# ChatGPT 0-click 插件利用有泄露私人 GitHub 存储库的风险

阅读量**77206**

发布时间 : 2024-03-14 10:28:08

**x**

##### 译文声明

本文是翻译文章

原文地址：<https://www.scmagazine.com/news/chatgpt-0-click-plugin-exploit-risked-leak-of-private-github-repos>

译文仅供参考，具体内容表达以及含义原文为准。

ChatGPT 及其多个第三方插件中的漏洞存在泄露用户对话和其他帐户内容的风险，其中包括零点击漏洞，该漏洞可能使攻击者能够访问受害者的私人 GitHub 存储库。

ChatGPT 插件漏洞是由 Salt Security 旗下的 Salt Labs 发现的，该实验室在周三的博客文章中发布了其研究成果。据 Salt Labs 称，这些问题分别于 2023 年 7 月和 9 月向 ChatGPT 和插件开发人员报告，现已得到解决。

ChatGPT 插件现在被称为通过自定义 GPT 提供的“操作”，代表了不断发展的“生成式 AI 生态系统”，允许像 ChatGPT 这样的大型语言模型 (LLM) 访问其训练数据之外的信息。

这些插件允许 ChatGPT 向其他网站（包括用户的私人第三方帐户）发送和接收潜在敏感数据，从而创建新的潜在攻击媒介。

Salt Security 研究副总裁 Yaniv Balmas 在一份声明中表示：“我们最近在 ChatGPT 中发现的漏洞说明了保护此类技术中的插件的重要性，以确保攻击者无法访问关键业务资产和执行帐户接管。”

**ChatGPT、多个插件中发现 OAuth 实现缺陷**

SaltLabs 团队发现的三个主要漏洞都涉及开放授权 (OAuth) 标准的错误实现。OAuth 允许应用程序访问其他网站上帐户的信息，而用户无需直接向应用程序提供登录凭据。

许多 ChatGPT 插件或自定义 GPT 使用 OAuth 来允许 ChatGPT 访问第三方网站上用户帐户的数据。尝试执行某些插件操作将提示 ChatGPT、用户和第三方站点之间请求和交换 OAuth 令牌。

如果实施不当，OAuth 令牌可能会被拦截、重定向或以其他方式滥用，从而允许攻击者访问受害者的帐户或将受害者的帐户连接到恶意应用程序。

Keeper Security 首席执行官兼联合创始人 Darren Guccione 表示：“越来越多的员工将专有数据输入人工智能工具，包括知识产权、财务数据、业务策略等，而恶意行为者未经授权的访问可能会给组织造成严重损害。” ，在一封电子邮件中告诉 SC Media。

Salt Labs 发现的 OAuth 缺陷之一是在 PluginLab 中发现的，PluginLab 是许多开发人员用来为 ChatGPT 创建插件的框架。研究人员发现，使用 PluginLab 开发的多个插件容易受到零点击漏洞的攻击，攻击者可以在这些插件使用的网站（包括 GitHub）上访问受害者的帐户。

研究人员演示了如何在“AskTheCode”插件上使用该漏洞，该插件允许用户查询其 GitHub 存储库。他们发现从 AskTheCode 发送到 PluginLab 授权页面的 OAuth 请求要求基于用户的“memberID”提供令牌；由于 PluginLab 没有对这些请求进行身份验证，因此攻击者可以更改请求以插入任何用户的 memberID。

我们发现，任何已经知道目标电子邮件地址的攻击者都可以轻松获取 memberID，因为该 ID 是用户电子邮件地址的 SHA-1 哈希值；还发现 PluginLab API 端点在使用包含用户电子邮件的请求进行调用时会泄漏 memberID。

一旦攻击者从包含目标 memberID 的请求中获取 OAuth 令牌，他们就可以将此令牌转发到 ChatGPT 并使用 AsktheCode 从 ChatGPT 界面访问受害者的 GitHub 存储库。这将包括请求所有私有存储库的列表并读取特定文件的能力，这可能会暴露专有代码、私钥和其他机密信息。

Salt Labs 描述的另外两个漏洞利用需要受害者点击链接来暴露他们的个人数据。其中之一是在 ChatGPT 本身中发现的，涉及攻击者创建自己的插件并让 ChatGPT 从攻击者控制的域请求 OAuth 令牌。生成 OAuth 令牌后，用户将被重定向到包含 OAuth 代码的 OpenAI 链接进行身份验证。

如果攻击者将此链接发送给受害者，并且受害者已登录其 OpenAI 帐户，则单击该链接将自动将攻击者的插件安装到其帐户中，而无需任何确认。然后，该插件可能会从受害者的 ChatGPT 对话中收集敏感信息。

\*第三个漏洞是在多个 ChatGPT 插件中发现的，其中包括“Charts by Kesem AI”，该插件无法验证 OAuth 令牌发送到的“redirect\_uri”链接。这允许攻击者插入自己的域作为redirect\_uri，并将更改后的身份验证链接发送到目标。

当目标单击该链接时，他们自己的帐户（例如他们的 Kesem AI 帐户）的 OAuth 令牌将发送给攻击者，然后攻击者可以使用它通过 ChatGPT 访问受害者的帐户内容。

“这些漏洞凸显了审查第三方集成的重要性，即使是在 ChatGPT 等可信平台内也是如此。IT 领导者应该在允许员工使用之前建立内部协议来审查插件，”Critical Start 的网络威胁情报研究分析师 Sarah Jones 在一封电子邮件中告诉 SC Media。

**生成式人工智能生态系统为网络威胁创造了新的攻击面**

虽然 ChatGPT 插件漏洞在发现后不久就得到了修复，但生成式 AI 工具的快速发展和采用仍然带来了许多新出现的风险。Salt Labs 表示，计划发布有关其研究人员在 ChatGPT 的自定义 GPT 市场中发现的网络风险的更多研究，该市场将取代旧的插件系统。

利用生成式人工智能的威胁多种多样，从敏感的法学硕士输入被盗，到提示操纵，再到大量生成令人信服的网络钓鱼电子邮件。据 HiddenLayer 称，本周还披露了谷歌 Gemini AI 中的漏洞，该漏洞可能允许攻击者获取隐藏的系统提示或滥用 Gemini Advanced 扩展来操纵用户输入敏感信息。

微软和 OpenAI 上个月还透露，来自俄罗斯、朝鲜、伊朗的国家资助黑客使用 ChatGPT 来执行从脚本帮助到目标侦察和漏洞研究等任务。

Guccione 表示：“随着组织急于利用人工智能来获得竞争优势并提高运营效率，快速实施这些解决方案的压力不应优先于安全评估和员工培训。”

本文翻译自 [原文链接](https://www.scmagazine.com/news/chatgpt-0-click-plugin-exploit-risked-leak-of-private-github-repos)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/293915](/post/id/293915)

安全KER - 有思想的安全新媒体

本文转载自:

如若转载,请注明出处： <https://www.scmagazine.com/news/chatgpt-0-click-plugin-exploit-risked-leak-of-private-github-repos>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [人工智能](/tag/%E4%BA%BA%E5%B7%A5%E6%99%BA%E8%83%BD)

**+1**4赞

收藏

![](https://p5.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p3.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p5.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=170061)

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

* ##### [人工智能可能修复帮助传播了 15 年的漏洞](/post/id/308401)

  2025-06-12 15:19:33
* ##### [浅析新型网络犯罪DeepSeek AI实战应用](/post/id/305102)

  2025-03-18 10:38:20
* ##### [360SRC x Hacking Group丨「奇御」AI安全技术沙龙议题征集！](/post/id/302279)

  2024-11-28 17:43:31
* ##### [从误用到滥用： 人工智能风险与攻击](/post/id/300992)

  2024-10-17 11:00:07
* ##### [一种用于网络钓鱼攻击的生成式人工智能恶意软件](/post/id/300410)

  2024-09-25 14:16:34
* ##### [苹果加入美国政府对人工智能安全的自愿承诺](/post/id/298565)

  2024-07-31 11:23:56
* ##### [Vanta筹集1.5亿美元，加速其AI产品创新](/post/id/298358)

  2024-07-25 15:02:41

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