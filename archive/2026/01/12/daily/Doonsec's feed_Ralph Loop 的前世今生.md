---
title: Ralph Loop 的前世今生
url: https://mp.weixin.qq.com/s/KfMYIdt_7XPbv2BZSDqaxg
source: Doonsec's feed
date: 2026-01-12
fetch_date: 2026-01-13T03:27:31.296517
---

# Ralph Loop 的前世今生

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/5r3L9YiaerKciadiccDY9k0w03bGI6y0hJibTDH99FKVcvAAUd7vsDReY5RSdTc1GtaibDmlJmJWA926ZU19TUWUnxg/0?wx_fmt=jpeg)

# Ralph Loop 的前世今生

原创

黑屋Ω号

漕河泾小黑屋

![]()

在小说阅读器中沉浸阅读

# 引言

如果你最近关注 AI Agent 领域，一定会被一个叫 Ralph Loop 的词刷屏。从 GitHub 趋势榜到各类开发者播客，这个听起来略显古怪的名字正成为自动化工程的代名词。

# Ralph Loop 是什么

Ralph Loop 并非由顶级实验室发布的论文定义，而是由开发者 Geoffrey Huntley (@GeoffreyHuntley) 在 2025 年中期提出。

他用一句话总结了其技术本质：

> Ralph is a Bash loop
>
> while :; do cat PROMPT.md | claude-code ; done

## 技术机制

在技术表现上，它可以简练到只有一行代码： `while :; do cat PROMPT.md | claude-code ; done`其运行逻辑是：通过一个无限循环，将同一个（或动态更新的）Prompt 文件反复喂给 AI Agent（如 Claude 或 Cursor Agent）。Agent 在不断读取自身对文件系统所做修改的基础上进行下一轮迭代，直到满足外部设定的校验条件（如通过所有单元测试）。

## 名称来源

这个名字取自《辛普森一家》中的角色 **Ralph Wiggum**。在剧中，Ralph 并不聪明，甚至显得有些笨拙，但他那句经典的台词—— **“我在帮忙！”（I'm helping!）**——恰好捕捉到了这种技术的精髓：

即便 Agent 在某一轮循环中只做了一个微小的重构、修复了一个拼写错误或增加了一个简单的判断语句，只要这种“笨拙的努力”被置于无限循环中，并配合严谨的外部校验（如编译器和测试框架），最终累积的结果将是惊人的。

# Ralph Loop 的发展史

回顾过去一年的发展，Ralph Loop 的走红路径堪称“草根逆袭”：

**大约 2025 年 5 月：概念萌芽**

澳大利亚开发者 Geoffrey Huntley 在使用 AI 编程助手时，对需要不断手动干预纠错感到沮丧，构思出一种通过自动化循环（后来被他称为“一个 Bash 循环”）强制 AI 自我迭代直到任务成功的技术雏形 [10, 16]。

**2025 年 6 月：思想分享**

在墨尔本举办的 Web Directions 大会上，Geoffrey Huntley 发表了主题演讲，分享了他对 AI 将如何重塑软件工程的看法，并展示了让 AI 在循环中自动完成复杂任务的早期实验，传播了“自主编程”的核心思想 [20, 22]。

**2025 年 7 月 14 日：正式命名与公布**

Geoffrey Huntley 在其个人博客发布了标志性文章《Ralph Wiggum as a "software engineer"》，首次将这种不断迭代、自我纠错的 AI 工作流命名为“The Ralph Wiggum Technique”。该命名致敬了《辛普森一家》中以“执着”著称的角色 Ralph Wiggum [8, 15]。

**2025 年 9 月 9 日：里程碑项目 Cursed 语言发布**

为了展示 Ralph Loop 的强大潜力，Geoffrey Huntley 宣布，通过一个长达三个月的连续 AI 循环，成功创造了一门功能完整的编程语言——Cursed。该语言以 Gen Z 俚语为关键字，拥有编译器和标准库 [38, 40]。

Cursed 项目的 GitHub 仓库拥有超过 1198 次提交，证明了 AI Agent 在无人监督下完成长期、复杂项目的能力，引发了社区对“自主智能体（Agent）”能力的重新评估 [4, 41]。

**2025 年 12 月：Anthropic 官方集成**

AI 巨头 Anthropic 正式为其 AI 编程工具 Claude Code 推出了名为 ralph-wiggum 的官方插件 [15, 32]。该插件通过内置的 Stop hook 机制，将 Ralph Wiggum 技术集成到 Claude Code 的核心功能中，用户可以通过 /ralph-loop 命令直接使用 [3, 15]。

此举标志着 Ralph Loop 从一个社区的“hack”技巧，演变为被主流技术栈认可和采纳的正式功能。

