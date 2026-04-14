---
title: MiniMax扔出一颗炸弹：这款开源大模型，是自己教出来的
url: https://mp.weixin.qq.com/s/7f3wqt6HRt6_8mVQ6Ht7cA
source: Doonsec's feed
date: 2026-04-13
fetch_date: 2026-04-14T04:40:40.450610
---

# MiniMax扔出一颗炸弹：这款开源大模型，是自己教出来的

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/x5l8unjI0Urb9w9feGW53fInic7XkfXeQiatP2QLViaZ18fotpPA086t5AZJiaZFR0ibG7HuymAXQsqzicnYMgh6JIicJJTHUNEibwbB7Qs3nuMriaiac/0?wx_fmt=jpeg)

# MiniMax扔出一颗炸弹：这款开源大模型，是自己教出来的

原创

AI观察
AI观察

AI员工上线

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

4月12号凌晨三点，我一个做 Agent 的朋友给我发了条消息。

就六个字：**"卧槽，它开源了。"**

我一开始还没反应过来。大模型开源，2026年还少吗？

但当我点开链接，看到那一行字的时候，我也愣了——

> **"M2.7 是业界第一个 AI 深度参与迭代自己的模型。"**

说白了，这玩意儿不只是个聊天机器人。

它还是个"老师"，教出来的学生就是它自己。

