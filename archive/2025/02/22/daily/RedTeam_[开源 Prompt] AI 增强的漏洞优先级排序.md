---
title: [开源 Prompt] AI 增强的漏洞优先级排序
url: https://mp.weixin.qq.com/s?__biz=Mzg5NjAxNjc5OQ==&mid=2247484194&idx=1&sn=ba76460d3a11bacb42d7e202d16181ae&chksm=c006cbd2f77142c41e4a49452be7eec286310a5de92e5470abe17c4d70060461949dbc0f45cb&scene=58&subscene=0#rd
source: RedTeam
date: 2025-02-22
fetch_date: 2025-10-06T20:40:13.098897
---

# [开源 Prompt] AI 增强的漏洞优先级排序

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/6USuqjXjYk6D5wAkPx7gbc7rd9PY5ZTibPks6eCib7hduqJPeSqTe8AmdImrXbCGOXfKSBehqgNM7l4X7Ky4hibDw/0?wx_fmt=jpeg)

# [开源 Prompt] AI 增强的漏洞优先级排序

原创

tonghuaroot

RedTeam

**Databricks 利用 LLM 针对第三方组件漏洞进行优先级排序，准确率达到了85%，安全团队人工分析的工作量减少了超过95%。**

## 前言

如何针对第三方组件的安全漏洞进行修复的优先级排序是一个行业难题。人工监控和分析每天发布的大量安全漏洞信息的成本非常高。

Databricks 安全团队的目标之一是保障数据智能平台的安全。工程团队设计了一个基于人工智能的系统，可以在漏洞公开的第一时间，根据漏洞的严重性、潜在影响及与Databricks基础设施的相关性，主动检测、分类并优先排序这些漏洞。

这一方法帮助Databricks有效减少了关键漏洞被忽视的风险。通过该系统，在识别对业务至关重要的漏洞时，准确率达到了约85%。借助优先级排序算法，安全团队人工分析的工作量减少了超过95%。他们现在能够集中精力处理仅占5%的需要立即行动的漏洞，而无需筛查数百个安全问题。

