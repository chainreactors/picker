---
title: [已开源] 基于大语言模型的自动化漏洞修复技术实践
url: https://mp.weixin.qq.com/s?__biz=Mzg5NjAxNjc5OQ==&mid=2247484218&idx=1&sn=798de36b9ce61a02dfbbd11529d91ff6&chksm=c006cbcaf77142dc7bde37c43bbb2960b02b68e3d95bda0dfb1f432a8319c62337ab2f62c84f&scene=58&subscene=0#rd
source: RedTeam
date: 2025-02-23
fetch_date: 2025-10-06T20:37:19.912959
---

# [已开源] 基于大语言模型的自动化漏洞修复技术实践

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/6USuqjXjYk79ftHfR798mBibjHkDaibLDMGAV9hDyNJwJUwUic8dicF0a2QePqOSufwNCLxkyKqTqobxbSKVVPKk3Q/0?wx_fmt=jpeg)

# [已开源] 基于大语言模型的自动化漏洞修复技术实践

原创

tonghuaroot

RedTeam

**本文介绍了如何基于 Patchwork 框架与大语言模型，构建可定制化的自动化代码漏洞修复工具，覆盖静态扫描、漏洞验证、智能补丁生成与代码兼容性检测的完整技术闭环。**

## 前言

本节将介绍 Patchflow 的工作流程，用于创建可定制化的 AutoFix 工具，能够使用 LLM 自动检测和修复安全漏洞。

