---
title: OpenAI 的 Q*没见过，一众创业公司的 Q*来了
url: https://mp.weixin.qq.com/s?__biz=MTMwNDMwODQ0MQ==&mid=2653048738&idx=2&sn=ffcad3de09e6831107399f2644a42edc&chksm=7e5732144920bb02dff0b5e27036d9ac02097d01299172b55b354a10d7b712fb38fa67f14f18&scene=58&subscene=0#rd
source: 极客公园
date: 2024-08-01
fetch_date: 2025-10-06T18:05:35.061174
---

# OpenAI 的 Q*没见过，一众创业公司的 Q*来了

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/8cu01Kavc5YGgy4GP7ynNibGATCicM3v9RzNNib2PicCwAUfVS2u3hVgQaNr8giaWuCRTqunKcpMcqibiaftIuz0ibQBPQ/0?wx_fmt=jpeg)

# OpenAI 的 Q\*没见过，一众创业公司的 Q\*来了

Stephanie

极客公园

![](https://mmbiz.qpic.cn/mmbiz_jpg/8cu01Kavc5YGgy4GP7ynNibGATCicM3v9Rav5TljUYibaHxpNYI4B0eCm85rYO0hn4qaT6WcpKgDr4ng6uaruNZjw/640?wx_fmt=jpeg&from=appmsg)

我们距离能做「慢思考」的 AI，还有多远。

**作者｜Stephanie Palazzolo**

**编译｜宛辰**

**编辑｜靖宇**

去年在 Sam Altman 被临时开除前后，有 OpenAI 的研究人员向董事会发出联名信，指出代号为 Q 的神秘项目可能会威胁全人类。OpenAI 在后续给员工的内部信承认了 Q\*，并将这个项目描述为「超越人类的自主系统」。

虽仍未见过 Q\*，但江湖中，它的传言一直都在。

谷歌 DeepMind 资深工程师卢一峰曾从专业的角度向极客公园作出猜想，[Q\*可能类似「慢思考」的能力](https://mp.weixin.qq.com/s?__biz=MTMwNDMwODQ0MQ==&mid=2653028573&idx=1&sn=be9d6ea935760bae4cf7831bbf2a09fd&scene=21#wechat_redirect)——需要模型意识到它对什么问题没把握，没把握以后应该怎么办。这时，模型可能需要像人类一样，上网、翻书、做实验、想一些莫名其妙的想法、跟别人讨论……。

今年在各个大模型厂商的 AI 助手类 App 里提问题，能够感受到比去年更靠谱的回答，不少厂商也表示正在发力让模型多一些思考，进一步提升推理能力。目前进展如何？

对于上述问题，The Information 记者 Stephanie Palazzolo 在《How OpenAI's Smaller Rivals Are Developing Their Own AI That 『Reasons』》一文中，探讨了现有创业公司提升模型推理能力的模式，包括中国公司的 Q\*。经极客公园整理，如下：

**01**

****OpenAI 的小型竞争对手****

****开发自己的「推理」AI****

剔除泡沫，这波 AI 到底有多大用，是今年被放在聚光灯下反复审视的话题。

大模型的原理是根据概率预测，生成一个一个词元，但凭训练时被喂的语料鹦鹉学舌，遇到没有见过的提问就幻觉般编造，显然不是大家的期待。进一步提升模型的推理能力，成为关键。

在这方面，我们仍未见到 OpenAI 和谷歌的进展，但一些创业公司和个人表示，他们已经想出了一些「便宜的」方法（cheap hacks）来实现 AI 在某些形式的推理能力。

**这些捷径包括将一个复杂的问题分解成更简单的步骤，并另外向模型提出几十个问题来帮助它分析这些步骤。**

举个例子，当被要求起草一篇关于新产品的博客文章时，AI 应用会自动触发额外的查询（query），比如要求大模型评估它（准备生成）的答案以及需要改进的地方。当然，在用户界面，看不到模型在后台做的这些动作。

这类似于苏格拉底（Socratic）教学生批判性地思考他们的信仰或论点的方法。后者采取一种问答式的教学方法，在与学生交流时，苏格拉底不会直接给出答案，而是通过不断提问，引导学生自己去发现问题、揭示其观点中的矛盾和不足之处，并逐步修正，得出正确的结论。

有了这个环节，AI 应用可以要求大模型重写上述的博客文章，写的时候把它刚刚给自己的反馈考虑在内。这个过程通常被称为反思（reflection），一位 AI 应用的创业者表示，这通常会带来更好的结果。

除了反思的方式，开发者还可以效仿谷歌，尝试**一种叫做抽样的技术。在抽样过程中，开发人员通过问同样的问题几十次甚至 100 次，然后选择最佳答案，以此来提高大模型产生创造性和随机答案的能力。**

例如，一个编程助手 App 可能会就同一个问题，让大模型给出 100 种不同答案，然后这个 App 再去运行所有这些代码片段。最终编程助手 App 会选择产生正确答案的代码，并自动选择最简洁的代码。

Meta 在其最近的 Llama 3 论文中也强调了一些类似的技术。

但这种解决方法——调用一个大型语言模型 100 次，或者要求它输出这么多文本和代码，是一种极其缓慢且成本高昂的方式。这可能就是为什么一些开发者批评了由 Cognition（一家使用这些技术的初创公司）制作的编程助手，因为它的性能缓慢。

开发者也看到了这个问题，他们正在尝试解决。方法是**选取对特定问题表现出良好推理能力的模型示例，并将它们「喂」回模型的****训练数据****集中来解决这个问题。**就像一位创业者说的，这种方式类似于在小学学习乘法表。最初，学生可能需要手动计算每一个乘法问题。但随着时间的推移，他们记住了这些乘法表，答案几乎成为学生直觉的一部分。

要开发这种 AI，开发者需要对大模型进行控制。但你很难从 OpenAI 或 Anthropic 的闭源模型中得到掌控感，所以他们更有可能使用像 Llama 3 这样的开放权重模型（开放权重是开源界的术语，意思是开放程度高的代码）来完成这项任务。

上面两种方法可能就是 OpenAI 在推理取得突破背后，所使用的技术。当然，OpenAI 现在还尚未发布 Q\*，后者又被称为「草莓」（Strawberry）项目。

**02**

**中国的 Q\***

中国的开发者和研究人员也逐渐掌握了这些技术。

中国 Skywork AI（天工 AI）和南洋理工大学 (Nanyang Technological University) 研究人员在今年 6 月发表了一篇关于这个问题的论文。在这篇文章中，他们也将这项技术命名为 Q\*，以纪念他们从未见过的 OpenAI 的版本。

中国的 Q\*技术可以让大模型解决具有多个步骤的问题，比如复杂的逻辑谜题。

方法是**通过在答案的每一步中「搜索」大模型应该尝试的最佳的下一步，而不是跟随步骤得出结论（该方法也被称为蒙特卡洛树搜索，早先被用于谷歌 AlphaGo)**。这是通过一个特殊的方程式实现的，这个方程式被称为 Q 值模型，帮助大模型估计每个可能的下一步的未来回报——或者说最终答案正确的可能性。

研究人员表示，他们计划在今年秋天公开发布这项技术。

一家智能体创业公司 Minion AI 的 CEO 亚历克斯·格雷夫利，同时也是 GitHub Copilot 的前首席架构师表示，他们还在尝试**教大语言模型在意识到出错时回退到前一步。他称，当大模型产生了一个错误答案，或者被要求反思其中间步骤时（类似于上面博客帖子中的例子），这种意识就可能发生**，意识到已经犯了一个错误。

业界还有更多的尝试，包括斯坦福大学和 Notbad AI 在 3 月发表的「Quiet-STaR」论文。就像人类在说话或写作前会先停下来思考自己的想法一样，这篇论文解释了如何教会大语言模型生成关于它们在复杂推理问题中，所采取的内部「思考」步骤，以帮助它们做出更好的决策。

OpenAI 的 Q\*/Strawberry 技术可能已经领先一步，但其他所有人似乎都在竞相追赶。

\*头图来源：GulfNews

**极客一问**

**你认为我们距离**

**能做「慢思考」的 AI，还有多远？**

![](https://mmbiz.qpic.cn/mmbiz_png/8cu01Kavc5YTxYGib55rtMHhP1YJ44FLtVGp8Keyg6D2X3AUhgNicT1ibKKh0fE1eiaGqkSXnTlW0ib96ib3HDAIrnVA/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_png/8cu01Kavc5bXib8IGpjbghqj305kKeYibwx0gmZO3iaFibnGncpOnsDNKDciaIH6xNBnpPpk7o5de1RKLzgq70eibBTw/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_png/8cu01Kavc5an0KBXb9IbCwiajJefiaywlMX2G9daxebRIz0bpONcZbhCkA7mNIG39fwRUOEzpoBIPvAXIuA82B9Q/640?wx_fmt=png)

**热点视频**

实测iOS 18.1 beta通话录音，安卓机仍能收到录音提示。

**点赞关注****极客公园视频号****，**

**观看更多精彩视频**

**![](https://mmbiz.qpic.cn/mmbiz_png/8cu01Kavc5an0KBXb9IbCwiajJefiaywlMX2G9daxebRIz0bpONcZbhCkA7mNIG39fwRUOEzpoBIPvAXIuA82B9Q/640?wx_fmt=png)

**更多阅读****

[![](https://mmbiz.qpic.cn/mmbiz_png/8cu01Kavc5ZOy3hlxyp03CAtXicxlY5942bvexbGKOXbLPCC83nOpbWNxGF4JnpSWWXQPc3rRH1nzBBTrXxGfsg/640?wx_fmt=png&from=appmsg)](http://mp.weixin.qq.com/s?__biz=MTMwNDMwODQ0MQ==&mid=2653048711&idx=1&sn=0c090469bcab57def340562c3ca27641&chksm=7e5732314920bb27c372a5e4bed0ef69378c343209be134f5fa443f15e787d10350c99d2dd0a&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/mmbiz_png/8cu01Kavc5ZOy3hlxyp03CAtXicxlY594PfSsvL3euXMBU5TFclcWgEoKrryQ9eaLTju76yujmYBGVm6o4odzoA/640?wx_fmt=png&from=appmsg)](http://mp.weixin.qq.com/s?__biz=MTMwNDMwODQ0MQ==&mid=2653048631&idx=1&sn=99bae12237f92c01ceb5ec09c0c76840&chksm=7e5732814920bb972f4b04bdea67daa45951fc2db30c3c7d29cebaf99c4a9e6a7c85bd7bd03e&scene=21#wechat_redirect)

![](https://mmbiz.qpic.cn/mmbiz_gif/8cu01Kavc5ZENt3gIiatQKstoLiatpXoWBUwkB6tO2b9y2Hoj5HpcnXc5zRJEX6MhbyXJ3q0gjTrrBIUF7boJGDA/640?wx_fmt=gif)

![](https://mmbiz.qpic.cn/mmbiz_gif/8cu01Kavc5YR1a8dIHV2UrCdNIhialnevdQkialrf9oMibXZhuHeD0nPUHuFlYzYB4WYzwnTbhSyAvj9ibZb7ibewPw/640?wx_fmt=gif)

‍

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