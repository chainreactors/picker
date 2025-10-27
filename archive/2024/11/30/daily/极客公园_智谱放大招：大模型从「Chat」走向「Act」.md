---
title: 智谱放大招：大模型从「Chat」走向「Act」
url: https://mp.weixin.qq.com/s?__biz=MTMwNDMwODQ0MQ==&mid=2653066185&idx=1&sn=8f79a7262dd109f88cc7a950eecb0f8f&chksm=7e57ee7f492067692e749a103f7dcd3ce748b696808804cbc90205498c699c291f18e06a6626&scene=58&subscene=0#rd
source: 极客公园
date: 2024-11-30
fetch_date: 2025-10-06T19:16:45.851093
---

# 智谱放大招：大模型从「Chat」走向「Act」

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/8cu01Kavc5b8fKdbvTDOV2lpJjvSog8zibxUt1jbZV5LC05xewfasQZXaSjXrD7RryJg3NGpuCOEDZfkc9u5kOw/0?wx_fmt=jpeg)

# 智谱放大招：大模型从「Chat」走向「Act」

原创

连冉

极客公园

![](https://mmbiz.qpic.cn/mmbiz_png/8cu01Kavc5abwyEr8w6ibliaw5C5oagUDBa9LbvEbZIm5P66DTLibicWR3Q5qbOzMpgHvuWZTg0P3udCCwv9Jvddcg/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_jpg/8cu01Kavc5b8fKdbvTDOV2lpJjvSog8zNWbHrsFKV6zHEns7IC19QFU90wyzgWzkOrASSnCJJhVOBz9VJ2Cvdg/640?wx_fmt=jpeg&from=appmsg)

只有对话功能的 Chatbot，正在进化为「有手、有脑、有眼睛」的自主 Agent。

**作者 | 连冉****编辑**| 郑玄****

每次不知道吃什么的时候，都会羡慕古代的富贵人家，不用自己想，比你自己还懂你的管家就安排的明明白白——今天随着 AI 的发展，这样的场景正在成为现实。

业内普遍认为，2025 年将是 Agent 爆发之年。Gartner 近期将 agentic AI 列为 2025 年十大技术趋势之一，并预测 2028 年至少有 15% 的日常工作决策将由 agentic AI 自主完成。

与 GenAI（生成式人工智能）不同，Agent 是目标驱动型的，能够完全执行工作流程，适应、学习、迭代、与其他系统和人类协作，并端到端地完成任务。在智谱 CEO 张鹏看来，Agent 可以看作是大模型通用操作系统 LLM-OS 的雏形。

此前在 10 月，智谱就推出了自主智能体——AutoGLM。AutoGLM 不仅能够模拟用户的屏幕操作，如点击手机应用，还能在浏览网页时有效辅助用户，涵盖了日常生活中广泛需用的多个领域，包括社交、网购、地图导航和火车票订购等。

今天，在其最新的「Agent OpenDay」活动中，智谱展示了 AutoGLM 多项进展，展示了大模型技术如何将「对话」从简单的互动提升为具有高度自主性的操作系统：可自主完成超过 50 步的复杂操作，并能跨应用程序协作执行任务；支持数十个网站的「无人驾驶」；此外，基于视觉多模态模型的 GLM-PC 也进入内测阶段，致力于探索通用智能体技术，实现像人类一样操控计算机。

在 Agent OpenDay 现场，智谱 CEO 张鹏 通过在现场下达语音指令，让 AutoGLM 面对面建群，给现场数百位嘉宾发送了总共 2 万元的微信红包，并且演示了手机远程指挥电脑自动发送文件。

***01***

**AutoGLM ：挑战变更复杂了，**

**也「变强」了**

在活动上，智谱重点展示了其最新升级的 AutoGLM，它能够自主执行复杂且多步骤的任务，跨应用处理需求，甚至在全程无人干预的情况下自动操作多平台。

AutoGLM 能够高效完成超长任务链，比如呀在购买火锅食材的场景中，AutoGLM 无需人工干预即可执行 54 步任务，且速度超越人工操作；支持跨应用任务执行，用户仅需发出简短指令，系统便能自动调度并完成多个应用间的任务；简化了操作流程，用户可通过简单语音命令启动复杂操作，如一句「点咖啡」便能自动完成从选择到购买咖啡的全部流程。

为了提升个性化体验，AutoGLM 还引入了「随便模式」，通过分析用户偏好和历史行为，主动为用户做出决策，进一步优化使用体验。

同时，智谱宣布 AutoGLM 启动大规模内测，并将尽快上线成为面向 C 端用户的产品；「10 个亿级 APP 免费 Auto 升级」的计划也已启动；支持核心场景和核心应用的 AutoGLM 标品 API，则会在两周内上线到智谱 maas 开放平台试用。

此外，智谱清言插件也上线了 AutoGLM 功能，支持搜索、微博、知乎、Github 等数十个网站的「无人驾驶」。

![](https://mmbiz.qpic.cn/mmbiz_png/8cu01Kavc5b8fKdbvTDOV2lpJjvSog8zj576NXibvKfNI0DfjhGkalDTMKG9H29cTrKJ92EUXOEsKBibm3oicHkXw/640?wx_fmt=png&from=appmsg)智谱清言插件上线 AutoGLM 功能｜图片来源：智谱

***02***

**GLM-PC ：**

**一次关于 PC「无人驾驶」的探索**

除了手机和浏览器，智谱还带来了基于 PC 的自主 Agent——GLM-PC。这是智谱在「无人驾驶」PC 领域的技术探索，基于其多模态模型 CogAgent 开发。

GLM-PC 目前已经开始第一阶段的内测，提供多项核心功能，包括帮助用户预定和参与会议，并自动发送会议总结；支持文档处理，如下载、发送、理解和总结文档；在指定平台（如微信公众号、知乎、小红书等）进行关键词搜索并完成总结；具备远程和定时操作功能，支持远程发指令并执行电脑任务，或在设定时间自动完成任务；此外，GLM-PC 还引入「隐形屏幕」模式，能够在用户工作时自主完成任务，释放屏幕使用空间。

「无人驾驶」电脑｜视频来源：智谱

GLM-PC 的设计理念是模拟人类的电脑使用方式——眼睛观察屏幕、脑海中进行规划，再通过手部操作执行指令。

凭借这一设计，GLM-PC 能够完成复杂的 PC 任务，甚至可以自主学习和执行所有为人类设计的应用，表现出跨平台的强大能力。这是一种系统级、跨平台的能力，不依赖于 HTML、API，具备更高的能力上限。

不过，智能体在执行复杂业务流程时，通常需要调动大量数据和应用程序，但由于许多网站和 APP 的 API 缺乏统一标准，这就会让企业在集成智能体时面临一些挑战。

**对于这一点，智谱 AutoGLM 技术负责人刘潇指出，AutoGLM 通过图形化用户交互界面来解决这一问题，而非依赖传统的****API****调用。**

与传统 API 集成容易因应用更新而导致失效不同，AutoGLM 模拟人类的操作方式，只要应用界面保持用户可理解并且易于使用，智能体就能够在该界面上顺利执行任务，从而规避了 API 标准化不足带来的问题。

由于 PC 任务的复杂性，目前 GLM-PC 还需要用户输入精准指令，距离全面替代人工办公还有一定差距。但随着技术的不断进步，GLM-PC 的能力将进一步增强，未来有望为用户提供更为高效、直观的 PC 操作体验。

***03***

**大模型应用新阶段：从 Chat 走向 Act**

**关于最近热议的 Scaling Law 是否放缓，张鹏认为，Scaling Law 放缓只是一个表面现象，背后可能存在更深层次的原因。**

他指出，尽管在语言处理领域可能接近人类认知的极限，但仍有可能通过大量数据和大规模处理突破这一瓶颈。在多模态应用和智能体等领域，Scaling 仍然有很大的探索空间。

在张鹏看来，计算量和有效信息可能是关键因素，预训练阶段的放缓并不意味着整体进展停滞。事实上，后训练阶段仍然存在 Scaling 效果，尽管这种效果不再像预训练时那样简单地依赖数据量和参数量的增加，而是更加复杂和精细。

这种突破正是当前 AI 技术发展的核心之一——如何将大模型从单纯的「理解」层面提升到「行动」的能力。大模型的价值不应只是作为 chatbot 存在，它的真正价值在于其强大的「理解」与「预测」能力。

这种能力使得大模型能够深度解析和理解人类的复杂语义、情感以及抽象概念，进而进行精准的推理和预测。如何将这些强大的能力从单纯的文本交互中解放出来，应用到更广泛、更实际的场景中，就要从现在的「Chat」走向「Act」。

Act，即行动，代表着大模型技术从理解和预测到实际行动的跨越。这不仅意味着模型能够根据输入的信息作出反应，更意味着它能在更复杂的动态环境中进行决策，解决问题，甚至创造新的价值。

在张鹏看来，「现阶段，AutoGLM 相当于在人与应用之间添加一个执行的调度层，很大程度上改变人机的交互形式。更重要的是，我们看到了 LLM-OS 的可能，基于大模型智能能力（从 L1 到 L4 乃至更高），未来有机会实现原生的人机交互。将人机交互范式带向新的阶段。」

AutoGLM 和 GLM-PC 是智谱对 AI 智能操作系统的一次重要尝试。它们的出现源于智谱在大语言模型、多模态模型、逻辑推理和工具使用等方面的技术积累。

从 2023 年 4 月的 AgentBench 开始，到 8 月的 CogAgent 模型，智谱针对 AutoGLM，和 GLM-PC 的模型 CogAgent 的研发工作进行了一年半的时间。

与 OpenAI 有所不同，智谱定义了大模型发展的五个阶段：L1 语言能力、L2 逻辑能力（多模态能力）、L3 使用工具的能力、 L4 自我学习能力、 L5 探究科学规律。

![](https://mmbiz.qpic.cn/mmbiz_png/8cu01Kavc5b8fKdbvTDOV2lpJjvSog8zCJfwrndZjTwib908dcEIKfCu2FQeqlyq5Mqa8PCeWbtS6dup3rYNF6A/640?wx_fmt=png&from=appmsg)智谱定义的大模型发展五个阶段｜图片来源：智谱

理论上，随着 Agent 能力持续提升，它们将能够驾驭越来越多的应用程序，适配多样化的操作系统，并执行日益复杂的自主操作。这被认为是大模型通用操作系统 LLM-OS 的初步形态。

为此，智谱已在芯片、操作系统 OS 、模型侧和应用 app 侧，进行了一段时间的探索。

在终端层面，智谱已经和手机厂商、PC 厂商实现深度合作，在 AIPC、智能助手 Agent 等领域有诸多成果。智谱也与高通、英特尔等芯片厂商展开密切协作，联合调教端侧大模型，以发挥最新芯片的性能。

通过端侧芯片性能优化和端云一体架构，Agent 不仅在操作系统 OS 和应用 app 上实现用户体验变革，还能将其推广到各类智能设备上，实现基于大模型的互联互通。

这种扩展，具体到当下的各种设备，从手机到电脑，再到汽车、眼镜、家居和各种 edge side 设备，理论上是没有边界限制的。

随着 Agent 技术的发展，AI 与人类的互动模式将不再局限于简单的对话，未来的机器将不仅能听懂人类的指令，还能够主动思考、决策并执行任务。

2025 年或许会成为 Agent 技术爆发的关键年份，Agent 将进一步改变我们与机器的关系，带来更加智能化、个性化和高效的生活与工作方式。

\*头图来源：智谱

本文为极客公园原创文章，转载请联系极客君微信 geekparkGO

**极客一问**

**一句话操作电脑和手机，**

**你心动了吗****？**

![](https://mmbiz.qpic.cn/mmbiz_png/8cu01Kavc5YTxYGib55rtMHhP1YJ44FLtVGp8Keyg6D2X3AUhgNicT1ibKKh0fE1eiaGqkSXnTlW0ib96ib3HDAIrnVA/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_png/8cu01Kavc5bXib8IGpjbghqj305kKeYibwJbLCR7ekIluWOwQhQdiaR8gj7ibC2JvhYKWq6fBeoqoNLSZTcuOMibFBQ/640?wx_fmt=png)

---

![](https://mmbiz.qpic.cn/mmbiz_gif/8cu01Kavc5ZyDevrGxiahDB5zibRefCZNibMC318RFF4532UCSQvWSnCoqWkmw0m8YXVtzcIDZroJf85gugdr3G0g/640?wx_fmt=gif&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/8cu01Kavc5an0KBXb9IbCwiajJefiaywlMX2G9daxebRIz0bpONcZbhCkA7mNIG39fwRUOEzpoBIPvAXIuA82B9Q/640?wx_fmt=png)

**热点视频**

雷军谈初代小米手机：卖多少无所谓，好产品要打磨。

**点赞关注****极客公园视频号****，**

**观看更多精彩视频**

**![](https://mmbiz.qpic.cn/mmbiz_png/8cu01Kavc5an0KBXb9IbCwiajJefiaywlMX2G9daxebRIz0bpONcZbhCkA7mNIG39fwRUOEzpoBIPvAXIuA82B9Q/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)

**更多阅读****

[![](https://mmbiz.qpic.cn/mmbiz_png/8cu01Kavc5ZXGQia4sHkaOTUN3fvEvRWyRtLdadCgjlnKRoFxf4prReEaicn2I0sdkvTlnUME9Pa7koiau0JJIkug/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MTMwNDMwODQ0MQ==&mid=2653066032&idx=1&sn=027ab889f7b4e1ac00f1f7497ececb1b&scene=21#wechat_redirect)

‍[![](https://mmbiz.qpic.cn/mmbiz_png/8cu01Kavc5ZXGQia4sHkaOTUN3fvEvRWy9v0bHrIs3gGsyBfhRUeY1CzGLCG0QdlHF1SHq58ALw4PU2Hiaic90ib1g/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MTMwNDMwODQ0MQ==&mid=2653065979&idx=1&sn=34a6dc8a754b904ce4cdcc950d2b9478&scene=21#wechat_redirect)‍

![](https://mmbiz.qpic.cn/mmbiz_gif/8cu01Kavc5ZENt3gIiatQKstoLiatpXoWBUwkB6tO2b9y2Hoj5HpcnXc5zRJEX6MhbyXJ3q0gjTrrBIUF7boJGDA/640?wx_fmt=gif&wxfrom=5&wx_lazy=1&tp=webp)

![](https://mmbiz.qpic.cn/mmbiz_gif/8cu01Kavc5YR1a8dIHV2UrCdNIhialnevdQkialrf9oMibXZhuHeD0nPUHuFlYzYB4WYzwnTbhSyAvj9ibZb7ibewPw/640?wx_fmt=gif&wxfrom=5&wx_lazy=1&tp=webp)

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