---
title: 新型 PoC 攻击可提取大模型关键架构
url: https://www.anquanke.com/post/id/293952
source: 安全客-有思想的安全新媒体
date: 2024-03-15
fetch_date: 2025-10-04T12:07:44.076245
---

# 新型 PoC 攻击可提取大模型关键架构

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

# 新型 PoC 攻击可提取大模型关键架构

阅读量**101940**

发布时间 : 2024-03-14 11:32:15

**x**

##### 译文声明

本文是翻译文章

原文地址：<https://www.darkreading.com/cyber-risk/researchers-develop-new-attack-for-extracting-secrets-from-chatgpt-other-genai-tools>

译文仅供参考，具体内容表达以及含义原文为准。

来自 Google DeepMind、Open AI、苏黎世联邦理工学院、麦吉尔大学和华盛顿大学的研究人员团队开发了一种新的攻击方法，用于从 ChatGPT 和 Google PaLM-2 等专有大语言模型 (LLM) 中提取关键架构信息。

该研究展示了对手如何从支持 LLM 的聊天机器人中提取所谓的隐藏数据，以便他们可以完全复制或窃取其功能。本周发布的一份技术报告中描述的这次攻击是过去一年中的几次攻击之一，这些攻击凸显了人工智能工具制造商在其产品采用率飙升的情况下仍然需要解决其技术中的弱点。

**提取隐藏数据**

正如新攻击背后的研究人员所指出的那样，公众对 GPT-4、Gemini 和 Claude 2 等大型语言模型的工作原理知之甚少。出于竞争和安全原因，这些技术的开发人员故意选择在模型中保留有关训练数据、训练方法和决策逻辑的关键细节。

研究人员在论文中指出：“尽管如此，虽然这些模型的权重和内部细节无法公开访问，但模型本身是通过 API 公开的。” 应用程序编程接口允许开发人员将 ChatGPT 等支持 AI 的工具集成到他们自己的应用程序、产品和服务中。这些 API 允许开发人员利用 GPT-4、GPT-3 和 PaLM-2 等 AI 模型来实现多种用例，例如构建虚拟助手和聊天机器人、自动化业务流程工作流、生成内容以及响应特定于领域的内容。

来自 DeepMind、OpenAI 和其他机构的研究人员希望了解他们可以通过 API 进行查询来从 AI 模型中提取哪些信息。与 2016 年的一次攻击不同，研究人员展示了如何通过在第一层或输入层运行特定提示来提取模型数据，研究人员选择了他们所描述的“自上而下”的攻击模型。目标是看看他们可以通过对负责根据输入数据生成输出预测的神经网络架构的最后一层或最后一层运行有针对性的查询来提取什么。

**自上而下的攻击**

该层中的信息可以包括有关模型如何处理输入数据、转换数据并通过一系列复杂的过程运行它以生成响应的重要线索。能够从这个所谓的“嵌入投影层”提取信息的攻击者可以获得对模型内部工作的宝贵见解，以便他们可以创建更多情感攻击、对模型进行逆向工程或尝试颠覆其行为。

研究人员表示，对这一层的成功攻击可以揭示“变压器模型的宽度，这通常与其总参数计数相关”。“其次，它稍微降低了模型作为完整‘黑匣子’的程度，这可能对未来的攻击有用。”

研究人员发现，通过攻击许多大模型的最后一层，他们能够提取有关模型的大量专有信息。研究人员写道：“我们的攻击花费不到 20 美元，提取了 OpenAI 的 ada 和 Babbage 语言模型的整个投影矩阵。” “我们还恢复了 gpt-3.5-turbo 模型的精确隐藏维度大小，并估计恢复整个投影矩阵的查询成本不到 2,000 美元。”

研究人员称，他们的攻击成功地恢复了目标人工智能模型的一小部分。但“事实上，完全有可能窃取生产模型的任何参数，这一事实令人惊讶，并引发了人们的担忧，即这种攻击的扩展可能能够恢复更多信息。”

在过去的一年里，还有许多其他报告强调了流行的 GenAI 模型的弱点。例如，本月早些时候，HiddenLayer 的研究人员发布了一份报告，描述了他们如何通过向Google 的 Gemini 技术发送精心构造的提示，使其以各种方式出现异常行为。其他人也发现了类似的方法来越狱 ChatGPT并让它生成不应该生成的内容。去年 12 月，来自 Google DeepMind 和其他地方的研究人员展示了如何通过提示ChatGPT 不断重复某些单词来提取 ChatGPT 的隐藏训练数据。

本文翻译自 [原文链接](https://www.darkreading.com/cyber-risk/researchers-develop-new-attack-for-extracting-secrets-from-chatgpt-other-genai-tools)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/293952](/post/id/293952)

安全KER - 有思想的安全新媒体

本文转载自:

如若转载,请注明出处： <https://www.darkreading.com/cyber-risk/researchers-develop-new-attack-for-extracting-secrets-from-chatgpt-other-genai-tools>

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