![](https://mmbiz.qpic.cn/mmbiz_png/6USuqjXjYk79ftHfR798mBibjHkDaibLDMicW2Alxgqy9aK1gVhPY7BicD6CU4ukXwCXpqibXF3jpRYyjdXRSLrBr5w/640?wx_fmt=png&from=appmsg)

在过去的一年中，许多搞 AppSec 的安全公司、开发工具提供商以及一些创业公司都发布了基于 LLM 的自动化代码漏洞修复工具。

但是，这些工具的灵活性较差，用户完全定定义配置和修改 prompts。

此外，这些工具通常不支持使用本地 LLM 或私有化的解决方案。

近期，我们与 OpenAI 合作，分享了如何构建 SOTA 的针对漏洞修复的微调模型。

我们还微调了开源模型，如 Llama-3.1。在我们微调工作的基础上，我们将展示如何使用我们开源框架 patchwork 构建自己的 AutoFix 工具。

AutoFix 工作流程概述：

![](https://mmbiz.qpic.cn/mmbiz_png/6USuqjXjYk79ftHfR798mBibjHkDaibLDMI2Olwic7ibcbNubZZqMicr4EeAWDfZskKe4zKYSibHib5AyDIjGdmQNibK8A/640?wx_fmt=png&from=appmsg)

## 克隆代码

第一步是获取你要分析的代码，可以通过克隆代码仓库并运行扫描以检测漏洞。需要注意的是，有些静态分析工具可以对二进制或字节码进行漏洞检测。但与只进行静态分析不同，我们需要访问源代码，因为在修复漏洞时需要源代码来生成修复补丁。

## 扫描漏洞

你可以使用许多开源漏洞扫描工具来查找代码中的漏洞。在我们的实现中，我们将使用 Semgrep，它是一个轻量级的扫描工具，具有可扩展的扫描规则集。Semgrep 已经与 Patchwork 集成，你可以通过在 Patchflow 中 call it as a step 来运行：

`ScanSemgrep(self.inputs).run()`

这一步会在当前文件夹内本地运行 Semgrep 命令，所以只要你克隆了代码仓库并进入该文件夹，就能使用 Semgrep 扫描该仓库。

Semgrep 提供了一组扫描规则，适用于在本地机器上扫描自己的代码。但如果你想通过应用程序或服务来运行扫描，你可以使用我们的 扫描规则集合。在 ScanSemgrep 步骤中，默认将扫描结果输出为标准格式 SARIF，这使得可以将其他静态分析工具集成进来，只要它们能输出 SARIF 格式。接下来的工作流程假定输入是 SARIF 格式，并基于此进行处理。

## 处理扫描结果

静态分析的结果可能包含误报，因此使用 LLM 对结果进行处理和分类，以排除误报是个不错的主意。我们可以将包含漏洞详细信息的 SARIF 报告与漏洞文件一起提供给 LLM，让它进行分类。如果我们简单地将整个 SARIF 报告提供给 LLM，可能会出现两个问题：首先，报告本身可能太大，超出模型的上下文长度；其次，最好将实际的源文件作为prompt的一部分，以便模型可以分析代码及其中的问题。

为了解决这个问题，我们可以处理 SARIF 报告，获取受影响源代码文件的文件路径。然后，我们可以使用 Patchwork 中的 ExtractCode 步骤来提取受影响的代码，作为模型的上下文部分。请注意，单个文件可能非常大，因此我们需要对文件进行分块并提取相关部分。所有这些工作都已在 ExtractCode 步骤中为你管理。如果你有兴趣，可以查看我们在 Patchwork 中实现的 上下文策略。

为了对扫描结果进行分析，我们可以使用类似如下prompt，并将 SARIF 报告中的漏洞详细信息与漏洞代码一起提供给 LLM。通过 LLM 输出特定的关键字（如），我们可以轻松解析输出结果。对于更复杂的输出结构，你也可以使用 JSON 模式。

```
You are a senior software engineer who is best in the world at triaging vulnerabilities. Do a vulnerability triage and analyze if the vulnerability can indeed be exploited in the given code.

If the vulnerability cannot be exploited, respond with <NOT VULNERABLE>.

else, If you cannot generate an exact fix for the vulnerability, respond with <NO FIX POSSIBLE>.

{{Vulnerability Details}}

{{Vulnerable Code}}
```

一旦我们解析了 LLM 的响应，就可以过滤掉被f分析为“不可被利用”或“无法修复”的漏洞。这有助于减少 Semgrep 报告中的误报。

## 生成补丁

接下来的步骤是生成实际的修复补丁来解决漏洞问题。我们可以很容易地通过 LLM 的 Prompt 来生成修复。

通过实验我们发现，给模型提供完整的文件或尽可能多的上下文，再要求修复问题，比只提供发现漏洞的那一行代码效果要好。因此，修复的提示看起来像这样：

```
You are an AI assistant specialized in fixing code vulnerabilities.

Your task is to provide corrected code that addresses the reported security issue.

Always maintain the original functionality while improving security.

Be precise and make only necessary changes.

Maintain the original code style and formatting unless it directly relates to the vulnerability.

Pay attention to data flow between sources and sinks when provided.

Vulnerability Report:

- Type: {cwe}

- Location: {lines}

- Description: {message}

Original Code:

{file_text}

Task: Fix the vulnerability in the code above. Provide only the complete fixed code without explanations or comments. Make minimal changes necessary to address the security issue while preserving the original functionality.
```

这是我们在 静态分析评估 中使用的 Prompt。生成的修复代码现在可以提交到仓库中。

## 检查兼容性

在生成补丁的过程中，LLM 可能会添加一些细节或修改代码，是的出现非预期的情况。为了避免这种情况，我们可以进行额外的检查，确定生成的补丁是否会引发兼容性问题。这可以通过类似于我们分类Prompt的方式来完成：

```
Do a brief change impact analysis to assess how these modifications might affect the overall system, considering both immediate and potential long-term compatibility issues.

Low: Code diff will be applied to the code base and automatically merged without review.

Medium: Code diff will be applied and a pull request will be sent to the developer to merge, but there are no indirect changes expected to be done in other parts of the system.

High: Code diff will be offered as a suggestion to the developer to review and then apply to the code base. There are likely other changes that need to be done by the developer before the change can be implemented.
```

当漏洞修复被分类为低、中、高时，你可以决定如何处理它们。例如，我们只为兼容性较高的补丁生成 PR，并对其他补丁仅给出修复建议。在 Patchwork 中，我们允许用户配置兼容性级别，只有在选择的级别下才会生成 PR。

## 创建 Pull Request

最后一步是创建 PR。Patchwork 中已经有一个 CreatePR 功能，可以将修改后的代码提交并生成 PR。这里展示了多个功能和 3 个不同的 prompt，在实现中，我们将这些工作简化为一个prompt，你可以在代码仓库中查看。你也可以查看 AutoFix 生成的 PR 示例：

![](https://mmbiz.qpic.cn/mmbiz_png/6USuqjXjYk79ftHfR798mBibjHkDaibLDMqC5F1L7X1dnd0Pk14icSiaWpOiaz2Vne3ia4U0D9NEtrP8tz2a13qy3Vmw/640?wx_fmt=png&from=appmsg)

上述是 AutoFix 的实现思路和实例，代码和相关文档请参考：https://github.com/patched-codes/patchwork/tree/main/patchwork/patchflows/AutoFix

以上内容编译自 patched

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