---
title: DeepSeek数据泄露——12000个硬编码的有效API密钥和密码遭曝光
url: https://www.anquanke.com/post/id/304864
source: 安全客-有思想的安全新媒体
date: 2025-03-01
fetch_date: 2025-10-06T21:55:49.124817
---

# DeepSeek数据泄露——12000个硬编码的有效API密钥和密码遭曝光

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

# DeepSeek数据泄露——12000个硬编码的有效API密钥和密码遭曝光

阅读量**387849**

|评论**1**

发布时间 : 2025-02-28 15:37:26

**x**

##### 译文声明

本文是翻译文章，文章原作者 Guru Baran，文章来源：cybersecuritynews

原文地址：<https://cybersecuritynews.com/deepseek-data-leak-api-keys-and-passwords/>

译文仅供参考，具体内容表达以及含义原文为准。

近期的一项分析发现，在公开抓取的网络数据中，存在 11908 个有效的 DeepSeek API 密钥、密码和身份验证令牌。

据网络安全公司 Truffle Security 称，这项研究凸显了在未经筛选的互联网快照上训练的人工智能模型，如何面临将不安全的编码模式内化并可能重现这些模式的风险。

在此之前，有披露显示大语言模型（LLMs）经常建议在代码库中硬编码凭证，这引发了人们对训练数据在强化这些行为中所起作用的质疑。

****DeepSeek 数据泄露****

Truffle Security 扫描了 Common Crawl 在 2024 年 12 月的 400TB 数据集，该数据集包含来自 4750 万个主机的 26.7 亿个网页。研究人员使用他们的开源工具 TruffleHog，识别出：

（1）11908 个已验证有效的机密信息，可用于认证访问亚马逊云服务（AWS）、Slack 和 Mailchimp 等服务。

（2）276 万个包含暴露凭证的网页，其中 63% 的密钥在多个域名中重复使用。

（3）一个 WalkScore API 密钥在 1871 个子域名中重复出现 57029 次，这表明凭证重用现象普遍存在。

值得注意的是，该数据集包含高风险的暴露信息，比如前端 HTML 中的 AWS 根密钥，以及在单个网页的聊天功能中硬编码的 17 个独特的 Slack 网络钩子。

Mailchimp API 密钥在泄露中占比最大（超过 1500 个实例）。它们通常直接嵌入客户端 JavaScript 中，这种做法为网络钓鱼活动和数据窃取提供了便利。

Common Crawl 的数据集存储在 90000 个 WARC 文件中，保留了抓取网站的原始 HTML、JavaScript 和服务器响应。

Truffle Security 部署了一个由 20 个节点组成的 AWS 集群来处理该存档，使用awk命令分割文件，并通过 TruffleHog 的验证引擎扫描每个片段。

该工具能够区分有效的机密信息（通过相关服务进行认证）和无效字符串 —— 鉴于大语言模型在训练过程中无法辨别有效凭证，这是至关重要的一步。

研究人员面临着基础设施方面的障碍：WARC 文件的流式传输效率低下最初减缓了处理速度，不过通过对 AWS 的优化，下载时间缩短了 5 – 6 倍。

尽管面临这些挑战，该团队优先考虑以合乎道德的方式进行披露，与 Mailchimp 等供应商合作撤销了数千个密钥，避免了向各个网站所有者进行类似垃圾邮件的通知。

这项研究凸显了一个日益严峻的困境：在公开可访问数据上训练的大语言模型继承了这些数据的安全缺陷。虽然像 DeepSeek 这样的模型采用了额外的保障措施，如微调、对齐技术和提示限制，但训练语料库中普遍存在的硬编码机密信息，可能会使不安全的做法常态化。

无实际功能的凭证（例如占位符令牌）也加剧了这个问题，因为大语言模型在生成代码时无法根据上下文评估它们的有效性。

Truffle Security 警告称，在多个客户端项目中重复使用 API 密钥的开发人员面临更高的风险。例如，一家软件公司共享的 Mailchimp 密钥暴露了与其账户关联的所有客户端域名，这对攻击者来说犹如一座宝库。

****缓解措施****

为了遏制人工智能生成的漏洞，Truffle Security 建议：

（1）通过 GitHub Copilot 的自定义指令等平台，将安全防护措施集成到人工智能编码工具中，这些措施可以执行禁止硬编码机密信息的策略。

（2）扩展机密扫描程序，将存档的网络数据纳入其中，因为历史上泄露的数据可能会重新出现在训练数据集中。

（3）采用符合道德规范的人工智能技术，使模型与安全最佳实践保持一致，减少敏感模式的无意暴露。

随着大语言模型在软件开发中发挥越来越重要的作用，保障其训练数据的安全不再是可有可无的 —— 这是构建更安全数字未来的基础。

本文翻译自cybersecuritynews [原文链接](https://cybersecuritynews.com/deepseek-data-leak-api-keys-and-passwords/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/304864](/post/id/304864)

安全KER - 有思想的安全新媒体

本文转载自: [cybersecuritynews](https://cybersecuritynews.com/deepseek-data-leak-api-keys-and-passwords/)

如若转载,请注明出处： <https://cybersecuritynews.com/deepseek-data-leak-api-keys-and-passwords/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [数据泄露](/tag/%E6%95%B0%E6%8D%AE%E6%B3%84%E9%9C%B2)

**+1**6赞

收藏

![](https://p5.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p2.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p5.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=175868)

[安全客](/member.html?memberId=175868)

这个人太懒了，签名都懒得写一个

* 文章
* **376**

* 粉丝
* **1**

### TA的文章

* ##### [mavinject.exe 遭利用，黑客绕过安全防线入侵系统](/post/id/306961)

  2025-04-28 10:48:18
* ##### [Docker 惊现新型加密挖矿攻击，借 Teneo 平台开辟恶意获利新路径](/post/id/306959)

  2025-04-28 10:39:59
* ##### [Cloudflare 隧道遭滥用，恶意 RAT 传播威胁加剧](/post/id/306957)

  2025-04-28 10:34:35
* ##### [xrpl.js 库遭供应链攻击，超 290 万次下载用户私钥成窃取目标](/post/id/306953)

  2025-04-28 10:29:02
* ##### [恶意后门借 ViPNet 更新渗透，俄罗斯多行业数据安全拉响警报](/post/id/306951)

  2025-04-28 10:22:13

### 相关文章

* ##### [航空公司向国土安全局出售乘客数据](/post/id/308408)

  2025-06-12 15:39:51
* ##### [西门子能源紧急警报：专用 5G 核心中的关键漏洞 (CVSS 9.9) 暴露了敏感数据！](/post/id/308380)

  2025-06-12 14:24:14
* ##### [德克萨斯州交通部 (TxDOT) 数据泄露事件暴露了 30 万份车祸报告](/post/id/308355)

  2025-06-11 16:33:57
* ##### [税务解决方案公司 Optima Tax Relief 遭勒索软件攻击，数据泄露](/post/id/308262)

  2025-06-09 17:29:27
* ##### [美国电话电报公司（AT&T）再次遭遇大规模身份数据泄露事件](/post/id/308193)

  2025-06-06 15:22:45
* ##### [美实名爆料：马斯克领导的DOGE被指入侵劳工机构系统，敏感数据疑遭泄露](/post/id/306743)

  2025-04-21 16:48:48
* ##### [天主教连锁医院：2023年黑客攻击影响近90万人](/post/id/303966)

  2025-02-08 11:09:24

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