---
title: FreeDrain：谷歌悄然发生加密货币盗窃案？大规模钓鱼网络曝光
url: https://www.anquanke.com/post/id/307302
source: 安全客-有思想的安全新媒体
date: 2025-05-13
fetch_date: 2025-10-06T22:23:23.621708
---

# FreeDrain：谷歌悄然发生加密货币盗窃案？大规模钓鱼网络曝光

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

# FreeDrain：谷歌悄然发生加密货币盗窃案？大规模钓鱼网络曝光

阅读量**58574**

发布时间 : 2025-05-12 14:26:56

**x**

##### 译文声明

本文是翻译文章，文章原作者 Ddos，文章来源：securityonline

原文地址：<https://securityonline.info/freedrain-silent-crypto-theft-on-google-massive-phishing-network-exposed/>

译文仅供参考，具体内容表达以及含义原文为准。

![攻击链摘要]()

攻击链摘要 | 图片：SentinelLABS

在 PIVOTcon 2025 大会上，SentinelLABS 和 Validin 的研究人员揭露了一场规模庞大的网络钓鱼活动，该活动一直在悄悄地从全球毫无戒心的用户手中窃取加密货币。这场名为 FreeDrain 的行动利用搜索引擎优化 (SEO)、免费虚拟主机和自动重定向链，无缝地实施大规模数字资产盗窃。

与依赖未经请求的电子邮件或恶意广告的传统网络钓鱼方法不同，FreeDrain 的攻击链始于用户感觉最安全的地方——主要搜索引擎。

报告解释说：“*受害者搜索与钱包相关的查询，点击排名靠前的恶意结果，进入诱饵页面，然后被重定向到窃取其种子短语的网络钓鱼页面。”*

研究人员证实，类似“Trezor 钱包余额”之类的查询经常会返回钓鱼链接，这些链接在 Google、Bing 和 DuckDuckGo 的搜索结果中都排在首页。这些页面看似简单，通常托管在 Gitbook.io、Webflow.io 或 Github.io 上，并包含一张类似加密钱包仪表盘的大型图片。

![加密网络钓鱼，FreeDrain]()

Trezor 钱包余额恶意导致 Google 搜索结果排名靠前 | 图片：SentinelLABS

单击图像会将用户重定向 – 有时会重定向到合法站点以建立信任，有时会经过多层重定向，最终重定向到托管在 AWS 或 Azure 上的网络钓鱼页面。

经过四个月的调查，研究人员发现了超过 38,000 个用于托管这些诱饵页面的独特子域名。其规模巨大，基础设施滥用也十分严重：

* 被滥用的平台：Gitbook、Webflow、GitHub Pages、Strikingly、WordPress、GoDaddySites 等
* 具有算法生成域名的重定向器，例如 causesconighty[.]com 和 posectsinsive[.]com
* 托管在 Amazon S3 或 Azure Web Apps 上的最终阶段网络钓鱼页面，模仿 Trezor、Ledger 和 MetaMask

报告警告称：*“这些并不是晦涩难懂或维护不善的网络钓鱼网站；而是专业制作的诱饵页面，免费托管在受信任平台的子域名上。”*

FreeDrain 运营者通过垃圾评论活动（即所谓的垃圾索引）将 SEO 武器化，目标是那些被遗弃或管理不善的网站。许多诱饵页面充斥着 AI 生成的文本，有时会草率地显示诸如“4o mini”（暗示 OpenAI 的 GPT-4o）之类的字符串。

为了逃避黑名单，攻击者使用拼写错误、零宽度空格和 Unicode 相似字符来伪装“Trezor”等关键词。

报告强调：*“一个引人注目的例子是，我们发现一个韩国大学相册页面，其中只有一张十多年前上传的图片，被埋在 26,000 条评论之下，几乎所有评论都包含垃圾链接。”*

一旦受害者输入钱包助记词，FreeDrain 的后端（通常是一个简单的 HTML 表单，其中包含 JavaScript POST 请求）就会将凭证发送到攻击者控制的端点。资金会在几分钟内被盗走，通常会通过加密货币混合器来避免被追踪。

报告警告说：“*尽管网络钓鱼后端很简单，但它却有效、可丢弃，而且通常难以追踪。 ”*

这并非一次完全自动化的攻击活动。SentinelLABS 和 Validin 在钓鱼页面上发现了 GitHub 提交元数据、Webflow 发布时间戳，甚至还有实时聊天互动——所有这些都表明攻击者可能来自印度，他们所在的时区是 UTC+05:30（印度标准时间）。

报告总结道：*“如果没有更强大的默认保护措施、身份验证或滥用应对基础设施，这些服务将继续被滥用。”*

本文翻译自securityonline [原文链接](https://securityonline.info/freedrain-silent-crypto-theft-on-google-massive-phishing-network-exposed/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/307302](/post/id/307302)

安全KER - 有思想的安全新媒体

本文转载自: [securityonline](https://securityonline.info/freedrain-silent-crypto-theft-on-google-massive-phishing-network-exposed/)

如若转载,请注明出处： <https://securityonline.info/freedrain-silent-crypto-theft-on-google-massive-phishing-network-exposed/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [安全资讯](/tag/%E5%AE%89%E5%85%A8%E8%B5%84%E8%AE%AF)
* [网络攻击](/tag/%E7%BD%91%E7%BB%9C%E6%94%BB%E5%87%BB)

**+1**4赞

收藏

![](https://p0.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p1.ssl.qhimg.com/t014757b72460d855bf.png)

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

* ##### [国庆重保+攻防演练大考在即！360大模型安全服务专项方案筑牢AI防线](/post/id/312460)

  2025-09-29 18:06:17
* ##### [Apache Airflow 存在权限漏洞，可导致只读用户获取敏感信息](/post/id/312457)

  2025-09-29 18:05:56
* ##### [Meta 旨在打造机器人领域的“Android”，为下一代人形AI提供通用平台](/post/id/312454)

  2025-09-29 18:05:34
* ##### [Formbricks 存在高危漏洞 (CVE-2025-59934)，攻击者可通过伪造JWT令牌导致未授权的密码重置](/post/id/312451)

  2025-09-29 18:05:05
* ##### [Notepad++ 中存在DLL劫持漏洞（CVE-2025-56383），可导致任意代码执行，且POC已公开](/post/id/312448)

  2025-09-29 18:04:33
* ##### [Morte僵尸网络被披露：正利用路由器与企业应用漏洞，迅速扩张其“加载器即服务”活动](/post/id/312444)

  2025-09-29 18:04:01
* ##### [Akira勒索软件利用SonicWall VPN账户发起急速入侵](/post/id/312438)

  2025-09-29 18:03:28

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