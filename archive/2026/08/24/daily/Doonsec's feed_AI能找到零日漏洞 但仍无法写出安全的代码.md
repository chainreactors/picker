---
title: AI能找到零日漏洞 但仍无法写出安全的代码
url: https://mp.weixin.qq.com/s/9bneN_4_er7aEt0zGZhlBg
source: Doonsec's feed
date: 2026-08-24
fetch_date: 2026-08-25T02:57:05.829615
---

# AI能找到零日漏洞 但仍无法写出安全的代码

# AI能找到零日漏洞 但仍无法写出安全的代码

数世咨询
数世咨询

内生安全联盟

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/2ZmL5d0ic88UaichSBdUE1lolf0iapNPh14ic8WEAUKmkdWyjBfibfyJYSHVSaHjS45HalEG0MV8ICYt5ZqAeUB02fcry7ANZPGFTFf3836YKBmU/640?wx_fmt=gif&from=appmsg#imgIndex=0)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/CpUPV7oBxfReFnwzTqDSv4gKKibZibIcX6r9tC6Gf2Oy0hxiaia6z4CmxBjyz8COXALNYFVpuDn8tHe5pmnqFicRuCUcwY220WPP2srhX8w9ic69Q/640?from=appmsg#imgIndex=1)

**本文关键看点：**

1、应用安全公司Veracode在过去一年进行的四次研究测试，共100多个模型版本中发现，AI生成代码的平均安全通过率几乎没有提升。44%的AI生成代码中至少包含一个已知的OWASP十大漏洞。

2、根据1Password的测试，六种主流大模型生成一个完全解决漏洞且未实质改变应用行为的补丁，平均成功率仅为26%。超过一半的LLM生成补丁未能解决漏洞。

3、专家一致认为，企业应保留现有的安全控制措施，而不是将基于AI的代码审查视为替代品。

********▍********以下正文内容基于英文原文编译，可能存在语义偏差，请以原文为准。

过去几个月，大语言模型（LLM）在网络安全领域完成了一次快速迭代：它们先是给开源项目和漏洞悬赏平台狂灌一些质量堪忧的安全报告，浪费了开发者大量时间；而现在已经能稳定发现人类与传统的安全审计工具多年都漏掉的零日漏洞——这种能力的进化速度，连它们自己的研发人员都感到害怕。

