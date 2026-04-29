---
title: 大可：不必恐慌Claude Mythos
url: https://mp.weixin.qq.com/s/9Zib9ZXVL6vAbPQ1eRhn6w
source: Doonsec's feed
date: 2026-04-28
fetch_date: 2026-04-29T05:10:53.856138
---

# 大可：不必恐慌Claude Mythos

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/ZwPehAqOhzFHDJAy6IxHl9rQRS6ejUw1osSqIWB0bG3icC1qwZMT1G0cNhibdNQU3p5dZL5QjHBaUA3VCzkMicRR5VtcO46t2fpce3TJFAmoW0/0?wx_fmt=jpeg)

# 大可：不必恐慌Claude Mythos

原创

刘奇
刘奇

中国电信大可实验室

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz_gif/9vcYYrdZXu5Giav2A7KiaT140sKiaZnZ1zDviaZxkyg9Nbz9e24t21rQvQyj8vpLGkvMYLDK8XibedsaIgSKvgNvKOg/640?wx_fmt=gif&from=appmsg)

最近，Claude Mythos Preview 引发了全球安全行业的强烈关注。根据 Anthropic 官方披露的信息，Mythos 发现了大量软件中此前未知的零日漏洞，覆盖主流操作系统、浏览器以及其他关键软件，其中不少属于高危级别的漏洞。 此外，该模型能够自主识别漏洞并构造利用方式，甚至发现了隐藏在“世界上最安全的操作系统” FreeBSD 中数十年的高危漏洞。鉴于潜在安全风险，Anthropic暂不面向公众开放该能力，而是通过 Project Glasswing 计划向部分合作伙伴提供受限使用，用于提前发现和修复关键软件中的漏洞。

    不少人的第一反应是：如果模型已经具备这样的能力，攻击者的能力是否会被迅速提高，我们又该如何应对？

    真正值得担忧的是，当前在 AI 技术发展的驱动下，漏洞挖掘的工作模式正在发生结构性和颠覆性变化。过去，漏洞研究高度依赖专家经验，往往需要人工阅读代码、手动跟踪调用链、反复构造输入及长时间验证。现在，大模型智能体已经可以在一定范围内参与代码理解、路径推理、工具调用、证据整理和漏洞验证等工作。漏洞发现本身，正在从低频次、重人力投入的工作模式，转向高频次、高自动化的阶段。

    Mythos 的意义，就在于把这个拐点摆到了大家面前。

