---
title: NDSS 2025｜Prompt泄露风险：抖音集团安全研究团队揭露多租户KV缓存共享漏洞
url: https://mp.weixin.qq.com/s?__biz=MzI1MzYzMjE0MQ==&mid=2247512517&idx=1&sn=5eeba37b918c35be1eb6209fed0aa9fc&chksm=e9d37a27dea4f3314f6b15c21cdad97ce21e9891d0e1ba2fb756e5fdd1ad4240630266dee1a2&scene=58&subscene=0#rd
source: 字节跳动技术团队
date: 2024-12-24
fetch_date: 2025-10-06T19:41:08.690327
---

# NDSS 2025｜Prompt泄露风险：抖音集团安全研究团队揭露多租户KV缓存共享漏洞

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/5EcwYhllQOhqvRciamjxlCCWg2do9wwaUQcPDYN5iaK8I6kOFdwF4vPmBgHTiahL3WzXhPkibht6yLVM5p8NjYT6Bw/0?wx_fmt=jpeg)

# NDSS 2025｜Prompt泄露风险：抖音集团安全研究团队揭露多租户KV缓存共享漏洞

原创

安全研究团队

字节跳动技术团队

抖音集团安全研究团队和南方科技大学可信系统安全实验室合作的研究论文揭示了大语言模型安全领域服务框架的侧信道漏洞，利用多租户场景下的KV缓存共享机制精确恢复了用户提示词。本工作成果《I Know What You Asked: Prompt Leakage via KV-Cache Sharing in Multi-Tenant LLM Serving》已被安全领域顶级会议NDSS 2025接收。

**一、研究背景**

大语言模型（LLM）在自然语言处理任务中取得了显著进展，广泛应用于文本生成、翻译、问答等领域，吸引了学术界和工业界的高度关注。这些模型在提供高效、准确的语言处理服务的同时，也面临着由于计算资源需求巨大所带来的性能瓶颈。为了满足不同用户的使用需求，优化资源利用率，大量多租户LLM框架应运而生，通过共享资源和更高效的调度算法，实现性能和成本的有效优化。

在众多多租户LLM的框架中，一个广泛应用的技术就是KV缓存共享（包括SGLang、vLLM等）。KV缓存共享的基本原理是允许不同请求在推理过程中复用已经计算过的KV缓存，但这种共享仅在前序token序列完全相同时才能实现。这种设计保证了不同用户的请求在一定程度上可以复用计算结果，提升了推理效率。目前SGLang提供了SOTA的KV缓存共享策略。具体而言，SGLang使用了一种基于Radix树的结构以便快速索引和访问。此外，SGLang实现了一种优化的调度算法，确保优先处理拥有更长复用匹配的请求，以最大化缓存命中率并减少重复计算。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/5EcwYhllQOhqvRciamjxlCCWg2do9wwaUBwgmTzGQUtUlugd28icIsGvu2lRseeqpibj2KQAcq9bTZjYm978E0eHw/640?wx_fmt=other&from=appmsg)

在我们最新发表于NDSS 2025的论文《I Know What You Asked: Prompt Leakage via KV-Cache Sharing in Multi-Tenant LLM Serving》中，我们首次利用不同用户间共享KV缓存的特性，实现了跨用户的提示窃取。这一研究揭示了当前多租户LLM服务框架在共享资源使用中的巨大潜在安全风险。抖音集团安全研究团队已经与SGLang建立联系，反映了上述安全问题。相关安全补丁将于近日提交至开源仓库。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/5EcwYhllQOhqvRciamjxlCCWg2do9wwaUFUtXycE2aQQDp4ryS5SKTicUzDo6V4EWM63zn9Uq32w0mG8TB2bCAjw/640?wx_fmt=other&from=appmsg)

#

# **二、攻击方法**

**攻击核心：如果攻击者能够观察到自身请求是否触发了KV缓存共享，则可以判断其请求与已处理的请求是否相同或部分相同。攻击者通过每次增加一个token并反复请求，从而逐个token地还原出其他用户的请求内容。**

接下来，我们用攻击过程中的一个片段来阐述攻击者如何还原其他用户请求中的一个token。通过反复重复这一操作，攻击者最终可以还原出完整请求。

如下图所示，假设目标语句是“Imagine you are an IT expert”，攻击者已经成功还原出“Imagine you are”，并企图还原出下一个token “an”。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/5EcwYhllQOhqvRciamjxlCCWg2do9wwaUoMynrukujXPsrIFRL1icxKWqnIKKic5sibiaO2FerdIl5kzDfib6cvrFJ7w/640?wx_fmt=other&from=appmsg)

* **本地候选生成：**攻击者利用本地LLM来生成可能的token。本地LLM不需要和目标LLM完全相同，只要拥有相同的Tokenizer来确保能够匹配到目标LLM的解析方法即可。在这个例子中，本地LLM可能会生成“a”，“an”，“the”等潜在的候选token。同时，本地LLM也会生成一个最不可能的token作为dummy token，为之后的攻击使用。
* **候选请求发送：**在生成本地候选之后， 攻击者会将三批请求依次发送，分别为由dummy token构成的dummy batch，候选token构成的候选batch，和另一批由dummy token构成的dummy batch。这样的设定是为了更容易观测到的侧信道信息。
* **侧信道结果观测：**通过观测发送请求的返回顺序作为侧信道信息，攻击者可以判断哪个请求成功触发KV缓存共享，从而确定对应的token。接下来我们对侧信道信息进行具体介绍。