**2026 年 1 月：社区热度与讨论爆发**

随着官方插件的推出和 Cursed 等成功案例的传播，Ralph Loop 在开发者社区和科技媒体中引发了广泛讨论。它被视为一种在大型代码重构、自动化测试和无人监督开发等场景下极具潜力的新范式 [10, 6]，不过其应用仍需视具体场景而定，并注意成本与安全控制 [3, 16]。

# Ralph Loop 靠谱吗？解析 Cursed 实验

很多人质疑：简单的循环真的能写出严谨的系统级软件吗？Geoffrey Huntley 的 Cursed 实验 给出了一个答案。

## 实验目标

Geoffrey 想创建一个全新的编程语言：它的功能类似 Golang，但所有的关键字必须替换为 Gen Z（Z世代）俚语。最疯狂的是，Geoffrey 本人并没有编写编译器的经验，他想看看 AI 在完全自主的情况下，极限在哪里。

## 实验设计

实验的设计采用了名为“Ralph Loop”（或称“Ralph Wiggum”方法）的循环机制，这是一种将AI模型Claude置于“while true”无限循环中的方式，允许它持续迭代和完善输出。整个过程持续了三个月，使用了一个单一的提示词（prompt）：

> "Hey, can you make me a programming language like Golang but all the lexical keywords are swapped so they're Gen Z slang?"

Claude 被赋予完全的自治权，可以根据需要设计和构建任何组件，包括编译器、标准库等，而无需人类干预代码。方法论强调通过提示引导AI的迭代生成，工具包括Claude AI模型本身，以及后续产生的编译器（支持解释和编译模式，能生成Mac OS、Linux和Windows的二进制文件）、部分编辑器集成（VSCode、Emacs、Vim）和Treesitter语法。

## 实验结果

实验的结果是成功创建了一个名为“Cursed”的Gen Z编程语言，该语言将传统关键词替换为Gen Z俚语，例如ready代替if、yeet代替import、slay代替func、based代替true、cap代替false等。该语言支持控制流、声明、类型等功能，并能编译和运行程序，例如一个LeetCode问题的解决方案（最大二叉树深度），包括递归和迭代实现，证明了其实际可用性。

项目开源在GitHub（ghuntley/cursed），并有专用网站（cursed-lang.org）。编辑器支持部分实现但不完整。

整体上，实验初步证明了 AI 能够在循环迭代中自主构建复杂软件系统，潜在问题或许可以通过更多 轮次的"Ralph Loop" 迭代和更熟练的提示词来解决。

# 理性看待 Ralph Loop 的能力与边界

Ralph Loop 的崛起并非因为它是一种“万能药”，而在于它揭示了一种极简的工程哲学：复杂性可以通过受控的重复来消化。 然而，在实际应用中，我们需要保持中立且理性的观察。Ralph Loop 并非在所有场景下都是最优解，使用它时必须考虑以下权衡：

* 资源与成本约束：这种“以算力换人力”的模式是以大量的 Token 消耗和 API 费用为代价的。对于逻辑简单的任务，传统的单次 Prompt 或脚本化处理显然更具性价比。
* 时间成本：循环迭代需要时间。在追求即时交付的场景下，Ralph Loop 缓慢的“小步快跑”可能不如人类直接干预高效。
* 适用场景：它最适合那些边界清晰但内部逻辑极其复杂、且拥有自动化校验手段（如编译器、单元测试）的任务。例如，从零构建编译器、进行大规模的陈旧代码重构或修复难以捉摸的边缘 Case。

总而言之，Ralph Loop 并不是神秘的魔法，而是一种工程上的取舍。它让我们看到：只要建立起合适的约束条件和退出机制，即便每次迭代只进步 1%，在持续的循环中，Agent 最终也能在复杂的荒原上构建起高楼大厦。

### 参考资料

Ralph Wiggum as a "software engineer"

https://ghuntley.com/ralph/

i ran Claude in a loop for three months, and it created a genz programming language called cursed

https://ghuntley.com/cursed/

Claude Code ralph-wiggum README.md

https://github.com/anthropics/claude-code/blob/main/plugins/ralph-wiggum/README.md

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz/5r3L9YiaerKevqpmP3HJsIqs9ianF9A6r7GzqvlqSGQZheERk1PrZwHbhhcungUyYccRDRU3FJugqUWjicsXw7EWw/0)

漕河泾小黑屋

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

![作者头像](http://mmbiz.qpic.cn/mmbiz/5r3L9YiaerKevqpmP3HJsIqs9ianF9A6r7GzqvlqSGQZheERk1PrZwHbhhcungUyYccRDRU3FJugqUWjicsXw7EWw/0)

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