![](https://mmbiz.qpic.cn/mmbiz_png/ZwPehAqOhzGPwtZMTOiagQWrBKHtAMKiaXRYojzIUPapt9K6RnAZo5thaZ9nc5qIHMEfdXUeQm59DfZZ831yic0WMqKJlh5eWcfebjmhqYJ7bk/640?wx_fmt=png&from=appmsg)

**理解Claude Mythos带来的变革**

![](https://mmbiz.qpic.cn/mmbiz_png/Ljib4So7yuWhGVamVRtnAYLVM2g76tOeku4JXEv8THJNVtj8ZJyvHIP0E4TPq6CxtfUAp7ojz8lapibBRWBf4fyQ/640?wx_fmt=png&from=appmsg)

    首先，无论 Mythos 的能力有多强，它发现的仍然是已经存在于代码、协议、组件、供应链和业务逻辑中的缺陷。它并没有创造出一种前所未有的漏洞类型，而是把过去长期潜伏、未被及时识别的问题，更高效地挖了出来。这意味着，我们要思考的不应该是“为什么 Mythos 这么强？”，而是**“为什么这些漏洞能在系统里存在这么久？”**。很多高风险问题并不是因为完全不可发现，而是因为过去的发现成本过高。

![](https://mmbiz.qpic.cn/mmbiz_png/ZwPehAqOhzGvXLXoTwCoDV3XYR3r8AVNXVwSp76PWJUiavaOBoD51IzFlVv4uR0xgp5j0WpAYPHiciciaXpseibkxlqBU3fFQ87j4CFI4c0BERJM/640?wx_fmt=png&from=appmsg)

  **兄弟，你可知道当年代码审计是按行数报价的？**

    面对大型代码库、复杂业务逻辑和漫长的调用路径，人工审计常常受限于时间、精力和上下文容量。某些漏洞并不隐藏在单个函数里，而是分散在参数传递、权限校验、状态切换和异常分支之中。只要审计范围稍大、代码关系稍复杂，人工审计效率就会迅速下降。

    传统安全体系长期依赖周期性扫描、人工审计、被动响应和补丁修复。这个体系在过去是有效的，但在 AI 智能体面前，它正在被降维打击。Anthropic 在相关材料中提到，Mythos 的能力并不单纯来自某种“安全专有领域训练”，而是来自更强的编码、推理、搜索、工具使用和任务调度能力。也就是说，**安全能力已经开始从通用模型能力中自然涌现，这才是关键。**

如果漏洞挖掘能力会随着通用大模型能力的提升而持续增强，那么攻击者迟早也会获得类似能力。届时，攻防差距并不主要取决于某个模型是否发布，而取决于防守方是否已经准备好新的防御机制。谁能更早把模型能力纳入安全生产流程，谁就更有可能在下一阶段占据主动。

**要抓紧争夺防守的窗口期**

![](https://mmbiz.qpic.cn/mmbiz_png/Ljib4So7yuWhGVamVRtnAYLVM2g76tOeku4JXEv8THJNVtj8ZJyvHIP0E4TPq6CxtfUAp7ojz8lapibBRWBf4fyQ/640?wx_fmt=png&from=appmsg)

Mythos 的 Project Glasswing 项目之所以值得重视，在于它说明国际领先厂商已经把AI漏洞发现能力放进了实际的防守体系。

这里至少有三层含义。

第一，当前讨论焦点已经不再是“模型是否有能力”，而是“能力如何尽快投入关键场景”。对核心软件、关键基础设施和广泛使用的开源组件而言，漏洞发现得越早，修复窗口就越充裕，攻击者能够利用的时间就越短。安全行业过去常说“先发现者拥有主动权”。而在AI时代，这句话会变得更具体：谁先把模型能力转化成批量排查、快速验证和有序修复的能力，谁就能缩短高风险漏洞的暴露时间。

第二，防守窗口正在变窄。过去，一个漏洞从出现到被发现、确认、修复，可能经历相当长的一段时间。现在，如果防守方已经在用智能体扫描关键软件，而对手仍停留在传统节奏上，那么这种差距会迅速拉开。今天看似还只是少数企业的内部试验，明天就可能变成安全团队之间的攻防代差。如果我们还处于观望或恐慌的状态，那么等到像 Mythos 这样的新型安全能力正式上线时，现有安全体系将会遭到降维打击。到那时需要补齐的就不止是模型能力本身了，还包括数据积累、规则沉淀、工具改造、流程重构和组织建设等一系列短板。

第三，Project Glasswing 也提醒我们，AI安全能力不只是发现能力，还是治理能力。一个可以用于发现未知漏洞的能力，如果缺少明确的授权边界、环境隔离、操作留痕和结果复核等机制，本身就会带来新的风险。正因如此，国际厂商一边强调其防守用途，一边通过受限合作的方式控制扩散范围。这说明他们已经意识到，强能力必须配套强治理。否则，再强的发现能力也可能在错误场景中变成负担。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ZwPehAqOhzEwoQQRFJQicDx2MreqHZ9W9mHcwib4icqC139Bh7qHcbdVVtOU0ibicfUQVfgytxwia3r211HEVcYicontYwibaAuVX43ZLyWhS6EK2d8/640?wx_fmt=png&from=appmsg)

对国内安全行业来说，我们要尽快构建自己的安全智能体能力，因为一旦这类能力普及，传统工作方式可能会很快崩塌。那时面临的问题，不只是漏洞响应效率的差距，更是体系化的防御能力差距。

窗口期存在，但稍纵即逝。所以现在最应该做的，是“吃饱饭、抓紧干”！

**智能体未来的优势在于“体系化运营”**

![](https://mmbiz.qpic.cn/mmbiz_png/Ljib4So7yuWhGVamVRtnAYLVM2g76tOeku4JXEv8THJNVtj8ZJyvHIP0E4TPq6CxtfUAp7ojz8lapibBRWBf4fyQ/640?wx_fmt=png&from=appmsg)

    当前讨论 Mythos 时，很多人容易陷入一个误区：似乎只要底座模型足够强，就能直接解决安全问题。但实际远非如此。底座模型只是能力来源之一，数据、工具、流程、场景和人工复核同样是能影响落地效果的重要因素。

    安全智能体不是在benchmark上长出来的，而是在真实的资产、代码、告警、攻击路径中经受真实的修复压力打磨出来的。只有进入实战，模型才知道什么是噪音、什么是真正的重要风险；什么是纸面漏洞、什么是真实可利用路径；什么是不可达的假设、什么是必须马上处置的红线问题。

    所以，面对国外先进大模型的封锁，以及代码资产的数据安全防护需求，我们的重点应当是：**抓紧打造面向真实云网环境、代码资产、业务系统、攻防场景的安全智能体。**同时，充分释放国产大模型的安全潜能，用模型、工具、流程、知识库和实战经验构建可控的安全智能体体系，有效支撑实战化安全运营工作。

    **或许有人会质疑：国产大模型在安全领域能力有限，难以胜任？**

    大可实验室此前在 AI 代码审计体系的相关文章中已提出：**大模型在漏洞挖掘方面缺乏鲁棒性，不是因为没有能力，而是缺少系统化的工作方法和明确的质量标准。**同样一套代码，如果没有合理的上下文组织、明确的覆盖率约束、严格的验证环节和统一的报告标准，模型就容易在大量线索中迷失方向，结论也容易漂移。只有将审计经验、流程规范、覆盖率门禁、验证机制、规则沉淀和标准化报告固化成可复用的 Skills，才能让 AI 具备稳定的实战能力。

    而国产大模型的潜力，要靠智能体引擎来释放。底座模型负责理解、推理和生成；智能体引擎负责规划、调度、工具调用、上下文管理、证据校验和任务闭环；自主进化的 Skills 模式负责固化漏洞研究方法、攻防经验和安全判断标准。

这三者结合，才是国产安全智能体真正可行的技术路线。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ZwPehAqOhzFy3pwuLDXfbnB99z31tZdZNjQCqJxiac94YMicrhXWOtGWdKu5IAmp8udsT97F4A4W98oFM75SXvztm2In6eib3xVNX12zvwyoyk/640?wx_fmt=png&from=appmsg)

    这一点已经在我们的实践中得到了验证，利用该方法，GLM5.1、DeepSeek3.2等国产主流大模型在漏洞挖掘场景中已具备与 Claude Opus 4.7近乎同等的水平。

**应对 Mythos 来临的中国电信实践**

![](https://mmbiz.qpic.cn/mmbiz_png/Ljib4So7yuWhGVamVRtnAYLVM2g76tOeku4JXEv8THJNVtj8ZJyvHIP0E4TPq6CxtfUAp7ojz8lapibBRWBf4fyQ/640?wx_fmt=png&from=appmsg)

    在真实安全实践中，仅发现疑似漏洞还远远不够。一个能够形成报告、触发修复流程、完成复测并实现运营闭环的安全问题，通常需要经过一条完整链路，包括资产识别、代码理解、组件分析、漏洞假设、路径追踪、利用条件判断、影响面评估、证据收集、修复建议、复测验证、规则更新和运营联动等一系列步骤。

    围绕这类需求，中国电信大可实验室近期推出了锐鉴 Raygine Code 智能体。它并非简单地把模型接入代码层面做问答，而是将模型能力深度嵌入可执行的安全工作流。目前，其价值主要体现在四个方面。

    一是任务编排能力。面对代码审计、二进制分析、协议安全检测、Web应用、移动应用、供应链组件和安全运营告警，让智能体按阶段推进、按优先级排序、按证据链验证，可靠且稳定地执行任务。

    二是深度推理能力。漏洞不是关键词匹配出来的。真正高价值的漏洞，往往隐藏在跨文件调用链、复杂状态机、权限边界、异常处理、业务逻辑和组件交互之中。锐鉴 Raygine Code 通过语义追踪、污点分析、路径约束、可达性判断和利用条件建模，把“可疑点”逐步收敛为“可验证的风险”。

    三是可信验证能力。AI安全产品的典型痛点在于产出无法复现的结论。每一个高置信判断都应回答三个问题：代码证据在哪里，触发路径是什么，成立条件是否满足。缺少证据链，模型输出就只能作为参考线索，无法构成高置信报告的有效内容。锐鉴 Raygine Code 在这一点上的目标，是严格把线索、证据和结论区分开，杜绝为提高产出数量而混淆三者。

四是持续运营能力。漏洞发现只是开始，后续还要有修复建议、优先级排序、回归验证、检测规则生成以及和安全运营联动。如果一个系统只能发现问题，却不能驱动后续处置闭环，那么它在大型安全项目中的价值将十分有限。锐鉴  Raygine Code 致力于把这些环节纳入同一条工作链条中，使每一次项目执行不仅形成当次结果，更能为后续任务沉淀可复用的规则和经验。

![](https://mmbiz.qpic.cn/mmbiz_png/ZwPehAqOhzGtxXVicx9cxAUSbt3oeF6a70WknUTcn4gGHR5q7EAwNfuBicUwQDeicMKEhYcfQgHaXibQByxmHIXN4aJYH7jTVoOPsQUO1O9hxOI/640?wx_fmt=png&from=appmsg)

    因此，评价国产安全智能体的水平，不能只看单次任务输出质量，还要看它在真实场景中能否长期稳定运行、能否支持复核、能否进入修复流程、能否在多轮项目后积累经验。

**结束语**

所以，不必恐慌 Claude Mythos。

    重点是它提醒我们三件事：

    一是攻防节奏已经变快，漏洞发现已经加速，传统安全体系必须升级。

    二是我们要用国产大模型构建自己的安全智能体体系，达到可比、可控的效果，避免技术“卡脖子”带来的降维打击。

    三是国家关键信息基础设施、国产软硬件生态和开源供应链，必须具备AI原生的主动防御能力。

    中国电信大可实验室研发锐鉴 Raygine Code 的价值就在于把国产大模型的潜能释放到真实安全场景中，通过自研智能体引擎和自主进化的 Skills 模式，把漏洞发现、风险验证、修复建议、规则沉淀和安全运营连接成闭环。

    在AI时代，安全防御不能再等风险暴露之后被动处置，我们要把智能体嵌入安全生产流程，把专家经验固化于系统，把国产模型能力转化为可控、可信、可持续进化的防御能力。

    未来已来，与君共勉。

供稿：刘奇

编辑：张简 王旭

审核：孟熹

签发：刘剑群

预览时标签不可点

修改于

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/9vcYYrdZXu5UBxuEWN5GMVd8nBvvlKG4BWWQpkpicicYNZMrYjK64Uljw0rQOHvKZxOMx3ePb9GQvWqlAwRVltzQ/0?wx_fmt=png)

中国电信大可实验室

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/9vcYYrdZXu5UBxuEWN5GMVd8nBvvlKG4BWWQpkpicicYNZMrYjK64Uljw0rQOHvKZxOMx3ePb9GQvWqlAwRVltzQ/0?wx_fmt=png)

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