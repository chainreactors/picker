---
title: OpenAI 发布实时 API，AI 实时语音时代如何抢占风口？
url: https://mp.weixin.qq.com/s?__biz=MTMwNDMwODQ0MQ==&mid=2653057277&idx=1&sn=0eeaad3bf2280f034f12cf25cd5214f3&chksm=7e570d4b4920845d56b850a9bd9b849743f2b4290fbc020645ae06f0cb481809a2fdb7c2ad7d&scene=58&subscene=0#rd
source: 极客公园
date: 2024-10-11
fetch_date: 2025-10-06T18:53:18.051294
---

# OpenAI 发布实时 API，AI 实时语音时代如何抢占风口？

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/8cu01Kavc5b88BRkZpN9rFpxEnboVl8oweVuicfwP6fKqoO4ib53Nb9AOW5DgKCzdGwiaDlefbMITY24Z5JibWSO2Q/0?wx_fmt=jpeg)

# OpenAI 发布实时 API，AI 实时语音时代如何抢占风口？

原创

油醋

极客公园

![](https://mmbiz.qpic.cn/mmbiz_jpg/8cu01Kavc5b88BRkZpN9rFpxEnboVl8o0dVELEVW4VViaOv7pme0qmBYiaZjwWcQeooiamsGnP7TEpIuI1o7PSP1g/640?wx_fmt=jpeg)

实时互动与 AI 结合的所有想象力，都会展现在今年的 RTE 大会上。

**作者 | 甘德****编辑**| 郑玄****

10 月 2 日，OpenAI 发布了实时 API 公开测试版，用于构建基于 GPT-4o 语音到语音的 AI 应用和智能体。这是 GPT-4o 发布之后，OpenAI 在实时语音交互能力上的最新进展。

GPT-4o 所展现出的实时语音交互能力让外界印象深刻。而这很大程度上归功于 GPT-4o 大幅降低的语音延迟，平均 320 毫秒的反应时间，让 AI 与人的对话第一次接近了人类真实对话间的反应速率。同时其语气和情感模拟，也更加深 AI 与人类沟通之间的沉浸感。

而国庆假期间，OpenAI 发布的实时 API 公开测试版，则瞄准了 GPT-4o 语音到语音的 AI 应用和智能体，这像是给所以 AI 应用开发者的一个信号，大模型发展近两年后，基于声音的实时对话式 AI 场景或许会开始变的瞩目起来。

OpenAI 这次也公布了三家语音 API 合作者的身份：LiveKit、Twilio，以及 Agora。值得一提的是，前几年曾经爆火的 ClubHouse，背后的技术提供方就是 Agora，其兄弟公司声网则在国内更为人所知。Agora 聚焦美国和国际市场，声网则已经俨然是中国市场中 RTC（实时音视频，Real-time Communications）能力最头部且主要的提供者。

![](https://mmbiz.qpic.cn/mmbiz_jpg/8cu01Kavc5b88BRkZpN9rFpxEnboVl8oW7EEo1NYSj1A9dYTrAqNbL3icAToh4CsPe57nF5AyGrKIx99G9QxPYw/640?wx_fmt=jpeg&from=appmsg)

而当下实时对话式 AI 这场还未完全起势的浪潮背后，发展多年的 RTC 技术作为一项基础能力，已经逐渐靠近实时多模态大模型发展浪潮的核心。

**01**

****RTC 是实时多模态****

****大模型的必由之路****

**无可置疑的，大模型能力的提升直接促进了端到端实时多模态大模型的崛起。**

此前，实时对话中的语音处理是基于传统的三步骤——语音识别、语音转文字、文字转语音（STT-LLM-TTS）——方法来进行的。现在得益于大模型自身能力的进化，端到端实时多模态模型能够直接处理语音，这与传统的三步骤处理方法相比，响应速度要提升很多，这也是为什么实时对话式 AI 的前景开始备受期待。

**语音处理这个技术难题被攻下后，大模型领域的头部玩家们已经开始用脚投票了。**

今年 6 月，Character AI 推出新的语音功能，用户可以与 AI 角色进行语音对话。这家人工智能聊天机器人初创公司表示，新的通话功能在推出初期就吸引了来自 300 多万用户的 2000 多万次通话。

Character AI 推出新语音功能几天后，微软 AI 负责人 Mustafa Suleyman 透露微软将在今年年底为用户拿出实时的语音界面，允许完全动态的交互。

而在国内的大模型领域，智谱 AI 8 月末在智谱清言中上线了国内首个面向 C 端的视频通话功能，该功能让用户能够通过应用程序进行语音和视频互动，整个体验类似于与真人对话。用户不仅可以使用手机的前置或后置摄像头进行视频通话，还能进行语音交互。这项功能特别适合在日常生活中的各种场景应用，比如协助学习、辨识物品等。

而在智谱清言新功能上线同日，科大讯飞星火极速超拟人交互技术也正式上线讯飞星火 APP，星火极速超拟人交互在响应和打断速度、情绪感知情感共鸣、语音可控表达、人设扮演四个方面实现重大突破，让整体交互体验更自然、更具情感。

电影《Her》中的场景，似乎真的要成真了。但 GPT-4o 进一步打开实时对话式 AI 的想象力所给人带来的启示，或许是我们仍然低估了「实时」在交互体验上的重要性。

**实时对话式 AI 中，「实时」与「AI」一样重要，甚至作为一场与 AI 的对话体验中最决定性的变量，「实时」实际上的重要性要更胜后者。但要把「实时」拉到极限，端到端实时多模态模型的崛起只是近来取得技术突破的一条明线——它从思考速度上缩短了语音的交互时间。而另一条更绵长的发展暗线则是 RTC（实时音视频，Real-Time Communications）技术的持续进步。**

更详细的拆解一下多模态大模型中实时语音交互的核心路径，大概就能辨析 RTC 技术在其中的重要意义：

首先，语音输入经过 RTC 传输到服务器，服务器端的多模态大模型接收到语音后开始预处理，这里的预处理主要包含了音频的 3A，例如语音的降噪、增益控制、回声消除等操作，使得后续的语音识别更加准确，让大模型更能听懂用户说的话；

随后，预处理的语音数据送入模型进行语音识别和理解，系统再通过模型生成回应，这其中还需要通过语音合成技术转换为语音信号；

最后，语音数据通过 RTC 传输到用户端，完成一次完整的语音交互。

![](https://mmbiz.qpic.cn/mmbiz_png/8cu01Kavc5b88BRkZpN9rFpxEnboVl8oUgKyRCRbs2nrVVc0jjoUre6tnBNjVoggrp29j6wVp4N6QdEDXhCZ4Q/640?wx_fmt=png&from=appmsg)

**声网在实践中发现**，传统的 AI 语音对话（STT-LLM-TTS）在应用 RTC 后，响应延时可从 4-5 秒降低到 1-2 秒，**而在具备端到端实时多模态处理能力后，通过 RTC 技术，大模型实时语音对话的延时可降到几百毫秒内。从体验上看，RTC 技术的应用让对话式大模型的交互更智能，更具真实感。**

在 GPT-4o 的发布会上，有一个细节引人注意：用于演示的手机连接了一根网线。工程师 Mark 解释说，这样做是为了确保网络的稳定性。这也揭示了一个事实，即 GPT-4o 的演示是在固定设备、固定网络和固定物理环境中进行的，以保证低延迟。

然而在实际应用中，用户的设备通常不能始终连接网线，最终无论多强的模型能力，都需要依靠 RTC 技术来真正落到实时对话的场景中。而这其中多模态大模型在与 RTC 技术结合时如何保障低延时、流畅的语音交互体验，变得尤为关键。

一句话来说，RTC 是将多模态大模型与实时互动场景连接起来最关键的技术桥梁。

而随着 RTC 从最初的一种前沿技术在近年逐渐变成一项基础设施级别的能力并迅速在各个场景中延伸，加入了场景视角的 RTE（实时互动，Real time engagement）概念开始取代 RTC，成为当下谈论实时互动能力新的技术名词。

以声网创始人兼 CEO 赵斌对 RTE 的概念表述：

「RTC（实时音视频）从 Communication 的视角，更多是在强调对语义信息进行高质量和高效率的传递。而 RTE（实时互动）更聚焦用户所需要的共享时空，即俗话所说的场景。」从 RTC 到 RTE，就是从基础能力向场景化能力的进化。

在这个端到端实时多模态模型产品化势头初现的时期，声网和 RTE 开发者社区联合发起了第十届 RTE 大会。**实时互动与 AI 的结合在当下所能承载的所有想象力，都会在这场大会中现身。**

**02**

****AI 浓度拉满，****

****第十届 RTE 大会亮点前瞻****

首先，不用怀疑的是，这场 RTE 大会上会有非常多足够有分量的观点交锋。

国内大模型领域在 ToB 方向上走的最深的智谱 AI，以及国内大模型领域在 C 端产品化上最有心得的 MiniMax 将会出现在 RTE 大会上。作为这两年随大模型迅速成长的创业公司，智谱 AI 和 MiniMax 在 RTE 技术在大模型的 ToB 和 ToC 两条路线上发展颇有心得。

而随着大模型开源生态的迅速发展，大量个人开发者从去年开始加入了这一股大模型浪潮，实时对话式 AI 开始成为一个备受开发者关注的产品赛道，通义千问也会带着国内最大开发者生态的经验在 RTE 大会中加入讨论。

除此之外，此次 RTE 大会也不乏业内备受瞩目的创业者身影。全球最受瞩目的 AI 科学家之一，一年前从阿里巴巴离职躬身入局大模型的贾扬清也会出现在此次 RTE 大会的主论坛上，来分享他在 AI 基础设施领域创业 18 个月后的经验心得，以及他对 RTE 与 AI 结合的未来趋势的判断。

![](https://mmbiz.qpic.cn/mmbiz_png/8cu01Kavc5b88BRkZpN9rFpxEnboVl8oUGicaQzIru2IKgISeH0bqwlic554am8tszpTJOicicI8ZpQkl0BzqhGzVg/640?wx_fmt=png&from=appmsg)

**本次 RTE 大会也将通过七场行业分论坛的形式，展现一幅最具想象力的 AIGC+RTE 行业场景应用图景，包括 AI+IoT、教育、泛娱乐、出海、数字化转型等七大行业。**50+行业大咖将会现身行业分论坛现场，带来一线的场景实战案例以及极具深度的行业洞察。

场景是技术迭代所结的果实，未来对于新场景的想象力也酝酿在当下技术的前沿趋势中。本次 RTE 大会也在行业场景应用的讨论之外，**设置了五场技术专场，分别聚焦在音频技术和 Voice AI、视频技术和 AI 生成、RTC+大模型、空间计算和新硬件、云架构和 AI 时代的 Infra 这五个技术方向**，30+的技术大咖和专家学者将会带来自己对所在领域最深入的技术见地。

当然，对于参与到 RTE 大会中的开发者们来说，这里提供的不仅仅是观点和见地。每年 RTE 大会都会为参会开发者设置专属活动，在今年的 Workshop 中提供了**用 TEN 开源框架来现场动手搭建拥有音视频理解能力的 AI Agent 的机会，这将为开发者带来更多 AI 实时互动场景创新灵感。**

2024 年，实时对话式 AI 火热，而 RTE 大会也迎来了十周年。

时间倒回到十年前，2015 年移动互联网那时在国内还未完全成熟，RTE 大会在十年里见证了直播、在线教育、远程办公这些新的技术场景景一次次以新物种的面目亮相并最终融入了大众生活。在这个过程中, 实时互动技术逐渐成为人们在社交和泛娱乐产品中的基础设施。而随着实时互动行业的发展，走过十年的 RTE 大会已经变得越来越重要，它已经是当下这个领域在全球范围内规模最大、议题最全, 最具影响力的行业大会。

现在，AI 与实时互动的碰撞正涌现出新的技术和产品浪潮。而无论从前沿技术的探讨深度，还是多场景创新应用的丰富性上，今年的第十届 RTE 大会都像极了这样一场「风口浪尖」上的实时互动领域盛会。

这场大会将会展现出这场变革至今为止最锐利最先锋的一面。已经身处这场变革中的开发者们，或者对实时互动即将出现的颠覆性变化感到兴奋的所有人来说，请及时到场。

文末点击**「阅读原文」**了解大会完整议程并预约报名

\*头图来源：视觉中国

本文为极客公园原创文章，转载请联系极客君微信 geekparkGO

**直播预告**

![](https://mmbiz.qpic.cn/mmbiz_jpg/8cu01Kavc5b88BRkZpN9rFpxEnboVl8oYQyXWDXLoMYvQbNq00OvpMNSZJMDKHpJI2pqXDqOJSPGnnYXRsIXKw/640?wx_fmt=jpeg&from=appmsg)

10 月 10 日，字节 AI 硬件团队发布了第一款产品智能耳机，将豆包大模型植入在内，用户戴上该耳机后，可通过语音对话随时使用豆包，在豆包 App 上也可以操控这款耳机。

在此前，AI 眼镜、独立的小型设备、玩具，甚至汽车，都已经开始和大模型结合，产生新的变化。

今晚 8 点，极客公园视频号直播间，来聊聊对于AI 硬件来说，真正的机会是什么？

![](https://mmbiz.qpic.cn/mmbiz_png/8cu01Kavc5YTxYGib55rtMHhP1YJ44FLtVGp8Keyg6D2X3AUhgNicT1ibKKh0fE1eiaGqkSXnTlW0ib96ib3HDAIrnVA/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_png/8cu01Kavc5aCSN7l3mxJiby091ndldJQLLGdjEVBcf1TwH0qibFG3BJcShAZbUckyeicDiaLgjvnvUwZ1wrLhpaREw/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/8cu01Kavc5an0KBXb9IbCwiajJefiaywlMX2G9daxebRIz0bpONcZbhCkA7mNIG39fwRUOEzpoBIPvAXIuA82B9Q/640?wx_fmt=png)

**热点视频**

蔡崇信：我和马云相互信任，从来不互相干扰。

**点赞关注****极客公园视频号****，**

**观看更多精彩视频**

**![](https://mmbiz.qpic.cn/mmbiz_png/8cu01Kavc5an0KBXb9IbCwiajJefiaywlMX2G9daxebRIz0bpONcZbhCkA7mNIG39fwRUOEzpoBIPvAXIuA82B9Q/640?wx_fmt=png)

**更多阅读****

[![](https://mmbiz.qpic.cn/mmbiz_png/8cu01Kavc5aIZOtjpq80ljtnt9YLMm6t9wfF52gtLazhcRA2h2bNiaSh73hmhxfwW9T9sq0x9UibtAtQqJd0XRpg/640?wx_fmt=png&from=appmsg)](http://mp.weixin.qq.com/s?__biz=MTMwNDMwODQ0MQ==&mid=2653056510&idx=1&sn=812163a898eb244823111604dcb1b7b3&chksm=7e5710484920995ea10174415854cb5ddcf8de69396695cd79a18515629078183241e7b51fa9&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/mmbiz_png/8cu01Kavc5aIZOtjpq80ljtnt9YLMm6tp9eXjIo2Wu6sPlqm9OtibPibw7TaiagCgX9E04uVtHKDgfXAN8qvdOvGg/640?wx_fmt=png&from=appmsg)](http://mp.weixin.qq.com/s?__biz=MTMwNDMwODQ0MQ==&mid=2653056478&idx=1&sn=d92d712ce9d0440e801de84b2d5dc3e4&chksm=7e5710684920997e1b83715e4b64b992ebaba3b53762c6143b98a18fc5a990f5281c33e44242&scene=21#wechat_redirect)

![](https://mmbiz.qpic.cn/mmbiz_gif/8cu01Kavc5ZENt3gIiatQKstoLiatpXoWBUwkB6tO2b9y2Hoj5HpcnXc5zRJEX6MhbyXJ3q0gjTrrBIUF7boJGDA/640?wx_fmt=gif)

![](https://mmbiz.qpic.cn/mmbiz_gif/8cu01Kavc5YR1a8dIHV2UrCdNIhialnevdQkialrf9oMibXZhuHeD0nPUHuFlYzYB4WYzwnTbhSyAvj9ibZb7ibewPw/640?wx_fmt=gif)

‍

预览时标签不可点

阅读原文

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