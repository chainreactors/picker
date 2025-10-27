---
title: 研究人员在 MLOps 平台中发现了 20 多个供应链漏洞
url: https://www.anquanke.com/post/id/299523
source: 安全客-有思想的安全新媒体
date: 2024-08-28
fetch_date: 2025-10-06T18:03:48.419393
---

# 研究人员在 MLOps 平台中发现了 20 多个供应链漏洞

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

# 研究人员在 MLOps 平台中发现了 20 多个供应链漏洞

阅读量**60944**

发布时间 : 2024-08-27 11:03:45

**x**

##### 译文声明

本文是翻译文章，文章原作者 Ravie Lakshmanan，文章来源：The Hacker News

原文地址：<https://thehackernews.com/2024/08/researchers-identify-over-20-supply.html>

译文仅供参考，具体内容表达以及含义原文为准。

在发现 20 多个可能被利用以 MLOps 平台为目标的漏洞后，网络安全研究人员警告机器学习 （ML） 软件供应链中存在安全风险。

这些漏洞被描述为固有和基于实现的缺陷，可能会产生严重的后果，从任意代码执行到加载恶意数据集。

MLOps 平台提供了设计和执行 ML 模型管道的能力，模型注册表充当存储库，用于存储和版本训练的 ML 模型。然后，这些模型可以嵌入到应用程序中，或者允许其他客户端使用 API（也称为模型即服务）查询它们。

“固有漏洞是由目标技术中使用的底层格式和流程引起的漏洞，”JFrog 研究人员在一份详细报告中说。

固有漏洞的一些示例包括滥用 ML 模型来运行攻击者选择的代码，方法是利用模型支持在加载时自动执行代码的事实（例如，Pickle 模型文件）。

此行为还扩展到某些数据集格式和库，这些格式和库允许自动执行代码，因此在仅加载公开可用的数据集时，可能会为恶意软件攻击打开大门。

另一个固有漏洞实例涉及 JupyterLab（以前称为 Jupyter Notebook），这是一个基于 Web 的交互式计算环境，使用户能够执行代码块（或单元）并查看相应的结果。

“许多人不知道的一个固有问题是在 Jupyter 中运行代码块时处理 HTML 输出，”研究人员指出。“你的 Python 代码的输出可能会发出 HTML 和 [JavaScript]，你的浏览器会很高兴地呈现它们。”

此处的问题在于，JavaScript 结果在运行时不会从父 Web 应用程序进行沙盒化，并且父 Web 应用程序可以自动运行任意 Python 代码。

换句话说，攻击者可以输出恶意 JavaScript 代码，以便在当前 JupyterLab 笔记本中添加一个新单元格，将 Python 代码注入其中，然后执行它。在利用跨站点脚本 （XSS） 漏洞时尤其如此。

为此，JFrog 表示，它在 MLFlow 中发现了一个 XSS 缺陷（CVE-2024-27132，CVSS 评分：7.5），该漏洞源于在运行不受信任的配方时缺乏足够的清理，导致客户端代码在 JupyterLab 中执行。

“我们从这项研究中得出的主要收获之一是，我们需要将 ML 库中的所有 XSS 漏洞视为潜在的任意代码执行，因为数据科学家可能会将这些 ML 库与 Jupyter Notebook 一起使用，”研究人员说。

第二组缺陷与实现弱点有关，例如 MLOps 平台中缺乏身份验证，可能允许具有网络访问权限的威胁行为者通过滥用 ML Pipeline 功能来获得代码执行功能。

这些威胁不是理论上的，出于经济动机的对手滥用这些漏洞，正如在未修补的 Anyscale Ray（CVE-2023-48022，CVSS 评分：9.8）的情况下观察到的那样，以部署加密货币矿工。

第二种类型的实现漏洞是针对 Seldon Core 的容器逃逸，它使攻击者能够超越代码执行，在云环境中横向移动，并通过将恶意模型上传到推理服务器来访问其他用户的模型和数据集。

将这些漏洞链接起来的最终结果是，它们不仅可能成为渗透和传播组织内部的武器，而且还会破坏服务器。

研究人员说：“如果你正在部署一个允许模型服务的平台，你现在应该知道，任何可以提供新模型的人实际上也可以在该服务器上运行任意代码。“确保运行模型的环境完全隔离并针对容器逃逸进行强化。”

在披露这一消息之际，Palo Alto Networks Unit 42 详细介绍了开源 LangChain 生成式 AI 框架中现已修补的两个漏洞（CVE-2023-46229 和 CVE-2023-44467），这些漏洞可能分别允许攻击者执行任意代码和访问敏感数据。

上个月，Trail of Bits 还揭示了检索增强一代 （RAG） 开源聊天机器人应用程序 Ask Astro 中的四个问题，这些问题可能导致聊天机器人输出中毒、文档摄取不准确和潜在的拒绝服务 （DoS）。

正如人工智能驱动的应用程序中暴露出安全问题一样，人们也在设计技术来毒害训练数据集，最终目标是诱骗大型语言模型 （LLM） 生成易受攻击的代码。

“与最近将恶意负载嵌入代码的可检测或不相关部分（例如评论）的攻击不同，CodeBreaker 利用 LLM（例如 GPT-4）进行复杂的负载转换（不影响功能），确保用于微调的中毒数据和生成的代码都可以逃避强大的漏洞检测，”康涅狄格大学的一组学者说。

本文翻译自The Hacker News [原文链接](https://thehackernews.com/2024/08/researchers-identify-over-20-supply.html)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/299523](/post/id/299523)

安全KER - 有思想的安全新媒体

本文转载自: [The Hacker News](https://thehackernews.com/2024/08/researchers-identify-over-20-supply.html)

如若转载,请注明出处： <https://thehackernews.com/2024/08/researchers-identify-over-20-supply.html>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [网络安全热点](/tag/%E7%BD%91%E7%BB%9C%E5%AE%89%E5%85%A8%E7%83%AD%E7%82%B9)
* [漏洞情报](/tag/%E6%BC%8F%E6%B4%9E%E6%83%85%E6%8A%A5)

**+1**0赞

收藏

![](https://p3.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p0.ssl.qhimg.com/t014757b72460d855bf.png)

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

* ##### [Apache Airflow 存在权限漏洞，可导致只读用户获取敏感信息](/post/id/312457)

  2025-09-29 18:05:56
* ##### [Formbricks 存在高危漏洞 (CVE-2025-59934)，攻击者可通过伪造JWT令牌导致未授权的密码重置](/post/id/312451)

  2025-09-29 18:05:05
* ##### [Notepad++ 中存在DLL劫持漏洞（CVE-2025-56383），可导致任意代码执行，且POC已公开](/post/id/312448)

  2025-09-29 18:04:33
* ##### [CISA称黑客利用GeoServer漏洞成功入侵一联邦机构](/post/id/312347)

  2025-09-24 16:45:06
* ##### [SolarWinds紧急发布补丁，修复高危远程代码执行漏洞CVE-2025-26399](/post/id/312357)

  2025-09-24 16:43:11
* ##### [Chrome浏览器存在高危漏洞，可致攻击者窃取敏感信息并引发系统崩溃](/post/id/312366)

  2025-09-24 16:42:08
* ##### [CVE-2025-55241：CVSS评分10.0的Microsoft Entra ID漏洞可能危及全球所有租户](/post/id/312294)

  2025-09-22 18:14:51

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