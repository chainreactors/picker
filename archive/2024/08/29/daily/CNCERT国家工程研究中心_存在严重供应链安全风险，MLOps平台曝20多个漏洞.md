---
title: 存在严重供应链安全风险，MLOps平台曝20多个漏洞
url: https://mp.weixin.qq.com/s?__biz=MzUzNDYxOTA1NA==&mid=2247546648&idx=1&sn=cb150b8f6ffe70f6026faf0867d2a5d4&chksm=fa9381d9cde408cf1c2866ce41eb8b47575dfdb10ec11865c14ab7d215fd37885b23f8ed099b&scene=58&subscene=0#rd
source: CNCERT国家工程研究中心
date: 2024-08-29
fetch_date: 2025-10-06T18:05:30.772313
---

# 存在严重供应链安全风险，MLOps平台曝20多个漏洞

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/GoUrACT176kYfsCD4us19ibxba9VnWDMuzPGZQ4YrNqbxRw2k6UpoFicyu0r2iaI2oVfd9wE7bhTfP2TC3oG2MZicg/0?wx_fmt=jpeg)

# 存在严重供应链安全风险，MLOps平台曝20多个漏洞

网络安全应急技术国家工程中心

网络安全研究人员警告称，在发现20多个漏洞后，机器学习（ML）软件供应链存在安全风险，这些漏洞可能被利用来针对MLOps平台。这些漏洞被描述为固有和实现方面的缺陷，可能会产生严重后果，从任意代码执行到加载恶意数据集。

![](https://mmbiz.qpic.cn/mmbiz_jpg/qq5rfBadR398GFTtRgzS3wjW2uMh15PgeibiaWeByTWnm2kxfOLwEibTRpxAOTR9AovNoBlsiaveZlxPkKmx5KdtGA/640?wx_fmt=jpeg&from=appmsg&tp=wxpic&wxfrom=5&wx_lazy=1&wx_co=1)

MLOps平台提供了设计和执行ML模型管道的能力，模型注册表作为存储和版本训练ML模型的存储库。然后可以将这些模型嵌入到应用程序中，或允许其他客户端使用API（即模型即服务）查询它们。

JFrog研究人员在一份详细报告中表示：“固有漏洞是由技术中所使用的底层格式和过程引起的。”固有漏洞的一些例子包括利用ML模型运行攻击者选择的代码，这是通过利用模型在加载时支持自动代码执行的事实（例如Pickle模型文件）。

这种行为也扩展到某些数据集格式和库，它们允许自动代码执行，从而在仅加载公开可用的数据集时就可能为恶意软件攻击敞开大门。另一个固有漏洞涉及JupyterLab（前身为Jupyter Notebook），这是一个基于Web的交互式计算环境，使用户能够执行代码块（或单元格）并查看相应的结果。

简单来说，攻击者可以输出恶意JavaScript代码，使其在当前JupyterLab笔记本中添加一个新单元格，将Python代码注入其中并执行它。特别是在利用跨站脚本（XSS）漏洞的情况下，这一点尤其明显。JFrog表示，它发现了一个MLFlow的XSS漏洞（CVE-2024-27132，CVSS评分：7.5），可导致在JupyterLab中执行客户端代码。

研究人员说：“我们从这项研究中的一个主要收获是，我们需要将ML库中的所有XSS漏洞视为潜在的任意代码执行，因为用户可能会将这些ML库与Jupyter Notebook一起使用。”

第二类漏洞涉及实现弱点，例如MLOps平台中缺乏身份验证，可能会允许具有网络访问权限的威胁行为者通过滥用ML管道功能获得代码执行能力。这些威胁并非理论上的，以经济利益为动机的对手可能滥用这些漏洞，如在未打补丁的Anyscale Ray（CVE-2023-48022，CVSS评分：9.8）的情况下，部署加密货币矿工。

第二种实现漏洞是针对Seldon Core的容器逃逸，使攻击者能够超越代码执行，在云环境中横向移动并访问其他用户的模型和数据集，方法是将恶意模型上传到推理服务器。它们不仅可以被武器化，在组织内部渗透、传播，还可以威胁服务器。

Palo Alto Networks Unit 42详细说明了开源LangChain生成式AI框架中的两个现已修复的漏洞（CVE-2023-46229和CVE-2023-44467），这两个漏洞可能允许攻击者执行任意代码和访问敏感数据。

上个月，Trail of Bits还揭示了Ask Astro中的四个问题，这是一个检索增强生成（RAG）开源聊天机器人应用程序，可能导致聊天机器人输出中毒、文档摄取不准确和潜在的拒绝服务（DoS）。

正如安全问题在人工智能驱动的应用程序中被暴露出来一样，人们也在设计技术来用最终目标欺骗大型语言模型（LLMs）产生易受攻击的代码来毒害训练数据集。

康涅狄格大学的一位学者表示：“与最近将恶意负载嵌入代码的可检测或不相关部分的攻击不同，CodeBreaker利用LLMs（例如GPT-4）进行复杂的负载转换（不影响功能），确保微调的毒害数据和生成的代码都可以规避强大的漏洞检测。”

**参考资料：**

https://thehackernews.com/2024/08/researchers-identify-over-20-supply.html

原文来源：FreeBuf

“投稿联系方式：sunzhonghao@cert.org.cn”

![](https://mmbiz.qpic.cn/mmbiz_jpg/GoUrACT176n1NvL0JsVSB8lNDX2FCGZjW0HGfDVnFao65ic4fx6Rv4qylYEAbia4AU3V2Zz801UlicBcLeZ6gS6tg/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/GoUrACT176mrRug7icLIhX4EvNQjNgGRibia7K9qOLTR5PDfQiaUesU9xge7pnF8iciaxVC3JVkNqHA2pvQDnrM0hDVQ/0?wx_fmt=png)

网络安全应急技术国家工程中心

向上滑动看下一个

知道了

![]()
微信扫一扫
使用小程序

取消
允许

取消
允许

取消
允许

×
分析

![跳转二维码]()

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/GoUrACT176mrRug7icLIhX4EvNQjNgGRibia7K9qOLTR5PDfQiaUesU9xge7pnF8iciaxVC3JVkNqHA2pvQDnrM0hDVQ/0?wx_fmt=png)

微信扫一扫可打开此内容，
使用完整服务

：
，
，
，
，
，
，
，
，
，
，
，
，
。

视频
小程序
赞
，轻点两下取消赞
在看
，轻点两下取消在看
分享
留言
收藏
听过