**侧信道信息：我们利用调度算法的特性，即与已有KV缓存匹配更长的请求会被优先处理，来实现攻击。成功匹配的请求相比未匹配的请求多一个token匹配，因此更早被处理。我们将请求的返回顺序作为侧信道信息，通过观察哪个请求被优先返回，从而判断其是否触发了缓存共享。**

如下图所示，当我们按照三个批次发送请求后，是否有匹配到的请求会有不同的处理模式：

* **没有触发KV缓存共享：**对于没有触发的场景，dummy请求的匹配长度为4（在第一个dummy请求被处理后后续请求都会有更长的匹配长度），而candidates请求的匹配长度为3。所以具体处理顺序依次为：第一个dummy batch，第二个dummy batch，和candidates batch。
* **触发KV缓存共享：**对于成功触发KV缓存共享的场景，dummy请求的匹配长度依旧为4，此时成功匹配的匹配长度也为4，其他的未匹配的请求的匹配长度为3。所以此时的具体处理顺序为：第一个dummy batch，匹配到的请求，第二个dummy batch，和其余的candidates。这里第二个dummy batch可以帮助放大顺序改变带来的差异，从而能够令攻击者在端侧判断出顺序的改变。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/5EcwYhllQOhqvRciamjxlCCWg2do9wwaUQbSGrlGic8552RbdP0W4Fic2EwgcFB0TggFoMOQuOPMUVT3U9lQrGabw/640?wx_fmt=other&from=appmsg)

通过反复重复这一操作，攻击者最终可以还原出完整请求。

**三、实验结果**

**实验环境：**实验环境基于SGLang框架，用户请求设定参考了OpenAI的标准，每3小时发送40次请求，以模拟真实的LLM使用场景。提示数据集包含四类：常规聊天、填空、角色扮演和指令型提示，用于全面评估攻击效果和成本。

下图展示了攻击的最终效果。结果表明，在Llama2-13B模型上，攻击者在知晓提示模版来回复提示输入上成功率达99%，知晓提示输入恢复提示模板成功率为98%，甚至在无任何背景知识恢复全部请求也有95%的成功率。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/5EcwYhllQOhqvRciamjxlCCWg2do9wwaUylhNQon4JFO319VsIHaiaOPQtOrEk3q9tmpAz3NfHibndGiaRELdCtJ0g/640?wx_fmt=other&from=appmsg)

#

# **四、总结与展望**

**无状态与有状态设计：**本工作基于有状态的大语言模型服务框架，即对于用户的共享KV缓存，开展输入窃取攻击，而这种攻击的本质是针对于系统的状态延续所进行的。在大型系统中，用户数据的状态延续往往伴随着潜在的安全风险，所以为了确保安全要尽可能做到单次服务后清除用户状态，如苹果近期提出的Private Computing Cloud。然而，对于延迟要求较高的服务场景，复用缓存等有状态的设计难以避免，但面临着诸如本篇工作的安全挑战。在此基础上，我们已基于本篇工作提出了更安全的KV缓存共享框架，为大语言模型服务提供安全性保障的同时实现了效率的提升。

**多租户LLM框架下的资源共享：**现有的LLM服务框架会有很多允许多用户/多请求间的共享资源（如KV，memory，Lora adapter），这些共享资源可以很大程度的提高服务性能，但是存在巨大的安全隐患（隐私泄漏，投毒等），所以在设计框架和部署服务的过程中需要谨慎处理基于共享资源的优化。框架设计师和服务提供商需要在保持性能的同时引入足够的隔离机制来保证多租户间的安全性。

**KV缓存的安全性考量：**KV缓存作为LLM中的独特机制，虽然提升了推理效率，也为LLM的安全性带来了新的攻击面。KV缓存与用户的输入token存在唯一对应关系，这使得一旦出现KV缓存信息泄漏，攻击者便能够通过缓存内容直接推测和重构相应的用户请求，从而导致敏感信息的暴露。本篇工作是第一次注意到了KV缓存所带来的安全风险，希望能够引起广泛的针对这一新属性的安全思考。

**建立安全的LLM推理服务：**不知攻，焉知防？攻击的意义是为系统防御设计指明方向——我们对SGLang提交的安全策略可以大大提高攻击者的消耗，尽可能减少攻击面。然而，从LLM服务的全局视角出发，当前的LLM推理服务框架安全能力尚不完善，需要多种安全机制保驾护航。因此，安全研究团队正在基于机密计算及密码学技术，在兼容多种推理框架的前提下，提供大模型可信推理服务，欢迎大家交流参考。

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/5EcwYhllQOhkoWTP1gVm0Lqs480XOARyoSYjPEsRVCSF35cbWIp6cliaYic8KUfNfiaSjVnruzTQUTCA0lmv9vUmw/0?wx_fmt=png)

字节跳动技术团队

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/5EcwYhllQOhkoWTP1gVm0Lqs480XOARyoSYjPEsRVCSF35cbWIp6cliaYic8KUfNfiaSjVnruzTQUTCA0lmv9vUmw/0?wx_fmt=png)

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