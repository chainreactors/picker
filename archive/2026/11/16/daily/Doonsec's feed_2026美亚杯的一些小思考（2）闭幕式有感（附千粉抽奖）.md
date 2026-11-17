---
title: 2026美亚杯的一些小思考（2）闭幕式有感（附千粉抽奖）
url: https://mp.weixin.qq.com/s/_YmDPNf8e4ngjt-H3kEDYA
source: Doonsec's feed
date: 2026-11-16
fetch_date: 2026-11-17T09:56:04.565847
---

# 2026美亚杯的一些小思考（2）闭幕式有感（附千粉抽奖）

# 2026美亚杯的一些小思考（2）闭幕式有感（附千粉抽奖）

原创

ljnljn
ljnljn

ljnljn学习之路

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

本来不打算再写第二篇，但今天参加完会议后，确实有一些困惑和落差，还是决定把公开信息中可讨论的部分整理出来

下面我想围绕美亚杯个人赛第一名公开分享中的解题报告部分，做一点技术层面的复盘和讨论。本文不针对选手个人，也不否定主办方和 Qiko 的整体工作，只是就公开信息中一些配置、流程和结果之间的匹配度提出疑问，供大家理性讨论。若有信息不完整或理解偏差，也欢迎各位师傅补充指正

![](https://mmbiz.qpic.cn/mmbiz_jpg/3Bkxl9ud7XMnp7DxoUECBUciaIpTTZVAkGbT643vmevIfQamwCSoPTlTz3Yjbhd3ITYZk6OXGL7Vic2YEBJaeInwGtMnxDsjicicPpmyVfrGhcE/640?wx_fmt=jpeg&from=appmsg)

## 题目讲解

首先看到ppt，这一看就是ai-generated的，谁会闲得无聊左下角写这个右下角写页码，这个时候基本上我对内容就没什么恋想了，这少说几千个人看的直播竟然不自己手搓一个PPT，这是对自己十分自信还是不给主办方面子 接下来就是对题目的讲解，首先讲解的时候结结巴巴的，因为我本人参加了团队赛的答辩，如果真的自己做了一点的话应该对题目内容会很熟悉，就不会隔一会卡一会（包括后面的师傅们也是非常清晰的给出了思考过程） ![](https://mmbiz.qpic.cn/sz_mmbiz_png/3Bkxl9ud7XNMDAJXvOCkCIZ3P29qJLTPhGPzG3LrlW8Ac0X9OgaFhx4bYfiaoVrlsMZyibKk0QhN4oMdciaYrLr4GiajnyhR3wwqjYOHIuqBkiac/640?wx_fmt=png) 这个让我想起了答辩的时候要是脑子里啥都没有就会出现的情况（我说的是在学校里 接下来就是最不能理解的部分了

## 大模型参与电子数据取证？

![](https://mmbiz.qpic.cn/mmbiz_png/3Bkxl9ud7XPzwqOtYiap9nGbct7WaOYFyLZolyLdJ9ClBhiaWHsV8bEtrpfg4EXhMQoW49tUmDZicicqYXmnQDBnxNf0XfqzkJOsO5OBYlx1VB4/640?wx_fmt=png) 如果是有准备美亚杯线下且了解过DGX Spark的师傅们应该都知道，目前来说主要的部署方案，单机就是qwen3.8-flash-next，我这里也是简单问了下ai，我贴出删去废话的记录和结果 问：qwen3.8flashnext和qwen3.6 35b a3b、qwen3.8 27b差了多少

答：这三款模型分属不同的技术路线，差异显著。**Qwen3.8-Flash-Next 是能力顶尖但体积庞大的“巨无霸”**，而 **Qwen3.6-35B-A3B 和 Qwen3.8-27B 则是为高效、本地部署而生的“精悍选手”**，其中后者更是以较小的参数量实现了越级的性能。

核心规格速览

| 特性 | **Qwen3.8-Flash-Next** | **Qwen3.6-35B-A3B** | **Qwen3.8-27B** |
| --- | --- | --- | --- |
| **模型架构** | 稀疏 MoE (混合专家) | 稀疏 MoE (混合专家) | **稠密模型** |
| **总参数量** | **125B** | 35B | 27B |
| **激活参数量** | **~6B** | **~3B** | **27B** (全部激活) |
| **上下文窗口** | 原生 256K / 可扩展1M | 原生 256K / 可扩展1M | 原生 262K / 可扩展1M |
| **多模态能力** | 文本、图像、视频 | 文本、图像 (视觉语言) | 文本、图像、视频 |
| **定位** | 云端性能旗舰，兼顾本地 | 极致能效的智能体编程利器 | 小体积、高性能的本地部署之王 |
| 问：如果dgx spark上部署的话哪个最合适，我打取证比赛 |  |  |  |

如果是在 **DGX Spark 上打取证比赛，最务实的选择是 Qwen3.8-27B**。它是在单台 DGX Spark 上能稳定、高效部署，并且足以应对取证分析任务的“甜点”模型。 你提到的另外两款模型，情况比较特殊：**Qwen3.8-Flash-Next 是性能天花板，但在单台 DGX Spark 上部署非常折腾**；而 **Qwen3.6-35B-A3B 则是特定场景（如搭配智能体）下的高效选择**。

⚙️ 在 DGX Spark 上的部署现实 DGX Spark 的核心是 **128GB 统一内存**（实际可用约 121GB），这个容量是决定模型能否顺畅运行的关键。 **Qwen3.8-27B：部署最顺畅，性能足够** 它是三者中最省心的。其 NVFP4 量化版本权重仅需 **21-25GB**，远低于 DGX Spark 的内存上限。在 DGX Spark 上，使用 SGLang 等引擎可以达到约 **23 tok/s** 的单流生成速度，这个速度对于交互式分析来说是完全可用的。它有充足的内存余量来维持**长上下文**，这对于分析大体积的日志、内存镜像或流量包至关重要。 **Qwen3.6-35B-A3B：官方优化，适合工具链整合** 这款模型在 DGX Spark 上也有官方验证过的部署方案，NVFP4 版本可以正常运行，并支持 **262K** 的长上下文。它的优势在于**激活参数仅 3B**，在理论上能提供更快的响应速度。在“美亚杯”的实战分析中，就有选手使用它在 DGX Spark 上搭配智能体（Qiko 3.0）进行代码阅读和线索归纳。如果你的比赛流程高度依赖智能体调用外部取证工具，它是个不错的选择。

> 注释：这里有个很搞笑的地方，把另一个公众号发的文章已经加入进去了

**Qwen3.8-Flash-Next：性能最强，但单机部署门槛极高** 这是你需要特别注意的一点。Qwen3.8-Flash-Next 的 NVFP4 检查点大小为 **126 GiB**，**无法完整放入单台 DGX Spark 的 128GB 统一内存中**。可行的部署方式非常复杂：

* **双机集群**：需要两台 DGX Spark 通过高速网络组成 TP=2 集群才能比较顺畅地运行。
* **单机极限操作**：在单机上，必须将模型的 N-gram 表**文件化卸载到 NVMe SSD** 上才能勉强运行，这会引入额外的 I/O 延迟和复杂性。 除非你愿意接受双机方案或进行极限优化，否则在紧张的比赛环境中，Flash-Next 的部署和维护成本可能会成为负担。
  > 注释：其实目前来看部署交给ai是完全没有问题的，我在之前的文章中也有提到过，而且部署大模型不应该先问下ai哪个好吗，反复试错不是正确的方式

🎯 取证比赛场景的匹配度 在取证比赛中，模型的**长上下文能力**和**对非结构化数据的理解力**是关键。

* **Qwen3.8-Flash-Next 在实战中表现惊艳**：有选手在“龙信杯”中使用其量化版（IQ3\_S，200K上下文），**在物联网固件和流量分析题目上达到了约 80% 的准确率**，展现了强大的原始分析潜力。它的性能无疑是顶尖的，但这是以巨大的部署开销为代价的。
* **Qwen3.8-27B 是能力与成本的平衡点**：27B 的稠密架构在提供强大推理能力的同时，对硬件的要求远低于 Flash-Next。它拥有完整的**多模态**能力和长上下文窗口，足以处理取证中常见的日志、代码和部分图像/视频数据。在单机 DGX Spark 上，你能用它获得一个**开箱即用、性能可靠**的分析引擎，把精力集中在解题上，而非调试部署。
* **Qwen3.6-35B-A3B 是智能体流程的“效率核心”**：它的 MoE 架构在效率上有天然优势。在“美亚杯”的技术分析中，它被定位为智能体（Agent）流程中的“大脑”，负责理解代码和文本，然后由智能体去调用具体的取证工具（如 Qiko）。如果你的比赛策略是构建自动化分析流水线，它是一个非常合理的组件。

好的，deepseek给我们推荐了qwen3.8-flash-next和qwen3.8-27b是最佳选择，那么实际上用了什么呢？ ![](https://mmbiz.qpic.cn/mmbiz_png/3Bkxl9ud7XMRhKUd0V1ib6NHtkjMc6Sw7W0Yf8IoJTrricvPGPSYwzCUuAElsiaEEZiaibGdlAkGriczGsDZkPWKESPvKJt3icKjrEC3Onx3jQboog/640?wx_fmt=png) 一台Spark+35b a3b+Qiko，就能跑出个人赛第一的成绩，我这次也是去线下看了，其他选手的设备有4台dgx的、星睿的、4090的，咋就没跑过我们的参赛选手呢？ 因为我的电脑上也只能跑这个模型，所以我对这个模型有深度的了解，总的来说就是个child级别，没有做非常深度的优化基本上无法做到解出题目来 ![](https://mmbiz.qpic.cn/mmbiz_png/3Bkxl9ud7XMVtoGjmsMKLicMOZ2qqibQmzmhnm4uLlBjpLkkzrV71XvUSZrIvLic72bcAEuibclquY5sPPZV35JicVqibwn5fJrh7LOcda1KDPk98/640?wx_fmt=png) 我自己的取证Agent用的qwen3.8 flash next，效果还是很不错的 ![](https://mmbiz.qpic.cn/sz_mmbiz_png/3Bkxl9ud7XNX4xfgAfQY9RYwkGDzlRkunCXDspMQl7E3TGR3v3F4yeYUFPpRtg3Xc41jYo5iaxbTMOnWJ6Z1cHWE3OwoXnyTTKtaAjF7e2ia0/640?wx_fmt=png)**不过35b a3b可以实现把大多数题目秒掉（个人赛两小时做一百多道啊，平均得一分钟一道），这个能力大多人肯定是不赞同的**，这模型也挺老了，对于这一套题目来说是远远不够的，所以包括我在内的大部分人都提出了质疑

然后可以看选手提供的图片，这台电脑我特意让豆包找了一下，您猜怎么着还真找到了 ![](https://mmbiz.qpic.cn/sz_mmbiz_png/3Bkxl9ud7XOyg2atpCLh33yYQp3585diaicfBPK5icyUWOla62dziahdWrUahJELMchWkuOxcf5KTpiaYoTd4z0lvtx6jUePYk6MlHjAuls78j5M/640?wx_fmt=png) 然后问了一下参数，感觉就是个轻薄本 ![](https://mmbiz.qpic.cn/sz_mmbiz_png/3Bkxl9ud7XNBe8aWojOO5pHBZ0GibibNd6iarxUq21MnibtqA8Mb1qGeo8tmQoTUdAjQXkzhTevr0WWxH5sR1fNlBa3LaYT5YeHmnRficiay8gwoQ/640?wx_fmt=png) 那么问题又来了，我周围打取证的哪一个不是用的游戏本，虽然不跑本地ai但是取证软件垃圾电脑也带不动啊，更别说Qiko了，因为是初创软件，所以目前占用内存还是很离谱的 为了防串我也留个截图，我是Qiko内测用户，提了非常多的建议 ![](https://mmbiz.qpic.cn/sz_mmbiz_png/3Bkxl9ud7XPLUsZtnz2ricpk90zmWyqhEN8mB5ac6Ut9rW3CkXChSCnqwPliaqfWfiaSzvTUuP7lBv0X2pFZf4y7aJed7EwDWOMTj3BpmU2B0A/640?wx_fmt=png) 印象很深刻，当时打我们学校的精武杯，因为电脑检材实际大小有1个多t，所以加载没多久Qiko直接崩溃了 ![](https://mmbiz.qpic.cn/sz_mmbiz_png/3Bkxl9ud7XN1qsVRLRM3Hs6Qud2pZp1mLgXZrhgvl2uPa2xEyD2qAcj4oLalwWVBMW1vhwmPrOqnic4KZ91LS3GoAIIjGHYcr6k8yibes0MUU/640?wx_fmt=png) 这个电脑能把检材全部分析出来并挂到Qiko上？骗鬼吧，除非里面进行了改装处理

就这个电脑和这个模型，能做到第一，你让后面带了4台dgx的，带了主机的情何以堪啊（笑）

> 别告诉我你用的是 **Qwen3.6-35B-A3B-FP8-Distill-gpt-Astra-6**（笑）

最搞笑的就是这两行，有人懂AI无法操作的幽默感吗，这人甚至PPT自己都没有审查一遍 ![](https://mmbiz.qpic.cn/sz_mmbiz_png/3Bkxl9ud7XPCufjPvgKkXUjwQGdia9qGYXNWnfkaxXia5BxTgOQgn3a1KVOsKC8cxaic6hta1ViaOnw4mZDsdv6p2LqclvZa2STzkownibj1iaGA8/640?wx_fmt=png) 好的，我们最后看看他怎么说的 q1：用智能体软件就不用下了吗？反而配置环境我觉得真的很麻烦，啥叫思路从这种方式转换了，搞笑吧 ![](https://mmbiz.qpic.cn/mmbiz_png/3Bkxl9ud7XP5wgPeIeEMFqoQaAjI0sxkGGvjNkxtfranEkdibhp7CoP5dx0pWDwLKUnicOiaRhkzY5D8ciaH0B5Rx9AY3QWV7mVtLElW3x7N5z4/640?wx_fmt=png) q2：gpt-oss-20b是多老的模型了，用这个打取证？我前年比赛就在用了，在取证上真的一窍不通，甚至还想用这个打吗 ![](https://mmbiz.qpic.cn/mmbiz_png/3Bkxl9ud7XPJI2rKO1L9Kc8gYVyyqlOc235Uiaa7icBB4n4ZZNicic2BYDhLVXgyBEj7bXlFeqy25FUuIoa1wFnCOeeItzibwZR9vvFPbn7aVcm8/640?wx_fmt=png) q3：你不会自己做吗，你知道harness的架构吗，超级取证大师mcp，火眼cli哪个不行，拿这个举例子只能说是一窍不通了 ![](https://mmbiz.qpic.cn/mmbiz_png/3Bkxl9ud7XObyiaCdCGADicrB9EVYxJLQTfFcqX1MjX8E3C6axfEPltlGLZwgOBrZaXiclw1L27nJ2wDRWx5TcIbsTwZYIbTuEew7OykmwUiaQ8/640?wx_fmt=png) q4：Qiko的上下文真的有点长，但凡自己试一下呢，反而自己做的上下文能压缩到很小 ![](https://mmbiz.qpic.cn/mmbiz_png/3Bkxl9ud7XMKYq4O7NHIMbib2DKW9Lz95DjsfL8CE0712U5OIb3bbwtqmf0UrC9IMqic8bribGgiaeamWjd3QYqUw5VTZY6QTFicDSGj0eN9FF88/640?wx_fmt=png) 第一篇基本也就这样了，总的来说学到了0样东西，只看到了把台下的选手一个个当沙子看的感觉

> 最后小说一句，大家可以听一下35:55-36:05这一段的视频，真的很奇怪，每年都有提问环节今年怎么直接消失了？

## 总结一下

2026年可以说是Agent元年，各个厂商（包括我们自己）为了做出自己的一份Agent都付出了时间、心血乃至Token。美亚公司也是在Agent道路上积极探索，开发了Qiko智能体、超级取证大师MCP等多个Agent方案，同时美亚杯也创立了智能体赛道和公用算力（虽然公用算力基本用不了），可以看出在这一方面的积极探索。

可是，大部分人对于Agent能力的验证都是在这些比赛中完成的，这次比赛给我们看到的就是一个轻薄本配上一个35ba3b的模型在两个小时之内做出了所有题目（没有贬低Qiko的意思但是按照这个配置来说是不合理的，两个小时可是要一分钟一道啊）说的不好听一点，真的是往其他选手头上拉屎，别人好不容易配出来的模型真成了乐子（千问：我怎么越来越烂了？）

美亚杯我也参与了两次，虽然上一次没参加线下赛，被别的比赛耽搁了，但是个人感觉这两年的题目真心出的非常好，很适合一个人慢慢手搓的。可惜这个题目被ai弄来弄去最后还是索了个干净

比如这里pdf下面藏有ai注入提示词，防止ai执行操作（虽然基本上被绕过了） ![](https://mmbiz.qpic.cn/sz_mmbiz_png/3Bkxl9ud7XNmTMicpDqMFiccrV8mjWdylAkjlH1RmTU7OMEpPewVR2icGUFGCrJ3iciaP9F0XqicyJZrdDuUZNX9VB2tsp9dwhibxMsia6BC0FgxDVc/640?wx_fmt=png) 也不知道后面取证比赛会变成什么样子吧，今年有了ai，题目也梭了，人也不学了，不过好的一点就是大家对于取证比赛的理解更加透彻了，有的设备就不可能两个小时之内跑出所有题目

写到这里已经凌晨三点了，已经有点眼花了，从开幕式到现在真的意难平，个人赛因为配置问题耽搁了一些时间，这部分我都是手搓完成的，基本上最后也没错多少，然而去年垫底的某支队伍今年直接干到第一，也没听说过和其他师傅取经，取证的能力一年提升的这么快我是不太相信（ ![](https://mmbiz.qpic.cn/sz_mmbiz_png/3Bkxl9ud7XNKvicR97naWiboI6Q0eeYcYdg1rn4YmxYVkToojU2E0Em5v97lvSiarJa95Xib382vkiaINAku6StpoDaRTytTYVRNHx31Sq9l8W7E/640?wx_fmt=png)

最后送给大家ppt里的一句话共勉（吗） ![](https://mmbiz.qpic.cn/sz_mmbiz_png/3Bkxl9ud7XOBu50LXGTnzDO2sL7jLpyJibE8U9AzjKfEUX1RmtoBZgkp6T0cfEibJ7FJic3yVgKV8PPoPXQnv9OxeegxImwUovITqSvA3xwbO0/640?wx_fmt=png) 照这么说可能台上那位可能真没有什么底气，不过各位师傅可以看后面几位讲的内容，真的能够学到很多东西

## 1000粉纪念

另外公众号突破1000粉啦，也是准备了一个小抽奖，后面会继续努力给大家产出高质内容的 关注公众号回复抽奖即可获得抽奖链接，也可以从...