![](https://mmbiz.qpic.cn/mmbiz_png/6USuqjXjYk6D5wAkPx7gbc7rd9PY5ZTib5ibPBaJXyemSRYkadE3iaFO88nSniaVicqHXWCb0femJ5SZJU5CG9c0Uicw/640?wx_fmt=png&from=appmsg)

**接下来，我们将探讨如何利用人工智能驱动的方法如何帮助识别、分类和排序漏洞。**

# 如何持续标记漏洞

该系统按照固定时间表定期识别并标记关键漏洞。该过程包括以下几个关键步骤：

1. 收集并处理数据
2. 生成相关特征
3. 利用人工智能提取CVE信息
4. 根据漏洞的严重性进行评估和评分
5. 为进一步处理生成 Jira 工单

下图展示了整体工作流程。

![](https://mmbiz.qpic.cn/mmbiz_png/6USuqjXjYk6D5wAkPx7gbc7rd9PY5ZTibN5bIialHmk0URHNGMFSN6CptaMo3yZs6KiadSh2IXicR54zdccUtfmJyg/640?wx_fmt=png&from=appmsg)

# 数据提取

我们提取了CVE数据，这些数据来源于多个渠道，识别并记录公开披露的网络安全漏洞，包括：

* Intel Strobes API: 提供软件包和版本的详细信息。
* GitHub Advisory Database: 当漏洞未作为CVE记录时，通常会以GitHub安全公告的形式出现。
* CVE Shield: 提供来自社交媒体的漏洞趋势数据。

此外，我们还收集了来自securityaffairs和hackernews等渠道的RSS订阅源以及其他提到网络安全漏洞的新闻文章和博客。

# 特征生成

接下来，我们将为每个CVE提取以下特征：

* 漏洞描述
* CVE的发布时间
* CVSS评分
* EPSS评分
* 影响评分
* 漏洞是否可以被利用
* 是否有修复补丁
* 在X平台的趋势状态
* 通知次数

虽然CVSS和EPSS评分能提供关于漏洞严重性和可利用性的有价值信息，但在某些场景下，它们可能不完全适用于漏洞的优先级排序。

CVSS评分并未完全反映一个组织的具体环境，因此，若受影响的组件未被使用或已通过其他安全措施缓解，即便CVSS评分较高，该漏洞的紧急性也可能较低。

同样，EPSS评分估算漏洞被利用的概率，但它未考虑组织的特定基础设施或安全状况。因此，一个高EPSS评分的漏洞可能一般情况下会被利用，但如果受影响的系统不在组织的攻击面内，则该漏洞可能并不相关。

单纯依赖CVSS和EPSS评分可能会导致过多的高优先级告警，从而使得漏洞管理和优先级排序变得困难。

# 漏洞评分

我们基于上述特征开发了一个综合评分系统：漏洞*严重性评分、组件评分和相关性评分，*来实现针对 CVE 漏洞的优先级排序，具体如下：

## 严重性评分

该评分帮助量化CVE漏洞的影响。我们通过对CVSS、EPSS和影响评分的加权平均来计算该评分。来自CVE Shield和其他新闻源的数据帮助我们评估安全社区及同行公司对某一CVE影响的看法。此评分的值较高则意味着该漏洞对行业和我们公司的影响较大。

## 组件评分

该评分量化了CVE对我们组织的重要性。组织中的每个库都会根据其所影响的服务分配一个分数。影响关键服务的库将获得更高的评分，而影响非关键服务的库评分则较低。

![](https://mmbiz.qpic.cn/mmbiz_png/6USuqjXjYk6D5wAkPx7gbc7rd9PY5ZTibzIw0hG1wNJlQ25MCzWhLymcibzroLibKqp2NHqd1g3jaPbrfIiaL3Dn9g/640?wx_fmt=png&from=appmsg)![](https://mmbiz.qpic.cn/mmbiz_png/6USuqjXjYk6D5wAkPx7gbc7rd9PY5ZTibUO2e9GrdEqT4WF6hquWYgBU8cic363ibB4FGWpj59zqE5UqibjffN7G8g/640?wx_fmt=png&from=appmsg)

### **基于人工智能的库匹配**

通过少量Prompt并使用LLM，我们从CVE描述中提取相关库。随后，我们利用基于人工智能的向量相似度方法，将识别出的库与Databricks现有库进行匹配。

在匹配CVE涉及的库（组件）与Databricks库时，必须理解不同库之间的依赖关系。例如，IPython中的漏洞可能不会直接影响CPython，但CPython中的问题可能会影响到IPython。同时，库名称的变化（如"scikit-learn"、"scikitlearn"、"sklearn"或"pysklearn"）也必须考虑在内。此外，特定版本的漏洞也应被考虑进去。例如，OpenSSL版本1.0.1到1.0.1f可能存在漏洞，但在后续版本如1.0.1g到1.1.1中可能已修复这些安全问题。

LLMs通过运用先进的推理能力和行业知识，提升了库匹配的准确性。我们通过使用真实数据集对多个模型进行微调，进一步提高了依赖包识别的准确度。

![](https://mmbiz.qpic.cn/mmbiz_png/6USuqjXjYk6D5wAkPx7gbc7rd9PY5ZTib45peswRLmEJ9w8PAGVbMOJygpbXzibEah5CsxpuSTBGqeY94wL1Pvlg/640?wx_fmt=png&from=appmsg)

下面的表格展示了与特定CVE相关的Databricks漏洞库实例。首先，通过人工智能相似性搜索来定位与CVE库密切相关的库。接着，使用LLM来验证这些相似库在Databricks中的漏洞。

![](https://mmbiz.qpic.cn/mmbiz_png/6USuqjXjYk6D5wAkPx7gbc7rd9PY5ZTib2lMAA9tKgaowib5YTqy4xHQ3LkUjI05VU8SEOiax14bTVZar2t5tTLkA/640?wx_fmt=png&from=appmsg)

手动优化LLM提示中的指令可能繁琐且容易出错。更高效的方法是使用迭代方法自动生成多组指令，并通过真实数据集优化它们的表现。这种方法减少了人为错误，并确保随着时间的推移更有效地提升指令的准确性。

我们应用了这一自动化指令优化技术来改进我们基于LLM的解决方案。最初，我们为LLM提供了指令和期望输出格式，并通过产品安全团队提供的人类标注数据进行了对比。

随后，我们使用第二个LLM——"指令调优器"。我们将初始提示和真实数据集的错误反馈输入该模型。通过迭代生成的改进提示，我们最终选出了表现最佳的版本。

![](https://mmbiz.qpic.cn/mmbiz_png/6USuqjXjYk6D5wAkPx7gbc7rd9PY5ZTibzLibibc16BdXPtbqeIhzjBQPEic5o6yHk2q9ib1WulIU66xrkwhbJ3iaBDg/640?wx_fmt=png&from=appmsg)

**自动化指令优化**

通过应用LLM指令优化技术，我们开发了以下经过精炼的提示：

```
You are an advanced language model that takes in a software library (which has a vulnerability) and a list of software libraries and determines which (if any) of the libraries in the given list of libraries are at risk.

When classifying software library names based on input text, follow these guidelines:

1. **Identify Specificity**: Select the most relevant and specific library name(s) directly associated with the input text.

2. **Avoid Over-Inclusion**: Do not include unrelated or broader library names that do not directly match the input text.

3. **Prioritize Primary Libraries**: If the input text refers to a well-known software or tool, prioritize the primary library name(s) associated with it.

4. **Handle Ambiguity**: If the input text is ambiguous or does not clearly refer to a specific library, return ['No Library'].

5. **No Library Found**: If no relevant library(s) is found, return ['No Library'].

Examples:

- Input: GStreamer, ["gstreamer1.0-plugins-base","gstreamer1.0-clutter-3.0","gstreamer1.0-gl","gstreamer1.0-pulseaudio","gstreamer1.0-x","gstreamer1.0-libav","gstreamer1.0-plugins-good"]

- Output: ['gstreamer1.0-plugins-base', 'gstreamer1.0-clutter-3.0', 'gstreamer1.0-gl', 'gstreamer1.0-pulseaudio', 'gstreamer1.0-x', 'gstreamer1.0-libav', 'gstreamer1.0-plugins-good']

- Input: radeon_rx_6700, ["libdrm-radeon1", "xserver-xorg-video-radeon"]

- Output: ['No Library']
```

### **选择合适的LLM**

我们使用一个包含300个手动标注示例的真实数据集进行了微调。测试的LLM包括gpt-4o、gpt-3.5-Turbo、llama3-70B和llama-3.1-405b-instruct。通过对真实数据集进行微调后，gpt-3.5-turbo-0125的准确率明显高于基础模型，而llama3-70B的微调效果仅略有提升，接近gpt-3.5-turbo-0125的准确度。

### **准确度比较**

下图展示了各种LLM微调后的准确度比较。通过对gpt-3.5-turbo-0125进行微调后，其准确率得到了显著提升，而llama3-70B在微调后的改进幅度较小，接近gpt-3.5-turbo-0125的表现。其他模型，如gpt-4o和llama-3.1-405b-instruct，表现出类似的微调效果。

![](https://mmbiz.qpic.cn/mmbiz_png/6USuqjXjYk6D5wAkPx7gbc7rd9PY5ZTibTZ08iaa0KqEkED7gOJCrTnjWaTzzffE61THWThZeceHuOLsqP8LtK8g/640?wx_fmt=png&from=appmsg)

**不同LLM的准确度比较**

一旦确定了CVE中涉及的Databricks库，我们会将该库的相应评分（即上文提到的*库评分*）作为CVE的组件评分。

## 相关性评分

在我们的方案中，我们利用了相关性评分，特别是LDA方法，将库根据它们所关联的服务进行聚类。每个库作为一个文档，而它所在的服务则作为该文档中的词汇。这种方法使我们能够有效地将库归类为具有共同服务上下文的主题。

下图展示了一个具体的实例，其中所有的Databricks运行时（DBR）服务被聚集在一起，并通过pyLDAvis进行了可视化展示。

![](https://mmbiz.qpic.cn/mmbiz_png/6USuqjXjYk6D5wAkPx7gbc7rd9PY5ZTib7YWIFAkf0O2A1esM2TM7G4U7xh7KhXk8oxjVocJRCgeKHmFB7xMDEw/640?wx_fmt=png&from=appmsg)

**显示Databricks运行时服务聚类**

对于每个识别出的相关性，我们都会为其分配一个反映其在我们基础设施中重要性的评分。这个评分使我们能够通过关联每个CVE与相关库的相关性评分，来更准确地优先排序漏洞。例如，如果一个库出现在多个关键服务中，那么该库的相关性评分将会更高，从而导致其相关CVE被赋予更高的优先级。

![](https://mmbiz.qpic.cn/mmbiz_png/6USuqjXjYk6D5wAkPx7gbc7rd9PY5ZTibzm19yxSs5E9HaL0kB9GcrxqLYTXe16Ria84xWolmg0e5wDmVcjqVJ7w/640?wx_fmt=png&from=appmsg)

**CVE相关性评分**

# **影响和结果**

我们利用多种聚合技术对上述评分进行整合。我们的模型通过三个月的CVE数据进行了测试，取得了约85%的正确率，成功识别出了与我们业务相关的CVE。该模型能够在CVE发布的当天（第0天）就准确指出关键漏洞，并标记出需要安全调查的漏洞。

为了评估模型产生的漏报，我们对比了由外部来源或安全团队人工分析的漏洞，这些漏洞未被模型检测到。通过这种方式，我们计算了漏检的关键漏洞百分比。值得注意的是，在回测数据中并未出现漏报。然而，我们仍然认识到需要在这一领域进行持续监控和评估。

我们的系统有效地简化了工作流程，将漏洞管理过程转变为更加高效、聚焦的安全筛查步骤。它大大降低了忽视对客户有直接影响的CVE的风险，并且减少了超过95%的人工分析的工作量。这一效率提升使得我们的安全团队能够将精力集中在少数几个漏洞上，而不必每一天都处理成百上千的漏洞信息。

### **总结**

通过引入基于人工智能的漏洞优先级排序方法，Databricks不仅显著提高了漏洞管理的效率，而且也加强了对关键漏洞的响应能力。通过准确识别和排序漏洞，安全团队能够更加聚焦于最需要关注的漏洞，大大减少了漏检和误判的可能性。随着人工智能技术的不断进步，我们相信这种自动化的漏洞检测和优先级排序将成为更多组织提升网络安全防护的重要工具。

文章编译自 Databricks

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/6USuqjXjYk7KoXCtYjrNnB2XprMPwXgFMP2CGxa880Qdfw9zo3A3rl7TTUJF0iaI90KwgZMTem4JVjDSS3XrClw/0?wx_fmt=png)

RedTeam

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/6USuqjXjYk7KoXCtYjrNnB2XprMPwXgFMP2CGxa880Qdfw9zo3A3rl7TTUJF0iaI90KwgZMTem4JVjDSS3XrClw/0?wx_fmt=png)

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