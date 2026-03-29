---
title: Harness or not harness, it is a question
url: http://xargin.com/harness-or-not-harness-it-is-a-question/
source: No Headback
date: 2026-03-28
fetch_date: 2026-03-29T04:41:48.947905
---

# Harness or not harness, it is a question

[No Headback](http://xargin.com)

* [Home](http://xargin.com/)
* [Readings](http://xargin.com/readings/)
* [WeChat](http://xargin.com/wechat/)
* [Github](http://github.com/cch123)
* [Friends](http://xargin.com/friends/)

# Harness or not harness, it is a question

Mar 28, 2026

15 min read

2026 年开年以来，harness engineering 这个词以病毒式传播的速度席卷了整个 AI 工程圈。Mitchell Hashimoto 给它命了名，OpenAI 用百万行零手写代码的项目给它做了广告，Stripe 每周 1300 个 AI PR 给它背了书。一时间，仿佛不谈 harness 就不配做 AI 工程师。

但热闹看完之后，有些问题值得冷静想一想。

## Harness 到底是什么

Harness 这个词来自马具——缰绳、马鞍、嚼子——把一匹强壮但不可预测的马引导到正确方向的全套装备。放到 AI agent 的语境里，harness 就是包裹在模型外面的约束、反馈循环、文档、工具编排和人类审批等一切基础设施。

模型是马，人是骑手，harness 是缰辔。没有 harness 的 agent 就像一匹在旷野上撒欢的纯血马——跑得快、看着帅、没有任何实际用处。

这个词翻成中文也挺麻烦。"约束工程"太窄——harness 不仅是约束，还有引导和赋能。"驾驭工程"语义接近但有个微妙错位——harness 是装备（名词），"驾驭"是动作（动词），你不会把"马具设计"叫做"骑马工程"。所以中文技术圈目前基本就直接用英文，第一次出现时加个括注解释。

Harness 和 Anthropic 的 Agent Teams 是什么关系？简单说，Agent Teams 是 Claude Code 里的一个具体功能——多个 Claude 实例协同工作，一个当 lead 协调，其他 teammates 各自独立工作并互相通信。它是 harness 的一个组件，但不是完整的 harness。完整的 harness 还需要你搞定 CLAUDE.md、测试约束、CI 集成、文件锁、冲突解决策略等一大堆东西。

## 谁真的落地了

把现有案例按成熟度排：

**Stripe Minions** 是目前最扎实的生产级落地。他们的 Minions 是完全自主的 coding agent，每周 merge 超过 1300 个 PR，零人类手写代码。它的 harness 是一个五层 pipeline，从 Slack 消息到生产级 PR。每个 Minion 跑在隔离的 devbox 里，有完整 shell 权限但不能碰生产系统。Agent harness 是 Block 开源项目 Goose 的深度 fork，针对无人值守场景做了大量改造。最关键的是，它连接了 Stripe 内部的 Toolshed（集中式 MCP server），暴露了近 500 个工具，不同 agent 按需请求工具子集。

**OpenAI 内部 Codex 项目**是"harness engineering"这个术语的源头。3 个工程师、5 个月、百万行代码、零手写。他们的核心发现是 AGENTS.md 不能当百科全书用——大文件会挤占 context、腐烂得很快、没法机械化验证。所以他们把 AGENTS.md 缩到约 100 行当"目录"用，真正的知识库放在结构化的 docs/ 目录里。

**Anthropic** 做了两件有意思的事。一是用 16 个 agent 从零写了一个能编译 Linux 内核的 C 编译器，10 万行 Rust，花了 $20,000 API 费用。二是最近发了一篇文章，把 GAN 的思路搬到 harness 里——Generator 负责写代码，Evaluator 用 Playwright 实际操作应用来打分，两者分离解决了"agent 给自己作品打高分"的问题。

**LangChain DeepAgents** 是开源社区里最系统化的实践。他们通过纯 harness 优化（不换模型），把 Terminal Bench 2.0 得分从 52.8% 提升到 66.5%，从 30 名开外冲到前 5。

有意思的是，尽管这几个项目的规模和风险容忍度差异很大，它们得出了非常相似的结论。

## Harness 的八个组件

梳理下来，一个完整的 harness 大概需要这些东西：

**Context engineering**——文档和 skill 的组织。不是"写好文档"那么简单，而是 context injection 策略的设计：什么时候、以什么方式注入 context window。OpenAI 的做法是三级架构：全局 AGENTS.md（永远加载、极短、当目录用）→ 目录级 rule file（按 agent 工作位置自动加载）→ skill/docs/（按需 lazy load）。

**TDD + 静态分析**——让 agent 的每次修改都能被机械化验证。但这里有个关键细节：测试本身要为 agent 而非人类设计。test harness 不能打印几千行无用输出污染 context window。

**可观测性**——OTel 集成、日志、dashboard 访问。让 agent 能"看到"运行时信息。

**架构约束**——用 ArchUnit、depguard 这类工具机械化地 enforce 分层规则，而不是在 AGENTS.md 里写"不要违反分层架构"。

**执行隔离**——Sandbox，这是所有其他层的物理保障。没有它，上面的约束都是"君子协定"。Stripe 每个 Minion 一个一次性 devbox，跑完销毁。

**工具裁剪**——不是把所有 MCP tool 都暴露给 agent。Vercel 砍掉 80% 的工具后 agent 表现反而更好。工具太多 = 决策空间太大 = agent 更容易选错。

**重试和升级策略**——agent 卡住了怎么办？Stripe 的设计是 CI 失败最多重试两次，第三次直接 flag human。LangChain 做了 LoopDetectionMiddleware 检测 doom loop。

**Entropy 治理**——agent 生成的代码会以跟人不同的方式积累技术债。需要定期跑"垃圾回收"agent 来扫描文档 drift、命名漂移、死代码堆积。

## 关于 AGENTS.md 的一些教训

OpenAI 试过"一个大 AGENTS.md"的方案，失败了。原因很直觉：context 是稀缺资源，大文件会挤占任务和代码的空间；当所有东西都"重要"时，什么都不重要；单体文件会腐烂成过时规则的坟场。

ETH Zurich 最近的研究也发现，LLM 生成的 AGENTS.md 对任务成功率有轻微负面影响。agent 确实会遵循指令——于是跑更多测试、读更多文件、执行更多搜索——但这些行为对解决具体任务往往不必要。

Stripe 的做法更进一步——用目录级 rule file，agent 遍历文件系统时按目录自动加载对应 context。他们还兼容了 Cursor 的 rule file 格式，跨 Minions/Cursor/Claude Code 三套 agent 系统同步。

所以核心原则是：AGENTS.md 越短越好，只放 agent 不可能自己推断出的信息。

## AI 写代码需要 TDD 吗

这个问题有人讨论过，但结论比较分裂。

TDD 派的核心论点是：如果让 agent 同时写代码和测试，它会写出 tautological test——测试只验证"代码做了什么"，而不是"代码该做什么"。测试先于实现，就切断了这条作弊路径。

但有一个反直觉的实验发现。TDAD 论文里，单纯给 agent TDD 指令（"先写测试再实现"），不仅没有减少回归，反而把回归率从 6.08% 提高到了 9.94%——比什么都不做还差。原因是：agent 不需要被告知"如何做 TDD"，它需要被告知"该检查哪些测试"。TDD 的流程本身对 agent 来说不是关键，关键是 dependency-aware 的测试选择。

回顾一下主流 harness 文章，几乎没有人显式提到 TDD。OpenAI 的做法是"最少的 blocking merge gate，PR 生命周期很短，test flake 用 follow-up run 解决"——跟 TDD 的"先写测试再实现"理念完全相反。Stripe 也类似——agent 写完代码后跑测试，CI 失败重试两次，第三次 flag human。

实际的做法分成三种流派：

人写测试、agent 写实现——最多人推荐，测试作为刚性合约，但本质上是把"定义什么是对的"这个最难的工作留给了人。

快速反馈循环——OpenAI/Stripe 的做法，不追求"一次对"，追求"快速收敛"。

TDD 的 context 而非 TDD 的流程——不告诉 agent "先写测试再写代码"，而是给它一张依赖图，让它知道"你改的东西会影响哪些测试"。

所以结论是：harness 不需要 enforce TDD 流程，但需要 enforce 两件事——测试由人类（或独立 agent）作为 spec 提供，以及 agent 有能力定位和运行 impact scope 内的测试。

## Stripe 的 300 万测试

Stripe 的 CI 不是纯单测。他们有一个三层反馈体系：Tier 1 是 Local Linters（5 秒内跑完），Tier 2 是 Selective CI（从 300 万测试里选跟改动文件相关的跑），Tier 3 是 Pragmatic Cap（失败返回给 agent 修，最多两轮）。

300 万测试，这个量级不可能全是单测。但单测是大头——只有这种粒度的测试才能做到 selective CI 和秒级反馈。

Stripe 有没有单测？有，而且证据很实锤。2015 年他们就公开写过一篇 "Running three hours of Ruby tests in under three minutes"，当时已经有 15,000 个测试用例。他们后来做了 Sorbet（Ruby 的渐进式类型系统），诞生原因之一就是"Ruby 是动态类型，一些错误只能通过运行单元测试来验证"。

**但 harness 文章为什么不讲"AI 写单测"？** 因为对 Stripe 来说，测试不是 agent 的产出，是 agent 的约束。300 万测试是十年人类工程师积累的资产，是 harness 的一部分，不是 agent 要交付的东西。让 agent 同时写代码和写测试，就回到了 tautological test 的问题。

## Anthropic 的 GAN 式 Harness

Anthropic 最近（3 月 24 日）发了一篇重要的文章，核心贡献是把 GAN 的 generator-discriminator 分离思路搬到了 agent harness 里。

他们发现两个关键失败模式：一是 context 退化，Sonnet 4.5 有一种"context anxiety"会提前收尾；二是自我评价失真，agent 评价自己的作品时会自信地给高分，即使质量明显一般。

解法是三 agent 架构：Planner（把简短 prompt 扩展成完整产品 spec）、Generator（按 sprint 逐个 feature 实现）、Evaluator（用 Playwright 实际操作应用来打分）。Evaluator 和 Generator 在每个 sprint 开始前还要协商 sprint contract——"什么算做完"要在写代码之前达成一致。

效果很明显。同一个 prompt（做一个 2D 复古游戏编辑器），solo agent 20 分钟 $9 但核心功能跑不起来，full harness 6 小时 $200 但出来一个真正能玩的应用。

最有意思的部分是 harness 随模型进化而简化。Opus 4.6 发布后，sprint 分解被去掉了（模型能连续跑两个多小时不跑偏），context reset 也不需要了。但 Evaluator 在模型能力边界上仍然关键。

作者最后说了一句很精辟的话："有趣的 harness 组合空间不会随模型提升而缩小，只会移动。"

## buffa：Anthropic 自己的 Harness 实践

Anthropic 还有一个不太引人注目但很有说服力的案例——buffa，一个 Rust 实现的 protobuf 库。六周内完成，Claude Opus 4.6 做了大部分工作，已经在 Anthropic 生产环境运行。

项目通过了 Google 的 protobuf conformance test suite，但作者明确说：conformance 通过是必要条件但远不充分。他举了几个 spec 盲区的例子——比如 closed enum 在 oneof 里的处理方式，spec 根本没定义，conformance 也不测。

最重要的 harness 洞察是：Claude 在发现这类 spec gap 上表现出色，但只在被明确 prompt "把 spec × tests × code 对照比较，找相对于标准实现的 gap"时才会触发。

这个项目证明了一件事——harness 不一定是复杂的多 agent 架构。有时候就是人 + 一个 agent + 好的测试套件 + 精准的 prompt。

## Human in the loop，还是 out of the loop？

看完所有案例之后，一个很明显的结论是：**harness engineering 的"自动化"叙事容易让人误以为是全自动，但实际上人从来没有 out of loop。**

回顾一下每个案例里人在做什么：

Stripe——人写任务描述、review 每个 PR、设计 harness 基础设施。Agent 是"无人值守执行"，但人在入口和出口都在。

OpenAI——人"prioritize work, translate user feedback into acceptance criteria, and validate outcomes"。Agent 写代码，人定义做什么、验收结果。

Anthropic——人设计评估标准、校准 evaluator 的打分偏好、读 trace 找 evaluator 判断跟自己不一致的地方再调 prompt。最终产出还是人去实际点一点看效果。

所以 harness 实际做的事情是把人从"写代码"挪到了"设计约束 + 审结果"——抽象层变了，但 human 并没有 out of loop。更准确地说是 human at a higher loop：不再是每行代码的循环里，而是在任务定义、harness 调优、最终验收这个更大的循环里。

这也解释了一个很多人好奇的问题：Stripe 都 AI harness 了，为什么没有大规模裁员？

看数据：2025 年 gross revenue 约 194 亿美元，同比增长 17%，净利润率 10.6%。员工 8000-10000 人。支付总量 1.4 万亿美元。最新估值 1590 亿。

答案是：Stripe 用 AI 扩产出，不是缩编制。每周 1300 个 AI PR、人均 3.5 PR/天，对应的不是"少雇人做同样的事"，而是"同样的人做更多的事"。AI 释放出来的工程产能被增长吃掉了。

工程师的工作内容变了——从写代码到写任务描述 + review AI PR + 维护 harness——但人还是需要的。真正被省掉的是人手敲键盘写实现的那段时间，不是人本身。

## Harness 最大的未解问题

所有成功案例摆在一起，一个没有被直面的问题浮出水面：**它们全都站在既有测试资产的肩膀上。**

Stripe 有 300 万测试，十年积累。buffa 有 Google protobuf conformance suite，现成的。C 编译器有 GCC torture test suite，现成的。OpenAI 那个 greenfield 项目让 Codex 自己写测试——Martin Fowler 直接批评"缺少对功能和行为的验证"。

真正的 greenfield + 无既有测试 + 高质量产出这个组合，目前没有人拿出过令人信服的实践。

这里面有一个结构性矛盾：

让 AI 同时写代码和测试——tautological test，测试只验证"代码做了什么"。

让人先写测试——那测试设计本身就是最耗脑力的工作，harness 省掉的只是"敲实现代码"这部分体力活。

让 AI 写测试、人 review 测试——可能是最实际的折中，但 review 测试的认知负担不比写测试低多少。

Anthropic 那篇文章里的 evaluator agent 是在尝试解决这个问题——用独立 agent 做验收。但作者自己承认，这个 evaluator 开箱即用时是个糟糕的 QA agent，它会发现问题然后说服自己"这不算大事"就放行。必须人类反复调校才能达到合理水平。

所以 greenfield 的真实成本结构是这样的：harness 叙事说的"人从写代码变成设计约束"，在 greenfield 场景下其实是"人从写代码变成设计测试 + 设计验收标准 + 校准 evaluator"。这部分工作的难度和工作量并没有被 AI 显著降低——因为它本质上是 spec 工作，是"定义什么是对的"，而不是"把对的东西实现出来"。

## 所以，to harness or not to harness？

Harness engineering 不是银弹。它是一套有效但有前提的方法论。

如果你的项目有高覆盖率的测试套件，有完善的 CI 基础设施，有清晰的架构约束——那 harness 能让你的团队产出翻倍甚至翻十倍。Stripe 就是最好的例子。

如果你是一个测试覆盖率 30%、没有 linter、架构约束全靠口头约定的 brownfield 项目——先把这些基础设施补上再谈 harness。harness 不会凭空产生约束，它只是让已有的约束能被 agent 消费。

如果你是一个 greenfield 项目——想清楚谁来定义"什么是对的"。这个问题 harness 不帮你回答。

harness engineering 的核心洞察是对的：模型是商品，harness 是护城河。但这个"护城河"的地...