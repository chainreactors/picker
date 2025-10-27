---
title: Llama-Code Shield解读：大模型代码安全护盾解析
url: https://mp.weixin.qq.com/s?__biz=MjM5NzE1NjA0MQ==&mid=2651206557&idx=1&sn=abeb0599973db60ec740c216d8334892&chksm=bd2cd63b8a5b5f2d43a93824451bee965f3c7af1bd8d20bf09c531903f4d33940c01f65da724&scene=58&subscene=0#rd
source: 腾讯安全应急响应中心
date: 2024-05-17
fetch_date: 2025-10-06T17:16:03.581273
---

# Llama-Code Shield解读：大模型代码安全护盾解析

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/JMH1pEQ7qP4lMhJy4M6Lzvy6F7cw0MxoaNsbvmt4cO7IHVSId1ZfXXZrkwrqCp1A1mCIw6U2icL4QcRBEP8Kmmg/0?wx_fmt=jpeg)

# Llama-Code Shield解读：大模型代码安全护盾解析

原创

腾讯朱雀实验室

腾讯安全应急响应中心

![](https://mmbiz.qpic.cn/mmbiz_gif/JMH1pEQ7qP4lMhJy4M6Lzvy6F7cw0MxoDZgSNC0DcUM5fPm9Hfly0KrU6GppiazQrwo0fbOVgn4kpSFZUiaTK4Yw/640?wx_fmt=gif&from=appmsg)

**引言**

大模型目前被广泛用于生成代码数据，能有效地提高研发效率。但LLM生成的代码中潜藏的安全漏洞，也成了悬在头顶的达摩克利斯之剑。最近，Llama-3的问世，不仅带来了新的代码生成能力，更配备了Code Shield这一安全检测利器，为LLM生成的代码筑起了一道坚固的防线。

腾讯朱雀实验室基于Llama-3开源的Code Shield项目，进行了相关的技术分析和实验测试。总体而言，Code Shield不仅为LLM生成的代码提供了安全检测的有效途径，更在误报率和扫描效率之间找到了平衡点。尽管当前开源版本的Code Shield在漏洞检测规则的使用上有所不足，但它的潜力巨大，只需根据项目需求添加相应的扫描检测规则，就能大幅提升检测成功率。

**1. 概述**

整体而言，Code Shield被嵌入了大模型部署的系统层面，专门对于LLM输入内容的代码安全进行监管和检测，其具体流程图如下图所示：

![](https://mmbiz.qpic.cn/mmbiz_png/JMH1pEQ7qP4lMhJy4M6Lzvy6F7cw0Mxokamdovo3SIPRtC76Mj2wUE1ia3ianl8zVEKLysvsxkl5L7s0N3yXd0rQ/640?wx_fmt=png&from=appmsg)

图1. Code Shield在生产部署环境中的流程图

**2. 技术分析：双层扫描，快速精准**

Code Shield通过两层扫描解决方案快速处理输入LLM生成的代码。根据Meta的技术报告，Code Shield将首先粗略扫描生成的代码，如果第一层扫描认为内容可疑，则进行更全面的分析。

Code Shield的项目介绍中显示，“在生产环境中，超过 98% 的流量被归类为良性流量，不需要进行全面扫描。这意味着在大约 99% 的情况下，请求会在 70 毫秒的时间内得到快速处理。对于需要更彻底扫描的剩余流量，现代生产服务器环境中的 p90 延迟为 450 毫秒”。这种优化确保 Code Shield 在不影响性能的情况下提供强大的安全性，使其成为安全性和速度都至关重要的生产环境的理想选择。

Code Shield使用了静态分析工具，即：不安全代码检测器（Insecure Code Detector，ICD），对 7 种编程语言进行分析，涵盖 50 多种 CWE。ICD具体包括了两种静态分析工具，Regex和Semgrep。前者为一个正则表达式的检测器，后者可以进一步识别代码模式，分析代码结构。

值得注意的是，ICD中覆盖的规则可以进一步结合业务代码需求进行补充。以Semgrep为例，Code Shield扫描规则中并没有直接覆盖使用Semgrep的全量规则，因此在漏洞检出率上有较大提升空间，具体实验结果在下文有较详细介绍。

**3. 落地实践效果**

从落地应用看，Code Shield在编码助手Codex系列和聊天机器人Chatbot系列的LLM应用上，都可以进行部署，用来提高生成代码的安全属性。为了对Code Shield代码安全检测能力进行综合测评，朱雀实验室分别在**LLM生成代码的应用场景和线下自有漏洞代码的应用场景**测试了Code Shield的综合能力。整体来看，Code Shield当前版本中，规则使用较为谨慎，在各类数据集上的漏洞检出率在10%以下。

**3.1 针对LLM生成代码的应用场景**

这是Code Shield主要设计的目标应用场景。之前研究表明，LLM在生成代码中会存在相当比例的漏洞代码。但针对LLM生成代码的具体场景，又存在一些应用差异。一方面CodeX系列的代码助手更多会通过生成/补全代码的方式进行编程辅助；另一方面，ChatBot系列的LLM本身进行了一些安全对齐，直接进行风险代码生成的要求会被拒绝。因此针对两类场景，我们分别设计了100条测试数据，使用Code Shield，对于LLM生成的代码进行了安全检测。

以CWE-119、CWE190为例，我们基于CWE漏洞类型设计了具体的prompt指令，使得LLM绕过安全限制，生成风险代码，并使用Code Shield进行检测验证。示例如下图所示。

![](https://mmbiz.qpic.cn/mmbiz_png/JMH1pEQ7qP4lMhJy4M6Lzvy6F7cw0MxoM3FWs4NOIkNky4wnR6om91SaXnQzRpXXrW7qBrET6jkO3WsxUuUwgg/640?wx_fmt=png&from=appmsg)

图2. CodeShield测试样例

**1）针对CodeX类的编程助手**

我们设计了50条prompt给出具体的代码生成指令，用来生成一些存在可能被利用的漏洞代码片段，我们共重复进行了2次代码生成任务，共获得了100条代码片段，覆盖了5种代码语言（C、C++、java、js、python），并使用Code Shield进行检测。其中有部分恶意prompt指令会在代码生成阶段被CodeX类编程助手合理避免并给出建议，但相当大部分仍会按照prompt给出有漏洞的风险代码内容。为了方便比较，我们也进一步对这些代码进行了人工校验标注。

![](https://mmbiz.qpic.cn/mmbiz_png/JMH1pEQ7qP4lMhJy4M6Lzvy6F7cw0MxoydMlL5VIOicsn8iaDmWs82D7iaXZehMYwGKmozkibUBKoOaLibRJsl4NMgQ/640?wx_fmt=png&from=appmsg)

表1. CodeX系列LLM上的Code Shield检测效果

**2）针对ChatBot类的LLM服务**

我们针对LLM（Llama-3， Llama-2， Code Llama等）也设计了50条prompt给出具体的代码生成指令，用来生成一些存在可能被利用的漏洞代码片段，共生成了50条代码数据，覆盖了5种代码语言（C、C++、java、js、python），并使用Code Shield进行检测。为了方便比较，我们也进一步对这些代码进行了人工校验。

![](https://mmbiz.qpic.cn/mmbiz_png/JMH1pEQ7qP4lMhJy4M6Lzvy6F7cw0MxoSOKj0wicWtTyz64iagrI4kZrjTa97UMiaFBjbOeP1kLAdNfry2ObeBngA/640?wx_fmt=png&from=appmsg)

表2. ChatBot系列LLM上的Code Shield检测效果

**3.2 针对线下自有漏洞代码的应用场景**

我们分别在开源漏洞代码数据集和自建漏洞代码数据集上对于Code Shield的代码安全检测能力进行了粗略测试。

**1）开源漏洞代码测试**

我们使用了200条业界常用的cve-fixes数据集【2】（104w条）和cwe test case数据集【3】（301条）。

![](https://mmbiz.qpic.cn/mmbiz_png/JMH1pEQ7qP4lMhJy4M6Lzvy6F7cw0MxoicNfCuDjZa1B1uZfptcHDLdb8mecGU1e7iaGyZAwaL8EicdY3mVicf5DFQ/640?wx_fmt=png&from=appmsg)

表3. 开源漏洞代码数据集上的Code Shield检测效果

**2）自建漏洞测试数据集**

我们使用了100条自建的业务漏洞数据，覆盖了4种漏洞类型（hardcode、SQLI、Command Injection、Code Injection）和5种不同代码语言（c、cpp、python、java、js）。其中，Code Shield整体检出率4%，误报率为0%。

值得注意的是，因为Code Shield本身是针对LLM生成代码进行的安全检测和防护，因此可能出于减少误报、不影响CodeX、LLM服务等角度考虑，本身提供的规则比较简单，也可以由用户自行增加扫描规则。因此3.2本小节测试并不是Code Shield应用的真实环境和目标场景，仅作为补充实验供大家参考。

**总结：Code Shield的潜力与未来**

Code Shield作为LLM生成代码的安全检测和防护工具，已经证明了其在提高代码安全性方面的有效性。虽然当前版本的规则设置较为宽松，但Code Shield的灵活性和可扩展性，随着更多定制化规则的加入，使其在未来的代码安全领域有着无限的可能。

参考文献

1. https://llama.meta.com/trust-and-safety/

2. GitHub - JHahn42/vulnerabilitydataset: C/C++ test cases formatted for input to an LSTM
3. https://huggingface.co/datasets/euisuh15/cveFixes1

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/JMH1pEQ7qP5asPR2KQZHIkuvt7d85Nic3JIRVcIMoJa1rEqMEkibSkxEptehGiaffy66vGXWxCrJ4ZbPibVYofAkyw/0?wx_fmt=png)

腾讯安全应急响应中心

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/JMH1pEQ7qP5asPR2KQZHIkuvt7d85Nic3JIRVcIMoJa1rEqMEkibSkxEptehGiaffy66vGXWxCrJ4ZbPibVYofAkyw/0?wx_fmt=png)

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