![](https://mmbiz.qpic.cn/mmbiz_png/lYWDmickZ2mzVN0ryakPJCsRaibgUYGh87mrqcavZHJHtSb3Q93r3icRULTFTxXRTOr980rVo13eib0qjlMAOUqUIibgcPJYFOFNSy8SialbvQdM8/640?wx_fmt=png&from=appmsg&watermark=1#imgIndex=0)

但与这种漏洞发现和利用能力相伴随的是AI模型在防御侧，尤其是代码生成与漏洞修补的进展明显更慢。它们生成出来的代码，仍然会留下大量基础性的安全缺陷。这一短板不仅只影响AI在软件开发中的广泛使用，也直接关系到AI能否为它自己能轻松发现和利用的漏洞提供有效补丁。

应用安全公司Veracode最近发布的研究显示，44%的AI生成代码至少包含一个已知的OWASP Top 10漏洞。即使是表现最好的前沿模型，安全通过率也没超过68%——也就是说，平均三次里仍会出现一次不安全的代码。

更值得注意的是，Veracode在过去一年里共做了四次研究快照，累计测试了100多个模型版本，AI生成代码的平均安全通过率几乎没有提升。

与此同时，所有受测模型的语法正确率高达99%。

Veracode首席安全布道师Chris Wysopal抛出了一个问题："为什么它们在语法上越来越强？为什么它们写漏洞利用代码越来越强，却写不出更安全的代码？这是我想问AI实验室的问题，也是我们试图衡量的东西。"

对于希望兑现AI加速软件开发承诺的IT领导者来说，这是个关键问题——尤其是在AI正把漏洞利用时间压缩到接近实时的当下。

攻防不对称

Veracode并不是唯一观察到LLM攻防能力不对称加剧的公司。荷兰软件质量保证公司Software Improvement Group（SIG）在其《2026年软件状况报告》的测试中发现，AI生成代码产生的安全风险违规大约是人类编写的两倍。

"我们还发现，所有代码（不只是AI代码）中，有71%的安全控制程度都偏低，"SIG的CTO Jasper Geurts在接受采访时表示。"AI并不是问题的制造者，而是放大器。在那些已经对代码质量进行度量和管理的企业里，AI加速了交付；而在没有这些基础的领域，AI只是在加速技术债和安全暴露。"

7月，由Theori开发的代码安全测试平台Xint.io的研究人员，使用Anthropic和OpenAI的5款较新AI模型vibe-code应用，并借助这些模型对一个已有人工编写的应用进行重新架构和安全加固。在28个应用变体中，研究人员发现并验证了434个安全缺陷，其中196个出现在新生成的代码库（greenfield，即全新构建）中，238个出现在被重新架构的应用（brownfield，即对既有应用的改造）中。

"总体上，我们发现AI生成代码中最常见的安全缺陷类型是这样的：代码仍然能编译——也就是说代码能跑，但会在内部留下密钥，或者在规模化运行时占用过多资源，"Theori旗下Xint的产品负责人Kay Kwak在接受采访时表示。"这在一定程度上是因为训练数据中的'捷径/快速起步'代码；另外，开发者通常只要求实现功能，而不会同时明确要求'加上安全护栏'。我们还发现，代码库越大、越复杂，AI就越容易丢失对细粒度用户权限的跟踪。"

Xint的研究表明，即使在已有代码库上工作，模型也难以生成安全的代码。这种问题延伸到了修复安全缺陷上——根据1Password旗下Off-By-1实验室的研究，他们针对复杂开源项目中6个已知且已修复的漏洞，测试了各种模型生成新补丁的质量。

在6,000多次测试中，生成一个能完全解决漏洞、且不会实质性改变应用行为的补丁，平均成功率仅为26%。超过一半的LLM生成补丁要么没有解决漏洞，要么引入了新的漏洞，要么两者兼而有之。

"我们的研究关注的是打补丁，所以观察到的更多是一个'编辑过程'，而非一个'全新创建过程'，"1Password的Off-By-1实验室负责人Keith Hoodlet在接受采访时表示。"因此，我们的研究和Veracode的研究应该被视为互补的，而不是在评估同一类挑战。话虽如此，我们的研究确实受到了他们研究的启发，而且两项研究在方向上都指向了相似的结论。"

单靠改进训练数据还不够

在AI实验室纷纷强调其模型在前沿漏洞研究上取得突破的同时，AI在安全代码生成与漏洞修复方面明显落后的原因，目前并不完全清楚。

Xint的Kwak认为，编写安全代码、并证明代码是安全的，本身就是难题。"这个困难并非AI所独有，"他说。"软件工程有一个'欠规范'问题：没有人会写下代码'不应该'做的所有事情。"

攻防场景对'成功'的不同定义，可能也部分解释了这种差距。攻击侧的'成功'相对容易验证：如果智能体能够复现或利用某个漏洞，结果就是具体的。但要判定一个补丁是否堵住了所有相关的利用路径与易受攻击的代码路径，难度就要大得多。

话虽如此，训练数据质量确实影响LLM的表现——可以合理推测，现有模型是基于大量质量与安全性参差不齐的公开代码训练出来的。

"我们听到的所有实验，都是他们在玩攻击能力、试图搞明白怎么去攻击——那些AI智能体就是这么'脱缰'的，"Veracode的Wysopal说，他指的是AI实验室近期的一系列事件——在这些事件中，智能体在测试期间突破了安全管控、对第三方系统发起了攻击。

"他们应该做的，是建立一个经过精心筛选的安全软件数据集，只用那份数据训练，告诉AI：忘掉你们之前在互联网随机代码上学到的那些东西，把那些全部丢掉，"他说。"从银行或者航电这类代码经过严格审查、明确已知安全的领域拿到最好的代码，然后只在那上面训练。这件事很难，也需要时间，但这是做防御的正确路径。据我所知，他们现在并没有这么做。"

与此同时，Hoodlet指出了LLM的另一个固有局限：注意力机制——即模型判断输入token上下文与相关性的方式。

"注意力机制是当前LLM运作方式的基础，它可能会从根本上限缩模型，使其永远无法完全解决修补漏洞的难题，"他说。"在我们论文的7.3节里，我们观察到：智能体生成的补丁，只覆盖了来自概念验证漏洞利用的某一条代码路径，而对相邻代码路径中字符级别相同的同一类漏洞却视而不见。考虑到这一固有局限，还需要多少训练才能产生更好的安全编码结果，目前并不清楚。"

Geurts认为，单纯改进训练的边际收益有限，因为模型默认并不掌握企业的架构、安全策略、威胁模型以及其他与具体应用相关的上下文。harness才能提供这些上下文，并把确定性的安全检查嵌入到开发流程中。

Harness工程仍是关键

Veracode的研究刻意使用了直接发给模型的极简提示，没有附加任何额外的安全指令——而这并非软件工程团队在实战中使用LLM的方式。其他研究则或多或少地加入了一些脚手架，但没有一项评估了一个成熟企业开发流水线中可能存在的全套控制措施——这些措施通常包括专门的AI编码助手、详细的规格说明、验证工作流、系统提示、MCP连接、技能定义以及其他配套工具。

这类Harness能够拉取相关文件与架构文档，提供威胁模型信息，列出已批准的编码模式，运行编译器与测试，调用静态和动态安全测试工具，并设置审批关卡——只有识别出的失败被处理掉，AI智能体才会被放行继续。

例如，OpenAI与Trail of Bits合作，让其模型去发现关键互联网基础设施相关的开源项目中的漏洞，并协助开发补丁。在名为"Patch the Planet"的项目中，研究人员搭建了专门的工作流与Harness。截至8月11日，该项目已记录1,250个问题、覆盖49个代码库，并提交了271个修复，其中146个被上游接受。

Kwak表示，Xint在内部测试中也观察到了类似的效果。公司针对包含17个注入漏洞的20.8万行代码评估了前沿模型。仅有裸提示的循环只找到了0到1个缺陷，而在Xint专用Harness内运行的模型能找到11到14个。

"裸提示循环打开的文件只占2.9%，而打不开的文件里就找不出bug，"Kwak说。

Harness可以决定哪些证据进入模型，哪些工具可以反驳模型的初步答案，什么算作'进展'，以及工作流应该在何时停止或升级。这种能力的重要性，在大型代码库中往往不亚于模型本身的选择。过去6个月里不乏这样的案例：能力相对较弱的开源模型，只要放在专门构建的Harness里，让其保持在正确轨道上、管理好它的"记忆"，表现就能与前沿模型持平。

SIG最近用Claude Sonnet 4.6把同一个测试项目构建了20次。其中10次只使用相同的模型、任务、脚手架、验收测试和初始指令；另外10次则额外通过MCP接入了公司的Sigrid Guardrails系统，作为强制性的安全与质量关卡。在SIG的分析下，带引导的运行所产生的高风险安全发现减少了约97%，可维护性得分则提高了24%。

"Harness就是AI智能体的'操作系统'，"Geurts指出。"它是让你放置约束条件、使智能体变得可靠的地方。没有它，AI跑得很快、看起来也很让人信服，哪怕它是错的。"

有效的Harness会把确定性分析工具嵌入到AI工作流中——比如代码检查器、类型检查器、安全扫描器和测试——它们会在智能体的输出得到验证之前阻止其继续。但即便有了精心构建的Harness，也不能保证一定没有漏洞残留。

"Harness的实施，很大程度上就是我们认为行业应该走的方向，"Off-By-1实验室的Hoodlet说。"如果你让工作流从'漏洞发现'走到'评审/裁决'，再走到'打补丁'，再走到'验证'，然后回到'漏洞发现'——要做多少轮循环才能达到90%或更高概率产出一份真正靠谱的补丁？10轮？100轮？还是1,000轮？这是我们想要进一步研究的东西。"

仍需人工监督

验证关卡和自动化检查可以减少流入开发者手中的有缺陷代码的数量，但它们并不会把责任转移到LLM身上。AI智能体可以基于扫描结果采取行动、运行测试、修订输出，但归根结底，组织仍需自行判断需求是否完整、验证是否充分、残留风险是否可接受。

Geurts认为，这改变了人工判断的着力点：随着企业规模化采用AI，人的角色会向上游移动——从"审代码"转向"治理该造什么、怎么造"。

专家一致认为，企业应保留现有使用的安全控制措施，而不是用基于AI的代码审查来替代它们。编译、类型检查、单元与集成测试、静态应用安全测试、软件组成分析、密钥扫描以及基础设施检查，可以分别捕获不同类型的安全失效。

"我们今天已有的所有控制措施都必须继续使用，但我们确实多了智能体式安全测试这一类新能力，"Wysopal在接受采访时说。他把确定性工具和基于AI的安全测试视为互补关系，因为它们各自能识别出对方漏掉的问题。

但归根结底，安全敏感的变更仍应保留在了解受影响代码及其在更大系统中角色的开发者手中。

"你不会让AI在没有任何人工参与的情况下部署你的软件——那你为什么要去追求那种能让你'跳过工程师'的'自动修复'式打补丁呢？"Kwak反问道。"合并变更和测试变更这些关键步骤，仍应是代码负责人的责任。"

来源：数世咨询

[![图片](https://mmbiz.qpic.cn/sz_mmbiz_jpg/2ZmL5d0ic88VEzjic1f7B8a9prz3icdEgQpXH1gOGyCYoZHyUAicqvDfdkVCKTCYm9qicEVTGF7fAosbaxdibXgxBT9na3DsrMjxBOyiadNzFvx5Po/640?wx_fmt=jpeg&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=2)](https://mp.weixin.qq.com/s?__biz=Mzg4MDU0NTQ4Mw==&mid=2247539413&idx=1&sn=477a535cc1c5dd21ac667eff0f60c271&scene=21#wechat_redirect)

[【征稿启事】2026 IEEE网络韧性与内生安全国际会议（IEEE CRESS 2026）相约南京，诚邀投稿！](https://mp.weixin.qq.com/s?__biz=Mzg4MDU0NTQ4Mw==&mid=2247539413&idx=1&sn=477a535cc1c5dd21ac667eff0f60c271&scene=21#wechat_redirect)

[![图片](https://mmbiz.qpic.cn/sz_mmbiz_gif/2ZmL5d0ic88Xr95JLPMCj3IEsZGAL0znMgDYy7QcmFibtBvxLR6nTbq4W4vTMnUhAdaobhKG9mibWfVugG7kFoImZBUEf8MqpF5H8AibmLbk1eI/640?wx_fmt=gif&from=appmsg&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=2)](https://mp.weixin.qq.com/s?__biz=Mzg4MDU0NTQ4Mw==&mid=2247538143&idx=1&sn=923217fe75c1c36cf9de5e5ac894ad10&scene=21#wechat_redirect)

[欢迎报名！“联盟货架” 征集工作正式启动](https://mp.weixin.qq.com/s?__biz=Mzg4MDU0NTQ4Mw==&mid=2247538143&idx=1&sn=923217fe75c1c36cf9de5e5ac894ad10&scene=21#wechat_redirect)

[聚力协同发展 | 中国质量认证中心有限公司南京分公司正式加入联盟，成为副理事长单位](https://mp.weixin.qq.com/s?__biz=Mzg4MDU0NTQ4Mw==&mid=2247538421&idx=1&sn=3ba126c3e04109879df4448e076a3494&scene=21#wechat_redirect)

2026-06-17

[![图片](https://mmbiz.qpic.cn/mmbiz_jpg/2ZmL5d0ic88XRibsIKXF2TFo31YtyfTpzRKp3lqA3JpyMFdGWKGGVtONQDgr2Hfm8pibrCwAiaQn5RWPJxTgelQxwFln0ZDrAwK8YuDWUgNaxFE/640?wx_fmt=jpeg&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=7)](https://mp.weixin.qq.com/s?__biz=Mzg4MDU0NTQ4Mw==&mid=2247538421&idx=1&sn=3ba126c3e04109879df4448e076a3494&scene=21#wechat_redirect)

[携手共建产业生态 | 紫光恒越正式升级联盟副理事长单位](https://mp.weixin.qq.com/s?__biz=Mzg4MDU0NTQ4Mw==&mid=2247538467&idx=1&sn=e66939c008f88f0003ccbc5fd9c08b81&scene=21#wechat_redirect)

2026-06-18

[![图片](https://mmbiz.qpic.cn/mmbiz_jpg/2ZmL5d0ic88Ug4pM2QBleSEh81Xt2icXIibBY5o6icibpSFMbFcu4TN9eNvibibict0BCDx8nCYrYViclCu2KGMdx7RnIAdrEvuSGtxKa20mBqH9IPhI/640?wx_fmt=jpeg&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=8)](https://mp.weixin.qq.com/s?__biz=Mzg4MDU0NTQ4Mw==&mid=2247538467&idx=1&sn=e66939c008f88f0003ccbc5fd9c08b81&scene=21#wechat_redirect)

****| 往期回顾****

**[AI4E如何重构数字生态系统网络发展范式？](https://mp.weixin.qq.com/s?__biz=Mzg4MDU0NTQ4Mw==&mid=2247532455&idx=1&sn=ee5102d94087e9440ede67b18386c621&scene=21#wechat_redirect)**

**[资料下载 | 十五五规划建议全文及说明](https://mp.weixin.qq.com/s?__biz=Mzg4MDU0NTQ4Mw==&mid=2247534593&idx=2&sn=7f9516f40cbafbcb1012d5999612157a&scene=21#wechat_redirect)**

**[《科技日报》整版访谈邬江兴院...