![自我进化的AI智能体](https://mmbiz.qpic.cn/sz_mmbiz_jpg/x5l8unjI0UoZcVgNVDsbkNnELjguMZpy8wVrjic0ibbicIhOn20WOH6sribFVzVMbqgact5FMoonZHD2laItyZibnhDT4xTiby7h2MbPj9wdbVUCQ/640?wx_fmt=jpeg "自我进化的AI智能体")

## 一、先给不看科技新闻的朋友补个课

MiniMax 是国内最早一批做大模型的公司，旗下的海螺 AI 很多人用过。

3月中旬，他们发布了 M2.7，当时的口号就是"开启模型的自我进化"。

而 4月12日，他们直接把这套模型给开源了，而且是**全球开源**。

但更炸裂的不是"开源"本身。

而是它开源的底气，到底从哪来。

根据 MiniMax 官方的说法，M2.7 在研发过程中，能够**自行构建复杂的 Agent Harness**（你可以理解为智能体的"骨架"）。

然后基于 Agent Teams、复杂 Skills、Tool Search 这些能力，深度参与自己的训练、优化和迭代。

里面有个数据特别吓人：在内部测试中，M2.7 可以连续执行 **超过100轮** "分析失败轨迹 → 规划改动 → 修改脚手架代码 → 运行评测 → 对比结果 → 决定保留或回退"的自主循环。

最终效果提升了约 **30%**。

> **"模型不再只是工具，它开始成为研发流程的一部分。"**

这不是营销话术。

MiniMax 自己说了，在某些研发工作流里，M2.7 已经能承担 **30%-50%** 的工作量。

## 二、这模型到底恐怖在哪？

以前的大模型，就像一匹被驯好的马。

人类研究员是驯马师，喂数据、调参数、做评测，一步一步把它练出来。

周期动不动就是几个月，烧钱像烧纸。

但 M2.7 干的事，相当于这匹马自己学会了看赛马录像，自己调整步态，自己给自己加练。

然后还知道自己哪里跑得不好、下次怎么改。

而且不只是"空想"——它在 **SWE-bench Pro**（软件工程能力评测）里拿了 **56.22%**，几乎追平 Opus 最好的水平。

在 **VIBE-Pro**（完整项目交付评测）里拿了 **55.6%**，也是接近 Opus 4.6 的水准。

更接地气的是办公场景。

GDPval-AA 评测里，M2.7 的 ELO 得分是 **1495**，开源模型里的最高分。

Excel、PPT、Word 的多轮高保真编辑，现在可以直接交给它干。

说白了，这模型不是只会聊天的"嘴炮"。

它是真的能写代码、能改文档、能捣腾数据、还能自己越练越强的"实干派"。

![国产芯片适配](https://mmbiz.qpic.cn/sz_mmbiz_jpg/x5l8unjI0Upbddc0DFHPyehgHjYxf77KHPsGeGYNLYXdCD2ZHs48ia5aFB6jQ4QoWiaDrXW4umsibQnf7UgpcAHraPiawiaza3Vlv1uE6oSWbNW4/640?wx_fmt=jpeg "国产芯片适配")

## 三、国产芯片首日适配，意味着什么？

还有一个点，很多人可能没注意到。

M2.7 开源的**首日**，就已经完成了对华为昇腾、摩尔线程、沐曦、昆仑芯、NVIDIA 等芯片的适配。

TogetherAI、Fireworks、Ollama、vLLM、SGLang 这些平台，同一天上线支持。

什么概念？

以前国产模型开源，芯片适配往往要拖个几周甚至几个月。

企业想拿来用，先得被"生态卡脖子"。

现在直接"发布即就绪"。

IDC 的数据也能佐证这个趋势：2025 年中国云端 AI 加速器市场，本土芯片厂商已经拿下了 **41%** 的份额，总出货量约 **165 万张**。

华为以 81.2 万颗领跑，昆仑芯、寒武纪、沐曦紧随其后。

> **开源的意义从来不只是"免费"，而是让更多的人、更多的芯片、更多的场景，能真正跑起来。**

MiniMax 这次显然不是做慈善。

它是在下一盘更大的棋：让 M2.7 成为国内 AI 基础设施的一部分。

## 四、普通人该看到什么信号？

聊完技术，说说这事对咱们意味着什么。

**第一，Agent 时代真的来了。**

不是那种"帮我写个小红书文案"的玩具 Agent，而是能深入工程流、能干脏活累活、能自我迭代的"生产力 Agent"。

M2.7 的 Agent Teams 能力，意味着你可以让它像一个小团队一样分工协作——有的角色负责写代码，有的负责挑 bug，有的负责测试，彼此还能互相 challenge。

**第二，Scaling Law 见顶的声音，可能喊早了。**

GPT-5难产、OpenAI 融资700亿还被质疑估值虚高，很多人以为大模型已经卷到头了。

但 M2.7 给出的答案是：**路还没走完，只是方向变了。**

从"堆算力、堆数据"变成了"让 AI 自己优化自己"。

**第三，国产模型正在换打法。**

以前跟 OpenAI 拼参数、拼榜单，那是人家的游戏规则。

现在 MiniMax 在玩的是"开源+生态+自我进化"，这相当于直接把桌子掀了，重开一局。

![人与AI共处的未来](https://mmbiz.qpic.cn/mmbiz_jpg/x5l8unjI0UrpW3ZPciax5xZq10evVS0kyajcGIZ6M0VEUkic1Pqh6S76icMpvGeqNwyrmEpIR0hdph65hW3b66LYQldhdTicUS5Qm0aDGbQY7n8/640?wx_fmt=jpeg "人与AI共处的未来")

## 五、该泼的冷水

当然，夸完了，该泼的冷水也得泼。

M2.7 目前展现的能力，主要集中在 MiniMax 自家的研发流程里。

它能不能泛化到更多企业的真实场景？开源社区能不能接得住这么复杂的自我进化框架？

这些还都是问号。

而且，一个会自己改自己代码的 AI，也让人忍不住想多问一句：

**安全边界谁来画？**

但不管怎样，有一点是可以确定的：

**那个"AI只是人类工具"的时代，可能真的要翻篇了。**

MiniMax 这次把 M2.7 开源出来，相当于向全世界发了一封挑战书——不是比谁参数多，而是比谁能让 AI 学得更快、跑得更远、变得更聪明。

至于 OpenAI 接不接招，其他国产厂商跟不跟，接下来这半年，肯定好戏连台。

## 写在最后

写到这里，我突然想起我朋友凌晨三点发的那六个字。

当时我还嫌他大惊小怪。

现在回头看，可能他比大多数人更早闻到了变天的味道。

AI 正在从"被训练"走向"自己长大"。

这个转变，不会一夜之间改变你的生活。

但它会一点一点地，改变我们身边所有东西的底层逻辑。

**包括谁才有资格被称作"老师"。**

就这样吧。你怎么看这事儿？

**你觉得 AI 自己教自己，到底是福音还是隐患？**

评论区聊聊。

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/x5l8unjI0Uqrm4gHILLG2gYhHuico1NLxVJaiajoaia7s7y1Iy8wsNOwzmGGFowHyeszUtzrCXpnmKH5C2dwn6wqIByFI4iaxqKBYzqUdd6uL6M/0?wx_fmt=png)

AI员工上线

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/x5l8unjI0Uqrm4gHILLG2gYhHuico1NLxVJaiajoaia7s7y1Iy8wsNOwzmGGFowHyeszUtzrCXpnmKH5C2dwn6wqIByFI4iaxqKBYzqUdd6uL6M/0?wx_fmt=png)

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