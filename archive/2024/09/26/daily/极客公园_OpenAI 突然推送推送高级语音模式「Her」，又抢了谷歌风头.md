---
title: OpenAI 突然推送推送高级语音模式「Her」，又抢了谷歌风头
url: https://mp.weixin.qq.com/s?__biz=MTMwNDMwODQ0MQ==&mid=2653055513&idx=2&sn=7bcabe4ee933bdd79659a7e2bd1b8d9a&chksm=7e5717af49209eb939fadf0a339b0e6d8d8e94244d189763cf747ff6197322aefb526d59bbc3&scene=58&subscene=0#rd
source: 极客公园
date: 2024-09-26
fetch_date: 2025-10-06T18:30:09.783698
---

# OpenAI 突然推送推送高级语音模式「Her」，又抢了谷歌风头

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/8cu01Kavc5ZXpic1ibSxoLgefnWMcFpcvhGZsiaQuiclSxx9Gsxh4fFUN67nm3dzKA999Re20MR0amTQH1Zp82l8RA/0?wx_fmt=jpeg)

# OpenAI 突然推送推送高级语音模式「Her」，又抢了谷歌风头

原创

Li Yuan

极客公园

**作者 | Li Yuan**

9 月 25 日早，Google 发布两款新模型 Gemini-1.5-Pro-002 和 Gemini-1.5-Flash-002。

在谷歌的系列模型中，Gemini Pro 属于中号模型，付费用户可以使用。而 Gemini Flash 则由 Gemini Pro 蒸馏而来，在今年 5 月的 Google I/O 上第一次亮相，目前用户可以免费在 Gemini 中使用，开发者也有一定免费的 api 使用配额。

模型升级的重点主要为 1.5 Pro 价格降低 >50%、1.5 Flash 的速率限制提高了 2 倍，1.5 Pro 的速率限制提高了约 3 倍、输出速度提高 2 倍，延迟降低 3 倍；过滤器切换为选择加入。

不过，**似乎 Google 今天的宣传节点再一次被 OpenAI 提前知晓。OpenAI 同日宣布，OpenAI 的高级语音模式，将今日起开始对 Plus 和 Team 用户推出。**

5 月，Google 发布 Gemini 模型的大更新前，OpenAI 就曾提前抢开发布会，宣布很快会带来高级语音模式，登上媒体头条「个人助理 Her 就要来了吗？」

接下来半年，高级语音模式的发布一再推迟，直至今日 Google 更新模型，OpenAI 立刻表示，本周内将推出语音模型。

**除了之前已经剧透过的语音模式与人类在对话中的反应时间相近，会变换语调之外，还增加了个性化指令功能——可以直接指令模型说话说慢点，或者用一个特定的口音，同时可以记住你的名字和提前提供的信息给出更个性化的回复。**

X 上有用户不禁感叹，OpenAI 已经养成了一个新爱好。等着 Google 发布一个更新，几个小时后马上发布一个更新。

![](https://mmbiz.qpic.cn/mmbiz_png/8cu01Kavc5ZXpic1ibSxoLgefnWMcFpcvhHVgic4ZZc0oLE6NPHcNwP5ndz9k06NYWv8gCmBozue8kP0t4vaQ23Xw/640?wx_fmt=png&from=appmsg)

**01.Google Gemini Pro 价格下降一半**

从 Gemini-1.5-Pro-002 和 Gemini-1.5-Flash-002 的名字也可以看出，此次 Google Gemini 的更新，不是一个大版本的更新，更多的是一次整体模型的升级。

**降低价格是一个重要的更新重点。**

Gemini 1.5 Pro 的输入 token 价格降低 64%，输出 token 价格降低 52%，增量缓存 token 价格降低 64%，适用于小于 128K token 的提示语，自 2024 年 10 月 1 日起生效。再加上上下文缓存，这将继续降低使用 Gemini 构建应用的成本。

此外，1.5 Flash 的速率限制从 1000 RPM 提高到 2000 RPM，1.5 Pro 的速率限制从 360 RPM 提高到 1000 RPM。在接下来的几周内生效。

Google 1.5 Flash 得到了 2 倍输出速度和 3 倍更低延迟。

同时，Google 表示，发布的 Gemini 模型，默认不会应用过滤器，开发者可以根据其用例自行决定最佳的配置。Gemini 将继续提供一系列安全过滤器，开发者可以根据需要为 Google 的模型应用这些过滤器。

Google 还表示，此次模型在数学、长上下文窗口和视觉方面取得了一定的进步。

在更具挑战性的 MMLU-Pro 基准测试中，看到大约 7% 的性能提升。而在数学和 HiddenMath（一个内部保留的数学竞赛问题集）基准测试中，两个模型都取得了约 20% 的显著进步。对于视觉和代码使用场景，两个模型在评估视觉理解和 Python 代码生成的测试中表现也更好，提升范围在约 2-7% 之间。

![](https://mmbiz.qpic.cn/mmbiz_png/8cu01Kavc5ZXpic1ibSxoLgefnWMcFpcvhRsUzmdZjtibCLI9x5gCVm9GsZVVLyPNvyHTYot2C3QqQYL2xER3MxJg/640?wx_fmt=png&from=appmsg)

8 月份发布的 Gemini-1.5-Flash-8B 实验模型也得到了新的更新。

**Gemini 模型本身的亮点包括长上下文和多模态功能。由于 Gemini Flash 对开发者有部分免费额度，新更新可能对于开发某些应用有着很好的效果。**

X 上的 AshutoshSrivastava 就表示，他使用 Google Flash 构建了一个应用，能够在 1 分钟内转写 13 分钟的长音频，且准确度很高（且免费）。在另一个应用中，他表示目标探测功能的表现也很不错。

![](https://mmbiz.qpic.cn/mmbiz_png/8cu01Kavc5ZXpic1ibSxoLgefnWMcFpcvhvxwzxibDtfsm8FLofWWO5gzwNdkupBIKKyAAgFib33Bndm2gicVhC2p9A/640?wx_fmt=png&from=appmsg)

**02.OpenAI 高级语音功能今日起推出**

转头看 OpenAI 这边。

凌晨两点，OpenAI 宣布高级语音模式今日起开始向订阅用户推出，周内会全量进行推送。

根据 OpenAI 的宣传片，与标准语音模式进行区分（黑色旋转球），高级语音将以蓝色旋转球表示，并增加 5 个新语音。

此次发布的一个重要亮点是，OpenAI 表示，高级语音模式可以提供个性化定义。

**在视频中，OpenAI的研究员表示，用户可以自定义指令，以让模型以某种口音发音、记住事件以及用户想要如何被称呼等。**

「你可以让模型用特定的语速说话，也许是非常清晰地发音，慢慢地说话，用你的名字或你喜欢的称呼来称呼你。」研究员表示。

另一位研究员提供了一个例子，对模型输入名字和所在城市，在向模型寻求周末的计划时，模型会根据所在城市，进行更个性化的规划。

高级语音对话目前仅适用于 ChatGPT Plus 和 Team 帐户的用户。免费用户仍然可以访问标准语音模式。

不过，**Plus 和 Team 用户每天仍然有高级语音的使用限制，并且每日限制可能会发生变化。当一天的高级语音还剩 15 分钟时，OpenAI 会向用户发出通知。**

同时，使用高级语音模式无法使用 GPTs，即用户设计的 OpenAI 的智能体。

高级语音模式因为对语音反应时间更敏感，在某些嘈杂的场景下，也更容易被打断。

最后，OpenAI 还用高级语音模式搞了一个活，表示 ChatGPT 目前可以用五十多种语言表示「对不起，我迟到了，我不是故意让你等这么久的。」

一起来听听中文的效果。

一个很有趣的点是，此次 Gemini 的发布，是由 Google 的 Logan Kilpatrick 主要负责对外沟通交流。

而 Logan Kilpatrick，正是 OpenAI 前开发者关系负责人。2024 年跳槽 Google。

而转头，此次 Google 发布新模型，OpenAI 就卡点发布高级语音模式。

OpenAI 此次宣布的时间点或许还有另外一个意义——此前外媒报道称，Meta 公司本周将在 Meta AI 中推出名人语调的音频对话功能。

在硅谷，AI 的战争还在热火朝天的继续。

\*头图来源：Figure

本文为极客公园原创文章，转载请联系极客君微信 geekparkGO

![](https://mmbiz.qpic.cn/mmbiz_png/8cu01Kavc5YTxYGib55rtMHhP1YJ44FLtVGp8Keyg6D2X3AUhgNicT1ibKKh0fE1eiaGqkSXnTlW0ib96ib3HDAIrnVA/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_png/8cu01Kavc5Z5rEl2poJuZqVBGZteWibbvpuA2OibrtXHS6bAJibcYSkxdsV1VicAF088bxt3yluWTQeMyL38W8bfrw/640?wx_fmt=png)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/8cu01Kavc5aZd3zlj8Yykibdibgmjs5Xm2KAOicKZoIGib0c12wVnDwaH10PY2076aqwaK6aCJHd4RibkpVrON2Oh0Q/0?wx_fmt=png)

极客公园

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/8cu01Kavc5aZd3zlj8Yykibdibgmjs5Xm2KAOicKZoIGib0c12wVnDwaH10PY2076aqwaK6aCJHd4RibkpVrON2Oh0Q/0?wx_fmt=png)

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